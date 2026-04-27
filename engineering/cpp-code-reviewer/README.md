# C++ Code Reviewer

Turns C++ review concerns into repeatable checklists and risk reports so reviewers can focus on ownership, safety, compatibility, and maintenance costs.

## Quick Start

```bash
python3 scripts/cpp_review_checklist_generator.py --help
```

## Included Tools

- `scripts/cpp_review_checklist_generator.py` — Generate a C++-specific review checklist from repository context and profile selection.
- `scripts/abi_break_detector.py` — Flag public API and ABI change risks across headers and exported symbols.
- `scripts/include_graph_analyzer.py` — Summarize include graph hotspots and layering issues in a C++ repository.
- `scripts/clang_tidy_profile_generator.py` — Generate clang-tidy rule profiles for C++ library, service, or embedded contexts.
- `scripts/cpp_risk_scorer.py` — Score a C++ change set for review risk based on ownership, concurrency, and API surface signals.

## References

- `references/cpp-review-checklist.md`
- `references/lifetime-and-ownership.md`
- `references/exception-safety.md`
- `references/abi-compatibility.md`
- `references/include-hygiene.md`

## Installation

### Claude Code

```bash
cp -R engineering/cpp-code-reviewer ~/.claude/skills/cpp-code-reviewer
```

### OpenAI Codex

```bash
cp -R engineering/cpp-code-reviewer ~/.codex/skills/cpp-code-reviewer
```

### Gemini CLI

```bash
activate_skill(name="cpp-code-reviewer")
```
