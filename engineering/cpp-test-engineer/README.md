# C++ Test Engineer

Bridges spec-first and TDD workflows into C++ by detecting local test frameworks, generating deterministic suite skeletons, and standardizing coverage and sanitizer planning.

## Quick Start

```bash
python3 scripts/cpp_test_framework_detector.py --help
```

## Included Tools

- `scripts/cpp_test_framework_detector.py` — Detect C++ test frameworks and recommend the best default for the repository.
- `scripts/cpp_test_stub_generator.py` — Generate C++ test suite skeletons from a spec document or structured criteria JSON.
- `scripts/cpp_fixture_generator.py` — Generate fixture outlines and shared setup plans for C++ test suites.
- `scripts/cpp_coverage_adapter.py` — Normalize lcov, gcov, and llvm-cov reports into a single coverage summary.
- `scripts/sanitizer_test_planner.py` — Plan how sanitizer jobs should be split across fast and slow C++ test suites.

## References

- `references/gtest-patterns.md`
- `references/catch2-patterns.md`
- `references/doctest-patterns.md`
- `references/cpp-test-pyramid.md`
- `references/coverage-workflows.md`

## Assets

- `assets/gtest-suite-template.cpp`
- `assets/catch2-suite-template.cpp`
- `assets/doctest-suite-template.cpp`

## Installation

### Claude Code

```bash
cp -R engineering/cpp-test-engineer ~/.claude/skills/cpp-test-engineer
```

### OpenAI Codex

```bash
cp -R engineering/cpp-test-engineer ~/.codex/skills/cpp-test-engineer
```

### Gemini CLI

```bash
activate_skill(name="cpp-test-engineer")
```
