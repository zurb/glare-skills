---
name: design-signals
description: Use this skill whenever the user asks about Design Signals as a top-level concept in Glare — "what is a design signal," "why do signals matter," "how is a signal different from a metric," "signals vs feedback," "how do I turn data into a decision," or wants the overview of the Design Signals section (Components, Signal Types, Signal Quality, Capturing Signals). Also use when the user is stuck moving from dashboards/feedback/intuition to an actual decision, when they say "we have data but no direction," when they want the working definition of a signal as the layer connecting user behavior, UX metrics, design decisions, and business outcomes, or when they need a map of which child skill to drop into next. Do NOT use when the user is already working on one specific aspect — anatomy of a signal (`glare:signals-components`), the four types Need/Use/Prefer/Adopt (`glare:signals-types`), evaluating whether a signal is usable (`glare:signals-quality`), or the capture workflow (`glare:signals-capturing`).
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user understand and use **Design Signals** — the working layer of Glare that turns user input into decisions.

## Core idea

A **Design Signal** is a measurable input from users that makes the invisible obvious. It forms when a user behavior is observed, a metric captures the reaction, the context explains why it happened, and a direction becomes clear. On their own, a metric, a piece of feedback, or a hunch is incomplete. A signal **connects** them into something the team can use.

The gap teams face is not information — it is direction. Signals close that gap by linking what users do to what the team should do next.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Design Signals master page (definition, why signals matter, signals as a working layer, the four child sections and what each is for, how it all fits together).

## How to apply

1. **Diagnose what the user actually wants.** Are they (a) asking for the definition / pitch, (b) trying to construct a signal right now, (c) checking if a signal they have is good enough, (d) looking for a signal-creation workflow inside their existing process, or (e) trying to figure out which type of signal is missing? Route accordingly.

2. **Default opener for "what is a design signal":** lead with the four-piece formation (behavior observed → metric captures reaction → context explains why → direction becomes clear) and the contrast with raw inputs (a metric shows what happened; feedback describes what users said; intuition suggests what might be wrong; a signal connects them).

3. **Frame signals as a working layer**, not just inputs. In Glare, signals connect user behavior, UX metrics, design decisions, and business outcomes. Input = user reactions, behavior, feedback. Process = structure, connect, evaluate. Output = direction that can be acted on.

4. **Keep signals as questions first.** Per the master doc: signals are most useful when treated as questions that surface what is happening, where the work is breaking down, and what needs to change. Resist letting the user collapse a signal into a single number.

5. **Hand off as soon as the question narrows** — see Handoffs below. Don't try to cover all four child topics in one answer.

## Critical rules

- **A signal needs all four pieces** — behavior observed + metric capturing reaction + context explaining why + direction becoming clear; a metric, a piece of feedback, or a hunch alone is not a signal.
- **Signals are questions first, numbers second** — resist collapsing a signal into a single number; a signal's job is to surface what is happening, where work is breaking, and what needs to change.
- **A signal is not a metric** — metrics describe what happened, feedback describes what users said, intuition suggests what might be wrong; the signal is what connects them into actionable direction.
- **Route to the right child quickly** — don't cover Components, Types, Quality, and Capturing in one answer; diagnose whether the user is building, classifying, evaluating, or capturing, then hand off.

## Handoffs

- Building a signal / the six-part anatomy (design intuition, UX metric, user need, context, business goal, direction) → `glare:signals-components`
- The four signal types (Need, Use, Prefer, Adopt) and ensuring coverage across the experience → `glare:signals-types`
- Deciding whether a signal is usable, strong-vs-weak, common failure points → `glare:signals-quality`
- The end-to-end capture workflow (frame → ground → measure → use) inside the work → `glare:signals-capturing`
- Picking the underlying user need or the metric that anchors the signal → `glare:define-user-needs`, `glare:define-ux-metrics`
- Running a fast test that produces a signal → `glare:measure`
- Comparing directions side-by-side once signals are captured → `glare:focus`
- Carrying signals into business narratives and rituals → `glare:lead`
- Walking a real artifact through a structured review with signals attached → `glare:design-review`
