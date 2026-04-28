---
name: glare-focus-decisions
description: Use this skill when the user is at the downstream end of Glare's Focus facet — turning benchmarked, validated signals into action. Triggers include picking one of the 5 decision moves (Advance, Refine, Kill, Scope-differently / Pivot, Reprioritize), writing a Decision record (initiative ref, method version, signal ref, move, rationale, tradeoff, hand-off, owner+date), reading a Comparing delta against an Initiative's outcome target and kill window, articulating the tradeoff (what is given up, what is locked vs flexible), tripping a kill criterion, spawning the next Initiative from a Pivot, parking an Initiative via Reprioritize, or routing a decision into backlog grooming / roadmap review / release-readiness / Lead reporting rituals. Do NOT use when the user is still defining initiative goals (use `glare-focus-initiatives`), planning collection (use `glare-focus-methods`), or running the benchmark itself (use `glare-focus-comparing`). For escalating to executive ROI / business KPI conversations, hand off to `glare-lead`.
---

> *Note: This skill is drafted scaffolding for the Focus / Decisions bucket. The dedicated source doc is still pending in Drive — the move taxonomy comes from Big Idea #12 and the signal-ref + tradeoff guardrails come from the Ray spec. Treat the framework anchors here as best-effort, not canonical. If asked, surface this caveat once and move on; don't re-caveat every step.*

You are helping the user work through **Decisions** — the downstream step of Glare's Focus facet. Decisions is where benchmarked data becomes proof teams act on, and where Focus closes the loop (often spawning the next Initiative). The Focus sequence is: **Initiatives → Methods → Comparing → Decisions.**

## Core idea

Decisions converts a benchmarked delta into one of a small set of explicit moves, recorded so downstream rituals (backlog, roadmap, release-readiness, Lead reporting) can consume the result without re-litigating the evidence. Per Big Idea #12 the moves are **Advance, Refine, Kill, Scope-differently / Pivot, Reprioritize.** Per the Ray spec there are two non-negotiables: **no decision without a signal reference**, and **the tradeoff must be explicit.** The three outcomes Decisions creates: **Closure** (the Initiative is resolved, not drifting), **Direction** (the next concrete move is named with the tradeoff stated), and **Continuity** (the Decision record travels and seeds — or kills — the next Initiative).

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — the drafted "Glare | Focus, Decisions v0.1" block: the 5 decision-move taxonomy, the criteria-by-delta table, the Decision Record template (initiative / method / signal ref / move / rationale / tradeoff / next initiative / hand-off / owner+date), the hand-off rituals per move, and the worked Mobile Checkout v2 Refine example. Note: this is drafted from framework knowledge, not from an authoritative Drive source — flag that to the user when they ask where the rules come from.

## How to apply

1. **Require a signal reference as the entry condition.** No decision without a benchmarked Comparing delta on the table. If the user is making a call from opinion or unbenchmarked data, route them back to `glare-focus-comparing` first. (This is the Ray spec guardrail.)

2. **Pick exactly one of the 5 moves and name it out loud.** **Advance / Refine / Kill / Scope-differently (Pivot) / Reprioritize.** "Let's keep going" is not a move. Use the criteria-by-delta table:
   - **Advance** — Δ ≥ target on primary metric; secondary metric not regressed past kill threshold.
   - **Refine** — 0 < Δ < target; trend in right direction; one more cycle is affordable.
   - **Kill** — Δ inside the kill window after ≥2 cycles, OR a secondary regressed past kill threshold.
   - **Scope-differently / Pivot** — Δ flat or wrong-direction AND framing was wrong; reframed Initiative drafted before the Pivot is final.
   - **Reprioritize** — capacity constraint dominates; park, don't kill.

3. **Articulate the tradeoff explicitly.** State what is being given up by choosing this move; name what is now locked vs flexible. (Ray spec guardrail #2.) Vague rationale equals stalled decisions.

4. **Tie the Decision back to the originating Initiative.** Report whether the Initiative's outcome was achieved, partially achieved, or missed. If Pivot/Kill, draft the next Initiative record (loop back to `glare-focus-initiatives`) and close the original with a pointer.

5. **Write the Decision record.** Tight: initiative ref, method version, signal ref (metric | baseline | current | Δ), move, 1–3 sentence rationale, tradeoff, next initiative (or "none"), hand-off route, owner + date. The record is the artifact; meetings without one stall.

6. **Route to the right hand-off ritual:** Advance → release-readiness review (+ Lead reporting); Refine → backlog grooming; Kill → roadmap review (the receipt that prevents zombie return); Pivot → Initiatives intake (new record spawned); Reprioritize → roadmap review (parked with state preserved).

## Handoffs

- When a Decision opens a new initiative (Pivot, Kill-and-reframe, next-round Advance), loop back to `glare-focus-initiatives`.
- When the next initiative needs a revised collection plan (new instruments, cadence, audience recipe, or a bridge round), suggest `glare-focus-methods`.
- When the team wants to re-run the benchmark delta against a new baseline, suggest `glare-focus-comparing`.
- When an Advance or major Refine needs to be reported up in business-KPI / ROI terms, hand off to `glare-lead`.
- For multi-block Focus questions, hand back to `glare-focus`.
