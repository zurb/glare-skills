---
name: glare-define-patterns
description: Use this skill when the user is working on the Patterns block of the Define area — recognizing recurring situations before weak decisions gain momentum. Triggers — "patterns," "pattern library," "we keep seeing the same problem," "engagement up but trust down," "completion high but support tickets rise," "AI produces more but we trust it less," "situations create meaning." Also use for the four pattern types — User Patterns (hesitation, abandonment, comparison paralysis), Workflow Patterns (review cycles, late validation, siloed optimization), Signal Patterns (engagement up while trust down, usability up while retention weakens), AI Workflow Patterns (faster output, weaker evaluation, overproduction). Do NOT use when naming user needs (use `glare-define-user-needs`), picking audience (`glare-define-audience`), gathering evidence (`glare-define-collecting`), or picking metrics (`glare-define-ux-metrics`). For broad Define, use `glare-define`. For the Decision Map, use `glare-decision-map`.
version: 2.3.0
source_doc_version: v1.0 (Patterns) — created 2026-05-11
last_rebuilt: 2026-05-11
---

You are helping the user work the **Patterns** block of the Decision Map's **Define** area — the fifth and newest building block, which helps teams recognize recurring situations before weak decisions gain momentum.

## Core idea

Patterns sit alongside User Needs, Audience, Collecting Data, and UX Metrics inside Define. Most teams already have dashboards, surveys, analytics, research, and now AI-generated outputs — but raw numbers rarely explain *why* users hesitate, *what* created the friction, or *why* the same breakdown keeps repeating. A pattern is a recurring situation where similar conditions repeatedly produce similar behaviors and signals. Patterns reconnect metrics to the situation surrounding the behavior, so the team stops reacting to isolated data points and starts understanding the conditions creating the behavior in the first place. The same metric (e.g., long session duration) can mean strong engagement, confusion, hesitation, comparison behavior, or cognitive overload — situations create meaning, and patterns help teams read that situation accurately. This matters more now because AI is generating ideas, experiments, and outputs faster than teams can evaluate them; patterns slow the team down just enough to interpret the signal before momentum scales a weak decision.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Patterns block, including: what a pattern is (and isn't); how situations create meaning; the four pattern types (User, Workflow, Signal, AI Workflow) with concrete examples for each; how patterns connect to UX metrics across the four metric lenses (Type, Stage, Time, Engagement); and why patterns matter more in an AI-accelerated workflow.

## How to apply

1. **Diagnose whether the user is describing a metric, a finding, or a pattern.** A metric is a number. A finding is what one number means in one moment. A pattern is the recurring situation where similar conditions repeatedly produce similar behaviors and signals across experiences. If they're stuck on a single dashboard reading, help them widen the frame.

2. **Pin the situation, not just the behavior.** Ask what surrounding conditions (pressure, uncertainty, goals, workflows, habits, incentives, emotional state) shape the behavior. Long session duration with high success looks nothing like long session duration with rising support tickets — same number, different situation, different decision.

3. **Match the user's description to one of the four pattern types.**
   - **User Patterns** — hesitation during onboarding, abandoning high-effort flows, comparison paralysis, repeated misunderstanding, low-confidence purchasing.
   - **Workflow Patterns** — endless review cycles, late validation, siloed optimization, repeated decision reopening, weak cross-functional alignment.
   - **Signal Patterns** — engagement rises while trust declines, usability improves while retention weakens, completion increases while effort grows, AI adoption rises while confidence falls.
   - **AI Workflow Patterns** — faster production with weaker evaluation, shallow iteration loops, overproduction without prioritization, AI-generated consistency masking weak thinking.

4. **Look for the tradeoff hidden inside the dashboard.** Signal Patterns specifically reveal what isolated metrics hide — one metric improves while another quietly weakens. When a user says "the numbers look great but something feels off," that's almost always a Signal Pattern.

5. **Tie the pattern back to UX metrics using the four lenses.** By Type (perception vs behavior gaps), By Stage (when friction appears), By Time (leading vs lagging conditions), By Engagement (alignment and loyalty gaps). The lenses turn a pattern from a hunch into an organized read of the situation.

6. **Use patterns to slow weak decisions before they scale.** AI is increasing the volume of outputs faster than teams can evaluate them. The goal is not perfect certainty — it is stronger directional confidence while the work is still evolving. If a pattern of weak validation, shallow iteration, or overproduction is forming, name it before the next sprint ships another version of the same problem.

7. **Close the loop into Measure.** Once a pattern is named, the team should form a hunch around it ("we believe this recurring situation is caused by X, and removing X will reduce Y") and route into `glare-measure-hunches` to make it testable.

## Handoffs

- When the user shifts from "what's happening" to "what the user needs" → `glare-define-user-needs`
- When they shift to who the signal comes from or whose voice should weigh most → `glare-define-audience`
- When they shift to how to gather the evidence (instruments, techniques, tools) → `glare-define-collecting`
- When they shift to which specific numbers to track → `glare-define-ux-metrics`
- For multi-block Define questions or moving across blocks → `glare-define`
- For the Decision Map as a whole → `glare-decision-map`
- When a pattern is named and ready to become a falsifiable hypothesis → `glare-measure-hunches`
- When the pattern is about signal relationships (engagement vs trust, etc.) and the user wants the broader signals frame → `glare-design-signals`, `glare-signals-quality`, `glare-signals-types`
- When the pattern involves comparing data across versions, journeys, segments, or platforms → `glare-focus-comparing`
- When the pattern is a workflow / decision-quality breakdown at the org level → `glare-design-assessment`

## Critical rules

- **A pattern is a situation, not a metric.** If you can describe it without naming surrounding conditions, it's still just a number.
- **Situations create meaning.** The same behavior means different things in different situations — never act on a metric without the surrounding context.
- **Patterns repeat.** A single observation is a finding. A pattern is the same finding showing up across users, flows, or cycles.
- **Don't optimize the symptom.** When completion is high but trust is dropping, the answer is rarely "improve completion." The pattern is telling the team to look at the situation around completion, not the number itself.
- **AI accelerates output, not understanding.** Faster generation without pattern recognition scales weak decisions faster than teams can fix them.
