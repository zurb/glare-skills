# Comparing — Reference

Verbatim extract from `focus-compressed.md`. Source: "Glare | Focus, Comparing v1.1."

---

## Glare | Focus, Comparing v1.1

**What Comparing does.** Benchmarking connects individual signals to a broader pattern of performance over time. Good comparing tracks improvements/regressions across releases, shows shifts in user behavior or satisfaction, validates that design changes deliver measurable outcomes, and gives context for interpreting earlier signals. Without comparison, data stays isolated; with it, data becomes proof.

**Four outcomes comparison creates:**
- **Accountability:** progress tracked and visible across time.
- **Context:** performance anchored to baselines or competitors.
- **Confidence:** evidence to prioritize what works and stop what doesn't.
- **Continuity:** consistent UX metrics that build a pattern of improvement.

**How Comparing fits in the Focus facet** (sequence: Initiatives → Methods → Comparing → Decisions):
- **Initiatives** — define goals/outcomes; benchmarking validates whether each one is achieved.
- **Methods** — outline how signals are collected; comparing reveals trends from those signals.
- **Comparing** — analyzes patterns and performance over time; turns signals into trends.
- **Decisions** — act on what's proven; benchmarked data becomes proof to prioritize, refine, or scale.

**Comparison Approaches (the 10 lenses):**
1. **Iteration** — track improvement across releases/versions (e.g., completion rates v1 vs v2 of checkout).
2. **Competitors** — relative market performance (satisfaction/engagement vs top competitors).
3. **Timeline** — UX metrics at consistent intervals (quarterly comprehension/satisfaction).
4. **Segments** — across user groups (new vs returning users).
5. **Journeys** — success at key journey stages (awareness, adoption, retention).
6. **Platforms/Devices** — friction across contexts (desktop vs mobile completion time).
7. **User Goals/Tasks** — effectiveness on primary goals across releases.
8. **Feature Usage** — adoption and perceived value before/after redesign.
9. **Behavioral Triggers** — engaged vs dormant cohort conversion.
10. **Season** — cyclical/campaign-based UX shifts (sentiment across seasonal cycles).

**Three questions consistent benchmarking answers:** Are we improving the experience or just changing it? Where does friction persist? Which design decisions move the right metrics?

### Begin Comparing Data — 5-Step Process

**STEP 1 — Establish Your Baseline.** Capture the "before" state, typically from Measure → Concepts. Stronger baselines stack attitudinal, behavioral, and performance metrics. Tips: capture user need + business goal behind the change; record comprehension, desirability, completion; document version, date, and audience for repeatability. Goal: answer "what works now" and "what success should look like later."

**STEP 2 — Define What You'll Benchmark.** Pick 4–5 primary approaches and note why each comparison matters. Common picks:
- **Iteration** — show measurable improvement v1 → v2.
- **Competitor** — understand positioning/differentiation.
- **Segment** — reveal friction or bias in key cohorts.
- **Journey** — identify drop-offs or weak funnel transitions.
- **Platform** — find where usability/speed impacts conversion.

**STEP 3 — Normalize Your Data.** Glare auto-normalizes UX metrics onto a **100-point scale** (Comprehension, Satisfaction, Desirability, Completion, etc.). For external data, match scales and adjust for outside factors. Checklist: same metric formulas, equivalent sample sizes/conditions, adjust for outliers and seasonal/campaign timing.

**STEP 4 — Identify the Deltas.** Look for where change occurs. Use a spreadsheet or Glare comparison view. Sample delta table format: Metric | Baseline | Current | Δ Change | Signal Interpretation. Large deltas (positive or negative) often point to the design decisions that matter most.

**STEP 5 — Interpret the Signal.** Numbers are useful only when they tell a story. Example (Klean Kanteen competitive review): the delta on "unoriginal imagery" exposed that black overlays on every banner photo improved legibility but dulled imagery and depressed sentiment. Lightening the overlays restored contrast → sentiment up, perceived originality up, conversion up. Visual clarity was functional proof, not aesthetics.

### Make It Practical — Repeatable Worksheet

| Step | Action | Output |
|---|---|---|
| 1. Establish Baseline | Record current design + UX metric stack tied to user need and business goal. | Clear starting point and proof of today. |
| 2. Define Benchmark Type | Choose approach (iteration/competitor/segment/journey/platform); note why. | Defined purpose and success criteria. |
| 3. Normalize Data | Confirm 100-point scale, audience size, method; adjust outliers. | One-to-one comparable data. |
| 4. Identify Deltas | Highlight what improved, declined, stayed flat; visualize. | Visible patterns of progress/gaps. |
| 5. Interpret & Share | Tie metric shifts to design changes; one-line summary linked to Decision record. | Structured proof of impact + next actions. |

**Quick Checklist:** reliable baseline tied to goals; benchmark type and reason clear; data normalized; deltas captured and visualized; findings shared and connected to next decisions.

### See It in Action — Homepage Benchmark Across Competitors

Five outdoor drinkware brands (Klean Kanteen, Yeti, Stanley, Owala, Hydro Flask) tested with the same UX metric stack: Engagement, Helpfulness, Sentiment, NPS. A market snapshot, not a redesign test.

| Brand | Engagement | Helpfulness | Sentiment (Net +) | NPS | Signal Highlights |
|---|---|---|---|---|---|
| Klean Kanteen | 27% | Low | 189% | 11.8 | Low engagement; imagery flat/unoriginal. |
| Yeti | 29% | Low | 188% | 25.0 | Customization draws interest; needs emotional variety. |
| Stanley | 35% | Medium | 192% | 19.7 | Carousel + brand collabs drive engagement. |
| Owala | 32% | Medium | 204% | 23.4 | Strong social proof; clear product storytelling. |
| Hydro Flask | 33% | Medium | 235% | 30.6 | Bright, joyful visuals; clear hierarchy; seasonal messaging. |

Klean Kanteen's sentiment lagged Hydro Flask by ~45 points. Visual review confirmed the cause: dark text overlays on every hero photo dulled imagery vs competitors using bolder color and lighter visuals. **Outcome:** the design problem was reframed from "we need a new homepage" to "we need stronger emotional clarity and originality," with future goals tied directly to first-click engagement, visual appeal, and brand sentiment.

### Apply and Evolve — 7 Habits to Make Benchmarking Stick

1. **Connect to Purpose** — every benchmark traces to a user need or business goal.
2. **Share What You See** — keep benchmarks visible in dashboards/reviews.
3. **Use Results to Drive Decisions** — bring comparison data into sprints, roadmaps, design reviews.
4. **Refresh Baselines on a Schedule** — same metric stack each release or quarter.
5. **Expand When Ready** — start with one flow, then widen to new audiences, devices, competitors.
6. **Link UX Metrics to Business Outcomes** — translate lifts in comprehension/satisfaction/completion into adoption, retention, conversion.
7. **Standardize and Automate** — store metrics, deltas, decisions in shared templates/dashboards.

**Quick Habit Check:** benchmarks connect to goals; results shared; baselines refreshed each release/quarter; trends visible over time; decisions informed by measurable improvement.

**Next Steps from Comparing:**
- → **Decisions** — apply benchmarks to guide direction and set priorities.
- → **Mapping** — translate clarity into measurable business alignment.
- → **Methods** — refine how/when you collect future benchmarks for consistency.

## Key terms

- **Focus (facet)** — Glare facet that links Initiatives → Methods → Comparing → Decisions to convert design signals into directional clarity.
- **Comparing / Benchmarking** — the discipline of measuring consistent UX metrics across versions, audiences, or competitors to validate progress.
- **Baseline** — documented "before" state of a design (version, date, audience, metric stack) used as the anchor for future comparison.
- **Delta (Δ)** — the change between baseline and current measurement; large deltas flag the design decisions that matter most.
- **Normalization** — aligning all metrics onto a comparable scale; Glare uses a 100-point scale for Comprehension, Satisfaction, Desirability, Completion, etc.
- **UX metric stack** — combined attitudinal, behavioral, and performance metrics captured together for stronger baselines.
- **Comparison Approaches** — the 10 lenses: Iteration, Competitors, Timeline, Segments, Journeys, Platforms/Devices, User Goals/Tasks, Feature Usage, Behavioral Triggers, Season.
- **Signal Interpretation** — the narrative meaning attached to a delta (e.g., sentiment up = emotional response improved).
- **Initiatives / Methods / Decisions** — the other three areas of the Focus facet that bracket Comparing.
- **Measure → Concepts** — the upstream Glare area where baselines are typically captured.
- **Define facet** — the cross-referenced facet that holds the data-collection techniques used by these comparisons.
