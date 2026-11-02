---
name: implement-feature
description: Implement a scoped feature in an existing codebase. Use when adding behavior from requirements or an agreed technical plan.
---

# Implement feature

Read project instructions, the requested behavior and relevant code/tests. Establish observable acceptance criteria and inspect current behavior. Resolve routine implementation choices using existing project patterns; clarify missing requirements that materially change the result.

Implement a cohesive change, preserving unrelated user edits and existing public contracts unless a change is requested. Include failure handling at actual system boundaries and migrations when required. Avoid adding abstractions or dependencies without a concrete use.

Run the project checks appropriate to the changed behavior. Add regression coverage for meaningful new behavior and edge cases; distinguish existing failures from regressions. Review the diff for unintended changes and secrets.

Report the resulting behavior, validation evidence and remaining limitations. Commit, push or deploy only within the user's authorized scope.
