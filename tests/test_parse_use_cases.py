import json
import os
import subprocess
import sys
from pathlib import Path

from masma.application.dto import ParseDirectoryCommand, ParseFileCommand
from masma.application.use_cases import ParsingJobService
from masma.infrastructure.filesystem.source_repository import FileSystemSourceRepository
from masma.infrastructure.masm.parser_adapter import MasmSyntaxParser
from masma.infrastructure.system import (
    InMemoryParsingJobRepository,
    StructuredLoggingEventPublisher,
    SystemClock,
)


ROOT = Path(__file__).resolve().parent.parent


def _build_service() -> ParsingJobService:
    return ParsingJobService(
        source_repository=FileSystemSourceRepository(),
        parser=MasmSyntaxParser(),
        event_publisher=StructuredLoggingEventPublisher(),
        clock=SystemClock(),
        job_repository=InMemoryParsingJobRepository(),
    )


def test_parse_file_extracts_masm_structure() -> None:
    service = _build_service()
    report = service.parse_file(ParseFileCommand(path=str(ROOT / "tests" / "fixtures" / "valid.asm")))

    assert report.summary.source_count == 1
    assert report.summary.technical_failure_count == 0
    assert report.sources[0].status == "succeeded"
    assert report.sources[0].parser_version.startswith("masm-hybrid-parser@")
    assert {element.kind for element in report.sources[0].structural_elements} >= {
        "include",
        "constant",
        "variable",
        "struct",
        "macro",
        "procedure",
        "segment",
    }


def test_parse_directory_returns_report_for_all_masm_sources() -> None:
    service = _build_service()
    report = service.parse_directory(ParseDirectoryCommand(root_path=str(ROOT / "tests" / "fixtures")))

    assert report.summary.source_count == 3
    assert len(report.sources) == 3


def test_parse_file_reports_unclosed_structured_block_as_diagnostic() -> None:
    service = _build_service()
    report = service.parse_file(ParseFileCommand(path=str(ROOT / "tests" / "fixtures" / "invalid.asm")))

    assert report.summary.source_count == 1
    assert report.summary.technical_failure_count == 0
    assert report.sources[0].status == "succeeded_with_diagnostics"
    assert any(".IF" in diagnostic.message for diagnostic in report.sources[0].diagnostics)


def test_cli_outputs_json_for_masm_parse() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "masma.presentation.cli.main",
            "parse-file",
            str(ROOT / "tests" / "fixtures" / "valid.asm"),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONPATH": str(ROOT / "src")},
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["summary"]["source_count"] == 1
    assert payload["sources"][0]["status"] == "succeeded"
    assert payload["sources"][0]["parser_version"].startswith("masm-hybrid-parser@")
