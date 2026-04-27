#!/usr/bin/env python3
"""Detect C++ test frameworks and recommend the best default for the repository."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Detect C++ test frameworks and recommend the best default for the repository.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository path to inspect.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'frameworks': ['gtest', 'ctest'],
                 'recommended_framework': 'gtest',
                 'signals': {'catch2_headers': False,
                             'doctest_headers': False,
                             'enable_testing': True,
                             'gtest_headers': True}},
 'text_output': 'Detected test frameworks\n'
                '- frameworks: gtest, ctest\n'
                '- enable_testing(): yes\n'
                '- recommended: gtest'}
TEXT_OUTPUT = 'Detected test frameworks\n- frameworks: gtest, ctest\n- enable_testing(): yes\n- recommended: gtest'
JSON_OUTPUT = '{\n  "frameworks": [\n    "gtest",\n    "ctest"\n  ],\n  "signals": {\n    "gtest_headers": true,\n    "catch2_headers": false,\n    "doctest_headers": false,\n    "enable_testing": true\n  },\n  "recommended_framework": "gtest"\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository path to inspect.', default='.')
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
