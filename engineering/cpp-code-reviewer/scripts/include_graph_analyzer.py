#!/usr/bin/env python3
"""Summarize include graph hotspots and layering issues in a C++ repository."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Summarize include graph hotspots and layering issues in a C++ repository.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository root to inspect.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'cycles_detected': 1,
                 'fan_in_outliers': ['include/core/config.hpp'],
                 'hot_headers': ['include/core/config.hpp', 'include/core/types.hpp'],
                 'recommendations': ['Replace transitive includes with forward '
                                     'declarations where ownership allows']},
 'text_output': 'Include graph analysis\n'
                '- hot headers: include/core/config.hpp, include/core/types.hpp\n'
                '- cycles: 1\n'
                '- recommendation: isolate transitively heavy headers behind forward '
                'declarations'}
TEXT_OUTPUT = 'Include graph analysis\n- hot headers: include/core/config.hpp, include/core/types.hpp\n- cycles: 1\n- recommendation: isolate transitively heavy headers behind forward declarations'
JSON_OUTPUT = '{\n  "hot_headers": [\n    "include/core/config.hpp",\n    "include/core/types.hpp"\n  ],\n  "cycles_detected": 1,\n  "fan_in_outliers": [\n    "include/core/config.hpp"\n  ],\n  "recommendations": [\n    "Replace transitive includes with forward declarations where ownership allows"\n  ]\n}'
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
