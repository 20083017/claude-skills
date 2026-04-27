---
name: "cpp-build-and-toolchain"
description: "Use when setting up or auditing C++ build systems, toolchains, CMake projects, compile_commands flows, CI pipelines, or sanitizer build matrices across CMake, Ninja, Make, Conan, and vcpkg based repositories."
---

# C++ Build and Toolchain

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** C++ / Build Systems / DevOps

## Overview

Detects C++ toolchains and build signals, normalizes them into machine-readable payloads, and generates practical CI baselines for multi-compiler repositories.

## When to Use

- Bootstrapping CI for a new C++ repository
- Auditing whether local build commands match the checked-in toolchain files
- Normalizing CMake, Ninja, Make, Conan, or vcpkg signals before automation
- Planning sanitizer jobs for pull requests and nightly pipelines

## Key Workflows

1. Detect or normalize repository signals before making decisions.
2. Capture a machine-readable payload for reuse in CI, review, or planning steps.
3. Generate starter artifacts only after the baseline context is explicit.
4. Treat outputs as editable baselines, not immutable final implementations.

## Script Contracts

| Script | Purpose | Inputs | Outputs |
|---|---|---|---|
| `toolchain_detector.py` | Detect C++ toolchain, build system, and package-manager signals from a repository. | `--repo, --input, --format` | `text|json` or generated artifact |
| `cmake_project_analyzer.py` | Inspect a CMake project and extract targets, presets, options, and test signals. | `--repo, --cmake-file, --format` | `text|json` or generated artifact |
| `compile_commands_doctor.py` | Validate compile_commands.json availability and downstream tooling readiness. | `--repo, --file, --format` | `text|json` or generated artifact |
| `cpp_pipeline_generator.py` | Generate baseline GitHub Actions or GitLab CI YAML for C++ repositories. | `--platform, --repo, --input, --output, --profile, --format` | `text|json` or generated artifact |
| `sanitizer_matrix_planner.py` | Recommend sanitizer profiles and scheduling strategies for a C++ repository. | `--repo, --input, --scope, --format` | `text|json` or generated artifact |

Run any script with `--contract` to print the draft input/output contract as JSON.

## Commands

- `cpp-pipeline.md`
- `cpp-toolchain-doctor.md`

## References

- [references/cmake-detection-signals.md](references/cmake-detection-signals.md)
- [references/cpp-ci-matrix-patterns.md](references/cpp-ci-matrix-patterns.md)
- [references/sanitizer-profiles.md](references/sanitizer-profiles.md)
- [references/package-manager-notes.md](references/package-manager-notes.md)

## Expected Outputs

- `expected_outputs/` contains sample JSON, YAML, Markdown, and source-file baselines that match the CLI contracts.

## Design Notes

- Scripts use Python standard library only.
- `--format json` is intended for automation handoff.
- Generated artifacts are starter baselines that teams can refine per repository.
