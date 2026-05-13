# ADR-0001: Choose Python Standard Library Stack

## Status
Accepted

## Context
Lab 13 requires:
- 3+ working features
- >=10 unit tests
- strong documentation and AI-collaboration evidence
- limited time (2 weeks)

We need a stack that enables fast iteration and reliable tests with minimal setup friction.

## Options Considered
1. Python + standard library (`unittest`)
2. Node.js + Express + Jest
3. Java + Spring Boot + JUnit

## Decision
Use **Python + standard library** for the Part B implementation.

## Rationale
- Lowest setup complexity and dependency overhead.
- Fastest path to high-quality unit tests.
- Keeps attention on assignment goals: workflow, verification, and reflection.
- Easy for deterministic logic and edge-case coverage.

## Consequences
### Positive
- Rapid development and testing.
- Lower risk of environment/dependency failures.
- Cleaner audit trail for AI-assisted development.

### Negative
- Not a full production web stack by default.
- If API surface is needed later, additional tooling may be required.
