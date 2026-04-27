# C++ Design and Architecture

Helps teams define clear module seams, public header policies, and architecture decision records before implementation details harden into expensive coupling.

## Quick Start

```bash
python3 scripts/cpp_architecture_scaffolder.py --help
```

## Included Tools

- `scripts/cpp_architecture_scaffolder.py` — Generate a starter C++ architecture outline with modules, layers, and boundary notes.
- `scripts/header_api_surface_analyzer.py` — Inspect public header surfaces and summarize stability, ownership, and dependency concerns.
- `scripts/dependency_boundary_checker.py` — Check whether declared module boundaries match observed include and dependency patterns.
- `scripts/cpp_adr_generator.py` — Generate Architecture Decision Record templates for C++ design choices.

## References

- `references/cpp-library-architecture.md`
- `references/error-model-decision-guide.md`
- `references/module-boundary-patterns.md`
- `references/public-header-policy.md`

## Assets

- `assets/cpp-adr-template.md`
- `assets/public-header-policy-template.md`
- `assets/package-layout-template.md`

## Installation

### Claude Code

```bash
cp -R engineering/cpp-design-and-architecture ~/.claude/skills/cpp-design-and-architecture
```

### OpenAI Codex

```bash
cp -R engineering/cpp-design-and-architecture ~/.codex/skills/cpp-design-and-architecture
```

### Gemini CLI

```bash
activate_skill(name="cpp-design-and-architecture")
```
