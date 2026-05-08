---
name: glare-review-coach
description: Use this skill when the user wants to prepare for an upcoming design review or client call, OR coach someone on behavioral improvements after one. Triggers include "prep me for a kickoff," "prep for a design review," "build a call brief," "what should I focus on for this call," "we have past SIGNAL scores — what do we improve," "coach this team member," "how do I get better at [Surface/Identify/Ground/Navigate/Align/Lock]," "give me a practice script for stating recommendations," or "we keep losing on Lock — what do we do." Also use when the user wants to look at patterns across multiple calls and turn them into focused coaching. Do NOT use when the user wants to evaluate or score a specific transcript — use `glare-review-rubric`. Do NOT use for in-the-moment techniques mid-review — use `glare-review-techniques` or the dimension skills.
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

Prepare for design reviews and coach on specific behavioral improvements. This is the companion to `glare-review-rubric` — the rubric tells you what happened, the coach helps you change what happens next.

## Read the reference first

- `reference.md` — full content (two modes, call brief template, call type playbooks, prep from past scores, coaching brief template, per-dimension coaching with failure modes / drills / success signals, pattern recognition across calls).

## Two modes

### Mode 1: Pre-Call Prep
Use before a call to build a game plan. Produces a focused brief — not a script.

### Mode 2: Post-Call Coaching
Use after running the SIGNAL rubric. Takes the scores and behavioral metrics and turns them into specific behavioral changes.

## How to apply (Mode 1: Pre-Call Prep)

1. **Gather inputs:** Client/audience name and context, call purpose, optional past SIGNAL scores or known weak dimensions, optional specific concerns.

2. **Pick the right call type playbook** (full table in `reference.md`):
   - Kickoff → emphasize S, I
   - Design Review → emphasize G, N
   - Decision Meeting → emphasize N, A, L
   - Check-in / Status → emphasize S, L
   - Stakeholder Presentation → emphasize G, N
   - Scope Discussion → emphasize I, A

3. **Produce the call brief** (template in `reference.md`): Objective, SIGNAL Focus, Opening Move, Key Questions to Surface Tension, Decision Point, Signals to Reference, Ownership Checkpoint, Lock Script, Watch For.

4. **If past SIGNAL scores are available**, address the weakest dimensions specifically (e.g., Low N → script the recommendation in advance: "Based on X, we recommend Y. Should we proceed?").

## How to apply (Mode 2: Post-Call Coaching)

1. **Inputs:** SIGNAL rubric evaluation (scores + narrative), optional team member focus, optional past coaching notes.

2. **Pick the primary gap** — not just the lowest score, but the one that would most improve outcomes if fixed. Usually the first weak letter in the SIGNAL flow.

3. **Produce the coaching brief** (template in `reference.md`): Score Summary, What Worked (keep doing), Primary Gap, Behavioral Drill (pattern + why it matters + the fix + practice script + success signal), Secondary Gaps, Next Call Focus.

4. **Use the per-dimension coaching content** in `reference.md` for failure modes, behavioral drills, and success signals for each letter.

5. **One gap per coaching session.** Don't overwhelm. Scripts should feel natural, not robotic. Use the person's own quotes from the transcript, not generic examples.

## Pattern recognition

When coaching the same person over time, watch for recurring patterns (full table in `reference.md`):
- Consistently low S, high G → leading with data instead of story
- Consistently low N → confidence issue, not knowledge
- High S, low I → surfaces problems but doesn't define success
- Low L across all calls → build a closing ritual
- Scores improving but client behavior unchanged → shift focus from team behavior to engagement strategy

## Notes

- Coaching is about behavior change, not knowledge. Don't explain what SIGNAL means — practice what it looks like.
- The best coaching evidence comes from the person's own calls — always use their quotes.
- Track coaching focus across calls. If the same gap persists after 3 calls, the coaching approach needs to change, not just the person.

## Handoffs

- The actual evaluation that produces scores → `glare-review-rubric`
- Per-dimension techniques to practice → `glare-review-surface`, `glare-review-identify`, `glare-review-ground`, `glare-review-navigate`, `glare-review-align`, `glare-review-lock`
- Just the score scale + bands → `glare-review-scoring-model`
- The end-to-end transcript workflow → `glare-review-run-transcript`
- Where coaching fits in Design Review → `glare-design-review`
