from pathlib import Path

import pytest

from masma.infrastructure.antlr.runtime import load_generated_types, parse_source_text
from masma.infrastructure.masm.parser_adapter import _build_structure_visitor
from masma.infrastructure.masm.support import iter_source_lines


ROOT = Path(__file__).resolve().parent.parent
_STATEMENT_ACCESSORS = (
    "includeStmt",
    "equStmt",
    "namedSegmentStmt",
    "simpleSegmentStmt",
    "structStartStmt",
    "structEndStmt",
    "macroStartStmt",
    "endmStmt",
    "procStartStmt",
    "procEndStmt",
    "labelStmt",
    "dataDeclStmt",
    "structuredDirectiveStmt",
    "endStmt",
    "instructionStmt",
)


def _parse_statement_kind(source_line: str) -> str:
    generated = load_generated_types()
    parse_result = parse_source_text(f"{source_line}\n", generated)
    assert parse_result.diagnostics == ()
    statement = parse_result.tree.line(0).statement()
    for accessor in _STATEMENT_ACCESSORS:
        if getattr(statement, accessor)() is not None:
            return accessor
    raise AssertionError(f"could not classify statement: {source_line!r}")


@pytest.mark.parametrize(
    ("source_line", "expected_kind"),
    (
        ("include windows.inc", "includeStmt"),
        ("VALUE equ 1", "equStmt"),
        ("DataSeg SEGMENT para public", "namedSegmentStmt"),
        (".code", "simpleSegmentStmt"),
        ("Point STRUCT", "structStartStmt"),
        ("Point ENDS", "structEndStmt"),
        ("PrintLine MACRO text:REQ", "macroStartStmt"),
        ("ENDM", "endmStmt"),
        ("main PROC value:DWORD", "procStartStmt"),
        ("main ENDP", "procEndStmt"),
        ("start_loop:", "labelStmt"),
        ("buffer db 0", "dataDeclStmt"),
        (".IF eax == 0", "structuredDirectiveStmt"),
        ("mov eax, ebx", "instructionStmt"),
        ("END main", "endStmt"),
    ),
)
def test_patched_masm_grammar_classifies_supported_statement_steps(
    source_line: str,
    expected_kind: str,
) -> None:
    assert _parse_statement_kind(source_line) == expected_kind


def test_patched_masm_grammar_parses_valid_fixture_without_diagnostics() -> None:
    generated = load_generated_types()
    source_text = (ROOT / "tests" / "fixtures" / "valid.asm").read_text(encoding="utf-8")

    parse_result = parse_source_text(source_text, generated)

    assert parse_result.diagnostics == ()
    non_empty_lines = [line for line in parse_result.tree.line() if line.statement() is not None]
    assert len(non_empty_lines) >= 12


def test_antlr_structure_visitor_extracts_expected_elements_from_valid_fixture() -> None:
    generated = load_generated_types()
    source_text = (ROOT / "tests" / "fixtures" / "valid.asm").read_text(encoding="utf-8")
    parse_result = parse_source_text(source_text, generated)
    lines = iter_source_lines(source_text)

    visitor = _build_structure_visitor(generated.visitor_type, {line.number: line for line in lines})()
    elements = visitor.visit(parse_result.tree)
    extracted = {(element.kind.value, element.name) for element in elements}

    assert ("include", "windows.inc") in extracted
    assert ("include", "kernel32.lib") in extracted
    assert ("constant", "STD_OUTPUT_HANDLE") in extracted
    assert ("segment", ".data") in extracted
    assert ("variable", "message") in extracted
    assert ("struct", "Point") in extracted
    assert ("macro", "PrintLine") in extracted
    assert ("segment", ".code") in extracted
    assert ("procedure", "main") in extracted
    assert ("procedure", "helper") in extracted


def test_patched_masm_grammar_tracks_statement_steps_inside_proc_body() -> None:
    generated = load_generated_types()
    source_text = """
demo PROC
start:
    cmp eax, 0
    .IF eax == 0
        inc eax
    .ENDIF
    jnz start
    ret
demo ENDP
""".strip() + "\n"

    parse_result = parse_source_text(source_text, generated)
    assert parse_result.diagnostics == ()

    steps = []
    for line in parse_result.tree.line():
        statement = line.statement()
        if statement is None:
            continue
        for accessor in _STATEMENT_ACCESSORS:
            if getattr(statement, accessor)() is not None:
                steps.append(accessor)
                break

    assert steps == [
        "procStartStmt",
        "labelStmt",
        "instructionStmt",
        "structuredDirectiveStmt",
        "instructionStmt",
        "structuredDirectiveStmt",
        "instructionStmt",
        "instructionStmt",
        "procEndStmt",
    ]
