---
name: cpp-toolchain-doctor
description: Inspect compile_commands, CMake targets, and toolchain health for C++ repositories. Usage: /cpp-toolchain-doctor [options]
---

# /cpp-toolchain-doctor

Audit the state of a C++ toolchain workspace before onboarding clangd, clang-tidy, or CI automation.

## Usage

```
/cpp-toolchain-doctor [--repo <project-dir>] [--file <compile_commands.json>] [--format text|json]
```

## Scripts
- `engineering/cpp-build-and-toolchain/scripts/cmake_project_analyzer.py`
- `engineering/cpp-build-and-toolchain/scripts/compile_commands_doctor.py`

## Skill Reference
→ `engineering/cpp-build-and-toolchain/SKILL.md`
