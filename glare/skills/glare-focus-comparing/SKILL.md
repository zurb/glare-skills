---
name: glare-focus-comparing
description: Use this skill when the user is **Comparing** in the Glare Focus facet — placing signals side by side to see what performs better. (Note: the v1.3 source doc is titled "Compare" but the skill folder keeps "comparing" to preserve install paths.) Triggers include "compare versions," "v1 vs v2," "we have results but no context," "is this score good or bad," "compare against a benchmark," "compare audiences/segments/cohorts," "competitor comparison," "side by side," "which option is stronger," "what's the tradeoff," "did this actually improve or just change," "compare across platforms/devices," "compare across regions," "before and after," "compare across the journey," "compare across seasons or cycles." Also use when the user mentions any of the 12 comparison points — Iteration, User Goals/Tasks, Competitors, Feature Usage, Timeline, Geographies, Segments, User Lifecycle, Journeys, Behavioral Triggers, Platforms/Devices, Season — or the 5-step comparing process (name the decision → choose the comparison point → use the same metric → look for the strongest signal and the tradeoff → turn the comparison into a finding). Do NOT use when the initiative isn't framed (use `glare-focus-initiatives`), the right frame for the data hasn't been chosen (use `glare-focus-methods`), or the team is ready to commit (use `glare-focus-decisions`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user **Compare** signals — the third move in the Glare Focus facet.

## Core idea

Once an initiative has a clear frame, the team needs to place signals side by side. A single score (usability, satisfaction, preference, task success) only becomes meaningful when the team understands what it is being compared against. Comparing helps teams see what changed, what improved, what fell behind, and which direction creates the strongest signal. It gives context to the data so teams can explain why one option deserves more energy than another. Without comparison, results stay isolated; with it, signals become easier to trust.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of Compare v1.3: why comparing matters, what goes into a comparison, the 12 comparison points (Iteration, User Goals/Tasks, Competitors, Feature Usage, Timeline, Geographies, Segments, User Lifecycle, Journeys, Behavioral Triggers, Platforms/Devices, Season), the 5-step comparing process, what comes out of comparing, and where comparing works best.

## How to apply

1. **Insist on a shared metric first.** Before placing results side by side, the team needs to know what is being measured and why. The comparison only works if signals are clear enough to line up. Same metric formulas, equivalent context, named exceptions.

2. **Confirm the inputs.** A strong comparison includes a clear initiative, a method frame, two or more things to compare, a UX metric that applies across them, an audience/segment, a signal from users, and a decision the comparison should support.

3. **Pick from the 12 comparison points** based on what the decision needs:
   - **Iteration** — Did the new version improve? Which change created the most lift?
   - **User Goals/Tasks** — Which task is easiest/hardest? Where does effort increase?
   - **Competitors** — Where do competitors create more clarity? What expectations are users bringing?
   - **Feature Usage** — Which features create most value? What should be built/improved/reduced/removed?
   - **Timeline** — What needs attention first? Are signals improving over time?
   - **Geographies** — Where does the experience perform better/worse by region?
   - **Segments** — Which segment sees most value? Which group struggles more?
   - **User Lifecycle** — What does a new user need vs. existing? Where does momentum break?
   - **Journeys** — Which journey moment creates most friction? Where does confidence drop?
   - **Behavioral Triggers** — What makes users start? What causes hesitation?
   - **Platforms/Devices** — Does the experience work across mobile/desktop/tablet? Where does usability drop?
   - **Season** — Does behavior change by season/cycle? Is the signal durable?

4. **Run the 5-step process:**
   - **Name the decision.** What does the comparison need to support? If unclear, the comparison feels like a report instead of a guide.
   - **Choose the comparison point.** What gets placed side by side? Should connect directly to the decision.
   - **Use the same metric.** Shared UX metric so the comparison is fair. If using different metrics, name that explicitly.
   - **Look for the strongest signal AND the tradeoff.** Don't only ask which option wins — ask what each option strengthens and what it weakens. The strongest direction is not always the highest score; it's the best signal for the decision.
   - **Turn the comparison into a finding.** End with: what was compared, which signal was stronger, what tradeoff showed up, what the team should do next. Not a data display — direction.

5. **Don't force a comparison without a metric.** If the team doesn't know what matters, everything looks comparable. Route back to `glare-focus-initiatives` or `glare-focus-methods` to clarify the metric or decision first.

6. **Hand off to `glare-focus-decisions`** once the comparison has produced a finding with a tradeoff — the next move is committing to a decision type.

## Handoffs

- Reframing the initiative if the metric is unclear → `glare-focus-initiatives`
- Choosing a different frame if the comparison won't lift → `glare-focus-methods`
- Turning the finding into a clear next move → `glare-focus-decisions`
- Upstream: turning hunches into testable signals → `glare-measure`
- Connecting the chosen direction to business outcomes → `glare-lead`
- The whole Focus flow → `glare-focus`
- The Define → Measure → Focus → Lead chain → `glare-decision-map`
