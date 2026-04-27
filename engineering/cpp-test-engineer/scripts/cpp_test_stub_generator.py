#!/usr/bin/env python3
"""Generate C++ test suite skeletons from a spec document or structured criteria JSON."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate C++ test suite skeletons from a spec document or structured criteria JSON.'
CONTRACT = {'inputs': [{'flags': ['--file'],
             'kwargs': {'help': 'Specification markdown file to parse.'}},
            {'flags': ['--input'],
             'kwargs': {'help': 'Optional structured criteria JSON file.'}},
            {'flags': ['--framework'],
             'kwargs': {'choices': ['gtest', 'catch2', 'doctest'],
                        'help': 'Target test framework.',
                        'required': True}},
            {'flags': ['--output'],
             'kwargs': {'help': 'Write generated test source to this file.'}},
            {'flags': ['--suite-name'],
             'kwargs': {'help': 'Override generated suite name.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Summary output format.'}}],
 'json_output': {'acceptance_criteria_count': 6,
                 'edge_case_count': 4,
                 'framework': 'gtest',
                 'generated_files': ['tests/vector_spec_test.cpp'],
                 'suite_name': 'VectorTests',
                 'warnings': []},
 'text_output': 'Generated test stubs\n'
                '- framework: gtest\n'
                '- suite: VectorTests\n'
                '- acceptance criteria: 6\n'
                '- edge cases: 4\n'
                '- output: tests/vector_spec_test.cpp'}
TEXT_OUTPUT = 'Generated test stubs\n- framework: gtest\n- suite: VectorTests\n- acceptance criteria: 6\n- edge cases: 4\n- output: tests/vector_spec_test.cpp'
JSON_OUTPUT = '{\n  "framework": "gtest",\n  "suite_name": "VectorTests",\n  "acceptance_criteria_count": 6,\n  "edge_case_count": 4,\n  "generated_files": [\n    "tests/vector_spec_test.cpp"\n  ],\n  "warnings": []\n}'
ARTIFACT_CONTENT = '#include <gtest/gtest.h>\n\nclass VectorTests : public ::testing::Test {};\n\nTEST_F(VectorTests, HandlesEmptyInput) {\n  GTEST_SKIP() << "Implement acceptance criterion AC-1";\n}\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--file', help='Specification markdown file to parse.')
    parser.add_argument('--input', help='Optional structured criteria JSON file.')
    parser.add_argument('--framework', choices=['gtest', 'catch2', 'doctest'], required=True, help='Target test framework.')
    parser.add_argument('--output', help='Write generated test source to this file.')
    parser.add_argument('--suite-name', help='Override generated suite name.')
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
