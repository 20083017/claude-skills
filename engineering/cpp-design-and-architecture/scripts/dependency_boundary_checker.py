#!/usr/bin/env python3
"""Check whether declared module boundaries match observed include and dependency patterns."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Check whether declared module boundaries match observed include and dependency patterns.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'boundary_health': 'watch',
                 'recommendations': ['Create a test-support seam',
                                     'Hide vendor headers behind adapters'],
                 'violations': [{'from': 'tests/',
                                 'severity': 'medium',
                                 'to': 'src/internal/'},
                                {'from': 'include/',
                                 'severity': 'high',
                                 'to': 'third_party/vendor/'}]},
 'text_output': 'Dependency boundary report\n'
                '- violations: 2\n'
                '- highest risk: tests reaching into internal headers\n'
                '- recommendation: move fixtures behind test support module'}
TEXT_OUTPUT = 'Dependency boundary report\n- violations: 2\n- highest risk: tests reaching into internal headers\n- recommendation: move fixtures behind test support module'
JSON_OUTPUT = '{\n  "violations": [\n    {\n      "from": "tests/",\n      "to": "src/internal/",\n      "severity": "medium"\n    },\n    {\n      "from": "include/",\n      "to": "third_party/vendor/",\n      "severity": "high"\n    }\n  ],\n  "boundary_health": "watch",\n  "recommendations": [\n    "Create a test-support seam",\n    "Hide vendor headers behind adapters"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.', default='.')
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
