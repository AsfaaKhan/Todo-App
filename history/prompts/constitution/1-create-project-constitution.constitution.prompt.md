---
id: 1
title: Create Project Constitution
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: Claude
command: /sp.constitution
labels: [constitution, setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```
/sp.constitution

You are Claude Code operating under Spec-Kit Plus.

Project: Command-line Todo Application

Core Principles:
- NO manual coding by the user
- All code generated through specs and tasks
- Follow clean code principles
- Modular Python project structure
- Explicit separation of concerns (UI, services, storage, models)
- Rich must be used for all terminal output
- Questionary must be used for all user input
- In-memory storage only (no database, no file persistence)

Development Workflow:
1. Write specification
2. Generate implementation plan
3. Break plan into atomic tasks
4. Implement each task sequentially
5. Maintain specs history

Rules:
- Ask no questions unless specification is ambiguous
- CLI must run cleanly via `python -m todo_cli`
- Python version >= 3.12+
- Use UV for dependency management
```

## Response snapshot

Updated the constitution template with project-specific values for the Command-line Todo Application, establishing core principles, technology requirements, and development workflow as specified in the user requirements.

## Outcome

- ✅ Impact: Created project constitution establishing governance principles
- 🧪 Tests: N/A
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Generate spec, plan, and tasks for the todo application
- 🧠 Reflection: Constitution successfully established foundational principles for the project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A