# Source Manifest + Staleness Script — Design Proposal

**Status:** Proposal — not yet implemented
**Date:** 2026-05-13
**Goal:** Make doc → skill freshness measurable without forcing auto-regeneration

---

## What this solves

Today, when a Drive doc gets updated, nothing in the marketplace knows. We notice drift only when someone asks "is X up to date?" and we manually crawl Drive to find out.

Same problem from the other direction: when we refresh a skill, we don't record which Drive docs we pulled from — so the next person can't quickly see what to re-check.

This proposal adds two small pieces:

1. **Source manifest** — every SKILL.md says which Drive docs it derives from
2. **Staleness script** — a tool that reports which skills are behind their sources

Together they make drift visible without forcing automation.

---

## Part 1: Source Manifest

### Where it lives

In each `SKILL.md` frontmatter, add a new `sources:` field:

```yaml
---
name: glare-define-patterns
description: Use this skill when the user is in the Patterns block of the Define area...
version: 3.1.0
source_doc_version: v1.0 (Patterns) — created 2026-05-11
last_rebuilt: 2026-05-13

sources:
  - doc_id: 1PsRVou0ugrH-36X-m5rDz6fVNtkvv4FLSxpS-h5NvMw
    title: Glare | Define, Patterns v1.0
    drive_url: https://docs.google.com/document/d/1PsRVou0ugrH-36X-m5rDz6fVNtkvv4FLSxpS-h5NvMw/edit
    last_synced: 2026-05-11
---
```

Multiple sources allowed when a skill draws from several docs:

```yaml
sources:
  - doc_id: 1efa33k8WND9QEybJ9pWdXNZn-8vtOF5rvuOKZMf8TsU
    title: Glare | UX Metrics, Overview v1.32
    drive_url: https://...
    last_synced: 2026-05-10
  - doc_id: 1vuyPfZ0HfRO2x9aVdVLuw7SB0WTeglAEWiZJ8kbFtpQ
    title: Glare | UX Metrics, Attitudinal Metrics v1.32
    drive_url: https://...
    last_synced: 2026-05-10
  - doc_id: 1oM01UcVMZSDCOaUmS8PfojofDtc2bHff-0NZjhoHhKM
    title: Glare | Attitudinal Metrics, Appeal v1.32
    drive_url: https://...
    last_synced: 2026-05-11
  # ... 8 more individual metric docs
```

### Field semantics

- **`doc_id`** — Google Drive document ID (the canonical identifier, doesn't change on rename)
- **`title`** — human label, kept in sync with Drive title; used in reports
- **`drive_url`** — full URL for one-click opening
- **`last_synced`** — date the human pulled content from this doc into the skill

### What it doesn't do

- Doesn't constrain content. The skill author still chooses what to use from each source.
- Doesn't enforce coverage. A skill can cite 3 sources and use only 10% of one.
- Doesn't track which sections were used. (See "Phase 2: DERIVED/ADDED markers" below for that.)

---

## Part 2: Staleness Script

### Where it lives

`scripts/check-staleness.py` (sibling to the existing `validate-skills.py`)

### What it does

1. Walks every `SKILL.md` in `glare/skills/`
2. Parses frontmatter, extracts `sources:` list
3. For each source `doc_id`:
   - Calls Drive API (or MCP `get_file_metadata`) to fetch current `modifiedTime`
   - Compares to `last_synced` in manifest
4. Categorizes each skill:
   - **Up to date** — all sources' `modifiedTime ≤ last_synced`
   - **Behind** — at least one source has `modifiedTime > last_synced`
   - **No manifest** — skill has no `sources:` field (legacy)
5. Reports — doesn't modify files

### Output format

```
=== Glare Skill Staleness Report ===
Run date: 2026-05-13
Marketplace: ~/Desktop/zurb.nosync/skills/glare-marketplace

Summary
-------
Up to date:    28 skills
Behind:        32 skills
No manifest:    0 skills

Skills behind (most behind first)
---------------------------------
glare-getting-started
  Source: Get Started, Introduction v1.34
  Last synced: 2026-05-04 (9 days ago)
  Drive modified: 2026-05-11 (2 days ago)
  Drift: 7 days behind

glare-design-review
  Source: Design Review v1.34
  Last synced: 2026-05-04
  Drive modified: 2026-05-11
  Drift: 7 days behind

glare-review-surface
  Source: Design Review v1.34
  Last synced: 2026-05-04
  Drive modified: 2026-05-11
  Drift: 7 days behind
... (29 more)

Action
------
Run `python3 scripts/refresh-skill.py <skill-name>` to refresh one
Run `python3 scripts/refresh-batch.py --area design-review` to refresh a cluster
```

### Exit codes

- `0` — all up to date
- `1` — at least one skill behind
- `2` — at least one skill missing a manifest (data quality issue)

Useful for CI / pre-commit hooks.

### What it doesn't do

- Doesn't fetch source content
- Doesn't modify any skill files
- Doesn't auto-refresh
- Doesn't judge whether the diff is meaningful — just reports time gap

The reasoning: a doc edit might be a typo fix (no skill update needed) or a structural rewrite (full refresh needed). Only humans can tell. The script just makes the gap visible.

---

## Bootstrap: how to add manifests to existing 60 skills

One-time data entry exercise. Grab the current Google Drive folder and run the prompt below.

### AI Prompt

```
Go through this Drive folder [link], look at the latest content and compare between the content and the skills today
```

The agent walks the Drive folder, matches docs to skills by title/version/content, and writes the `sources:` blocks into each SKILL.md frontmatter. Human reviews any uncertain matches.

---

## How archival changes the design (important)

ZURB's doc workflow: **major updates = new doc with new Drive ID; old doc gets moved to an `_Archives/` subfolder.** This is actually cleaner than continuous editing — every version is preserved verbatim, and supersession is detectable.

It also means a `doc_id` in a manifest can become stale **two ways**:

1. **Edited in place** — same `doc_id`, `modifiedTime > last_synced`. Could be a typo fix or substantive change.
2. **Archived + superseded** — same `doc_id` still exists, but its parent folder is now `_Archives/`. There's a new doc in the original location with a higher version number.

The staleness script should detect both, with different urgency:

```
glare-define-patterns
  ⚠ Source archived: Glare | Define, Patterns v1.0 (moved to _Archives 2026-05-15)
  ⤷ Likely successor: Glare | Define, Patterns v1.34
     New doc_id: 1abc123def456...
     Sitting in: Decision Map / Define / (original location)
  Action: update manifest doc_id, then refresh skill content
```

vs.

```
glare-design-review
  Source edited: Glare | Design Review v1.34
  Last synced: 2026-05-04
  Drive modified: 2026-05-15
  Drift: 11 days behind (in-place edit, may or may not need refresh)
```

Archived = always needs human attention. In-place edit = sometimes a typo, sometimes substantive.

### Successor detection heuristic

When the script sees an archived source, it looks in the doc's previous parent folder for the likely successor:

1. Find docs in the same non-archive parent folder
2. Match by title prefix ("Glare | Define, Patterns v") ignoring the version suffix
3. Pick the one with the highest version number
4. Suggest as the successor; let human confirm in the manifest

False positives are fine — the human verifies before updating the manifest. The script just saves the lookup.

### Optional: keep history in the manifest

When updating to a successor, you could preserve the chain:

```yaml
sources:
  - doc_id: 1abc123def456...      # current
    title: Glare | Define, Patterns v1.34
    drive_url: https://...
    last_synced: 2026-05-15
    supersedes:
      - doc_id: 1PsRVou0ug...     # archived
        title: Glare | Define, Patterns v1.0
        archived: 2026-05-15
```

This makes the skill's source history visible — useful for understanding why content shifted between v1.0 and v1.34. Optional; can skip if you don't need it.

---

## Operating model

### Daily / weekly

Run `python3 scripts/check-staleness.py`. Eyeball the report.

If 0 skills behind: nothing to do.

If a few skills behind: open them, check if the Drive change matters, refresh if yes.

If many skills behind (like today, ~32 behind): batch refresh by section.

### When refreshing a skill manually

1. Read the source doc(s) for what changed
2. Update the relevant sections in `reference.md` (and `SKILL.md` body if needed)
3. Bump `last_synced` in frontmatter to today's date
4. Bump skill's `version` and `last_rebuilt` per existing convention
5. Run validator
6. Commit

### When the script reports an archived source

1. Open the suggested successor doc in Drive — verify it's actually the replacement
2. Update the manifest:
   - Replace `doc_id` and `title` with the successor's
   - Set `last_synced` to today's date
   - Optionally add a `supersedes:` entry preserving the old doc_id
3. Read the new doc — what changed in this version?
4. Refresh content per the manual refresh steps above
5. Bump `version` (likely a minor bump since it's a real content change)
6. Commit

The supersession case is when most real refreshes happen, since ZURB archives and replaces rather than editing in place for major changes.

### When the script reports `No manifest` skills

Backfill the manifest. Don't refresh content; just add the source pointers so future staleness checks work.

---

## Phase 2 (later): DERIVED / ADDED region markers

Once manifests + staleness work, the next layer is **section-level derivation tracking** inside `reference.md`. Use HTML comments:

```markdown
<!-- DERIVED FROM: 1PsRVou0ug...PsRVou0ug, sections "What is a Pattern" and "How patterns work" -->

A pattern is a recurring situation where similar conditions repeatedly produce similar behaviors and signals...

<!-- /DERIVED -->

## When to use

<!-- ADDED 2026-05-13 (audit pass) -->

- When the user is...

<!-- /ADDED -->
```

Then a future refresh script can:

1. Find DERIVED regions
2. Re-fetch source content for each
3. Diff against current
4. Replace only the DERIVED content
5. Leave ADDED regions untouched

Phase 2 is more work and not needed yet — the manifest + staleness script give you 80% of the value with much less infrastructure.

---

## Phase 3 (much later): refresh-skill.py

Once Phase 2 markers are in place, build `scripts/refresh-skill.py <skill-name>`:

1. Read skill's manifest
2. Fetch source content from Drive
3. For each DERIVED region in reference.md, replace with new content
4. Output a unified diff
5. Either auto-apply (if `--auto` and diff < threshold) or open for review

This is the path to "docs as source code" without losing skill structure. But Phase 1 (manifest + staleness) gets you most of the way and is the right next step.

---

## Effort estimate

| Phase | Work | Effort |
|---|---|---|
| **1.a** Source manifest schema + bootstrap on 32 stale skills | Mostly data entry | ~2-3 hours |
| **1.b** `scripts/check-staleness.py` | Single Python file, uses Drive MCP for metadata fetch | ~1-2 hours |
| **1.c** Add manifests to remaining 28 skills | Data entry | ~2 hours |
| **2.a** DERIVED/ADDED marker convention + manual conversion | Per-skill judgment | ~6-8 hours |
| **2.b** Validator update to enforce markers | Add to existing validator | ~1 hour |
| **3.a** `scripts/refresh-skill.py` | Diff + replacement logic | ~1 day |
| **3.b** `scripts/refresh-batch.py --area X` | Wrapper around refresh-skill | ~half day |

Phase 1 alone (~5 hours total) gives you the freshness signal. Phase 2 + 3 take you from "I know what's stale" to "I can refresh in one command."

---

## Decisions to make before building

1. **Where do source IDs come from?** Manual lookup from Drive URL, or scraped from the conversation/build history?
2. **What counts as "synced"?** The date the human last looked at the doc, or the date the doc was last processed by an agent?
3. **Stale threshold for warnings?** 7 days behind = warning, 14 days = error? Or strict (any drift = warning)?
4. **Where does the script live?** Local script run on demand, or scheduled (cron / GitHub Action)?
5. **Bootstrapping order — by section or by recency?** Stale-first gets value sooner; section-by-section is easier to verify.
6. **Should the manifest preserve `supersedes:` history?** Useful for understanding evolution; small extra metadata cost.
7. **Successor detection heuristic — title-prefix match, or also fuzzy on subtitle?** Title prefix works for ZURB's current naming (`Glare | <Section>, <Subsection> v<X>`); may need adjustment if naming changes.

These are all small calls — but worth deciding before writing the script so it doesn't need rework.

---

## Why this is the right next step

Today the marketplace can drift indefinitely without anyone noticing. The audit caught some of it (Perceptual vs Intelligence, Show vs Lead) but only because we ran a deliberate audit.

Source manifests + staleness make drift **continuous and visible** instead of episodic. That alone changes the maintenance pattern from "remember to check Drive" to "let the script tell me what to check."

Once that signal exists, the question of "should we auto-refresh?" becomes evidence-based, not philosophical. Maybe drift is rare enough that manual refresh is fine. Maybe it's frequent enough that Phase 3 is worth building. You won't know until you measure.
