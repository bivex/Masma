"""Collect syntax diagnostics from ANTLR parsing."""

from __future__ import annotations

from antlr4.error.ErrorListener import ErrorListener

from masma.domain.model import DiagnosticSeverity, SyntaxDiagnostic


class CollectingErrorListener(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.diagnostics: list[SyntaxDiagnostic] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e) -> None:  # noqa: N802
        self.diagnostics.append(
            SyntaxDiagnostic(
                severity=DiagnosticSeverity.ERROR,
                message=msg,
                line=line,
                column=column + 1,
            )
        )
