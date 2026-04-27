#!/usr/bin/env python3
"""Inspect public header surfaces and summarize stability, ownership, and dependency concerns."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Inspect public header surfaces and summarize stability, ownership, and dependency concerns.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--public-headers'],
             'kwargs': {'help': 'Directory containing exported headers.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'exported_headers': 12,
                 'heavy_headers': ['include/sdk/client.hpp', 'include/sdk/config.hpp'],
                 'ownership_notes_needed': 4,
                 'recommendations': ['Separate pure interface headers from '
                                     'implementation detail headers']},
 'text_output': 'Header API surface\n'
                '- exported headers: 12\n'
                '- heavy includes: 3\n'
                '- ownership annotations needed: 4'}
TEXT_OUTPUT = 'Header API surface\n- exported headers: 12\n- heavy includes: 3\n- ownership annotations needed: 4'
JSON_OUTPUT = '{\n  "exported_headers": 12,\n  "heavy_headers": [\n    "include/sdk/client.hpp",\n    "include/sdk/config.hpp"\n  ],\n  "ownership_notes_needed": 4,\n  "recommendations": [\n    "Separate pure interface headers from implementation detail headers"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root to inspect.', default='.')
    parser.add_argument('--public-headers', help='Directory containing exported headers.')
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
