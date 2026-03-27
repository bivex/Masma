# Architecture

Masma is a layered monolith with hexagonal boundaries.

## Layers

* `domain`
  Defines the core model, ports, errors, and events.
* `application`
  Orchestrates parse-report and diagram use cases.
* `infrastructure`
  Implements the MASM parser, control-flow extractor, filesystem repository, HTML renderer, and logging.
* `presentation`
  Exposes the CLI commands and JSON contract.

## Main Flow

1. The CLI loads a file or directory command.
2. `FileSystemSourceRepository` returns `SourceUnit` values.
3. `ParsingJobService` calls the `SyntaxParser` port and maps outcomes to DTOs.
4. `NassiDiagramService` calls the `ControlFlowExtractor` port and passes diagrams to `NassiDiagramRenderer`.
5. The CLI prints JSON and optionally writes HTML files.

## Architectural Rules

* the domain must not depend on filesystem, CLI, or HTML concerns
* parsing strategy stays behind a port
* diagram rendering stays behind a port
* adapters may evolve without breaking stable application contracts
