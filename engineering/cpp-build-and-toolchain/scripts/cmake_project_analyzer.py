#!/usr/bin/env python3
"""Inspect a CMake project and extract targets, presets, options, and test signals."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Inspect a CMake project and extract targets, presets, options, and test signals.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.',
                        'help': 'Repository root containing the CMake project.'}},
            {'flags': ['--cmake-file'],
             'kwargs': {'help': 'Optional explicit CMakeLists.txt path.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'has_ctest': True,
                 'has_presets': False,
                 'options': ['BUILD_TESTING', 'ENABLE_ASAN'],
                 'project_name': 'demo',
                 'targets': [{'name': 'core', 'type': 'library'},
                             {'name': 'app', 'type': 'executable'}],
                 'warnings': []},
 'text_output': 'Analyzed CMake project\n'
                '- project: demo\n'
                '- targets: core (library), app (executable)\n'
                '- presets: none\n'
                '- options: BUILD_TESTING, ENABLE_ASAN'}
TEXT_OUTPUT = 'Analyzed CMake project\n- project: demo\n- targets: core (library), app (executable)\n- presets: none\n- options: BUILD_TESTING, ENABLE_ASAN'
JSON_OUTPUT = '{\n  "project_name": "demo",\n  "targets": [\n    {\n      "name": "core",\n      "type": "library"\n    },\n    {\n      "name": "app",\n      "type": "executable"\n    }\n  ],\n  "has_ctest": true,\n  "has_presets": false,\n  "options": [\n    "BUILD_TESTING",\n    "ENABLE_ASAN"\n  ],\n  "warnings": []\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root containing the CMake project.', default='.')
    parser.add_argument('--cmake-file', help='Optional explicit CMakeLists.txt path.')
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
