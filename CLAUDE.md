# CLAUDE.md

Project: F.CSM311 Lab 13 - Personal Task Tracker

## Purpose
This file defines how AI assistants should collaborate in this repository with predictable quality, safety, and traceability.

## Build Commands
- Run tests:
  - `cd partB && python3 -m unittest discover -s tests -p "test_*.py" -v`
- Run a quick module check:
  - `cd partB && python3 -m py_compile src/task_tracker.py`
- Optional local usage:
  - `cd partB && python3 src/task_tracker.py`

## Repository Conventions
- Keep the required assignment structure unchanged:
  - `partA/`, `partB/`, `partC/`, `.claude/commands/`
- Keep Part A as planning documents only (no production code).
- Keep Part C as reflection and evidence only.
- Place all implementation code in `partB/src/`.
- Place all tests in `partB/tests/`.
- Use clear English identifiers in source code.
- Documentation can be Mongolian/English mixed for course readability.

## Coding Conventions
- Prefer small, pure functions for filtering/search logic.
- Validate input in public APIs.
- Raise explicit exceptions for invalid task operations.
- Avoid hidden side effects.
- Keep date format as ISO (`YYYY-MM-DD`).
- Keep priorities constrained to: `low`, `medium`, `high`.

## Testing Conventions
- Every new feature needs at least one direct unit test.
- Include edge-case tests (invalid date, missing task, empty filters).
- Keep tests deterministic and isolated.

## Security & Robustness Rules
- Never execute user-provided strings as code.
- Never use `eval`/`exec`.
- Sanitize and validate all inputs before storing.
- Do not trust AI-generated code blindly; verify behavior with tests.
- Avoid leaking internal stack traces in user-facing CLI output.

## No-Go Zones
- Do not change assignment-required folder names or filenames.
- Do not fabricate AI usage evidence; logs must reflect real sessions.
- Do not claim manual authorship for AI-generated content.
- Do not remove failing tests without replacement/fix rationale.
- Do not add unrelated dependencies without a clear reason.

## Git/Commit Guidance
- Use Conventional Commits: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`.
- Keep commits small and focused.
- For AI-assisted commits, include disclosure in commit body:
  - `Co-Authored-By: Claude <noreply@anthropic.com>`

## Slash Commands in this Repo
- `/review`: security + robustness check (OWASP mindset)
- `/test`: add/update tests for edge cases
- `/docs`: update docstrings and README sections
- `/commit`: propose conventional commit message
- `/security`: identify top risk points and mitigations

## Review Checklist Before Final Submission
- Required files all present.
- `python3 -m unittest ...` passes with >=10 tests.
- AI session logs present in Part A and Part B.
- Part C includes >=1500 words and required evidence sections.
