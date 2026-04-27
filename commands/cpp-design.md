---
name: cpp-design
description: Scaffold C++ architecture outlines, ADRs, and boundary checks. Usage: /cpp-design [options]
---

# /cpp-design

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
