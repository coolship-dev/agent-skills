# Maintaining this repository

Follow `docs/authoring-guidelines.md` when editing skills. Canonical packages live at `skills/<category>/<name>/`; keep them portable across agents. Root instructions apply to maintainers, not projects installing a skill.

Read `PROMPT.md` and `coolship-deploy-prompt-implementation.md` as the original design inputs. Keep credentials and private infrastructure topology out of published packages. Preserve user work and do not run real deployments while validating documentation.

Run `python3 scripts/validate-skills.py` and `python3 -m unittest discover -s tests` before committing. Use isolated temporary application repositories to test installers and scripts. Validate shell syntax and exercise changed helpers with fake tools; never require live production access for CI.

Keep CLI examples grounded in upstream documentation and installed help; record source/version limitations. Add realistic evaluation cases for important behavior changes. Do not add platform-specific plugin manifests or a workflow orchestrator without a concrete request.
