# /review

Perform a security + robustness review of relevant code.

Focus order:
1. Security risks (OWASP-minded): input validation, injection-like patterns, data handling.
2. Behavioral regressions: logic changes that can break existing behavior.
3. Reliability: unhandled errors, weak edge-case handling, brittle assumptions.
4. Test gaps: missing tests for risky paths.

Output format:
- Findings first, ordered by severity.
- For each finding: file, risk, impact, recommendation.
- If no issues found, explicitly state that and list residual risks.
