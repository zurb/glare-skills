# Glare AI Skills

Skills operationalize the Decision Map and core components of Glare.

Inside Glare, AI Skills provide reusable workflows teams use to structure decisions, evaluate direction, compare options, and generate stronger signals across product and design work.

## Why AI Skills Exist

AI accelerated how quickly teams can generate ideas, concepts, prototypes, flows, and experiments. What did not accelerate at the same pace was judgment.

Product and design teams now face a new problem: too much output and not enough structure for evaluating what deserves to move forward. Without structure, organizations accumulate more work, more opinions, and more uncertainty.

AI Skills are repeatable operational systems tied directly to the Decision Map. They help teams move from:

- Ideas to evaluation
- Prompts to workflows
- Feedback to signals
- Signals to decisions
- Decisions to measurable outcomes

Instead of relying on scattered prompts, inconsistent reviews, disconnected workflows, and subjective interpretation, teams apply shared operational patterns that make decision-making clearer and more scalable.

## AI Skills Across the Decision Map

### Define Skills

Structure user needs, clarify audiences, build UX metrics, frame stronger questions, and expose assumptions.

### Measure Skills

Evaluate concepts, structure experiments, analyze findings, generate Design Signals, and interpret user feedback.

### Focus Skills

Compare directions, benchmark performance, expose tradeoffs, prioritize opportunities, and guide product decisions.

### Lead Skills

Align stakeholders, operationalize workflows, connect outcomes to business goals, communicate evidence clearly, and scale decision systems across the organization.

## What's Inside (56 Skills)

| Section | Skills | What it covers |
|---|---:|---|
| **Get Started** | 7 | Onboarding, first signal, AI workflows, glossary |
| **Design Review** | 12 | SIGNAL framework (Surface, Identify, Ground, Navigate, Align, Lock), scoring, coaching |
| **Design Signals** | 5 | Signal anatomy, types (Need/Use/Prefer/Adopt), quality, capturing |
| **Decision Map** | 21 | Define / Measure / Focus / Lead (4 sub-skills each + parent) |
| **Design Assessment** | 9 | 5 org-maturity dimensions, scoring, pattern reading |
| **UX Metrics** | 1 | 4 metric types (Attitudinal, Behavioral, Performance, Intelligence) |
| **Navigation** | 1 | `glare-router` cross-section meta-skill |

## Install

### Claude Code (recommended)

```
/plugin marketplace add zurb/glare-skills
/plugin install glare@glare-marketplace
```

Then run `/reload-plugins`. Skills load under the plugin's name, as `glare:measure-hunches`, `glare:define-ux-metrics` and so on, and auto-trigger when your conversation matches their domain.

### Cursor, Codex, and other coding tools

```
npx skills add zurb/glare-skills
```

Since 4.0.0 the skill folders no longer carry a `glare-` prefix, so a flat install names them `measure-hunches` rather than `glare-measure-hunches`, and they can collide with other skills of the same name. Prefer the plugin install where your tool supports it.

### General LLMs (ChatGPT, Claude, Gemini)

Download a skill file and drop it into your LLM chat. The portable prompt versions live in [`glare-prompts-flat/`](../glare-prompts-flat/) -- one `.md` file per skill, plus a master prompt covering the entire framework.

## How AI Skills Work

Each skill is a self-contained prompt module with:

- **SKILL.md** -- YAML frontmatter with trigger conditions + step-by-step coaching instructions
- **reference.md** -- Compressed source material (worksheets, tables, worked examples)

You don't invoke skills by name. Claude reads each skill's description and loads the right one when your message matches. Examples:

| Say this | Loads this |
|---|---|
| "let's pick metrics for checkout" | `glare:define-ux-metrics` |
| "we need to benchmark v1 vs v2" | `glare:focus-comparing` |
| "how do I tell sales this is working?" | `glare:lead-workflows` |
| "we believe simplifying onboarding will improve activation" | `glare:measure-hunches` |
| "I'm stuck and don't know where to start" | `glare-router` |

A typical workflow might frame a user problem, generate multiple concepts, structure testing criteria, compare directions, analyze UX metrics, identify stronger signals, guide a recommendation, and prepare a decision review. Each skill focuses on a specific part. Together, they create systems for evaluation, comparison, interpretation, prioritization, alignment, and decision-making.

## Subset Packages

For teams that want a focused install rather than the full set:

| Package | Skills | Use case |
|---|---:|---|
| Core Decision Map | 21 | Just the Decision Map cluster + router |
| Design Review | 12 | Just the SIGNAL framework + scoring/rubric/coach |

## From AI Output to Organizational Clarity

Most organizations no longer struggle to generate ideas. They struggle to evaluate what matters, maintain alignment, reduce uncertainty, move with confidence, and preserve momentum.

AI Skills help teams operationalize decision-making itself. Over time, Skills become reusable systems organizations rely on to create clearer workflows, stronger signals, faster alignment, more measurable decisions, and scalable product and design operations.

This is where AI becomes more than output generation. It becomes part of the operational system teams use to guide direction, strengthen confidence, and make better product and design decisions.

## Version

**2.1.0** (2026-05-08) -- Full 56-skill set restored. See [CHANGELOG.md](CHANGELOG.md) for complete history.

Open source -- [github.com/zurb/glare-skills](https://github.com/zurb/glare-skills)
