#!/usr/bin/env python3
"""Validate portable packages without contacting deployment services."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import tomllib
from urllib.parse import unquote, urlsplit

import yaml

ALLOWED = {'name', 'description', 'license', 'compatibility', 'metadata', 'allowed-tools'}
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
LINK = re.compile(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')


def validate(root):
    root = Path(root).resolve()
    errors = []
    skills = sorted((root / 'skills').glob('*/*/SKILL.md'))
    discovered = set((root / 'skills').rglob('SKILL.md'))
    if not skills:
        errors.append('No skills found at skills/<category>/<name>/SKILL.md')
    for misplaced in discovered - set(skills):
        errors.append(f'{misplaced.relative_to(root)}: expected category/name layout')
    names = set()
    for entry in skills:
        label = str(entry.relative_to(root))
        text = entry.read_text()
        parts = text.split('---', 2)
        if len(parts) != 3 or parts[0] != '' or not parts[1].startswith('\n'):
            errors.append(f'{label}: missing YAML frontmatter')
            continue
        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                raise ValueError('frontmatter must be a mapping')
            if set(meta) - ALLOWED:
                raise ValueError(f'unsupported fields: {set(meta) - ALLOWED}')
            name = meta.get('name')
            if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
                raise ValueError('invalid name')
            if name != entry.parent.name or name in names:
                raise ValueError('name must match directory and be globally unique')
            names.add(name)
            for field, limit in [('description', 1024), ('compatibility', 500)]:
                if field == 'description' or field in meta:
                    value = meta.get(field)
                    if not isinstance(value, str) or not value.strip() or len(value) > limit:
                        raise ValueError(f'{field} must be a nonempty string of at most {limit} characters')
            if 'metadata' in meta and (not isinstance(meta['metadata'], dict) or
                    any(not isinstance(k, str) or not isinstance(v, str) for k, v in meta['metadata'].items())):
                raise ValueError('metadata must map strings to strings')
            if not parts[2].strip():
                raise ValueError('missing instructions')
            if len(text.splitlines()) >= 500:
                raise ValueError('keep SKILL.md below 500 lines')
        except (yaml.YAMLError, ValueError) as exc:
            errors.append(f'{label}: {exc}')
        for file in entry.parent.rglob('*'):
            if not file.is_file():
                continue
            rel = str(file.relative_to(root))
            if file.suffix == '.sh':
                result = subprocess.run(['sh', '-n', str(file)], capture_output=True, text=True)
                if result.returncode:
                    errors.append(f'{rel}: {result.stderr.strip()}')
                if not file.stat().st_mode & 0o111:
                    errors.append(f'{rel}: script must be executable')
            if file.suffix in {'.yaml', '.yml', '.toml', '.json'} or file.name.endswith('.toml.example'):
                try:
                    data = file.read_text()
                    if '.toml' in file.name:
                        tomllib.loads(data)
                    elif file.suffix == '.json':
                        cases = json.loads(data)
                        if file.name == 'cases.json':
                            if not isinstance(cases, list) or not cases:
                                raise ValueError('cases must be a nonempty list')
                            ids = set()
                            for case in cases:
                                if not isinstance(case, dict):
                                    raise ValueError('each case must be an object')
                                for key in ('id', 'request'):
                                    if not isinstance(case.get(key), str) or not case[key].strip():
                                        raise ValueError(f'case needs {key}')
                                if case['id'] in ids:
                                    raise ValueError('duplicate case id')
                                ids.add(case['id'])
                                behavior = case.get('expected_behavior')
                                if not isinstance(behavior, list) or not behavior or any(not isinstance(x, str) or not x.strip() for x in behavior):
                                    raise ValueError('case needs expected_behavior strings')
                                if 'should_trigger' in case and not isinstance(case['should_trigger'], bool):
                                    raise ValueError('should_trigger must be boolean')
                    else:
                        yaml.safe_load(data)
                except (ValueError, yaml.YAMLError) as exc:
                    errors.append(f'{rel}: {exc}')
    # All Markdown links must resolve; installed skill packages must stay self-contained.
    for file in root.rglob('*.md'):
        if '.git' in file.parts or any(part.startswith('.') for part in file.relative_to(root).parts[:-1]):
            continue
        package = next((s.parent for s in skills if file.is_relative_to(s.parent)), None)
        for target in LINK.findall(file.read_text()):
            target = target.strip('<>')
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (file.parent / unquote(url.path)).resolve()
            if not destination.exists():
                errors.append(f'{file.relative_to(root)}: broken link {target}')
            if package and not destination.is_relative_to(package):
                errors.append(f'{file.relative_to(root)}: link escapes installed package: {target}')
    return errors, len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, count = validate(args.root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f'Validated {count} skills; {len(errors)} error(s).')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
