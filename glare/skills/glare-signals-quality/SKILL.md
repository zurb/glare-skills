---
name: glare-signals-quality
description: Use this skill when the user is trying to evaluate whether a Design Signal is good enough to act on — "is this signal usable," "is this a signal or just a metric," "how do I know if a signal is strong enough," "weak vs strong signal," "why is our signal not leading to a decision," "should we act on this or refine it." Triggers also include debugging signals that produce more debate than direction, identifying common failure points (missing need, missing context, wrong metric, no direction), or running the usable / not-usable filter before a decision. Do NOT use for the structural anatomy of a signal (`glare-signals-components`), the four signal types (`glare-signals-types`), or the capture workflow (`glare-signals-capturing`).
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user **evaluate Signal Quality** — deciding whether a signal is complete enough to guide a decision.

## Core idea

Not everything that looks like a signal can guide a decision. Teams often see movement in a metric or hear strong feedback and assume they have enough to act, but without the right structure those inputs create interpretation, not clarity. Signal Quality answers one question: **Is this signal complete enough to guide a decision?** It treats every signal through a simple filter: **usable** or **not usable**.

## Read the reference first

- `reference.md` — full content on what makes a signal usable, the not-usable patterns, what strong vs. weak signals feel like, common failure points, and the quick-use checklist.

## How to apply

1. **Run the usable check** before any decision. A signal is usable when:
   - the behavior is clear
   - the user need explains why it matters
   - the context is specific
   - the metric matches the question
   - the direction is visible

   If any of these is unclear, the signal needs more work — do not act yet.

2. **Identify the not-usable pattern.** A signal is not usable yet when:
   - it's just a metric without context
   - feedback is vague or disconnected
   - behavior is unclear or inconsistent
   - the signal doesn't point to a next step

   Name which pattern is happening. That tells the user where to strengthen.

3. **Use the strong-vs-weak feel test.** Strong signals point to a specific moment, connect behavior to intent, make tradeoffs visible, and lead naturally to a decision — the team doesn't have to figure out what it means. Weak signals invite multiple interpretations, the team debates what it means, the connection to the user is unclear, no clear direction forms. If the user describes the second pattern, the signal isn't ready.

4. **Map symptoms to the four common failure points:**
   - behavior is being misread → **missing need**
   - signal feels too general → **missing context**
   - results don't reflect reality → **wrong metric**
   - nothing moves forward → **no direction**

   These don't mean the signal is wrong. They mean it isn't ready yet.

5. **Frame the output crisply.** After a quality check, the team should leave with: a clear understanding of whether the signal holds, a shared view across the team, a decision they can move forward with or refine. Less time interpreting, more time moving.

## Handoffs

- Top-level concept of Design Signals → `glare-design-signals`
- Strengthening any of the six structural parts that turned out to be weak → `glare-signals-components`
- Coverage check across Need / Use / Prefer / Adopt → `glare-signals-types`
- Workflow for capturing signals correctly the first time → `glare-signals-capturing`
- If "wrong metric" is the failure → `glare-define-ux-metrics`
- If "missing need" is the failure → `glare-define-user-needs`
- If you have multiple competing signals and need to compare directions → `glare-focus-comparing`
- If the signal holds and now needs to be carried into a decision moment → `glare-design-review`
