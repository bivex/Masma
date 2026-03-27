# Requirements

## Functional Requirements

1. The system must parse a single `.asm` or `.inc` file.
2. The system must parse a directory recursively and ignore non-MASM files.
3. The system must return a versioned parse report for each source unit.
4. The system must aggregate file-level outcomes into one parsing job result.
5. The system must capture diagnostics with message, severity, line, and column.
6. The system must continue parsing other files when one file has diagnostics.
7. The system must extract a stable structural model containing at least includes, constants, variables, segments, structs, macros, procedures, and labels.
8. The system must expose parser version and report schema version in the result contract.
9. The system must distinguish successful parsing, parsing with diagnostics, and technical failure.
10. The CLI must return machine-readable JSON for parse workflows.
11. The system must extract structured control flow for MASM procedures using `.IF/.ELSEIF/.ELSE/.ENDIF`, `.WHILE/.ENDW`, `.REPEAT/.UNTIL`, and common `cmp/test + jcc/jmp + label` patterns.
12. The system must build an HTML Nassi-Shneiderman diagram for a single MASM file.
13. The system must build a directory bundle of diagrams and an index page.
14. Diagram metadata must expose source location, procedure count, and procedure names.

## Non-Functional Requirements

### Maintainability

* keep domain and application layers independent from parsing strategy, filesystem, HTML rendering, and CLI code
* keep adapters small and explicit
* use constructor injection and stable DTO contracts

### Testability

* cover domain rules with unit tests
* cover MASM parsing behavior with boundary tests
* cover diagram generation at HTML contract level

### Resilience

* isolate file failures from the rest of a parsing job
* surface unsupported or unbalanced MASM constructs as diagnostics
* keep diagram generation failures explicit

### Security

* do not execute parsed source
* do not perform hidden network calls during parsing or diagram generation

## Constraints and Honesty

Masma is a structured MASM analyzer, not a full assembler implementation. It is strongest on code that uses MASM high-level directives and conservative line-oriented syntax. When the tool cannot infer compiler-grade meaning, the contract must expose that limitation instead of hiding it.
