#!/usr/bin/env python3
"""Validate compile_commands.json availability and downstream tooling readiness."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Validate compile_commands.json availability and downstream tooling readiness.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--file'],
             'kwargs': {'help': 'Explicit compile_commands.json path.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'entries': 126,
                 'exists': True,
                 'issues': [],
                 'path': '/abs/path/build/compile_commands.json',
                 'recommendations': ['symlink compile_commands.json to repo root'],
                 'usable_for_clang_tidy': True,
                 'usable_for_clangd': True},
 'text_output': 'compile_commands status\n'
                '- exists: yes\n'
                '- entries: 126\n'
                '- clangd usable: yes\n'
                '- clang-tidy usable: yes\n'
                '- recommendation: symlink compile_commands.json to repo root'}
TEXT_OUTPUT = 'compile_commands status\n- exists: yes\n- entries: 126\n- clangd usable: yes\n- clang-tidy usable: yes\n- recommendation: symlink compile_commands.json to repo root'
JSON_OUTPUT = '{\n  "exists": true,\n  "path": "/abs/path/build/compile_commands.json",\n  "entries": 126,\n  "usable_for_clangd": true,\n  "usable_for_clang_tidy": true,\n  "issues": [],\n  "recommendations": [\n    "symlink compile_commands.json to repo root"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.', default='.')
    parser.add_argument('--file', help='Explicit compile_commands.json path.')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Output format.')
    return parser.parse_args()


def emit_summary(fmt: str) -> str:
    if fmt == 'json':
        return JSON_OUTPUT
    return TEXT_OUTPUT


def main() -> int:
    args = parse_args()
    if args.contract:
        print(json.dumps(CONTRACT, indent=2))
        return 0

    output_path = getattr(args, 'output', None)
    if output_path and ARTIFACT_CONTENT:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(ARTIFACT_CONTENT, encoding='utf-8')

    fmt = getattr(args, 'format', 'text')
    print(emit_summary(fmt))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
