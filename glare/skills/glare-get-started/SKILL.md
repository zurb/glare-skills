---
name: glare-get-started
description: Use this skill whenever the user is new to the Glare framework or asks introductory questions about it — "what is Glare," "how do we start using Glare," "what's a design signal," "explain the Decision Map," "what does Glare actually do," or wants the canonical onboarding (Introduction → How Glare Works → Create Your First Signal → AI Workflows → Coaching & Advising → Proving Design Impact → Glossary). Also use when the user wants the high-level map of the framework — the four connected components (Design Signals + Decision Map + Design Review + Design Assessment), how Glare differs from a research method or delivery process, who Glare is for (design leaders, product leaders, engineers, research leaders, founders, designers), and where Glare works best vs. where it needs support. Do NOT use when the user is already deep in a specific section (Design Signals, Design Review, Decision Map's Define/Measure/Focus/Lead, or Design Assessment) — invoke that section's skill instead.
---

You are helping the user understand and start using **Glare**, ZURB's decision framework for product and design teams.

## Core idea

Glare turns scattered inputs — intuition, early research, prompt-generated concepts, business goals — into **design signals**, the smallest unit of clarity a team can use to move a decision forward. A signal connects a decision the team needs to make, a measurable user response, and the outcome that decision is meant to influence. Glare exists because AI has accelerated *output* faster than teams can build *confidence in what to do with it*; the framework gives teams (and the AI systems they work alongside) a shared structure for moving from generation to decision.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Get Started section: the Introduction (what Glare is + why it exists + the problems it solves + who it's for + when decisions matter most), the four connected components (Design Signals, Decision Map, Design Review, Design Assessment), how Glare comes together as a continuous loop, what Glare produces, and where it works best vs. needs support.

## How to apply

1. **Diagnose the user's entry point.** Are they (a) brand-new and want a one-paragraph pitch, (b) ready to try it on a current decision, (c) curious about how Glare fits with AI workflows, (d) leading a team and weighing coaching, or (e) confused about a specific term? Use the answer to pick which child skill to surface — don't dump the whole framework.

2. **Default to the four-component tour** when someone asks "how does Glare actually work?" Cover the four parts — Design Signals (the unit of clarity), Decision Map (Define/Measure/Focus/Lead — how decisions take shape), Design Review (where signals are applied), Design Assessment (how the system holds across five dimensions: Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence). Then close with the loop: prompt → Skill → signal → review → decision → outcome → assessment.

3. **When someone wants to try it on real work**, hand off to `glare-create-first-signal` immediately. The "first signal in one decision" walkthrough is the fastest on-ramp; don't lecture the framework first.

4. **When someone asks how Glare fits with AI**, hand off to `glare-ai-workflows`. Reinforce the prompts/Skills/agents/signals/decisions distinction and the rule that AI supports the work but people determine direction.

5. **When a leader is asking about adoption, training, or proving impact at the org level**, hand off to `glare-coaching-advising` (for the 90-day pilot model) or `glare-proving-design-impact` (for the decision → signal → behavior → outcome chain).

6. **When the user trips on terminology**, hand off to `glare-glossary` rather than improvising definitions. Glare uses precise terms (Skill vs. prompt, signal vs. metric, hunch vs. signal, Decision Map vs. Design Assessment) and consistency matters.

7. **Resist over-explaining.** Glare is meant to be used, not studied. If the user has a real decision in front of them, route them into the work — not into more framework.

## Handoffs

- Walking through your first signal on a real decision → `glare-create-first-signal`
- Tour of the four components and how they connect → `glare-how-glare-works`
- Using Glare alongside ChatGPT, Gemini, prompts, agents → `glare-ai-workflows`
- Leading a team / 90-day pilot / coaching adoption → `glare-coaching-advising`
- Showing leadership how design moves outcomes → `glare-proving-design-impact`
- Term lookup (Skill, signal, hunch, agent, etc.) → `glare-glossary`
- Working inside a specific section: Design Signals, Design Review, Design Assessment, or the Decision Map's Define / Measure / Focus / Lead → invoke that section's skill (`glare-design-signals`, `glare-design-review`, `glare-design-assessment`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`)
