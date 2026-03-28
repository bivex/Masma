"""Hybrid MASM parser adapter backed by ANTLR and line-based recovery."""

from __future__ import annotations

from time import perf_counter

from masma.domain.errors import GeneratedParserNotAvailableError
from masma.domain.model import (
    ParseOutcome,
    ParseStatistics,
    ParserVersion,
    SourceUnit,
    StructuralElement,
    StructuralElementKind,
    SyntaxDiagnostic,
)
from masma.domain.ports import SyntaxParser
from masma.infrastructure.antlr.runtime import (
    ANTLR_PARSER_VERSION,
    load_generated_types,
    parse_source_text,
)
from masma.infrastructure.masm.support import (
    EQU_RE,
    INCLUDE_RE,
    LABEL_RE,
    MACRO_RE,
    CEND_RE,
    CPROC_RE,
    PROC_RE,
    STRUCT_RE,
    VARIABLE_RE,
    SourceLine,
    classify_segment,
    collect_syntax_diagnostics,
    compact_text,
    is_code_directive,
    is_data_directive,
    iter_source_lines,
    token_count,
)


LINE_PARSER_VERSION = ParserVersion("masm-line-parser@1.0.0")


class MasmSyntaxParser(SyntaxParser):
    def __init__(self) -> None:
        self._generated = _try_load_generated_types()

    @property
    def parser_version(self) -> ParserVersion:
        if self._generated is None:
            return LINE_PARSER_VERSION
        return ANTLR_PARSER_VERSION

    def parse(self, source_unit: SourceUnit) -> ParseOutcome:
        started_at = perf_counter()
        try:
            lines = iter_source_lines(source_unit.content)
            diagnostics = list(collect_syntax_diagnostics(lines))
            elements = tuple(_extract_structural_elements(lines))
            parser_version = LINE_PARSER_VERSION

            if self._generated is not None:
                try:
                    parse_result = parse_source_text(source_unit.content, self._generated)
                    diagnostics = _merge_diagnostics(diagnostics, parse_result.diagnostics)
                    antlr_elements = tuple(
                        _build_structure_visitor(
                            self._generated.visitor_type,
                            {line.number: line for line in lines},
                        )().visit(parse_result.tree)
                    )
                    elements = _merge_elements(antlr_elements, elements)
                    parser_version = ANTLR_PARSER_VERSION
                except Exception:
                    parser_version = LINE_PARSER_VERSION

            elapsed_ms = round((perf_counter() - started_at) * 1000, 3)
            return ParseOutcome.success(
                source_unit=source_unit,
                parser_version=parser_version,
                diagnostics=tuple(diagnostics),
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


def _try_load_generated_types():
    try:
        return load_generated_types()
    except GeneratedParserNotAvailableError:
        return None


def _merge_diagnostics(
    primary: list[SyntaxDiagnostic] | tuple[SyntaxDiagnostic, ...],
    secondary: tuple[SyntaxDiagnostic, ...],
) -> list[SyntaxDiagnostic]:
    merged: list[SyntaxDiagnostic] = list(primary)
    seen = {(item.severity.value, item.message, item.line, item.column) for item in merged}
    for item in secondary:
        key = (item.severity.value, item.message, item.line, item.column)
        if key in seen:
            continue
        merged.append(item)
        seen.add(key)
    return merged


def _merge_elements(
    primary: tuple[StructuralElement, ...],
    secondary: tuple[StructuralElement, ...],
) -> tuple[StructuralElement, ...]:
    merged: list[StructuralElement] = list(primary)
    seen = {
        (item.kind.value, item.name, item.line, item.column, item.container, item.signature)
        for item in merged
    }
    for item in secondary:
        key = (item.kind.value, item.name, item.line, item.column, item.container, item.signature)
        if key in seen:
            continue
        merged.append(item)
        seen.add(key)
    return tuple(sorted(merged, key=lambda item: (item.line, item.column, item.kind.value, item.name)))


def _build_structure_visitor(visitor_base: type, lines_by_number: dict[int, SourceLine]) -> type:
    class MasmStructureVisitor(visitor_base):
        def __init__(self) -> None:
            super().__init__()
            self.elements: list[StructuralElement] = []
            self._current_segment: str | None = None
            self._current_procedure: str | None = None

        def visitCompilationUnit(self, ctx):  # noqa: N802
            for line_ctx in ctx.line():
                self.visit(line_ctx)
            return tuple(self.elements)

        def visitSimpleSegmentStmt(self, ctx):  # noqa: N802
            name = self._source_text(ctx).lower()
            self._current_segment = name
            self._append(
                StructuralElementKind.SEGMENT,
                name,
                ctx.start.line,
                signature=self._source_text(ctx),
            )
            return None

        def visitNamedSegmentStmt(self, ctx):  # noqa: N802
            name = ctx.identifier().getText()
            self._current_segment = name
            self._append(
                StructuralElementKind.SEGMENT,
                name,
                ctx.start.line,
                signature=self._source_text(ctx),
            )
            return None

        def visitIncludeStmt(self, ctx):  # noqa: N802
            source_text = self._source_text(ctx)
            match = INCLUDE_RE.match(source_text)
            target = compact_text(match.group("target")) if match is not None else source_text
            self._append(
                StructuralElementKind.INCLUDE,
                target,
                ctx.start.line,
                signature=source_text,
            )
            return None

        def visitEquStmt(self, ctx):  # noqa: N802
            self._append(
                StructuralElementKind.CONSTANT,
                ctx.identifier().getText(),
                ctx.start.line,
                container=self._current_segment,
                signature=self._source_text(ctx),
            )
            return None

        def visitStructStartStmt(self, ctx):  # noqa: N802
            self._append(
                StructuralElementKind.STRUCT,
                ctx.identifier().getText(),
                ctx.start.line,
                container=self._current_segment,
                signature=self._source_text(ctx),
            )
            return None

        def visitMacroStartStmt(self, ctx):  # noqa: N802
            self._append(
                StructuralElementKind.MACRO,
                ctx.identifier().getText(),
                ctx.start.line,
                container=self._current_segment,
                signature=self._source_text(ctx),
            )
            return None

        def visitProcStartStmt(self, ctx):  # noqa: N802
            name = ctx.identifier().getText()
            self._current_procedure = name
            self._append(
                StructuralElementKind.PROCEDURE,
                name,
                ctx.start.line,
                container=self._current_segment,
                signature=self._source_text(ctx),
            )
            return None

        def visitProcEndStmt(self, ctx):  # noqa: N802
            if self._current_procedure and self._current_procedure.lower() == ctx.identifier().getText().lower():
                self._current_procedure = None
            return None

        def visitLabelStmt(self, ctx):  # noqa: N802
            self._append(
                StructuralElementKind.LABEL,
                ctx.identifier().getText(),
                ctx.start.line,
                container=self._current_procedure or self._current_segment,
                signature=ctx.identifier().getText(),
            )
            return None

        def visitDataDeclStmt(self, ctx):  # noqa: N802
            kind = (
                StructuralElementKind.CONSTANT
                if (self._current_segment or "").lower() == ".const"
                else StructuralElementKind.VARIABLE
            )
            self._append(
                kind,
                ctx.identifier().getText(),
                ctx.start.line,
                container=self._current_segment,
                signature=self._source_text(ctx),
            )
            return None

        def _append(
            self,
            kind: StructuralElementKind,
            name: str,
            line: int,
            *,
            container: str | None = None,
            signature: str | None = None,
        ) -> None:
            self.elements.append(
                StructuralElement(
                    kind=kind,
                    name=name,
                    line=line,
                    column=1,
                    container=container,
                    signature=compact_text(signature or name, limit=140),
                )
            )

        def _source_text(self, ctx) -> str:
            line = lines_by_number.get(ctx.start.line)
            if line is None:
                return ctx.getText()
            return line.text

    return MasmStructureVisitor


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

        if proc_match := (PROC_RE.match(line.text) or CPROC_RE.match(line.text)):
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

        if line.text.lower().endswith(" endp") or CEND_RE.match(line.text):
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
