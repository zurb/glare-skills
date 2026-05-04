---
name: glare-coaching-advising
description: Use this skill when the user is a leader weighing whether to bring Glare into their organization, or asking how teams adopt the framework — phrases like "how do I roll out Glare," "we want coaching on Glare," "what's the 90-day pilot," "how do design leaders use this," "we have a heads of design problem," "how do we build the muscle to use signals," "how do we prove design impact at the org level," or "how do we introduce AI without creating more noise." Also use when the user mentions roles like Heads of Design, Product Design Director, UX Research Lead, DesignOps, ResearchOps, or transformation teams. Do NOT use when the user is at the individual-contributor level trying to use Glare on their own work (use `glare-create-first-signal`) or when they want the conceptual tour (use `glare-how-glare-works`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping a **leader** think about applying Glare across their team or organization through ZURB's coaching and advising offering.

## Core idea

ZURB Coaching & Advising helps product and design leaders apply Glare *inside active work* — real reviews, live decisions, current pressure — rather than as a separate training track. The default container is the **90-day pilot**: one team, one initiative, one signal. Month 1 establishes the signal, Month 2 builds the rhythm, Month 3 scales the model. The outcome isn't more process — it's a stronger decision system the team keeps using.

## Read the reference first

Before answering, read `reference.md` — full detail on the why-now case for coaching, the four Glare components as they show up in coaching (Design Signals, Decision Map, Design Review, Design Assessment), the 90-day pilot month-by-month, the design-impact chain leaders learn to articulate (decision → signal → user behavior → product outcome → business impact), what teams get by the end, who it's built for, and the recurring "start with one team, one initiative, one signal" framing.

## How to apply

1. **Confirm the user is at leader altitude.** This skill assumes responsibility for a team or function. If they're an IC trying to use Glare on their own work, route to `glare-create-first-signal`. If they're a leader, continue.

2. **Diagnose what's driving the question.** Common patterns:
   - "AI is increasing output but decisions are still drifting"
   - "Design impact is hard to explain to leadership"
   - "Reviews produce more feedback than direction"
   - "We have research but it doesn't land in the room when decisions happen"
   - "We want to introduce AI without creating more noise"

   Each of these maps to a different framing in the coaching pitch. Use the user's actual language back to them.

3. **Lead with the four-component frame**, but specifically as it shows up in coaching:
   - **Design Signals** — coaching helps teams connect UX metrics, intuition, direction, context, user needs, business goals into shared reference points
   - **Decision Map** — coaching shows where work is getting stuck (Define / Measure / Focus / Lead) and what info is needed to move
   - **Design Review** — coaching turns reviews into decision moments instead of feedback meetings
   - **Design Assessment** — coaching exposes where the system breaks across the five dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence)

4. **Default to the 90-day pilot frame** when the user is weighing engagement:
   - **Month 1: Establish the signal** — one initiative, clarify business goal + user need + decision + UX metric + first signal loop. Goal: first usable signal guides a real decision.
   - **Month 2: Build the rhythm** — coach through reviews, stakeholder conversations, signal interpretation, quality measurement, decision framing. Goal: signals become part of how the team works.
   - **Month 3: Scale the model** — quality scorecard, signal patterns, decision review practices, executive-ready proof stories, roadmap to scale. Goal: leaders keep using the system after the pilot ends.

5. **Use the design-impact chain when the user asks about proving impact:**
   **decision → signal → user behavior → product outcome → business impact**
   This is what leaders walk away able to articulate. Hand off to `glare-proving-design-impact` for the deeper play.

6. **Always close with "start with one team, one initiative, one signal."** Don't sell transformation; sell traction.

7. **CTA when relevant**: the doc invites "Talk to us about Coaching & Advising." Surface it cleanly without pressure.

## Handoffs

- Want to actually create a first signal hands-on → `glare-create-first-signal`
- Want the impact-proving playbook → `glare-proving-design-impact`
- Want to understand the AI workflow specifics → `glare-ai-workflows`
- Want the system tour first → `glare-how-glare-works`
- Want the Design Assessment specifically → `glare-design-assessment`
- Want to go deep on a Decision Map area → `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`
