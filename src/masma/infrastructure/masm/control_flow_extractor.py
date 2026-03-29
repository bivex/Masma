"""Structured control-flow extraction for MASM procedures."""

from __future__ import annotations

import re

from masma.domain.control_flow import (
    ActionFlowStep,
    AlignFlowStep,
    CallFlowStep,
    DataDeclFlowStep,
    ControlFlowDiagram,
    FileDecl,
    ForInFlowStep,
    IfFlowStep,
    IfdefFlowStep,
    FunctionControlFlow,
    StackFlowStep,
    InvokeFlowStep,
    LabelFlowStep,
    JumpFlowStep,
    LocalDeclFlowStep,
    MacroCallFlowStep,
    RepeatStringFlowStep,
    RepeatWhileFlowStep,
    SwitchCaseFlow,
    SwitchFlowStep,
    WhileFlowStep,
)
from masma.domain.control_flow import FileDecl
from masma.domain.model import SourceUnit
from masma.domain.ports import ControlFlowExtractor
from masma.infrastructure.masm.support import (
    ALIGN_RE,
    COND_ASSEMBLE_RE,
    COND_ASSEMBLE_PARSE_RE,
    EQU_RE,
    EXTERN_RE,
    EXTERN_NAMES_RE,
    ELSE_BARE_RE,
    ELSEIF_BARE_RE,
    ELSEIF_RE,
    ELSE_RE,
    ENDIF_BARE_RE,
    ENDIF_RE,
    ENDW_RE,
    IF_RE,
    IGNORED_ACTION_DIRECTIVES,
    INCLUDE_RE,
    LABEL_RE,
    MACRO_RE,
    TYPEDEF_RE,
    PROC_RE,
    PUBLIC_RE,
    REPEAT_RE,
    SEGMENT_RE,
    UNTIL_RE,
    VARIABLE_RE,
    WHILE_RE,
    compact_text,
    extract_entry_point,
    extract_file_header,
    iter_source_lines,
    scan_label_as_proc_blocks,
    scan_macro_blocks,
    scan_procedure_blocks,
    scan_struct_blocks,
)

_COMPARE_RE = re.compile(r"^(?P<op>cmp|test)\s+(?P<lhs>[^,]+)\s*,\s*(?P<rhs>.+)$", re.IGNORECASE)
_COND_JUMP_RE = re.compile(
    r"^(?P<op>j(?:"
    r"e|z|ne|nz"           # equal / zero
    r"|g|ge|l|le"          # signed comparison
    r"|ng|nge|nl|nle"      # negated signed
    r"|a|ae|b|be"          # unsigned comparison
    r"|na|nae|nb|nbe"      # negated unsigned
    r"|c|nc"               # carry
    r"|o|no"               # overflow
    r"|s|ns"               # sign
    r"|p|pe|np|po"         # parity
    r"|cxz|ecxz|rcxz"     # count-register zero (no FLAGS used)
    r"))\s+(?P<label>[A-Za-z_.$?@][\w.$?@]*)$",
    re.IGNORECASE,
)
# Used for structural loop/switch detection — symbolic labels only
_JMP_RE = re.compile(r"^jmp\s+(?P<label>[A-Za-z_.$?@][\w.$?@]*)$", re.IGNORECASE)
# Used for JumpFlowStep — any jmp form: label, register, memory indirect, far
_JMP_ANY_RE = re.compile(r"^jmp(?:f|s)?\s+(?P<target>.+)$", re.IGNORECASE)
_LOOP_INSTR_RE = re.compile(
    r"^(?P<op>loop(?:e|ne|z|nz)?)\s+(?P<label>[A-Za-z_.$?@][\w.$?@]*)$",
    re.IGNORECASE,
)
_MOV_ECX_RE = re.compile(r"^mov\s+(?P<reg>e?cx)\s*,\s*(?P<val>.+)$", re.IGNORECASE)
_INVOKE_RE = re.compile(
    r"^invoke\s+(?P<target>[A-Za-z_.$?@][\w.$?@]*)(?:\s*,\s*(?P<args>.+))?$",
    re.IGNORECASE,
)
_REP_INSTR_RE = re.compile(
    r"^(?P<prefix>rep(?:e|ne|z|nz)?)\s+(?P<instr>movs[bwdq]?|stos[bwdq]?|lods[bwdq]?|scas[bwdq]?|cmps[bwdq]?)$",
    re.IGNORECASE,
)
_CALL_RE = re.compile(
    r"^call\s+(?P<target>[A-Za-z_.$?@][\w.$?@]*)$",
    re.IGNORECASE,
)
_MACRO_CALL_RE = re.compile(
    r"^(?P<target>[A-Za-z_.$?@][\w.$?@]*)(?:\s+(?P<args>.+))?$",
    re.IGNORECASE,
)
_PUSH_RE = re.compile(r"^push(?:w|d|q)?\s+(?P<operand>.+)$", re.IGNORECASE)
_POP_RE = re.compile(r"^pop(?:w|d|q)?\s+(?P<operand>.+)$", re.IGNORECASE)
# Local variable declarations:
#   "AllocFlag equ byte ptr [bp - 2]"
#   "MemSize equ [bp - 8]"
#   "local dw ?"  (from ml.exe-generated prologues)
_LOCAL_DECL_RE = re.compile(
    r"^(?P<name>[A-Za-z_@$][A-Za-z0-9_@$?]*)\s+equ\s+(?P<typeinfo>.+)$",
    re.IGNORECASE,
)

_CMP_PREDICATES = {
    "je": "=",
    "jz": "=",
    "jne": "≠",
    "jnz": "≠",
    "jg": ">",
    "jnle": ">",
    "jge": "≥",
    "jnl": "≥",
    "jl": "<",
    "jnge": "<",
    "jle": "≤",
    "jng": "≤",
    "ja": ">",
    "jnbe": ">",
    "jae": "≥",
    "jnb": "≥",
    "jnc": "≥",
    "jb": "<",
    "jnae": "<",
    "jc": "<",
    "jbe": "≤",
    "jna": "≤",
}
_INVERSE_OPERATORS = {"=": "≠", "≠": "=", ">": "≤", "≥": "<", "<": "≥", "≤": ">"}


def _scan_macro_names(lines) -> frozenset[str]:
    """Return the set of macro names (uppercased) defined anywhere in the source."""
    names: set[str] = set()
    for line in lines:
        m = MACRO_RE.match(line.text)
        if m:
            names.add(m.group("name").upper())
    return frozenset(names)


class MasmControlFlowExtractor(ControlFlowExtractor):
    def extract(self, source_unit: SourceUnit) -> ControlFlowDiagram:
        lines = iter_source_lines(source_unit.content)
        procedures = scan_procedure_blocks(lines)
        if not procedures:
            procedures = scan_label_as_proc_blocks(lines)
        macro_blocks = scan_macro_blocks(lines)
        macro_names = _scan_macro_names(lines)

        # Collect top-level declarations info
        includes: list[FileDecl] = []
        externals: list[FileDecl] = []
        publics: list[FileDecl] = []
        segments: list[FileDecl] = []
        constants: list[FileDecl] = []
        variables: list[FileDecl] = []
        typedefs: list[FileDecl] = []

        for line in lines:
            if m := INCLUDE_RE.match(line.text):
                includes.append(FileDecl(name=m.group("target").strip(), detail=line.text.strip()))
            elif m := TYPEDEF_RE.match(line.text):
                typedefs.append(FileDecl(name=m.group("name").strip(), detail=line.text.strip()))
            elif m := EXTERN_RE.match(line.text):
                # EXTERN/EXTERNDEF can have comma-separated entries; EXTERN_RE only captures the first name
                raw = line.text.strip()
                names_m = EXTERN_NAMES_RE.match(raw)
                if names_m:
                    for entry in (e.strip() for e in names_m.group("names").split(",")):
                        name = entry.split(":")[0].strip()
                        if name:
                            externals.append(FileDecl(name=name, detail=raw))
                else:
                    externals.append(FileDecl(name=m.group("name").strip(), detail=raw))
            elif m := PUBLIC_RE.match(line.text):
                for name in (n.strip() for n in m.group("names").split(",")):
                    if name:
                        publics.append(FileDecl(name=name, detail=line.text.strip()))
            elif m := EQU_RE.match(line.text):
                constants.append(FileDecl(name=m.group("name").strip(), detail=line.text.strip()))
            elif m := VARIABLE_RE.match(line.text):
                variables.append(FileDecl(name=m.group("name").strip(), detail=line.text.strip()))

            seg_match = SEGMENT_RE.match(line.text)
            if seg_match:
                if seg_match.group("name"):
                    segments.append(FileDecl(name=seg_match.group("name"), detail=line.text.strip()))
                elif seg_match.group("directive"):
                    segments.append(FileDecl(name=seg_match.group("directive"), detail=line.text.strip()))

        proc_flows = tuple(
            _extract_procedure(procedure, macro_names=macro_names)
            for procedure in procedures
        )
        macro_flows = tuple(
            _extract_macro(macro, macro_names=macro_names)
            for macro in macro_blocks
        )
        # procs first, then macros — keeps "code" before "helpers"
        functions = proc_flows + macro_flows
        return ControlFlowDiagram(
            source_location=source_unit.location,
            functions=functions,
            file_header=extract_file_header(lines),
            structs=scan_struct_blocks(lines),
            entry_point=extract_entry_point(lines),
            includes=_dedup_decls(includes),
            externals=_dedup_decls(externals),
            publics=_dedup_decls(publics),
            segments=_dedup_decls(segments),
            constants=_dedup_decls(constants),
            variables=_dedup_decls(variables),
            typedefs=_dedup_decls(typedefs),
        )


def _dedup_decls(decls: list[FileDecl]) -> tuple[FileDecl, ...]:
    """Deduplicate by name, keep first occurrence's detail, sort by name."""
    seen: dict[str, FileDecl] = {}
    for d in decls:
        if d.name not in seen:
            seen[d.name] = d
    return tuple(sorted(seen.values(), key=lambda d: d.name))


def _extract_procedure(procedure, *, macro_names: frozenset[str] = frozenset()) -> FunctionControlFlow:
    label_positions = _build_label_positions(procedure.body_lines)
    steps, _ = _parse_sequence(
        procedure.body_lines,
        0,
        label_positions=label_positions,
        stop_tokens=frozenset(),
        end_index=len(procedure.body_lines),
        macro_names=macro_names,
    )
    return FunctionControlFlow(
        name=procedure.name,
        signature=procedure.signature,
        container=None,
        steps=steps,
        kind="proc",
        segment=procedure.segment,
    )


def _extract_macro(macro, *, macro_names: frozenset[str] = frozenset()) -> FunctionControlFlow:
    label_positions = _build_label_positions(macro.body_lines)
    steps, _ = _parse_sequence(
        macro.body_lines,
        0,
        label_positions=label_positions,
        stop_tokens=frozenset(),
        end_index=len(macro.body_lines),
        macro_names=macro_names,
    )
    return FunctionControlFlow(
        name=macro.name,
        signature=macro.signature,
        container=None,
        steps=steps,
        kind="macro",
        segment=macro.segment,
    )


def _parse_sequence(
    lines,
    index: int,
    *,
    label_positions: dict[str, int],
    stop_tokens: frozenset[str],
    end_index: int,
    macro_names: frozenset[str] = frozenset(),
    _stack_depth: int = 0,
):
    steps = []
    stack_depth = _stack_depth
    while index < end_index:
        line = lines[index]
        token = _line_token(line.text)
        if token in stop_tokens:
            break

        if not line.text or _should_skip(line.text):
            index += 1
            continue

        if COND_ASSEMBLE_RE.match(line.text):
            step, index = _parse_cond_assemble_block(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
                macro_names=macro_names,
            )
            steps.append(step)
            continue

        if IF_RE.match(line.text):
            step, index = _parse_if(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
                macro_names=macro_names,
            )
            steps.append(step)
            continue

        jump_loop = _parse_jump_loop(
            lines,
            index,
            label_positions=label_positions,
            stop_tokens=stop_tokens,
            end_index=end_index,
            macro_names=macro_names,
        )
        if jump_loop is not None:
            step, index = jump_loop
            # When a ForInFlowStep was recovered via the loop instruction, the
            # immediately preceding ActionFlowStep that held "mov ecx, N" has
            # been absorbed into the header.  Remove it from steps so it is not
            # emitted twice.
            if (
                isinstance(step, ForInFlowStep)
                and steps
                and isinstance(steps[-1], ActionFlowStep)
                and _MOV_ECX_RE.match(steps[-1].label)
            ):
                steps.pop()
            steps.append(step)
            continue

        switch_result = _parse_switch(
            lines, index,
            label_positions=label_positions,
            stop_tokens=stop_tokens,
            end_index=end_index,
            macro_names=macro_names,
        )
        if switch_result is not None:
            step, index = switch_result
            steps.append(step)
            continue

        jump_if = _parse_jump_if(
            lines,
            index,
            label_positions=label_positions,
            stop_tokens=stop_tokens,
            end_index=end_index,
            macro_names=macro_names,
        )
        if jump_if is not None:
            step, index = jump_if
            steps.append(step)
            continue

        if WHILE_RE.match(line.text):
            step, index = _parse_while(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
                macro_names=macro_names,
            )
            steps.append(step)
            continue

        if REPEAT_RE.match(line.text):
            step, index = _parse_repeat(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
                macro_names=macro_names,
            )
            steps.append(step)
            continue

        if PROC_RE.match(line.text):
            index += 1
            continue

        if token == "ENDP":
            break

        invoke_match = _INVOKE_RE.match(line.text)
        if invoke_match is not None:
            target = invoke_match.group("target")
            raw_args = invoke_match.group("args") or ""
            args = tuple(compact_text(a.strip(), limit=40) for a in raw_args.split(",") if a.strip())
            steps.append(InvokeFlowStep(target=target, args=args))
            index += 1
            continue

        rep_match = _REP_INSTR_RE.match(line.text)
        if rep_match is not None:
            rep_step = RepeatStringFlowStep(
                prefix=rep_match.group("prefix").upper(),
                instruction=rep_match.group("instr").lower(),
            )
            if (
                steps
                and isinstance(steps[-1], ActionFlowStep)
                and _MOV_ECX_RE.match(steps[-1].label)
            ):
                steps.pop()
            steps.append(rep_step)
            index += 1
            continue

        call_match = _CALL_RE.match(line.text)
        if call_match is not None:
            steps.append(CallFlowStep(target=call_match.group("target")))
            index += 1
            continue

        if macro_names:
            macro_match = _MACRO_CALL_RE.match(line.text)
            if macro_match is not None and macro_match.group("target").upper() in macro_names:
                target = macro_match.group("target")
                raw_args = macro_match.group("args") or ""
                args = tuple(compact_text(a.strip(), limit=40) for a in raw_args.split(",") if a.strip())
                steps.append(MacroCallFlowStep(target=target, args=args))
                index += 1
                continue

        align_match = ALIGN_RE.match(line.text)
        if align_match is not None:
            steps.append(AlignFlowStep(boundary=int(align_match.group("boundary"))))
            index += 1
            continue

        label_match = LABEL_RE.match(line.text)
        if label_match is not None:
            steps.append(LabelFlowStep(name=label_match.group("name")))
            rest = (label_match.group("rest") or "").strip()
            if rest:
                # Inline instruction after label — parse it as a pseudo-line
                from masma.infrastructure.masm.support import SourceLine
                pseudo = SourceLine(number=line.number, raw=line.raw, text=rest)
                sub_steps, _ = _parse_sequence(
                    (pseudo,), 0,
                    label_positions=label_positions,
                    stop_tokens=stop_tokens,
                    end_index=1,
                    macro_names=macro_names,
                )
                steps.extend(sub_steps)
            index += 1
            continue

        # Push / Pop — stack operations
        push_m = _PUSH_RE.match(line.text)
        if push_m is not None:
            stack_depth += 1
            steps.append(StackFlowStep(
                direction="push",
                operand=push_m.group("operand").strip(),
                stack_depth=stack_depth,
            ))
            index += 1
            continue

        pop_m = _POP_RE.match(line.text)
        if pop_m is not None:
            stack_depth = max(0, stack_depth - 1)
            steps.append(StackFlowStep(
                direction="pop",
                operand=pop_m.group("operand").strip(),
                stack_depth=stack_depth,
            ))
            index += 1
            continue

        # Local variable declarations: "AllocFlag equ byte ptr [bp - 2]", "MemSize equ [bp - 8]"
        local_m = _LOCAL_DECL_RE.match(line.text)
        if local_m is not None:
            typeinfo = local_m.group("typeinfo").strip()
            lowered_ti = typeinfo.lower()
            if "[bp" in lowered_ti or "ptr" in lowered_ti:
                # Stack-frame alias
                steps.append(LocalDeclFlowStep(
                    name=local_m.group("name"),
                    type_info=typeinfo,
                    source=compact_text(line.text),
                ))
                index += 1
                continue
            else:
                # Inline constant/data declaration (label-as-proc style)
                steps.append(DataDeclFlowStep(
                    name=local_m.group("name"),
                    type_info=typeinfo,
                    source=compact_text(line.text),
                ))
                index += 1
                continue

        # Inline data declarations: "vulkan_instance dq 0", "buf db 16 dup(0)"
        var_m = VARIABLE_RE.match(line.text)
        if var_m is not None:
            steps.append(DataDeclFlowStep(
                name=var_m.group("name"),
                type_info=compact_text(f"{var_m.group('type')}{var_m.group('tail')}"),
                source=compact_text(line.text),
            ))
            index += 1
            continue

        # Unstructured jumps — didn't form if/while/switch above
        jmp_m = _JMP_ANY_RE.match(line.text)
        if jmp_m is not None:
            steps.append(JumpFlowStep(
                target=jmp_m.group("target").strip(),
                condition=None,
                source=compact_text(line.text),
            ))
            index += 1
            continue

        cj_m = _COND_JUMP_RE.match(line.text)
        if cj_m is not None:
            steps.append(JumpFlowStep(
                target=cj_m.group("label"),
                condition=cj_m.group("op").lower(),
                source=compact_text(line.text),
            ))
            index += 1
            continue

        steps.append(ActionFlowStep(label=compact_text(line.text)))
        index += 1

    return tuple(steps), index


def _parse_if(lines, index: int, *, label_positions, end_index: int, macro_names: frozenset[str] = frozenset()):
    branches: list[tuple[str, tuple]] = []
    else_steps = ()

    match = IF_RE.match(lines[index].text)
    assert match is not None
    condition = _condition_text(match.group("condition"))
    index += 1
    then_steps, index = _parse_sequence(
        lines,
        index,
        label_positions=label_positions,
        stop_tokens=frozenset({"ELSEIF", "ELSE", "ENDIF"}),
        end_index=end_index,
        macro_names=macro_names,
    )
    branches.append((condition, then_steps))

    while index < len(lines):
        line = lines[index]
        elseif_match = ELSEIF_RE.match(line.text)
        if elseif_match is not None:
            index += 1
            branch_steps, index = _parse_sequence(
                lines,
                index,
                label_positions=label_positions,
                stop_tokens=frozenset({"ELSEIF", "ELSE", "ENDIF"}),
                end_index=end_index,
                macro_names=macro_names,
            )
            branches.append((_condition_text(elseif_match.group("condition")), branch_steps))
            continue

        if ELSE_RE.match(line.text):
            index += 1
            else_steps, index = _parse_sequence(
                lines,
                index,
                label_positions=label_positions,
                stop_tokens=frozenset({"ENDIF"}),
                end_index=end_index,
                macro_names=macro_names,
            )
        break

    if index < len(lines) and ENDIF_RE.match(lines[index].text):
        index += 1

    step = IfFlowStep(
        condition=branches[-1][0],
        then_steps=branches[-1][1],
        else_steps=else_steps,
    )
    for condition, branch_steps in reversed(branches[:-1]):
        step = IfFlowStep(
            condition=condition,
            then_steps=branch_steps,
            else_steps=(step,),
        )
    return step, index


def _parse_while(lines, index: int, *, label_positions, end_index: int, macro_names: frozenset[str] = frozenset()):
    match = WHILE_RE.match(lines[index].text)
    assert match is not None
    condition = _condition_text(match.group("condition"))
    index += 1
    body_steps, index = _parse_sequence(
        lines,
        index,
        label_positions=label_positions,
        stop_tokens=frozenset({"ENDW"}),
        end_index=end_index,
        macro_names=macro_names,
    )
    if index < len(lines) and ENDW_RE.match(lines[index].text):
        index += 1
    return WhileFlowStep(condition=condition, body_steps=body_steps), index


def _parse_repeat(lines, index: int, *, label_positions, end_index: int, macro_names: frozenset[str] = frozenset()):
    index += 1
    body_steps, index = _parse_sequence(
        lines,
        index,
        label_positions=label_positions,
        stop_tokens=frozenset({"UNTIL"}),
        end_index=end_index,
        macro_names=macro_names,
    )
    condition = "until condition"
    if index < len(lines):
        match = UNTIL_RE.match(lines[index].text)
        if match is not None:
            suffix = match.group("condition").strip()
            keyword = match.group("kind").upper()
            condition = _prettify_condition(compact_text(f"{keyword} {suffix}".strip(), limit=100))
            index += 1
    return RepeatWhileFlowStep(condition=condition, body_steps=body_steps), index


def _parse_cond_assemble_block(
    lines,
    index: int,
    *,
    label_positions: dict[str, int],
    end_index: int,
    macro_names: frozenset[str] = frozenset(),
) -> tuple["IfdefFlowStep", int]:
    """Parse an assembly-time IFDEF/IFNDEF/IF ... [ELSEIF ...] [ELSE] ENDIF block.

    Returns (IfdefFlowStep, next_index).
    """
    m = COND_ASSEMBLE_PARSE_RE.match(lines[index].text)
    assert m is not None
    kind = m.group("kind").upper()
    condition = m.group("condition").strip()
    index += 1

    # Collect branches: list of (kind, condition, steps)
    branches: list[tuple[str, str, tuple]] = []
    else_steps: tuple = ()

    # First branch body
    body_steps, index = _parse_sequence(
        lines,
        index,
        label_positions=label_positions,
        stop_tokens=frozenset({"ENDIF_BARE", "ELSE_BARE", "ELSEIF_BARE"}),
        end_index=end_index,
        macro_names=macro_names,
    )
    branches.append((kind, condition, tuple(body_steps)))

    # Consume ELSEIF / ELSE / ENDIF
    while index < end_index:
        line = lines[index]
        if ELSEIF_BARE_RE.match(line.text):
            elif_m = ELSEIF_BARE_RE.match(line.text)
            elif_cond = elif_m.group(1).strip()
            index += 1
            branch_steps, index = _parse_sequence(
                lines,
                index,
                label_positions=label_positions,
                stop_tokens=frozenset({"ENDIF_BARE", "ELSE_BARE", "ELSEIF_BARE"}),
                end_index=end_index,
                macro_names=macro_names,
            )
            branches.append(("ELSEIF", elif_cond, tuple(branch_steps)))
            continue

        if ELSE_BARE_RE.match(line.text):
            index += 1
            else_body, index = _parse_sequence(
                lines,
                index,
                label_positions=label_positions,
                stop_tokens=frozenset({"ENDIF_BARE"}),
                end_index=end_index,
                macro_names=macro_names,
            )
            else_steps = tuple(else_body)
            continue

        if ENDIF_BARE_RE.match(line.text):
            index += 1
            break

        # Shouldn't happen — but stop if unknown token
        break

    # Flatten: primary branch stored in body_steps (backward compat),
    # additional ELSEIF branches and ELSE in new fields.
    primary = branches[0]
    rest = branches[1:] if len(branches) > 1 else ()

    return IfdefFlowStep(
        kind=primary[0],
        condition=primary[1],
        body_steps=primary[2],
        branches=tuple(rest),
        else_steps=else_steps,
    ), index


def _line_token(text: str) -> str:
    upper = text.upper()
    if upper.startswith(".ELSEIF"):
        return "ELSEIF"
    if upper == ".ELSE":
        return "ELSE"
    if upper == ".ENDIF":
        return "ENDIF"
    if upper == ".ENDW":
        return "ENDW"
    if upper.startswith(".UNTIL"):
        return "UNTIL"
    if upper.endswith(" ENDP"):
        return "ENDP"
    if ENDIF_BARE_RE.match(text):
        return "ENDIF_BARE"
    if ELSE_BARE_RE.match(text):
        return "ELSE_BARE"
    if ELSEIF_BARE_RE.match(text):
        return "ELSEIF_BARE"
    return ""


_COND_UNICODE = [
    (" != ", " ≠ "),
    (" == ", " = "),
    (" >= ", " ≥ "),
    (" <= ", " ≤ "),
]


def _prettify_condition(text: str) -> str:
    for ascii_op, unicode_op in _COND_UNICODE:
        text = text.replace(ascii_op, unicode_op)
    return text


def _condition_text(text: str) -> str:
    return _prettify_condition(compact_text(text.strip() or "condition", limit=100))


def _should_skip(text: str) -> bool:
    lowered = text.lower()
    if lowered in IGNORED_ACTION_DIRECTIVES:
        return True
    if lowered.startswith("local "):
        return True
    # NASM-style section directives inside flat-style MASM (label-as-proc)
    if lowered.startswith("section "):
        return True
    return False


def _build_label_positions(lines) -> dict[str, int]:
    positions: dict[str, int] = {}
    for index, line in enumerate(lines):
        match = LABEL_RE.match(line.text)
        if match is None:
            continue
        positions.setdefault(match.group("name").lower(), index)
    return positions


def _parse_jump_loop(lines, index: int, *, label_positions, stop_tokens, end_index: int, macro_names: frozenset[str] = frozenset()):
    label_match = LABEL_RE.match(lines[index].text)
    if label_match is None:
        return None

    label_name = label_match.group("name")
    top_tested = _parse_top_tested_jump_loop(
        lines,
        index,
        label_name=label_name,
        label_positions=label_positions,
        stop_tokens=stop_tokens,
        end_index=end_index,
        macro_names=macro_names,
    )
    if top_tested is not None:
        return top_tested

    return _parse_bottom_tested_jump_loop(
        lines,
        index,
        label_name=label_name,
        label_positions=label_positions,
        stop_tokens=stop_tokens,
        end_index=end_index,
        macro_names=macro_names,
    )


def _parse_top_tested_jump_loop(lines, index: int, *, label_name: str, label_positions, stop_tokens, end_index: int, macro_names: frozenset[str] = frozenset()):
    compare_index, jump_index = _find_compare_and_jump(lines, index + 1, end_index, stop_tokens)
    if jump_index is None:
        return None

    jump_info = _parse_conditional_jump(lines[jump_index].text)
    if jump_info is None:
        return None

    _, exit_label = jump_info
    exit_index = label_positions.get(exit_label.lower())
    if exit_index is None or exit_index <= jump_index or exit_index >= end_index:
        return None

    back_jump_index = _find_unconditional_jump_to_label(
        lines,
        jump_index + 1,
        exit_index,
        label_name,
    )
    if back_jump_index is None:
        return None

    body_steps, _ = _parse_sequence(
        lines,
        jump_index + 1,
        label_positions=label_positions,
        stop_tokens=frozenset(),
        end_index=back_jump_index,
        macro_names=macro_names,
    )
    if not body_steps:
        return None

    return (
        WhileFlowStep(
            condition=_infer_jump_condition(
                compare_line=lines[compare_index].text if compare_index is not None else None,
                jump_line=lines[jump_index].text,
                invert=True,
            ),
            body_steps=body_steps,
        ),
        exit_index + 1,
    )


def _parse_bottom_tested_jump_loop(lines, index: int, *, label_name: str, label_positions, stop_tokens, end_index: int, macro_names: frozenset[str] = frozenset()):
    search_index = index + 1
    while search_index < end_index:
        token = _line_token(lines[search_index].text)
        if token in stop_tokens:
            return None

        jump_info = _parse_conditional_jump(lines[search_index].text)
        if jump_info is not None and jump_info[1].lower() == label_name.lower():
            compare_index = _previous_compare_index(lines, search_index, lower_bound=index + 1)
            body_end = compare_index if compare_index is not None else search_index
            body_steps, _ = _parse_sequence(
                lines,
                index + 1,
                label_positions=label_positions,
                stop_tokens=frozenset(),
                end_index=body_end,
                macro_names=macro_names,
            )
            if not body_steps:
                return None
            return (
                RepeatWhileFlowStep(
                    condition=_infer_jump_condition(
                        compare_line=lines[compare_index].text if compare_index is not None else None,
                        jump_line=lines[search_index].text,
                        invert=False,
                    ),
                    body_steps=body_steps,
                ),
                search_index + 1,
            )

        loop_match = _LOOP_INSTR_RE.match(lines[search_index].text)
        if loop_match is not None and loop_match.group("label").lower() == label_name.lower():
            body_steps, _ = _parse_sequence(
                lines, index + 1,
                label_positions=label_positions,
                stop_tokens=frozenset(),
                end_index=search_index,
                macro_names=macro_names,
            )
            if not body_steps:
                return None
            return (
                ForInFlowStep(
                    header=_infer_loop_counter_header(lines, index),
                    body_steps=body_steps,
                ),
                search_index + 1,
            )

        search_index += 1

    return None


def _parse_jump_if(lines, index: int, *, label_positions, stop_tokens, end_index: int, macro_names: frozenset[str] = frozenset()):
    compare_index, jump_index = _find_compare_and_jump(lines, index, end_index, stop_tokens)
    if jump_index is None or jump_index != index and compare_index != index:
        return None

    jump_info = _parse_conditional_jump(lines[jump_index].text)
    if jump_info is None:
        return None

    _, false_label = jump_info
    false_index = label_positions.get(false_label.lower())
    if false_index is None or false_index <= jump_index or false_index >= end_index:
        return None

    end_jump = _find_first_unconditional_jump(lines, jump_index + 1, false_index)
    if end_jump is not None:
        end_jump_index, end_label = end_jump
        end_label_index = label_positions.get(end_label.lower())
        if end_label_index is not None and false_index < end_label_index < end_index:
            then_steps, _ = _parse_sequence(
                lines,
                jump_index + 1,
                label_positions=label_positions,
                stop_tokens=frozenset(),
                end_index=end_jump_index,
                macro_names=macro_names,
            )
            else_steps, _ = _parse_sequence(
                lines,
                false_index + 1,
                label_positions=label_positions,
                stop_tokens=frozenset(),
                end_index=end_label_index,
                macro_names=macro_names,
            )
            if then_steps or else_steps:
                return (
                    IfFlowStep(
                        condition=_infer_jump_condition(
                            compare_line=lines[compare_index].text if compare_index is not None else None,
                            jump_line=lines[jump_index].text,
                            invert=True,
                        ),
                        then_steps=then_steps,
                        else_steps=else_steps,
                    ),
                    end_label_index + 1,
                )

    then_steps, _ = _parse_sequence(
        lines,
        jump_index + 1,
        label_positions=label_positions,
        stop_tokens=frozenset(),
        end_index=false_index,
        macro_names=macro_names,
    )
    if not then_steps:
        return None

    return (
        IfFlowStep(
            condition=_infer_jump_condition(
                compare_line=lines[compare_index].text if compare_index is not None else None,
                jump_line=lines[jump_index].text,
                invert=True,
            ),
            then_steps=then_steps,
            else_steps=(),
        ),
        false_index + 1,
    )


def _find_compare_and_jump(lines, index: int, end_index: int, stop_tokens: frozenset[str]):
    current = _next_meaningful_index(lines, index, end_index, stop_tokens)
    if current is None:
        return None, None

    if _is_compare_line(lines[current].text):
        jump_index = _next_meaningful_index(lines, current + 1, end_index, stop_tokens)
        if jump_index is not None and _parse_conditional_jump(lines[jump_index].text) is not None:
            return current, jump_index
        return None, None

    if _parse_conditional_jump(lines[current].text) is not None:
        return None, current

    return None, None


def _next_meaningful_index(lines, index: int, end_index: int, stop_tokens: frozenset[str]):
    current = index
    while current < end_index:
        token = _line_token(lines[current].text)
        if token in stop_tokens:
            return None
        if lines[current].text and not _should_skip(lines[current].text):
            return current
        current += 1
    return None


def _previous_compare_index(lines, index: int, *, lower_bound: int):
    current = index - 1
    while current >= lower_bound:
        text = lines[current].text
        if not text or _should_skip(text):
            current -= 1
            continue
        if _is_compare_line(text):
            return current
        if LABEL_RE.match(text) or _parse_conditional_jump(text) or _parse_unconditional_jump(text):
            return None
        current -= 1
    return None


def _find_unconditional_jump_to_label(lines, start: int, end_index: int, label_name: str):
    for current in range(start, end_index):
        jump_info = _parse_unconditional_jump(lines[current].text)
        if jump_info is not None and jump_info.lower() == label_name.lower():
            return current
    return None


def _find_first_unconditional_jump(lines, start: int, end_index: int):
    for current in range(start, end_index):
        jump_info = _parse_unconditional_jump(lines[current].text)
        if jump_info is not None:
            return current, jump_info
    return None


def _is_compare_line(text: str) -> bool:
    return _COMPARE_RE.match(text) is not None


def _parse_conditional_jump(text: str):
    match = _COND_JUMP_RE.match(text)
    if match is None:
        return None
    return match.group("op").lower(), match.group("label")


def _parse_unconditional_jump(text: str):
    match = _JMP_RE.match(text)
    if match is None:
        return None
    return match.group("label")


def _infer_jump_condition(*, compare_line: str | None, jump_line: str, invert: bool) -> str:
    jump_info = _parse_conditional_jump(jump_line)
    if jump_info is None:
        return compact_text(jump_line)

    jump_op, jump_label = jump_info
    if compare_line is None:
        base = compact_text(f"{jump_op} {jump_label}", limit=100)
        return compact_text(f"not ({base})" if invert else base, limit=100)

    compare_match = _COMPARE_RE.match(compare_line)
    if compare_match is None:
        return compact_text(compare_line, limit=100)

    compare_op = compare_match.group("op").lower()
    lhs = compact_text(compare_match.group("lhs").strip(), limit=40)
    rhs = compact_text(compare_match.group("rhs").strip(), limit=40)

    if compare_op == "test":
        base = f"{lhs} & {rhs} {'=' if jump_op in {'je', 'jz'} else '≠'} 0"
    else:
        operator = _CMP_PREDICATES.get(jump_op)
        if operator is None:
            base = f"{lhs} ? {rhs}"
        else:
            base = f"{lhs} {operator} {rhs}"

    if invert:
        base = _invert_condition_text(base)
    return compact_text(base, limit=100)


def _invert_condition_text(condition: str) -> str:
    for operator, inverse in _INVERSE_OPERATORS.items():
        surrounded = f" {operator} "
        if surrounded in condition:
            lhs, rhs = condition.split(surrounded, 1)
            return f"{lhs}{' '}{inverse}{' '}{rhs}"
    return f"not ({condition})"


def _parse_switch(lines, index: int, *, label_positions, stop_tokens, end_index: int, macro_names: frozenset[str] = frozenset()):
    """Detect a cmp/je chain switch pattern starting at index.

    Requires >= 2 consecutive (cmp reg, val / je label) pairs with the same
    register.  Returns (SwitchFlowStep, next_index) or None.
    """
    scan = index
    pairs: list[tuple[str, str, int]] = []  # (val, case_label, case_label_index)
    first_reg: str | None = None

    while scan < end_index:
        text = lines[scan].text
        if not text or _should_skip(text):
            scan += 1
            continue

        cmp_match = _COMPARE_RE.match(text)
        if cmp_match is None or cmp_match.group("op").lower() != "cmp":
            break

        reg = compact_text(cmp_match.group("lhs").strip(), limit=40)
        val = compact_text(cmp_match.group("rhs").strip(), limit=40)

        if first_reg is None:
            first_reg = reg
        elif reg.lower() != first_reg.lower():
            break

        # Must be followed by je or jz
        next_scan = scan + 1
        while next_scan < end_index and (not lines[next_scan].text or _should_skip(lines[next_scan].text)):
            next_scan += 1

        if next_scan >= end_index:
            break

        jump_info = _parse_conditional_jump(lines[next_scan].text)
        if jump_info is None:
            break
        jump_op, case_label = jump_info
        if jump_op.lower() not in ("je", "jz"):
            break

        case_label_index = label_positions.get(case_label.lower())
        if case_label_index is None or case_label_index <= next_scan:
            break

        pairs.append((val, case_label, case_label_index))
        scan = next_scan + 1

    if len(pairs) < 2 or first_reg is None:
        return None

    # Check for optional trailing jmp default_label
    default_label: str | None = None
    default_label_index: int | None = None
    trailing = scan
    while trailing < end_index and (not lines[trailing].text or _should_skip(lines[trailing].text)):
        trailing += 1
    if trailing < end_index:
        jmp_label = _parse_unconditional_jump(lines[trailing].text)
        if jmp_label is not None:
            jmp_index = label_positions.get(jmp_label.lower())
            if jmp_index is not None and jmp_index > trailing:
                default_label = jmp_label
                default_label_index = jmp_index
                scan = trailing + 1

    # Region containing all case bodies starts after the last je/jmp header
    region_start = scan

    # Find exit label — the common jmp target used at end of each case body
    case_count = len(pairs) + (1 if default_label is not None else 0)
    exit_label, exit_label_index = _find_switch_exit(
        lines, region_start, end_index, label_positions, case_count
    )
    if exit_label is None or exit_label_index is None:
        return None

    # Build sorted list of all case labels (val, label_str, label_index)
    all_cases: list[tuple[str, str, int]] = [(val, lbl, idx) for val, lbl, idx in pairs]
    if default_label is not None and default_label_index is not None:
        all_cases.append(("default", default_label, default_label_index))
    all_cases.sort(key=lambda t: t[2])

    # Parse each case body between its label and the next case/exit label
    case_boundaries = [idx for _, _, idx in all_cases] + [exit_label_index]

    cases: list[SwitchCaseFlow] = []
    for i, (val, _lbl, lbl_idx) in enumerate(all_cases):
        body_end = case_boundaries[i + 1]
        # Trim trailing jmp exit_label from body
        body_end_trimmed = body_end
        for scan_back in range(body_end - 1, lbl_idx, -1):
            text = lines[scan_back].text
            if not text or _should_skip(text):
                continue
            jmp = _parse_unconditional_jump(text)
            if jmp is not None and jmp.lower() == exit_label.lower():
                body_end_trimmed = scan_back
            break

        body_steps, _ = _parse_sequence(
            lines,
            lbl_idx + 1,
            label_positions=label_positions,
            stop_tokens=frozenset(),
            end_index=body_end_trimmed,
            macro_names=macro_names,
        )
        cases.append(SwitchCaseFlow(label=val, steps=body_steps))

    return (
        SwitchFlowStep(expression=first_reg, cases=tuple(cases)),
        exit_label_index + 1,
    )


def _find_switch_exit(lines, region_start: int, end_index: int, label_positions: dict[str, int], case_count: int):
    """Find the most common forward jmp target label in [region_start, end_index).

    Returns (label_str, label_index) or (None, None).
    """
    counts: dict[str, int] = {}
    for i in range(region_start, end_index):
        jmp = _parse_unconditional_jump(lines[i].text)
        if jmp is None:
            continue
        jmp_idx = label_positions.get(jmp.lower())
        if jmp_idx is not None and jmp_idx >= region_start:
            counts[jmp] = counts.get(jmp, 0) + 1

    if not counts:
        return None, None

    threshold = max(1, case_count - 1)
    best_label = max(counts, key=lambda l: counts[l])
    if counts[best_label] < threshold:
        return None, None

    best_index = label_positions.get(best_label.lower())
    if best_index is None:
        return None, None
    return best_label, best_index


def _infer_loop_counter_header(lines, label_index: int) -> str:
    """Search backwards up to 5 lines from label_index for mov ecx/cx, N."""
    for back in range(label_index - 1, max(-1, label_index - 6), -1):
        text = lines[back].text
        if not text:
            continue
        mov_match = _MOV_ECX_RE.match(text)
        if mov_match is not None:
            reg = mov_match.group("reg")
            val = compact_text(mov_match.group("val").strip(), limit=40)
            return f"{reg} = {val}"
    return "ecx"
