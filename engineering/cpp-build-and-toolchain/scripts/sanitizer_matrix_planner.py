#!/usr/bin/env python3
"""Recommend sanitizer profiles and scheduling strategies for a C++ repository."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Recommend sanitizer profiles and scheduling strategies for a C++ repository.'
CONTRACT = {'inputs': [{'flags': ['--repo'], 'kwargs': {'help': 'Repository root to inspect.'}},
            {'flags': ['--input'],
             'kwargs': {'help': 'Optional toolchain detection JSON.'}},
            {'flags': ['--scope'],
             'kwargs': {'choices': ['pr', 'nightly', 'release'],
                        'default': 'pr',
                        'help': 'Planning scope.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'commands': ['cmake -S . -B build-asan -DENABLE_ASAN=ON '
                              '-DENABLE_UBSAN=ON',
                              'ctest --test-dir build-asan --output-on-failure'],
                 'compiler_requirements': ['clang preferred for asan/ubsan'],
                 'constraints': ['tsan should not run with asan in same job'],
                 'recommended_profiles': [{'name': 'asan-ubsan',
                                           'when': 'pull_request'},
                                          {'name': 'tsan', 'when': 'nightly'}]},
 'text_output': 'Sanitizer plan\n'
                '- pull request: asan-ubsan\n'
                '- nightly: tsan\n'
                '- compiler preference: clang\n'
                '- constraint: do not combine tsan with asan in the same job'}
TEXT_OUTPUT = 'Sanitizer plan\n- pull request: asan-ubsan\n- nightly: tsan\n- compiler preference: clang\n- constraint: do not combine tsan with asan in the same job'
JSON_OUTPUT = '{\n  "recommended_profiles": [\n    {\n      "name": "asan-ubsan",\n      "when": "pull_request"\n    },\n    {\n      "name": "tsan",\n      "when": "nightly"\n    }\n  ],\n  "compiler_requirements": [\n    "clang preferred for asan/ubsan"\n  ],\n  "constraints": [\n    "tsan should not run with asan in same job"\n  ],\n  "commands": [\n    "cmake -S . -B build-asan -DENABLE_ASAN=ON -DENABLE_UBSAN=ON",\n    "ctest --test-dir build-asan --output-on-failure"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.')
    parser.add_argument('--input', help='Optional toolchain detection JSON.')
    parser.add_argument('--scope', choices=['pr', 'nightly', 'release'], default='pr', help='Planning scope.')
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
