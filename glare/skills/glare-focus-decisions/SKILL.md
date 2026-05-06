---
name: glare-focus-decisions
description: Use this skill when the user is making a **Decision** in the Focus facet — turning signals into action. Triggers: "make the call," "we need to decide," "should we ship this," "should we test another iteration," "should we kill this," "revisit later," "we keep circling," "findings sit in decks," "explain the tradeoff," "lock the next move," writing a decision record, distinguishing strategic decisions (investment / roadmap / product direction) from tactical. Also use when picking any of the 5 tactical decision types — **Implement, Refine Design, Test Iteration, Revisit Later, Do Not Pursue** — or the decision triangle (strategic at top, tactical at bottom). Do NOT use when the initiative isn't framed (use `glare-focus-initiatives`), the frame isn't chosen (use `glare-focus-methods`), or signals haven't been placed side by side (use `glare-focus-comparing`). For executive ROI / KPI, use `glare-lead`.
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user make a **Decision** — the fourth and final move in the Glare Focus facet.

## Core idea

Decisions turn signals into action. By the time a team reaches Decisions, the work should no longer be floating in opinion: the initiative is clear, the method has framed the data, and Comparing has shown what is stronger. Now the team needs to choose. A decision is where Focus becomes movement — it takes the signal, names the tradeoff, and gives the business a clear next step. Without a decision, findings stay in decks, concepts stay open, meetings keep circling the same questions.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of Decisions v1.3: why decisions matter, the two levels (strategic vs. tactical), the 5 tactical decision types (Implement / Refine Design / Test Iteration / Revisit Later / Do Not Pursue), what goes into a decision, the 5-step process for making one, what comes out of a decision, and where decisions work best.

## How to apply

1. **Diagnose strategic vs tactical.** Strategic decisions are about direction, investment, roadmap (Should we invest? Should this become a priority? Should this shift resources?). Tactical decisions are about the next move on a specific concept (Should we implement? Refine? Test another iteration? Revisit later? Stop?). Both matter, and both can use the same 5-step process.

2. **Insist on grounding the decision in a signal.** A decision should not come from a feeling alone. It should come from a signal that has been framed and compared clearly enough to support action. If the signal isn't there, route back to `glare-focus-comparing` or `glare-focus-methods`.

3. **Run the 5-step process:**
   - **Name what is being decided.** What are we deciding? Strategic or tactical? Which initiative does this support? What happens if we do not decide?
   - **Ground the decision in the signal.** What signal matters most? What metric supports it? What user feedback explains it? What comparison gives it context?
   - **Explain the tradeoff.** What gets stronger if we choose this? What might get weaker? What risk are we accepting? What are we choosing not to do?
   - **Choose the decision type.** Pick exactly one of the 5: Implement, Refine Design, Test Iteration, Revisit Later, Do Not Pursue.
   - **Lock the next move.** Who owns the next step? What needs to happen? What evidence carries forward? When should the decision be reviewed again, if needed?

4. **Use the 5 tactical decision types precisely:**
   - **Implement** — signal is strong, tradeoff acceptable, next step clear; move into production/planning/rollout.
   - **Refine Design** — direction is right but design needs improvement; the team knows what to change.
   - **Test Iteration** — direction still open, current signal incomplete; need a sharper comparison or another round.
   - **Revisit Later** — idea has potential but timing or context is wrong; capture the rationale, keep alive.
   - **Do Not Pursue** — signal is weak or tradeoff is not worth it; stop or remove from consideration. Not failure — a useful protective decision.

5. **A "Test Iteration" decision is still a decision.** Don't let the team leave the meeting with vague "let's keep exploring" unless the actual decision is to run another iteration with a defined comparison.

6. **The decision record should travel.** Capture: the initiative, the concept/flow/feature/message considered, the UX metric, the signal, the comparison, the tradeoff accepted, and the next step. This is what lets product prioritize, design refine, research target, marketing sharpen, and leadership back the direction.

7. **Hand off to `glare-lead`** when the decision is made and the conversation turns to business goals, workflows, KPI relationships, or proving impact at the org level.

## Handoffs

- Reframing the initiative if the decision feels premature → `glare-focus-initiatives`
- Choosing a different frame if the data isn't decision-ready → `glare-focus-methods`
- Sharpening the comparison if the signal isn't strong enough → `glare-focus-comparing`
- Connecting the chosen direction to business outcomes → `glare-lead`
- The whole Focus flow → `glare-focus`
- The Define → Measure → Focus → Lead chain → `glare-decision-map`
