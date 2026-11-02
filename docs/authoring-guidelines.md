# Authoring skills

Use the [Agent Skills specification](https://agentskills.io/specification). Every package needs YAML frontmatter with a unique lowercase hyphenated `name` matching its directory and a concise `description` explaining when it applies. Keep the entrypoint below 500 lines.

Write focused procedures with observable outcomes, failure handling and clear authorization boundaries. Existing user authorization persists; do not add repeated approval gates for already requested actions. Keep model names, proprietary tool syntax and personal infrastructure out of portable instructions.

Put conditional detail in linked `references/`, reproducible helpers in `scripts/`, reusable templates in `assets/`, and behavioral scenarios in `evals/cases.json`. Create directories only when used. References and templates must work when the package is installed by itself.

Verify command examples against official documentation and installed help. Record version limits instead of inventing flags. Helpers must document dependencies, avoid secret output, handle failures and be executable. Do not run mutations in validation.

Evaluation cases use `id`, `request`, `expected_behavior` (a nonempty list) and optional `should_trigger` (boolean). Cases guide manual behavioral evaluation; structural validation is not proof of agent behavior.
