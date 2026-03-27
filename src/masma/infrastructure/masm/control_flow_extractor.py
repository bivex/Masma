"""Structured control-flow extraction for MASM procedures."""

from __future__ import annotations

import re

from masma.domain.control_flow import (
    ActionFlowStep,
    ControlFlowDiagram,
    IfFlowStep,
    FunctionControlFlow,
    RepeatWhileFlowStep,
    WhileFlowStep,
)
from masma.domain.model import SourceUnit
from masma.domain.ports import ControlFlowExtractor
from masma.infrastructure.masm.support import (
    ELSEIF_RE,
    ELSE_RE,
    ENDIF_RE,
    ENDW_RE,
    IF_RE,
    IGNORED_ACTION_DIRECTIVES,
    LABEL_RE,
    PROC_RE,
    REPEAT_RE,
    UNTIL_RE,
    WHILE_RE,
    compact_text,
    iter_source_lines,
    scan_procedure_blocks,
)

_COMPARE_RE = re.compile(r"^(?P<op>cmp|test)\s+(?P<lhs>[^,]+)\s*,\s*(?P<rhs>.+)$", re.IGNORECASE)
_COND_JUMP_RE = re.compile(r"^(?P<op>j(?:e|z|ne|nz|g|ge|l|le|a|ae|b|be|c|nc|na|nae|nb|nbe|ng|nge|nl|nle))\s+(?P<label>[A-Za-z_.$?@][\w.$?@]*)$", re.IGNORECASE)
_JMP_RE = re.compile(r"^jmp\s+(?P<label>[A-Za-z_.$?@][\w.$?@]*)$", re.IGNORECASE)

_CMP_PREDICATES = {
    "je": "==",
    "jz": "==",
    "jne": "!=",
    "jnz": "!=",
    "jg": ">",
    "jnle": ">",
    "jge": ">=",
    "jnl": ">=",
    "jl": "<",
    "jnge": "<",
    "jle": "<=",
    "jng": "<=",
    "ja": ">",
    "jnbe": ">",
    "jae": ">=",
    "jnb": ">=",
    "jnc": ">=",
    "jb": "<",
    "jnae": "<",
    "jc": "<",
    "jbe": "<=",
    "jna": "<=",
}
_INVERSE_OPERATORS = {"==": "!=", "!=": "==", ">": "<=", ">=": "<", "<": ">=", "<=": ">"}


class MasmControlFlowExtractor(ControlFlowExtractor):
    def extract(self, source_unit: SourceUnit) -> ControlFlowDiagram:
        lines = iter_source_lines(source_unit.content)
        procedures = scan_procedure_blocks(lines)
        functions = tuple(_extract_procedure(procedure) for procedure in procedures)
        return ControlFlowDiagram(
            source_location=source_unit.location,
            functions=functions,
        )


def _extract_procedure(procedure) -> FunctionControlFlow:
    label_positions = _build_label_positions(procedure.body_lines)
    steps, _ = _parse_sequence(
        procedure.body_lines,
        0,
        label_positions=label_positions,
        stop_tokens=frozenset(),
        end_index=len(procedure.body_lines),
    )
    return FunctionControlFlow(
        name=procedure.name,
        signature=procedure.signature,
        container=None,
        steps=steps,
    )


def _parse_sequence(
    lines,
    index: int,
    *,
    label_positions: dict[str, int],
    stop_tokens: frozenset[str],
    end_index: int,
):
    steps = []
    while index < end_index:
        line = lines[index]
        token = _line_token(line.text)
        if token in stop_tokens:
            break

        if not line.text or _should_skip(line.text):
            index += 1
            continue

        if IF_RE.match(line.text):
            step, index = _parse_if(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
            )
            steps.append(step)
            continue

        jump_loop = _parse_jump_loop(
            lines,
            index,
            label_positions=label_positions,
            stop_tokens=stop_tokens,
            end_index=end_index,
        )
        if jump_loop is not None:
            step, index = jump_loop
            steps.append(step)
            continue

        jump_if = _parse_jump_if(
            lines,
            index,
            label_positions=label_positions,
            stop_tokens=stop_tokens,
            end_index=end_index,
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
            )
            steps.append(step)
            continue

        if REPEAT_RE.match(line.text):
            step, index = _parse_repeat(
                lines,
                index,
                label_positions=label_positions,
                end_index=end_index,
            )
            steps.append(step)
            continue

        if PROC_RE.match(line.text):
            index += 1
            continue

        if token == "ENDP":
            break

        steps.append(ActionFlowStep(label=compact_text(line.text)))
        index += 1

    return tuple(steps), index


def _parse_if(lines, index: int, *, label_positions, end_index: int):
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


def _parse_while(lines, index: int, *, label_positions, end_index: int):
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
    )
    if index < len(lines) and ENDW_RE.match(lines[index].text):
        index += 1
    return WhileFlowStep(condition=condition, body_steps=body_steps), index


def _parse_repeat(lines, index: int, *, label_positions, end_index: int):
    index += 1
    body_steps, index = _parse_sequence(
        lines,
        index,
        label_positions=label_positions,
        stop_tokens=frozenset({"UNTIL"}),
        end_index=end_index,
    )
    condition = "until condition"
    if index < len(lines):
        match = UNTIL_RE.match(lines[index].text)
        if match is not None:
            suffix = match.group("condition").strip()
            keyword = match.group("kind").upper()
            condition = compact_text(f"{keyword} {suffix}".strip(), limit=100)
            index += 1
    return RepeatWhileFlowStep(condition=condition, body_steps=body_steps), index


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
    return ""


def _condition_text(text: str) -> str:
    return compact_text(text.strip() or "condition", limit=100)


def _should_skip(text: str) -> bool:
    lowered = text.lower()
    if lowered in IGNORED_ACTION_DIRECTIVES:
        return True
    if lowered.startswith("local "):
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


def _parse_jump_loop(lines, index: int, *, label_positions, stop_tokens, end_index: int):
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
    )


def _parse_top_tested_jump_loop(lines, index: int, *, label_name: str, label_positions, stop_tokens, end_index: int):
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


def _parse_bottom_tested_jump_loop(lines, index: int, *, label_name: str, label_positions, stop_tokens, end_index: int):
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

        search_index += 1

    return None


def _parse_jump_if(lines, index: int, *, label_positions, stop_tokens, end_index: int):
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
            )
            else_steps, _ = _parse_sequence(
                lines,
                false_index + 1,
                label_positions=label_positions,
                stop_tokens=frozenset(),
                end_index=end_label_index,
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
        base = f"{lhs} & {rhs} {'==' if jump_op in {'je', 'jz'} else '!='} 0"
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
