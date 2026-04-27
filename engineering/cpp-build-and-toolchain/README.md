# C++ Build and Toolchain

Detects C++ toolchains and build signals, normalizes them into machine-readable payloads, and generates practical CI baselines for multi-compiler repositories.

## Quick Start

```bash
python3 scripts/toolchain_detector.py --help
```

## Included Tools

- `scripts/toolchain_detector.py` — Detect C++ toolchain, build system, and package-manager signals from a repository.
- `scripts/cmake_project_analyzer.py` — Inspect a CMake project and extract targets, presets, options, and test signals.
- `scripts/compile_commands_doctor.py` — Validate compile_commands.json availability and downstream tooling readiness.
- `scripts/cpp_pipeline_generator.py` — Generate baseline GitHub Actions or GitLab CI YAML for C++ repositories.
- `scripts/sanitizer_matrix_planner.py` — Recommend sanitizer profiles and scheduling strategies for a C++ repository.

## References

- `references/cmake-detection-signals.md`
- `references/cpp-ci-matrix-patterns.md`
- `references/sanitizer-profiles.md`
- `references/package-manager-notes.md`

## Installation

### Claude Code

```bash
cp -R engineering/cpp-build-and-toolchain ~/.claude/skills/cpp-build-and-toolchain
```

### OpenAI Codex

```bash
cp -R engineering/cpp-build-and-toolchain ~/.codex/skills/cpp-build-and-toolchain
```

### Gemini CLI

```bash
activate_skill(name="cpp-build-and-toolchain")
```
