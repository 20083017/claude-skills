---
name: cpp-review
description: Generate focused C++ review checklists and risk summaries. Usage: /cpp-review [options]
---

# /cpp-review

Create C++ review checklists that emphasize ownership, safety, ABI, and maintainability.

## Usage

```
/cpp-review [--repo <project-dir>] [--diff <changes.diff>] [--profile library|service|embedded|general]
```

## Scripts
- `engineering/cpp-code-reviewer/scripts/cpp_review_checklist_generator.py`
- `engineering/cpp-code-reviewer/scripts/cpp_risk_scorer.py`
- `engineering/cpp-code-reviewer/scripts/include_graph_analyzer.py`

## Skill Reference
→ `engineering/cpp-code-reviewer/SKILL.md`
