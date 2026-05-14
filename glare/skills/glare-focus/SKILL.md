---
name: glare-focus
description: Use this skill when the user is in the **Focus** facet of the Decision Map — turning signals into direction. Triggers — "what should we focus on," "we have findings but don't know what to do," "decide between concepts," "compare versions," "Initiatives Methods Comparing Decisions," "narrow the work," "we keep circling," "make the call," naming an initiative, choosing a frame, competitor/segment/journey/platform comparisons. Also when the user mentions Focus's four moves (Initiatives → Methods → Comparing → Decisions) or the five tactical decision types (Implement / Refine Design / Test Iteration / Revisit Later / Do Not Pursue). Do NOT use when still gathering findings (use `glare-measure`), defining the problem (use `glare-define`), or escalating to leadership KPIs (use `glare-lead`). For depth, use `glare-focus-initiatives`, `glare-focus-methods`, `glare-focus-comparing`, or `glare-focus-decisions`.
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user work through the **Focus** facet of Glare — where design work gets sharper.

## Core idea

Focus is the third facet of the Decision Map. Measure helps teams turn hunches into questions and findings; Focus takes those findings and helps teams decide what deserves more attention, what should be compared, and what direction is strong enough to move forward. Focus is more than picking a winner — it sharpens design direction, tests desirability, and turns scattered signals into decisions the team can act on.

Focus works through **four moves**:
- **Initiatives** — define the area of work that needs attention
- **Methods** — choose the best frame to learn through
- **Comparing** — place signals side by side
- **Decisions** — turn evidence into action

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Focus Overview v1.3: the four moves, the inputs Focus needs, what each move contributes, how Focus moves teams from learning to choosing, what improves when Focus is working, and where Focus fits between Measure and Lead.

## How to apply

1. **Locate the user in the Focus sequence.** Initiatives (defining the area of work) → Methods (framing the data) → Comparing (placing signals side by side) → Decisions (turning evidence into action). Don't drift backward; Focus flows in order. Diagnose which move the conversation is actually in before answering.

2. **Initiatives — name what needs attention.** Without a clear initiative, signals scatter across too many ideas. A strong initiative connects a user need, a business goal, and a measurable part of the experience. Five steps: map the request to the larger goal → find the user need behind the work → group concepts that could create value → decide what signal would create confidence → choose the initiative where design can create the most value. For depth, hand off to `glare-focus-initiatives`.

3. **Methods — frame the data.** A method is broader than "what test to run" — it is the **frame** the team uses to look at the work (journey frame, competitor frame, segment frame, iteration frame, etc.). Choose the frame that fits the decision. Focus methods include 13 frames (Competitors, Iterations, Timeline, Journeys, Platforms/Devices, User Goals/Tasks, Geographies, User Lifecycle, Behavioral Triggers, Segments, Feature Usage, Risk and Proof, Frameworks). For depth, hand off to `glare-focus-methods`.

4. **Comparing — see what performs better.** A single score rarely tells the whole story. Comparing places signals side by side using a **shared metric**, then surfaces the strongest signal **and the tradeoff**. Five steps: name the decision → choose the comparison point → use the same metric → look for the strongest signal and the tradeoff → turn the comparison into a finding. For depth, hand off to `glare-focus-comparing`.

5. **Decisions — turn evidence into action.** A decision names the choice, grounds it in the signal, explains the tradeoff, and locks the next move. Use one of **five tactical decision types**: Implement, Refine Design, Test Iteration, Revisit Later, Do Not Pursue. Distinguish strategic decisions (investment, roadmap, direction) from tactical decisions (the meeting next-move). For depth, hand off to `glare-focus-decisions`.

6. **Insist on the four Focus inputs** before any move runs: an initiative, something concrete to evaluate (concept/flow/page/experience), a UX metric, a signal from users, and a comparison point. Without those, Focus turns into preference.

7. **Hand off to `glare-lead`** once the decision is made and the conversation turns to business goals, workflows, KPI relationships, or proving impact at the org level.

## Critical rules

- **Focus flows in order — don't drift backward** — Initiatives → Methods → Comparing → Decisions is sequential; jumping into Comparing without a named Initiative produces preference, not direction.
- **Require all four Focus inputs before any move** — an initiative, something concrete to evaluate, a UX metric, a user signal, and a comparison point; without them, Focus collapses into opinion.
- **Compare on a shared metric or don't compare** — a single score rarely tells the whole story; place signals side by side on the same metric, then surface the strongest signal AND the tradeoff.
- **Every decision must name its type** — pick one of the five (Implement, Refine Design, Test Iteration, Revisit Later, Do Not Pursue); ambiguity here is why the same conversation comes back next week.
- **Ground the decision in the signal** — name the choice, cite the signal, explain the tradeoff, and lock the next move; decisions without all four don't survive contact with the team.

## Handoffs

- Defining the area of work that needs attention → `glare-focus-initiatives`
- Choosing the right frame for the data → `glare-focus-methods`
- Placing signals side by side → `glare-focus-comparing`
- Turning evidence into a clear next move → `glare-focus-decisions`
- Upstream: clarifying user need, audience, success → `glare-define`
- Upstream: turning concepts/hunches into signals → `glare-measure`
- Downstream: connecting decisions to business goals and outcomes → `glare-lead`
- The whole flow Define → Measure → Focus → Lead → `glare-decision-map`
