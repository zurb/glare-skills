# Glare Skills Catalog (v2.0.0)

Quick reference for the **22 skills** in the slimmed Glare plugin. The marketplace now ships only the **Decision Map cluster** (Define · Measure · Focus · Lead, the spine of Glare) plus a cross-facet router. Other Glare sections (Design Review, Design Signals, Design Assessment, UX Metrics, Get Started extras) are available separately — see "Outside this install" at the bottom.

After installing, you don't invoke skills by name — Claude loads the right one when your conversation matches its description. This catalog helps you scan what's available.

**Install once:**

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

All 22 skills become available.

---

## Navigation (1)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-router` | mid-flow and lost — need a pointer to one specific skill in the Decision Map | "where should I go next" · "which Glare skill applies" · "I'm stuck and don't know where to start" |

---

## Decision Map (21)

The four facets connect into one decision flow: Define → Measure → Focus → Lead, looping back to Define.

### Decision Map parent

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-decision-map` | working with the four-facet flow that connects user needs to outcomes | "Decision Map" · "trace a decision from problem to outcome" · "how do the four facets connect" |

### Define (5) — agree on what matters before building

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-define` | in the Define area, multi-block question | "Credibility" · "who are we designing for" · "what should we measure" |
| `glare-define-user-needs` | working on the User Needs block (what users actually need) | "what user need does this solve" · "is this a want or a need" · "5 categories × 4 needs" |
| `glare-define-audience` | defining WHO their signals come from (the four-voice frame) | "who are we designing for" · "design for everyone is design for no one" |
| `glare-define-collecting` | in the Collecting block (instruments, techniques, tools) | "how do we gather evidence" · "should we use a survey or A/B test" |
| `glare-define-ux-metrics` | in the UX Metrics block (Attitudinal / Behavioral / Performance / Intelligence) | "high satisfaction + low completion" · "vanity vs actionable metrics" |

### Measure (5) — turn intuition into evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-measure` | producing evidence within the Measure area | "we believe that [change] for [audience] will [impact]" |
| `glare-measure-concepts` | working on the Concepts move (anchor intent before solutioning) | the 5-minute test · "what's the user need + business goal + signal here" |
| `glare-measure-hunches` | forming a falsifiable Hunch | "we believe…" · "we believe that [change] for [audience] will [impact] because [reason]" |
| `glare-measure-questioning` | drafting, critiquing, or organizing research questions | "Do people like our homepage?" · "Can users find pricing within 5 seconds?" |
| `glare-measure-findings` | in the Findings move (translate data into signals) | "what does this data mean" · "I have a number but no decision" |

### Focus (5) — turn signals into directional clarity

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-focus` | working in the Focus area, broad question | "v1 vs v2" · "competitor review" |
| `glare-focus-initiatives` | choosing what to pursue (the 10 initiative types) | "what should we focus on" · "Simplify Identity & Access vs Streamline Checkout" |
| `glare-focus-methods` | picking how to measure (the 13 method frames) | "HEART" · "RICE" · "Kano" · "JTBD" · "what method should we use" |
| `glare-focus-comparing` | benchmarking versions, competitors, or segments | "how do we compare" · "is this an improvement or just a change" |
| `glare-focus-decisions` | making the call (Implement / Refine / Test / Revisit / Do Not Pursue) | "what's the decision" · "Decision Record" · "meeting ended without a decision" |

### Lead (5) — translate design work into business evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-lead` | connecting design to business impact, broad question | "prove design ROI" · "executive narrative" |
| `glare-lead-business-goals` | anchoring to the 9 business pressures and 20 measurable goals | "Reduce churn" · "Lower support costs" · "Growth / Retention / Efficiency" |
| `glare-lead-mapping` | drawing the Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Goal) | "Chain of Proof" · "ladder our metrics" |
| `glare-lead-results` | running the Initiatives → Findings → Decisions → Outcomes loop | "outputs vs outcomes" · "leadership doesn't see what we're contributing" |
| `glare-lead-workflows` | translating signals into Sales / Marketing / Product / Eng / Strategy / Ops / Finance / Legal language | "how do I tell sales this is working" · "design ROI for Finance" |

---

## How activation works

Claude reads each skill's description (the YAML frontmatter `description:` field) and matches against the user's message. The richer the trigger phrasing in your message, the more reliably the right skill loads. Phrases in quotes above are pulled directly from each skill's description — using them in conversation is the fastest way to invoke a specific skill.

Parent skills (`glare-decision-map`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`) handle multi-bucket questions and route to children. If you're not sure which child applies, just stay in the parent — it covers enough surface to keep going.

When you're lost across facets, use `glare-router` — it diagnoses entry state and recommends ONE specific skill.

## Versioning

- Plugin version: **2.0.0** (slimmed to Decision Map core, 2026-05-07)
- Each `SKILL.md` carries `version`, `source_doc_version` (which Drive doc generation it was built from), and `last_rebuilt`. See `CHANGELOG.md` for the full history.

## Outside this install

The full Glare framework has additional sections that aren't part of this Decision Map–focused install. They're preserved for use as portable prompts and as a separate non-plugin skills folder:

| Topic | Where to find it |
|---|---|
| Design Review (SIGNAL framework, score a transcript) | `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-review-*` and `glare-design-review` |
| Design Signals (6-piece anatomy, Need/Use/Prefer/Adopt) | `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-signals-*` and `glare-design-signals` |
| Design Assessment (5 dimensions, scoring, reading patterns) | `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-assessment-*` and `glare-design-assessment` |
| UX Metrics (top-level framework, 4 types incl. Intelligence) | `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-ux-metrics/` |
| Get Started extras (onboarding, AI workflows, glossary) | `~/Desktop/zurb.nosync/skills/glare-skills-flat/glare-get-started`, `glare-create-first-signal`, `glare-how-glare-works`, `glare-ai-workflows`, `glare-coaching-advising`, `glare-proving-design-impact`, `glare-glossary` |

For portable prompt versions of any skill — to paste into ChatGPT, Gemini, Claude.ai, custom GPTs — see `~/Desktop/zurb.nosync/skills/glare-prompts-flat/`. 55 prompts named `<skill-name>.md` plus `_master-glare-framework.md`.

The master combined prompt at `glare-marketplace/glare-framework-prompt.md` still covers all sections in one shot — it wasn't slimmed when the marketplace was, since it's a separate distributable.
