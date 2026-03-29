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
class StackFlowStep(ControlFlowStep):
    direction: str  # "push" | "pop"
    operand: str
    stack_depth: int = 0  # depth AFTER this operation


@dataclass(frozen=True, slots=True)
class LabelFlowStep(ControlFlowStep):
    name: str  # label name without the trailing colon


@dataclass(frozen=True, slots=True)
class LocalDeclFlowStep(ControlFlowStep):
    name: str       # e.g. "AllocFlags"
    type_info: str   # e.g. "byte ptr [bp - 2]", "[bp - 8]", "DWORD"
    source: str      # full line text


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
    """Assembly-time conditional block (IFDEF/IFNDEF/IF without dot).

    branches: tuple of (kind, condition, body_steps) — first branch is the
              opening directive, subsequent ones are ELSEIF branches.
    else_steps: steps under the ELSE branch (empty if no ELSE).
    """
    kind: str          # "IFDEF", "IFNDEF", "IF", etc. — uppercased
    condition: str     # the symbol or expression after the directive
    body_steps: tuple[ControlFlowStep, ...]
    branches: tuple[tuple[str, str, tuple[ControlFlowStep, ...]], ...] = ()
    else_steps: tuple[ControlFlowStep, ...] = ()


@dataclass(frozen=True, slots=True)
class AlignFlowStep(ControlFlowStep):
    boundary: int  # e.g. 4, 8, 16


@dataclass(frozen=True, slots=True)
class RepeatStringFlowStep(ControlFlowStep):
    prefix: str
    instruction: str


@dataclass(frozen=True, slots=True)
class JumpFlowStep(ControlFlowStep):
    """An unconditional or conditional jump that didn't form a structured block."""
    target: str          # destination label
    condition: str | None  # None → unconditional jmp; string → e.g. "je", "jnz"
    source: str          # full original line text


@dataclass(frozen=True, slots=True)
class FunctionControlFlow:
    name: str
    signature: str
    container: str | None
    steps: tuple[ControlFlowStep, ...]
    kind: str = "proc"      # "proc" | "macro"
    segment: str | None = None  # e.g. ".code", "TEXT", None

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
class FileDecl:
    name: str
    detail: str = ""


@dataclass(frozen=True, slots=True)
class ControlFlowDiagram:
    source_location: str
    functions: tuple[FunctionControlFlow, ...]
    file_header: str | None = None
    structs: tuple[StructDefinition, ...] = ()
    entry_point: str | None = None
    includes: tuple[FileDecl, ...] = ()
    externals: tuple[FileDecl, ...] = ()
    publics: tuple[FileDecl, ...] = ()
    segments: tuple[FileDecl, ...] = ()
    constants: tuple[FileDecl, ...] = ()
    variables: tuple[FileDecl, ...] = ()
    typedefs: tuple[FileDecl, ...] = ()

