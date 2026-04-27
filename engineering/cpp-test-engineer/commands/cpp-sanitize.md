---
name: cpp-sanitize
description: Plan sanitizer-aware C++ test lanes and fixture strategies. Usage: /cpp-sanitize [options]
---

# /cpp-sanitize

Separate fast and slow C++ sanitizer jobs so PR feedback stays quick while deeper nightly checks still run.

## Usage

```
/cpp-sanitize [--repo <project-dir>] [--scope pr|nightly|release] [--framework gtest|catch2|doctest]
```

## Scripts
- `engineering/cpp-test-engineer/scripts/sanitizer_test_planner.py`
- `engineering/cpp-test-engineer/scripts/cpp_fixture_generator.py`

## Skill Reference
→ `engineering/cpp-test-engineer/SKILL.md`
