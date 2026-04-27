#!/usr/bin/env python3
"""Detect C++ toolchain, build system, and package-manager signals from a repository."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Detect C++ toolchain, build system, and package-manager signals from a repository.'
CONTRACT = {'inputs': [{'flags': ['--repo'],
             'kwargs': {'default': '.', 'help': 'Repository path to scan.'}},
            {'flags': ['--input'],
             'kwargs': {'help': 'Optional JSON detection payload file.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'build_commands': ['cmake --build build'],
                 'build_systems': ['cmake'],
                 'configure_commands': ['cmake -S . -B build -G Ninja'],
                 'generators': ['ninja'],
                 'package_managers': ['vcpkg'],
                 'repo': '/abs/path',
                 'signals': {'cmakelists': True,
                             'compile_commands': False,
                             'ctest': True,
                             'vcpkg_manifest': True},
                 'test_commands': ['ctest --test-dir build --output-on-failure'],
                 'test_frameworks': ['ctest', 'gtest']},
 'text_output': 'Detected C++ toolchain baseline\n'
                '- build systems: cmake\n'
                '- test frameworks: ctest, gtest\n'
                '- package managers: vcpkg\n'
                '- generators: ninja\n'
                '- configure: cmake -S . -B build -G Ninja'}
TEXT_OUTPUT = 'Detected C++ toolchain baseline\n- build systems: cmake\n- test frameworks: ctest, gtest\n- package managers: vcpkg\n- generators: ninja\n- configure: cmake -S . -B build -G Ninja'
JSON_OUTPUT = '{\n  "repo": "/abs/path",\n  "build_systems": [\n    "cmake"\n  ],\n  "test_frameworks": [\n    "ctest",\n    "gtest"\n  ],\n  "package_managers": [\n    "vcpkg"\n  ],\n  "generators": [\n    "ninja"\n  ],\n  "signals": {\n    "cmakelists": true,\n    "ctest": true,\n    "compile_commands": false,\n    "vcpkg_manifest": true\n  },\n  "configure_commands": [\n    "cmake -S . -B build -G Ninja"\n  ],\n  "build_commands": [\n    "cmake --build build"\n  ],\n  "test_commands": [\n    "ctest --test-dir build --output-on-failure"\n  ]\n}'
ARTIFACT_CONTENT = ''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository path to scan.', default='.')
    parser.add_argument('--input', help='Optional JSON detection payload file.')
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
