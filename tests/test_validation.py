import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('validator', Path(__file__).resolve().parents[1] / 'scripts/validate-skills.py')
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / 'skills/example/test-skill'
        self.skill.mkdir(parents=True)
        self.entry = self.skill / 'SKILL.md'
        self.entry.write_text('---\nname: test-skill\ndescription: Test example skills.\n---\n\nInstructions.\n')

    def errors(self):
        return validator.validate(self.root)[0]

    def test_valid_package(self):
        self.assertEqual(self.errors(), [])

    def test_rejects_mismatched_name(self):
        self.entry.write_text(self.entry.read_text().replace('name: test-skill', 'name: wrong'))
        self.assertTrue(any('match directory' in e for e in self.errors()))

    def test_rejects_broken_link(self):
        self.entry.write_text(self.entry.read_text() + '\n[Missing](references/missing.md)\n')
        self.assertTrue(any('broken link' in e for e in self.errors()))

    def test_rejects_package_escape(self):
        (self.root / 'README.md').write_text('Repository documentation.')
        self.entry.write_text(self.entry.read_text() + '\n[Outside](../../../README.md)\n')
        self.assertTrue(any('escapes installed package' in e for e in self.errors()))

    def test_rejects_bad_shell(self):
        script = self.skill / 'bad.sh'
        script.write_text('#!/bin/sh\nif then\n')
        script.chmod(0o755)
        self.assertTrue(self.errors())

    def test_rejects_invalid_evaluation(self):
        (self.skill / 'cases.json').write_text(json.dumps([{'id': 'case', 'request': 'Deploy', 'expected_behavior': []}]))
        self.assertTrue(any('expected_behavior' in e for e in self.errors()))

    def test_rejects_invalid_template(self):
        (self.skill / 'config.toml.example').write_text('version = [')
        self.assertTrue(self.errors())
