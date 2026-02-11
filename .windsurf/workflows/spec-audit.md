---
description: Validate spec consistency — check traceability, detect redundancy, find stale language, compare spec to disk layout, and verify documentation sync. Use before refining a spec or as a health check. Keywords: audit, validate, check, consistency, traceability, redundancy, drift, stale, health, spec, windloop.
---

## Audit a Spec

Pass the spec name in your message (e.g. `/spec-audit myfeature`).
If omitted, check `.windloop/index.md`. If only one active spec exists, use it.

Let SPEC be the resolved spec name.

1. Read `.windloop/SPEC/spec.md`, `design.md`, `tasks.md`.

2. **Traceability check**:
   - Extract all requirement IDs (R-numbers, NF-numbers) from spec.md
   - Extract all property IDs and their `Validates:` references from design.md
   - Extract all task `Requirements:` and `Properties:` references from tasks.md
   - Report: orphan requirements (no property), orphan properties (no task), broken references (nonexistent IDs)

3. **Redundancy check**:
   - Flag requirements in different sections that describe the same behavior
   - Flag properties where one is a strict subset of another
   - Flag requirements that are implementation details (belong in Constraints)

4. **Stale language check**:
   - Flag requirements using future tense ("should be", "must be", "currently") where the implementing task is done (`[x]`)
   - Flag goals checked off (`[x]`) but with unchecked sub-requirements

5. **Spec↔disk drift check**:
   - Parse the directory structure block from spec.md
   - Compare against actual repo layout
   - Flag: paths in spec but not on disk, significant files on disk but not in spec
   - Compare Data Models examples against actual files

6. **Documentation sync check**:
   - If project documentation files exist (README, architecture docs, agent docs), compare key facts (ports, tool versions, directory paths, command names) against spec.md
   - Flag inconsistencies

7. **Print findings report**:

```
╔══════════════════════════════════════════════════╗
║           SPEC AUDIT: [SPEC]                     ║
╠══════════════════════════════════════════════════╣

Traceability:
  ✓ N requirements, M properties, K tasks
  ⚠ [R-id] has no validating property (orphan)
  ✓ All property→task references valid

Redundancy:
  ⚠ [R-id] and [R-id] both describe "[behavior]"
  ⚠ [P-id] is a subset of [P-id]

Stale Language:
  ⚠ [R-id] says "[phrase]" but [T-id] is done

Spec↔Disk Drift:
  ✗ spec lists "[path]" — not found on disk
  ⚠ "[path]" exists on disk but not in spec

Documentation Sync:
  ✓ Key facts match across spec and docs
  ⚠ [doc] says "[value]" but spec says "[value]"

Summary: E errors, W warnings, I info
╚══════════════════════════════════════════════════╝
```

8. Suggest: "Run `/spec-plan SPEC refine` to act on these findings."
