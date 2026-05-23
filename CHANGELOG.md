# Glare Marketplace Changelog

## 3.4.0 — 2026-05-22 (7th doc — Agent Operations split into its own file)

Bryan added a 7th source doc to the User Needs block: **Agent Operations**, a runtime contract written for AI Skills (not practitioners). Rather than fold it into `reference.md` alongside the other six sections, the skill splits it into a new file `agent-operations.md`. The highest-leverage rules are also duplicated into `SKILL.md` so they bind on every invocation, even without consulting the file.

### Why split

The other six sections (Overview, Techniques, Playbook, References, Decisions, Examples) are practitioner reference content — humans read them, discuss them, apply them. Agent Operations is operating instructions for the Skill itself — output schema, confidence vocabulary, input minimums, escalation triggers, guardrails. Different audience, different content type, different load discipline. Splitting it into a separate file makes the architectural distinction explicit and prevents the runtime contract from getting buried inside practitioner content.

### New file layout for `glare-define-user-needs`

```
glare-define-user-needs/
├── SKILL.md              ← always loaded; carries promoted AO rules
├── reference.md          ← 6 practitioner sections
└── agent-operations.md   ← NEW; AI Skill runtime contract
```

### What got promoted into SKILL.md

The Operating Rules section of `SKILL.md` now carries the binding rules so they load on every invocation regardless of whether `agent-operations.md` is consulted:

- **Required inputs minimums** — ≥2 input types + ≥1 behavioral signal for a Hunch; ≥3 input types + repeated behavioral evidence for an emerging need; cross-source reinforcement for a validated pattern
- **Output Contract** — the 10-field Primary User Need Output schema, in order
- **Confidence labels** — the 6-state vocabulary (Weak signal → Possible pattern → Hunch → Emerging need → Recurring signal → Validated pattern); the Skill must not invent alternatives or upgrade for cleaner results
- **Prohibited output behaviors** — recommending solutions before Hunch validation, inferring intent without behavioral evidence, flattening conflicting signals, hiding ambiguity, overstating confidence, collapsing distinct needs
- **Escalation triggers** — when to stop and surface to a human rather than auto-resolve

The full prescriptive detail (Runtime Flow, Classification Constraints, Transition Logic table, Failure Modes table, Ambiguity Handling, Guardrails, Multi-Agent Workflows, Human Judgment scope) lives in `agent-operations.md`.

### What this controls vs what it doesn't

Mechanically enforceable (will measurably change Skill output):
- Output schema — Skill will use the 10 fields in order
- Confidence vocabulary — Skill will use the 6 labels rather than inventing alternatives
- Input minimums + routing to Collecting on thin evidence
- Escalation triggers — Skill stops and surfaces uncertainty rather than producing an output it shouldn't

Aspirational (depends on Skill judgment):
- "Preserve evidence visibility," "preserve signal separation," "do not optimize for narrative smoothness" — only land if the Skill has multiple pieces of conflicting evidence in context AND chooses to keep them visible

The intended verification path: pick a real scenario (one of the 5 worked examples in Examples is a good candidate), run it through the Skill with and without AO loaded, diff the outputs. The interesting question is whether the difference is *the kind of difference Bryan wants* — more structured, more calibrated, less likely to over-confidently jump to a need without enough signals.

### Overview doc inconsistency surfaced

Bryan's v1.4 Overview doc shows a 6-section table with Agent Operations in the slot where Decisions used to be, implying AO replaces Decisions. The skill keeps both because they serve different audiences (Decisions = practitioner router; AO = Skill runtime contract) and have non-overlapping content. If the canonical framework decision is to deprecate Decisions, that's a one-line edit to remove the Decisions section from `reference.md`. Flagged in `reference.md` header for visibility.

### Source manifest

`SKILL.md` frontmatter now lists 7 source IDs (was 6):

```yaml
sources:
  - 1YBZeC...  Overview v1.4
  - 15P4dY...  Techniques v1.4
  - 1VrZ9k...  Playbook v1.4
  - 1l6QiT...  References v1.4
  - 1SlEfU...  Decisions v1.4
  - 1fZw7v...  Examples v1.4
  - 1NtO0P...  Agent Operations v1.4 (NEW)
```

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `3.4.0`
- Skill count unchanged: 60
- 59 skills still on the v3.1.0 audit-driven structure; 1 skill on the v3.4.0 seven-doc + split-file template
- `glare-marketplace-core` package also bumped 3.3.0 → 3.4.0; 5 sibling skill copies also synced
- `glare-packages/glare-full` (2.1.0) and `glare-packages/glare-decision-map` (2.0.0) still left at v2.x — multiple majors behind, sync/retire decision still pending

### Description trigger update

`SKILL.md` description now fires on agent-ops vocabulary: `"agent operations and AI Skill runtime contract"`, `"output schema"`, `"confidence labels"`, `"input minimums"`, `"escalation triggers"`. Length verified under the 1024-char limit.

---

## 3.3.0 — 2026-05-22 (6-doc template — User Needs full rebuild)

User Needs becomes the first skill on the **6-doc template** — Bryan added two new sections (Decisions, Examples) and refreshed the original four (Overview, Techniques, Playbook, References) from v1.3 → v1.4. This is the second iteration of the pilot pattern established in v3.2.0.

### What changed

**`glare-define-user-needs` refreshed to v3.3.0**

The skill's `reference.md` now has 6 DERIVED sections instead of 4, sourced from Bryan's v1.4 Drive docs:

| Section | Source | What changed |
|---|---|---|
| **Overview** | User Needs, Overview v1.4 (refreshed) | Adds explicit 6-section structure table; tightened prose on "Turning data into user understanding"; "User Needs Across Teams" expanded |
| **Techniques** | User Needs, Techniques v1.4 (refreshed) | New **Characteristics of Strong vs Weak User Needs** section; new **From User Needs to Measurable Signals** section; new **Connecting Techniques to the Playbook** handoff |
| **Playbook** | User Needs, Playbook v1.4 (refreshed) | Added **Example User Need Summary** short-form output; added **three prioritization questions** for multiple-needs cases (blocking / evidence / business outcome) |
| **References** | User Needs, References v1.4 (refreshed) | Replaced per-need bullets with **Needs at a Glance** tables — each of the 20 needs now has a core behavioral signal + primary UX metrics; added **How the Needs Work Together** explaining how Basics cascade, Trust+Personal interact, Impact+Feelings depend on lower layers |
| **Decisions** | User Needs, Decisions v1.4 (NEW) | 8 situation-based entries with "what to do" guidance + quick reference table — designed as the **front door** for "I'm stuck, where do I start in User Needs?" |
| **Examples** | User Needs, Examples v1.4 (NEW) | 5 worked examples (Useful · Reliable · Insightful · Efficient · Desirable), each showing Situation → Inputs → Hunch → What's not yet measured → What this orients → Decision. Plus a 5-row **Pattern Library** for AI calibration and a **Near-Miss** showing the cost of skipping Collecting/Patterns after a Hunch is formed |

Preserved at the end: `ADDED` regions for **When to use** and **Failure modes** (refreshed with new Decisions + Examples guidance).

### Bug fixes

- **22 → 20 needs.** Earlier versions of the skill described "22 individual need types." The canonical count is **20** (Basics 4 · Trust 4 · Personal 4 · Impact 4 · Feelings 4). Fixed throughout `SKILL.md` description, body, and `reference.md`.

### Skill description triggers updated

The skill's description now fires on the new vocabulary: `"worked examples"`, `"pattern library"`, `"near-miss"`, `"picking which part of User Needs to apply to a situation"`. This ensures Decisions and Examples actually pull the skill into context when the user describes those situations.

### Source manifest

`SKILL.md` frontmatter now lists 6 source IDs (was 4):

```yaml
sources:
  - 1YBZeC...  Overview v1.4
  - 15P4dY...  Techniques v1.4
  - 1VrZ9k...  Playbook v1.4
  - 1l6QiT...  References v1.4
  - 1SlEfU...  Decisions v1.4 (NEW)
  - 1fZw7v...  Examples v1.4 (NEW)
```

All 6 IDs in the manifest match the 6 `DERIVED FROM` markers in `reference.md` — verified by grep diff.

### Pattern this establishes

The v3.2.0 pilot proved that explicit inputs/outputs in a Playbook section makes skills produce more useful output. v3.3.0 extends that with two more roles:

- **Decisions** is the **router** — given a plain-language stuck situation, it points the user to the right part of the block before they read anything else
- **Examples** is the **calibration layer** — worked examples model what good output looks like, the Pattern Library compresses that for AI use, and the Near-Miss shows what failure looks like when validation is skipped

When the remaining 3 Define blocks (Audience, Collecting, Patterns) get their full 6-doc sets shipped, they'll follow the same pattern.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `3.3.0`
- Skill count unchanged: 60
- 59 skills still on the v3.1.0 audit-driven structure; 1 skill on the v3.3.0 six-doc template
- `glare-marketplace-core` package also bumped 3.1.0 → 3.3.0
- Note: `glare-packages/glare-full` (2.1.0) and `glare-packages/glare-decision-map` (2.0.0) received the file content but their package manifests were left at v2.x — those bundles are multiple majors behind and need a separate sync or retirement decision

---

## 3.2.0 — 2026-05-17 (4-doc template pilot — User Needs)

First skill on Bryan's new 4-doc template (Overview / Techniques / Playbook / References). This establishes the structural pattern that will scale to all 16 blocks of the framework once Bryan finishes shipping the remaining 4-doc sets.

### What changed

**`glare-define-user-needs` refreshed to v3.2.0**

The skill's `reference.md` was restructured around the new 4-section template, sourced from Bryan's 4 new Drive docs:

| Section | Source | What it covers |
|---|---|---|
| **Overview** | User Needs, Overview v1.3 (refreshed today) | Why this matters, 5-layer model, strong/weak needs, Decision Map fit |
| **Techniques** | User Needs, Techniques v1.3 (NEW) | Wants vs needs, 4 evaluation questions, Observation, Interviews, Five Whys, Process Mapping |
| **Playbook** | User Needs, Playbook v1.3 (NEW) | 11-row inputs table, pattern-to-need mapping, AI prompt structure, primary output template, multi-need format |
| **References** | User Needs, References v1.3 (NEW) + Reference/ subfolder | Category index + 22 individual user-need definitions with behavioral cues |

Plus the audit additions (When to use, Failure modes) preserved at the end.

### New machinery introduced

**DERIVED / ADDED region markers** — `reference.md` now uses HTML comments to delimit which sections come from Drive docs vs. which were added by the skill-builder:

```markdown
<!-- DERIVED FROM: <doc_id> -->
[content from source doc]
<!-- /DERIVED -->

<!-- ADDED 2026-05-13 (audit pass) -->
[content added by skill-builder]
<!-- /ADDED -->
```

This is the contract for the future refresh script — it will replace DERIVED regions when source docs update, leave ADDED regions untouched.

**Source manifest in SKILL.md frontmatter** — `glare-define-user-needs` now carries a `sources:` block listing the 4 Drive doc IDs it derives from, with per-source `last_synced` dates. This is the contract for the future staleness script:

```yaml
sources:
  - doc_id: 1EXcLG... (Overview v1.3) — last_synced: 2026-05-17
  - doc_id: 1WmQ_l... (Techniques v1.3) — last_synced: 2026-05-17
  - doc_id: 1JLtOo... (Playbook v1.3) — last_synced: 2026-05-17
  - doc_id: 1CeWhp... (References v1.3) — last_synced: 2026-05-17
```

See `SOURCE-MANIFEST-PROPOSAL.md` for the full design.

### Why pilot a single skill

Bryan's hypothesis: explicit inputs/outputs in the Playbook section will make the skills produce more useful outputs. We need a clean comparison — one skill on the new template alongside 59 skills on the old structure — so we can judge whether the difference is real before applying the template to all 16 blocks.

The other 3 Define blocks (Audience, Collecting, Patterns) have new folders today but only their Overview docs renamed — Techniques/Playbook/References haven't been created yet. We'll batch-refresh them when Bryan ships the full 4-doc sets.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `3.2.0`
- Skill count unchanged: 60
- 59 skills still on the audit-driven v3.1.0 structure; 1 skill on the new v3.2.0 template

### Downstream sync

- `glare-skills-flat/glare-define-user-needs/` — synced
- `glare-skills-hierarchical/decision-map/define/glare-define-user-needs/` — synced
- `glare-prompts-flat/glare-define-user-needs.md` — regenerated portable prompt

---

## 3.1.0 — 2026-05-13

Audit-driven cleanup pass + uniform skill version reset. No structural changes; this is a polish release driven by the v0.2 Skill Quality Rubric audit (see `audit/RUBRIC-RESULTS.md`).

### What changed

**1. Critical rules sections added to 9 parent SKILL.md files** — non-negotiable rules lifted out of buried numbered steps into a dedicated `## Critical rules` section. Sets the template for child skills:
- `glare-decision-map`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`
- `glare-design-review`, `glare-design-signals`, `glare-design-assessment`, `glare-ux-metrics`

**2. `## When to use` section added to all 60 reference.md files** — surfaces trigger and anti-trigger info that was scattered through prose. 3-5 "use when" bullets + 1 "don't use when" line per skill.

**3. `## Failure modes` section added to all 60 reference.md files** — each skill now names 3-5 specific ways it goes wrong in practice with cause and fix. Sourced from existing scattered material plus skill-domain extrapolation where source had no explicit failure content.

**4. Three broken handoff references renamed:**
- `glare-get-started` → `glare-getting-started` (typo)
- `glare-coaching-advising` → `glare-getting-started` (content absorbed into consolidated)
- `glare-proving-design-impact` → `glare-getting-started` (content absorbed into consolidated)

Affected SKILL.md files: `glare-design-assessment`, `glare-decision-map`, `glare-design-review`, `glare-assessment-scaling-influence`, `glare-assessment-using-results`, `glare-ux-metrics-mapping`.

**5. Symptoms-to-skill lookup table added to SKILLS-CATALOG.md** — 25 rows mapping common stuck patterns ("Meeting ended with no decision," "We have data but no decision," etc.) to entry-point skills.

### Uniform version reset

All 60 SKILL.md files reset to:
```yaml
version: 3.1.0
last_rebuilt: 2026-05-13
```

Previously skill versions had drifted across 1.3.0 / 1.4.0 / 2.2.0 / 2.3.0 / 3.0.0 from accumulated content edits. Reset to a clean baseline since reference.md content changed for all 60.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `3.1.0`
- Skill count unchanged: 60

### Audit impact

Predicted shift from the rubric:
- Section 3.5 (Critical rules): 48 Missing → ~0 Missing for 9 parents (children still need follow-up)
- Section 5.4 (When to use): 40 Missing → 0 Missing
- Section 5.6 (Failure modes): 13 Missing + 47 Partial → mostly Strong
- Section 8.1 (Graph integrity, broken handoffs): Partial → Strong
- Sections 9.4 + 10.1 (Discoverability): Partial → Strong
- System-wide Missing: 12% → ~3-4%

### What's next

Bucket-level skills (the ~30-40 children under the 9 parents) still don't have `## Critical rules` sections. The 9 parents now set the template — applying it to children is the next high-leverage pass.

---

## 2.3.0 — 2026-05-11

New Patterns block under Define. Decision Map and Define parent skills refreshed to v1.34/v1.1+patterns. Skill count: 65 → 66.

### New skill — `glare-define-patterns`

The Define area of the Decision Map now has **5 blocks** instead of 4: User Needs · Audience · Collecting · UX Metrics · **Patterns**. The new Patterns block reconnects raw metrics to the situations that surround behavior — same metric (e.g., long session duration) can mean engagement OR confusion OR hesitation OR comparison OR overload, and patterns help the team read the situation accurately rather than reacting to isolated data points.

Source: `Glare | Define, Patterns v1.0` (Drive, created today). Frontmatter: `version: 2.3.0`, `source_doc_version: v1.0 (Patterns) — created 2026-05-11`, `last_rebuilt: 2026-05-11`.

### Refresh — `glare-decision-map`

Refreshed from `Glare | Decision Map v1.34` (Drive, modified today). v1.34 changes vs prior v1.3:

- Opening framing tightened to "operational system" — the Decision Map is what *connects user needs, design signals, decisions, and outcomes across product and design work*.
- AI now explicitly named as one of the streams that fragment without the map ("research, testing, AI systems, reviews, metrics, stakeholders, business goals").
- Define facet description emphasizes context and recurring situations — dovetails with new Patterns block.
- Canonical worked example reframed from "simplify mobile navigation" → "simplify mobile onboarding" (same four-facet shape).

No structural shift to Measure / Focus / Lead. Loop and chain unchanged.

### Refresh — `glare-define`

Updated to describe **5 blocks** (added Patterns). Description triggers updated to include pattern-related phrasing. Handoffs section gained a route to `glare-define-patterns`.

### Source-doc note

The Define Overview Drive doc (`1bH6Of8XXB9aRyZ8I_GQ6ajeio-fYjlwhQp6CxUl-MUI`) is still v1.1 and still describes 4 blocks. The new Patterns block is sourced from its own v1.0 doc but isn't yet integrated into the parent Overview. The marketplace's `glare-define/reference.md` carries an explicit callout flagging this — the Overview should be re-edited upstream to reflect 5 blocks.

The Decision Map source doc header reads "May 10, 2026 v1.4" but the Drive title says "v1.34." Used `v1.34` per the file title; worth confirming the canonical label.

### Synced

All three changes copied to `glare-skills-flat/` to keep the archive in sync.

### Research Stacks expansion (not yet absorbed)

A new `Research Stacks/` subfolder under Define landed 2026-05-10 with 16 per-instrument .docx files (SUS · NPS · SEQ · CES · NASA-TLX · SUMI · QUIS · WAMMI · SUPR-Q · PSSUQ · PURE · UEQ · UX-Lite · L-DERLY · CASTLE · Usability Heuristics). These deepen the existing `glare-define-collecting` skill rather than need their own skills. Flagged for a future content refresh of `glare-define-collecting`.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `2.3.0`
- Skill count: 65 → 66

---

## 2.2.1 — 2026-05-11

Content refresh for `glare-measure-hunches` and `glare-measure-questioning` from updated Drive docs.

### glare-measure-hunches

Refreshed from `Glare | Measure, Hunches v1.0` (Sep 21, 2025; re-edited 2026-05-11). Net additions:
- Ideation framing (hunches + questions emerge from the wide ideation space)
- Helio integration callouts (attitudinal/behavioral metrics as leading indicators)
- 6 Benefits of Using Hunches as a labeled callout
- Full Resources list (Torres, Gothelf, MacCarthy, Stillman, Berger, Schirò, Zmijewski/Helio, Sokhan)

5-step process unchanged: Start with Context → Capture Initial Assumptions → Spot Opportunities → Form Your Hunch → Translate Into Questions. "We believe..." templates and weak/strong example preserved verbatim.

### glare-measure-questioning

Refreshed from `Glare | Measure, Questioning v1.1` (Oct 26, 2025; re-edited 2026-05-11). Net additions:
- 5-section scaffold: Getting Started → Begin Questioning → Make It Practical → See It in Action → Apply and Evolve
- 5 workflow routines: Weekly Discovery Review · Sprint Planning · Post-Test Reflection · Share the Questions Not Just Answers · Build a Question Library
- Question Library surfaced as a named concept (added to description and body)
- Helio integration callouts at Step 6 (UX metric alignment) and Step 8 (technique matching)
- Verbatim bias check
- Full Resources list (User Interviews, Maze, dscout, Envoy, PlaybookUX, UX Insight, Hotjar)

8-step process unchanged. 4 question types (People · Process · Product · Problem) and 3 modes (Exploratory · Evaluative · Comparative) preserved.

### Perceptual vs Intelligence taxonomy note

The v1.1 Questioning source doc still uses **Behavioral · Attitudinal · Performance · Perceptual** as the 4 UX-metric families. The marketplace UX Metrics framework v1.32 (added in v2.2.0) uses **Attitudinal · Behavioral · Performance · Intelligence** instead, with Perceptual content folded into Behavioral.

`glare-measure-questioning/reference.md` preserves the source-doc Perceptual wording (so users inside Questioning get the doc's own vocabulary) but adds a Source-doc note flagging the conflict and pointing handoffs to `glare-ux-metrics` for the v1.32 mapping. SKILL.md handoff section also notes this.

### Synced to glare-skills-flat

Both refreshed skill folders copied to `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-measure-hunches/` and `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-measure-questioning/`.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `2.2.1` (patch — content refresh, no structural change)
- Skill count unchanged: 65

---

## 2.2.0 — 2026-05-10

UX Metrics section expanded from a single overview skill into a full 10-skill library, driven by the v1.32 Drive content drop. Skill count: 56 → 65.

### New UX Metrics cluster

The previous `glare-ux-metrics` parent stays (refreshed to v1.32 content). 9 new sub-skills join it:

| Skill | Source doc |
|---|---|
| `glare-ux-metrics` (refreshed) | UX Metrics, Overview v1.32 |
| `glare-ux-metrics-what-is` | What is a UX Metric? v1.32 — four parts of a UX metric (User Attribute · Data Type · Collection Method · Benchmark) |
| `glare-ux-metrics-why` | Why UX Metrics Matter v1.32 — AI-acceleration argument, design needs its own signals, leading-indicator framing |
| `glare-ux-metrics-system` | Measurement System v1.32 — three patterns: Confusion Trap · Friction Wall · Trust Gap |
| `glare-ux-metrics-attitudinal` | Attitudinal Metrics v1.32 + 9-metric library: Appeal · Brand Score · Desirability · Expectations · Feeling · Loyalty · Satisfaction · Sentiment · Usefulness |
| `glare-ux-metrics-behavioral` | Behavioral Metrics v1.32 + 8-metric library: Completion · Comprehension · Effort · Engagement · Frequency · Intent · Success · Usability |
| `glare-ux-metrics-performance` | Performance Metrics v1.32 + 11-metric library: Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency |
| `glare-ux-metrics-stack` | UX Metrics Stack v1.32 — Design Stacks vs Research Stacks, four experience traps |
| `glare-ux-metrics-mapping` | Mapping Design Impact v1.32 — Situation → Intent → Outcomes → Results |
| `glare-ux-metrics-applying` | Applying UX Metrics v1.32 — eight operational use cases |

### Per-metric library

The three type-level skills (Attitudinal · Behavioral · Performance) each include a per-metric summary table inside their `reference.md`: definition, when to use, common mistakes, how it shows up. Compressed from 28 individual metric source docs (each 200KB-2MB) — full per-metric depth lives in Drive.

### Intelligence (4th metric type)

Mentioned in the refreshed `glare-ux-metrics` parent and listed in scope (recommendation quality · prompt effectiveness · AI guidance usefulness · adaptation quality · confidence calibration · workflow assistance) but no separate sub-skill yet. The v1.32 Drive folder ships full per-metric subfolders for the first three types only — Intelligence will get its own sub-skill once that content lands.

### Source-doc inconsistencies flagged (in reference.md notes)

- "Usefulness" doc body in the Attitudinal subfolder contains Sentiment content (copy-paste collision in source) — used the canonical type-level definition.
- Performance subfolder ships an "Abandonment Rate" doc and a duplicate "Completion" doc that overlaps Behavioral Completion — used the Overview list as canonical.
- Behavioral type-level doc carries a stale "v1.3" version banner inside a v1.32 file — cosmetic only.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `2.2.0`
- Skill count: 56 → 65

---

## 2.1.0 — 2026-05-08

**Restored full skill set.** v2.0.0 slimmed the marketplace to the Decision Map cluster + router (22 skills); v2.1.0 reverses that — the main marketplace ships everything Glare again. Subset packages (`glare-decision-map`, `glare-design-review`) live separately under `glare-packages/` for users who want a focused install.

### What's in the marketplace now (56 skills)

- **Get Started** (7) — `glare-get-started`, `glare-create-first-signal`, `glare-how-glare-works`, `glare-ai-workflows`, `glare-coaching-advising`, `glare-proving-design-impact`, `glare-glossary`
- **Design Review** (12) — `glare-design-review` parent + 6 SIGNAL letter skills (Surface · Identify · Ground · Navigate · Align · Lock) + Techniques + Scoring Model + Rubric + Coach + Run a Transcript
- **Design Signals** (5) — `glare-design-signals` parent + Components, Types, Quality, Capturing
- **Decision Map** (21) — `glare-decision-map` parent + Define / Measure / Focus / Lead each with 4 buckets + parent
- **Design Assessment** (9) — `glare-design-assessment` parent + 5 dimensions + Scoring + Reading Patterns + Using Results
- **UX Metrics** (1) — `glare-ux-metrics` (new top-level section, with 4 metric types including the new Intelligence type)
- **Navigation** (1) — `glare-router` cross-section meta-skill (refreshed for the full set)

### Why reverse the slim-down?

The Decision Map slim-down made sense as a tighter install for users who only want the spine. But after building three separate packages under `glare-packages/` (Full, Decision Map, Design Review) for testing the vercel-labs/skills install pattern, having two parallel "everything" containers (`glare-marketplace/` slim + `glare-packages/glare-full/`) was confusing. Cleaner: the main marketplace is canonical and ships all of Glare; the test packages live under `glare-packages/` as standalone subsets.

### Router refresh

`glare-router` reverted from the v2.0 slim version (knew 22 skills) to the broader v1.5 version that routes across the full set, then bumped to v2.1.0 with two updates:
- Skill count corrected to 56 throughout
- Added a new routing line for `glare-ux-metrics` (top-level UX Metrics section) and `glare-define-ux-metrics` (in-Define metric picking)

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `2.1.0`
- Description rewritten back to the 6-section, 56-skill framing

### Subset packages (in `glare-packages/`)

For users who want a focused install rather than the full marketplace:

| Package | Skills | Use case |
|---|---:|---|
| `glare-packages/glare-full/` | 56 | Same content as this marketplace, packaged as a standalone install |
| `glare-packages/glare-decision-map/` | 22 | Just the Decision Map cluster + router — for users who want the spine only |
| `glare-packages/glare-design-review/` | 12 | Just the SIGNAL framework + scoring/rubric/coach — for call evaluation use cases |

---

## 2.0.0 — 2026-05-07

**Major scope reduction.** The marketplace now ships only the Decision Map cluster (the spine of Glare) plus the router. Skill count dropped from 56 to 22.

### Why

The Decision Map (Define → Measure → Focus → Lead) is the canonical Glare framework. The other sections (Design Review with SIGNAL, Design Signals, Design Assessment, UX Metrics top-level, Get Started extras) are valuable but functionally independent — they don't need to be installed alongside the Decision Map for it to work. Slimming the install keeps the plugin focused on one mental model and lets users opt into other sections separately.

### What's in the marketplace now (22 skills)

- **`glare-decision-map`** (parent — the spine that connects all four facets)
- **Define area** (5): `glare-define` parent + `glare-define-user-needs`, `glare-define-audience`, `glare-define-collecting`, `glare-define-ux-metrics`
- **Measure area** (5): `glare-measure` parent + `glare-measure-concepts`, `glare-measure-hunches`, `glare-measure-questioning`, `glare-measure-findings`
- **Focus area** (5): `glare-focus` parent + `glare-focus-initiatives`, `glare-focus-methods`, `glare-focus-comparing`, `glare-focus-decisions`
- **Lead area** (5): `glare-lead` parent + `glare-lead-business-goals`, `glare-lead-mapping`, `glare-lead-results`, `glare-lead-workflows`
- **`glare-router`** (cross-facet navigation, rewritten for v2.0)

### Removed from marketplace (34 skills, preserved elsewhere)

Removed from `glare/skills/` but **still available in `~/Desktop/zurb.nosync/skills/glare-skills-flat/`** (full skill content) and `~/Desktop/zurb.nosync/skills/glare-prompts-flat/` (portable prompts):

- **Get Started extras** (7): `glare-get-started`, `glare-create-first-signal`, `glare-how-glare-works`, `glare-ai-workflows`, `glare-coaching-advising`, `glare-proving-design-impact`, `glare-glossary`
- **Design Review** (12): `glare-design-review` + 6 SIGNAL letter skills + techniques + scoring-model + rubric + coach + run-transcript
- **Design Signals** (5): `glare-design-signals` + components + types + quality + capturing
- **Design Assessment** (9): `glare-design-assessment` + 5 dimensions + scoring + reading + using-results
- **UX Metrics** (1): `glare-ux-metrics` (the new top-level section)

### Router rewrite

`glare-router` was rewritten to match the new scope. Now references only the 22 marketplace skills in its primary routing logic. A short "Outside the core marketplace" section in `reference.md` acknowledges the removed sections and points users to `glare-skills-flat/` for full content.

Stuck-pattern shortcuts re-mapped where possible:
- "Meeting ended with no decision" → `glare-focus-decisions` (was `glare-review-lock`)
- "I have a number but no decision" → `glare-measure-findings` (was `glare-signals-quality`)
- Patterns with no Decision Map analog (review-meeting symptoms, org-maturity diagnostics) routed via the "Outside the core" pointer

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `2.0.0`
- Description rewritten to reflect Decision Map focus
- Skill count: 56 → 22

### What hasn't changed

- All 22 remaining skills' content is unchanged from v1.6.0
- `glare-skills-flat/` and `glare-prompts-flat/` still hold all 56 skills and prompts
- `glare-framework-prompt.md` (master combined prompt at marketplace root) still covers the whole framework — see "Outside this install" note

### Migration

Anyone on v1.x with the full 56 skills installed will see the 34 non-core skills disappear after upgrade. To get them back as a separate install, point at `glare-skills-flat/`. Or stay on v1.6.0 if you need the full set.

---

## 1.6.0 — 2026-05-07

UX Metrics promoted to its own top-level section. New 4th metric type ("Intelligence") for AI-assisted experiences.

### New section — UX Metrics

UX Metrics now sits as a top-level Glare section alongside Get Started / Design Review / Design Signals / Decision Map / Design Assessment. Previously UX Metrics existed only as a block inside the Define area (`glare-define-ux-metrics`). The block stays — it's still where you pick metrics during the Define stage — but the broader framework now has its own home.

- **`glare-ux-metrics`** (new parent skill) — covers the 4-type taxonomy, why UX metrics matter, where they fit across all of Glare, and the planned sub-sections (Types, Metric Structures, Building Metrics, Operationalizing Metrics, Using with Design Signals, UX Metric Stacks, AI + Metrics).

The 7 planned sub-section docs in Drive are still mostly stubs as of 2026-05-07 — only the Overview and Why UX Metrics Matter are substantive. Sub-skills will be added as those docs land. Stub status flagged in `glare-ux-metrics/reference.md`.

### New 4th metric type — Intelligence

Source-of-truth shifted again on metric type count:
- v1.0 (Sept 2025): 3 types — Attitudinal · Behavioral · Performance
- v1.1: added Perceptual → 4 types
- v1.0 re-edit (2026-05-06): removed Perceptual → 3 types
- **v1.3 UX Metrics Overview (2026-05-07)**: adds **Intelligence** → 4 types

Intelligence metrics evaluate AI-assisted understanding, recommendations, and decision support quality (recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance). Goal: evaluate whether AI is improving outcomes, not just generating more output.

### Updated — `glare-define-ux-metrics`

- Added Intelligence as the 4th metric type.
- Reference now includes the full version-history walkthrough (3 → 4 → 3 → 4) so future readers don't get lost.
- Description updated to handoff to new `glare-ux-metrics` for broad framework questions; this skill stays focused on Define-stage metric picking.

### Source-doc inconsistencies flagged in v1.3 Overview

- The Drive Overview has Attitudinal/Behavioral bullet lists swapped under their headers. Per-metric URL slugs (e.g., `behavioral-metrics/completion`) are correct — the swap is in the bullet text only. Used URL slugs as the source of truth for metric assignments.
- Intelligence metrics listed by name only; per-metric URL slugs not yet enumerated.

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `1.6.0`
- Skill count: 55 → 56

---

## 1.5.1 — 2026-05-06

Cleanup release. Separated installable plugin content from portable prompt content.

### Removed from marketplace

- All 55 `prompt_chatgpt.md` files have been removed from `glare/skills/<skill>/`. Each skill folder now contains only `SKILL.md` and `reference.md` — exactly what the Claude plugin system needs.
- Marketplace footprint went from 165 skill files (55 × 3) to 110 (55 × 2).

### Where the prompts went

Portable prompt versions now live in their own sibling folder: `~/Desktop/zurb.nosync/skills/glare-prompts-flat/`. 55 files named `<skill-name>.md`, plus `_master-glare-framework.md`. Plus the master prompt remains at `glare-marketplace/glare-framework-prompt.md` (marketplace root) for one-stop access.

### Why

The plugin folder is now strictly the installable artifact. Portable prompts are a separate distributable for users who don't want to install a Claude plugin. Cleaner separation of concerns:

- `glare-marketplace/` — installable Claude plugin (skills only)
- `glare-skills-flat/` — same skills, no plugin wrapper, for sharing
- `glare-prompts-flat/` — portable prompts for ChatGPT/Gemini/etc.

### Updated

- `plugin.json` and `marketplace.json` bumped to `1.5.1`
- `glare/README.md` updated to point at `glare-prompts-flat/` for portable prompts
- `SKILLS-CATALOG.md` updated to point at `glare-prompts-flat/` for portable prompts

---

## 1.5.0 — 2026-05-06

Two changes: a YAML bug fix that was breaking 18 skills, and a new cross-section router skill.

### Bug fix — YAML frontmatter

The v1.4.0 description-trim pass introduced bare `Triggers:` substrings inside the description value of 18 skill files. YAML parses `Word:` as a new key, which broke skill loading on those files. Replaced with em-dashes (`Triggers —`) inside descriptions. All 55 skill `SKILL.md` files now parse cleanly.

Affected skills: `glare-define`, `glare-define-audience`, `glare-define-collecting`, `glare-define-user-needs`, `glare-define-ux-metrics`, `glare-focus`, `glare-focus-comparing`, `glare-focus-decisions`, `glare-focus-initiatives`, `glare-focus-methods`, `glare-lead-business-goals`, `glare-lead-mapping`, `glare-lead-results`, `glare-lead-workflows`, `glare-measure-concepts`, `glare-measure-findings`, `glare-measure-hunches`, `glare-measure-questioning`.

### New skill — `glare-router`

A cross-section navigation meta-skill. Triggers when users ask "where should I go next," "which Glare skill applies," "I'm stuck and don't know where to start," etc. Diagnoses entry state, asks 1-2 clarifying questions if needed, and recommends ONE specific skill out of the 55 (not a list).

Different from existing routing:
- `glare-get-started` is for first-time onboarding (canonical tour)
- Section parents (`glare-define`, `glare-design-review`, etc.) route within their section
- `glare-router` routes **across** the whole framework when the user is mid-flow and lost

Includes a stuck-pattern shortcut table covering the 18 most common "I'm lost" symptoms (e.g., "meeting ended with no decision" → `glare-review-lock`; "we have data but no decision" → `glare-signals-quality`; "team can't agree on what we're solving" → `glare-define-user-needs`).

3 files: `SKILL.md` (913-char description, valid YAML), `reference.md` (full routing table + 3 named flows + stuck-pattern shortcuts), `prompt_chatgpt.md` (standalone portable version).

### Plugin metadata

- `plugin.json` and `marketplace.json` bumped to `1.5.0`
- Description updated to mention 55 skills + router

---

## 1.4.0 — 2026-05-06

Define section content refresh from updated Drive source. Affects 5 skills (parent + 4 buckets); other 49 skills unchanged.

### What changed

- **glare-define-user-needs — major restructure.** The 7-layer UX Honeycomb (Findable / Accessible / Usable / Credible / Reliable / Valuable / Desirable) was replaced by **5 categories × 4 needs = 22 individual user-need types** in the Drive source:
  - **Basics** — Usable · Useful · Findable · Accessible
  - **Trust** — Credible · Secure · Reliable · Intuitive
  - **Personal** — Inclusive · Adaptable · Connected · Insightful
  - **Impact** — Valuable · Sustainable · Efficient · Scalable
  - **Feelings** — Desirable · Delightful · Engaging · Empowering

  All 22 needs now have a 1-2 paragraph synthesis in `reference.md` (definition, key questions, signal types, example metrics, common failure mode). A compatibility note explains the 7-layer → 5-category change for readers familiar with the older model.

- **glare-define-ux-metrics — restored to 3 metric types.** The today-edited Drive doc (`Glare | Define, UX Metrics v1.0` — modified 2026-05-06) explicitly defines **Attitudinal / Behavioral / Performance** with NO Perceptual type. Removed all Perceptual references. Comprehension/recognition (formerly under Perceptual) now sit under Behavioral. Reference includes a compatibility note explaining the v1.1 → v1.0 re-edit path. Added Helio integration callouts (attitudinal/behavioral as leading indicators in Helio; proxy stage). Quick checklist gained a 9th item: "Does it build momentum instead of slowing it down?"

- **glare-define-audience — per-voice depth.** Pulled in the four v1.1 sub-docs (Project Team, Stakeholders, Customers, Participants) for richer per-voice content. Four-voice frame intact (internal voices guide, external voices validate).

- **glare-define-collecting — technique catalog.** Added detail from the 12 collection technique docs (A/B, Card Sorting, Conversion Rate, Eye Tracking, Surveys, First Click, Multivariate, Clickstream, Heatmaps, Task Success, Web Analytics, Time on Task) plus Tools and Research Stacks docs. Five-step process intact.

- **glare-define — parent refresh** to reflect downstream changes.

### Version metadata

The 5 Define skills bumped to:
```yaml
version: 1.4.0
source_doc_version: v1.1   # (or "v1.0 (re-edited 2026-05-06)" for ux-metrics)
last_rebuilt: 2026-05-06
```

The other 49 skills remain at `version: 1.3.0` since their content didn't change. The plugin's overall version bumps to `1.4.0` because the marketplace as a whole has changed.

### Carry-forward

Cross-references to `glare-measure`, `glare-decision-map`, `glare-signals-*`, `glare-design-review`, `glare-design-assessment` all preserved. The parallel UX-metrics ↔ signal-types distinction (UX metric families ≠ Need/Use/Prefer/Adopt) preserved in UX Metrics SKILL.md.

---

## 1.3.0 — 2026-05-04

Major rebuild. Replaced the v1.1 5-block model (Get Started + Define / Measure / Focus / Lead) with the v1.3 5-section model (Get Started + Design Review + Design Signals + Decision Map + Design Assessment).

### Per-skill source-doc tracking

Every `SKILL.md` frontmatter now carries:

```yaml
version: 1.3.0          # plugin version this skill ships with
source_doc_version: v1.X # which Drive doc generation the skill was built from
last_rebuilt: YYYY-MM-DD  # when this rebuild happened
```

Distribution at v1.3.0:

| `source_doc_version` | Count | Skills |
|---|---:|---|
| **v1.3** (built fresh from v1.3 source) | 39 | All Get Started, Design Review, Design Signals, Design Assessment, Decision Map parent, all Focus |
| **v1.1** (refreshed framing, source unchanged) | 12 | All Define + all Measure + Lead Mapping + Lead Results |
| **v1.0** (refreshed framing, source unchanged) | 3 | Lead parent + Lead Business Goals + Lead Workflows |

When the Drive docs for Define / Measure / Lead get a v1.3 update, those skills' source-doc versions can be bumped accordingly.

### New sections

- **Design Review** (12 skills) — SIGNAL model: Surface · Identify · Ground · Navigate · Align · Lock + Techniques + Scoring Model + Rubric + Coach + Run a Transcript. Supersedes the standalone `signal-call-rubric` and `signal-call-coach` skills (those should be deleted from `~/Desktop/zurb.nosync/skills/`).
- **Design Signals** (5 skills) — Components (6-piece anatomy: Design intuition + UX metric + User need + Context + Business goal + Direction), Types (Need / Use / Prefer / Adopt), Quality (4 failure points), Capturing (4-stage flow).
- **Design Assessment** (9 skills) — Per-dimension docs for the 5 Glare Dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence) + Scoring Model + Reading Patterns + Using Results. **Note:** v1.3 abandoned the uniform 4×4 Define/Measure/Focus/Show grid — each dimension now has its own internal model (4 layers, 3 levels, 4 areas).
- **Decision Map** (1 new parent + 20 nested skills) — New parent skill connecting Define → Measure → Focus → Lead as one decision flow. The four facets are now nested under Decision Map.

### Updated content

- **Focus** fully rebuilt to v1.3:
  - Initiatives — replaced Goal/Outcome/Metric template with **10 named initiative types** (Simplify Identity & Access, Accelerate Onboarding, Optimize Navigation, Streamline Checkout, Increase Engagement, Personalize, Strengthen Collaboration, Elevate Marketing, Improve Content/Support, Expand Device/Context).
  - Methods — replaced 5 Levers with **13 method frames** + named-method catalog (HEART, RICE, Kano, EAST, JTBD, MoSCoW, Eisenhower, Service blueprint, etc.).
  - Comparing — 10 lenses → **12 comparison points** (added Geographies and User Lifecycle as distinct from Segments). Replaced 100-point normalization with tradeoff-surfacing process.
  - Decisions — replaced Advance/Refine/Kill/Pivot/Reprioritize with **5 tactical decision types** (Implement / Refine Design / Test Iteration / Revisit Later / Do Not Pursue) + strategic vs tactical distinction.
- **Show → Lead rename** completed across all Lead skills.

### Get Started expanded (1 → 7 skills)

Added: `glare-create-first-signal`, `glare-how-glare-works`, `glare-ai-workflows`, `glare-coaching-advising`, `glare-proving-design-impact`, `glare-glossary`.

### Portable prompts

Every skill now has a `prompt_chatgpt.md` (54 total). Master combined prompt at `glare-framework-prompt.md` regenerated for v1.3.

### Known gaps

- Drive docs for Define / Measure / Lead are still on v1.0/v1.1 — those skills are aligned to v1.3 framing but the underlying source content hasn't been refreshed by ZURB yet. When new docs land, bump `source_doc_version` accordingly.
- Drive doc titled "Glare | Focus, Compare v1.3" uses "Compare" but the Decision Map and Focus parent docs call the step "Comparing." Skill folder kept as `glare-focus-comparing` to preserve install paths. Worth a future canonical decision on terminology.

---

## 1.1.0 — 2026-04-24 *(prior release)*

21 skills across 5 blocks: Get Started + Define / Measure / Focus / Lead. 4 buckets per facet. Each skill: SKILL.md + reference.md + prompt_chatgpt.md (prompts added later, also at v1.1.0).
