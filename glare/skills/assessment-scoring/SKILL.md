---
name: assessment-scoring
description: Use this skill when the user is asking about how the Design Assessment is scored or measured — "how does the assessment work," "what do the score bands mean," "what's a good design assessment score," "what's Reactive vs Developing vs Functional vs Strong vs Leading," "how are dimension scores calculated," "how do survey responses become scores," "what does our 75 mean," or wants to understand the structure (dimensions, layers, score ranges) before taking or reviewing the assessment. Also use when the user asks why each dimension has its own score, what behavior creates a score, what the assessment does NOT measure (individual designer skill), or how layered scoring helps explain *why* a dimension is strong or weak. Do NOT use when the user is interpreting the shape across dimensions (`glare:assessment-reading`), choosing what to do next (`glare:assessment-using-results`), or already deep in one dimension's content — drop into those instead.
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user understand the **scoring model** behind the Design Assessment — how scores are built, what each band means, and how to read a single dimension score.

## Core idea

The score is not the point. The Design Assessment uses scoring to **make patterns easier to see**. It helps teams understand where design impact is strong, where it breaks down, and where improvement will create the most movement.

Each of the five dimensions (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence) gets its own score on a 0–100 scale, mapped to five bands: **Reactive (0–40), Developing (41–60), Functional (61–80), Strong (81–90), Leading (91–100)**. Each dimension is broken into layers, so the score doesn't just say "this is weak" — it shows *which part* is weak.

The score measures the system, not the people. A low score does not mean the designers are bad. It means a part of the system around the work needs more support.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Scoring Model and How It's Measured pages: why scoring matters, what the score measures, how survey responses become scores, the five score bands, the layers inside each dimension, what the measurement reveals, and what it does *not* measure.

## How to apply

1. **Confirm scoring is the right entry.** If the user is staring at a score and asking "what now," route to `glare:assessment-using-results`. If they're trying to read the *shape* across dimensions, route to `glare:assessment-reading`. Scoring is for understanding *what the number means* and *how it was built*.

2. **Default opener for "how does scoring work":** five dimensions, each scored 0–100, mapped to five bands. The score reflects how people describe the actual system of work — not how the team hopes the process works. Each dimension is layered, so the score points to *where* the issue lives.

3. **Use the bands honestly:**
   - **0–40 Reactive** → impact hard to trace, system mostly informal, decisions rely on memory/meetings/individual effort. Needs a clearer foundation before scaling.
   - **41–60 Developing** → some practices exist, inconsistent. Pockets of strong work depending on specific people. Needs more consistency.
   - **61–80 Functional** → working system. Evidence used, decisions clearer, gaps remain. Tighten the weakest parts.
   - **81–90 Strong** → impact visible and repeatable. Leaders understand the value. Ready to scale what's working.
   - **91–100 Leading** → design is part of the organization's decision system. Evidence shapes priorities, reduces risk, guides investment.

4. **Always say: "the score helps start the conversation, the pattern shows what to do."** Two teams can both score 75 and have very different problems. One score per dimension is a beginning, not an answer.

5. **Read each dimension score in two ways.** First on its own (what does this number say about this dimension). Then against the others (is this dimension helping or hurting the system; is it strong enough to support the next dimension).

6. **Resist gaming the score.** A low score is not always the place to start. The best place to start is usually the dimension where improvement creates the most movement across the system.

## Handoffs

- The broader assessment overview → `glare:design-assessment`
- Each dimension's content and what the score reflects → `glare:assessment-organizing-work`, `glare:assessment-managing-complexity`, `glare:assessment-building-proof`, `glare:assessment-guiding-decisions`, `glare:assessment-scaling-influence`
- Reading the *shape* across all five dimensions → `glare:assessment-reading`
- Turning the result into one focused next move → `glare:assessment-using-results`
