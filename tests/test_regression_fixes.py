"""
Regression tests for bugs found during the dosstuff batch-verification run.

Three failure patterns were identified:
  1. File without trailing newline → ANTLR `mismatched input '<EOF>' expecting EOL`
  2. Named ENDM (``ENDM Bus``) → line scanner "MACRO 'Bus' is not closed"
  3. ``End`` directive at EOF without newline → same ANTLR EOF/EOL mismatch

Tests are written *before* the fixes so they fail first, then pass after.
"""

from __future__ import annotations

import pytest

from masma.domain.control_flow import (
    DataDeclFlowStep,
    JumpFlowStep,
    LocalDeclFlowStep,
)
from masma.domain.model import DiagnosticSeverity, SourceUnit, SourceUnitId
from masma.infrastructure.antlr.runtime import load_generated_types, parse_source_text
from masma.infrastructure.masm.control_flow_extractor import MasmControlFlowExtractor
from masma.infrastructure.masm.support import collect_syntax_diagnostics, iter_source_lines


# ---------------------------------------------------------------------------
# Pattern 1 & 3: file without trailing newline
# ---------------------------------------------------------------------------


def test_antlr_parser_accepts_file_without_trailing_newline() -> None:
    """A file that ends with a statement but no final newline must parse clean."""
    generated = load_generated_types()
    # Deliberately no trailing \n
    source = "Foo PROC\n  mov ax, 0\n  ret\nFoo ENDP"

    result = parse_source_text(source, generated)

    assert result.diagnostics == (), (
        f"Expected no ANTLR diagnostics, got: {result.diagnostics}"
    )


def test_antlr_parser_accepts_end_directive_at_eof_without_newline() -> None:
    """``End`` at the very end of a file (no trailing newline) must parse clean."""
    generated = load_generated_types()
    source = "Foo PROC\n  ret\nFoo ENDP\nEnd"

    result = parse_source_text(source, generated)

    assert result.diagnostics == (), (
        f"Expected no ANTLR diagnostics, got: {result.diagnostics}"
    )


def test_antlr_parser_accepts_end_with_label_at_eof_without_newline() -> None:
    """``End main`` at EOF without trailing newline."""
    generated = load_generated_types()
    source = "main PROC\n  ret\nmain ENDP\nEnd main"

    result = parse_source_text(source, generated)

    assert result.diagnostics == (), (
        f"Expected no ANTLR diagnostics, got: {result.diagnostics}"
    )


def test_antlr_parser_accepts_constant_declaration_without_trailing_newline() -> None:
    """An EQU/constant at the last line with no newline must parse clean."""
    generated = load_generated_types()
    source = ".code\nVALUE equ 1"

    result = parse_source_text(source, generated)

    assert result.diagnostics == (), (
        f"Expected no ANTLR diagnostics, got: {result.diagnostics}"
    )


# ---------------------------------------------------------------------------
# Pattern 2: named ENDM — ``ENDM MacroName``
# ---------------------------------------------------------------------------


def test_collect_syntax_diagnostics_accepts_named_endm() -> None:
    """``ENDM Bus`` must close the open MACRO 'Bus' without error."""
    source = "Bus MACRO Value\n  mov ax, Value\nENDM Bus\n"
    lines = iter_source_lines(source)

    diagnostics = collect_syntax_diagnostics(lines)

    assert diagnostics == (), (
        f"Expected no diagnostics for named ENDM, got: {diagnostics}"
    )


def test_collect_syntax_diagnostics_accepts_named_endm_nested() -> None:
    """Named ENDM at outer macro level still closes correct block."""
    source = (
        "Outer MACRO x\n"
        "  Inner MACRO y\n"
        "    mov bx, y\n"
        "  ENDM Inner\n"
        "  mov ax, x\n"
        "ENDM Outer\n"
    )
    lines = iter_source_lines(source)

    diagnostics = collect_syntax_diagnostics(lines)

    assert diagnostics == (), (
        f"Expected no diagnostics for nested named ENDM, got: {diagnostics}"
    )


def test_collect_syntax_diagnostics_still_errors_on_truly_unclosed_macro() -> None:
    """A macro that genuinely has no ENDM must still produce an error."""
    source = "Open MACRO x\n  mov ax, x\n"
    lines = iter_source_lines(source)

    diagnostics = collect_syntax_diagnostics(lines)

    assert len(diagnostics) == 1
    assert diagnostics[0].severity == DiagnosticSeverity.ERROR
    assert "Open" in diagnostics[0].message


def test_scan_macro_blocks_handles_named_endm() -> None:
    """scan_macro_blocks must recognize ``ENDM MacroName`` as the block closer."""
    from masma.infrastructure.masm.support import scan_macro_blocks

    source = "Bus MACRO Value\n  mov ax, Value\nENDM Bus\n"
    lines = iter_source_lines(source)

    macros = scan_macro_blocks(lines)

    assert len(macros) == 1
    assert macros[0].name == "Bus"


# ---------------------------------------------------------------------------
# New feature: JumpFlowStep
# ---------------------------------------------------------------------------


def test_control_flow_extractor_emits_jump_flow_step_for_unconditional_jmp() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("jmp-test"),
        location="jmp-test.asm",
        content="demo PROC\n  jmp exit_label\n  mov ax, 1\nexit_label:\n  ret\ndemo ENDP\n",
    )

    diagram = extractor.extract(source)

    steps = diagram.functions[0].steps
    jump_steps = [s for s in steps if isinstance(s, JumpFlowStep)]
    assert len(jump_steps) >= 1
    unconditional = [s for s in jump_steps if s.condition is None]
    assert len(unconditional) >= 1
    assert unconditional[0].target == "exit_label"


def test_control_flow_extractor_emits_jump_flow_step_for_conditional_jcc() -> None:
    extractor = MasmControlFlowExtractor()
    # jz to the immediately following label — empty then-body so it is NOT
    # absorbed into an IfFlowStep and falls through to a raw JumpFlowStep.
    source = SourceUnit(
        identifier=SourceUnitId("jcc-test"),
        location="jcc-test.asm",
        content="demo PROC\n  jz zero_target\nzero_target:\n  ret\ndemo ENDP\n",
    )

    diagram = extractor.extract(source)

    steps = diagram.functions[0].steps
    jump_steps = [s for s in steps if isinstance(s, JumpFlowStep)]
    assert len(jump_steps) >= 1
    conditional = [s for s in jump_steps if s.condition is not None]
    assert len(conditional) >= 1
    assert conditional[0].target == "zero_target"
    assert conditional[0].condition == "z"


@pytest.mark.parametrize("mnemonic,expected_cond", [
    ("jo",    "o"),
    ("jno",   "no"),
    ("js",    "s"),
    ("jns",   "ns"),
    ("jp",    "p"),
    ("jpe",   "pe"),
    ("jnp",   "np"),
    ("jpo",   "po"),
    ("jcxz",  "cxz"),
    ("jecxz", "ecxz"),
    ("jrcxz", "rcxz"),
])
def test_control_flow_extractor_recognises_extended_conditional_jumps(
    mnemonic: str, expected_cond: str
) -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId(f"{mnemonic}-test"),
        location=f"{mnemonic}-test.asm",
        content=f"demo PROC\n  {mnemonic} target\ntarget:\n  ret\ndemo ENDP\n",
    )

    diagram = extractor.extract(source)

    steps = diagram.functions[0].steps
    jump_steps = [s for s in steps if isinstance(s, JumpFlowStep)]
    assert len(jump_steps) >= 1
    assert jump_steps[0].condition == expected_cond


# ---------------------------------------------------------------------------
# New feature: LocalDeclFlowStep
# ---------------------------------------------------------------------------


def test_control_flow_extractor_emits_local_decl_flow_step_for_stack_equ() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("local-decl"),
        location="local-decl.asm",
        content=(
            "demo PROC\n"
            "  localVar equ [ebp-4]\n"
            "  mov eax, localVar\n"
            "  ret\n"
            "demo ENDP\n"
        ),
    )

    diagram = extractor.extract(source)

    steps = diagram.functions[0].steps
    local_steps = [s for s in steps if isinstance(s, LocalDeclFlowStep)]
    assert len(local_steps) == 1
    assert local_steps[0].name == "localVar"
    assert "[ebp-4]" in local_steps[0].type_info


# ---------------------------------------------------------------------------
# New feature: DataDeclFlowStep inside procedure body
# ---------------------------------------------------------------------------


def test_control_flow_extractor_emits_data_decl_flow_step_for_inline_db() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("data-decl"),
        location="data-decl.asm",
        content=(
            "demo PROC\n"
            "  msgBuf db 16 dup(0)\n"
            "  lea esi, msgBuf\n"
            "  ret\n"
            "demo ENDP\n"
        ),
    )

    diagram = extractor.extract(source)

    steps = diagram.functions[0].steps
    data_steps = [s for s in steps if isinstance(s, DataDeclFlowStep)]
    assert len(data_steps) == 1
    assert data_steps[0].name == "msgBuf"
    assert "db" in data_steps[0].type_info.lower()


# ---------------------------------------------------------------------------
# New feature: label-as-proc fallback (flat-style files)
# ---------------------------------------------------------------------------


def test_control_flow_extractor_uses_label_as_proc_fallback_for_flat_file() -> None:
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("flat"),
        location="flat.asm",
        content=(
            ".code\n"
            "MainEntry:\n"
            "  mov ax, 0\n"
            "  ret\n"
            "HelperFunc:\n"
            "  inc bx\n"
            "  ret\n"
        ),
    )

    diagram = extractor.extract(source)

    names = [fn.name for fn in diagram.functions]
    assert "MainEntry" in names
    assert "HelperFunc" in names


def test_control_flow_extractor_does_not_treat_jump_target_as_proc() -> None:
    """Labels that are jump targets must NOT become pseudo-procedures."""
    extractor = MasmControlFlowExtractor()
    source = SourceUnit(
        identifier=SourceUnitId("flat-jump"),
        location="flat-jump.asm",
        content=(
            ".code\n"
            "Entry:\n"
            "  cmp ax, 0\n"
            "  jz internal_label\n"
            "  mov ax, 1\n"
            "internal_label:\n"
            "  ret\n"
        ),
    )

    diagram = extractor.extract(source)

    names = [fn.name for fn in diagram.functions]
    assert "Entry" in names
    assert "internal_label" not in names
