---
name: cpp-pipeline
description: Detect C++ toolchains and generate pipeline configs. Usage: /cpp-pipeline <detect|generate|sanitize> [options]
---

# /cpp-pipeline

Detect C++ build signals, generate CI baselines, and plan sanitizer lanes for modern toolchains.

## Usage

```
/cpp-pipeline detect [--repo <project-dir>]
/cpp-pipeline generate --platform github|gitlab [--repo <project-dir>] [--profile baseline|sanitizers|release-matrix]
/cpp-pipeline sanitize [--repo <project-dir>] [--scope pr|nightly|release]
```

## Scripts
- `engineering/cpp-build-and-toolchain/scripts/toolchain_detector.py` — detect toolchains and build signals
- `engineering/cpp-build-and-toolchain/scripts/cpp_pipeline_generator.py` — generate GitHub Actions or GitLab CI YAML
- `engineering/cpp-build-and-toolchain/scripts/sanitizer_matrix_planner.py` — recommend sanitizer profiles and job placement

## Skill Reference
→ `engineering/cpp-build-and-toolchain/SKILL.md`
