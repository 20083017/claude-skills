---
name: "cpp-test-engineer"
description: "Use when generating C++ test scaffolds, detecting GoogleTest/Catch2/doctest setups, planning fixtures, normalizing coverage output, or designing sanitizer-aware test workflows for modern C++ codebases."
---

# C++ Test Engineer

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** C++ / Testing / Quality

## Overview

Bridges spec-first and TDD workflows into C++ by detecting local test frameworks, generating deterministic suite skeletons, and standardizing coverage and sanitizer planning.

## When to Use

- Converting acceptance criteria into GoogleTest, Catch2, or doctest skeletons
- Auditing whether a repository already has test framework signals
- Planning sanitizer-aware test runs before wiring them into CI
- Normalizing coverage output across gcov, lcov, and llvm-cov

## Key Workflows

1. Detect or normalize repository signals before making decisions.
2. Capture a machine-readable payload for reuse in CI, review, or planning steps.
3. Generate starter artifacts only after the baseline context is explicit.
4. Treat outputs as editable baselines, not immutable final implementations.

## Script Contracts

| Script | Purpose | Inputs | Outputs |
|---|---|---|---|
| `cpp_test_framework_detector.py` | Detect C++ test frameworks and recommend the best default for the repository. | `--repo, --format` | `text|json` or generated artifact |
| `cpp_test_stub_generator.py` | Generate C++ test suite skeletons from a spec document or structured criteria JSON. | `--file, --input, --framework, --output, --suite-name, --format` | `text|json` or generated artifact |
| `cpp_fixture_generator.py` | Generate fixture outlines and shared setup plans for C++ test suites. | `--framework, --suite-name, --output, --format` | `text|json` or generated artifact |
| `cpp_coverage_adapter.py` | Normalize lcov, gcov, and llvm-cov reports into a single coverage summary. | `--input, --tool, --format` | `text|json` or generated artifact |
| `sanitizer_test_planner.py` | Plan how sanitizer jobs should be split across fast and slow C++ test suites. | `--repo, --framework, --scope, --format` | `text|json` or generated artifact |

Run any script with `--contract` to print the draft input/output contract as JSON.

## Commands

- `cpp-test.md`
- `cpp-sanitize.md`

## References

- [references/gtest-patterns.md](references/gtest-patterns.md)
- [references/catch2-patterns.md](references/catch2-patterns.md)
- [references/doctest-patterns.md](references/doctest-patterns.md)
- [references/cpp-test-pyramid.md](references/cpp-test-pyramid.md)
- [references/coverage-workflows.md](references/coverage-workflows.md)

## Assets

- [assets/gtest-suite-template.cpp](assets/gtest-suite-template.cpp)
- [assets/catch2-suite-template.cpp](assets/catch2-suite-template.cpp)
- [assets/doctest-suite-template.cpp](assets/doctest-suite-template.cpp)

## Expected Outputs

- `expected_outputs/` contains sample JSON, YAML, Markdown, and source-file baselines that match the CLI contracts.

## Design Notes

- Scripts use Python standard library only.
- `--format json` is intended for automation handoff.
- Generated artifacts are starter baselines that teams can refine per repository.
