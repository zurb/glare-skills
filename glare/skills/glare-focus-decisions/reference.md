# Glare | Focus, Decisions — Drafted (no source doc available)

> This block is **drafted from framework knowledge**, not from a dedicated Drive source doc. It extrapolates from `focus-compressed.md` (Comparing v1.1), the `glare-focus` parent skill, the Big Idea #12 decision-move taxonomy, and the Ray spec's signal-reference and tradeoff-articulation guardrails. Treat as best-effort scaffolding until an authoritative "Glare | Focus, Decisions" source lands.

## What this block is about

In Glare v1.0, **Decisions** is the downstream step of the Focus facet (sequence: Initiatives → Methods → Comparing → Decisions). Decisions is where benchmarked, validated signals become action — and where Focus closes the loop, often spawning the next Initiative. Per the Comparing doc: "Decisions — act on what's proven; benchmarked data becomes proof to prioritize, refine, or scale." Per Big Idea #12, the available moves are explicit. Per the Ray spec, no decision is allowed without a signal reference and an articulated tradeoff.

## Glare | Focus, Decisions v0.1 (drafted)

**What Decisions does.** Decisions converts a benchmarked delta — produced by Comparing against an Initiative's outcome target — into one of a small set of explicit moves, recorded in a way that downstream rituals (backlog, roadmap, release-readiness) can consume without re-litigating the evidence.

**Three outcomes Decisions creates:**
- **Closure** — the Initiative is resolved (achieved / partial / missed) instead of drifting indefinitely.
- **Direction** — the next concrete move is named, with the tradeoff stated.
- **Continuity** — the Decision record travels into backlog/roadmap and seeds (or kills) the next Initiative.

### The 5 Decision Moves (Big Idea #12 taxonomy)

Force the team to name which one. "Let's keep going" is not a decision.

1. **Advance** — ship / roll out / scale. The Initiative's outcome target was met or exceeded; design and Method are stable enough to widen audience or platform.
2. **Refine** — iterate again on the same Initiative. Direction is right, magnitude is short. Re-run Methods at the same M-version.
3. **Kill** — stop the Initiative. The kill criterion (set during Initiatives) was tripped, or repeated refinement isn't moving the metric.
4. **Scope-differently / Pivot** — the metric isn't moving because the problem was framed wrong. Reframe the Initiative (often the Klean Kanteen pattern: "we need a new homepage" → "we need stronger emotional clarity"). Pivot is a sub-case where the audience or surface changes too.
5. **Reprioritize** — the data is fine but a higher-priority Initiative now claims the team's capacity. Park, don't kill; record so future planning can resume.

### Criteria for Each Move — Based on Benchmark Deltas

Read against the Initiative's named outcome target (e.g., Completion +13 pts) and the kill criterion (e.g., ±2 pts).

| Move | Delta vs target | Other conditions |
|---|---|---|
| Advance | Δ ≥ target on primary metric; secondary metric not regressed past kill threshold | Method M-version stable; audience representative; tradeoff articulated. |
| Refine | 0 < Δ < target; trend in right direction | At least one more refinement cycle is affordable; specific design lever identified. |
| Kill | Δ inside the kill window (e.g., ±2 pts) after ≥2 cycles, OR a secondary metric regressed past kill threshold | Reframing already attempted, or no plausible reframe remains. |
| Scope-differently / Pivot | Δ flat or wrong-direction AND post-mortem reveals the Initiative's framing was wrong | Reframed Initiative drafted before the Pivot is final. |
| Reprioritize | Any Δ; capacity constraint dominates | New top-priority Initiative named; current Initiative parked with state preserved. |

The Ray spec's guardrail applies to all five: **no decision without a signal reference**, and **the tradeoff must be explicit** — what is being given up, which constraints are now locked vs flexible.

### The Decision Record Template

Every Decision writes one of these. Tight. The record is the artifact; meetings without one stall.

```
INITIATIVE:    [link to Initiative record]
METHOD:        [M-version; link to Method record]
SIGNAL REF:    [Comparing benchmark output: metric | baseline | current | Δ]
MOVE:          [Advance | Refine | Kill | Scope-differently / Pivot | Reprioritize]
RATIONALE:     [1–3 sentences tying the Δ to the move]
TRADEOFF:      [What is being given up; what is now locked vs flexible]
NEXT INITIATIVE: [Link if Pivot/Kill spawns a new one; "none" if Advance/Reprioritize]
HAND-OFF:      [Backlog | Roadmap | Release-readiness | Lead reporting]
OWNER + DATE:  [Who decided; when]
```

### Hand-off Rituals — Where Decisions Travel

A Decision is only real once it lands in the rituals downstream teams already run. Per move:

- **Advance →** *Release-readiness review.* The Decision record is the green-light artifact; the Method record is the proof of how the green light was earned. Also goes to **Lead** for cross-functional reporting (Workflows + Mapping pull the chain of proof up to Business KPIs).
- **Refine →** *Backlog grooming.* The Decision record becomes a prioritized backlog item with the named design lever and the next Method-cycle date.
- **Kill →** *Roadmap review.* Removes the Initiative from active capacity; the Decision record is the receipt explaining why so the same Initiative doesn't come back as someone's pet idea next quarter.
- **Scope-differently / Pivot →** *Initiatives intake.* Decision spawns a new Initiative record (back to `glare-focus-initiatives`); the original Initiative is closed with a pointer to the new one.
- **Reprioritize →** *Roadmap review.* Initiative parked with state preserved (last benchmark, last Method version, kill criterion); resumable when capacity returns.

### Decision Record — Worksheet

| Field | Action | Output |
|---|---|---|
| Signal reference | Pull the Comparing delta table row(s) that triggered the Decision. | No decision without evidence. |
| Move | Pick one of the 5; never "let's keep going." | Concrete next state. |
| Rationale | Tie the Δ to the move in 1–3 sentences. | Auditable reasoning. |
| Tradeoff | State what's given up; what's locked vs flexible. | Honest commitment. |
| Hand-off | Route to backlog / roadmap / release-readiness / Lead reporting. | Decision actually travels. |
| Loop-back | Spawn next Initiative if Pivot/Kill; close current. | Focus loop closes. |

**Quick Checklist:** signal ref present; move named (one of 5); tradeoff explicit; hand-off route chosen; original Initiative closed or refined; Decision record stored where downstream rituals consume it.

### See It in Action — Mobile Checkout Decision

Continuing the example from `focus-initiatives-compressed.md` and `focus-methods-compressed.md`. v2 of mobile checkout shipped under Method M1. Comparing produced:

| Metric | Baseline (v1) | Current (v2) | Δ | Interpretation |
|---|---|---|---|---|
| Completion | 62 | 71 | +9 | Direction right, short of +13 target. |
| Error Rate (inverted, 100-pt) | 67 | 78 | +11 | Exceeded −8 target (8 → +11 in 100-pt terms). |
| Satisfaction | 64 | 70 | +6 | Confirms the experience improved, not just the funnel. |

Decision record:
```
INITIATIVE:    Mobile Checkout v1 → v2 (first-time mobile US)
METHOD:        M1 (n=120 task-success + post-task Likert; frozen)
SIGNAL REF:    Completion +9 (target +13); Error Rate +11 (target +8); Satisfaction +6
MOVE:          REFINE
RATIONALE:     Error Rate target met and Satisfaction up, but Completion fell 4 pts short of target.
               Diagnostic review on the v2 funnel shows residual friction at the address-confirm step,
               which the redesign didn't touch. One more refinement cycle is affordable in Q3.
TRADEOFF:      One additional sprint of Engineering capacity now allocated to address-confirm; the
               adjacent guest-checkout Initiative is delayed two weeks. Locked: Method M1 (no audience
               or instrument changes). Flexible: the address-confirm UI pattern.
NEXT INITIATIVE: none (same Initiative, refinement v2.1)
HAND-OFF:      Backlog grooming (next sprint) + Lead reporting (Q3 mid-cycle update)
OWNER + DATE:  Design lead — 2026-04-22
```

If Completion had landed at 63 instead of 71, the kill window (±2 pts) would have been tripped and the move would be **Kill** with a pointer to a new Initiative on payment-provider integration (per the Initiative's pre-named kill plan).

### Next Steps from Decisions

- → **Initiatives** — Pivot/Kill moves spawn new Initiative records; the loop reopens.
- → **Lead** (`glare-lead`) — Advance moves and major Refine cycles get translated into business-KPI language for executive reporting.
- → **Methods** — if the Decision included a Method-version change (M1 → M2), Methods owns the bridge round before the next Comparing cycle.

## Key terms

- **Decision** — a recorded move (one of 5) that converts a benchmarked signal into action; closes the Focus loop.
- **5 Decision Moves** — Advance, Refine, Kill, Scope-differently/Pivot, Reprioritize (per Big Idea #12).
- **Signal reference** — the specific Comparing delta(s) that justify the Decision; required by Ray spec.
- **Tradeoff articulation** — explicit statement of what is being given up; required by Ray spec.
- **Decision record** — the artifact downstream rituals (backlog, roadmap, release-readiness) consume.
- **Kill window** — the ±delta range, defined upfront in Initiatives, that triggers a Kill move.
- **Hand-off rituals** — backlog grooming, roadmap review, release-readiness review, Lead reporting; where Decisions actually travel.
- **Loop closure** — the property that every Decision either closes its Initiative or spawns the next one; Focus is a loop, not a one-shot.
