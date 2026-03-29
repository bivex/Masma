"""CLI application."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from html import escape
from pathlib import Path

from masma.application.control_flow import (
    BuildNassiDiagramCommand,
    BuildNassiDirectoryCommand,
    NassiDiagramBundleDTO,
    NassiDiagramService,
)
from masma.application.dto import ParseDirectoryCommand, ParseFileCommand, ParsingJobReportDTO
from masma.application.use_cases import ParsingJobService
from masma.domain.errors import MasmaError
from masma.infrastructure.filesystem.source_repository import FileSystemSourceRepository
from masma.infrastructure.masm.control_flow_extractor import MasmControlFlowExtractor
from masma.infrastructure.masm.parser_adapter import MasmSyntaxParser
from masma.infrastructure.rendering.nassi_html_renderer import HtmlNassiDiagramRenderer
from masma.infrastructure.system import (
    InMemoryParsingJobRepository,
    StructuredLoggingEventPublisher,
    SystemClock,
    configure_logging,
)


def main(argv: list[str] | None = None) -> int:
    parser = _build_argument_parser()
    args = parser.parse_args(argv)

    configure_logging(verbose=getattr(args, "verbose", False))

    try:
        if args.command == "parse-file":
            report = _build_parse_service().parse_file(ParseFileCommand(path=args.path))
        elif args.command == "parse-dir":
            report = _build_parse_service().parse_directory(ParseDirectoryCommand(root_path=args.path))
        elif args.command == "nassi-file":
            document = _build_nassi_service().build_file_diagram(
                BuildNassiDiagramCommand(path=args.path)
            )
            output_path = _resolve_output_path(args.path, args.out)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(document.html, encoding="utf-8")

            payload = document.to_dict()
            payload["output_path"] = str(output_path)
            print(json.dumps(payload, indent=2))
            return 0
        elif args.command == "nassi-dir":
            bundle = _build_nassi_service().build_directory_diagrams(
                BuildNassiDirectoryCommand(root_path=args.path)
            )
            output_dir = _resolve_output_directory(args.path, args.out)
            written_diagrams = _write_directory_diagrams(bundle, output_dir)
            index_path = output_dir / "index.html"
            index_path.write_text(
                _render_directory_index(bundle.root_path, written_diagrams),
                encoding="utf-8",
            )

            payload = bundle.to_dict()
            payload["output_dir"] = str(output_dir)
            payload["index_path"] = str(index_path)
            payload["documents"] = [
                {
                    "source_location": diagram.source_location,
                    "procedure_count": diagram.procedure_count,
                    "procedure_names": list(diagram.procedure_names),
                    "output_path": str(diagram.output_path),
                    "relative_output_path": diagram.relative_output_path,
                }
                for diagram in written_diagrams
            ]
            print(json.dumps(payload, indent=2))
            return 0
        else:
            parser.error(f"unsupported command: {args.command}")
    except MasmaError as error:
        print(json.dumps({"error": str(error)}, indent=2), file=sys.stderr)
        return 2

    print(json.dumps(report.to_dict(), indent=2))
    return _exit_code_for(report)


def _build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Parse MASM source code and render structured diagrams.")
    parser.add_argument("--verbose", action="store_true", help="Enable lifecycle logging.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_file = subparsers.add_parser("parse-file", help="Parse one MASM source file.")
    parse_file.add_argument("path", help="Path to a .asm or .inc file.")

    parse_dir = subparsers.add_parser("parse-dir", help="Parse all MASM source files in a directory.")
    parse_dir.add_argument("path", help="Path to a directory.")

    nassi_file = subparsers.add_parser(
        "nassi-file",
        help="Build a Nassi-Shneiderman HTML diagram for one MASM source file.",
    )
    nassi_file.add_argument("path", help="Path to a .asm or .inc file.")
    nassi_file.add_argument(
        "--out",
        help="Output HTML path. Defaults to <input>.nassi.html.",
    )

    nassi_dir = subparsers.add_parser(
        "nassi-dir",
        help="Build Nassi-Shneiderman HTML diagrams for all MASM source files in a directory.",
    )
    nassi_dir.add_argument("path", help="Path to a directory.")
    nassi_dir.add_argument(
        "--out",
        help="Output directory. Defaults to <input>.nassi/.",
    )
    return parser


def _build_parse_service() -> ParsingJobService:
    return ParsingJobService(
        source_repository=FileSystemSourceRepository(),
        parser=MasmSyntaxParser(),
        event_publisher=StructuredLoggingEventPublisher(),
        clock=SystemClock(),
        job_repository=InMemoryParsingJobRepository(),
    )


def _build_nassi_service() -> NassiDiagramService:
    return NassiDiagramService(
        source_repository=FileSystemSourceRepository(),
        extractor=MasmControlFlowExtractor(),
        renderer=HtmlNassiDiagramRenderer(),
    )


def _exit_code_for(report: ParsingJobReportDTO) -> int:
    if report.summary.technical_failure_count > 0:
        return 1
    return 0


def _resolve_output_path(input_path: str, explicit_output_path: str | None) -> Path:
    if explicit_output_path:
        return Path(explicit_output_path).expanduser().resolve()

    resolved_input = Path(input_path).expanduser().resolve()
    return resolved_input.with_suffix(".nassi.html")


def _resolve_output_directory(input_path: str, explicit_output_path: str | None) -> Path:
    if explicit_output_path:
        return Path(explicit_output_path).expanduser().resolve()

    resolved_input = Path(input_path).expanduser().resolve()
    return resolved_input.with_name(f"{resolved_input.name}.nassi")


@dataclass(frozen=True, slots=True)
class _WrittenNassiDiagram:
    source_location: str
    procedure_count: int
    procedure_names: tuple[str, ...]
    output_path: Path
    relative_output_path: str
    relative_source_path: str


def _write_directory_diagrams(
    bundle: NassiDiagramBundleDTO,
    output_dir: Path,
) -> tuple[_WrittenNassiDiagram, ...]:
    root_path = Path(bundle.root_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    written_diagrams: list[_WrittenNassiDiagram] = []
    for document in bundle.documents:
        source_path = Path(document.source_location)
        relative_source_path = source_path.relative_to(root_path)
        output_path = (output_dir / relative_source_path).with_suffix(".nassi.html")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(document.html, encoding="utf-8")
        written_diagrams.append(
            _WrittenNassiDiagram(
                source_location=document.source_location,
                procedure_count=document.procedure_count,
                procedure_names=document.procedure_names,
                output_path=output_path,
                relative_output_path=output_path.relative_to(output_dir).as_posix(),
                relative_source_path=relative_source_path.as_posix(),
            )
        )
    return tuple(written_diagrams)


def _render_directory_index(
    root_path: str,
    written_diagrams: tuple[_WrittenNassiDiagram, ...],
) -> str:
    total_procs = sum(d.procedure_count for d in written_diagrams)

    # Build JSON data blob for Alpine.js — one entry per file
    files_data = json.dumps(
        [
            {
                "path": d.relative_source_path,
                "href": d.relative_output_path,
                "procs": list(d.procedure_names),
                "count": d.procedure_count,
            }
            for d in written_diagrams
        ],
        ensure_ascii=False,
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Masma — {escape(Path(root_path).name)}</title>
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.14.1/dist/cdn.min.js"></script>
  <style>
    :root {{
      --bg:          #0a0f18;
      --bg-accent:   #10182a;
      --surface:     #111827;
      --surface-2:   #172131;
      --surface-3:   #1c2940;
      --border:      #2b3b59;
      --border-soft: #182338;
      --text:        #cfd8f6;
      --text-bright: #f4f7ff;
      --muted:       #8e9bbb;
      --blue:        #82aaff;
      --blue-dim:    #1c2e55;
      --green:       #a6da95;
      --green-dim:   #163628;
      --amber:       #f1ca7a;
      --amber-dim:   #39290f;
      --mono: "JetBrains Mono","Fira Code","Cascadia Code",monospace;
      --ui:   "IBM Plex Sans",-apple-system,"Segoe UI",system-ui,sans-serif;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--ui);
      font-size: 14px;
      color: var(--text);
      background: radial-gradient(circle at top, rgba(130,170,255,.10) 0%, transparent 28%),
                  var(--bg);
      min-height: 100vh;
    }}

    /* ── Header ─────────────────────────────────────────── */
    .header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(10,15,24,.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 14px 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .header-top {{
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .logo {{
      font-family: var(--mono);
      font-size: 15px;
      font-weight: 600;
      color: var(--blue);
      letter-spacing: .06em;
      flex-shrink: 0;
    }}
    .root-path {{
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      flex: 1;
      min-width: 0;
    }}
    .stats {{
      display: flex;
      gap: 8px;
      flex-shrink: 0;
      flex-wrap: wrap;
    }}
    .stat-chip {{
      padding: 3px 10px;
      border-radius: 99px;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .03em;
      white-space: nowrap;
    }}
    .stat-chip.files  {{ background: var(--blue-dim);  color: var(--blue);  }}
    .stat-chip.procs  {{ background: var(--green-dim); color: var(--green); }}
    .stat-chip.shown  {{ background: var(--surface-3); color: var(--muted); }}
    .search-wrap {{
      position: relative;
    }}
    .search-wrap svg {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--muted);
      pointer-events: none;
    }}
    .search {{
      width: 100%;
      padding: 9px 14px 9px 38px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      color: var(--text-bright);
      font-family: var(--ui);
      font-size: 14px;
      outline: none;
      transition: border-color .15s;
    }}
    .search:focus {{ border-color: var(--blue); }}
    .search::placeholder {{ color: var(--muted); }}

    /* ── Main content ────────────────────────────────────── */
    .content {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px 24px 48px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    /* ── Directory group ─────────────────────────────────── */
    .dir-group {{
      border: 1px solid var(--border-soft);
      border-radius: 10px;
      overflow: hidden;
      background: var(--surface);
    }}
    .dir-header {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 16px;
      background: var(--bg-accent);
      cursor: pointer;
      user-select: none;
      border-bottom: 1px solid var(--border-soft);
      transition: background .12s;
    }}
    .dir-header:hover {{ background: var(--surface-2); }}
    .dir-caret {{
      color: var(--muted);
      transition: transform .18s;
      flex-shrink: 0;
    }}
    .dir-caret.open {{ transform: rotate(90deg); }}
    .dir-icon {{ color: var(--amber); flex-shrink: 0; }}
    .dir-name {{
      font-family: var(--mono);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-bright);
      flex: 1;
    }}
    .dir-meta {{
      font-size: 11px;
      color: var(--muted);
      white-space: nowrap;
    }}
    .dir-body {{
      display: flex;
      flex-direction: column;
    }}

    /* ── File row ────────────────────────────────────────── */
    .file-row {{
      display: grid;
      grid-template-columns: 1fr auto;
      grid-template-rows: auto auto;
      gap: 4px 12px;
      padding: 10px 16px 10px 40px;
      border-bottom: 1px solid var(--border-soft);
      transition: background .1s;
    }}
    .file-row:last-child {{ border-bottom: 0; }}
    .file-row:hover {{ background: var(--surface-2); }}
    .file-link {{
      font-family: var(--mono);
      font-size: 12px;
      color: var(--blue);
      text-decoration: none;
      font-weight: 500;
      grid-row: 1;
      grid-column: 1;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .file-link:hover {{ color: var(--text-bright); text-decoration: underline; }}
    .file-link svg {{ color: var(--muted); flex-shrink: 0; }}
    .proc-count {{
      grid-row: 1;
      grid-column: 2;
      align-self: center;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 99px;
      background: var(--blue-dim);
      color: var(--blue);
      white-space: nowrap;
    }}
    .proc-count.zero {{
      background: var(--surface-3);
      color: var(--muted);
    }}
    .proc-pills {{
      grid-row: 2;
      grid-column: 1 / -1;
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }}
    .pill {{
      font-family: var(--mono);
      font-size: 10px;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--surface-3);
      color: var(--muted);
      cursor: pointer;
      border: 1px solid transparent;
      transition: all .1s;
    }}
    .pill:hover {{
      background: var(--blue-dim);
      color: var(--blue);
      border-color: var(--border);
    }}
    .pill.match {{
      background: var(--green-dim);
      color: var(--green);
      border-color: var(--green-dim);
    }}

    /* ── Empty state ─────────────────────────────────────── */
    .empty {{
      text-align: center;
      padding: 64px 24px;
      color: var(--muted);
      font-size: 15px;
    }}
    .empty svg {{ margin-bottom: 16px; color: var(--border); }}
  </style>
</head>
<body x-data="app()" x-init="init()">

  <header class="header">
    <div class="header-top">
      <span class="logo">MASMA</span>
      <span class="root-path" title="{escape(root_path)}">{escape(root_path)}</span>
      <div class="stats">
        <span class="stat-chip files">{len(written_diagrams)} files</span>
        <span class="stat-chip procs">{total_procs} procedures</span>
        <span class="stat-chip shown" x-text="shownLabel"></span>
      </div>
    </div>
    <div class="search-wrap">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>
      <input
        class="search"
        type="search"
        placeholder="Filter by file name or procedure…"
        x-model.debounce.120ms="query"
        x-ref="searchInput"
        @keydown.escape="query = ''"
      >
    </div>
  </header>

  <main class="content">
    <template x-for="group in visibleGroups" :key="group.dir">
      <div class="dir-group">
        <div class="dir-header" @click="toggleDir(group.dir)">
          <svg class="dir-caret" :class="{{ open: openDirs.has(group.dir) }}" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <polyline points="9 18 15 12 9 6"/>
          </svg>
          <svg class="dir-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7z"/>
          </svg>
          <span class="dir-name" x-text="group.dir || '(root)'"></span>
          <span class="dir-meta" x-text="group.files.length + ' files · ' + group.totalProcs + ' procs'"></span>
        </div>
        <div class="dir-body" x-show="openDirs.has(group.dir)" x-collapse.duration.200ms>
          <template x-for="file in group.files" :key="file.path">
            <div class="file-row">
              <a class="file-link" :href="file.href">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                </svg>
                <span x-text="file.name"></span>
              </a>
              <span class="proc-count" :class="{{ zero: file.count === 0 }}" x-text="file.count + (file.count === 1 ? ' proc' : ' procs')"></span>
              <div class="proc-pills" x-show="file.procs.length > 0">
                <template x-for="proc in file.procs" :key="proc">
                  <span
                    class="pill"
                    :class="{{ match: query && proc.toLowerCase().includes(query.toLowerCase()) }}"
                    x-text="proc"
                    @click="query = proc"
                    :title="'Filter by ' + proc"
                  ></span>
                </template>
              </div>
            </div>
          </template>
        </div>
      </div>
    </template>

    <div class="empty" x-show="visibleGroups.length === 0">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>
      <p>No results for &ldquo;<span x-text="query"></span>&rdquo;</p>
    </div>
  </main>

  <script>
    const FILES = {files_data};

    function app() {{
      return {{
        query: '',
        openDirs: new Set(),
        allGroups: [],
        visibleGroups: [],
        shownLabel: '',

        init() {{
          // Group files by directory
          const dirMap = new Map();
          for (const f of FILES) {{
            const parts = f.path.split('/');
            const name  = parts.pop();
            const dir   = parts.join('/');
            if (!dirMap.has(dir)) dirMap.set(dir, []);
            dirMap.get(dir).push({{ ...f, name, dir }});
          }}
          this.allGroups = [...dirMap.entries()].map(([dir, files]) => ({{
            dir,
            files,
            totalProcs: files.reduce((s, f) => s + f.count, 0),
          }}));
          // Open all dirs by default
          for (const g of this.allGroups) this.openDirs.add(g.dir);
          this.applyFilter();
          this.$watch('query', () => this.applyFilter());
        }},

        applyFilter() {{
          const q = this.query.toLowerCase().trim();
          if (!q) {{
            this.visibleGroups = this.allGroups;
            this.shownLabel = '';
            return;
          }}
          let totalShown = 0;
          this.visibleGroups = this.allGroups
            .map(g => {{
              const files = g.files.filter(f =>
                f.name.toLowerCase().includes(q) ||
                f.path.toLowerCase().includes(q) ||
                f.procs.some(p => p.toLowerCase().includes(q))
              );
              totalShown += files.length;
              return {{ ...g, files }};
            }})
            .filter(g => g.files.length > 0);
          // Auto-expand dirs that match
          for (const g of this.visibleGroups) this.openDirs.add(g.dir);
          this.shownLabel = totalShown + ' shown';
        }},

        toggleDir(dir) {{
          if (this.openDirs.has(dir)) this.openDirs.delete(dir);
          else this.openDirs.add(dir);
          // Trigger Alpine reactivity on Set
          this.openDirs = new Set(this.openDirs);
        }},
      }};
    }}
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    raise SystemExit(main())
