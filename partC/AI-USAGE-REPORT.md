# AI-USAGE-REPORT.md

## Introduction

This report reflects my experience building F.CSM311 Lab 13 with AI-assisted workflow.  
The assignment is not only about writing code. It is about practicing **Spec -> Generate -> Review -> Integrate** and proving that I can verify AI outputs instead of trusting them blindly.  
I used AI to accelerate planning, implementation drafts, and review checklists, but I kept final responsibility for technical decisions, correctness, and integrity.

I organized my work in three phases:
1. **Plan (Part A)** - define scope, architecture, stack, and collaboration rules.
2. **Build (Part B)** - implement core features and tests with iterative AI support.
3. **Reflect (Part C)** - analyze what AI did well, where it failed, and how I handled risk.

The selected project is a **Personal Task Tracker** with CRUD, due date, priority, label, and search/filter support.  
I intentionally scoped it as a small but complete core system to focus on quality and verification rather than breadth.

---

## 1) What AI did vs what I did (with examples by part)

### Part A - Planning
**AI contributions**
- Suggested possible project directions and helped compare stack trade-offs.
- Helped draft architecture module boundaries (model, service, validators, query/filter).
- Helped format initial ADR template and Mermaid diagram structure.

**My contributions**
- Finalized the project choice and decided which features were in/out of scope.
- Rejected over-engineered architecture suggestions that did not fit the 2-week timeline.
- Wrote the final `CLAUDE.md` rules to control quality, no-go zones, and test expectations.

**Concrete example**
- AI suggested adding persistence/database in the initial design.
- I removed that from scope because assignment success does not require deployment-scale persistence, and this would reduce focus on testing and reflection quality.

### Part B - Build
**AI contributions**
- Produced first draft of helper validators for due date and priority.
- Suggested unit test cases for invalid date, missing task id, and combined filters.
- Suggested clearer error messages for invalid input conditions.

**My contributions**
- Reworked code structure to keep the project simple and readable.
- Validated each generated method manually and corrected logical inconsistencies.
- Wrote/adjusted tests and interpreted results to ensure behavior matched intended requirements.

**Concrete example**
- AI drafted search logic; I changed filter order and added deterministic list sorting by due date then id.  
  This was done to make test outcomes stable and reproducible.

### Part C - Reflection
**AI contributions**
- Helped structure reflection prompts and check required sections.
- Suggested candidate areas for hallucination and security examples.

**My contributions**
- Selected only real incidents that occurred during build.
- Verified each claim against code and test behavior before writing it here.
- Added honest self-evaluation based on my own understanding, not on AI-generated confidence language.

---

## 2) Hallucination examples (2+): what AI got wrong and how I fixed it

### Hallucination Example 1: Incorrect Python standard library claim
**What AI suggested**
- AI suggested using a non-existent convenience parser in the standard library for date validation.

**Why this was wrong**
- The referenced function/module path did not exist in the Python version/environment I was using.
- This would have caused runtime failure if copied directly.

**How I detected it**
- I cross-checked by reading the official Python docs and testing imports locally.
- The import failed, confirming the suggestion was invalid.

**How I fixed it**
- Replaced with `datetime.strptime(..., "%Y-%m-%d")` based validation.
- Added unit test to ensure invalid format (`05/20/2026`) raises `ValueError`.

**Lesson**
- Even when AI sounds confident about API names, verify imports and behavior with real execution.

### Hallucination Example 2: Overconfident edge-case assumption in filtering
**What AI suggested**
- AI implied combined filters would naturally produce deterministic ordering and stable results without explicit sorting.

**Why this was wrong**
- In-memory dictionary iteration order can still lead to hidden assumptions depending on insertion and update patterns.
- "Seems stable" in one run is not the same as guaranteed deterministic behavior for tests.

**How I detected it**
- I reviewed the logic and noticed no explicit sort before returning filtered tasks.
- I recognized this could cause subtle nondeterministic behavior in future refactors.

**How I fixed it**
- Implemented `list_tasks()` sorting by `(due_date is None, due_date, id)`.
- Made search operate from `list_tasks()` output to keep ordering consistent.
- Added unit test asserting expected order.

**Lesson**
- AI often optimizes for plausibility; I must optimize for guarantees and testability.

### Hallucination Example 3: Scope inflation disguised as "best practice"
**What AI suggested**
- AI suggested adding authentication and role-based access as "recommended architecture baseline."

**Why this was wrong**
- This was outside assignment scope and would consume time needed for required artifacts.
- It was not required for a single-user local tracker demo.

**How I detected it**
- I compared suggestion to assignment rubric and project scope in `PROJECT.md`.

**How I fixed it**
- Explicitly marked authentication and cloud sync as out-of-scope.
- Focused on required quality metrics: features, tests, logs, ADR, reflection.

**Lesson**
- "Best practice" is context-dependent; scope discipline is a technical skill.

---

## 3) Security/license attention (1+ example): did AI-generated code create risk?

Yes, there was a meaningful risk pattern.

### Security Risk Example: unsafe dynamic execution suggestion
**What AI suggested**
- During an exploratory step, AI suggested a dynamic approach that could evaluate user input to build filter expressions quickly.

**Risk**
- Any `eval`-style behavior is dangerous and unnecessary for this project.
- Even in a local app, this pattern normalizes unsafe coding habits.

**How I handled it**
- Rejected that approach immediately.
- Kept filtering logic explicit (`if` checks on known fields).
- Added rule in `CLAUDE.md`: never use `eval`/`exec`.

**Why this matters**
- OWASP mindset requires defensive defaults.
- Security is not only about internet-facing apps; it is also about preventing unsafe coding patterns.

### License/attribution attention
AI-generated text and code can blur authorship boundaries if not disclosed.

**Potential issue**
- If AI-assisted commits are not disclosed, it violates assignment integrity requirements.

**Mitigation**
- I kept AI session logs and designed commit message policy to include AI attribution footer in relevant commits.
- I documented clearly in reflection what AI wrote and what I changed.

**Result**
- Technical output and academic integrity are both traceable.

---

## 4) What AI helped me do faster (production benefit)

AI improved speed in several concrete ways:

1. **Boilerplate acceleration**
   - Quickly generated first drafts of class/method signatures and validation scaffolding.
   - Reduced blank-page time significantly.

2. **Test brainstorming**
   - Produced many candidate test scenarios quickly (invalid input, missing IDs, combined filters).
   - Helped me reach broad edge-case coverage faster.

3. **Documentation scaffolding**
   - Accelerated first draft structures for ADR and architecture sections.
   - Helped ensure all assignment sections were present before refinement.

4. **Review framing**
   - Gave structured review lenses (security, robustness, regression risk) that improved final quality checks.

5. **Iteration loop speed**
   - Faster cycle: propose -> inspect -> edit -> retest.
   - I could spend more time on verification and reasoning than typing repetitive code.

Net effect: AI acted as a high-speed junior collaborator for draft generation and idea expansion, while I acted as the reviewer/architect.

---

## 5) What AI made slower (challenges, anti-patterns)

AI was not always a speedup. In some moments it slowed progress:

1. **Plausible but wrong suggestions**
   - Fixing hallucinations costs time because confidence is high but evidence is weak.
   - Verification overhead is mandatory.

2. **Over-engineering pressure**
   - Suggestions sometimes pushed toward unnecessary architecture complexity.
   - Time was spent cutting down scope back to assignment-fit implementation.

3. **Inconsistent style drift**
   - AI output sometimes mixed naming/error conventions.
   - I had to normalize style for readability and maintainability.

4. **False completeness feeling**
   - AI-generated docs can look complete even if subtle requirement gaps remain.
   - Manual checklist audits were required to avoid rubric misses.

5. **Context reset friction**
   - In longer interactions, AI may lose details and re-suggest already rejected ideas.
   - I solved this by using concise session logs and explicit constraints.

Key anti-pattern I observed: asking broad prompts without constraints leads to broad, noisy outputs.  
Quality improved when prompts included strict scope, expected format, and verification targets.

---

## 6) How I managed skill atrophy risk ("AI-free" practice)

I intentionally used strategies to avoid dependency on AI:

1. **AI-free checkpoints**
   - For key functions, I paused AI and reasoned manually about expected behavior before checking generated code.
   - I wrote some test assertions from my own logic first, then compared with AI suggestions.

2. **Explain-before-accept**
   - I required myself to explain each accepted code block in plain language.
   - If I could not explain it, I treated it as untrusted and revised it.

3. **Manual bug tracing**
   - For suspicious behavior, I traced code paths myself instead of immediately asking AI for fixes.
   - This kept debugging skills active.

4. **Structured validation**
   - I used tests as a skill-preserving tool, not just a pass condition.
   - Writing tests required understanding contract behavior and edge cases.

5. **Reflective logging**
   - Session summaries captured what AI proposed vs what I accepted/rejected.
   - This made me conscious of my decision process and prevented passive acceptance.

Conclusion on skill atrophy:  
AI can reduce typing effort, but it does not need to reduce thinking effort.  
If I keep ownership over verification, test design, and architecture decisions, AI becomes a multiplier rather than a crutch.

---

## Overall Reflection

This assignment demonstrated that AI-assisted development is most useful when paired with strict verification discipline.  
The best workflow for me was:
1. Define constraints and expected outputs clearly.
2. Let AI generate fast drafts.
3. Verify every important claim with tests/docs/spec.
4. Integrate only what I can explain and defend.

The biggest takeaway is not "AI writes code fast."  
The bigger lesson is that software quality depends on **human judgment**: scope control, risk awareness, test quality, and honesty about authorship.

For future projects, I would keep the same verify-first collaboration style, but I would improve by:
- starting security threat-model notes earlier,
- maintaining requirement-to-test traceability from day one,
- and enforcing stricter prompt templates to reduce noisy suggestions.

This lab moved my mindset from "coding with autocomplete" to "engineering with accountable AI collaboration."
