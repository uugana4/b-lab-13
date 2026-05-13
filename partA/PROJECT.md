# PROJECT.md

## Project Title
Personal Task Tracker (Option 2)

## Brief
This project is a small task management system focused on practical productivity needs:
creating tasks, tracking due dates, assigning priorities/labels, and searching/filtering tasks quickly.

## Problem Statement
Students and individual users often keep tasks in scattered notes. Without priority and due-date structure,
important tasks are missed and follow-up is inconsistent.

## Scope
### In Scope (Core Features)
1. Task CRUD (create, read/list, update, delete)
2. Due date support (`YYYY-MM-DD`)
3. Priority support (`low`, `medium`, `high`)
4. Label tagging and label-based filtering
5. Text search and combined filtering (status/priority/label/query)

### Out of Scope
- Multi-user authentication
- Cloud sync and external integrations
- Complex recurring schedule rules
- Frontend web UI (Part B focuses on robust backend logic + tests)

## Success Criteria
- At least 3 core features are implemented and verifiably working.
- At least 10 unit tests pass.
- Documentation and AI collaboration evidence are complete for Part A/B/C.

## Risks and Mitigations
- **Risk:** Invalid date/priority inputs cause inconsistent data.  
  **Mitigation:** strict validation and explicit exceptions.
- **Risk:** Search/filter behavior becomes ambiguous.  
  **Mitigation:** deterministic filter order and test coverage for combined filters.
- **Risk:** Over-reliance on AI suggestions.  
  **Mitigation:** verify with manual review, tests, and reflection logs.
