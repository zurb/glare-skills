# Capturing Signals — Reference

Source: Glare | Design Signal, Capturing Signals v1.3, May 3, 2026.

## Why this exists

Signals are most useful when they are part of the work, not something added after. Many teams wait until the end to gather feedback or review metrics. By that point, decisions have already been made, and it's harder to change direction. Capturing signals earlier keeps the work grounded while it's still moving.

## What this does

Capturing signals gives you a simple way to turn input into direction as you go.

- **Input:** ideas, hunches, designs, or flows
- **Process:** shape and test the signal
- **Output:** a clearer direction the team can act on

This helps the team move forward without waiting for perfect certainty.

## When to use

- When the user wants the end-to-end workflow for creating Design Signals as part of the work, not after.
- When the team gathers feedback too late and decisions are already made by the time signals arrive.
- When following the four-stage flow — Frame → Ground → Measure → Use.
- When turning a hunch into a question, anchoring to a metric, comparing versions, and keeping the signal attached to the decision.
- When making signals part of the sprint rather than a post-launch activity.

**Don't use when** the user wants the structural anatomy of one signal (`glare:signals-components`), the four signal types (`glare:signals-types`), or evaluating whether a built signal is usable (`glare:signals-quality`).

## How signals are captured

Signals don't start as signals. They start as small moments in the work. A question comes up in a review. A design feels unclear. Two directions are on the table and no one is sure which one will hold. The team has a sense of what might be happening, but not enough clarity to move forward with confidence.

Instead of pushing through or waiting for more data, this is where signals begin to take shape.

Capturing a signal means slowing down just enough to connect what the team is seeing to something that can be understood and acted on. It doesn't require a full study or a long research cycle. It requires making the thinking visible, grounding it in what matters, and bringing in just enough input to reduce uncertainty.

The work follows a simple flow with four stages.

## 1. Frame the Signal

### Start with a hunch

Every signal begins with a moment where something doesn't feel right. This usually comes up in a review or while looking at the work. Someone notices friction, confusion, or an opportunity to improve. It's not proven yet, but it's enough to pause and ask a question.

The important part: **pull that thought out of the conversation and make it visible.**

Example: "We think users might not understand what to do on this screen."

At this point, you're not solving it. You're just capturing where to look.

### Make it clear

Hunches are often vague. If they stay that way, the conversation drifts. This step is about tightening the thinking by asking a better question. The goal is to make it specific enough that the team can actually respond to it. You're moving from a feeling to something you can test.

Example: "Do users understand what action to take on this screen?"

Now the team is aligned on what they're trying to learn.

## 2. Ground the Signal

### Connect to what matters

A question on its own isn't enough. It needs to be tied to why it matters. This is where you connect the work to:

- what the user is trying to accomplish
- what outcome the team is trying to move

This step grounds the signal so it's not just about the interface, but about impact.

Example:
- user need → "complete the next step without hesitation"
- business goal → "increase onboarding completion"

Now the team understands why this matters.

## 3. Measure the Signal

### Anchor it to a metric

At this point, the team knows what they're looking for. Now they need a way to read it. Choose a metric that reflects the question. The goal isn't to measure everything. It's to measure the one thing that will make the answer clear.

Example: comprehension → do users understand what to do.

This gives the signal a way to be seen, not just discussed.

### Put it next to the work

Signals only work when they are tied to real options. Place the signal next to the designs or directions the team is considering. Instead of reviewing work in isolation, you are now evaluating how each option holds up.

Example:
- Version A → detailed explanation
- Version B → simple call to action

Now the signal has something concrete to test against.

### Bring in real input

This is where the signal starts to gain weight. Bring in just enough user input to see what's actually happening. This can be fast and lightweight. The goal is not to run a full study, but to reduce uncertainty.

Look for both:
- metrics → what users did
- comments → why they reacted that way

Example:
- 72% understood Version B
- comments: "this one is easier to follow"

Now the signal reflects real behavior, not just team opinion.

## 4. Use the Signal

### Compare and read

This is where most teams fall back into opinion. Instead, you stay with the signal. You're not just looking at numbers. You're reading how the options differ and what that means.

You're asking:
- where is one direction clearly stronger
- where do both struggle
- where do the results and comments align

Example: Version B shows higher comprehension and clearer feedback. Version A shows hesitation and confusion.

Now the tradeoff is visible. The signal is doing the work.

### Decide what moves forward

With the signal in place, the decision becomes clearer. You're not trying to prove something is perfect. You're choosing the direction that holds up better.

This might mean:
- selecting one option
- refining the stronger one
- combining parts
- stopping something

Example: Move forward with Version B and simplify the CTA further.

The signal doesn't remove judgment. It gives it focus.

### Keep the signal attached

Most decisions don't fail in the moment. They drift later. This step keeps the signal connected to the work as it moves forward. It gives the team a shared reference point so they don't have to restart the conversation.

Example: "We chose this because users understood it faster."

Now the decision holds across reviews, handoffs, and future changes.

## What you get vs. where it breaks

### What you get

When signals are captured this way:
- decisions form earlier
- feedback connects to something concrete
- tradeoffs are easier to explain
- direction carries forward with more confidence

The team spends less time revisiting decisions and more time moving forward.

### Where it breaks

Signals lose value when:
- hunches stay vague
- metrics don't match the question
- no clear direction is defined
- input is gathered too late

In these cases, signals come in after the decision instead of guiding it.

## Quick use

To capture a signal:
- write the hunch
- connect it to a need and goal
- choose a metric
- compare directions
- decide what moves forward
- keep the signal attached

You don't need perfect clarity. You need enough to move.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Capture-after-launch.** Treating signal capture as a research deliverable that arrives after decisions are made. By then the direction is locked and the signal has no leverage. Move capture earlier — during Frame and Ground, not after Use.
- **Skipping Frame.** Jumping into Measure without anchoring the question. The data arrives but doesn't answer anything because nothing was framed.
- **Heavy capture.** Stacking 5+ instruments on one signal because the team is uncertain. Heavy capture slows the loop and produces conflicting data. Light, fast, repeated capture beats one perfect session.
- **Signal detached from the decision.** Capturing signals and then letting them sit in a research repo while the decision moves forward without them. Keep the signal attached — name which decision it informs and surface it at the decision moment.

## Cross-references the source doc explicitly calls out

The Capturing Signals doc points to these deeper resources at each stage:
- **Frame:** Explore Hunches, Explore Questions
- **Ground:** User Needs, Business Goals
- **Measure:** Collecting, UX Metrics, Concepts, UX Metrics
- **Use:** Comparison, Decisions, Run a Design Review

These map into the Define facet (User Needs, Collecting, UX Metrics), the Measure facet (Hunches, Questions, Concepts), the Focus facet (Comparison), and the Design Review and Lead sections (Decisions, Run a Design Review).

## How this fits

Capturing Signals shows **how signals are created in the work**.

- **Components** show how signals are built
- **Signal Types** show where they apply
- **Signal Quality** shows if they can be trusted

Together, these turn signals into a practical layer the team can rely on.
