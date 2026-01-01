<!--
Sync Impact Report:
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All principles and sections added for Command-line Todo Application
Removed sections: N/A
Templates requiring updates: N/A (new constitution created)
Follow-up TODOs: None
-->
# Command-line Todo Application Constitution

## Core Principles

### NO manual coding by the user
All code generated through specs and tasks; No manual coding by the user; Follow clean code principles; Modular Python project structure

### Explicit separation of concerns
Clear separation between UI, services, storage, and models; Rich must be used for all terminal output; Questionary must be used for all user input

### In-memory storage only
No database, no file persistence; In-memory storage only; Use Rich for terminal output; Use Questionary for user input

### Spec-Driven Development
Write specification first; Generate implementation plan; Break plan into atomic tasks; Implement each task sequentially; Maintain specs history

### Clean Architecture
Modular Python project structure; Explicit separation of concerns (UI, services, storage, models); Use Rich and Questionary libraries as required

### Dependency Management
Python version >= 3.12+; Use UV for dependency management; CLI must run cleanly via `python -m todo_cli`

## Technology Requirements
Python version >= 3.12+; Use Rich for terminal output; Use Questionary for user input; Use UV for dependency management; CLI must run via `python -m todo_cli`

## Development Workflow
Write specification first; Generate implementation plan; Break plan into atomic tasks; Implement each task sequentially; Maintain specs history; Ask no questions unless specification is ambiguous

## Governance
All code must follow clean code principles; Modular Python structure required; In-memory storage only (no persistence); Use Rich and Questionary as specified; Follow Spec-Driven Development workflow

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
