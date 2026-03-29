#!/usr/bin/env python3
"""
debug_verify.py — internal SDK verification script for Masma.

Runs all three pipeline stages on one or more .asm/.inc files and
reports any errors, warnings, or unexpected step types.

Usage:
    uv run python scripts/debug_verify.py path/to/file.asm
    uv run python scripts/debug_verify.py path/to/dir/
    uv run python scripts/debug_verify.py path/to/file.asm --verbose
    uv run python scripts/debug_verify.py path/to/file.asm --steps   # dump all flow steps
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# ── SDK imports ────────────────────────────────────────────────────────────────
from masma.domain.control_flow import (
    ActionFlowStep,
    AlignFlowStep,
    CallFlowStep,
    DataDeclFlowStep,
    ForInFlowStep,
    GuardFlowStep,
    IfFlowStep,
    IfdefFlowStep,
    InvokeFlowStep,
    JumpFlowStep,
    LabelFlowStep,
    LocalDeclFlowStep,
    MacroCallFlowStep,
    RepeatStringFlowStep,
    RepeatWhileFlowStep,
    StackFlowStep,
    SwitchFlowStep,
    WhileFlowStep,
)
from masma.domain.model import (
    DiagnosticSeverity,
    ParseStatus,
    SourceUnit,
    SourceUnitId,
)
from masma.infrastructure.filesystem.source_repository import FileSystemSourceRepository
from masma.infrastructure.masm.control_flow_extractor import MasmControlFlowExtractor
from masma.infrastructure.masm.parser_adapter import MasmSyntaxParser

# ── ANSI colours (disabled on non-TTY) ────────────────────────────────────────
_TTY = sys.stdout.isatty()
_R  = "\033[31m" if _TTY else ""
_Y  = "\033[33m" if _TTY else ""
_G  = "\033[32m" if _TTY else ""
_C  = "\033[36m" if _TTY else ""
_DIM = "\033[2m"  if _TTY else ""
_B  = "\033[1m"  if _TTY else ""
_RST = "\033[0m" if _TTY else ""

KNOWN_STEP_TYPES = (
    ActionFlowStep, AlignFlowStep, CallFlowStep, DataDeclFlowStep,
    ForInFlowStep, GuardFlowStep, IfFlowStep, IfdefFlowStep,
    InvokeFlowStep, JumpFlowStep, LabelFlowStep, LocalDeclFlowStep,
    MacroCallFlowStep, RepeatStringFlowStep, RepeatWhileFlowStep,
    StackFlowStep, SwitchFlowStep, WhileFlowStep,
)


def _fmt_step(step, indent: int = 0) -> list[str]:
    """Recursively format a flow step and its children."""
    pad = "  " * indent
    name = type(step).__name__
    lines = []
    if isinstance(step, ActionFlowStep):
        lines.append(f"{pad}{_DIM}{name}{_RST}  {step.label!r}")
    elif isinstance(step, IfFlowStep):
        lines.append(f"{pad}{_C}{name}{_RST}  cond={step.condition!r}")
        for s in step.then_steps:
            lines.extend(_fmt_step(s, indent + 1))
        if step.else_steps:
            lines.append(f"{pad}  {_DIM}else:{_RST}")
            for s in step.else_steps:
                lines.extend(_fmt_step(s, indent + 1))
    elif isinstance(step, (WhileFlowStep, RepeatWhileFlowStep, ForInFlowStep)):
        header = getattr(step, "condition", getattr(step, "header", ""))
        lines.append(f"{pad}{_C}{name}{_RST}  {header!r}")
        for s in step.body_steps:
            lines.extend(_fmt_step(s, indent + 1))
    elif isinstance(step, SwitchFlowStep):
        lines.append(f"{pad}{_C}{name}{_RST}  expr={step.expression!r}")
        for case in step.cases:
            lines.append(f"{pad}  case {case.label!r}")
            for s in case.steps:
                lines.extend(_fmt_step(s, indent + 2))
    elif isinstance(step, IfdefFlowStep):
        lines.append(f"{pad}{_C}{name}{_RST}  {step.kind} {step.condition!r}")
        for s in step.body_steps:
            lines.extend(_fmt_step(s, indent + 1))
    elif isinstance(step, JumpFlowStep):
        kind = f"cond={step.condition}" if step.condition else "unconditional"
        lines.append(f"{pad}{_Y}{name}{_RST}  {kind} → {step.target!r}")
    elif isinstance(step, LocalDeclFlowStep):
        lines.append(f"{pad}{_DIM}{name}{_RST}  {step.name} = {step.type_info!r}")
    elif isinstance(step, DataDeclFlowStep):
        lines.append(f"{pad}{_DIM}{name}{_RST}  {step.name} {step.type_info!r}")
    elif isinstance(step, StackFlowStep):
        lines.append(f"{pad}{_DIM}{name}{_RST}  {step.direction} {step.operand}  depth={step.stack_depth}")
    else:
        lines.append(f"{pad}{_DIM}{name}{_RST}  {step!r}")
    return lines


def _walk_steps(steps, func):
    """Walk all steps recursively, calling func(step)."""
    for step in steps:
        func(step)
        for attr in ("then_steps", "else_steps", "body_steps", "branches"):
            for child in getattr(step, attr, ()):
                if isinstance(child, tuple) and len(child) == 3:
                    # IfdefFlowStep branches: (kind, cond, steps)
                    _walk_steps(child[2], func)
                else:
                    _walk_steps([child] if hasattr(child, "__class__") and not isinstance(child, tuple) else child, func)
        if isinstance(step, SwitchFlowStep):
            for case in step.cases:
                _walk_steps(case.steps, func)


def verify_file(path: Path, *, verbose: bool, show_steps: bool) -> bool:
    """Run all three SDK stages on a file. Returns True if clean."""
    content = path.read_text(encoding="utf-8", errors="replace")
    source_unit = SourceUnit(
        identifier=SourceUnitId(path.name),
        location=str(path),
        content=content,
    )

    ok = True
    sep = f"{_DIM}{'─' * 70}{_RST}"
    print(f"\n{sep}")
    print(f"{_B}{path}{_RST}")

    # ── Stage 1: Syntax parser ─────────────────────────────────────────────
    t0 = time.perf_counter()
    parse_outcome = MasmSyntaxParser().parse(source_unit)
    parse_ms = (time.perf_counter() - t0) * 1000

    status_color = _G if parse_outcome.status == ParseStatus.SUCCEEDED else (_Y if "diagnostics" in parse_outcome.status else _R)
    print(f"\n  {_B}[1] Syntax parser{_RST}  {status_color}{parse_outcome.status}{_RST}  "
          f"{_DIM}{parse_ms:.1f}ms  parser={parse_outcome.parser_version.value}{_RST}")
    print(f"      elements={parse_outcome.statistics.structural_element_count}  "
          f"tokens={parse_outcome.statistics.token_count}  "
          f"diagnostics={parse_outcome.statistics.diagnostic_count}")

    for d in parse_outcome.diagnostics:
        color = _R if d.severity == DiagnosticSeverity.ERROR else _Y
        print(f"      {color}[{d.severity}] line {d.line}:{d.column}  {d.message}{_RST}")
        if d.severity == DiagnosticSeverity.ERROR:
            ok = False

    if verbose:
        for e in parse_outcome.structural_elements:
            cont = f"  ← {e.container}" if e.container else ""
            print(f"      {_DIM}{e.kind:12}{_RST}  {e.name}{cont}  {_DIM}line {e.line}{_RST}")

    # ── Stage 2: Control flow extractor ───────────────────────────────────
    t0 = time.perf_counter()
    try:
        diagram = MasmControlFlowExtractor().extract(source_unit)
        cf_ms = (time.perf_counter() - t0) * 1000

        print(f"\n  {_B}[2] Control flow extractor{_RST}  {_G}ok{_RST}  "
              f"{_DIM}{cf_ms:.1f}ms{_RST}")
        print(f"      procs={len(diagram.functions)}  "
              f"structs={len(diagram.structs)}  "
              f"externals={len(diagram.externals)}  "
              f"typedefs={len(diagram.typedefs)}  "
              f"constants={len(diagram.constants)}")

        # Count step types
        step_counts: dict[str, int] = {}
        unknown_steps: list[str] = []

        def _count(step):
            stype = type(step).__name__
            step_counts[stype] = step_counts.get(stype, 0) + 1
            if not isinstance(step, KNOWN_STEP_TYPES):
                unknown_steps.append(repr(step))

        for fn in diagram.functions:
            _walk_steps(fn.steps, _count)

        if step_counts:
            parts = "  ".join(f"{k}={v}" for k, v in sorted(step_counts.items()))
            print(f"      steps: {_DIM}{parts}{_RST}")

        if unknown_steps:
            print(f"      {_R}UNKNOWN step types:{_RST}")
            for s in unknown_steps[:10]:
                print(f"        {s}")
            ok = False

        # Per-procedure detail
        if verbose or show_steps:
            for fn in diagram.functions:
                print(f"\n    {_C}{fn.name}{_RST}  {_DIM}{fn.signature}{_RST}")
                if show_steps:
                    for step in fn.steps:
                        for line in _fmt_step(step, indent=3):
                            print(line)
                elif verbose:
                    print(f"      {len(fn.steps)} top-level steps")

    except Exception as exc:
        cf_ms = (time.perf_counter() - t0) * 1000
        print(f"\n  {_B}[2] Control flow extractor{_RST}  {_R}EXCEPTION{_RST}  {_DIM}{cf_ms:.1f}ms{_RST}")
        print(f"      {_R}{type(exc).__name__}: {exc}{_RST}")
        ok = False
        diagram = None

    # ── Stage 3: Renderer ──────────────────────────────────────────────────
    if diagram is not None:
        from masma.infrastructure.rendering.nassi_html_renderer import HtmlNassiDiagramRenderer
        t0 = time.perf_counter()
        try:
            html = HtmlNassiDiagramRenderer().render(diagram)
            render_ms = (time.perf_counter() - t0) * 1000
            print(f"\n  {_B}[3] Renderer{_RST}  {_G}ok{_RST}  "
                  f"{_DIM}{render_ms:.1f}ms  {len(html):,} bytes HTML{_RST}")
        except Exception as exc:
            render_ms = (time.perf_counter() - t0) * 1000
            print(f"\n  {_B}[3] Renderer{_RST}  {_R}EXCEPTION{_RST}  {_DIM}{render_ms:.1f}ms{_RST}")
            print(f"      {_R}{type(exc).__name__}: {exc}{_RST}")
            ok = False

    status = f"{_G}CLEAN{_RST}" if ok else f"{_R}ERRORS{_RST}"
    print(f"\n  result: {status}")
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Masma internal SDK verifier")
    parser.add_argument("path", nargs="+", help=".asm/.inc file or directory")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show structural elements and per-proc detail")
    parser.add_argument("--steps", action="store_true", help="Dump all flow steps for every procedure")
    args = parser.parse_args()

    paths: list[Path] = []
    for raw in args.path:
        p = Path(raw)
        if p.is_dir():
            paths.extend(sorted(p.rglob("*.asm")) + sorted(p.rglob("*.inc")))
        elif p.is_file():
            paths.append(p)
        else:
            print(f"{_R}not found: {p}{_RST}", file=sys.stderr)
            sys.exit(1)

    if not paths:
        print(f"{_R}no .asm/.inc files found{_RST}", file=sys.stderr)
        sys.exit(1)

    total = len(paths)
    failures = 0
    t_total = time.perf_counter()

    for path in paths:
        clean = verify_file(path, verbose=args.verbose, show_steps=args.steps)
        if not clean:
            failures += 1

    elapsed = (time.perf_counter() - t_total) * 1000
    print(f"\n{'─' * 70}")
    color = _G if failures == 0 else _R
    print(f"{color}{_B}{total - failures}/{total} files clean{_RST}  {_DIM}{elapsed:.0f}ms total{_RST}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
