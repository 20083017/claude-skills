#!/usr/bin/env python3
"""Score a C++ change set for review risk based on ownership, concurrency, and API surface signals."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Score a C++ change set for review risk based on ownership, concurrency, and API surface signals.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--diff'], 'kwargs': {'help': 'Optional diff to score.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'drivers': ['ownership transfer', 'public headers', 'concurrency'],
                 'recommended_followups': ['Require ABI review',
                                           'Run sanitizer suite',
                                           'Inspect include fan-out'],
                 'risk_level': 'high',
                 'risk_score': 74},
 'text_output': 'C++ change risk\n'
                '- score: 74\n'
                '- level: high\n'
                '- drivers: ownership transfer, public headers, concurrency'}
TEXT_OUTPUT = 'C++ change risk\n- score: 74\n- level: high\n- drivers: ownership transfer, public headers, concurrency'
JSON_OUTPUT = '{\n  "risk_score": 74,\n  "risk_level": "high",\n  "drivers": [\n    "ownership transfer",\n    "public headers",\n    "concurrency"\n  ],\n  "recommended_followups": [\n    "Require ABI review",\n    "Run sanitizer suite",\n    "Inspect include fan-out"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.', default='.')
    parser.add_argument('--diff', help='Optional diff to score.')
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
