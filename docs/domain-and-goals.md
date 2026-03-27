# Domain And Goals

Masma exists to turn MASM source files into two stable outputs:

1. a structural parse report for downstream tooling
2. a control-flow diagram for human inspection

## Primary Goals

* parse MASM source in a repeatable, automatable way
* extract structural elements that matter for code inventory and review
* extract structured procedure flow from MASM high-level directives
* keep parsing, rendering, and delivery concerns outside the domain core

## In Scope

* reading `.asm` and `.inc` files
* extracting includes, constants, variables, segments, structs, macros, procedures, and labels
* building structured diagrams from MASM procedures
* returning machine-readable JSON from the CLI

## Out Of Scope

* assembling or executing source code
* macro expansion semantics
* full jump-graph reconstruction for arbitrary label-and-branch programs
* binary generation

## Core Domain Concepts

* `SourceUnit`: one MASM source file with identity, location, and content
* `ParseOutcome`: the structural result for one source unit
* `ParsingJob`: a multi-file parsing run
* `ControlFlowDiagram`: the diagram model for one file
* `FunctionControlFlow`: one MASM procedure rendered as a Nassi-Shneiderman block
