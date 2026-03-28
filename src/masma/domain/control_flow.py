"""Domain model for structured control flow diagrams."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ControlFlowStep:
    """Base type for a structured control flow step."""


@dataclass(frozen=True, slots=True)
class ActionFlowStep(ControlFlowStep):
    label: str


@dataclass(frozen=True, slots=True)
class LabelFlowStep(ControlFlowStep):
    name: str  # label name without the trailing colon


@dataclass(frozen=True, slots=True)
class IfFlowStep(ControlFlowStep):
    condition: str
    then_steps: tuple[ControlFlowStep, ...]
    else_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class GuardFlowStep(ControlFlowStep):
    condition: str
    else_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class WhileFlowStep(ControlFlowStep):
    condition: str
    body_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class ForInFlowStep(ControlFlowStep):
    header: str
    body_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class RepeatWhileFlowStep(ControlFlowStep):
    condition: str
    body_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class SwitchCaseFlow:
    label: str
    steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class SwitchFlowStep(ControlFlowStep):
    expression: str
    cases: tuple[SwitchCaseFlow, ...]


@dataclass(frozen=True, slots=True)
class CatchClauseFlow:
    pattern: str
    steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class DoCatchFlowStep(ControlFlowStep):
    body_steps: tuple[ControlFlowStep, ...]
    catches: tuple[CatchClauseFlow, ...]


@dataclass(frozen=True, slots=True)
class DeferFlowStep(ControlFlowStep):
    body_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class InvokeFlowStep(ControlFlowStep):
    target: str
    args: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CallFlowStep(ControlFlowStep):
    target: str


@dataclass(frozen=True, slots=True)
class MacroCallFlowStep(ControlFlowStep):
    target: str
    args: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class IfdefFlowStep(ControlFlowStep):
    """Assembly-time conditional block (IFDEF/IFNDEF/IF without dot)."""
    kind: str          # "IFDEF", "IFNDEF", "IF", etc. — uppercased
    condition: str     # the symbol or expression after the directive
    body_steps: tuple[ControlFlowStep, ...]


@dataclass(frozen=True, slots=True)
class RepeatStringFlowStep(ControlFlowStep):
    prefix: str
    instruction: str


@dataclass(frozen=True, slots=True)
class FunctionControlFlow:
    name: str
    signature: str
    container: str | None
    steps: tuple[ControlFlowStep, ...]
    kind: str = "proc"  # "proc" | "macro"

    @property
    def qualified_name(self) -> str:
        if self.container:
            return f"{self.container}.{self.name}"
        return self.name


@dataclass(frozen=True, slots=True)
class StructField:
    name: str
    type: str


@dataclass(frozen=True, slots=True)
class StructDefinition:
    name: str
    fields: tuple[StructField, ...]
    line: int


@dataclass(frozen=True, slots=True)
class ControlFlowDiagram:
    source_location: str
    functions: tuple[FunctionControlFlow, ...]
    file_header: str | None = None
    structs: tuple[StructDefinition, ...] = ()

