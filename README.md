# Masma

**Masma** is a Python tool for parsing x86 MASM assembly source files, extracting structured control flow, and generating interactive [Nassi-Shneiderman diagrams](https://en.wikipedia.org/wiki/Nassi%E2%80%93Shneiderman_diagram) as standalone HTML pages.

Designed for reverse engineers, malware analysts, and assembly programmers who need to quickly understand the logic flow of complex x86 MASM procedures.

## What it does

- **Parses** `.asm`, `.inc`, and `.mac` MASM source files
- **Extracts** structured control flow from MASM procedures
- **Recovers** unstructured jump-based flow (if/else, loops, switch chains) from raw `cmp/jcc` patterns
- **Renders** Nassi-Shneiderman block diagrams as standalone HTML with syntax-colored blocks
- **Reports** structural elements: procedures, macros, structs, unions, type aliases, constants, variables, externals, publics
- **Diagnoses** unbalanced `PROC/ENDP`, `STRUCT/ENDS`, `MACRO/ENDM`, and structured directives

## Screenshots

**Nassi-Shneiderman diagram** — all control-flow step types rendered from `feature_tour.asm`:

![Masma Nassi diagram](docs/screenshots/feature_nassi.png)

## Quick Start

```bash
# Install
uv sync --extra dev

# Parse a single MASM file
uv run masma parse-file path/to/program.asm

# Generate a Nassi-Shneiderman HTML diagram
uv run masma nassi-file path/to/program.asm --out output/program.html

# Process an entire directory
uv run masma nassi-dir path/to/project --out output/bundle/
```

## Control Flow Step Types

| Step type | Visual | Source construct |
|---|---|---|
| `ActionFlowStep` | plain block | straight-line instructions; `ret` highlighted |
| `IfFlowStep` | triangle split | `.IF/.ELSEIF/.ELSE/.ENDIF`; recovered `cmp/test + jcc` |
| `WhileFlowStep` | ↻ | `.WHILE/.ENDW`; recovered top-tested `cmp/jcc + jmp` loop |
| `RepeatWhileFlowStep` | ↺ | `.REPEAT/.UNTIL` / `.UNTILCXZ`; recovered bottom-tested loop |
| `SwitchFlowStep` | ⎇ | recovered 2+ `cmp reg, val + je label` chains on same register |
| `ForInFlowStep` | ∀ | MASM `loop label` (ECX-counted) |
| `InvokeFlowStep` | ⇒ | MASM `INVOKE proc, args` |
| `CallFlowStep` | ⇒ | direct `call proc` |
| `MacroCallFlowStep` | ▷ | user-defined macro calls (`NAME MACRO … ENDM`) |
| `RepeatStringFlowStep` | ⊛ | `REP`/`REPE`/`REPNE` string instructions |
| `JumpFlowStep` | ↪ / ⇒ | standalone conditional (amber) or unconditional (red) jumps not forming a structured block; supports all x86 `jcc`, indirect `jmp reg`, `jmp [mem]`, `jmpf` |
| `LocalDeclFlowStep` | ≡ | stack-frame local variable aliases (`name EQU [bp−n]`) |
| `LabelFlowStep` | — ruler — | standalone `name:` labels as visual separator markers |
| `IfdefFlowStep` | `# IFDEF …` | assembly-time `IFDEF`/`IFNDEF`/`IF`/`ELSEIF*`/`ELSE`/`ENDIF` |
| `StackFlowStep` | ↓↑ | `push`/`pop` with live stack depth badge |
| `AlignFlowStep` | ⊟ | `ALIGN n` directives |

## Supported MASM Constructs

**File-level declarations:**
`INCLUDE`/`INCLUDELIB`, `EXTERN`/`EXTERNDEF`, `PUBLIC`, `TYPEDEF`, `EQU`, `SEGMENT/ENDS`, `.data`/`.data?`/`.const`/`.code`

**Type definitions:**
`STRUCT/ENDS` (with field extraction, `container=StructName`), `UNION/ENDS` (same)

**Procedures & macros:**
`PROC/ENDP`, `MACRO/ENDM`, `FOR`/`FORC`/`IRP`/`IRPC`/`REPT`/`WHILE` macro loops

**Structured flow directives:**
`.IF`/`.ELSEIF`/`.ELSE`/`.ENDIF`, `.WHILE`/`.ENDW`, `.REPEAT`/`.UNTIL`/`.UNTILCXZ`

**Assembly-time conditionals (full set):**
`IFDEF`, `IFNDEF`, `IFDIF`, `IFDIFI`, `IFIDN`, `IFIDNI`, `IFB`, `IFNB`, `IF1`, `IF2`, `IF` + all `ELSEIF*` variants (`ELSEIFDEF`, `ELSEIFNDEF`, `ELSEIFDIF`, `ELSEIFDIFI`, `ELSEIFIDN`, `ELSEIFIDNI`, `ELSEIFB`, `ELSEIFNB`, `ELSEIF1`, `ELSEIF2`)

**All x86 conditional jumps:**
`je/jz`, `jne/jnz`, `jg/jnle`, `jge/jnl`, `jl/jnge`, `jle/jng`, `ja/jnbe`, `jae/jnb`, `jb/jnae`, `jbe/jna`, `jo`, `jno`, `js`, `jns`, `jp/jpe`, `jnp/jpo`, `jcxz`, `jecxz`, `jrcxz` + indirect `jmp reg` / `jmp [mem]` / `jmpf`

## Architecture

Hexagonal (ports & adapters) with four layers:

```
domain/          — model, ports, invariants (no dependencies)
application/     — parse-report and diagram use cases
infrastructure/  — MASM parser, ANTLR backend, renderer, filesystem
presentation/    — CLI (argparse)
```

The ANTLR-backed parser uses a patched grammar (`resources/grammars/masm/patched/Masm.g4`) derived from the upstream [`grammars-v4`](https://github.com/antlr/grammars-v4/tree/master/asm/masm) MASM grammar, extended with `EXTERN/EXTERNDEF/PUBLIC`, full `ELSEIF*` variants, `TYPEDEF`, `UNION`, `ALIGN/ASSUME/OPTION/ORG/EVEN`, and an `anyKeyword` rule that allows reserved words as instruction operands.

Regenerate after grammar changes:

```bash
uv run python scripts/generate_masm_parser.py
```

## Testing

```bash
uv run pytest
```

## Scope and limitations

Masma is a **source-level static analyzer**, not a full assembler or disassembler. It does not:
- resolve `INCLUDE` chains or expand macros
- recover arbitrary jump graphs (spaghetti code produces `JumpFlowStep` nodes, not structured blocks)
- parse binary executables — input must be MASM `.asm`/`.inc` source

The strongest diagram output comes from MASM code that uses structured directives (`.IF`, `.WHILE`, etc.).

---

## Keywords

x86 assembly · MASM · Microsoft Macro Assembler · Nassi-Shneiderman diagram · structured flowchart · control flow graph · reverse engineering · malware analysis · static analysis · assembly visualization · x86 disassembly · ANTLR grammar · assembly parser · code structure · flow diagram · assembly code analyzer · IDA Pro alternative · assembly documentation · win32 assembly · DOS assembly · 16-bit assembly · 32-bit assembly
