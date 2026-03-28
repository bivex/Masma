"""Shared helpers for MASM source scanning."""

from __future__ import annotations

from dataclasses import dataclass
import re

from masma.domain.model import DiagnosticSeverity, SyntaxDiagnostic


_NAME = r"[A-Za-z_.$?@][\w.$?@]*"
_COMMENT_MARKER = ";"
_WHITESPACE_RE = re.compile(r"\s+")

INCLUDE_RE = re.compile(r"^(?P<kind>include|includelib)\s+(?P<target>.+)$", re.IGNORECASE)
EQU_RE = re.compile(rf"^(?P<name>{_NAME})\s+equ\b(?P<value>.*)$", re.IGNORECASE)
PROC_RE = re.compile(rf"^(?P<name>{_NAME})\s+proc\b(?P<tail>.*)$", re.IGNORECASE)
ENDP_RE = re.compile(rf"^(?P<name>{_NAME})\s+endp\b$", re.IGNORECASE)
STRUCT_RE = re.compile(rf"^(?P<name>{_NAME})\s+struct\b$", re.IGNORECASE)
ENDS_RE = re.compile(rf"^(?P<name>{_NAME})\s+ends\b$", re.IGNORECASE)
MACRO_RE = re.compile(rf"^(?P<name>{_NAME})\s+macro\b(?P<tail>.*)$", re.IGNORECASE)
ENDM_RE = re.compile(r"^endm\b$", re.IGNORECASE)
# Assembly-time conditional directives (no leading dot, unlike runtime .IF/.ENDIF)
COND_ASSEMBLE_RE = re.compile(
    r"^(?:ifdef|ifndef|ifdif|ifdifi|ifidn|ifidni|ifb|ifnb|if)\b",
    re.IGNORECASE,
)
COND_ASSEMBLE_PARSE_RE = re.compile(
    r"^(?P<kind>ifdef|ifndef|ifdif|ifdifi|ifidn|ifidni|ifb|ifnb|if)\s*(?P<condition>.*)$",
    re.IGNORECASE,
)
ENDIF_BARE_RE = re.compile(r"^endif\b", re.IGNORECASE)
LABEL_RE = re.compile(rf"^(?P<name>{_NAME}):$", re.IGNORECASE)
SEGMENT_RE = re.compile(
    r"^(?P<name>\.(?:code|const|data\??)|[A-Za-z_.$?@][\w.$?@]*)\s+(?P<kind>segment)\b|^(?P<directive>\.(?:code|const|data\??))\b",
    re.IGNORECASE,
)
VARIABLE_RE = re.compile(
    rf"^(?P<name>{_NAME})\s+(?P<type>db|dw|dd|dq|dt|df|byte|word|dword|qword|tbyte|real4|real8|real10)\b(?P<tail>.*)$",
    re.IGNORECASE,
)
IF_RE = re.compile(r"^\.if\b(?P<condition>.*)$", re.IGNORECASE)
ELSEIF_RE = re.compile(r"^\.elseif\b(?P<condition>.*)$", re.IGNORECASE)
ELSE_RE = re.compile(r"^\.else\b$", re.IGNORECASE)
ENDIF_RE = re.compile(r"^\.endif\b$", re.IGNORECASE)
WHILE_RE = re.compile(r"^\.while\b(?P<condition>.*)$", re.IGNORECASE)
ENDW_RE = re.compile(r"^\.endw\b$", re.IGNORECASE)
REPEAT_RE = re.compile(r"^\.repeat\b$", re.IGNORECASE)
UNTIL_RE = re.compile(r"^\.(?P<kind>until|untilcxz)\b(?P<condition>.*)$", re.IGNORECASE)

DATA_DIRECTIVES = {".data", ".data?", ".const"}
CODE_DIRECTIVES = {".code"}
IGNORED_ACTION_DIRECTIVES = {
    ".code",
    ".data",
    ".data?",
    ".const",
    ".stack",
    ".model",
    "option",
    "assume",
    "end",
}


@dataclass(frozen=True, slots=True)
class SourceLine:
    number: int
    raw: str
    text: str

    @property
    def upper(self) -> str:
        return self.text.upper()


@dataclass(frozen=True, slots=True)
class ProcedureBlock:
    name: str
    signature: str
    line: int
    body_lines: tuple[SourceLine, ...]


def extract_file_header(lines: tuple[SourceLine, ...]) -> str | None:
    """Return the leading comment block (consecutive ';' lines) as a single string.

    Blank lines at the top are skipped.  The first non-comment, non-blank line
    stops collection.  Returns *None* when there is no leading comment block.
    """
    comment_lines: list[str] = []
    for line in lines:
        stripped = line.raw.strip()
        if not stripped:
            if comment_lines:
                break
            continue
        if stripped.startswith(";"):
            comment_lines.append(stripped.lstrip(";").strip())
        else:
            break
    return "\n".join(comment_lines) if comment_lines else None


def iter_source_lines(source_text: str) -> tuple[SourceLine, ...]:
    lines: list[SourceLine] = []
    for number, raw_line in enumerate(source_text.splitlines(), start=1):
        text = _strip_comment(raw_line).strip()
        lines.append(SourceLine(number=number, raw=raw_line.rstrip(), text=text))
    return tuple(lines)


def compact_text(text: str, *, limit: int = 96) -> str:
    compact = _WHITESPACE_RE.sub(" ", text).strip()
    if len(compact) <= limit:
        return compact
    return f"{compact[: limit - 3].rstrip()}..."


def token_count(source_text: str) -> int:
    tokens = re.findall(r"[A-Za-z_.$?@][\w.$?@]*|0[0-9A-Fa-f]+h|\d+|[^\s]", source_text)
    return len(tokens)


def collect_syntax_diagnostics(lines: tuple[SourceLine, ...]) -> tuple[SyntaxDiagnostic, ...]:
    diagnostics: list[SyntaxDiagnostic] = []
    stack: list[tuple[str, str, int]] = []

    for line in lines:
        if not line.text:
            continue

        if proc_match := PROC_RE.match(line.text):
            stack.append(("PROC", proc_match.group("name"), line.number))
            continue

        if endp_match := ENDP_RE.match(line.text):
            if not stack or stack[-1][0] != "PROC":
                diagnostics.append(_error("ENDP without matching PROC", line.number))
                continue
            _, expected_name, _ = stack.pop()
            if expected_name.lower() != endp_match.group("name").lower():
                diagnostics.append(
                    _error(
                        f"ENDP closes '{endp_match.group('name')}' but '{expected_name}' is open",
                        line.number,
                    )
                )
            continue

        if struct_match := STRUCT_RE.match(line.text):
            stack.append(("STRUCT", struct_match.group("name"), line.number))
            continue

        if ends_match := ENDS_RE.match(line.text):
            if not stack or stack[-1][0] != "STRUCT":
                diagnostics.append(_error("ENDS without matching STRUCT", line.number))
                continue
            _, expected_name, _ = stack.pop()
            if expected_name.lower() != ends_match.group("name").lower():
                diagnostics.append(
                    _error(
                        f"ENDS closes '{ends_match.group('name')}' but '{expected_name}' is open",
                        line.number,
                    )
                )
            continue

        if macro_match := MACRO_RE.match(line.text):
            stack.append(("MACRO", macro_match.group("name"), line.number))
            continue

        if ENDM_RE.match(line.text):
            if not stack or stack[-1][0] != "MACRO":
                diagnostics.append(_error("ENDM without matching MACRO", line.number))
                continue
            stack.pop()
            continue

        if IF_RE.match(line.text):
            stack.append(("IF", ".IF", line.number))
            continue

        if ELSEIF_RE.match(line.text) or ELSE_RE.match(line.text):
            if not stack or stack[-1][0] != "IF":
                diagnostics.append(_error(f"{line.text.split()[0]} without matching .IF", line.number))
            continue

        if ENDIF_RE.match(line.text):
            if not stack or stack[-1][0] != "IF":
                diagnostics.append(_error(".ENDIF without matching .IF", line.number))
                continue
            stack.pop()
            continue

        if WHILE_RE.match(line.text):
            stack.append(("WHILE", ".WHILE", line.number))
            continue

        if ENDW_RE.match(line.text):
            if not stack or stack[-1][0] != "WHILE":
                diagnostics.append(_error(".ENDW without matching .WHILE", line.number))
                continue
            stack.pop()
            continue

        if REPEAT_RE.match(line.text):
            stack.append(("REPEAT", ".REPEAT", line.number))
            continue

        if UNTIL_RE.match(line.text):
            if not stack or stack[-1][0] != "REPEAT":
                diagnostics.append(_error(".UNTIL without matching .REPEAT", line.number))
                continue
            stack.pop()

    for kind, name, line_number in reversed(stack):
        diagnostics.append(_error(f"{kind} '{name}' is not closed", line_number))

    return tuple(diagnostics)


def scan_procedure_blocks(lines: tuple[SourceLine, ...]) -> tuple[ProcedureBlock, ...]:
    procedures: list[ProcedureBlock] = []
    current_name: str | None = None
    current_signature = ""
    current_line = 0
    body: list[SourceLine] = []

    for line in lines:
        if current_name is None:
            proc_match = PROC_RE.match(line.text)
            if proc_match is None:
                continue
            current_name = proc_match.group("name")
            current_signature = compact_text(line.text, limit=140)
            current_line = line.number
            body = []
            continue

        endp_match = ENDP_RE.match(line.text)
        if endp_match and endp_match.group("name").lower() == current_name.lower():
            procedures.append(
                ProcedureBlock(
                    name=current_name,
                    signature=current_signature,
                    line=current_line,
                    body_lines=tuple(body),
                )
            )
            current_name = None
            current_signature = ""
            current_line = 0
            body = []
            continue

        body.append(line)

    if current_name is not None:
        procedures.append(
            ProcedureBlock(
                name=current_name,
                signature=current_signature,
                line=current_line,
                body_lines=tuple(body),
            )
        )

    return tuple(procedures)


def is_data_directive(line: SourceLine) -> bool:
    return line.text.lower() in DATA_DIRECTIVES


def is_code_directive(line: SourceLine) -> bool:
    return line.text.lower() in CODE_DIRECTIVES


def classify_segment(line: SourceLine) -> str | None:
    match = SEGMENT_RE.match(line.text)
    if match is None:
        return None
    if match.group("directive"):
        return match.group("directive")
    return match.group("name")


def _strip_comment(line: str) -> str:
    in_string = False
    result: list[str] = []
    for char in line:
        if char == '"':
            in_string = not in_string
        if char == _COMMENT_MARKER and not in_string:
            break
        result.append(char)
    return "".join(result)


def _error(message: str, line: int) -> SyntaxDiagnostic:
    return SyntaxDiagnostic(
        severity=DiagnosticSeverity.ERROR,
        message=message,
        line=line,
        column=1,
    )
