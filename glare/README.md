# Glare (Claude Code plugin)

ZURB / Helio's Glare framework, packaged as 56 skills across 6 sections. Install once and Claude will automatically load the right skill when you're working a specific part of the framework.

## What's inside (56 skills)

| Section | Skills | Parent | Contents |
|---|---:|---|---|
| Get Started | 7 | `glare-get-started` | Onboarding, first signal, AI workflows, glossary |
| Design Review | 12 | `glare-design-review` | SIGNAL framework (Surface, Identify, Ground, Navigate, Align, Lock) + techniques, scoring, rubric, coach, transcript |
| Design Signals | 5 | `glare-design-signals` | Signal anatomy, types, quality, capturing |
| Decision Map | 21 | `glare-decision-map` | Define / Measure / Focus / Lead (parent + 4 sub-skills each) |
| Design Assessment | 9 | `glare-design-assessment` | 5 org-maturity dimensions + scoring, reading, using results |
| UX Metrics | 1 | `glare-ux-metrics` | 4 metric types (Attitudinal, Behavioral, Performance, Intelligence) |
| Navigation | 1 | `glare-router` | Cross-section meta-skill — points to ONE skill when you're stuck |

Each skill has a `SKILL.md` with trigger conditions and step-by-step apply instructions, plus a `reference.md` with the compressed source material (worksheets, tables, worked examples) that the skill reads before answering.

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

For tools that don't support Claude plugins (ChatGPT, Gemini, Claude Projects), portable prompt versions are available as individual `.md` files plus a master prompt covering the whole framework.

## Version

**2.1.0** (2026-05-08) — Full 56-skill set restored across all 6 sections.

See [CHANGELOG.md](../CHANGELOG.md) at the marketplace root for the full history.
