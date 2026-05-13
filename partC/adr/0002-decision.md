# ADR-0002: Keep In-Memory Storage Instead of File/DB Persistence

## Status
Accepted

## Context
During Part B implementation, we considered adding JSON-file persistence.
The project requirements prioritize:
- 3-5 working features
- >=10 reliable unit tests
- AI workflow traceability and reflection quality

Adding persistence would increase complexity (I/O failures, migration concerns, state reset strategy) and reduce time for required reflection artifacts.

## Decision
Use **in-memory storage** for the current assignment version.

## Considered Alternatives
1. In-memory storage only
2. JSON file persistence
3. SQLite persistence

## Rationale
- In-memory approach keeps business logic clear and test-friendly.
- Fewer moving parts improves reliability for required feature/test threshold.
- Assignment grading does not require deployment-grade persistence.
- Reflection and verification quality get more time.

## Consequences
### Positive
- Faster implementation and debugging.
- Deterministic tests without file cleanup complexity.
- Reduced risk of accidental data corruption bugs.

### Negative
- Data is lost on process restart.
- Not suitable for real multi-session production use.

## Follow-up
If extended beyond Lab 13, next step is adding a repository interface and optional SQLite adapter while preserving existing tests.
