---
name: glare-design-assessment
description: Use this skill when the user asks about Design Assessment as a top-level concept — "what's our team's design maturity," "score our org," "where is design impact breaking down," "how do I run a design assessment," "what are the five dimensions," or wants the overview (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence; plus Scoring Model, Reading Patterns, Using Results). Also for symptoms — "research never gets used," "leadership doesn't see our value," "design proof stays trapped" — or a system-level diagnostic, not a single-project review. Do NOT use when deep in one dimension (`glare-assessment-organizing-work`, `glare-assessment-managing-complexity`, `glare-assessment-building-proof`, `glare-assessment-guiding-decisions`, `glare-assessment-scaling-influence`), interpreting a score (`glare-assessment-scoring`, `glare-assessment-reading`), or planning improvement (`glare-assessment-using-results`).
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user understand and use **Design Assessment** — the Glare section that measures how well design impact moves through an organization, across five dimensions.

## Core idea

Design work rarely fails all at once. It loses strength as it moves. An idea starts with promise, gets explored, debated, refined, pushed forward — and somewhere along the way clarity fades, proof gets harder to explain, decisions slow down. The work keeps going, but momentum drops.

The Design Assessment surfaces *where* that breakdown happens. It looks beyond outputs at the system around the work: how learning gets captured, how complexity is handled, how proof gets built, how decisions get made, how evidence travels. Five dimensions, each scored on its own, together revealing the shape of how design impact moves — or stops moving — inside the organization.

The score matters, but the pattern matters more. Two teams can both score 75 and have very different problems.

## Read the reference first

Before answering substantive questions, read:

- `reference.md` — full compressed content of the Design Assessment overview: what the assessment is, what it measures (and what it does not), the five dimensions and what each one shows, how the assessment works as a system, what teams get from it, and how to use the results.

## How to apply

1. **Diagnose the user's entry point.** Are they (a) brand-new to the assessment and want a one-paragraph pitch, (b) about to take it and want to understand the structure, (c) staring at a result and trying to interpret it, (d) sure which dimension is broken and want to go deep, or (e) trying to choose what to improve first? Route accordingly — don't dump all five dimensions if they only need one.

2. **Default opener for "what is the Design Assessment":** the five dimensions in one breath — Organizing Work (does learning compound or get lost), Managing Complexity (does growing work stay clear or get tangled), Building Proof (does design connect to results or stay trapped), Guiding Decisions (do signals create direction or get lost in debate), Scaling Influence (does proof travel or stay local). Then: each is scored separately on a 0–100 band; the pattern across all five is the real story.

3. **Frame the assessment as system diagnosis, not performance review.** The score does not judge designers. It measures the system around the work. A low score means a part of the system needs more support, not that the team is failing.

4. **When the user names a symptom**, map it to the dimension and hand off:
   - "Findings keep getting lost" / "Every project starts from scratch" → Organizing Work
   - "Big initiatives keep getting tangled" / "Dependencies surprise us" → Managing Complexity
   - "Leaders don't see our value" / "We can't show what changed" → Building Proof
   - "We keep relitigating the same decisions" / "Reviews end without commitment" → Guiding Decisions
   - "Our proof stays local" / "Strategy forms without our evidence" → Scaling Influence

5. **Push toward the smallest-leverage next move.** Never recommend chasing a perfect score or fixing all five at once. Ask: which dimension, if it improved, would unlock movement across the others? That is where to start. One visible improvement in 30 days beats a transformation plan.

6. **Resist over-explaining the framework.** The assessment is meant to change what the team does next. If the user has results in front of them, route them into Reading Patterns and Using Results — not into more theory.

## Critical rules

- **The pattern matters more than the score** — two teams can both score 75 and have very different problems; never lead with the number alone.
- **Assessment is system diagnosis, not performance review** — the score measures the system around the work, not designers; a low dimension means the system needs more support, not that anyone is failing.
- **Never chase a perfect score or fix all five at once** — recommend one smallest-leverage move: which dimension, if it improved, would unlock the others; one visible win in 30 days beats a transformation plan.
- **Map symptoms to dimensions before routing** — "findings keep getting lost" → Organizing Work, "leaders don't see our value" → Building Proof, "we relitigate decisions" → Guiding Decisions, "proof stays local" → Scaling Influence, "initiatives tangle" → Managing Complexity.
- **If results are in front of the user, route to Reading Patterns or Using Results** — not into more theory; the assessment exists to change the next move.

## Handoffs

- The five dimensions in detail → `glare-assessment-organizing-work`, `glare-assessment-managing-complexity`, `glare-assessment-building-proof`, `glare-assessment-guiding-decisions`, `glare-assessment-scaling-influence`
- How the score is built and what each band (Reactive / Developing / Functional / Strong / Leading) means → `glare-assessment-scoring`
- Interpreting the shape of results across dimensions (balanced, uneven, strong-start-weak-finish, etc.) → `glare-assessment-reading`
- Turning results into one focused 30-day improvement → `glare-assessment-using-results`
- Where Design Assessment fits in the broader Glare framework → `glare-getting-started`
- Strengthening the underlying decision system that the assessment measures → `glare-decision-map`, `glare-design-signals`, `glare-design-review`
