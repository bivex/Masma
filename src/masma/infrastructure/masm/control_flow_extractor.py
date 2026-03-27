"""Structured control-flow extraction for MASM procedures."""

from __future__ import annotations

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
    PROC_RE,
    REPEAT_RE,
    UNTIL_RE,
    WHILE_RE,
    compact_text,
    iter_source_lines,
    scan_procedure_blocks,
)


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
    steps, _ = _parse_sequence(procedure.body_lines, 0, stop_tokens=frozenset())
    return FunctionControlFlow(
        name=procedure.name,
        signature=procedure.signature,
        container=None,
        steps=steps,
    )


def _parse_sequence(lines, index: int, *, stop_tokens: frozenset[str]):
    steps = []
    while index < len(lines):
        line = lines[index]
        token = _line_token(line.text)
        if token in stop_tokens:
            break

        if not line.text or _should_skip(line.text):
            index += 1
            continue

        if IF_RE.match(line.text):
            step, index = _parse_if(lines, index)
            steps.append(step)
            continue

        if WHILE_RE.match(line.text):
            step, index = _parse_while(lines, index)
            steps.append(step)
            continue

        if REPEAT_RE.match(line.text):
            step, index = _parse_repeat(lines, index)
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


def _parse_if(lines, index: int):
    branches: list[tuple[str, tuple]] = []
    else_steps = ()

    match = IF_RE.match(lines[index].text)
    assert match is not None
    condition = _condition_text(match.group("condition"))
    index += 1
    then_steps, index = _parse_sequence(
        lines,
        index,
        stop_tokens=frozenset({"ELSEIF", "ELSE", "ENDIF"}),
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
                stop_tokens=frozenset({"ELSEIF", "ELSE", "ENDIF"}),
            )
            branches.append((_condition_text(elseif_match.group("condition")), branch_steps))
            continue

        if ELSE_RE.match(line.text):
            index += 1
            else_steps, index = _parse_sequence(
                lines,
                index,
                stop_tokens=frozenset({"ENDIF"}),
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


def _parse_while(lines, index: int):
    match = WHILE_RE.match(lines[index].text)
    assert match is not None
    condition = _condition_text(match.group("condition"))
    index += 1
    body_steps, index = _parse_sequence(lines, index, stop_tokens=frozenset({"ENDW"}))
    if index < len(lines) and ENDW_RE.match(lines[index].text):
        index += 1
    return WhileFlowStep(condition=condition, body_steps=body_steps), index


def _parse_repeat(lines, index: int):
    index += 1
    body_steps, index = _parse_sequence(lines, index, stop_tokens=frozenset({"UNTIL"}))
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
