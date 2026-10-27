# Signal Quality — Reference

Source: Glare | Design Signal, Signal Quality v1.3, May 3, 2026.

## Why this exists

Not everything that looks like a signal can guide a decision. Teams often see movement in metrics or hear strong feedback and assume they have enough to act. But without the right structure, those inputs create interpretation, not clarity.

Signal Quality answers a simple question: **Is this signal complete enough to guide a decision?**

## When to use

- When the user is evaluating whether a Design Signal is complete enough to guide a decision.
- When asking "is this signal usable" or "is this a signal or just a metric."
- When applying the usable / not-usable filter before a decision.
- When debugging signals that produce more debate than direction.
- When identifying common failure points (missing need, missing context, wrong metric, no direction).
- When deciding whether to act on a signal or refine it first.

**Don't use when** the user wants the structural anatomy (`glare:signals-components`), the four signal types (`glare:signals-types`), or the capture workflow (`glare:signals-capturing`).

## What Signal Quality does

Signal Quality gives you a simple way to evaluate a signal before acting on it.

- **Input:** a signal made up of behavior, metrics, and context
- **Check:** are the pieces complete and connected
- **Output:** a clear call to move forward or refine

This keeps decisions grounded in something the team can trust.

## What makes a signal usable

A signal is usable when the story holds together. You should be able to see:

- what is happening
- why it is happening
- where it is happening
- what it affects
- what to do next

If any of these are unclear, the signal needs more work. Before using a signal, run a quick check. A signal is usable when:

- the behavior is clear
- the user need explains why it matters
- the context is specific
- the metric matches the question
- the direction is visible

At this point, the signal points to a decision the team can make.

## A signal is not usable yet when

- it's just a metric without context
- feedback is vague or disconnected
- behavior is unclear or inconsistent
- the signal doesn't point to a next step

In these cases, the signal creates discussion, not direction.

## Strong vs weak signals

### What strong signals feel like

Strong signals are easy to read.
- they point to a specific moment
- they connect behavior to intent
- they make tradeoffs visible
- they lead naturally to a decision

The team doesn't have to figure out what it means. The meaning is already there.

### What weak signals feel like

Weak signals slow the work down.
- multiple interpretations are possible
- the team debates what it means
- the connection to the user is unclear
- no clear direction forms

The signal doesn't hold, so decisions stall.

## Common failure points

Signals often break in predictable ways:

- **missing need** → behavior is misread
- **missing context** → the signal is too general
- **wrong metric** → results don't reflect reality
- **no direction** → nothing moves forward

These don't mean the signal is wrong. It means it's not ready yet.

After checking signal quality, you should have:
- a clear understanding of whether the signal holds
- a shared view across the team
- a decision you can move forward with or refine

The team spends less time interpreting and more time moving.

## Quick use

Before acting on a signal, ask:

- is the behavior clear
- does the need explain why it matters
- is the context specific
- does the metric match the question
- is the direction obvious

If the answer isn't clear, strengthen the signal before deciding.

## How this fits

Signal Quality focuses on **whether a signal can be trusted**.

- **Components** show how signals are built
- **Signal Types** show where they apply
- **Capturing Signals** shows how they are created

Together, these help the team move from input to decisions with confidence.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Acting on not-usable signals.** Movement in a metric without need, context, or direction gets treated as enough — and the resulting decision feels confident but is shaky. Run the filter before acting.
- **Treating quality as a yes/no on data.** Signal quality isn't about whether the data is "good" — it's about whether the *structure* is complete. A weak survey with all six components beats a perfect dashboard with two.
- **Confirming the signal you wanted.** Looking at a signal through the lens of the answer you already prefer. Quality means stress-testing — what would make this signal not usable?
- **Refining forever.** Treating quality as a perfectionism game. Signals don't need to be perfect; they need to pass the usable filter. Once they pass, act.

