---
name: glare-define-collecting
description: Use this skill when the user is in the Collecting block — turning raw input into usable signals, OR formatting a completed Collection Brief for a specific reader. Triggers — research mode (Exploratory / Evaluative / Comparative), 5-step process (Intent → Stack → Approach → Techniques → Connect), 12 techniques in 5 groups (Navigation, Task, Comparison, Behavior, Feedback), named instruments (SUS, NPS, SEQ, CES, NASA-TLX, UEQ), 4 feedback types (View / See / Sense / Hear), 5 Design Stacks (Website, Mobile App, Product, E-commerce, Marketing), Define → Capture → Connect cadence, Collection Brief, Show Your Sources, "Glarify this study," format triggers (study proposal, deck, doc handoff, business case for Helio study), agent operations runtime contract. Do NOT use when naming the need (use `glare-define-user-needs`), defining who data comes from (use `glare-define-audience`), or picking metrics (use `glare-define-ux-metrics`).
version: 3.6.0
source_doc_version: "v1.2 (7-doc) + v1.4 Formats (8-doc — Overview, Techniques, Playbook, References, Decisions, Examples, Formats, Agent Operations)"
last_rebuilt: 2026-06-23

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
  - folder_id: 17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs
    title: Glare | Define, Collecting, Formats/ subfolder — 6 of 9 per-format docs v1.4 (Messages, Decks, Boards, Scripts, Docs, Experiment; Brief, Business Case, Roadmap not yet published)
    drive_url: https://drive.google.com/drive/folders/17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs
    last_synced: 2026-06-23
    note: Overview doc for Formats not yet published — formats.md adapted from User Needs Formats v1.4 pattern with Collecting's Brief Confidence model.
---

You are helping the user work the **Collecting** block of the Decision Map's **Define** area — the discipline that turns raw input into usable signals and prevents drift back into "loudest voice wins."

## Core idea

Collecting sits inside the Define area. User Needs names what users are trying to do. Audience defines who you are learning from. Collecting is the step that turns both into actual evidence — behavior observed, reactions captured, perceptions recorded.

The output of every Collecting workflow is a **Collection Brief** (14 fields) handed off to **Situations** (formerly Patterns; Bryan archived Patterns). Every effort follows the **Define → Capture → Connect** cadence and the **five-step workflow**: Start with Intent → Choose Your Stack → Identify the Approach → Apply the Techniques → Connect and Ready Your Data.

## Files to read

This skill ships three files alongside `SKILL.md`. Read in this order:

1. **`agent-operations.md` first.** Runtime contract for **producing** the Collection Brief — required inputs per step, confidence thresholds, 14-field output contract, routing logic, escalation triggers. Governs how the Brief is *made*.
2. **`formats.md` — only when the user is packaging a Brief or Signal Produced for delivery.** Runtime contract for **Glarifying** — 4-step resolution sequence (Brief Confidence → Purpose → Reader → Format), 9 format types (per-format Drive pages at folder `17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs`), Show Your Sources non-negotiable, compatibility matrices. Triggered by "Glarify this study," "write a study proposal," "how do I present these findings," "make the case for a Helio study."
3. **`reference.md` third.** Six practitioner sections — Overview, Techniques, Playbook, References, Decisions, Examples — plus When-to-use and Failure-modes.

The highest-leverage rules from both AO layers are duplicated into "Operating rules" below.

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

### Formats (Glarify) — the second runtime contract

When the user has a Collection Brief (partial or complete) and asks to share it, present it, or format it, the Formats layer applies. Resolve four variables **in order**:

| Step | Variable | Values |
|---|---|---|
| 1 | **Brief Confidence** | Assess from the Brief. High (all 14 fields, Signal Produced as metric result, sources documented) · Medium (fields uncertain, only one feedback type, metrics not fully connected) · Low (no hypothesis writable, no audience, sources missing). **Determines what the output can honestly say.** |
| 2 | **Purpose** | Inform · Align · Decide · Prioritize · Validate · Hand Off |
| 3 | **Reader** | Research team · Product team · Designer · Product leader · Executive · Cross-functional (Situations) |
| 4 | **Format** | Messages · Decks · Boards · Scripts · Docs · Brief · Roadmap · Experiment · Business Case |

**Every formatted output must include a visible Brief Confidence signal early.** High: "The signal shows... [technique, sample, metric]..." · Medium: "Early findings suggest, though validation on [gap] pending..." · Low: "The Brief is incomplete on [X]. We need help resolving..."

**Show Your Sources is non-negotiable.** Technique + audience + metrics in every formatted output. If word count can't accommodate all three, use a shorter format that can — never drop them.

**What Confidence can honestly do:**
- **High** → ship/iterate/kill recommendation · route to Situations · any purpose
- **Medium** → share interim findings with flagged gaps · request methodology critique · Inform/Align/Validate — do not route to Situations until gap resolved
- **Low** → Validate purpose only. Ask for help resolving the gap.

**Prohibited on Formats:** presenting Medium/Low as ship-ready · omitting sources · Direct tone on Medium/Low · retroactively citing methodology not documented · formatting Multi-Study Synthesis without per-study sources.

Full compatibility matrices and per-format structural rules live in `formats.md`.

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
