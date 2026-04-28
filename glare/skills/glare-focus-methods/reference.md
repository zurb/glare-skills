# Glare | Focus, Methods — Drafted (no source doc available)

> This block is **drafted from framework knowledge**, not from a dedicated Drive source doc. It extrapolates from `focus-compressed.md` (Comparing v1.1), the `glare-focus` parent skill, and the data-collection vocabulary established in Measure → Questioning v1.1 (`measure-compressed.md`). Treat as best-effort scaffolding until an authoritative "Glare | Focus, Methods" source lands.

## What this block is about

In Glare v1.0, **Methods** is the second step of the Focus facet (sequence: Initiatives → Methods → Comparing → Decisions). Methods is where teams design *how* signals get collected so that comparisons later are repeatable and trustworthy. Per the Comparing doc: "Methods — outline how signals are collected; comparing reveals trends from those signals." The Comparing doc explicitly loops back here ("→ Methods — refine how/when you collect future benchmarks for consistency"), which is the strongest hint that Methods owns the discipline of collection-design, not collection itself.

## Glare | Focus, Methods v0.1 (drafted)

**What Methods does.** Methods turns an Initiative's named outcome and metric(s) into a *collection plan* — cadence, instruments, sample size, audience definitions, and normalization rules — so that every future round produces data Comparing can normalize and trend without rebuilding the test. Without Methods, every benchmark is a snowflake; with it, deltas reflect the *design*, not collection drift.

**Four outcomes Methods creates:**
- **Repeatability** — version N+1 collects the same data the same way as version N.
- **Stackability** — attitudinal + behavioral + performance metrics captured together, not in separate one-off tests.
- **Normalizability** — data lands on the 100-point scale by design, so Comparing's Step 3 is a check, not a rebuild.
- **Auditability** — every collection records version, date, audience, and instrument, so a baseline can always be re-traced.

### Inputs from Initiatives

Methods doesn't pick goals. It operationalizes the Initiative record. Confirm before designing:

- **Metric(s)** — which slots of the 100-point stack (Comprehension / Satisfaction / Desirability / Completion / Error Rate / First-Click / Time-on-Task) the Initiative named.
- **Audience** — the cohort/segment/device/journey-stage definition the Initiative locked.
- **Outcome target** — the delta the Initiative committed to (e.g., Completion +13 pts).
- **Kill criterion** — the upfront falsifier so Methods can size the test for the smallest delta that would matter.

### Plan Signal-Collection — 5 Levers

For each Initiative, Methods picks an explicit setting for each of these. Future iterations must keep all five frozen unless the team explicitly versions the Method.

1. **Cadence.** Per release / quarterly / per major iteration / per campaign. The cadence has to outlast personnel changes; pick the slowest cadence that still meets the decision tempo.
2. **Instruments.** The technique used per metric layer (see method catalog below). Each metric should have one and only one default instrument per Initiative.
3. **Sample sizes.** Sized to the smallest delta the kill criterion needs to detect. Floor of n=30 per cohort for attitudinal; n=80–120 for behavioral; document the rule used.
4. **Audience definitions.** Recruitment criteria written as a recipe (cohort filter, device, region, recency, prior exposure). The same recipe is reused every round.
5. **Conditions.** Device mix, time-of-day window, campaign overlap, seasonality flags. Frozen at v1 and re-applied at every subsequent collection.

### Method Catalog — Mapped to the 100-Point Comparison Stack

These are the default instruments Methods recommends per metric. Pick one per Initiative metric and stick with it.

| Metric (100-pt stack) | Layer | Default Instrument(s) | Notes for Comparing |
|---|---|---|---|
| Comprehension | Perceptual | Survey + 5-second test; Heatmap-supported recall | Score on 100-pt comprehension rubric. |
| Satisfaction | Attitudinal | Post-task Likert + open-text sentiment coding | Net-positive transformed to 100-pt. |
| Desirability | Attitudinal | Microsoft Reaction Cards / desirability scoring | Aggregate to 100-pt scale. |
| Completion | Performance | Task-success test (moderated or unmoderated) | Direct % → 100-pt. |
| Error Rate | Performance | Task test with error tagging | Inverted to 100-pt (fewer errors = higher). |
| First-Click Success | Behavioral | First-click test | Direct % → 100-pt. |
| Time-on-Task | Performance | Task test with timer | Normalized vs benchmark median. |
| Engagement | Behavioral | Clickstream / session analytics | Cohort-normalized. |
| NPS | Attitudinal | Standard NPS prompt | Mapped to 100-pt scale (per Klean Kanteen example in Comparing). |

Stronger baselines stack at least one metric from each layer (per Comparing doc Step 1). Default recommendation: pick 1 attitudinal + 1 behavioral + 1 performance per Initiative.

### Repeatability Rules

- **Version the Method, not the metric.** If you change cadence/instrument/sample/audience/conditions, increment Method version (M1 → M2). Comparing must know whether a delta crossed a Method-version boundary, because that breaks like-for-like.
- **Freeze conditions at v1.** If v1 ran on iOS-only desktop browsers in November, v2 runs the same way. If conditions must change, run a parallel "bridge" round that collects under both conditions to quantify the shift.
- **Normalize at collection time.** Apply the 100-point transformation when data is captured, not later. For external/third-party sources, define the scale-matching rule in the Method record.
- **Record every collection.** Version, date, audience recipe, instrument, sample size, conditions. This is what makes a baseline a baseline.
- **Bias check the instrument.** Same hygiene as Measure → Questioning: is the question leading? echoing assumptions? emotionally loaded? too technical? Re-check at every cadence.

### Method Record — Worksheet

| Field | Action | Output |
|---|---|---|
| Initiative ref | Link the Initiative the Method serves. | Traceability. |
| Cadence | Pick the slowest cadence that meets decision tempo. | Predictable refresh schedule. |
| Instruments | One default per metric (from catalog). | Same instrument every round. |
| Sample size | Floor + rule (e.g., powered to detect kill-threshold delta). | Statistically defensible deltas. |
| Audience recipe | Cohort + device + region + recency + recruitment filter. | Repeatable cohort. |
| Conditions | Device mix, time window, campaign/seasonality flags. | Drift-controlled environment. |
| Normalization rule | 100-pt transformation applied at capture. | Comparing Step 3 becomes a check, not a rebuild. |
| Version | M1, M2, … incremented when any lever changes. | Honest like-for-like. |

**Quick Checklist:** metric/audience pulled from Initiative; instrument chosen per metric; cadence locked; sample size sized to kill threshold; conditions frozen; normalization applied at capture; Method version recorded.

### See It in Action — Methods for the Mobile Checkout Initiative

Continuing the Initiative from `focus-initiatives-compressed.md`: Completion +13 pts on first-time mobile US, with Error Rate −8 pts as the second metric.

Method M1 record:
- **Cadence:** Per release (target: v1 baseline now, v2 after redesign ships in Q3).
- **Instruments:** Unmoderated task-success test (Completion + Error Rate); post-task Likert (Satisfaction, third metric for stacking).
- **Sample size:** n=120 per round (powered to detect a 6-pt completion delta at 80% power; smaller than the 13-pt target so the kill criterion of ±2 pts is also resolvable).
- **Audience recipe:** First-time visitors, mobile (iOS + Android, 50/50 split), US, no prior exposure to checkout in last 30 days.
- **Conditions:** Tuesday–Thursday 10am–4pm ET; no overlap with seasonal sale campaigns; checkout sandbox with $24.99 standard cart.
- **Normalization:** Completion and Error Rate captured as % and inverted/transformed to 100-pt at capture; Satisfaction Likert mapped to 100-pt via standard rubric.
- **Method version:** M1 (frozen for v1 baseline and v2 comparison).

When v3 ships and the team wants to widen to Canada/UK, that's an M2 — the audience recipe changed, so a bridge round is required to keep deltas honest.

### Next Steps from Methods

- → **Comparing** — once M1 collects v1 baseline, Comparing runs the 5-step process; same Method runs again at v2 for like-for-like deltas.
- → **Decisions** — Method record travels with the benchmark so Decisions can audit how the data was produced.
- ← **Initiatives** — if a kill criterion isn't detectable at the planned sample size, send the Initiative back for tighter scoping.

## Key terms

- **Methods** — the Focus-facet step that designs *how* signals get collected so Comparing is repeatable.
- **5 Levers** — Cadence, Instruments, Sample Size, Audience, Conditions; the five settings every Method record locks.
- **Method Catalog** — default instruments mapped to each slot of the 100-point UX metric stack.
- **Stackable metric set** — at least one attitudinal + one behavioral + one performance metric, captured together (per Comparing Step 1).
- **Method version (M1, M2…)** — incremented when any lever changes; Comparing must know about version changes to interpret deltas honestly.
- **Bridge round** — a parallel collection under both old and new conditions to quantify the impact of a Method-version change.
- **Normalization at capture** — applying the 100-point transformation when data is recorded rather than during analysis.
- **Audience recipe** — the reusable recruitment definition (cohort + device + region + recency + filter) that future rounds re-apply.
- **Kill-threshold sizing** — sizing samples to detect the smallest delta that would trigger the Initiative's kill criterion.
