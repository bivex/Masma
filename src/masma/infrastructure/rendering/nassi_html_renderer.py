"""Render structured control flow as Nassi-Shneiderman HTML."""

from __future__ import annotations

from html import escape
from math import ceil
import re

from masma.domain.control_flow import (
    ActionFlowStep,
    AlignFlowStep,
    CallFlowStep,
    ControlFlowDiagram,
    ControlFlowStep,
    DeferFlowStep,
    DoCatchFlowStep,
    ForInFlowStep,
    GuardFlowStep,
    IfdefFlowStep,
    IfFlowStep,
    InvokeFlowStep,
    LabelFlowStep,
    MacroCallFlowStep,
    RepeatStringFlowStep,
    RepeatWhileFlowStep,
    StructDefinition,
    SwitchCaseFlow,
    SwitchFlowStep,
    WhileFlowStep,
)
from masma.domain.ports import NassiDiagramRenderer


class HtmlNassiDiagramRenderer(NassiDiagramRenderer):
    def _depth_badge(self, i: int) -> str:
        if i == 0:
            return ""
        if i <= 20:
            return f" {chr(0x2460 + i - 1)}"
        if i <= 35:
            return f" {chr(0x3251 + i - 21)}"
        return f" {chr(0x32B1 + i - 36)}"

    def _depth_css(self) -> str:
        colors = ["blue", "green", "purple", "teal", "amber"]
        rules = []
        for i in range(51):
            c = colors[i % 5]
            rules.append(f"      .ns-if-depth-{i}-triangle {{ fill: var(--{c}-dim); stroke: var(--{c}); }}")
            rules.append(f"      .ns-if-depth-{i}-diagonal {{ stroke: var(--{c}); }}")
        return "\n".join(rules)

    def render(self, diagram: ControlFlowDiagram) -> str:
        sections = "".join(
            self._render_function(function, entry_point=diagram.entry_point)
            for function in diagram.functions
        )
        if not sections:
            sections = '<section class="function-panel"><p class="empty-file">No procedures found.</p></section>'
        if diagram.structs:
            sections = self._render_structs(diagram.structs) + sections
        if diagram.file_header:
            header_block = (
                f'<div class="file-header-block">{escape(diagram.file_header)}</div>'
            )
            sections = header_block + sections
        # File overview section: includes, externals, publics, segments, constants| variables
        sections = self._render_file_overview(diagram) + sections

        return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Nassi-Shneiderman Control Flow</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
      :root {{
        /* Palette — editor-first dark */
        --bg:          #0a0f18;
        --bg-accent:   #10182a;
        --surface:     #111827;
        --surface-2:   #172131;
        --surface-3:   #1c2940;
        --surface-4:   #233452;
        --border:      #2b3b59;
        --border-strong: #3f5378;
        --border-soft: #182338;
        --text:        #cfd8f6;
        --text-bright: #f4f7ff;
        --muted:       #8e9bbb;
        --shadow:      0 24px 72px rgba(3, 8, 18, 0.56);

        /* Accent colours */
        --blue:        #82aaff;
        --blue-dim:    #243b69;
        --green:       #a6da95;
        --green-dim:   #163628;
        --red:         #ff93a9;
        --red-dim:     #371925;
        --orange:      #ffb86b;
        --orange-dim:  #37230f;
        --teal:        #56d4dd;
        --teal-dim:    #11343b;
        --purple:      #c4a7ff;
        --purple-dim:  #2a1d41;
        --amber:       #f1ca7a;
        --amber-dim:   #39290f;

        /* Block fills */
        --loop-fill:   #132033;
        --switch-fill: #102529;
        --guard-fill:  #23190c;
        --do-fill:     #1a1624;
        --defer-fill:  #241d0d;
        --yes-fill:    #102217;
        --no-fill:     #251019;
        --action-fill: var(--surface-2);
        --note-fill:   #101720;

        /* Code font */
        --mono: "JetBrains Mono", "Fira Code", "Cascadia Code", "SF Mono", "Menlo", monospace;
        --ui:   "IBM Plex Sans", -apple-system, "Segoe UI", system-ui, sans-serif;
      }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        font-family: var(--ui);
        font-size: 14px;
        color: var(--text);
        background:
          radial-gradient(circle at top, rgba(130, 170, 255, 0.12), transparent 28%),
          linear-gradient(180deg, var(--bg) 0%, #0c121d 100%);
        padding: 24px;
        min-height: 100vh;
        overflow-x: auto;
        color-scheme: dark;
        -webkit-font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
      }}
      /* ── Viewer shell ── */
      .viewer {{
        width: max-content;
        min-width: min(1200px, calc(100vw - 48px));
        margin: 0 auto;
        border: 1px solid var(--border-strong);
        border-radius: 14px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
          var(--surface);
        box-shadow: var(--shadow);
        overflow: hidden;
      }}
      .titlebar {{
        padding: 10px 16px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0)),
          var(--surface-3);
        border-bottom: 1px solid var(--border-strong);
        display: flex;
        align-items: center;
        gap: 10px;
      }}
      .titlebar-icon {{
        width: 14px; height: 14px;
        border-radius: 50%;
        background: var(--blue-dim);
        border: 1px solid var(--blue);
        flex-shrink: 0;
      }}
      .titlebar-text {{
        font-size: 13.5px;
        font-weight: 600;
        color: var(--text-bright);
        letter-spacing: 0.01em;
      }}
      .toolbar {{
        padding: 9px 16px;
        border-bottom: 1px solid var(--border-soft);
        background:
          linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0)),
          var(--surface);
        display: flex;
        flex-wrap: wrap;
        gap: 8px 14px;
        align-items: baseline;
      }}
      .toolbar-label {{
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--blue);
        background: rgba(130, 170, 255, 0.14);
        border: 1px solid rgba(130, 170, 255, 0.3);
        border-radius: 999px;
        padding: 3px 8px;
        white-space: nowrap;
      }}
      .toolbar-path {{
        font-family: var(--mono);
        font-size: 12px;
        color: var(--muted);
        overflow-wrap: anywhere;
      }}
      /* ── Viewer body ── */
      .viewer-body {{
        padding: 16px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0) 180px),
          var(--bg);
      }}
      /* ── Function panel ── */
      .function-panel {{
        margin-bottom: 16px;
        border: 1px solid var(--border);
        border-radius: 10px;
        background: rgba(10, 15, 24, 0.72);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
        overflow: hidden;
      }}
      .function-panel:last-child {{ margin-bottom: 0; }}
      .function-head {{
        padding: 12px 16px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
          var(--surface-3);
        border-bottom: 1px solid var(--border-strong);
      }}
      .function-title {{
        font-size: 15px;
        font-weight: 600;
        color: var(--text-bright);
        line-height: 1.3;
        display: flex;
        align-items: center;
        gap: 8px;
      }}
      .anchor-link {{
        font-size: 13px;
        font-weight: 400;
        color: var(--muted);
        text-decoration: none;
        opacity: 0;
        transition: opacity 0.15s;
        flex-shrink: 0;
      }}
      .function-head:hover .anchor-link {{
        opacity: 1;
      }}
      .anchor-link:hover {{
        color: var(--blue);
      }}
      .function-panel.is-macro {{
        border-color: var(--purple-dim);
      }}
      .function-panel.is-macro .function-head {{
        background:
          linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
          var(--purple-dim);
        border-bottom-color: rgba(196, 167, 255, 0.3);
      }}
      .function-panel.is-macro .function-title {{
        color: var(--purple);
      }}
      .macro-badge {{
        display: inline-block;
        font-size: 9.5px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--purple);
        background: rgba(196, 167, 255, 0.15);
        border: 1px solid rgba(196, 167, 255, 0.35);
        border-radius: 999px;
        padding: 1px 7px;
        margin-right: 7px;
        vertical-align: middle;
      }}
      .function-signature {{
        margin-top: 5px;
        font-family: var(--mono);
        font-size: 12px;
        line-height: 1.6;
        color: var(--muted);
        overflow-wrap: anywhere;
        word-break: break-word;
      }}
      .function-body {{
        padding: 12px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0)),
          rgba(7, 11, 18, 0.84);
      }}
      .function-body > .ns-sequence {{
        width: max-content;
        min-width: 100%;
      }}
      /* ── Node sequence ── */
      .ns-sequence {{
        display: flex;
        flex-direction: column;
        width: max-content;
        min-width: 100%;
      }}
      .ns-sequence > .ns-node + .ns-node,
      .ns-cases > .case + .case,
      .ns-catches > .ns-node + .ns-node {{
        margin-top: -1px;
      }}
      .ns-node {{
        border: 1px solid var(--border);
        border-radius: 6px;
        background: var(--action-fill);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
      }}
      /* ── Block headers/footers ── */
      .ns-header,
      .ns-footer,
      .case-title {{
        padding: 7px 12px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0)),
          var(--blue-dim);
        color: var(--text-bright);
        font-family: var(--mono);
        font-size: 12px;
        font-weight: 500;
        line-height: 1.4;
        border-bottom: 1px solid var(--border-strong);
        overflow-wrap: anywhere;
        word-break: break-word;
      }}
      .ns-footer {{
        border-top: 1px solid var(--border);
        border-bottom: 0;
      }}
      /* ── Action label ── */
      .ns-label,
      .empty,
      .ns-note {{
        padding: 8px 12px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0)),
          var(--action-fill);
      }}
      .action-text {{
        display: block;
        font-family: var(--mono);
        font-size: 13px;
        line-height: 1.72;
        color: var(--text-bright);
        letter-spacing: -0.01em;
        font-variant-ligatures: none;
        tab-size: 2;
        white-space: pre-wrap;
        overflow-wrap: anywhere;
      }}
      /* ── Block type colours ── */
      .ns-guard   {{ background: var(--guard-fill); }}
      .ns-loop,
      .ns-repeat  {{ background: var(--loop-fill); }}
      .ns-switch  {{ background: var(--switch-fill); }}
      .ns-do-catch {{ background: var(--do-fill); }}
      .ns-defer   {{ background: var(--defer-fill); }}
      .ns-invoke  {{ background: var(--surface-2); border-left: 3px solid var(--green); }}
      .ns-invoke  > .ns-label {{ background: rgba(166, 218, 149, 0.10); }}
      .ns-ret {{ border-left: 3px solid var(--red); }}
      .ns-ret > .ns-label {{ background: rgba(255, 147, 169, 0.08); }}
      .ns-macro  {{ background: var(--surface-2); border-left: 3px solid var(--purple); }}
      .ns-macro  > .ns-label {{ background: rgba(196, 167, 255, 0.08); }}
      .ns-ifdef {{ border-left: 3px dashed var(--muted); background: var(--surface); }}
      .ns-ifdef > .ns-header {{ background: var(--surface-3); color: var(--muted); font-style: italic; }}
      .ns-ifdef-branch {{ border-top: 1px dashed var(--border-soft); }}
      .ns-ifdef-branch > .ns-header {{ background: rgba(142, 155, 187, 0.06); color: var(--muted); font-style: italic; }}
      .ns-align-marker {{
        display: flex;
        align-items: center;
        gap: 6px;
        padding: 3px 12px;
        color: var(--amber);
        font-family: var(--mono);
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: rgba(241, 202, 122, 0.05);
        border-top: 1px dashed rgba(241, 202, 122, 0.25);
        border-bottom: 1px dashed rgba(241, 202, 122, 0.25);
      }}
      .ns-align-marker::before,
      .ns-align-marker::after {{
        content: "";
        flex: 1;
        height: 1px;
        background: rgba(241, 202, 122, 0.2);
      }}
      .segment-badge {{
        display: inline-block;
        font-size: 9.5px;
        font-weight: 600;
        letter-spacing: 0.06em;
        color: var(--muted);
        background: rgba(142, 155, 187, 0.12);
        border: 1px solid rgba(142, 155, 187, 0.25);
        border-radius: 999px;
        padding: 1px 7px;
        margin-right: 7px;
        vertical-align: middle;
        font-family: var(--mono);
      }}
      /* ── File overview panel ── */
      .file-overview {{
        margin-bottom: 16px;
        border: 1px solid var(--border);
        border-radius: 10px;
        background: rgba(10, 15, 24, 0.72);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.02);
        overflow: hidden;
      }}
      .file-overview-head {{
        padding: 10px 16px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01)),
          var(--surface-3);
        border-bottom: 1px solid var(--border-strong);
        font-size: 13.5px;
        font-weight: 600;
        color: var(--text-bright);
      }}
      .file-overview-grid {{
        padding: 12px 16px;
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
        gap: 12px;
      }}
      .overview-card {{
        border: 1px solid var(--border-soft);
        border-radius: 8px;
        padding: 10px 12px;
        background: var(--surface);
      }}
      .overview-card-title {{
        font-size: 9.5px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 6px;
      }}
      .overview-card-title.inc {{ color: #56d4dd; }}
      .overview-card-title.ext {{ color: var(--orange); }}
      .overview-card-title.pub {{ color: var(--green); }}
      .overview-card-title.seg {{ color: var(--amber); }}
      .overview-card-title.const {{ color: var(--purple); }}
      .overview-card-title.var {{ color: var(--teal); }}
      .overview-card-list {{
        display: flex;
        flex-wrap: wrap;
        gap: 4px 8px;
      }}
      .overview-tag {{
        font-family: var(--mono);
        font-size: 11px;
        color: var(--text);
        background: var(--surface-2);
        border: 1px solid var(--border-soft);
        border-radius: 4px;
        padding: 2px 6px;
        white-space: nowrap;
      }}
      .entry-badge {{
        display: inline-block;
        font-size: 9.5px;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: var(--green);
        background: rgba(166, 218, 149, 0.14);
        border: 1px solid rgba(166, 218, 149, 0.35);
        border-radius: 999px;
        padding: 1px 7px;
        margin-right: 7px;
        vertical-align: middle;
      }}
      .function-panel.is-entry {{
        border-color: rgba(166, 218, 149, 0.35);
      }}
      .function-panel.is-entry .function-head {{
        border-bottom-color: rgba(166, 218, 149, 0.3);
        background:
          linear-gradient(180deg, rgba(166, 218, 149, 0.07), rgba(255,255,255,0)),
          var(--surface-3);
      }}
      .ns-label-marker {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 5px 12px;
        background: var(--surface-3);
        border-top: 1px solid var(--border-soft);
        border-bottom: 1px solid var(--border-soft);
        color: var(--muted);
        font-family: var(--mono);
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }}
      .ns-label-marker::before {{
        content: "";
        display: block;
        width: 32px;
        height: 1px;
        background: var(--border-strong);
        flex-shrink: 0;
      }}
      .ns-label-marker::after {{
        content: "";
        display: block;
        flex: 1;
        height: 1px;
        background: var(--border-strong);
      }}
      .file-header-block {{
        margin: 0 0 12px 0;
        padding: 10px 16px;
        background: var(--surface-3);
        border: 1px solid var(--border-soft);
        border-radius: 8px;
        border-left: 3px solid var(--muted);
        color: var(--muted);
        font-family: var(--mono);
        font-size: 11.5px;
        line-height: 1.65;
        white-space: pre-wrap;
        overflow-wrap: anywhere;
      }}

      .ns-guard   > .ns-header {{ background: var(--orange-dim); color: var(--orange); }}
      .ns-switch  > .ns-header,
      .case-title              {{ background: var(--teal-dim);   color: var(--teal);   }}
      .ns-do-catch > .ns-header {{ background: var(--purple-dim); color: var(--purple); }}
      .ns-defer   > .ns-header {{ background: var(--amber-dim);  color: var(--amber);  }}

      /* Left accent stripes */
      .ns-node.ns-loop,
      .ns-node.ns-repeat  {{ border-left: 3px solid var(--blue); }}
      .ns-node.ns-guard   {{ border-left: 3px solid var(--orange); }}
      .ns-node.ns-switch  {{ border-left: 3px solid var(--teal); }}
      .ns-node.ns-do-catch {{ border-left: 3px solid var(--purple); }}
      .ns-node.ns-defer   {{ border-left: 3px solid var(--amber); }}

      /* Depth tinting */
      .ns-depth-1 > .ns-node {{ background-color: rgba(255,255,255,0.012); }}
      .ns-depth-2 > .ns-node {{ background-color: rgba(255,255,255,0.020); }}
      .ns-depth-3 > .ns-node {{ background-color: rgba(255,255,255,0.028); }}

      /* ── If/else branches (classic NS diagram with SVG) ── */
      .ns-if-cap {{
        border-bottom: 1px solid var(--border);
        line-height: 0;
      }}
      .ns-if-svg {{
        display: block;
        height: auto;
      }}
      .ns-if-triangle {{
        fill: var(--blue-dim);
        stroke: var(--border);
        stroke-width: 1;
      }}
      .ns-if-diagonal {{
        stroke: var(--border);
        stroke-width: 1;
      }}
      .ns-if-condition-fo {{
        overflow: hidden;
      }}
      .ns-if-condition-text {{
        font-family: var(--mono);
        font-size: 13px;
        font-weight: 500;
        color: var(--text-bright);
        text-align: center;
        word-break: break-word;
        overflow-wrap: anywhere;
        line-height: 1.3;
        padding: 4px 8px;
      }}
      .ns-if-label-yes {{
        font-family: var(--mono);
        font-size: 11px;
        font-weight: 700;
        fill: var(--green);
        text-transform: uppercase;
        letter-spacing: 0.06em;
      }}
      .ns-if-label-no {{
        font-family: var(--mono);
        font-size: 11px;
        font-weight: 700;
        fill: var(--red);
        text-transform: uppercase;
        letter-spacing: 0.06em;
      }}

      /* ── Switch/case (classic NS diagram) ── */
      .ns-switch-header {{
        padding: 9px 12px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0)),
          var(--teal-dim);
        color: var(--text-bright);
        font-family: var(--mono);
        font-size: 12px;
        font-weight: 500;
        border-bottom: 1px solid var(--border-strong);
        overflow-wrap: anywhere;
        word-break: break-word;
      }}
      .ns-switch-cases {{
        display: grid;
        grid-auto-flow: column;
        grid-auto-columns: minmax(140px, max-content);
        background: var(--bg);
        width: max-content;
        min-width: 100%;
      }}
      .ns-switch-case-col {{
        border-right: 1px solid var(--border);
        min-width: 140px;
        display: flex;
        flex-direction: column;
      }}
      .ns-switch-case-col:last-child {{
        border-right: none;
      }}
      .ns-switch-case-value {{
        padding: 9px 12px;
        background: rgba(16, 24, 39, 0.86);
        color: var(--teal);
        font-family: var(--mono);
        font-size: 11px;
        font-weight: 600;
        border-bottom: 1px solid var(--border-strong);
        text-align: center;
        overflow-wrap: anywhere;
        word-break: break-word;
      }}
      .ns-switch-case-body {{
        padding: 0;
        background: var(--bg);
        min-height: 40px;
      }}
      .ns-switch-case-body .ns-sequence {{
        padding: 8px;
      }}

      /* Depth-coded if-cap triangles and diagonals (0-50, cycling blue→green→purple→teal→amber) */
{self._depth_css()}

      .ns-branches {{
        display: grid;
        grid-template-columns: repeat(2, max-content);
        background: var(--surface-2);
        width: max-content;
        min-width: 100%;
      }}
      .ns-branches-single {{ grid-template-columns: max-content; }}
      .ns-branch {{
        border-left: 2px solid var(--border);
        background: var(--surface-2);
      }}
      .ns-branch-yes {{
        background: rgba(158, 206, 106, 0.08);
      }}
      .ns-branch-no {{
        background: rgba(247, 118, 142, 0.08);
      }}
      .ns-branch-yes > .ns-sequence > .ns-node {{
        background: rgba(158, 206, 106, 0.12);
      }}
      .ns-branch-no > .ns-sequence > .ns-node {{
        background: rgba(247, 118, 142, 0.12);
      }}
      .ns-branch-yes .ns-label,
      .ns-branch-yes .empty,
      .ns-branch-yes .ns-note {{
        background: rgba(158, 206, 106, 0.14);
      }}
      .ns-branch-no .ns-label,
      .ns-branch-no .empty,
      .ns-branch-no .ns-note {{
        background: rgba(247, 118, 142, 0.14);
      }}
      .ns-branch-yes > .ns-branch-title {{
        background: rgba(158, 206, 106, 0.2);
        color: var(--green);
      }}
      .ns-branch-no > .ns-branch-title {{
        background: rgba(247, 118, 142, 0.18);
        color: var(--red);
      }}
      .ns-branch:first-child {{ border-left: 0; }}
      .ns-branch-title {{
        padding: 7px 12px;
        border-bottom: 1px solid var(--border);
        background: rgba(18, 26, 41, 0.92);
        color: var(--muted);
        font-size: 10.5px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
      }}
      .ns-cases {{ background: var(--surface-2); }}
      .case {{ border-top: 1px solid var(--border); }}
      .case:first-child {{ border-top: 0; }}
      .ns-catches {{ border-top: 1px solid var(--border); }}

      .empty {{
        color: var(--muted);
        font-style: italic;
        font-size: 12px;
        background: rgba(20, 28, 41, 0.92);
      }}
      .ns-note {{
        color: var(--muted);
        font-family: var(--mono);
        font-size: 11px;
        font-style: italic;
        background: var(--note-fill);
        border-top: 1px solid var(--border);
        padding: 8px 12px;
      }}
      .empty-file {{
        padding: 24px;
        color: var(--muted);
      }}

      /* ── Struct definitions panel ── */
      .structs-panel {{
        margin-bottom: 16px;
        border: 1px solid var(--border);
        border-radius: 10px;
        overflow: hidden;
        background: rgba(10, 15, 24, 0.72);
      }}
      .structs-panel-head {{
        padding: 9px 16px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0)),
          var(--surface-3);
        border-bottom: 1px solid var(--border-strong);
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--teal);
      }}
      .structs-grid {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        padding: 12px;
        background: rgba(7, 11, 18, 0.84);
      }}
      .struct-card {{
        border: 1px solid var(--border);
        border-left: 3px solid var(--teal);
        border-radius: 7px;
        min-width: 160px;
        overflow: hidden;
        background: var(--surface-2);
      }}
      .struct-card-name {{
        padding: 6px 12px;
        background:
          linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0)),
          var(--teal-dim);
        color: var(--teal);
        font-family: var(--mono);
        font-size: 12px;
        font-weight: 600;
        border-bottom: 1px solid var(--border-strong);
      }}
      .struct-fields {{
        padding: 6px 0;
      }}
      .struct-field {{
        display: flex;
        align-items: baseline;
        gap: 8px;
        padding: 3px 12px;
        font-family: var(--mono);
        font-size: 11.5px;
        line-height: 1.55;
      }}
      .struct-field:hover {{
        background: rgba(255,255,255,0.03);
      }}
      .struct-field-name {{
        color: var(--text-bright);
        flex-shrink: 0;
      }}
      .struct-field-type {{
        color: var(--muted);
        font-size: 10.5px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }}

      @media (max-width: 800px) {{
        body {{ padding: 12px; }}
        .viewer {{
          width: auto;
          min-width: 0;
        }}
        .viewer-body {{ padding: 8px; }}
        .function-body {{
          padding: 6px;
          overflow-x: auto;
        }}
        .function-body > .ns-sequence,
        .ns-sequence {{
          width: 100%;
          min-width: 0;
        }}
        .ns-branches {{
          width: 100%;
          min-width: 0;
          grid-template-columns: 1fr;
        }}
        .ns-branches-single {{ grid-template-columns: 1fr; }}
        .ns-branch {{
          border-left: 0;
          border-top: 1px solid var(--border);
        }}
        .ns-branch:first-child {{ border-top: 0; }}
      }}
    </style>
  </head>
  <body>
    <div class="viewer">
      <div class="titlebar">
        <div class="titlebar-icon"></div>
        <span class="titlebar-text">Masma · NSD Viewer</span>
      </div>
      <div class="toolbar">
        <span class="toolbar-label">Nassi-Shneiderman</span>
        <code class="toolbar-path">{escape(diagram.source_location)}</code>
      </div>
      <main class="viewer-body">{sections}</main>
    </div>
  </body>
</html>
"""

    def _render_file_overview(self, diagram: ControlFlowDiagram) -> str:
        cards: list[str] = []

        def _tag_list(items: tuple, css_class: str) -> str:
            if not items:
                return ""
            tags = "".join(
                f'<span class="overview-tag" title="{escape(getattr(t, "detail", "") or t.name)}">{escape(t.name)}</span>'
                for t in items
            )
            return f'<div class="overview-card-list">{tags}</div>'

        def _card(title: str, items: tuple[str, ...], css_class: str) -> str:
            content = _tag_list(items, css_class)
            if not content:
                return ""
            return (
                f'<div class="overview-card">'
                f'<div class="overview-card-title {css_class}">{title}</div>'
                f'{content}'
                f'</div>'
            )

        cards.append(_card("Includes", diagram.includes, "inc"))
        cards.append(_card("Externals", diagram.externals, "ext"))
        cards.append(_card("Publics", diagram.publics, "pub"))
        cards.append(_card("Segments", diagram.segments, "seg"))
        cards.append(_card("Constants", diagram.constants, "const"))
        cards.append(_card("Variables", diagram.variables, "var"))
        filtered = [c for c in cards if c]
        if not filtered:
            return ""
        return (
            '<div class="file-overview">'
            '<div class="file-overview-head">File Overview</div>'
            f'<div class="file-overview-grid">{"".join(filtered)}</div>'
            '</div>'
        )

    def _render_structs(self, structs: tuple[StructDefinition, ...]) -> str:
        cards = []
        for struct in structs:
            if struct.fields:
                fields_html = "".join(
                    f'<div class="struct-field">'
                    f'<span class="struct-field-name">{escape(f.name)}</span>'
                    f'<span class="struct-field-type">{escape(f.type)}</span>'
                    f'</div>'
                    for f in struct.fields
                )
            else:
                fields_html = '<div class="struct-field" style="color:var(--muted);font-style:italic">empty</div>'
            cards.append(
                f'<div class="struct-card">'
                f'<div class="struct-card-name">{escape(struct.name)}</div>'
                f'<div class="struct-fields">{fields_html}</div>'
                f'</div>'
            )
        return (
            '<div class="structs-panel">'
            '<div class="structs-panel-head">Structures</div>'
            f'<div class="structs-grid">{"".join(cards)}</div>'
            '</div>'
        )

    def _render_function(self, function, *, entry_point: str | None = None) -> str:
        is_macro = getattr(function, "kind", "proc") == "macro"
        is_entry = (
            entry_point is not None
            and function.name.lower() == entry_point.lower()
            and not is_macro
        )
        panel_class = "function-panel"
        if is_macro:
            panel_class += " is-macro"
        if is_entry:
            panel_class += " is-entry"
        kind_badge = '<span class="macro-badge">▷ macro</span>' if is_macro else ""
        entry_badge = '<span class="entry-badge">▶ entry</span>' if is_entry else ""
        seg = getattr(function, "segment", None)
        seg_badge = f'<span class="segment-badge">{escape(seg)}</span>' if seg else ""
        anchor_id = re.sub(r"[^a-zA-Z0-9_-]", "-", function.name).strip("-").lower()
        anchor_link = f'<a class="anchor-link" href="#{anchor_id}" title="Link to {escape(function.name)}">#</a>'
        return (
            f'<section class="{panel_class}" id="{anchor_id}">'
            '<div class="function-head">'
            f'<h2 class="function-title">{seg_badge}{kind_badge}{entry_badge}{escape(function.qualified_name)}{anchor_link}</h2>'
            f'<div class="function-signature">{escape(function.signature)}</div>'
            "</div>"
            '<div class="function-body">'
            f"{self._render_sequence(function.steps, depth=0)}"
            "</div>"
            "</section>"
        )

    def _render_sequence(self, steps: tuple[ControlFlowStep, ...], *, depth: int) -> str:
        if not steps:
            return '<div class="empty">No structured steps.</div>'
        rendered = "".join(self._render_step(step, depth=depth) for step in steps)
        return f'<div class="ns-sequence ns-depth-{depth}">{rendered}</div>'

    def _render_step(self, step: ControlFlowStep, *, depth: int) -> str:
        if isinstance(step, ActionFlowStep):
            is_ret = step.label.lower() in ("ret", "retn", "retf")
            css = "ns-node ns-action ns-ret" if is_ret else "ns-node ns-action"
            return (
                f'<div class="{css}">'
                f'<div class="ns-label" aria-label="Action {escape(step.label)}">'
                f'<code class="action-text">{escape(step.label)}</code>'
                "</div>"
                "</div>"
            )
        if isinstance(step, IfFlowStep):
            if step.else_steps:
                else_markup = (
                    '<div class="ns-branch ns-branch-no" aria-label="Else branch">'
                    f"{self._render_sequence(step.else_steps, depth=depth + 1)}"
                    "</div>"
                )
                branches_class = "ns-branches"
                trailing_note = ""
            else:
                else_markup = ""
                branches_class = "ns-branches ns-branches-single"
                trailing_note = '<div class="ns-note">No branch continues after the decision.</div>'

            return (
                '<div class="ns-node ns-if">'
                f"{self._render_if_cap(step.condition, depth=depth)}"
                f'<div class="{branches_class}">'
                '<div class="ns-branch ns-branch-yes" aria-label="Then branch">'
                f"{self._render_sequence(step.then_steps, depth=depth + 1)}"
                "</div>"
                f"{else_markup}"
                "</div>"
                f"{trailing_note}"
                "</div>"
            )
        if isinstance(step, GuardFlowStep):
            return (
                '<div class="ns-node ns-guard">'
                f"{self._render_header(f'⚑ Guard {step.condition}')}"
                '<div class="ns-branch ns-branch-no"><div class="ns-branch-title">Failure / exit</div>'
                f"{self._render_sequence(step.else_steps, depth=depth + 1)}"
                "</div>"
                "</div>"
            )
        if isinstance(step, WhileFlowStep):
            return self._render_single_body(f"↻ While {step.condition}", step.body_steps, depth=depth)
        if isinstance(step, ForInFlowStep):
            return self._render_single_body(f"∀ For {step.header}", step.body_steps, depth=depth)
        if isinstance(step, RepeatWhileFlowStep):
            cond = step.condition
            footer_text = f"↺ {cond}" if cond.upper().startswith("UNTIL") else f"↺ While {cond}"
            return (
                '<div class="ns-node ns-repeat">'
                f"{self._render_header('↺ Repeat')}"
                f"{self._render_sequence(step.body_steps, depth=depth + 1)}"
                f"{self._render_footer(footer_text)}"
                "</div>"
            )
        if isinstance(step, SwitchFlowStep):
            return self._render_switch(step, depth=depth)
        if isinstance(step, DoCatchFlowStep):
            catches = "".join(
                self._render_single_body(
                    f"Catch {catch.pattern}",
                    catch.steps,
                    depth=depth + 1,
                    css_class="ns-do-catch",
                )
                for catch in step.catches
            )
            return (
                '<div class="ns-node ns-do-catch">'
                f"{self._render_header('Do')}"
                f"{self._render_sequence(step.body_steps, depth=depth + 1)}"
                f'<div class="ns-catches">{catches}</div>'
                "</div>"
            )
        if isinstance(step, DeferFlowStep):
            return self._render_single_body("Defer", step.body_steps, depth=depth, css_class="ns-defer")
        if isinstance(step, InvokeFlowStep):
            args_text = ", ".join(step.args) if step.args else ""
            label = f"⇒ INVOKE {step.target}" + (f", {args_text}" if args_text else "")
            return (
                '<div class="ns-node ns-invoke">'
                f'<div class="ns-label" aria-label="Invoke {escape(step.target)}">'
                f'<code class="action-text">{escape(label)}</code>'
                "</div>"
                "</div>"
            )
        if isinstance(step, CallFlowStep):
            label = f"⇒ call {step.target}"
            return (
                '<div class="ns-node ns-invoke">'
                f'<div class="ns-label" aria-label="Call {escape(step.target)}">'
                f'<code class="action-text">{escape(label)}</code>'
                "</div>"
                "</div>"
            )
        if isinstance(step, MacroCallFlowStep):
            args_text = ", ".join(step.args) if step.args else ""
            label = f"▷ {step.target}" + (f", {args_text}" if args_text else "")
            return (
                '<div class="ns-node ns-macro">'
                f'<div class="ns-label" aria-label="Macro {escape(step.target)}">'
                f'<code class="action-text">{escape(label)}</code>'
                "</div>"
                "</div>"
            )
        if isinstance(step, IfdefFlowStep):
            header = f"# {step.kind} {step.condition}".rstrip()
            body_html = self._render_sequence(step.body_steps, depth=depth + 1)
            # ELSEIF branches
            elseif_html = ""
            for elif_kind, elif_cond, elif_steps in step.branches:
                elif_header = f"# ELSEIF {elif_cond}".rstrip()
                elseif_html += (
                    f'<div class="ns-ifdef-branch">'
                    f"{self._render_header(elif_header)}"
                    f"{self._render_sequence(elif_steps, depth=depth + 1)}"
                    "</div>"
                )
            # ELSE branch
            else_html = ""
            if step.else_steps:
                else_html = (
                    f'<div class="ns-ifdef-branch">'
                    f"{self._render_header('# ELSE')}"
                    f"{self._render_sequence(step.else_steps, depth=depth + 1)}"
                    "</div>"
                )
            return (
                '<div class="ns-node ns-ifdef">'
                f"{self._render_header(header)}"
                f"{body_html}"
                f"{elseif_html}"
                f"{else_html}"
                "</div>"
            )
        if isinstance(step, AlignFlowStep):
            return (
                f'<div class="ns-align-marker" aria-label="Align {step.boundary}">⊞ ALIGN {step.boundary}</div>'
            )
        if isinstance(step, LabelFlowStep):
            return (
                f'<div class="ns-label-marker" aria-label="Label {escape(step.name)}">'
                f"{escape(step.name)}:"
                "</div>"
            )
        if isinstance(step, RepeatStringFlowStep):
            label = f"⊛ {step.prefix.upper()} {step.instruction.lower()}"
            return (
                '<div class="ns-node ns-repeat">'
                f'<div class="ns-header" aria-label="{escape(label)}">{escape(label)}</div>'
                "</div>"
            )
        raise TypeError(f"unsupported step type: {type(step)!r}")

    def _render_single_body(
        self,
        title: str,
        steps: tuple[ControlFlowStep, ...],
        *,
        depth: int,
        css_class: str = "ns-loop",
    ) -> str:
        return (
            f'<div class="ns-node {css_class}">'
            f"{self._render_header(title)}"
            f"{self._render_sequence(steps, depth=depth + 1)}"
            "</div>"
        )

    def _render_header(self, title: str) -> str:
        escaped = escape(title)
        return f'<div class="ns-header" aria-label="{escaped}">{escaped}</div>'

    def _if_cap_geometry(self, condition: str, badge: str) -> tuple[int, int, int, int, int]:
        text = f"{badge} {condition}".strip()
        char_count = max(len(text), 12)
        tokens = [token for token in re.split(r"\s+", text) if token]
        longest_token = max((len(token) for token in tokens), default=char_count)

        content_width = max(
            360,
            min(
                1600,
                max(longest_token * 8 + 48, ceil(char_count / 2) * 7 + 64),
            ),
        )
        svg_width = content_width + 40
        chars_per_line = max(18, int(content_width / 7.4))
        line_count = max(
            1,
            ceil(char_count / chars_per_line),
            ceil(longest_token / chars_per_line),
        )
        text_height = 24 + (line_count - 1) * 17
        split_y = 18 + text_height
        svg_height = split_y + 30
        return svg_width, svg_height, content_width, text_height, split_y

    def _render_if_cap(self, condition: str, *, depth: int = 0) -> str:
        escaped = escape(condition)
        d = min(depth, 50)
        badge = self._depth_badge(d)
        svg_width, svg_height, content_width, text_height, split_y = self._if_cap_geometry(
            condition,
            badge,
        )
        half_width = svg_width / 2
        yes_x = svg_width / 4
        no_x = svg_width * 0.75
        label_y = svg_height - 8

        return (
            f'<div class="ns-if-cap ns-if-depth-{d}" aria-label="If {escaped}">'
            f'<svg class="ns-if-svg" viewBox="0 0 {svg_width} {svg_height}" '
            f'width="{svg_width}" height="{svg_height}" preserveAspectRatio="xMidYMid meet">'
            f'<polygon points="0,0 {svg_width},0 {half_width},{split_y}" '
            f'class="ns-if-triangle ns-if-depth-{d}-triangle"/>'
            f'<foreignObject x="20" y="6" width="{content_width}" height="{text_height}" '
            'class="ns-if-condition-fo">'
            f'<div xmlns="http://www.w3.org/1999/xhtml" class="ns-if-condition-text">{badge} {escaped}</div>'
            '</foreignObject>'
            f'<line x1="0" y1="{split_y}" x2="{half_width}" y2="{svg_height}" '
            f'class="ns-if-diagonal ns-if-depth-{d}-diagonal"/>'
            f'<line x1="{svg_width}" y1="{split_y}" x2="{half_width}" y2="{svg_height}" '
            f'class="ns-if-diagonal ns-if-depth-{d}-diagonal"/>'
            f'<text x="{yes_x}" y="{label_y}" text-anchor="middle" class="ns-if-label-yes">Yes</text>'
            f'<text x="{no_x}" y="{label_y}" text-anchor="middle" class="ns-if-label-no">No</text>'
            '</svg>'
            "</div>"
        )

    def _render_switch(self, step: SwitchFlowStep, *, depth: int) -> str:
        case_count = len(step.cases)
        if case_count == 0:
            return (
                '<div class="ns-node ns-switch">'
                f"{self._render_header(f'⎇ Switch {step.expression}')}"
                '<div class="empty">No cases.</div>'
                "</div>"
            )

        # Build case columns with values on top, bodies below
        cases_html = []
        for case in step.cases:
            label = self._normalize_case_label(case.label.strip())
            cases_html.append(
                f'<div class="ns-switch-case-col" aria-label="{escape(label)}">'
                f'<div class="ns-switch-case-value">{escape(label)}</div>'
                f'<div class="ns-switch-case-body">{self._render_sequence(case.steps, depth=depth + 1)}</div>'
                "</div>"
            )

        d = min(depth, 50)
        badge = self._depth_badge(d)

        return (
            f'<div class="ns-node ns-switch ns-if-depth-{d}">'
            f'<div class="ns-switch-header">{badge} ⎇ switch {escape(step.expression)}</div>'
            f'<div class="ns-switch-cases">{"".join(cases_html)}</div>'
            "</div>"
        )

    def _render_footer(self, title: str) -> str:
        escaped = escape(title)
        return f'<div class="ns-footer" aria-label="{escaped}">{escaped}</div>'

    def _render_case_title(self, label: str) -> str:
        text = self._normalize_case_label(label.strip())
        escaped = escape(text)
        return f'<div class="case-title" aria-label="{escaped}">{escaped}</div>'

    def _normalize_case_label(self, label: str) -> str:
        compact = label.removesuffix(":").strip()
        if compact.startswith("default"):
            return "default"
        if compact.startswith("case "):
            return compact
        return compact
