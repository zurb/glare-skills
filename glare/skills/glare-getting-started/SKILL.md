---
name: glare-getting-started
description: Use whenever the user is new to Glare or asks an intro question — "what is Glare," "how do we start," "conceptual tour," "the six components," "create my first signal," "I have a real decision," "two directions no clear winner," "use Glare with ChatGPT or Gemini," "what is Ray," "prompt vs Skill vs agent," "roll Glare out," "the 90-day pilot," "coach our team," "prove design impact," "design ROI," "leading vs lagging indicator," the chain decision → signal → user behavior → product outcome → business impact, or any "what does X mean" vocab question (design signal, hunch, UX metric, Decision Map, Design Review, Design Assessment, AI Skill, AI Agent, the 6 components, the 5 dimensions, the 4 metric types). Also for first-time onboarding or picking a sub-skill. Do NOT use when the user is already deep inside a component — invoke `glare-decision-map`, `glare-design-review`, `glare-design-signals`, `glare-design-assessment`, or `glare-ux-metrics` instead.
version: 3.1.0
source_doc_version: v1.3 + v1.32 + v1.34 (multi-source, consolidated)
last_rebuilt: 2026-05-13
---

You are helping the user **get started with Glare** — ZURB's open decision framework for product and design teams. This skill is the consolidated on-ramp: first-time introduction, conceptual tour of the six components, first-signal walkthrough, AI workflow guidance, coaching/rollout framing, design-impact narrative, and vocabulary lookup all live here.

## Core idea

Glare turns scattered inputs — intuition, early research, prompt-generated concepts, business goals — into **design signals**, the smallest unit of clarity a team can use to move a decision forward. A signal connects a decision the team needs to make, a measurable user response, and the outcome that decision is meant to influence. Glare exists because AI has accelerated *output* faster than teams can build *confidence in what to do with it*; the framework gives teams (and the AI systems they work alongside) a shared structure for moving from generation to decision. The system has six connected components: **Get Started + Decision Map + Design Review + UX Metrics + Design Signals + Design Assessment**, orchestrated together by `glare-master`.

## Read the reference first

Before answering substantive questions, read `reference.md` — the unified Getting Started reference, organized into seven sections: (1) What Glare is and why it exists, (2) How Glare works — the six-component architecture, (3) Creating your first signal — the six-move walkthrough, (4) Glare + AI workflows — prompts, Skills, agents, signals, decisions, (5) Coaching and advising — the 90-day pilot model for rolling Glare out, (6) Proving design impact — the chain from decision to business outcome, (7) Glossary — canonical term definitions.

## How to apply

1. **Diagnose the user's entry point first.** Which of the seven sections does their question land in? Don't dump the whole framework — pick the right one and route. The seven entry shapes:
   - "What is Glare / why does it exist / who is it for" → section 1 (What Glare is)
   - "How does Glare work / what are the parts / show me the loop" → section 2 (How Glare works — six components)
   - "I have a real decision in front of me / two directions / help me make a signal" → section 3 (Creating your first signal)
   - "How do I use Glare with ChatGPT / what's a Skill vs a prompt / what's Ray" → section 4 (AI workflows)
   - "How do we roll this out / 90-day pilot / coach our team" → section 5 (Coaching and advising)
   - "How do we prove design impact / connect design to revenue / leading vs lagging" → section 6 (Proving design impact)
   - "What does X mean / define this term / what's the difference between Y and Z" → section 7 (Glossary)

2. **Default to the six-component tour when the user asks "how does Glare actually work."** Walk through the six components in order — Get Started (this skill), Decision Map (Define/Measure/Focus/Lead), Design Review (SIGNAL — Surface, Identify, Ground, Navigate, Align, Lock), UX Metrics (the measurement layer underneath everything), Design Signals (the unit of clarity), Design Assessment (the five-dimension diagnostic). Close with the loop: prompt → Skill → signal → review → decision → outcome → assessment.

3. **When someone wants to try Glare on real work**, run the six-move first-signal arc from section 3 immediately: **Start with a Hunch → Make It Clear → Shape the Signal → Use the Signal → Decide What Moves Forward → Make Decisions Hold**. Don't lecture the framework first. The signal walkthrough only works against a concrete choice the team needs to make.

4. **When someone asks how Glare fits with AI**, walk the five-role workflow from section 4: **prompts generate → Skills shape → agents coordinate (Ray) → participant input creates signals → teams decide**. Reinforce: AI supports the work, people determine direction. Always clarify the prompt vs. Skill distinction — a prompt tells AI what to do once; a Skill defines how to do something repeatedly.

5. **When a leader asks about adoption or rollout**, use the 90-day pilot from section 5: Month 1 establish the signal (one team, one initiative, one signal), Month 2 build the rhythm (reviews, stakeholder conversations, signal interpretation), Month 3 scale the model (quality scorecard, signal patterns, executive-ready proof stories). Always close with "start with one team, one initiative, one signal." Don't sell transformation — sell traction.

6. **When the user is trying to prove design impact**, walk the chain from section 6: **decision → signal → user behavior → product outcome → business impact**. Position UX metric signals (Attitudinal · Behavioral · Performance · Intelligence) as leading indicators that show experience change before lagging business metrics (revenue, retention, conversion, cost-to-serve) move. Isolation is rarely perfect — the connection can still be made visible.

7. **When the user trips on terminology**, look the term up in section 7 (Glossary) — don't improvise. Glare uses precise terms (AI Skill vs. prompt, signal vs. UX metric, hunch vs. signal, agent vs. Skill, Decision Map vs. Design Assessment) and consistency matters.

8. **Resist over-explaining.** Glare is meant to be used, not studied. If the user has a real decision in front of them, route them into the work — not into more framework.

## Handoffs

- The orchestrator across the six components → `glare-master`
- Walking the full Decision Map (Define → Measure → Focus → Lead) → `glare-decision-map`
  - Defining user needs, audience, patterns, data collection, UX metrics → `glare-define`
  - Concepts, hunches, questions, findings, signals → `glare-measure`
  - Initiatives, methods, comparing, decisions → `glare-focus`
  - Business goals, mapping, workflows, results → `glare-lead`
- Running a strong design review (SIGNAL framework) → `glare-design-review`
- The measurement layer underneath everything → `glare-ux-metrics`
- The unit of clarity itself — anatomy, types, quality, capturing → `glare-design-signals`
- The five-dimension diagnostic of how the system holds → `glare-design-assessment`
- Going deep into a single facet, dimension, or technique → invoke that section's nested skill (the v3 marketplace has dedicated skills for each)
