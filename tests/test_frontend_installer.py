"""Offline tests for the optional frontend skills installer."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install-frontend.sh"


class FrontendInstallerTests(unittest.TestCase):
    def run_script(self, agents=(), playwright=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bin_dir = root / "bin"
            bin_dir.mkdir()
            log = root / "commands.log"

            npx = bin_dir / "npx"
            npx.write_text('#!/bin/sh\nprintf "npx:%s\\n" "$*" >> "$COMMANDS_LOG"\n')
            npx.chmod(0o755)

            if playwright:
                cli = bin_dir / "playwright-cli"
                cli.write_text('#!/bin/sh\nprintf "playwright:%s\\n" "$*" >> "$COMMANDS_LOG"\n')
                cli.chmod(0o755)

            env = os.environ.copy()
            env["PATH"] = str(bin_dir) + os.pathsep + "/usr/bin:/bin"
            env["COMMANDS_LOG"] = str(log)
            proc = subprocess.run(["sh", str(SCRIPT), *agents], cwd=root, env=env,
                                  capture_output=True, text=True, check=False)
            return proc, log.read_text().splitlines() if log.exists() else []

    def test_default_is_project_scoped(self):
        proc, calls = self.run_script()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(len(calls), 3)
        self.assertIn("skills add coolship-dev/agent-skills", calls[0])
        self.assertIn("--skill frontend-architecture", calls[0])
        self.assertIn("--skill frontend-review", calls[0])
        self.assertIn("skills add vercel-labs/agent-skills", calls[1])
        self.assertIn("--skill vercel-composition-patterns", calls[1])
        self.assertIn("skills add anthropics/skills", calls[2])
        for line in calls:
            self.assertIn("-a codex claude-code cursor opencode -y", line)
            self.assertNotIn(" -g ", line)
        self.assertIn("npm install -g @playwright/cli@latest", proc.stdout)

    def test_selected_agents_and_existing_playwright(self):
        proc, calls = self.run_script(("codex", "claude-code"), playwright=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(len(calls), 4)
        for line in calls[:3]:
            self.assertIn("-a codex claude-code -y", line)
        self.assertEqual(calls[3], "playwright:install --skills")

    def test_rejects_unknown_agent_without_installing(self):
        proc, calls = self.run_script(("unknown",))
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(calls, [])
        self.assertIn("Unsupported agent", proc.stderr)


if __name__ == "__main__":
    unittest.main()
