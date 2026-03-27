"""Generate an HTML feature-set report for the demo MASM source file."""

from __future__ import annotations

from html import escape
from pathlib import Path

from masma.application.control_flow import BuildNassiDiagramCommand, NassiDiagramService
from masma.application.dto import ParseFileCommand
from masma.application.use_cases import ParsingJobService
from masma.domain.control_flow import (
    ActionFlowStep,
    ControlFlowStep,
    IfFlowStep,
    RepeatWhileFlowStep,
    WhileFlowStep,
)
from masma.infrastructure.filesystem.source_repository import FileSystemSourceRepository
from masma.infrastructure.masm.control_flow_extractor import MasmControlFlowExtractor
from masma.infrastructure.masm.parser_adapter import MasmSyntaxParser
from masma.infrastructure.rendering.nassi_html_renderer import HtmlNassiDiagramRenderer
from masma.infrastructure.system import (
    InMemoryParsingJobRepository,
    StructuredLoggingEventPublisher,
    SystemClock,
)


ROOT = Path(__file__).resolve().parent.parent
SOURCE_PATH = ROOT / "docs" / "reports" / "masm-feature-set.asm"
REPORT_PATH = ROOT / "docs" / "reports" / "masm-feature-set.report.html"
NASSI_PATH = ROOT / "docs" / "reports" / "masm-feature-set.nassi.html"

FEATURES = (
    "ANTLR-backed hybrid parser",
    "include / includelib",
    "EQU constants",
    ".const / .data / .data?",
    "STRUCT / ENDS",
    "MACRO / ENDM",
    "PROC / ENDP",
    "labels",
    "structured directives (.IF/.WHILE/.REPEAT)",
    "jump-based if/else recovery",
    "jump-based loop recovery",
)


def main() -> None:
    parse_service = ParsingJobService(
        source_repository=FileSystemSourceRepository(),
        parser=MasmSyntaxParser(),
        event_publisher=StructuredLoggingEventPublisher(),
        clock=SystemClock(),
        job_repository=InMemoryParsingJobRepository(),
    )
    nassi_service = NassiDiagramService(
        source_repository=FileSystemSourceRepository(),
        extractor=MasmControlFlowExtractor(),
        renderer=HtmlNassiDiagramRenderer(),
    )

    parse_report = parse_service.parse_file(ParseFileCommand(path=str(SOURCE_PATH)))
    source_report = parse_report.sources[0]

    nassi_document = nassi_service.build_file_diagram(BuildNassiDiagramCommand(path=str(SOURCE_PATH)))
    NASSI_PATH.write_text(nassi_document.html, encoding="utf-8")

    source_unit = FileSystemSourceRepository().load_file(str(SOURCE_PATH))
    diagram = MasmControlFlowExtractor().extract(source_unit)
    step_blocks = "".join(_render_procedure_steps(proc.qualified_name, proc.steps) for proc in diagram.functions)

    element_rows = "".join(
        (
            "<tr>"
            f"<td>{escape(element.kind)}</td>"
            f"<td>{escape(element.name)}</td>"
            f"<td>{element.line}:{element.column}</td>"
            f"<td>{escape(element.container or '-')}</td>"
            f"<td>{escape(element.signature or '-')}</td>"
            "</tr>"
        )
        for element in source_report.structural_elements
    )
    diagnostic_rows = "".join(
        (
            "<tr>"
            f"<td>{escape(item.severity)}</td>"
            f"<td>{escape(item.message)}</td>"
            f"<td>{item.line}:{item.column}</td>"
            "</tr>"
        )
        for item in source_report.diagnostics
    )
    if not diagnostic_rows:
        diagnostic_rows = '<tr><td colspan="3">No diagnostics</td></tr>'

    feature_badges = "".join(f'<span class="badge">{escape(feature)}</span>' for feature in FEATURES)

    html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Masma Feature Set Report</title>
    <style>
      :root {{
        --bg: #f2eee5;
        --panel: #fffaf0;
        --ink: #18222f;
        --muted: #596677;
        --line: #2e4765;
        --accent: #0f7c90;
        --accent-2: #f0b429;
        --good: #197278;
        --shadow: 0 20px 40px rgba(24, 34, 47, 0.16);
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        font-family: "IBM Plex Sans", "Segoe UI", sans-serif;
        color: var(--ink);
        background:
          radial-gradient(circle at top left, rgba(15, 124, 144, 0.16), transparent 28%),
          linear-gradient(180deg, #efe7d6 0%, var(--bg) 100%);
        padding: 28px;
      }}
      .shell {{
        max-width: 1240px;
        margin: 0 auto;
        background: var(--panel);
        border: 2px solid var(--line);
        box-shadow: var(--shadow);
      }}
      .hero {{
        padding: 20px 24px 18px;
        border-bottom: 2px solid var(--line);
        background: linear-gradient(135deg, #0f7c90, #155e75);
        color: #f8fbff;
      }}
      .hero h1 {{
        margin: 0;
        font-size: 30px;
      }}
      .hero p {{
        margin: 8px 0 0;
        max-width: 900px;
        line-height: 1.55;
      }}
      .content {{
        padding: 22px;
        display: grid;
        gap: 18px;
      }}
      .stats {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 12px;
      }}
      .card {{
        background: #fffdf8;
        border: 1px solid #d5c6ab;
        padding: 14px 16px;
      }}
      .card .label {{
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
      }}
      .card .value {{
        margin-top: 6px;
        font-size: 22px;
        font-weight: 700;
      }}
      .section {{
        background: #fffdf8;
        border: 1px solid #d5c6ab;
        padding: 16px;
      }}
      .section h2 {{
        margin: 0 0 12px;
        font-size: 20px;
      }}
      .badges {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
      }}
      .badge {{
        padding: 6px 10px;
        border-radius: 999px;
        background: rgba(25, 114, 120, 0.12);
        border: 1px solid rgba(25, 114, 120, 0.35);
        color: var(--good);
        font-size: 13px;
        font-weight: 600;
      }}
      table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
      }}
      th, td {{
        padding: 10px 8px;
        border-top: 1px solid #e8dcc7;
        vertical-align: top;
        text-align: left;
      }}
      th {{
        border-top: 0;
        color: var(--muted);
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
      }}
      .steps {{
        display: grid;
        gap: 12px;
      }}
      .proc {{
        border: 1px solid #dfcfb7;
        background: #fffaf2;
        padding: 12px;
      }}
      .proc h3 {{
        margin: 0 0 8px;
      }}
      .tree {{
        font-family: "JetBrains Mono", monospace;
        font-size: 13px;
        line-height: 1.7;
        white-space: pre-wrap;
      }}
      .links {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
      }}
      .links a {{
        color: #0b5cad;
        font-weight: 700;
        text-decoration: none;
      }}
      iframe {{
        width: 100%;
        min-height: 640px;
        border: 1px solid #d5c6ab;
        background: #fff;
      }}
    </style>
  </head>
  <body>
    <div class="shell">
      <section class="hero">
        <h1>Masma Feature Set Report</h1>
        <p>Demonstration report for the current MASM feature set, generated from one source file through the hybrid parser, structural extractor, and Nassi renderer.</p>
      </section>
      <main class="content">
        <section class="stats">
          <div class="card"><div class="label">Source</div><div class="value">{escape(SOURCE_PATH.name)}</div></div>
          <div class="card"><div class="label">Parser</div><div class="value">{escape(source_report.parser_version)}</div></div>
          <div class="card"><div class="label">Status</div><div class="value">{escape(source_report.status)}</div></div>
          <div class="card"><div class="label">Elements</div><div class="value">{len(source_report.structural_elements)}</div></div>
          <div class="card"><div class="label">Procedures</div><div class="value">{nassi_document.procedure_count}</div></div>
          <div class="card"><div class="label">Diagnostics</div><div class="value">{len(source_report.diagnostics)}</div></div>
        </section>

        <section class="section">
          <h2>Supported Features In This File</h2>
          <div class="badges">{feature_badges}</div>
        </section>

        <section class="section">
          <h2>Artifacts</h2>
          <div class="links">
            <a href="{escape(SOURCE_PATH.name)}">{escape(SOURCE_PATH.name)}</a>
            <a href="{escape(NASSI_PATH.name)}">{escape(NASSI_PATH.name)}</a>
          </div>
        </section>

        <section class="section">
          <h2>Structural Elements</h2>
          <table>
            <thead>
              <tr><th>Kind</th><th>Name</th><th>Location</th><th>Container</th><th>Signature</th></tr>
            </thead>
            <tbody>{element_rows}</tbody>
          </table>
        </section>

        <section class="section">
          <h2>Diagnostics</h2>
          <table>
            <thead>
              <tr><th>Severity</th><th>Message</th><th>Location</th></tr>
            </thead>
            <tbody>{diagnostic_rows}</tbody>
          </table>
        </section>

        <section class="section">
          <h2>Control-Flow Steps</h2>
          <div class="steps">{step_blocks}</div>
        </section>

        <section class="section">
          <h2>Embedded Nassi Report</h2>
          <iframe src="{escape(NASSI_PATH.name)}" title="Nassi diagram"></iframe>
        </section>
      </main>
    </div>
  </body>
</html>
"""
    REPORT_PATH.write_text(html, encoding="utf-8")


def _render_procedure_steps(name: str, steps: tuple[ControlFlowStep, ...]) -> str:
    return (
        '<article class="proc">'
        f"<h3>{escape(name)}</h3>"
        f'<div class="tree">{escape(_render_steps(steps))}</div>'
        "</article>"
    )


def _render_steps(steps: tuple[ControlFlowStep, ...], *, depth: int = 0) -> str:
    lines: list[str] = []
    prefix = "  " * depth
    for step in steps:
        if isinstance(step, ActionFlowStep):
            lines.append(f"{prefix}- action: {step.label}")
            continue
        if isinstance(step, IfFlowStep):
            lines.append(f"{prefix}- if: {step.condition}")
            lines.append(f"{prefix}  then:")
            lines.append(_render_steps(step.then_steps, depth=depth + 2))
            if step.else_steps:
                lines.append(f"{prefix}  else:")
                lines.append(_render_steps(step.else_steps, depth=depth + 2))
            continue
        if isinstance(step, WhileFlowStep):
            lines.append(f"{prefix}- while: {step.condition}")
            lines.append(_render_steps(step.body_steps, depth=depth + 1))
            continue
        if isinstance(step, RepeatWhileFlowStep):
            lines.append(f"{prefix}- repeat-until: {step.condition}")
            lines.append(_render_steps(step.body_steps, depth=depth + 1))
            continue
        lines.append(f"{prefix}- step: {step.__class__.__name__}")
    return "\n".join(line for line in lines if line.strip())


if __name__ == "__main__":
    main()
