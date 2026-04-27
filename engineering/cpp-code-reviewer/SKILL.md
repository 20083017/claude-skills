---
name: "cpp-code-reviewer"
description: "Use when reviewing C++ changes for ownership, ABI safety, include hygiene, clang-tidy policy, and risk hotspots in modern C++ libraries, services, and platform code."
---

# C++ Code Reviewer

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** C++ / Code Review / Static Analysis

## Overview

Turns C++ review concerns into repeatable checklists and risk reports so reviewers can focus on ownership, safety, compatibility, and maintenance costs.

## When to Use

- Preparing a focused review checklist for a risky C++ diff
- Auditing ABI compatibility before a library release
- Mapping include graph hotspots and layering violations
- Generating clang-tidy profiles aligned with repository policy

## Key Workflows

1. Detect or normalize repository signals before making decisions.
2. Capture a machine-readable payload for reuse in CI, review, or planning steps.
3. Generate starter artifacts only after the baseline context is explicit.
4. Treat outputs as editable baselines, not immutable final implementations.

## Script Contracts

| Script | Purpose | Inputs | Outputs |
|---|---|---|---|
| `cpp_review_checklist_generator.py` | Generate a C++-specific review checklist from repository context and profile selection. | `--repo, --diff, --profile, --format` | `text|json` or generated artifact |
| `abi_break_detector.py` | Flag public API and ABI change risks across headers and exported symbols. | `--repo, --baseline, --public-headers, --format` | `text|json` or generated artifact |
| `include_graph_analyzer.py` | Summarize include graph hotspots and layering issues in a C++ repository. | `--repo, --format` | `text|json` or generated artifact |
| `clang_tidy_profile_generator.py` | Generate clang-tidy rule profiles for C++ library, service, or embedded contexts. | `--profile, --output, --format` | `text|json` or generated artifact |
| `cpp_risk_scorer.py` | Score a C++ change set for review risk based on ownership, concurrency, and API surface signals. | `--repo, --diff, --format` | `text|json` or generated artifact |

Run any script with `--contract` to print the draft input/output contract as JSON.

## Commands

- `cpp-review.md`
- `cpp-abi.md`

## References

- [references/cpp-review-checklist.md](references/cpp-review-checklist.md)
- [references/lifetime-and-ownership.md](references/lifetime-and-ownership.md)
- [references/exception-safety.md](references/exception-safety.md)
- [references/abi-compatibility.md](references/abi-compatibility.md)
- [references/include-hygiene.md](references/include-hygiene.md)

## Expected Outputs

- `expected_outputs/` contains sample JSON, YAML, Markdown, and source-file baselines that match the CLI contracts.

## Design Notes

- Scripts use Python standard library only.
- `--format json` is intended for automation handoff.
- Generated artifacts are starter baselines that teams can refine per repository.
