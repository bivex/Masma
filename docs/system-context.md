# System Context

Masma owns the flow from MASM source input to two output families:

* structural parse reports
* Nassi-Shneiderman HTML diagrams

## External Actors

* developers inspecting MASM codebases
* CI jobs validating or cataloging assembly sources
* downstream tooling consuming JSON reports

## External Dependencies

* the local filesystem that stores MASM input files and generated artifacts
* the Python runtime and CLI invocation environment

## Boundaries

Masma owns:

* source discovery
* structural parsing
* structured control-flow extraction
* HTML diagram rendering
* CLI response formatting

Masma does not own:

* MASM assembly or linking
* executable semantics
* include resolution outside the provided source text
* authoritative meaning of arbitrary jump graphs
