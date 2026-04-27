---
title: "/cpp-pipeline — Slash Command for AI Coding Agents"
description: "Detect C++ toolchains and generate pipeline configs. Usage: /cpp-pipeline <detect|generate|sanitize> [options]. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /cpp-pipeline

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/cpp-pipeline.md">Source</a></span>
</div>


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
