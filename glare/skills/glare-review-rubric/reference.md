# SIGNAL Call Rubric — Reference

Compressed source: Glare | Design Review, Signal Call Rubric V1.3 + Glare | Prompt: Design Review v1.3 + Glare | Skill: Design Review v1.3.

## SIGNAL framework

**Surface → Identify → Ground → Navigate → Align → Lock**

Decision cycle: **Tension → Clarity → Evidence → Commitment → Responsibility → Momentum**

Each dimension builds on the previous. When a call stalls, it's almost always because an earlier dimension was skipped or undercooked.

## Inputs

- Speaker-attributed transcript
- Optional speaker tagging — "us" (team) vs "client" / stakeholder

If transcript is under ~500 words OR one-sided OR speakers aren't tagged, handle per "Common Issues" below.

## Dimension rubrics

### S — Surface Challenges

**Intent:** Expose the real tension behind the request.
**Why it matters:** Most requests are symptoms, not root problems. If we optimize the surface, we create polished irrelevance.
**Evaluate:** Did we move beyond the stated request? Did we clarify consequences of inaction? Was measurable cost articulated? Did the room acknowledge the tension?

| Score | Description |
|---|---|
| 5 | Clear pain and consequence surfaced |
| 4 | Tension identified, consequence partially quantified |
| 3 | Friction visible but soft — no consequence articulated |
| 2 | Surface-level acknowledgment, no depth |
| 1 | Feature-level conversation only |

*Metric hint: Problem Ownership.*

### I — Identify Outcomes

**Intent:** Define what "better" means in measurable terms.
**Why it matters:** Without clear outcomes, stakeholders critique artifacts instead of results.
**Evaluate:** Is the business objective explicit? Is the user need explicit? Are success criteria measurable? Is there shared agreement?

| Score | Description |
|---|---|
| 5 | Clear, measurable outcome agreed |
| 4 | Outcomes stated and mostly measurable, agreement implicit |
| 3 | Goals stated but vague |
| 2 | Outcomes mentioned but not defined |
| 1 | Deliverables dominate discussion |

### G — Ground in Signals

**Intent:** Anchor decisions in evidence instead of opinion.
**Why it matters:** Design signals reduce politics and increase credibility.
**Evaluate:** Did we reference measurable signals? Did we show baseline or delta? Did signals influence direction? Did we reduce subjective loops?

| Score | Description |
|---|---|
| 5 | Signals drove the conversation |
| 4 | Signals referenced and influenced key decisions |
| 3 | Some signal grounding |
| 2 | Signals mentioned but not used for decisions |
| 1 | Opinion-driven review |

*Metric hint: Reframe Adoption.*

### N — Navigate Decisions

**Intent:** Lead the decision process and secure commitment.
**Why it matters:** Direction without agreement creates rework. Decisions not secured in the room reopen later.
**Evaluate:** Did we provide a clear recommendation? Was it grounded in signal? Did the room verbally agree? Was the decision documented or confirmed?

| Score | Description |
|---|---|
| 5 | Clear recommendation and explicit agreement |
| 4 | Recommendation given, agreement mostly clear |
| 3 | Direction provided but commitment soft |
| 2 | Options presented without recommendation |
| 1 | Discussion without decision |

*Metric hint: Decision Language.*

### A — Align Ownership

**Intent:** Create clarity around responsibility and boundaries.
**Why it matters:** Ambiguity creates drift. Unclear ownership weakens accountability.
**Evaluate:** Is ownership of outcomes clear? Is decision authority clear? Did we reduce cross-team ambiguity? Did we prevent scope drift?

| Score | Description |
|---|---|
| 5 | Clear ownership and clean boundaries |
| 4 | Most ownership explicit, minor gaps |
| 3 | Partial clarity |
| 2 | Some ownership discussed, not confirmed |
| 1 | Ambiguity persists |

### L — Lock Momentum

**Intent:** Convert insight into forward motion.
**Why it matters:** Momentum compounds influence. Meetings that end without next steps lose value.
**Evaluate:** Did we restate business impact? Were next steps specific? Were owner and timeline defined? Did the room confirm alignment?

| Score | Description |
|---|---|
| 5 | Impact and next steps locked |
| 4 | Next steps defined with owners, timeline soft |
| 3 | Next steps soft |
| 2 | Vague follow-up mentioned |
| 1 | Call ended without commitment |

## Score bands (total /30)

| Range | Band | Meaning |
|---|---|---|
| 25–30 | Leading | Exceptional across all dimensions |
| 19–24 | Advancing | Strong overall, approaching leading on most dimensions |
| 13–18 | Functional | Adequate, clear gaps in some areas |
| 6–12 | Reactive | Below expectations, significant improvement needed |

## Behavioral metrics

Diagnostic — not scored. Explain *why* dimensions scored the way they did.

### Talk Time Ratio
Word count split between team and client speakers, expressed as percentages.

### Problem Ownership (client only)
Count of moments where the client/stakeholder uses language indicating they own/internalize problems ("our issue is…", "we're struggling with…", "the challenge we face…").
- High: openly acknowledges and owns problems
- Medium: some ownership but hedging
- Low: deflection or blame-shifting

Include count, 2–3 example quotes, level, and 1–2 sentence interpretation.

### Decision Language (client only)
Count of moments where the client uses decisive language ("let's go with…", "we should…", "I want to…", "we've decided…").

Characterize tone: collaborative / hesitant / directive.

Include count, 2–3 example quotes, tone, and 1–2 sentence interpretation.

### Reframe Adoption
Number of times team reframes a problem vs. number of times client adopts/builds on that reframe. Rate = client adoptions ÷ team reframes. List each specific reframe and whether the client adopted it. Include 1–2 sentence interpretation.

## Output structure

### 1. Summary

```
**Total Score:** X/30 — [Leading | Advancing | Functional | Reactive]
**Call Pattern:** [Directional label, e.g. "Strong Signal Grounding, Weak Decision Locking"]

[2–3 sentence overall summary]

**SIGNAL Flow:** [1–2 sentences on how the call progressed and where it broke down]

**What Went Well**
- ...

**Areas for Improvement**
- ...

**Primary Improvement:** [The single most important thing to change for the next call]
```

### 2. Dimension evaluations (for each S → I → G → N → A → L)

```markdown
## S — Surface Challenges (X/5)

[1–2 summary sentences — no heading, just prose]

### Key Observations

**1. [Bold title]**

> "[Verbatim quote from transcript]"
> — Speaker Name

**2. [Bold title]**

> "[Verbatim quote]"
> — Speaker Name

### Why this isn't a 5

- [Specific concrete gap]
- [Specific concrete gap]
```

Rules:
- 2–4 key observations per dimension
- Each observation: bold title + verbatim blockquote with real speaker name
- NO description paragraphs or takeaway sentences after quotes — title and quote are the entire item
- Include both what went RIGHT and what went WRONG
- Close with "Why this isn't a 5" (or "Why this is a [score]" for scores below 3)
- Bullet points only in the closing — no summary paragraph after

### 3. Behavioral Metrics

```
### Talk Time Ratio
- [Speaker] (team): X% (X words)
- [Speaker] (client): X% (X words)

### Problem Ownership (client only)
- Count: X instances
- Level: High / Medium / Low
- Examples:
  - "..."
  - "..."
- Interpretation: [1–2 sentences]

### Decision Language (client only)
- Count: X instances
- Tone: collaborative / hesitant / directive
- Examples:
  - "..."
- Interpretation: [1–2 sentences]

### Reframe Adoption
- Team Reframes: X
- Client Adoptions: X
- Adoption Rate: X%
- Reframes:
  - ✓ [Adopted reframe — short description]
  - ✗ [Not adopted reframe — short description]
- Interpretation: [1–2 sentences]
```

### 4. Strengths
2–4 specific things the call did well that should be repeated.

### 5. Improvement Areas
2–4 specific, actionable improvements.

### 6. Primary Improvement
The single most important thing to change for the next call.

### 7. Automation Opportunities
3 specific moments or patterns from the call that could be automated with Glare Blocks:

```
1.
- Friction Observed: [What was inefficient]
- Automation Idea: [Concrete tool or automation]
- Glare Block: [Define | Measure | Focus | Lead] — [Subcategory]
- Impact: [Why it matters]

2. [Same structure]

3. [Same structure]
```

## Scoring calibration

- **3 is the most common score.** Reserve 5 for truly exceptional and 1 for clear failures.
- Score each dimension **independently** — don't let one bleed into another.
- A 4 means "almost leading, one specific gap prevents a 5" — name the gap.
- A 2 means "something was attempted but fell short" — name what was attempted.
- Every claim anchored to a direct quote. No paraphrasing.
- If no quote supports a dimension: "No direct evidence found in transcript."

## Critical rules

### Evidence
- Every dimension MUST include at least one direct quote.
- 1–3 quotes per dimension max — strongest evidence first.
- Do not invent or paraphrase quotes. Use exact language.
- Blockquote attribution MUST use a real speaker name. Never use "Speaker" or "Transcript Extract."

### Narrative
- Open each dimension with 1–2 prose sentences (no heading).
- Each Key Observation = bold numbered title + verbatim blockquote with attribution. No description paragraph after.
- Include both what went RIGHT and what went WRONG.
- Typically 2–4 observations per dimension.
- Close each dimension with "Why this isn't a 5" (or "Why this is a [score]" for scores below 3). Bullet points only.

### Analysis
- Quotes anchor insights, they don't decorate them.
- Tie every claim to something said on the call.
- Focus on cause-and-effect: *what happened → why it matters*.
- Be concise but sharp.

### Tone
- The goal is not to evaluate the call. The goal is to improve how the next call is run.

## Common issues

- **Transcript too short** (<~500 words): Provide observations without numeric scores.
- **Speakers not identified**: Ask before guessing. Misattribution breaks behavioral metrics.
- **One-sided transcript**: Note this limitation. Score what's observable but flag gaps.
- **No decisions were made**: This is itself a finding — score N and L accordingly and call out why.
