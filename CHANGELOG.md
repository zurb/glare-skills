# Glare Marketplace Changelog

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
