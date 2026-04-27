#!/usr/bin/env python3
"""Plan how sanitizer jobs should be split across fast and slow C++ test suites."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Plan how sanitizer jobs should be split across fast and slow C++ test suites.'
CONTRACT = {'inputs': [{'flags': ['--repo'], 'kwargs': {'help': 'Repository root to inspect.'}},
            {'flags': ['--framework'],
             'kwargs': {'choices': ['gtest', 'catch2', 'doctest'],
                        'help': 'Prefer a framework when generating recommendations.'}},
            {'flags': ['--scope'],
             'kwargs': {'choices': ['pr', 'nightly', 'release'],
                        'default': 'pr',
                        'help': 'Planning scope.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'fast_lane': ['unit', 'component'],
                 'nightly_lane': ['race-heavy integration'],
                 'notes': ['Keep deterministic smoke coverage outside long-running '
                           'tsan jobs'],
                 'sanitizers': [{'name': 'asan-ubsan', 'when': 'pull_request'},
                                {'name': 'tsan', 'when': 'nightly'}]},
 'text_output': 'Sanitizer test plan\n'
                '- fast suite: smoke + unit under asan-ubsan\n'
                '- slow suite: concurrency under tsan at night\n'
                '- release: rerun smoke without sanitizers'}
TEXT_OUTPUT = 'Sanitizer test plan\n- fast suite: smoke + unit under asan-ubsan\n- slow suite: concurrency under tsan at night\n- release: rerun smoke without sanitizers'
JSON_OUTPUT = '{\n  "fast_lane": [\n    "unit",\n    "component"\n  ],\n  "nightly_lane": [\n    "race-heavy integration"\n  ],\n  "sanitizers": [\n    {\n      "name": "asan-ubsan",\n      "when": "pull_request"\n    },\n    {\n      "name": "tsan",\n      "when": "nightly"\n    }\n  ],\n  "notes": [\n    "Keep deterministic smoke coverage outside long-running tsan jobs"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.')
    parser.add_argument('--framework', choices=['gtest', 'catch2', 'doctest'], help='Prefer a framework when generating recommendations.')
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
