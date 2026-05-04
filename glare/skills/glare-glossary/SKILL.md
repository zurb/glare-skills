---
name: glare-glossary
description: Use this skill when the user is asking what a Glare term means or wants a precise definition — phrases like "what's a design signal," "what's the difference between a prompt and a Skill," "what does Define mean in Glare," "what's a hunch," "what's an AI agent in Glare," "define UX metric," "what's the Decision Map," or any "what does X mean" question about Glare vocabulary. Also use when the user is mixing up terms (signal vs. metric, prompt vs. Skill, hunch vs. signal, agent vs. Skill, Decision Map vs. Design Assessment), or when they're embedding Glare concepts into their own writing/prompts and need accurate language. Do NOT use when the user wants to actually apply a concept — route to the relevant skill (`glare-create-first-signal`, `glare-how-glare-works`, etc.).
---

You are providing **precise definitions of Glare terminology**. Consistency matters — Glare uses each term carefully.

## Core idea

Glare uses a small set of terms to explain how product and design decisions move from uncertainty to impact. The glossary gives each term a simple meaning so teams, leaders, and AI systems can use the same language. **Don't paraphrase named concepts** like Design Signal, Decision Map, Skill, Hunch — use the canonical phrasing.

## Read the reference first

Before answering substantive questions, read `reference.md` — full term-by-term glossary covering AI Agent, AI Skill, AI Workflow, Business Goal, Design Assessment, Design Impact, Design Review, Design Signal, Decision, Decision Map, Define / Measure / Focus / Lead, Hunch, Intuition, Participant Input, Prompt, Signal Loop, Tradeoff, User Need, UX Metric.

## How to apply

1. **Look up the term in `reference.md` first.** Don't improvise definitions — Glare's vocabulary is intentional.

2. **For "what's the difference between X and Y" questions**, lean on the canonical contrasts:
   - **Prompt vs. Skill** — a prompt tells AI what to do once; a Skill defines how to do something repeatedly.
   - **Hunch vs. Signal** — a hunch is an early read before evidence is clear; a signal is a hunch shaped with UX metric + user need + business goal so it can guide a decision.
   - **Signal vs. UX metric** — a UX metric is a measurement (comprehension, usability, etc.); a signal connects that metric with intuition + direction + context + user need + business goal.
   - **Agent vs. Skill** — an agent (Ray) manages the goal and chooses Skills; Skills do the repeatable steps.
   - **Decision Map vs. Design Assessment** — Decision Map shows how decisions take shape (Define/Measure/Focus/Lead); Design Assessment shows how decisions move through the org over time across five dimensions.

3. **When a user is using Glare terms in their own writing or prompts**, give them the canonical phrasing. Don't accept paraphrases that drift.

4. **When a term appears that isn't in the glossary**, flag it as outside the canonical Glare vocabulary and ask whether they want the closest equivalent.

5. **Stay short.** Glossary entries are definitions, not explainers. If the user wants to *use* the concept, hand off to the appropriate skill.

## Handoffs

- Want to use a term in real work → the relevant working skill (`glare-create-first-signal`, `glare-how-glare-works`, `glare-ai-workflows`, etc.)
- Want the conceptual tour → `glare-how-glare-works`
- Want to start using Glare → `glare-get-started`
- Going deep into a Decision Map area → `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`
- Going deep into the Design Assessment dimensions → `glare-design-assessment`
