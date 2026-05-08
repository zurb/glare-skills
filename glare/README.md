# Glare Decision Map (Claude Code plugin)

ZURB / Helio's Glare Decision Map, packaged as 22 skills (Define → Measure → Focus → Lead, plus a router). Install once and Claude will automatically load the right skill when you're working a specific part of the framework.

This is the **slimmed v2.0 install** — just the Decision Map cluster + router. Other Glare sections (Design Review, Design Signals, Design Assessment, UX Metrics, Get Started extras) are available separately. See the bottom of this README.

## What's inside (22 skills)

| Section | Parent | Sub-skills |
|---|---|---|
| Decision Map | `glare-decision-map` | nested below: |
| ↳ Define (area) | `glare-define` | `define-user-needs`, `define-audience`, `define-ux-metrics`, `define-collecting` |
| ↳ Measure (area) | `glare-measure` | `measure-concepts`, `measure-hunches`, `measure-questioning`, `measure-findings` |
| ↳ Focus (area) | `glare-focus` | `focus-initiatives`, `focus-methods`, `focus-comparing`, `focus-decisions` |
| ↳ Lead (area) | `glare-lead` | `lead-business-goals`, `lead-workflows`, `lead-mapping`, `lead-results` |
| Navigation | `glare-router` | (cross-facet meta-skill — points to ONE skill when you're stuck) |

Each skill has a `SKILL.md` with trigger conditions and step-by-step apply instructions, plus a `reference.md` with the compressed source material (worksheets, tables, worked examples) that the skill reads before answering. Portable prompt versions of each skill (for pasting into ChatGPT, Gemini, Claude.ai, etc.) live in a sibling folder: `~/Desktop/zurb.nosync/skills/glare-prompts-flat/`.

## Install

Install happens through slash commands inside a Claude Code or Cowork session. Plugins install from a marketplace, and this plugin ships inside its own marketplace wrapper (the parent directory, `glare-marketplace/`). Two slash commands, in this order:

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

Then run `/reload-plugins` to activate. After that, the 22 skills auto-trigger when you mention their domain.

For a graphical manager instead of typed commands, run `/plugin` or `/plugins` and use the Discover / Manage panels.

## How it activates

Each skill's YAML description lists the triggers that make Claude load it. Examples:

- Say "let's pick metrics for checkout" → `glare-define-ux-metrics`
- Say "we need to benchmark v1 vs v2" → `glare-focus-comparing`
- Say "how do I tell sales this is working?" → `glare-lead-workflows`
- Say "we believe that simplifying onboarding will improve activation" → `glare-measure-hunches`
- Say "I'm stuck and don't know where to start" → `glare-router`

Parent skills (`glare-decision-map`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`) handle multi-block questions and route to the right child. When the entry point isn't obvious, `glare-router` diagnoses where you are and recommends ONE specific skill.

## Portable prompts

If you want to use a Glare skill in a tool that doesn't support Claude plugins (ChatGPT custom GPTs, Gemini Gems, Claude Projects), the portable prompt versions live in `~/Desktop/zurb.nosync/skills/glare-prompts-flat/` — 55 files named `<skill-name>.md`, plus a `_master-glare-framework.md` covering the whole framework (including the sections not in this install). The master prompt is also at `glare-framework-prompt.md` in this marketplace root.

## Outside this install

The full Glare framework includes additional sections that aren't shipped in this Decision Map–focused plugin. They're preserved in `~/Desktop/zurb.nosync/skills/glare-skills-flat/` (all 56 skills) and `~/Desktop/zurb.nosync/skills/glare-prompts-flat/` (all 56 portable prompts):

| Topic | Section |
|---|---|
| Improving design review meetings (SIGNAL framework, score a transcript) | Design Review (12 skills) |
| Building, evaluating, capturing design signals (6-piece anatomy, Need/Use/Prefer/Adopt) | Design Signals (5 skills) |
| Diagnosing where design impact breaks down (5 dimensions, scoring, reading patterns) | Design Assessment (9 skills) |
| Top-level UX Metrics framework (4 types incl. Intelligence) | UX Metrics (1 skill, expanding) |
| Onboarding extras (first signal, AI workflows, glossary, coaching) | Get Started extras (7 skills) |

## Version

**2.0.0** (2026-05-07) — slimmed to the Decision Map core + router.

Prior releases:
- 1.6.0 — added top-level UX Metrics section (Intelligence as 4th metric type)
- 1.5.1 — separated portable prompts from plugin into `glare-prompts-flat/`
- 1.5.0 — added `glare-router` cross-section meta-skill
- 1.4.0 — Define section content refresh from updated Drive
- 1.3.0 — major restructure to v1.3 5-section model

See `CHANGELOG.md` at the marketplace root for the full history.
