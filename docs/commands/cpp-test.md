---
title: "/cpp-test — Slash Command for AI Coding Agents"
description: "Generate C++ test scaffolds, detect frameworks, and summarize coverage. Usage: /cpp-test <detect|generate|coverage> [options]. Slash command for Claude Code, Codex CLI, Gemini CLI."
---

# /cpp-test

<div class="page-meta" markdown>
<span class="meta-badge">:material-console: Slash Command</span>
<span class="meta-badge">:material-github: <a href="https://github.com/alirezarezvani/claude-skills/tree/main/commands/cpp-test.md">Source</a></span>
</div>


Detect GoogleTest/Catch2/doctest usage, generate C++ test skeletons, and normalize coverage output.

## Usage

```
/cpp-test detect [--repo <project-dir>]
/cpp-test generate --framework gtest|catch2|doctest [--file <spec.md>] [--output <test.cpp>]
/cpp-test coverage --input <coverage-dir-or-file> [--tool lcov|gcov|llvm-cov|auto]
```

## Scripts
- `engineering/cpp-test-engineer/scripts/cpp_test_framework_detector.py`
- `engineering/cpp-test-engineer/scripts/cpp_test_stub_generator.py`
- `engineering/cpp-test-engineer/scripts/cpp_coverage_adapter.py`

## Skill Reference
→ `engineering/cpp-test-engineer/SKILL.md`
