# STACK-COMPARISON.md

## Goal
Compare 3 viable stacks and choose 1 for fast, testable implementation of a Personal Task Tracker.

## Compared Stacks

### Stack A: Python + Standard Library (`unittest`, in-memory model)
**Pros**
- Fast setup, no external dependency required
- Very quick test authoring with built-in `unittest`
- Great for demonstrating logic correctness in a course setting

**Cons**
- Minimal built-in API scaffolding compared to full frameworks
- UI requires additional work if needed later

**Fit**
- Excellent for this assignment's focus on AI workflow, tests, and documentation.

---

### Stack B: Node.js + Express + Jest
**Pros**
- Familiar REST stack with rich ecosystem
- Easy to extend into web frontend

**Cons**
- More setup overhead (package config, lint, test tooling)
- Dependency management may consume time in a short assignment window

**Fit**
- Good if API/demo deployment is the primary goal, but heavier than needed now.

---

### Stack C: Java + Spring Boot + JUnit
**Pros**
- Strong architecture patterns for larger systems
- Mature test/story for enterprise-like services

**Cons**
- Highest setup and boilerplate overhead
- Slower iteration for a small two-week assignment

**Fit**
- Strong long-term stack, but overkill for this scope.

## Decision
**Selected: Stack A (Python + Standard Library).**

## Why this Choice
1. Minimizes setup friction and protects time for Part C reflection quality.
2. Enables fast unit test iteration (>=10 tests requirement).
3. Keeps the implementation transparent, making AI review and manual verification easier.
4. Reduces dependency/security surface for a small project.

## AI Planning Session Summary (Short)
- AI suggested Node.js and Python as top options.
- We prioritized reproducible tests and low setup overhead.
- We selected Python to focus on correctness, documentation, and verifiable workflow.
