# Glossary

`Source Unit`
: One MASM source file treated as an addressable input with stable identity, location, and content.

`Parse Outcome`
: The structural result of parsing one source unit, including diagnostics and extracted elements.

`Structural Element`
: One extracted item such as an include, constant, variable, segment, struct, macro, procedure, or label.

`Control Flow Diagram`
: The structured representation of procedures extracted from one source file.

`Source Repository`
: The boundary that loads one file or enumerates MASM source files from a root path.

`Syntax Parser`
: The boundary that turns a `SourceUnit` into a `ParseOutcome`.

`Control Flow Extractor`
: The boundary that builds a `ControlFlowDiagram` from a `SourceUnit`.
