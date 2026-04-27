---
title: "/cpp-design — Slash Command for AI Coding Agents"
description: "Scaffold C++ architecture outlines, ADRs, and boundary checks. Usage: /cpp-design [options]. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /cpp-design

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/cpp-design.md">Source</a></span>
</div>


Plan modular C++ architectures, analyze exported header surfaces, and record architecture decisions before implementation.

## Usage

```
/cpp-design [--repo <project-dir>] [--profile library|service|sdk|embedded]
/cpp-design adr --title "<decision>" [--status proposed|accepted|superseded]
```

## Scripts
- `engineering/cpp-design-and-architecture/scripts/cpp_architecture_scaffolder.py`
- `engineering/cpp-design-and-architecture/scripts/header_api_surface_analyzer.py`
- `engineering/cpp-design-and-architecture/scripts/dependency_boundary_checker.py`
- `engineering/cpp-design-and-architecture/scripts/cpp_adr_generator.py`

## Skill Reference
→ `engineering/cpp-design-and-architecture/SKILL.md`
