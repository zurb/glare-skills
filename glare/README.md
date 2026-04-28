# Glare (Claude Code plugin)

ZURB / Helio's Glare framework, packaged as 21 skills across 5 blocks. Install once and Claude will automatically load the right skill when you're working a specific part of the framework.

## What's inside

| Block | Parent | Buckets |
|---|---|---|
| Get Started | `glare-get-started` | (single skill) |
| Define | `glare-define` | `user-needs`, `audience`, `ux-metrics`, `collecting` |
| Measure | `glare-measure` | `concepts`, `hunches`, `questioning`, `findings` |
| Focus | `glare-focus` | `initiatives`, `methods`, `comparing`, `decisions` |
| Lead | `glare-lead` | `business-goals`, `workflows`, `mapping`, `results` |

Each skill has a `SKILL.md` with trigger conditions and step-by-step apply instructions, plus a `reference.md` with the compressed source material (worksheets, tables, worked examples) that the skill reads before answering.

## Install

Install happens through slash commands inside a Claude Code or Cowork session — there's no shell-level `claude plugin` CLI for this. Plugins install from a marketplace, and this plugin ships inside its own marketplace wrapper (the parent directory, `glare-marketplace/`). Two slash commands, in this order:

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

Then run `/reload-plugins` to activate. After that, the 21 skills auto-trigger when you mention their domain (e.g., "help me pick UX metrics for checkout" → `glare-define-ux-metrics`).

For a graphical manager instead of typed commands, run `/plugin` or `/plugins` and use the Discover / Manage panels.

## How it activates

Each skill's YAML description lists the triggers that make Claude load it. Examples:

- Ask "how do I start using Glare?" → `glare-get-started` fires
- Say "let's pick metrics for checkout" → `glare-define-ux-metrics`
- Say "we need to benchmark v1 vs v2" → `glare-focus-comparing`
- Say "how do I tell sales this is working?" → `glare-lead-workflows`

Parent skills (`glare-define`, `glare-measure`, etc.) handle multi-block questions and route to the right bucket child.

## Version

1.1.0 — aligned to Glare v1.1 (7-layer UX Honeycomb, Perceptual metric family, "Lead" facet name, four Focus buckets: Initiatives → Methods → Comparing → Decisions).
