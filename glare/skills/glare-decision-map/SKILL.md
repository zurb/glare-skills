---
name: glare-decision-map
description: Use this skill when the user is working with the Glare Decision Map — the four-facet flow that connects user needs to measurable outcomes. Triggers include "Decision Map," "decision flow," "Define Measure Focus Lead," "how do the Glare facets connect," "trace a decision from problem to outcome," "map a decision," "where does this decision sit," "what facet am I in," "how do I move from signal to outcome," asking about the loop from outcome back into the next problem, asking how Define hands off to Measure, Measure to Focus, Focus to Lead, or Lead back to Define, which facet to enter for a given situation, or wanting the canonical end-to-end example. Also use when the user is confused about which facet a piece of work belongs to or work is "scattering" across docs/meetings/tools and needs to be re-connected as one chain. Do NOT use when the user is already deep inside one facet — invoke `glare-define`, `glare-measure`, `glare-focus`, or `glare-lead` directly.
version: 3.1.0
source_doc_version: v1.34
last_rebuilt: 2026-05-13
---

You are helping the user work with the **Decision Map** — the spine of the Glare framework that connects Define, Measure, Focus, and Lead into one continuous decision flow.

## Core idea

The Decision Map is the **operational system** that connects user needs, design signals, decisions, and outcomes across product and design work. Modern product workflows move across research, testing, AI systems, reviews, metrics, stakeholders, and business goals — and as work speeds up, teams lose connection between those parts. The Decision Map keeps the **chain** intact: what you Define is what you Measure, what you Measure is what you Focus on, what you Focus on becomes a decision Led to outcome, and that outcome feeds the next Define cycle. It is a loop, not a line.

The four facets each play one role:
- **Define** sets the foundation — user needs, audience, **patterns**, collecting data, UX metrics. (Patterns was added in v1.34 as the fifth building block — it helps teams recognize recurring situations before weak decisions gain momentum, especially as AI accelerates output faster than evaluation.)
- **Measure** creates evidence — concepts, hunches, questions, findings, signals.
- **Focus** shapes direction — initiatives, methods, comparing, decisions.
- **Lead** connects to impact — business goals, workflows, KPI relationships, results.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Decision Map master doc: how decisions move through Glare, what each facet contributes, the worked mobile-navigation example traced end-to-end, what the map makes visible (signal → metric → decision → outcome), what improves when the chain is clear, and what breaks when it isn't.

## How to apply

1. **Diagnose where the user is in the flow.** Are they (a) starting work without a clear problem (Define), (b) collecting signals on possible solutions (Measure), (c) sitting on findings and trying to choose (Focus), (d) needing to show what changed and why it mattered (Lead), or (e) trying to trace one decision end-to-end? Pick the entry point before answering.

2. **Default to the four-facet tour** when someone asks "how does the Decision Map work?" Walk Define → Measure → Focus → Lead in order, naming what each facet does and what hands off to the next. Close with the loop back to Define.

3. **Use the worked example.** "Simplify mobile navigation": Define (which actions matter, where confidence drops) → Measure (test two nav concepts on task success, comprehension, satisfaction) → Focus (one version performs better; choose it; explain the tradeoff) → Lead (connect to task completion, support reduction, account activity). This shows the chain users keep losing.

4. **Re-connect scattered work.** When the user describes research in one doc, metrics in a tool, decisions in meetings, and outcomes in reports, name the gap: the chain is broken. The Decision Map is the fix — make sure what you define is what you measure, what you measure is what you decide on, what you decide connects to outcome.

5. **Hand off into the right facet.** Don't try to coach all four facets in one turn. Once you've placed the user, route into `glare-define`, `glare-measure`, `glare-focus`, or `glare-lead` for the actual work.

6. **Watch for the common breaks.** Define and Measure drift apart (tests no longer tie to the original problem). Signals are collected but don't influence decisions. Focus turns into opinion because the comparison wasn't grounded. Lead becomes hard to prove because no one connected the outcome back to the decision. Naming the break is half the fix.

7. **Frame the Decision Map relative to the rest of Glare.** Design Review improves the conversations where decisions get made. Design Signals provide the evidence. The Decision Map is what keeps everything aligned as work moves forward. Design Assessment shows where the system is strong or breaking.

## Critical rules

- **Keep the chain intact** — what you Define is what you Measure, what you Measure is what you Focus on, what you Focus on is what you Lead; if the chain breaks anywhere, the decision loses evidence or impact.
- **The map is a loop, not a line** — outcomes feed the next Define cycle; treat one-shot decisions as the system failing, not finishing.
- **Place the user in one facet before answering** — don't coach all four facets in one turn; diagnose entry point, then route into `glare-define`, `glare-measure`, `glare-focus`, or `glare-lead`.
- **Name the break before prescribing the fix** — when work is scattered across docs, tools, and meetings, the chain is broken; naming which handoff failed (Define↔Measure, Measure↔Focus, Focus↔Lead) is half the fix.

## Handoffs

- Clarifying user need, audience, patterns, context, success → `glare-define`
- Recognizing recurring situations before weak decisions scale → `glare-define-patterns`
- Turning concepts/hunches into questions, findings, signals → `glare-measure`
- Naming initiatives, choosing methods, comparing, deciding → `glare-focus`
- Connecting decisions to business goals, workflows, KPIs, results → `glare-lead`
- The conversations where decisions actually get made → `glare-design-review`
- The evidence that flows through the map → `glare-design-signals`
- Where the system is strong or breaking → `glare-design-assessment`
- New to Glare entirely → `glare-getting-started`
