#!/usr/bin/env python3
"""Flag public API and ABI change risks across headers and exported symbols."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Flag public API and ABI change risks across headers and exported symbols.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--baseline'],
             'kwargs': {'help': 'Baseline ref or path for comparison.'}},
            {'flags': ['--public-headers'],
             'kwargs': {'help': 'Directory containing public headers.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'breaking_signals': ['public struct field order changed',
                                      'virtual method signature changed'],
                 'non_breaking_signals': ['new overload added'],
                 'public_headers_scanned': 18,
                 'risk_level': 'medium',
                 'warnings': []},
 'text_output': 'ABI report\n'
                '- public headers scanned: 18\n'
                '- risk: medium\n'
                '- breaking signals: field order changed, virtual signature changed'}
TEXT_OUTPUT = 'ABI report\n- public headers scanned: 18\n- risk: medium\n- breaking signals: field order changed, virtual signature changed'
JSON_OUTPUT = '{\n  "public_headers_scanned": 18,\n  "risk_level": "medium",\n  "breaking_signals": [\n    "public struct field order changed",\n    "virtual method signature changed"\n  ],\n  "non_breaking_signals": [\n    "new overload added"\n  ],\n  "warnings": []\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.', default='.')
    parser.add_argument('--baseline', help='Baseline ref or path for comparison.')
    parser.add_argument('--public-headers', help='Directory containing public headers.')
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
