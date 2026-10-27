# SIGNAL Call Coach — Reference

Compressed source: signal-call-coach (existing standalone skill, refreshed for Glare v1.3) + per-dimension coaching from each Design Review v1.3 dimension doc.

## Two modes

- **Mode 1: Pre-Call Prep** — build a focused brief before a call.
- **Mode 2: Post-Call Coaching** — turn rubric scores into behavioral change.

## When to use

- When the user wants to prepare for an upcoming design review or client call (pre-call prep mode).
- When coaching someone on behavioral improvements after a call (post-call coaching mode).
- When building a call brief or game plan.
- When the user has past SIGNAL scores and wants to know what to improve.
- When asking "how do I get better at [Surface/Identify/Ground/Navigate/Align/Lock]" or wanting a practice script.
- When looking at patterns across multiple calls to turn into focused coaching.

**Don't use when** the user wants to evaluate or score a specific transcript — use `glare:review-rubric`. For in-the-moment techniques mid-review, use `glare:review-techniques` or the dimension skills.

## Mode 1: Pre-Call Prep

### Inputs

- Client/audience name and context
- Call purpose (kickoff, review, decision meeting, check-in, etc.)
- Optional: past SIGNAL scores or known weak dimensions
- Optional: specific concerns or goals ("they tend to defer decisions," "we need to lock scope")

### Call brief template

```markdown
## Call Brief: [Audience] — [Date]

### Objective
[One sentence: what does success look like for this call?]

### SIGNAL Focus
[Which 1–2 SIGNAL dimensions matter most for this call type, and why]

### Opening Move
[How to open the call to set the right frame — specific language, not generic advice]

### Key Questions to Surface Tension
- [Question targeting the real problem behind the stated agenda]
- [Question that forces consequence articulation]
- [Question that tests whether outcomes are clear]

### Decision Point
[What decision should be made on this call? Frame as: "By the end of this call, we should have agreement on ___"]

### Signals to Reference
[What data, metrics, baselines, or prior findings should be brought into the conversation?]

### Ownership Checkpoint
[Who needs to own what coming out of this call? Name specific people and responsibilities]

### Lock Script
[Exact closing language to lock momentum — restate impact, confirm next steps, assign owners, set timeline]

### Watch For
- [Behavioral pattern to watch for based on history]
- [Common derailer for this call type]
- [Signal that the call is going off track]
```

### Call type playbooks

| Call Type | Primary Dimensions | Coach Focus |
|---|---|---|
| Kickoff | S, I | Surface real tension early. Don't let it stay in logistics. Define measurable outcomes before leaving the room. |
| Design Review | G, N | Ground feedback in signals, not opinion. Navigate to a decision — don't end with "we'll think about it." |
| Decision Meeting | N, A, L | Come with a recommendation. Make trade-offs explicit. Lock the decision with clear ownership. |
| Check-in / Status | S, L | Use the check-in to resurface tension that may have drifted. Lock next steps — don't let it be purely informational. |
| Stakeholder Presentation | G, N | Lead with signal. Make the recommendation clear. Secure explicit agreement, not just nodding. |
| Scope Discussion | I, A | Clarify outcomes before discussing scope. Align ownership to prevent creep. |

### Prep from past scores

- **Low S (1–2):** Plan specific tension-surfacing questions. Prepare a "what happens if nothing changes" framing.
- **Low I (1–2):** Write the outcome statement in advance. Bring it to the call and confirm it explicitly.
- **Low G (1–2):** Prepare 2–3 specific signals with baselines/benchmarks. Reference them early.
- **Low N (1–2):** Prepare a clear recommendation with rationale. Script the ask: "Based on X, we recommend Y. Should we proceed?"
- **Low A (1–2):** Prepare an ownership map. Ask "who makes the final call on this?" early.
- **Low L (1–2):** Prepare closing language in advance. Include specific dates, owners, and confirmation asks.

## Mode 2: Post-Call Coaching

### Inputs

- SIGNAL rubric evaluation (scores + narrative)
- Optional: which team member to focus coaching on
- Optional: past coaching notes or patterns

### Coaching brief template

```markdown
## Coaching Brief: [Call] — [Date]

### Score Summary
[Total /30, band, pattern headline from rubric]

### What Worked — Keep Doing This
[2–3 specific behaviors from the call that should be repeated, with quotes as evidence]

### Primary Gap
[The single biggest behavioral gap — not just the lowest score, but the one that would most improve outcomes if fixed]

### Behavioral Drill: [Gap Name]

**The Pattern:** [What happened on the call — specific moment, with quote]
**Why It Matters:** [Consequence of this pattern continuing]
**The Fix:** [Specific behavioral change — concrete language and timing]
**Practice Script:** [2–3 example phrases to use in the next call]
**Success Signal:** [How to know the behavior change is working — what the client will say or do differently]

### Secondary Gaps
[1–2 additional gaps with lighter treatment — pattern, fix, practice script]

### Next Call Focus
[Based on this coaching, what 1–2 things should they focus on in the next call?]
```

## Coaching by dimension

### S — Surface Challenges

**Common failure modes:**
- Accepting the stated request at face value
- Moving to solutions before understanding the problem
- Letting the client/PM set the frame instead of reframing

**Behavioral drills:**
- "Before we talk about what to build, help me understand what's not working today."
- "What happens if we don't address this in the next 90 days?"
- "When you say [their word], what does that actually look like?"

**Success signal:** Someone in the room articulates consequence or cost unprompted.

### I — Identify Outcomes

**Common failure modes:**
- Discussing deliverables instead of outcomes
- Accepting vague goals ("improve the experience")
- Not separating user outcome from business outcome

**Behavioral drills:**
- "What would success look like in 6 months — what number changes?"
- "If we do this perfectly, what happens for your users? And what happens for the business?"
- "Let me play that back: the outcome we're targeting is ___. Is that right?"

**Success signal:** Someone confirms a measurable outcome in their own words.

### G — Ground in Signals

**Common failure modes:**
- Debating preferences instead of referencing data
- Having signal data but not introducing it
- Letting stakeholder opinion override evidence

**Behavioral drills:**
- "The signal shows ___. That means ___."
- "Before we decide based on preference, let's look at what the data says."
- "The benchmark for this is ___. We're currently at ___. The gap is ___."

**Success signal:** Someone references the signal data in their own reasoning.

### N — Navigate Decisions

**Common failure modes:**
- Presenting options without a recommendation
- Not asking explicitly for agreement
- Letting "we'll think about it" stand as an outcome

**Behavioral drills:**
- "Based on [signal], we recommend [option] because [reason]. Should we proceed?"
- "The trade-off is ___. Given your priorities, we'd suggest ___."
- "I want to make sure we leave with a decision on this. Are we aligned on ___?"

**Success signal:** Someone uses commitment language ("let's do that," "yes, proceed," "agreed").

### A — Align Ownership

**Common failure modes:**
- Vague responsibility ("the team will handle it")
- Not identifying decision authority
- Scope creeping because boundaries aren't set

**Behavioral drills:**
- "Who on your side is the final decision-maker for ___?"
- "Let me clarify the split: we own ___, you own ___. Does that match your understanding?"
- "If new requirements come up, how should we handle scope changes?"

**Success signal:** Someone names specific people for specific responsibilities.

### L — Lock Momentum

**Common failure modes:**
- Ending without restating impact
- Vague next steps ("we'll follow up")
- No timeline or owner on actions

**Behavioral drills:**
- "Before we wrap — the business impact here is ___. The next step is ___, owned by ___, by [date]."
- "Let me confirm what we agreed to: [list]. Did I miss anything?"
- "Can we lock [date] for the next session? I'll send a calendar invite with the agenda."

**Success signal:** Someone confirms next steps with specifics, not "sounds good."

## Pattern recognition across calls

| Pattern | What it means | Coaching response |
|---|---|---|
| Consistently low S, high G | Good at evidence, bad at framing tension | Leading with data instead of story. Surface the "so what" before the signal. |
| Consistently low N | Avoids pushing for commitment | Usually a confidence issue, not a knowledge gap. Script the recommendation in advance, practice saying it. |
| High S, low I | Surfaces problems but doesn't define success | Good instinct, incomplete follow-through. Always translate tension into a measurable outcome before moving on. |
| Low L across all calls | Consistent weak close | Build a closing ritual: impact restate, next steps, owners, dates, confirmation. Practice until automatic. |
| Scores improving but metrics flat | Better team performance, client behavior unchanged | Shift focus from team behavior to client engagement strategy. |

## Notes

- Coaching is about behavior change, not knowledge. Don't explain what SIGNAL means — practice what it looks like.
- One gap per coaching session. Don't overwhelm.
- Scripts should feel natural, not robotic. Adapt language to the person's style.
- The best coaching evidence comes from the person's own calls — always use their quotes.
- Track coaching focus across calls to measure improvement. If the same gap persists after 3 calls, the coaching approach needs to change, not just the person.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Coaching script as performance.** Treating the call brief as lines to deliver. The brief is a *plan* — a small set of moves to land — not a script to read.
- **Prepping every dimension equally.** Pre-call prep that lists 6 things to do is unusable in the moment. Pick the 1–2 dimensions most at risk for this call and rehearse those.
- **Post-call coaching without the rubric.** Trying to coach behavioral change without a scored transcript produces generic advice. The rubric tells you what happened; the coach uses it.
- **Skipping pattern recognition across calls.** Coaching one call in isolation when the same Lock weakness has shown up in five reviews. Look at the trend before naming the coaching focus.

