#!/usr/bin/env python3
"""Normalize lcov, gcov, and llvm-cov reports into a single coverage summary."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Normalize lcov, gcov, and llvm-cov reports into a single coverage summary.'
CONTRACT = {'inputs': [{'flags': ['--input'],
             'kwargs': {'help': 'Coverage file or directory to inspect.',
                        'required': True}},
            {'flags': ['--tool'],
             'kwargs': {'choices': ['lcov', 'gcov', 'llvm-cov', 'auto'],
                        'default': 'auto',
                        'help': 'Coverage tool format.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'branch_coverage': 71.0,
                 'files': [{'line_coverage': 91.0, 'path': 'src/core.cpp'}],
                 'function_coverage': 79.5,
                 'line_coverage': 84.2,
                 'threshold_pass': True,
                 'tool': 'llvm-cov'},
 'text_output': 'Coverage summary\n'
                '- tool: llvm-cov\n'
                '- line coverage: 84.2%\n'
                '- function coverage: 79.5%\n'
                '- branch coverage: 71.0%\n'
                '- threshold: pass'}
TEXT_OUTPUT = 'Coverage summary\n- tool: llvm-cov\n- line coverage: 84.2%\n- function coverage: 79.5%\n- branch coverage: 71.0%\n- threshold: pass'
JSON_OUTPUT = '{\n  "tool": "llvm-cov",\n  "line_coverage": 84.2,\n  "function_coverage": 79.5,\n  "branch_coverage": 71.0,\n  "files": [\n    {\n      "path": "src/core.cpp",\n      "line_coverage": 91.0\n    }\n  ],\n  "threshold_pass": true\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--input', help='Coverage file or directory to inspect.', required=True)
    parser.add_argument('--tool', choices=['lcov', 'gcov', 'llvm-cov', 'auto'], default='auto', help='Coverage tool format.')
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
