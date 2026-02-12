
## Audit a Spec

Pass the spec name (e.g. `/spec-audit myfeature`).
If omitted, use the **Spec Resolution** rules from SKILL.md.

Let SPEC be the resolved spec name and SPEC_DIR the resolved directory.

1. Read `SPEC_DIR/requirements.md`, `design.md`, `tasks.md`.

2. **Traceability check**:
   - Extract all requirement IDs (Requirement N, criteria N.N, NF N) from requirements.md
   - Extract all property IDs and their `Validates:` references from design.md
   - Extract all task Requirements and Properties references from tasks.md
   - Report: orphan requirements (no property), orphan properties (no task), broken references

3. **Redundancy check**:
   - Flag requirements in different sections that describe the same behavior
   - Flag properties where one is a strict subset of another
   - Flag requirements that are implementation details (belong in Constraints)

4. **Stale language check**:
   - Flag requirements using future tense where the implementing task is done (`[x]`)
   - Flag goals checked off but with unchecked sub-requirements

5. **Spec↔disk drift check**:
   - Parse the directory structure block from design.md
   - Compare against actual repo layout
   - Flag: paths in spec but not on disk, significant files on disk but not in spec

6. **Documentation sync check**:
   - Compare key facts in README, architecture docs, etc. against requirements.md and design.md
   - Flag inconsistencies

7. **Print findings report**:

```
╔══════════════════════════════════════════════════╗
║           SPEC AUDIT: [SPEC]                     ║
╠══════════════════════════════════════════════════╣

Traceability:
  ✓ N requirements, M properties, K tasks
  ⚠ Requirement [N] has no validating property
  ✓ All property→task references valid

Redundancy:
  ⚠ Requirement [N] and [M] both describe "[behavior]"
  ⚠ Property [N] is a subset of Property [M]

Stale Language:
  ⚠ Requirement [N] says "[phrase]" but task [N.N] is done

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
