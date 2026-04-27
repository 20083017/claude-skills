---
name: cpp-review
description: Generate focused C++ review checklists, ABI checks, and risk summaries. Usage: /cpp-review [options]
---

# /cpp-review

Generate C++ review checklists that focus on ownership, ABI compatibility, include hygiene, and risk scoring.

## Usage

```
/cpp-review [--repo <project-dir>] [--diff <changes.diff>] [--profile library|service|embedded|general]
```

## Scripts
- `engineering/cpp-code-reviewer/scripts/cpp_review_checklist_generator.py`
- `engineering/cpp-code-reviewer/scripts/abi_break_detector.py`
- `engineering/cpp-code-reviewer/scripts/cpp_risk_scorer.py`

## Skill Reference
→ `engineering/cpp-code-reviewer/SKILL.md`
