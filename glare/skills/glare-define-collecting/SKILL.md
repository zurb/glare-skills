---
name: glare-define-collecting
description: Use this skill when the user is in the Collecting block of the Define area — turning raw input into usable signals. Triggers — picking a research mode (Exploratory / Evaluative / Comparative), the five-step process (Intent → Stack → Approach → Techniques → Connect), the 12 techniques grouped 5 ways (Navigation, Task, Comparison, Behavior, Feedback), named instruments (SUS, NPS, SEQ, CES, NASA-TLX, PURE, SUMI, WAMMI, UEQ, SUPR-Q, L-DERLY), the four feedback types (View / See / Sense / Hear), the five Design Stacks (Website, Mobile App, Product, E-commerce, Marketing), the Define → Capture → Connect cadence, the Collection Brief, Show Your Sources, agent operations runtime contract. Do NOT use when naming the underlying need (use `glare-define-user-needs`), defining who data comes from (use `glare-define-audience`), or picking metrics (use `glare-define-ux-metrics`). For broad Define, use `glare-define`; for the Decision Map, use `glare-decision-map`.
version: 3.5.0
source_doc_version: v1.2 (7-doc template — Overview + Techniques + Playbook + References + Decisions + Examples + Agent Operations)
last_rebuilt: 2026-05-26

sources:
  - doc_id: 1EVxEz0UXcGnRoHvb52Lk-7JMmnCLOKlCFFL9k6t7qrk
    title: Glare | Define, Collecting, Overview v1.2
    drive_url: https://docs.google.com/document/d/1EVxEz0UXcGnRoHvb52Lk-7JMmnCLOKlCFFL9k6t7qrk/edit
    last_synced: 2026-05-26
  - doc_id: 1aOi9vwu3nZe2Ri_4DAwQUHQp6RcmIb6R6v_T-t-Dm8c
    title: Glare | Define, Collecting, Techniques v1.2
    drive_url: https://docs.google.com/document/d/1aOi9vwu3nZe2Ri_4DAwQUHQp6RcmIb6R6v_T-t-Dm8c/edit
    last_synced: 2026-05-26
  - doc_id: 1LTpFv9_vtn82w3Jak0aOZWpQZwA3AQZVBHOld6q6wts
    title: Glare | Define, Collecting, Playbook v1.2
    drive_url: https://docs.google.com/document/d/1LTpFv9_vtn82w3Jak0aOZWpQZwA3AQZVBHOld6q6wts/edit
    last_synced: 2026-05-26
  - doc_id: 1y1EAqBw_HeoRRT4UrStJ1CRqw1ZKmHRS3DfVktxCPGI
    title: Glare | Define, Collecting, References v1.2
    drive_url: https://docs.google.com/document/d/1y1EAqBw_HeoRRT4UrStJ1CRqw1ZKmHRS3DfVktxCPGI/edit
    last_synced: 2026-05-26
  - doc_id: 11gGTw6Ya5SpyqVY8XPhe5UuGi6g_1touyfwV3VHz6RU
    title: Glare | Define, Collecting, Decisions v1.2
    drive_url: https://docs.google.com/document/d/11gGTw6Ya5SpyqVY8XPhe5UuGi6g_1touyfwV3VHz6RU/edit
    last_synced: 2026-05-26
  - doc_id: 1y2AGbaWxUHVcSlfLAlHvBCAfWKJH4NfNm8m7Js1Oo50
    title: Glare | Define, Collecting, Examples v1.2
    drive_url: https://docs.google.com/document/d/1y2AGbaWxUHVcSlfLAlHvBCAfWKJH4NfNm8m7Js1Oo50/edit
    last_synced: 2026-05-26
  - doc_id: 1l7zlfC-jU3f0vI2CXN5GrRNzU9-FtQoZitI9Sm_MtJ0
    title: Glare | Define, Collecting, Agent Operations v1.2
    drive_url: https://docs.google.com/document/d/1l7zlfC-jU3f0vI2CXN5GrRNzU9-FtQoZitI9Sm_MtJ0/edit
    last_synced: 2026-05-26
---

You are helping the user work the **Collecting** block of the Decision Map's **Define** area — the discipline that turns raw input into usable signals and prevents drift back into "loudest voice wins."

## Core idea

Collecting sits inside the Define area. User Needs names what users are trying to do. Audience defines who you are learning from. Collecting is the step that turns both into actual evidence — behavior observed, reactions captured, perceptions recorded.

The output of every Collecting workflow is a **Collection Brief** (14 fields) handed off to **Situations** (formerly Patterns; Bryan archived Patterns). Every effort follows the **Define → Capture → Connect** cadence and the **five-step workflow**: Start with Intent → Choose Your Stack → Identify the Approach → Apply the Techniques → Connect and Ready Your Data.

## Files to read

This skill ships two files alongside `SKILL.md`. Read in this order:

1. **`agent-operations.md` first.** Runtime contract for working with Collecting — required inputs per step, confidence thresholds, the 14-field Collection Brief output contract, routing logic, escalation triggers. Operating instructions, not reference content. The highest-leverage rules are duplicated into "Operating rules" below.
2. **`reference.md` second.** Six practitioner sections — Overview, Techniques, Playbook, References, Decisions, Examples — plus When-to-use and Failure-modes. Read for the 12 techniques (grouped 5 ways), the 11+ named instruments, the 4 tool categories, the 5 Design Stacks, and the 5 worked Examples (including the Near-Miss Pattern Library).

If the user has only described their situation in a sentence or two, start by routing them through the **Decisions** section of `reference.md` — match their situation to the Primary Routing Table.

## Operating rules

Binding rules from `agent-operations.md`. They apply on every invocation regardless of whether the full file is read.

### Required inputs per step

| To evaluate… | Need at minimum |
|---|---|
| **Intent (Step 1)** | Stated question, problem, or observation + a named user need OR business goal OR prior User Needs output. **If neither, route to User Needs.** |
| **Stack and Approach (Steps 2–3)** | Written hypothesis + named audience with source type (else route to Audience) + enough context to identify mode (Exploratory / Evaluative / Comparative) |
| **Technique and Tool (Step 4)** | Confirmed testable question (knowledge gap, observable evidence, decision-changing result) + named mode and stack + evidence of ≥2 feedback types |
| **Completed effort (Step 5)** | Named technique + tool + UX metrics + signal as metric result (not raw observation) + sources documented (technique, audience, metrics) + position on hypothesis (confirmed / refuted / open with next question) |

### Output Contract — The Collection Brief

Every Brief uses these 14 fields. Briefs below contract are **not handed off**.

| Field | From |
|---|---|
| User Need | User Needs block |
| Business Goal | Step 1 |
| Hypothesis | Step 1 |
| Audience (with source type + credibility level) | Audience block |
| Mode (Exploratory / Evaluative / Comparative) | Step 2 |
| Stack (Research or Design) | Step 2 |
| Approach (Exploring / Evaluating / Comparing) | Step 3 |
| Technique(s) + sample size | Step 4 |
| Tool(s) | Step 4 |
| UX Metrics | Step 4 |
| Feedback Types (≥2 of View / See / Sense / Hear) | Step 4 |
| Sharing Level (project / cross-team / leadership) | Step 5 |
| Signal Produced (as UX metric result, not raw observation) | Step 5 |
| Hypothesis Resolved? (confirmed / refuted / open + next question) | Step 5 |

### Confidence and routing

| Confidence | Conditions | Skill behavior |
|---|---|---|
| **High** | All 14 Brief fields present, sequence followed, signal expressed as metric result | Hand off to **Situations** |
| **Medium** | Hypothesis testability uncertain, audience credibility ≤ Medium, mode named but stack/approach unclear, metrics not connected, only one feedback type | Partial Brief with named gaps. **Does not route to Situations.** Holds until gap is resolved |
| **Low** | No hypothesis writable, no user need identifiable, no audience defined, sources missing on a completed study | Stops. Escalates with specific statement of what's missing |

### Routing rules

| Condition | Route to |
|---|---|
| Complete Brief at High confidence | **Situations** (formerly Patterns) |
| No user need or business goal in inputs | **User Needs** |
| Audience absent or credibility insufficient | **Audience** |
| Question not testable (too broad, not observable) | **Step 3** — rewrite |
| Only one feedback type present | **Step 4** — add second technique from different type |
| Completed study with sources missing | **Step 5** — document technique, audience, metrics |
| Effort produced a new question instead of resolving the hypothesis | **Step 1** — new Brief for the new question |

### Top-priority escalation triggers

- No user need can be identified from any input — never invent one
- Audience undefined and no prior Audience Definition Card available — never assume "general users"
- Completed study with no sources — never invent the technique
- Team pressure to skip a step — flag the gap and hold the Brief at Medium; don't silently proceed
- Signal cannot connect to any named UX metric — never assign one ("this seems like Satisfaction")

### Top-priority prohibited behaviors

- **Tool before intent.** Choosing a platform before Step 1 is the #1 cause of "we have a lot of data but no signal." Hypothesis first.
- **Treating a single feedback type as sufficient.** Analytics without attitudinal data tells you *what* happened, not *why*. Pair at least two.
- **Comparative mode on unvalidated designs.** A/B testing two designs neither of which has been evaluated for usability produces a false winner.
- **Sharing findings without sources.** Technique + audience + metrics, every time. Without them, findings are opinions.
- **Reporting raw observations as signals.** "Users struggled with X" is not a signal. "58% task success at the payment step, measuring Completion and Comprehension" is.

## How to apply

1. **Identify the entry point.** If the user has a question, Step 1. If they have raw data, Step 1 anyway (write the hypothesis before interpreting). If they have a design/prototype, Step 3. If they have a completed study, Step 5. (See full input → entry table in `reference.md` Playbook.)

2. **Walk the five steps in order.** Skipping Step 1 (intent) is the #1 failure mode. Skipping Step 3 (testability) is the #2.

3. **Match technique to mode, not to familiarity.** Exploratory → Navigation/Feedback. Evaluative → Task/Behavior. Comparative → Comparison/Behavior. Use the technique groups in `reference.md` Techniques.

4. **Pair at least two feedback types.** Behavioral + attitudinal. View + Hear, or See + Sense. If only one is present, recommend the second technique that fills the gap.

5. **Recommend named instruments rather than vague methods.** SUS for usability. NPS for loyalty. SEQ for post-task ease. CES for effort. The full Research Stacks catalog with metric mappings is in `reference.md` References.

6. **Apply the Show Your Sources rule.** Every shared finding includes technique + audience + metrics. Without them, the finding is an opinion. Without the Collection Brief filled out at the time of collection, you cannot reconstruct sources after the fact.

7. **Produce the Collection Brief at the appropriate confidence level.** High → route to Situations. Medium → flag the gap, hold the Brief. Low → escalate.

8. **Route per the table above.** If routing to Patterns appears in source content, **always use Situations** in the canonical marketplace — Patterns has been archived.

## What's new in v3.5.0

- **Upgraded from v1.1 → v1.2 source docs.** Structural rev: 12 techniques now grouped into 5 (Navigation, Task, Comparison, Behavior, Feedback). Five-step workflow renamed and tightened.
- **Collection Brief** introduced as the standard output artifact (14 fields, minimum contract). All workflows now produce this.
- **High/Medium/Low confidence model** with explicit Skill behavior at each level.
- **Show Your Sources rule** formalized — technique + audience + metrics in every shared finding.
- **Agent Operations split into its own file** (`agent-operations.md`) with full Runtime Flow, per-step input minimums, four-form ambiguity handling, and Skill Boundaries.
- **Operating rules promoted into SKILL.md** so the binding rules bind on every invocation.
- **Downstream routing updated**: Patterns block has been archived by Bryan and replaced with **Situations**. The Collection Brief now hands off to Situations, not Patterns. References to "Patterns" in source content are preserved as DERIVED but cross-block routing in SKILL.md and the Decisions section have been updated.

## Handoffs

- When the user shifts to *naming the underlying need*, suggest `glare-define-user-needs`.
- When they ask *who the participants/customers should be*, suggest `glare-define-audience`.
- When they ask *which numbers to track or how to interpret them*, suggest `glare-define-ux-metrics`.
- **When a Collection Brief is complete and ready for pattern synthesis, suggest `glare-define-situations` (replaces the deprecated `glare-define-patterns`).**
- When the data is collected and the team is moving to calibrated benchmarks and concept testing, hand off out of Define toward `glare-measure`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* to capture (not just instruments) and how to structure them, route to `glare-design-signals` and the bucket skills.
- When preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When assessing team maturity, route to `glare-design-assessment`.
