---
name: assessment-reading
description: Use this skill when the user wants to interpret the *shape* of their Design Assessment results across dimensions — "what does our pattern mean," "how do I read these scores together," "we're balanced but low," "we're strong on proof but weak on influence," "we have a strong start, weak finish," "high activity, low impact," "what pattern do we have," or asks how multiple dimension scores work together. Also use when the user describes a specific shape — uneven scores, one strong dimension carrying the others, weak link creating drag — or names a common pattern like "balanced and strong," "weak start strong finish," "strong proof weak influence," "strong decisions weak proof," "strong organization weak complexity," "local strength limited scale." Do NOT use when the user wants to understand how scores are *built* (`glare:assessment-scoring`), is choosing a 30-day next move (`glare:assessment-using-results`), or is in one specific dimension — drop into those instead.
version: 3.1.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user **read the pattern** across their five Design Assessment scores — what the shape reveals about how design impact is moving (or not moving) through the organization.

## Core idea

The pattern matters more than any single score. A score shows where something is strong or weak. A pattern shows how design impact moves, slows, or breaks across the organization. Reading Patterns helps teams understand what the scores mean *as a system*.

A low score does not automatically mean "fix this first." The real question is how that low score affects the rest of the system. Strong Building Proof with weak Guiding Decisions means evidence exists but isn't shaping choices. Strong Organizing Work with weak Scaling Influence means knowledge is captured but proof isn't traveling. The score shows the parts. The pattern shows the flow.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of the Reading Patterns page: why patterns matter, what they reveal, the nine common pattern types (with what each suggests and what to risk), how to read your own pattern, and how patterns guide action.

## How to apply

1. **Confirm pattern reading is the right entry.** If the user is staring at one score and asking what it means, route to `glare:assessment-scoring`. If they already know what they want to fix and need a 30-day move, route to `glare:assessment-using-results`. Reading Patterns is for the "what does the *shape* mean" moment.

2. **Get all five scores before naming a pattern.** Don't accept one or two — the whole story comes from how they relate. If the user has only some scores, ask for the rest, or explicitly mark the pattern read as partial.

3. **Match symptoms to pattern types** when the user describes what's happening:
   - All scores in a similar range, all decent → Balanced and strong
   - All scores in a similar range, all low → Balanced but low
   - Early dimensions strong, later ones weak → Strong start, weak finish
   - Later dimensions stronger than earlier ones → Weak start, strong finish
   - High Building Proof, low Scaling Influence → Strong proof, weak influence
   - High Guiding Decisions, low Building Proof → Strong decisions, weak proof
   - High Organizing Work, low Managing Complexity → Strong organization, weak complexity
   - Lots of activity, mid-range scores, low Proof or Influence → High activity, low impact
   - Uneven scores, inconsistent responses → Local strength, limited scale

4. **Don't only chase the lowest number.** Ask: which break in the system is affecting the most other dimensions? A weak link that creates drag elsewhere matters more than an isolated low score.

5. **Treat patterns as a current read, not a label.** Patterns can change as teams improve. Never use a pattern to blame a team or person. The pattern shows where the system needs support.

6. **End every read with a transition to action.** Reading Patterns is the diagnosis. Once the pattern is named, hand off to `glare:assessment-using-results` to choose the 30-day move.

## Handoffs

- The broader assessment overview → `glare:design-assessment`
- How the scores are built and what each band means → `glare:assessment-scoring`
- Choosing one 30-day improvement based on the pattern → `glare:assessment-using-results`
- Going deeper on a specific dimension once the pattern points to it → `glare:assessment-organizing-work`, `glare:assessment-managing-complexity`, `glare:assessment-building-proof`, `glare:assessment-guiding-decisions`, `glare:assessment-scaling-influence`
