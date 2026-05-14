# Skills Compression Recommendation

**Status:** Proposal — not yet implemented
**Date:** 2026-05-11
**Current state:** 60 skills across 6 components + master + decision-map parent
**Recommended target:** 37 skills (38% reduction)

---

## TL;DR

The Glare marketplace has grown to 60 skills with meaningful redundancy. **Recommend compressing to ~37 skills** by collapsing letter-by-letter SIGNAL skills, Design Assessment dimensions, Design Signals sub-skills, and UX Metrics utility skills into their respective parents. **Keep the Decision Map's 22 skills intact** — that's where workflow precision matters most.

---

## Where the bloat is

Four patterns of redundancy:

### Pattern 1: Parent + bucket duplication
Each cluster has a parent skill that covers what its children cover, just at a higher level. The Decision Map alone has 5 parents (`glare-decision-map`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`) — each one re-explains the section.

### Pattern 2: Letter-by-letter SIGNAL
6 separate skills for Surface · Identify · Ground · Navigate · Align · Lock. Each is ~80 lines of SKILL.md doing roughly the same shape (Core idea + How to apply + Handoffs).

### Pattern 3: Utility sprawl
Design Review has 5 utility skills (techniques, scoring, rubric, coach, run-transcript). Design Assessment has 3 (scoring, reading, using-results). UX Metrics has 4 framework skills (what-is, why, system, stack) plus 2 use-case skills (mapping, applying). All could fold up.

### Pattern 4: Define-UX-Metrics vs UX-Metrics-everything
`glare-define-ux-metrics` is partially redundant with the entire UX Metrics top-level section. Same content lives in two places.

---

## Three compression tiers

### Tier 1: Light compression (60 → ~40 skills)
- Collapse SIGNAL letter skills (6 → 1)
- Collapse Design Assessment dimensions (5 → 1)
- Collapse Design Signals sub-skills (4 → 1)
- Collapse UX Metrics framework skills (what-is/why/system → 1 parent)

### Tier 1.5: Recommended target (60 → ~37 skills)
All of Tier 1 plus collapse Design Review utility skills (techniques/rubric/coach into their letters), UX Metrics use-case skills (mapping/applying/stack into parent).

### Tier 2: Aggressive compression (60 → ~25 skills)
All of Tier 1.5 plus Decision Map facets become single skills (Define + 4 buckets → 1; same for Measure, Focus, Lead).

### Tier 3: Maximum compression (60 → ~10 skills)
All of Tier 2 plus each section becomes 1 skill total.

---

## Recommended: Tier 1.5 (~37 skills)

| Component | Now | After | What changes |
|---|---:|---:|---|
| Getting Started | 1 | 1 | unchanged |
| Master | 1 | 1 | unchanged |
| Decision Map | 22 | 22 | **keep all** — workflow depth is the framework's value, per-bucket triggering matters |
| Design Review | 12 | 3 | parent + scoring + run-transcript. Folds 6 SIGNAL letters into parent reference.md, folds techniques/rubric/coach into the SIGNAL letters |
| UX Metrics | 10 | 5 | parent + 3 type-level (att/beh/perf with full metric pages) + applying. Folds what-is/why/system/stack/mapping into parent |
| Design Signals | 5 | 1 | absorbs all 4 sub-skills (components, types, quality, capturing) into parent — small enough section that the 4 sub-skills don't earn their keep |
| Design Assessment | 9 | 4 | parent + scoring + reading + using-results. Folds 5 dimensions into parent reference.md (each dimension still gets a section, just no longer its own skill) |
| **Total** | **60** | **37** | **38% reduction** |

---

## Tradeoffs

### What this preserves
- Decision Map's 22 skills stay — that's where workflow precision matters most ("we believe…" → `glare-measure-hunches` directly)
- UX Metrics 28-metric library stays at full depth in the 3 type-level skills
- The 6-component mental model is unchanged

### What this costs
- Less precise triggering for SIGNAL letter–level questions (e.g., "we keep looping on opinion" used to fire `glare-review-ground` directly, now fires `glare-design-review` which has to find the right section)
- Reference.md files for collapsed parents get bigger (~30-50% larger) but stay well under context limits
- Users browsing the catalog see fewer entry points — could be a feature, not a bug

---

## What to NOT compress

- **Decision Map parents (5 of them).** They're real entry points users hit constantly. Don't merge `glare-define` into `glare-decision-map` — they trigger differently.
- **Per-metric library skills.** The 3 type-level UX Metrics skills with 28 full pages have unique value the parent can't absorb (would explode reference.md).
- **Getting Started.** Already consolidated; one skill is the right size.

---

## Other compression ideas to consider

### Replace `glare-define-ux-metrics` with a thin pointer
This skill is now mostly "go to UX Metrics for this." Could keep its description (so it traps Define-stage triggers) but make its body a 3-line route to the canonical UX Metrics skills. Saves duplicating the 28-metric content. Saves 0 skills but reduces maintenance burden.

### Drop the Master skill
`glare-master` was added to replace the router. But the 6 component parents already do most of the routing. If Getting Started and the parents are well-tuned, Master is mostly redundant. Could shave 1 more skill (60 → 36).

### Audit trigger overlaps
Some skills have overlapping triggers that suggest natural merge points:
- `glare-review-surface` and `glare-review-identify` both trigger on "what's the problem here"
- `glare-ux-metrics-system` and `glare-ux-metrics-mapping` both trigger on "how do metrics fit"
- Skills with very generic triggers ("when working with X") may have already been absorbed into parents

---

## Easiest wins to try first (test compression incrementally)

If you want to test compression incrementally rather than commit to all of Tier 1.5 at once, these three changes alone take you 60 → 41 with zero loss to Decision Map or UX Metrics depth:

1. **Design Review: 12 → 3** (collapse SIGNAL letters into parent)
2. **Design Assessment: 9 → 4** (collapse dimensions into parent)
3. **Design Signals: 5 → 1** (collapse all sub-skills into parent)

Could be done in one focused sweep. Validates the compression hypothesis before committing to fold UX Metrics utility skills too.

---

## How to execute (when ready)

Phase by component:

1. **Pick a component to compress** (e.g., Design Review: 12 → 3)
2. **For each child to be absorbed:**
   - Read its `SKILL.md` and `reference.md`
   - Add a new section to the parent's `reference.md` with that child's content
   - Update the parent's `SKILL.md` description to absorb the child's trigger phrases
   - Update the parent's `SKILL.md` "How to apply" body to mention the absorbed step
   - Delete the child's folder
3. **Update the parent's frontmatter:** bump version, add a note in `last_rebuilt`
4. **Update the hierarchical browse folder** (`glare-skills-hierarchical/`) to match
5. **Update Master / Router** if it referenced the deleted child skills by name
6. **Update SKILLS-CATALOG.md, CHANGELOG.md, README.md**
7. **Run the validator** (`python3 scripts/validate-skills.py`) — should pass
8. **Bump plugin version** — minor bump per component compressed, or wait until all done and bump major
9. **Test triggering** — invoke the absorbed child's known triggers, verify the parent loads cleanly

### Risks to watch for

- **Description bloat.** Each absorbed child's triggers need to fit in the parent's description. Parent descriptions may approach the 1024-char limit after multiple absorptions. Monitor with the validator.
- **Reference.md context cost.** A parent that absorbs 6 children might balloon to 800+ lines. Claude reads `reference.md` before answering — bigger reference = slower first response. Worth measuring.
- **Trigger collision.** When `glare-review-surface` and `glare-review-ground` merge into `glare-design-review`, their distinct triggers compete for relevance in the same description. Some user phrases may now route ambiguously.

---

## Open questions

- Is `glare-master` earning its keep, or should it merge into Getting Started?
- Should `glare-define-ux-metrics` be a pointer rather than a full skill?
- After compression, should the 6 component parents be the only "entry point" skills, with everything else discoverable through them?
- Is the 22-skill Decision Map cluster truly the right level of granularity, or are some buckets (e.g., the 4 Lead buckets) candidates for further compression?

---

## Decision

Not implemented yet — saved for future consideration.
