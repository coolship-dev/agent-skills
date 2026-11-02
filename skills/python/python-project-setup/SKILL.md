---
name: python-project-setup
description: Set up or repair Python project tooling. Use for Python environments, packaging, dependency management, tests or lint configuration.
---

# Python project setup

Inspect the repository's Python version, pyproject.toml, lockfiles, CI and existing package manager. Preserve the established toolchain; for a new project choose a supported Python version and one dependency manager based on its deployment needs.

Create an isolated environment and declare runtime/development dependencies in the project's canonical configuration. Keep lockfiles consistent with the chosen tool; avoid mixing competing dependency sources. Configure the actual package/module layout and install path, including src layouts when used.

Add only tooling needed by the project: a test runner, formatter/linter and type checker where useful. Use the tool's supported configuration for the installed version. Exclude virtual environments, caches and secrets from Git. Provide reproducible setup and check commands.

Verify from a clean environment that installation, imports and the relevant tests/checks work. For distributable packages, build and inspect the artifact. Report supported Python versions and commands; do not claim cross-version compatibility from a single interpreter run.
