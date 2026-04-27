---
name: "cpp-design-and-architecture"
description: "Use when designing C++ library boundaries, public header policy, dependency seams, or architecture decision records for reusable systems, SDKs, platform layers, and maintainable modular codebases."
---

# C++ Design and Architecture

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** C++ / Architecture / API Design

## Overview

Helps teams define clear module seams, public header policies, and architecture decision records before implementation details harden into expensive coupling.

## When to Use

- Designing a new reusable C++ library or SDK layout
- Clarifying dependency boundaries before a refactor
- Producing ADRs for error handling, packaging, or public API policy
- Auditing public headers and package layout against a desired architecture

## Key Workflows

1. Detect or normalize repository signals before making decisions.
2. Capture a machine-readable payload for reuse in CI, review, or planning steps.
3. Generate starter artifacts only after the baseline context is explicit.
4. Treat outputs as editable baselines, not immutable final implementations.

## Script Contracts

| Script | Purpose | Inputs | Outputs |
|---|---|---|---|
| `cpp_architecture_scaffolder.py` | Generate a starter C++ architecture outline with modules, layers, and boundary notes. | `--repo, --profile, --output, --format` | `text|json` or generated artifact |
| `header_api_surface_analyzer.py` | Inspect public header surfaces and summarize stability, ownership, and dependency concerns. | `--repo, --public-headers, --format` | `text|json` or generated artifact |
| `dependency_boundary_checker.py` | Check whether declared module boundaries match observed include and dependency patterns. | `--repo, --format` | `text|json` or generated artifact |
| `cpp_adr_generator.py` | Generate Architecture Decision Record templates for C++ design choices. | `--title, --status, --output, --format` | `text|json` or generated artifact |

Run any script with `--contract` to print the draft input/output contract as JSON.

## Commands

- `cpp-design.md`
- `cpp-adr.md`

## References

- [references/cpp-library-architecture.md](references/cpp-library-architecture.md)
- [references/error-model-decision-guide.md](references/error-model-decision-guide.md)
- [references/module-boundary-patterns.md](references/module-boundary-patterns.md)
- [references/public-header-policy.md](references/public-header-policy.md)

## Assets

- [assets/cpp-adr-template.md](assets/cpp-adr-template.md)
- [assets/public-header-policy-template.md](assets/public-header-policy-template.md)
- [assets/package-layout-template.md](assets/package-layout-template.md)

## Expected Outputs

- `expected_outputs/` contains sample JSON, YAML, Markdown, and source-file baselines that match the CLI contracts.

## Design Notes

- Scripts use Python standard library only.
- `--format json` is intended for automation handoff.
- Generated artifacts are starter baselines that teams can refine per repository.
