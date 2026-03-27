"""Line-oriented MASM parser adapter."""

from __future__ import annotations

from time import perf_counter

from masma.domain.model import (
    ParseOutcome,
    ParseStatistics,
    ParserVersion,
    SourceUnit,
    StructuralElement,
    StructuralElementKind,
)
from masma.domain.ports import SyntaxParser
from masma.infrastructure.masm.support import (
    EQU_RE,
    INCLUDE_RE,
    LABEL_RE,
    MACRO_RE,
    PROC_RE,
    STRUCT_RE,
    VARIABLE_RE,
    classify_segment,
    collect_syntax_diagnostics,
    compact_text,
    is_code_directive,
    is_data_directive,
    iter_source_lines,
    token_count,
)


MASM_PARSER_VERSION = ParserVersion("masm-line-parser@1.0.0")


class MasmSyntaxParser(SyntaxParser):
    @property
    def parser_version(self) -> ParserVersion:
        return MASM_PARSER_VERSION

    def parse(self, source_unit: SourceUnit) -> ParseOutcome:
        started_at = perf_counter()
        try:
            lines = iter_source_lines(source_unit.content)
            diagnostics = collect_syntax_diagnostics(lines)
            elements = tuple(_extract_structural_elements(lines))
            elapsed_ms = round((perf_counter() - started_at) * 1000, 3)

            return ParseOutcome.success(
                source_unit=source_unit,
                parser_version=self.parser_version,
                diagnostics=diagnostics,
                structural_elements=elements,
                statistics=ParseStatistics(
                    token_count=token_count(source_unit.content),
                    structural_element_count=len(elements),
                    diagnostic_count=len(diagnostics),
                    elapsed_ms=elapsed_ms,
                ),
            )
        except Exception as error:
            elapsed_ms = round((perf_counter() - started_at) * 1000, 3)
            return ParseOutcome.technical_failure(
                source_unit=source_unit,
                parser_version=self.parser_version,
                message=str(error),
                elapsed_ms=elapsed_ms,
            )


def _extract_structural_elements(lines):
    current_segment: str | None = None
    current_procedure: str | None = None

    for line in lines:
        if not line.text:
            continue

        if segment_name := classify_segment(line):
            current_segment = segment_name
            yield StructuralElement(
                kind=StructuralElementKind.SEGMENT,
                name=segment_name,
                line=line.number,
                column=1,
                signature=compact_text(line.text),
            )
            if is_code_directive(line):
                current_segment = segment_name
            continue

        if include_match := INCLUDE_RE.match(line.text):
            yield StructuralElement(
                kind=StructuralElementKind.INCLUDE,
                name=compact_text(include_match.group("target")),
                line=line.number,
                column=1,
                signature=compact_text(line.text),
            )
            continue

        if equ_match := EQU_RE.match(line.text):
            yield StructuralElement(
                kind=StructuralElementKind.CONSTANT,
                name=equ_match.group("name"),
                line=line.number,
                column=1,
                container=current_segment,
                signature=compact_text(line.text),
            )
            continue

        if struct_match := STRUCT_RE.match(line.text):
            yield StructuralElement(
                kind=StructuralElementKind.STRUCT,
                name=struct_match.group("name"),
                line=line.number,
                column=1,
                container=current_segment,
                signature=compact_text(line.text),
            )
            continue

        if macro_match := MACRO_RE.match(line.text):
            yield StructuralElement(
                kind=StructuralElementKind.MACRO,
                name=macro_match.group("name"),
                line=line.number,
                column=1,
                container=current_segment,
                signature=compact_text(line.text, limit=140),
            )
            continue

        if proc_match := PROC_RE.match(line.text):
            current_procedure = proc_match.group("name")
            yield StructuralElement(
                kind=StructuralElementKind.PROCEDURE,
                name=current_procedure,
                line=line.number,
                column=1,
                container=current_segment,
                signature=compact_text(line.text, limit=140),
            )
            continue

        if line.text.lower().endswith(" endp"):
            current_procedure = None
            continue

        if label_match := LABEL_RE.match(line.text):
            yield StructuralElement(
                kind=StructuralElementKind.LABEL,
                name=label_match.group("name"),
                line=line.number,
                column=1,
                container=current_procedure or current_segment,
                signature=label_match.group("name"),
            )
            continue

        if current_segment and (is_data_directive(line) or current_segment.lower() in {".data", ".data?", ".const"}):
            variable_match = VARIABLE_RE.match(line.text)
            if variable_match is not None:
                kind = (
                    StructuralElementKind.CONSTANT
                    if current_segment.lower() == ".const"
                    else StructuralElementKind.VARIABLE
                )
                yield StructuralElement(
                    kind=kind,
                    name=variable_match.group("name"),
                    line=line.number,
                    column=1,
                    container=current_segment,
                    signature=compact_text(line.text),
                )
