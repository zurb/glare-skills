# Skill Audit Results

We checked all 60 skills against the rubric. The rubric has 32 things per skill (does it have a clear name, is the description specific, does it have failure modes listed, etc.). That's **1,920 individual checks** total (60 skills × 32 things).

Each check got one of three grades:
- **Strong** — present and doing its job
- **Partial** — started but not finished, or inconsistent
- **Missing** — not there at all

---

## The headline

**Most checks passed. Two specific gaps repeat across nearly every skill.**

| Grade | Count | Percentage |
|---|---:|---:|
| Strong | 1,175 | 61% |
| Partial | 515 | 27% |
| Missing | 230 | 12% |

The 12% Missing isn't spread evenly — it clusters around two recurring problems (see below). Fix those and the Missing percentage drops dramatically.

---

## What's working well

- **Names and metadata** — every skill has a clear name and proper version info. No issues.
- **Descriptions** — almost all skills clearly say "use this when…" and give example phrases users would actually type.
- **Handoffs exist** — every skill points to siblings and parents. Nothing is an orphan or a dead-end.
- **Two clear entry points** — `glare-getting-started` for first-timers, `glare-master` when you're lost.

---

## What's broken

### #1 — Critical rules are buried

**48 out of 60 skills hide their critical rules inside numbered steps.** They should be in their own labeled section so Claude can't miss them.

What it looks like now:
> Step 4: Always check the metric against the canonical 28 (this is critical).

What it should look like:
> ## Critical rules
> - Recommendations must come from the canonical 28 metrics only.

This is the single most common problem. Fixing it on the 9 parent skills first would set a template for everyone else.

### #2 — No clear "when to use it" section in references

**40 out of 60 reference docs** don't have an explicit "When to use" heading. The info is there, but scattered. A standardized `## When to use` heading on every reference doc would fix this in one pass.

### #3 — Examples aren't specific enough

Across 60 skills, **only 14 had Strong examples** (real numbers, real situations). Most had generic ones ("a user might…") or none. Specific beats generic — "ran a 5-day onboarding test with 80 users, completion dropped from 72% to 48%" lands harder than "users had trouble with onboarding."

### #4 — Failure modes are implied, not named

Almost no skill has a labeled `## Failure modes` or `## Common mistakes` section. The traps are mentioned in passing inside other content, but never collected.

---

## Three broken handoff links

Three skills are referenced in handoffs but don't exist as folders:

- `glare-proving-design-impact`
- `glare-coaching-advising`
- `glare-get-started` ← almost certainly a typo for the actual folder `glare-getting-started`

Either rename the handoff references or build the missing skills. The third one is just a rename.

---

## Best skills (most polished)

1. `glare-review-surface` — 23 Strong / 2 Missing
2. `glare-decision-map` — 23 Strong / 3 Missing
3. `glare-define-patterns` — 23 Strong / 4 Missing
4. `glare-measure-hunches` — 22 Strong / 2 Missing
5. `glare-review-ground` — 22 Strong / 2 Missing

## Skills that need the most work

1. `glare-review-techniques` — 9 things missing
2. `glare-focus-initiatives` — 7 missing
3. `glare-ux-metrics-mapping` — 7 missing
4. `glare-ux-metrics-why` — 7 missing
5. `glare-lead-mapping` — 6 missing

---

## If you fix these 5 things, you fix half the problems

1. **Add a `## Critical rules` section** to the 9 parent skills (`glare-define`, `glare-measure`, `glare-focus`, `glare-lead`, `glare-design-review`, `glare-design-signals`, `glare-design-assessment`, `glare-ux-metrics`, `glare-decision-map`). Set a template the children follow.

2. **Add a `## When to use` section** to every reference.md. Standardized heading, 3-5 bullets per skill.

3. **Add a `## Failure modes` section** to every reference.md. List 3+ named ways the skill goes wrong.

4. **Rename or build the 3 broken handoff targets** (`glare-get-started`, `glare-coaching-advising`, `glare-proving-design-impact`).

5. **Add a "symptoms → skill" lookup table** to the catalog. Something like "meeting ended without a decision → `glare-review-lock`" or "we have data but no direction → `glare-signals-quality`." Helps newcomers find a skill from how they're feeling, not just from topic name.

That's it. Those 5 fixes alone would lift the overall score from "mostly good with consistent gaps" to "consistently good."

---

## What's in the audit folder

- **This file** — the human summary
- **`skills-rubric-summary.csv`** — one row per skill, totals per section (open in Excel/Google Sheets)
- **`skills-rubric-detail.csv`** — one row per skill, every individual item scored (open in Excel/Google Sheets if you want to drill into specifics)

The CSVs are the raw data. This file is the readable version.
