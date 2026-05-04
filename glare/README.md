# Glare (Claude Code plugin)

ZURB / Helio's Glare framework v1.3, packaged as 54 skills across 5 sections. Install once and Claude will automatically load the right skill when you're working a specific part of the framework.

## What's inside

| Section | Parent | Sub-skills |
|---|---|---|
| Get Started | `glare-get-started` | `create-first-signal`, `how-glare-works`, `ai-workflows`, `coaching-advising`, `proving-design-impact`, `glossary` |
| Design Review (SIGNAL) | `glare-design-review` | `review-surface`, `review-identify`, `review-ground`, `review-navigate`, `review-align`, `review-lock`, `review-techniques`, `review-scoring-model`, `review-rubric`, `review-coach`, `review-run-transcript` |
| Design Signals | `glare-design-signals` | `signals-components`, `signals-types`, `signals-quality`, `signals-capturing` |
| Decision Map | `glare-decision-map` | nested below: |
| ↳ Define (area) | `glare-define` | `define-user-needs`, `define-audience`, `define-ux-metrics`, `define-collecting` |
| ↳ Measure (area) | `glare-measure` | `measure-concepts`, `measure-hunches`, `measure-questioning`, `measure-findings` |
| ↳ Focus (area) | `glare-focus` | `focus-initiatives`, `focus-methods`, `focus-comparing`, `focus-decisions` |
| ↳ Lead (area) | `glare-lead` | `lead-business-goals`, `lead-workflows`, `lead-mapping`, `lead-results` |
| Design Assessment | `glare-design-assessment` | `assessment-organizing-work`, `assessment-managing-complexity`, `assessment-building-proof`, `assessment-guiding-decisions`, `assessment-scaling-influence`, `assessment-scoring`, `assessment-reading`, `assessment-using-results` |

Each skill has a `SKILL.md` with trigger conditions and step-by-step apply instructions, plus a `reference.md` with the compressed source material (worksheets, tables, worked examples) that the skill reads before answering. Each also has a `prompt_chatgpt.md` — a portable system prompt you can paste into ChatGPT, Gemini, Claude.ai, or any other chat tool to get the same behavior outside Claude Code.

## Install

Install happens through slash commands inside a Claude Code or Cowork session — there's no shell-level `claude plugin` CLI for this. Plugins install from a marketplace, and this plugin ships inside its own marketplace wrapper (the parent directory, `glare-marketplace/`). Two slash commands, in this order:

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

Then run `/reload-plugins` to activate. After that, the 54 skills auto-trigger when you mention their domain (e.g., "help me pick UX metrics for checkout" → `glare-define-ux-metrics`, "evaluate this design review transcript" → `glare-review-rubric`, "what's our team's design maturity" → `glare-design-assessment`).

For a graphical manager instead of typed commands, run `/plugin` or `/plugins` and use the Discover / Manage panels.

## How it activates

Each skill's YAML description lists the triggers that make Claude load it. Examples:

- Ask "how do I start using Glare?" → `glare-get-started` fires
- Say "let's pick metrics for checkout" → `glare-define-ux-metrics`
- Say "we need to benchmark v1 vs v2" → `glare-focus-comparing`
- Say "how do I tell sales this is working?" → `glare-lead-workflows`
- Say "score this design review transcript" → `glare-review-rubric`
- Say "is this a usable signal?" → `glare-signals-quality`
- Say "where is design impact breaking down" → `glare-design-assessment`

Parent skills (`glare-design-review`, `glare-design-signals`, `glare-decision-map`, `glare-design-assessment`, plus the four facet parents) handle multi-block questions and route to the right child.

## Portable prompts

If you want to use a Glare skill in a tool that doesn't support Claude plugins (ChatGPT custom GPTs, Gemini Gems, Claude Projects), each skill folder contains a `prompt_chatgpt.md` — a self-contained system prompt you can paste in. There's also a master combined prompt at the marketplace root (`glare-framework-prompt.md`) covering the whole framework in one shot.

## Version

1.3.0 — aligned to Glare v1.3:

- 5-section structure (Get Started + Design Review + Design Signals + Decision Map + Design Assessment) replaces the old 5-block model
- New **Design Review** section based on the **SIGNAL** model (Surface / Identify / Ground / Navigate / Align / Lock) — folds in and supersedes the standalone `signal-call-rubric` and `signal-call-coach` skills
- New **Design Signals** section with 6-piece signal anatomy (Design intuition + UX metric + User need + Context + Business goal + Direction) and outcome-keyed signal types (Need / Use / Prefer / Adopt)
- New **Design Assessment** section with full per-dimension docs for the five Glare Dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence)
- New **Decision Map** parent skill connecting Define → Measure → Focus → Lead as one decision flow
- Focus area fully refreshed to v1.3 (10 initiative types, 13 method frames, 12 comparison points, 5 tactical decision types)
- Define / Measure / Lead refreshed for v1.3 alignment (descriptions, handoffs, vocabulary blocks) — source content unchanged from v1.0/v1.1
- Show → Lead rename completed across all Lead skills
