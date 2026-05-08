# Glare Router — Compressed Routing Reference (v2.0)

A flat lookup the router uses to recommend ONE skill, fast. This install ships the **Decision Map cluster** (21 skills) plus this router — 22 total.

---

## The Decision Map, one line per facet

| Facet | What it covers | Parent |
|---|---|---|
| **Decision Map** (spine) | Define → Measure → Focus → Lead, the four-facet loop end-to-end | `glare-decision-map` |
| **Define** | User needs, audience, UX metrics, collecting data — the Credibility stage | `glare-define` |
| **Measure** | Concepts → Hunches → Questioning → Findings — turning intuition into testable signals | `glare-measure` |
| **Focus** | Initiatives → Methods → Comparing → Decisions — turning signals into direction | `glare-focus` |
| **Lead** | Business Goals, Mapping (Chain of Proof), Results, Workflows — connecting design to impact | `glare-lead` |

---

## Phrase to skill lookup

Match what the user said to the leftmost trigger; route to the right skill.

### Decision Map — parent (1)

| Phrase the user uses | Route to |
|---|---|
| "Decision Map" / "trace a decision from problem to outcome" / "how do the four facets connect" / "the chain is broken" / "where does this decision sit" | `glare-decision-map` |

### Define (5)

| Phrase the user uses | Route to |
|---|---|
| In Define area, multi-block / "Credibility" / "who are we designing for" (broad) / "what should we measure" (broad) | `glare-define` |
| "what user need does this solve" / "is this a want or a need" / team can't agree on what we're solving / Basics / Trust / Personal / Impact / Feelings | `glare-define-user-needs` |
| "who are we designing for" / "design for everyone is design for no one" / four-voice frame / Project Team / Stakeholders / Customers / Participants | `glare-define-audience` |
| "how do we gather evidence" / "should we use a survey or A/B test" / SUS / NPS / SEQ / CES / first-click / card sorting / heatmaps | `glare-define-collecting` |
| "high satisfaction + low completion" / "vanity vs actionable metrics" / Attitudinal / Behavioral / Performance / leading vs lagging | `glare-define-ux-metrics` |

### Measure (5)

| Phrase the user uses | Route to |
|---|---|
| Measure area broad / "we believe that [change] for [audience] will [impact]" | `glare-measure` |
| 5-minute test / "what's the user need + business goal + signal here" / Concepts move | `glare-measure-concepts` |
| "we believe..." / forming a falsifiable hunch / "users like shorter forms" rewrite | `glare-measure-hunches` |
| "Do people like our homepage?" / "Can users find pricing within 5 seconds?" / drafting research questions / People — Process — Product — Problem types | `glare-measure-questioning` |
| "what does this data mean" / "how do I share what we learned" / Findings move / "I have a Helio test result and don't know what to do with it" | `glare-measure-findings` |

### Focus (5)

| Phrase the user uses | Route to |
|---|---|
| Focus area broad / "v1 vs v2" / "competitor review" / "we have findings but don't know what to do" | `glare-focus` |
| "what should we focus on" / 10 initiative types / scope the work / map the request to a goal | `glare-focus-initiatives` |
| "HEART" / "RICE" / "Kano" / "JTBD" / "what method should we use" / journey frame / segment frame / iteration frame | `glare-focus-methods` |
| "how do we compare" / "is this an improvement or just a change" / side by side / before and after / across the journey | `glare-focus-comparing` |
| "what's the decision" / "Decision Record" / Implement / Refine Design / Test Iteration / Revisit Later / Do Not Pursue | `glare-focus-decisions` |

### Lead (5)

| Phrase the user uses | Route to |
|---|---|
| Lead area broad / "prove design ROI" / "executive narrative" / connect design to business | `glare-lead` |
| "Reduce churn" / "Lower support costs" / Growth / Retention / Efficiency / Operations / 20 measurable goals | `glare-lead-business-goals` |
| "Chain of Proof" / "ladder our metrics" / User Need → Design KPI → Product KPI → Business KPI | `glare-lead-mapping` |
| "where is design impact breaking down" / "outputs vs outcomes" / "we have a roadmap but can't prove anything moved" / Initiatives → Findings → Decisions → Outcomes loop | `glare-lead-results` |
| "how do I tell sales this is working" / "design ROI for Finance" / translating to Sales / Marketing / Product / Engineering / Strategy / Ops / Finance / Legal | `glare-lead-workflows` |

---

## Named flows that have order

When the user is mid-flow, route by step rather than by facet.

### Decision Map — four facets in flow (loop, not line)

`Define → Measure → Focus → Lead → (back to Define)`

If the user names which facet they're stuck in, go to that parent. If they're on a handoff (e.g., "we have findings but don't know how to choose"), route to the *next* facet's parent (`glare-focus`). Don't fight the loop — outcomes feed the next Define cycle.

### Measure — four moves in arc

`Concepts → Hunches → Questioning → Findings`

If the user is forming a believe-statement → `glare-measure-hunches`. If they're trying to draft research questions → `glare-measure-questioning`. If they have data and need to translate it → `glare-measure-findings`. If they're upstream of all of it (anchoring intent) → `glare-measure-concepts`.

### Focus — four moves in arc

`Initiatives → Methods → Comparing → Decisions`

If the user is naming the area of work → `glare-focus-initiatives`. If they're choosing the frame → `glare-focus-methods`. If they're putting two things side by side → `glare-focus-comparing`. If they're locking the next move → `glare-focus-decisions`.

### Lead — four buckets

`Business Goals · Mapping · Results · Workflows`

Lead doesn't run strictly in order — pick the bucket that matches the conversation. Goal-anchoring → `glare-lead-business-goals`. Building the ladder → `glare-lead-mapping`. Closing the proof loop → `glare-lead-results`. Translating to a function → `glare-lead-workflows`.

---

## Common stuck patterns to high-leverage entry point

These are the most-frequent "I'm lost" scenarios. Match the symptom, route to the skill, explain in one sentence.

| Symptom | Route to | Why |
|---|---|---|
| "We have data but no decision" / "I have a number but don't know what to do with it" | `glare-measure-findings` | Findings is the move that turns raw data into a signal tied to user value and business result |
| "We're picking metrics and they're not landing" / "high satisfaction but low completion" | `glare-define-ux-metrics` | Attitudinal / Behavioral / Performance distinction usually fixes the mismatch |
| "Team can't agree on what we're solving" | `glare-define-user-needs` | The user-need block is where shared problem definition lives |
| "Designers, PMs, engineers all see different problems" | `glare-define-audience` | Four-voice frame forces alignment on whose voice the signal represents |
| "How do we gather evidence" / "survey vs A/B" | `glare-define-collecting` | Five-step process picks the right approach and instrument |
| "We have a hunch but it's not testable" / "we believe users like shorter forms" | `glare-measure-hunches` | Falsifiable template forces a concrete, testable bet |
| "Our research questions are leading / loaded" | `glare-measure-questioning` | Bias check + question-type taxonomy is the fix |
| "We're solutioning before we've named the bet" | `glare-measure-concepts` | The 5-minute test forces user need + business goal + signal alignment first |
| "We have v1 and v2 and can't choose" | `glare-focus-comparing` | Comparing is the move; turn it into a structured side-by-side on a shared metric |
| "What should we focus on" / "everything feels important" | `glare-focus-initiatives` | The initiative is the area of work; without it, signals scatter |
| "What method should we use" / "HEART vs RICE" | `glare-focus-methods` | Pick the frame that fits the decision, not the frame that's trendy |
| "We keep circling without a call" / "findings sit in decks" | `glare-focus-decisions` | The five tactical decision types force the next move |
| "Meeting ended with no decision" / "we always end with 'we'll follow up'" | `glare-focus-decisions` | Without naming the move (Implement / Refine / Test / Revisit / Do Not Pursue), the room can't close |
| "We have a roadmap but can't prove anything moved" | `glare-lead-results` | Initiatives → Findings → Decisions → Outcomes loop is the proof structure |
| "We did the research but can't connect it to business" | `glare-lead-mapping` | Chain of Proof ladders user need → Design KPI → Product KPI → Business KPI |
| "How do we tell Finance / Sales / Eng this matters" | `glare-lead-workflows` | Translation by function, not generic ROI |
| "Which business pressure does this serve" / "Growth or Retention or Efficiency" | `glare-lead-business-goals` | Anchor the work to one of the 20 measurable business goals before mapping |
| "How do all four facets connect" / "trace a decision end-to-end" | `glare-decision-map` | The spine view — Define hands to Measure hands to Focus hands to Lead and back |

---

## When ambiguous — the one-question protocol

If the diagnosis is genuinely 50/50 between two very different facets, ask ONE question. Common useful ones:

- "Do you have data already, or are you trying to figure out what to test?" — disambiguates `glare-measure-findings` vs. `glare-measure-questioning`
- "Are you trying to pick a direction, or trying to prove the direction worked?" — disambiguates Focus vs. Lead
- "Are you naming the bet, or already running it?" — disambiguates `glare-measure-concepts` vs. `glare-measure-hunches`
- "Are you picking what to compare, or comparing the things you've already chosen?" — disambiguates `glare-focus-initiatives` vs. `glare-focus-comparing`

Then route. Don't ask twice.

---

## Outside the core marketplace

This install is the Decision Map cluster only. Glare has more — but it isn't shipped here. If the user asks about a topic below, name the skill they want and tell them where to find it.

| Topic the user raises | Skill that covers it (not in this install) | Where to find it |
|---|---|---|
| Running / scoring / coaching a design review meeting; the SIGNAL framework (Surface, Identify, Ground, Navigate, Align, Lock); pasting a transcript; rubric or scoring model | `glare-design-review` and the SIGNAL letter skills, `glare-review-techniques`, `glare-review-scoring-model`, `glare-review-rubric`, `glare-review-coach`, `glare-review-run-transcript` | `~/Desktop/zurb.nosync/skills/glare-skills-flat/` (full skills) or `~/Desktop/zurb.nosync/skills/glare-prompts-flat/` (portable prompts) |
| The 6-piece signal anatomy (design intuition / UX metric / user need / context / business goal / direction); the Need / Use / Prefer / Adopt taxonomy; signal quality; capturing signals in the work | `glare-design-signals`, `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing` | same two folders |
| Team / org maturity diagnostic — the five dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence); score bands; reading patterns; using results | `glare-design-assessment` and the five dimension skills, plus `glare-assessment-scoring`, `glare-assessment-reading`, `glare-assessment-using-results` | same two folders |
| UX Metrics as a top-level section (the four metric types treated separately from Define) | `glare-ux-metrics` | same two folders |
| Onboarding extras — "what is Glare," conceptual tour, AI workflows, coaching / advising, proving design impact, glossary, creating your first signal | `glare-get-started`, `glare-how-glare-works`, `glare-create-first-signal`, `glare-ai-workflows`, `glare-coaching-advising`, `glare-proving-design-impact`, `glare-glossary` | same two folders |

When you route someone to a skill outside this install, name the exact skill, point them at the folder, and stop. Don't try to do that skill's work from here — the router only routes inside the 21 Decision Map skills it ships with.

---

## What the router never does

- Recommends a list of skills. (One.)
- Recommends a skill that isn't installed in this marketplace (the 21 Decision Map skills). External skill names appear only in the "Outside the core marketplace" note as a pointer.
- Tries to do the destination skill's work itself.
- Re-routes a user who is already productive in their current skill.
- Lectures the framework before routing. If they want the spine view, the right route is `glare-decision-map`.
