"""Runtime helpers for the generated MASM ANTLR parser."""

from __future__ import annotations

from dataclasses import dataclass
import importlib

from antlr4 import CommonTokenStream, InputStream

from masma.domain.errors import GeneratedParserNotAvailableError
from masma.domain.model import ParserVersion, SyntaxDiagnostic
from masma.infrastructure.antlr.error_listener import CollectingErrorListener


ANTLR_PARSER_VERSION = ParserVersion("masm-hybrid-parser@1.2.0+antlr4.13.2")


@dataclass(frozen=True, slots=True)
class GeneratedTypes:
    lexer_type: type
    parser_type: type
    visitor_type: type


@dataclass(frozen=True, slots=True)
class ParseResult:
    tree: object
    token_stream: CommonTokenStream
    diagnostics: tuple[SyntaxDiagnostic, ...]


def load_generated_types() -> GeneratedTypes:
    try:
        lexer_module = importlib.import_module("masma.infrastructure.antlr.generated.masm.MasmLexer")
        parser_module = importlib.import_module("masma.infrastructure.antlr.generated.masm.MasmParser")
        visitor_module = importlib.import_module("masma.infrastructure.antlr.generated.masm.MasmVisitor")
    except ModuleNotFoundError as error:
        raise GeneratedParserNotAvailableError(
            "generated MASM parser artifacts are missing; run "
            "`uv run python scripts/generate_masm_parser.py` first"
        ) from error

    return GeneratedTypes(
        lexer_type=lexer_module.MasmLexer,
        parser_type=parser_module.MasmParser,
        visitor_type=visitor_module.MasmVisitor,
    )


def parse_source_text(source_text: str, generated: GeneratedTypes) -> ParseResult:
    lexer = generated.lexer_type(InputStream(source_text))
    parser_error_listener = CollectingErrorListener()
    lexer_error_listener = CollectingErrorListener()

    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    token_stream = CommonTokenStream(lexer)
    parser = generated.parser_type(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    tree = parser.compilationUnit()
    diagnostics = tuple(lexer_error_listener.diagnostics + parser_error_listener.diagnostics)
    return ParseResult(tree=tree, token_stream=token_stream, diagnostics=diagnostics)
