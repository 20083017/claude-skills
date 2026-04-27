---
name: cpp-abi
description: Check public header changes for C++ ABI risk and clang-tidy policy drift. Usage: /cpp-abi [options]
---

# /cpp-abi

Focus on library compatibility before release by inspecting ABI-sensitive header changes and lint policy outputs.

## Usage

```
/cpp-abi [--repo <project-dir>] [--baseline <ref>] [--public-headers <dir>]
```

## Scripts
- `engineering/cpp-code-reviewer/scripts/abi_break_detector.py`
- `engineering/cpp-code-reviewer/scripts/clang_tidy_profile_generator.py`

## Skill Reference
→ `engineering/cpp-code-reviewer/SKILL.md`
