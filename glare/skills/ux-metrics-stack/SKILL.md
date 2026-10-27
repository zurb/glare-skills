---
name: ux-metrics-stack
description: Use this skill when the user is combining multiple UX metrics together to evaluate a workflow or experience — phrases like "UX metric stack," "metric stack," "combine UX metrics," "stack of metrics," "Design Stack," "Research Stack," "feature findability stack," "onboarding stack," "checkout stack," "metrics that explain each other," "high completion plus low confidence," "Confusion Trap," "Friction Wall," "Trust Gap," "Commitment Check," "behavior plus attitudinal plus performance," or asks how 3-7 metrics work together. Also use when the user wants to build a reusable stack for a recurring workflow type, or compare workflows using a stack instead of single metrics. Do NOT use for single-metric definitions (use type sub-skills `glare:ux-metrics-attitudinal` / `glare:ux-metrics-behavioral` / `glare:ux-metrics-performance`), the broader framework (use `glare:ux-metrics`), or research-method picking (use `glare:define-collecting`).
version: 3.2.0
source_doc_version: v1.32
last_rebuilt: 2026-05-13
---

You are helping the user build and use **UX Metric Stacks** — reusable groups of 3-7 metrics combined together to evaluate a larger workflow, feature, product area, or research situation.

## Core idea

UX Metrics become more useful when they work together. A single metric can only show one small part of the experience. Most product and design problems are shaped by multiple signals happening at the same time — a workflow may technically function while users still hesitate, feel confused, lose confidence, struggle to complete tasks, or abandon entirely. A UX Metric Stack combines 3-7 metrics so the metrics begin explaining each other. A workflow may look successful at first because completion is high, engagement increased, and users finished — but deeper patterns may reveal trust weakened, effort increased, hesitation appeared, comprehension declined, confidence dropped. The stack helps teams understand not just whether users completed the workflow, but how the experience actually behaved underneath.

## Two kinds of stacks (v1.32)

- **Design Stacks** — organize UX metrics around a workflow, feature, or product experience. Examples — onboarding, navigation, dashboards, feature findability, AI workflows, mobile experiences, conversion flows. Instead of reviewing isolated screens, Design Stacks evaluate the larger workflow surrounding the experience.
- **Research Stacks** — organize UX metrics around a research method or evaluative process. They connect the method, the metrics, the findings, the interpretation, and the decisions. Instead of simply running a survey or usability test, the Research Stack helps teams understand what happened, why it happened, and what should change next. They support usability studies, benchmark comparisons, evaluative testing, workload analysis, and concept comparisons.

## Example — Feature Findability Design Stack

Combines: discoverability · comprehension · usability · confidence · hesitation. Together these metrics help teams understand whether users can find important features, understand what they do, and move through the workflow confidently — a much clearer signal than clicks or completion rates alone.

## The four experience traps a stack reveals

- **Confusion Trap** — users hesitate, guess, repeatedly scan the interface because they don't clearly understand what to do next. Comprehension drops, confidence weakens, navigation feels unclear, onboarding becomes overwhelming.
- **Friction Wall** — users understand the workflow, but effort, time, and repeated actions slow them down. Long task times, repeated clicks, extra workflow steps, growing frustration.
- **Trust Gap** — the workflow technically functions, but confidence and trust quietly weaken. AI systems, onboarding, fintech, healthcare, automation. Users continue using the workflow while quietly doubting it.
- **Commitment Check** — users complete the workflow, but signals reveal weak long-term momentum. Users may not return, loyalty weakens, adoption slows, recommendations decrease.

## Read the reference first

Before answering, read `reference.md` — it carries the full v1.32 UX Metric Stack content, both stack types in detail, the Feature Findability example, all four experience traps, the behavior-first stacking principle, and how stacks connect to Design Signals, AI Skills, Design Reviews, Decision Maps, and Design Assessments.

## How to apply

1. **Pick stack type from the question.** "How is this onboarding workflow performing?" → Design Stack. "How do I structure my usability study?" → Research Stack. The two are complementary, not competing.

2. **Default to 3-7 metrics across all three families.** Pick at least one Behavioral, at least one Attitudinal, and at least one Performance metric. If AI is in the experience, add at least one Intelligence-type signal once that sub-skill is built. Stacks below 3 metrics under-inform; stacks above 7 over-load and slow review.

3. **Lead with behavior first.** Inside Glare, stacks often begin with behavior because it surfaces what users actually do before assumptions about feelings or efficiency take over. Then layer attitudinal to explain *why*, and performance to expose the *cost*.

4. **Use the four traps as a diagnostic.** When the stack produces a pattern, name which trap matches — Confusion Trap, Friction Wall, Trust Gap, Commitment Check. Naming the trap is the difference between "the numbers are mixed" and "we have a Confusion Trap at step 3."

5. **Build reusable stacks for recurring workflow types.** Onboarding, navigation, dashboards, feature findability, AI workflows, mobile, e-commerce, marketing — each of these can have a default stack the team adapts rather than building from scratch each sprint.

6. **Hand off the stack into Design Signals.** Once the stack reveals a pattern, the next move is to wrap that pattern into a six-piece Design Signal so it carries direction (`glare:signals-components`).

## Saving to Ray

Optional. If the Ray MCP is connected (its tools include `list_projects` and `create_metric`), offer to save the stack's metrics to the project's Decision Map in Ray. If it isn't, skip this section: nothing else in the skill depends on it.

- Save each metric in the stack with `create_metric`, as `glare:define-ux-metrics` describes, and name the stack in each `definition` so the set reads as one.
- Link every metric to the same business goal (`goalIds`) so the stack shows up together under it.

Pick the project with `list_projects` and ask when more than one could fit; don't create a project unasked. Call `list_metrics` first so nothing is saved twice, and save only wording the person has approved.

## Handoffs

- For the broader UX Metrics framework, route to `glare:ux-metrics`.
- For the four parts of any individual UX metric, route to `glare:ux-metrics-what-is`.
- For per-metric definitions in each family, route to `glare:ux-metrics-attitudinal`, `glare:ux-metrics-behavioral`, `glare:ux-metrics-performance`.
- For UX metrics as a connected operational system across the org, route to `glare:ux-metrics-system`.
- For Define-stage metric picking on a specific decision (the four lenses, vanity vs actionable, etc.), route to `glare:define-ux-metrics`.
- For research-method picking and instrument selection, route to `glare:define-collecting`.
- For the six-piece Design Signal anatomy that wraps a stack into direction, route to `glare:signals-components`.
- For applying stacks across reviews, prioritization, and AI workflow evaluation, route to `glare:ux-metrics-applying`.
- For mapping a stack upward to product KPI to business KPI, route to `glare:lead-mapping`.
