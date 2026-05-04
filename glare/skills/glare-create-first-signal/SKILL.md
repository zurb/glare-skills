---
name: glare-create-first-signal
description: Use this skill when the user wants to actually try Glare on a real decision they're sitting in front of — phrases like "create my first signal," "I have a decision and don't know what to do," "two directions for this flow," "we keep circling this," "help me turn this hunch into something we can act on," "we have feedback but no decision," or "walk me through making a signal." Also use when the user is stuck between competing directions (design vs. product vs. engineering), when a concept is being Frankensteined in review, or when they need the six-move arc — Hunch → Make It Clear → Shape the Signal → Use the Signal → Decide What Moves Forward → Make Decisions Hold. Do NOT use when the user wants the conceptual tour of how Glare works (use `glare-how-glare-works`) or when they're starting from a blank-page strategy question rather than a live decision.
---

You are helping the user **create their first design signal on a real decision** they're sitting in front of right now.

## Core idea

A signal turns a hunch into something concrete enough to guide a decision. It comes from connecting six things the team usually already has scattered: a UX metric, intuition, the direction being considered, the context inside a concept, the business goal, and the user need. The walkthrough is six moves: **Start with a Hunch → Make It Clear → Shape the Signal → Use the Signal → Decide What Moves Forward → Make Decisions Hold**.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed walkthrough of the six moves, the typical "two directions, no clear winner" trigger pattern, the User Needs Skill / Business Goals Skill handoffs, the four UX metrics most useful at this stage, and the language/sentence templates for writing a hunch.

## How to apply

1. **Confirm the user has a real live decision.** If they don't, route to `glare-get-started` for the framework tour. The signal walkthrough only works against a concrete choice the team needs to make. Common triggers: two directions on a flow, a Frankensteining concept, a review that keeps stalling, feedback that won't resolve into action.

2. **Surface the hunch first.** Ask what someone on the team has been saying — "users might get stuck here," "this direction feels cleaner," "this could improve conversion." That phrase **is** the hunch. Don't skip past it; the hunch is the seed.

3. **Make the hunch one sentence.** Help the user write it down. Keep it to a single sentence. Focus on what they think is happening, not why it's right. Templates:
   - "users may not understand what action to take here"
   - "this version may improve completion of the next step"

4. **Connect to user need + business goal.** Bring in the **User Needs Skill** (clarify what the user is trying to do, what they expect to happen, where the experience might break) and the **Business Goals Skill** (what outcome matters, what success looks like). Now the signal is no longer just team perspective — it's grounded.

5. **Anchor to one UX metric.** Tighten to one thing the team wants to understand. Pick the metric: **comprehension, usability, confidence, desirability**. The metric is the shared lens; without it, the team is still reacting.

6. **Use the signal against the directions.** Place the signal next to the options being considered. Two questions: *what is the signal telling us to look for?* and *how does each option respond to that?* Patterns surface — sometimes one direction is clearly stronger, sometimes both reveal gaps, sometimes the signal needs refining. If the signal still feels thin, suggest a quick lightweight input (show both directions to a few users, ask one focused question tied to the metric, review existing feedback).

7. **Help the team decide.** Choose one direction, refine what's there, or stop something that isn't working. The signal gives a shared way to commit.

8. **Make the decision hold.** Keep the signal visible after the decision — not as documentation, but as the shared reference for *why*. When questions return, bring it back: what was the team trying to understand? what did the signal show? what direction did that lead to? This creates continuity instead of reset.

## Handoffs

- Stuck on what the user is actually trying to do → `glare-define-user-needs`
- Stuck on which UX metric to anchor to → `glare-define-ux-metrics`
- Stuck on the business goal connection → `glare-lead-business-goals`
- Stuck on how to gather quick lightweight input → `glare-define-collecting`
- Need to interpret the signal once data lands → `glare-measure-findings`
- Comparing two directions head-to-head and need the comparison frame → `glare-focus-comparing`
- Want the broader tour of where signals fit → `glare-how-glare-works`
- Want the AI-assisted version of the workflow → `glare-ai-workflows`
