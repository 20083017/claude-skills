---
title: "/cpp-review — Slash Command for AI Coding Agents"
description: "Generate focused C++ review checklists, ABI checks, and risk summaries. Usage: /cpp-review [options]. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /cpp-review

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/cpp-review.md">Source</a></span>
</div>


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
