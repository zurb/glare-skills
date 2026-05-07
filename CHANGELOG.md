# Glare Marketplace Changelog

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
