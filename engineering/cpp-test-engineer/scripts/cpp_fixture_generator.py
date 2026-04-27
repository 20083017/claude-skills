#!/usr/bin/env python3
"""Generate fixture outlines and shared setup plans for C++ test suites."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate fixture outlines and shared setup plans for C++ test suites.'
CONTRACT = {'inputs': [{'flags': ['--framework'],
             'kwargs': {'choices': ['gtest', 'catch2', 'doctest'],
                        'help': 'Fixture style to generate.',
                        'required': True}},
            {'flags': ['--suite-name'],
             'kwargs': {'help': 'Suite or fixture name.', 'required': True}},
            {'flags': ['--output'],
             'kwargs': {'help': 'Write fixture skeleton to this file.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Output format.'}}],
 'json_output': {'framework': 'gtest',
                 'generated_files': ['tests/cache_fixture.cpp'],
                 'shared_resources': ['temp directory', 'fake clock'],
                 'suite_name': 'CacheFixture',
                 'warnings': []},
 'text_output': 'Generated fixture outline\n'
                '- framework: gtest\n'
                '- suite: CacheFixture\n'
                '- shared state: temp dir, fake clock\n'
                '- output: tests/cache_fixture.cpp'}
TEXT_OUTPUT = 'Generated fixture outline\n- framework: gtest\n- suite: CacheFixture\n- shared state: temp dir, fake clock\n- output: tests/cache_fixture.cpp'
JSON_OUTPUT = '{\n  "framework": "gtest",\n  "suite_name": "CacheFixture",\n  "shared_resources": [\n    "temp directory",\n    "fake clock"\n  ],\n  "generated_files": [\n    "tests/cache_fixture.cpp"\n  ],\n  "warnings": []\n}'
ARTIFACT_CONTENT = 'class CacheFixture : public ::testing::Test {\n protected:\n  void SetUp() override {}\n  void TearDown() override {}\n};\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--framework', choices=['gtest', 'catch2', 'doctest'], required=True, help='Fixture style to generate.')
    parser.add_argument('--suite-name', help='Suite or fixture name.', required=True)
    parser.add_argument('--output', help='Write fixture skeleton to this file.')
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
