# Session 03 - Refactor and Test Expansion

## Objective
Improve maintainability and complete unit-test threshold.

## AI Assistance
- Recommended helper functions for due date/priority/labels validation.
- Proposed adding combined filter tests to reduce regression risk.

## Human Decisions
- Refactored with `_validate_due_date`, `_validate_priority`, `_normalize_labels`.
- Added tests for label+priority filtering and sorted listing.

## Result
- Cleaner code paths and >=10 passing unit tests.
