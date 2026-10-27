# Design Review — Reference

Compressed source: Glare | Design Review v1.3 (master), with anchors into Scoring Model, Rubric, Run a Transcript, and Techniques.

## What a design review is

A design review is where ideas are discussed, feedback is shared, and decisions are made. Most teams already run them. The harder part is getting clear outcomes from the conversation. A review can feel useful in the moment and still leave the team with scattered feedback, unclear direction, and slow progress.

Glare treats the design review as a **decision system** and applies the SIGNAL framework to it. The goal is to help teams turn feedback into decisions that move the work forward.

## What SIGNAL solves

Design reviews break down in predictable ways:

- the real problem stays unclear
- success is not defined
- feedback turns into scattered opinions
- the conversation circles without direction
- ownership is vague after the call
- decisions are implied instead of confirmed

A stronger review helps the team focus on the right problem, align on what matters, use signals to guide the discussion, move toward a clear decision, and carry momentum into the next step.

## The SIGNAL flow

**Surface → Identify → Ground → Navigate → Align → Lock**

In parallel: **Tension → Clarity → Evidence → Commitment → Responsibility → Momentum**

Each step reduces uncertainty. By the end of the flow, the group moves from an open problem to a committed next step.

| Letter | Step | Focus |
|---|---|---|
| S | Surface Challenges | Clarify the underlying problem |
| I | Identify Outcomes | Define what "better" means |
| G | Ground in Signals | Bring evidence into the conversation |
| N | Navigate Decisions | Shape a clear direction |
| A | Align Ownership | Make responsibility visible |
| L | Lock Momentum | Turn the conversation into action |

When a meeting stalls or feels incomplete, the cause is almost always in an earlier step that did not fully develop.

## During the review

SIGNAL helps teams:

- surface the real problem
- identify what success should look like
- ground feedback in signals
- navigate options with more focus
- align on ownership
- lock the next step before the call ends

## After the review

The **SIGNAL Call Rubric** evaluates how well a review followed the flow. The easiest input is a **call transcript** — it shows what actually happened, not what people remember.

Using the transcript, teams can see where the problem became clear, where success was defined or left vague, where signals shaped the direction, where the conversation circled or moved forward, where ownership was clarified, and where momentum was locked into action.

## When to use

- When the user is running, scoring, or improving a design review — the meeting itself.
- When asking "what is SIGNAL" or wanting the overview (Surface → Identify → Ground → Navigate → Align → Lock).
- When a review stalled, feedback scattered, decisions felt weak, or ownership ended unclear.
- When picking which of the six dimensions to drop into next.
- When choosing between scoring a transcript (`glare:review-rubric`) or prepping a call (`glare:review-coach`).

**Don't use when** already deep in one dimension (Surface/Identify/Ground/Navigate/Align/Lock), evaluating a transcript with the rubric (`glare:review-rubric`), preparing for a specific call (`glare:review-coach`), or wanting the scoring math only (`glare:review-scoring-model`).

## Scoring

Each dimension is scored 1–5 (see `glare:review-scoring-model` for the full rubric).

- **5 Leading** — the step clearly shaped how the group thought and decided
- **4 Strong** — clear and influential, minor gaps
- **3 Functional** — present and working but not shaping the conversation
- **2 Emerging** — shows up briefly but does not influence direction
- **1 Reactive** — mostly absent

Total /30 maps to bands: 25–30 Leading, 19–24 Advancing, 13–18 Functional, 6–12 Reactive. **Patterns matter more than the total.** Look for the step where clarity first dropped — that's usually the best place to improve.

## Run a transcript

- **Input:** a transcript from a real design review
- **Process:** evaluate across Surface, Identify, Ground, Navigate, Align, Lock
- **Output:** a clear view of where the review created clarity and where it lost strength

You don't need to adopt everything at once. Start by reviewing one recent call, finding where the conversation lost clarity, and applying one or two techniques in the next review.

See `glare:review-run-transcript` for the full workflow (Skill / Prompt / Ray app paths).

## Techniques

Each SIGNAL letter has a small set of in-the-moment techniques you can use to bring the conversation back when it's losing strength. They are small moves — usually one or two well-timed ones can shift the entire review.

See `glare:review-techniques` for the overview, then the individual dimension skills for full technique sets.

## Why this matters

Design reviews improve when teams can see how decisions are forming. SIGNAL makes that visible. It shows where the conversation gained clarity, where it lost strength, and what to do next. That makes design review repeatable. Teams learn how to turn feedback into decisions that move the work forward.

## Section map

| Skill | Use when |
|---|---|
| `glare:design-review` (this) | Overview, definitions, routing |
| `glare:review-surface` | Surfacing the real problem |
| `glare:review-identify` | Defining what better means |
| `glare:review-ground` | Bringing in evidence/signals |
| `glare:review-navigate` | Forming a recommendation |
| `glare:review-align` | Clarifying who owns the next move |
| `glare:review-lock` | Closing with action and timing |
| `glare:review-techniques` | Picking a technique by stuck-moment |
| `glare:review-scoring-model` | Scoring 1–5 per dimension |
| `glare:review-rubric` | Full evaluation output (scores + observations + behavioral metrics) |
| `glare:review-coach` | Pre-call prep + post-call coaching |
| `glare:review-run-transcript` | Practical end-to-end workflow |

## Failure modes

These are common ways this skill goes wrong in practice:

- **Treating SIGNAL as a checklist.** The six letters are diagnostic, not procedural. A review can land Surface and Identify in 90 seconds and spend the rest of the call on Navigate. Forcing equal time on each letter wastes the room.
- **Skipping Surface to "save time."** The most common failure. The review jumps to Navigate and Align, ownership gets assigned for solving the wrong problem, and the same conversation comes back two weeks later. Surface is where time pays back tenfold.
- **Lock as a calendar entry.** "Let's follow up next week" isn't Lock. Lock names who, by when, and what triggers the next conversation. Without that, decisions evaporate within 48 hours.
- **Running design reviews without a problem owner.** SIGNAL assumes someone in the room is accountable for moving the decision. When no one owns the problem, every letter softens — Surface drifts, Navigate stalls, Align stays vague.

