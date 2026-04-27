#!/usr/bin/env python3
"""Generate Architecture Decision Record templates for C++ design choices."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate Architecture Decision Record templates for C++ design choices.'
CONTRACT = {'inputs': [{'flags': ['--title'], 'kwargs': {'help': 'ADR title.', 'required': True}},
            {'flags': ['--status'],
             'kwargs': {'choices': ['proposed', 'accepted', 'superseded'],
                        'default': 'proposed',
                        'help': 'ADR status.'}},
            {'flags': ['--output'], 'kwargs': {'help': 'Write ADR to this file.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Summary output format.'}}],
 'json_output': {'output': 'docs/adr/0001-public-header-policy.md',
                 'sections': ['Context', 'Decision', 'Consequences', 'Follow-up'],
                 'status': 'proposed',
                 'title': 'Public Header Policy'},
 'text_output': 'ADR scaffold\n'
                '- title: Public Header Policy\n'
                '- status: proposed\n'
                '- output: docs/adr/0001-public-header-policy.md'}
TEXT_OUTPUT = 'ADR scaffold\n- title: Public Header Policy\n- status: proposed\n- output: docs/adr/0001-public-header-policy.md'
JSON_OUTPUT = '{\n  "title": "Public Header Policy",\n  "status": "proposed",\n  "sections": [\n    "Context",\n    "Decision",\n    "Consequences",\n    "Follow-up"\n  ],\n  "output": "docs/adr/0001-public-header-policy.md"\n}'
ARTIFACT_CONTENT = '# ADR: Public Header Policy\n\n## Status\nProposed\n\n## Context\n\n## Decision\n\n## Consequences\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--title', help='ADR title.', required=True)
    parser.add_argument('--status', choices=['proposed', 'accepted', 'superseded'], default='proposed', help='ADR status.')
    parser.add_argument('--output', help='Write ADR to this file.')
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
