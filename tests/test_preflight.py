import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/devops/coolship-deploy/scripts/preflight.sh'


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'app'
        self.repo.mkdir()
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        self.log = self.root / 'calls'
        fake = self.bin / 'coolship'
        fake.write_text('''#!/bin/sh
printf '%s\\n' "$*" >> "$PREFLIGHT_CALLS"
case "$*" in
  '--version'|'config show'|'doctor'|'status') ;;
  *) exit 99 ;;
esac
if [ "$1" = doctor ]; then exit "${PREFLIGHT_DOCTOR_EXIT:-0}"; fi
''')
        fake.chmod(0o755)
        self.env = {**os.environ, 'PATH': str(self.bin) + os.pathsep + os.environ['PATH'], 'PREFLIGHT_CALLS': str(self.log)}

    def git(self, *args):
        subprocess.run(['git', *args], cwd=self.repo, check=True, capture_output=True)

    def commit(self):
        self.git('init')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '--allow-empty', '-m', 'Initial')

    def run_script(self):
        return subprocess.run(['sh', str(SCRIPT)], cwd=self.repo, env=self.env, capture_output=True, text=True)

    def test_success_only_calls_read_only_commands(self):
        self.commit()
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.log.read_text().splitlines(), ['--version', 'config show', 'doctor', 'status'])

    def test_remote_failure_is_nonzero(self):
        self.commit()
        self.env['PREFLIGHT_DOCTOR_EXIT'] = '1'
        self.assertEqual(self.run_script().returncode, 1)

    def test_unborn_repository_stops_before_remote_calls(self):
        self.git('init')
        self.assertEqual(self.run_script().returncode, 2)
        self.assertFalse(self.log.exists())

    def test_non_repository_is_rejected(self):
        self.assertEqual(self.run_script().returncode, 2)
        self.assertFalse(self.log.exists())
