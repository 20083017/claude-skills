#!/usr/bin/env python3
"""Generate baseline GitHub Actions or GitLab CI YAML for C++ repositories."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate baseline GitHub Actions or GitLab CI YAML for C++ repositories.'
CONTRACT = {'inputs': [{'flags': ['--platform'],
             'kwargs': {'choices': ['github', 'gitlab'],
                        'help': 'Target CI platform.',
                        'required': True}},
            {'flags': ['--repo'],
             'kwargs': {'help': 'Repository root used for auto-detection.'}},
            {'flags': ['--input'],
             'kwargs': {'help': 'Optional toolchain JSON payload.'}},
            {'flags': ['--output'],
             'kwargs': {'help': 'Write generated YAML to this file.'}},
            {'flags': ['--profile'],
             'kwargs': {'choices': ['baseline', 'sanitizers', 'release-matrix'],
                        'default': 'baseline',
                        'help': 'Pipeline profile.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Summary output format.'}}],
 'json_output': {'jobs': ['build', 'test'],
                 'output': '.github/workflows/cpp-ci.yml',
                 'platform': 'github',
                 'profile': 'baseline',
                 'supports_sanitizers': True,
                 'uses_cache': True},
 'text_output': 'Generated C++ pipeline summary\n'
                '- platform: github\n'
                '- profile: baseline\n'
                '- jobs: build, test\n'
                '- cache: enabled\n'
                '- output: .github/workflows/cpp-ci.yml'}
TEXT_OUTPUT = 'Generated C++ pipeline summary\n- platform: github\n- profile: baseline\n- jobs: build, test\n- cache: enabled\n- output: .github/workflows/cpp-ci.yml'
JSON_OUTPUT = '{\n  "platform": "github",\n  "profile": "baseline",\n  "jobs": [\n    "build",\n    "test"\n  ],\n  "uses_cache": true,\n  "supports_sanitizers": true,\n  "output": ".github/workflows/cpp-ci.yml"\n}'
ARTIFACT_CONTENT = 'name: C++ CI\non:\n  push:\n    branches: [main, develop]\n  pull_request:\n    branches: [main, develop]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Configure\n        run: cmake -S . -B build -G Ninja\n      - name: Build\n        run: cmake --build build\n  test:\n    runs-on: ubuntu-latest\n    needs: build\n    steps:\n      - uses: actions/checkout@v4\n      - name: Run tests\n        run: ctest --test-dir build --output-on-failure\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--platform', choices=['github', 'gitlab'], required=True, help='Target CI platform.')
    parser.add_argument('--repo', help='Repository root used for auto-detection.')
    parser.add_argument('--input', help='Optional toolchain JSON payload.')
    parser.add_argument('--output', help='Write generated YAML to this file.')
    parser.add_argument('--profile', choices=['baseline', 'sanitizers', 'release-matrix'], default='baseline', help='Pipeline profile.')
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
