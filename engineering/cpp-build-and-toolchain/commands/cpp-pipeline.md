---
name: cpp-pipeline
description: Detect C++ toolchains and generate baseline CI/CD pipeline configs. Usage: /cpp-pipeline <detect|generate|sanitize> [options]
---

# /cpp-pipeline

Detect C++ build signals, emit normalized toolchain payloads, and generate starter CI/CD pipelines.

## Usage

```
/cpp-pipeline detect [--repo <project-dir>]
/cpp-pipeline generate --platform github|gitlab [--repo <project-dir>] [--profile baseline|sanitizers|release-matrix]
/cpp-pipeline sanitize [--repo <project-dir>] [--scope pr|nightly|release]
```

## Scripts
- `engineering/cpp-build-and-toolchain/scripts/toolchain_detector.py`
- `engineering/cpp-build-and-toolchain/scripts/cpp_pipeline_generator.py`
- `engineering/cpp-build-and-toolchain/scripts/sanitizer_matrix_planner.py`

## Skill Reference
→ `engineering/cpp-build-and-toolchain/SKILL.md`
