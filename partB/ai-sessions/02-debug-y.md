# Session 02 - Debug and Edge Case Review

## Objective
Harden input validation and test failure paths.

## AI Assistance
- Highlighted potential inconsistencies around date format and empty title handling.
- Suggested adding tests for invalid priorities and missing task IDs.

## Human Verification
- Added tests for invalid due date format and invalid priority.
- Confirmed `KeyError` for missing IDs in `get_task` and `delete_task`.

## Result
- Error paths are now explicit and covered by tests.
