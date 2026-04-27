#!/usr/bin/env python3
"""Generate a starter C++ architecture outline with modules, layers, and boundary notes."""

import argparse
import json
from pathlib import Path

DESCRIPTION = 'Generate a starter C++ architecture outline with modules, layers, and boundary notes.'
CONTRACT = {'inputs': [{'flags': ['--repo'], 'kwargs': {'help': 'Repository root for context.'}},
            {'flags': ['--profile'],
             'kwargs': {'choices': ['library', 'service', 'sdk', 'embedded'],
                        'default': 'library',
                        'help': 'Architecture profile.'}},
            {'flags': ['--output'],
             'kwargs': {'help': 'Write generated outline to this file.'}},
            {'flags': ['--format'],
             'kwargs': {'choices': ['text', 'json'],
                        'default': 'text',
                        'help': 'Summary output format.'}}],
 'json_output': {'layers': ['api', 'domain', 'infra', 'tests'],
                 'output': 'docs/cpp-architecture-outline.md',
                 'profile': 'library',
                 'recommended_dirs': ['include/', 'src/', 'tests/', 'docs/adr/']},
 'text_output': 'Architecture scaffold\n'
                '- profile: library\n'
                '- layers: api, domain, infra, tests\n'
                '- output: docs/cpp-architecture-outline.md'}
TEXT_OUTPUT = 'Architecture scaffold\n- profile: library\n- layers: api, domain, infra, tests\n- output: docs/cpp-architecture-outline.md'
JSON_OUTPUT = '{\n  "profile": "library",\n  "layers": [\n    "api",\n    "domain",\n    "infra",\n    "tests"\n  ],\n  "recommended_dirs": [\n    "include/",\n    "src/",\n    "tests/",\n    "docs/adr/"\n  ],\n  "output": "docs/cpp-architecture-outline.md"\n}'
ARTIFACT_CONTENT = '# C++ Architecture Outline\n\n## Layers\n- API\n- Domain\n- Infrastructure\n- Tests\n'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--contract', action='store_true', help='Print the input/output contract as JSON and exit.')
    parser.add_argument('--repo', help='Repository root for context.')
    parser.add_argument('--profile', choices=['library', 'service', 'sdk', 'embedded'], default='library', help='Architecture profile.')
    parser.add_argument('--output', help='Write generated outline to this file.')
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
