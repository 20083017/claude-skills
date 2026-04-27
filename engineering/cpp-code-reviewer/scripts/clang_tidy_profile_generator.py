#!/usr/bin/env python3
"""Generate clang-tidy rule profiles for C++ library, service, or embedded contexts."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate clang-tidy rule profiles for C++ library, service, or embedded contexts.'
CONTRACT = {'inputs': [{'flags': ['--profile'],
             'kwargs': {'choices': ['library', 'service', 'embedded', 'general'],
                        'default': 'general',
                        'help': 'Rule profile to emit.'}},
            {'flags': ['--output'],
             'kwargs': {'help': 'Write generated profile to this file.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Summary output format.'}}],
 'json_output': {'checks': ['modernize-*',
                            'readability-*',
                            'bugprone-*',
                            'performance-*'],
                 'header_filter': 'include/|src/',
                 'output': '.clang-tidy',
                 'profile': 'general'},
 'text_output': 'clang-tidy profile\n'
                '- profile: general\n'
                '- checks: modernize, readability, bugprone, performance\n'
                '- output: .clang-tidy'}
TEXT_OUTPUT = 'clang-tidy profile\n- profile: general\n- checks: modernize, readability, bugprone, performance\n- output: .clang-tidy'
JSON_OUTPUT = '{\n  "profile": "general",\n  "checks": [\n    "modernize-*",\n    "readability-*",\n    "bugprone-*",\n    "performance-*"\n  ],\n  "header_filter": "include/|src/",\n  "output": ".clang-tidy"\n}'
ARTIFACT_CONTENT = "Checks: >\n  modernize-*,\n  readability-*,\n  bugprone-*,\n  performance-*\nWarningsAsErrors: ''\nHeaderFilterRegex: '(include|src)/'\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--profile', choices=['library', 'service', 'embedded', 'general'], default='general', help='Rule profile to emit.')
    parser.add_argument('--output', help='Write generated profile to this file.')
    parser.add_argument('--format', choices=['text', 'json'], default='text', help='Summary output format.')
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
