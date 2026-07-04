---
name: glare-define-audience
description: Use this skill when the user is defining WHO their signals come from in the Define area — picking audiences, evaluating credibility, building Audience Definition Cards, OR formatting a completed Card for a specific reader. Triggers — "who are we designing for," "is this audience credible," the four source types (Helio, Advertising, CRM, Internal Assumption), the four audience types (Participants, Customers, Stakeholders, Project Team), Audience Definition Card, High/Medium/Low credibility, 3–5 attributes, lifecycle segments, audience drift, label vs behavior, "Glarify this audience," format triggers (brief/deck/message/board/business case for a Helio study), agent operations runtime contract. Do NOT use when naming the need (use `glare-define-user-needs`), choosing techniques (use `glare-define-collecting`), or picking metrics (use `glare-define-ux-metrics`).
version: 3.6.0
source_doc_version: "v1.2 (7-doc) + v1.4 Formats (8-doc — Overview, Techniques, Playbook, References, Decisions, Examples, Formats, Agent Operations)"
last_rebuilt: 2026-06-23

sources:
  - doc_id: 1aAepKOT5eyKwn-xXHByVyIycqXE3wI_qHB4klYomig8
    title: Glare | Define, Audience, Overview v1.2
    drive_url: https://docs.google.com/document/d/1aAepKOT5eyKwn-xXHByVyIycqXE3wI_qHB4klYomig8/edit
    last_synced: 2026-05-26
  - doc_id: 1Ski3LJdIeBnGA6vaHs9yrAMnsbCaueFctilvJfgL72Q
    title: Glare | Define, Audience, Techniques v1.2
    drive_url: https://docs.google.com/document/d/1Ski3LJdIeBnGA6vaHs9yrAMnsbCaueFctilvJfgL72Q/edit
    last_synced: 2026-05-26
  - doc_id: 1Qc-UrF3tcMz-nRqOHywnjK33N3S_V6SGq9DZkmFqFhg
    title: Glare | Define, Audience, Playbook v1.2
    drive_url: https://docs.google.com/document/d/1Qc-UrF3tcMz-nRqOHywnjK33N3S_V6SGq9DZkmFqFhg/edit
    last_synced: 2026-05-26
  - doc_id: 1yGaaGU21proQusWcFDt76fgId-Itc6vRvWFZ1ibwlQI
    title: Glare | Define, Audience, References v1.2
    drive_url: https://docs.google.com/document/d/1yGaaGU21proQusWcFDt76fgId-Itc6vRvWFZ1ibwlQI/edit
    last_synced: 2026-05-26
  - doc_id: 1-GljLFEIjXRieBq-PfIhO-V4N_XygP8qao3QeqKa0RY
    title: Glare | Define, Audience, Decisions v1.2
    drive_url: https://docs.google.com/document/d/1-GljLFEIjXRieBq-PfIhO-V4N_XygP8qao3QeqKa0RY/edit
    last_synced: 2026-05-26
  - doc_id: 14d22zJTUp2UbVrGCQpj5mV8Sdxckil6JUshKar-oIbs
    title: Glare | Define, Audience, Examples v1.2
    drive_url: https://docs.google.com/document/d/14d22zJTUp2UbVrGCQpj5mV8Sdxckil6JUshKar-oIbs/edit
    last_synced: 2026-05-26
  - doc_id: 1n3O9f8n7eGdF7DgOiC4WkHawPQ61w20jsEgLUWWkMKw
    title: Glare | Define, Audience, Agent Operations v1.2
    drive_url: https://docs.google.com/document/d/1n3O9f8n7eGdF7DgOiC4WkHawPQ61w20jsEgLUWWkMKw/edit
    last_synced: 2026-05-26
  - folder_id: 1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm
    title: Glare | Define, Audiences, Formats/ subfolder — 10 per-format docs v1.4 (Brief, Business Case, Boards, Decks, Docs, Experiment, Messages, Roadmap, Scripts)
    drive_url: https://drive.google.com/drive/folders/1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm
    last_synced: 2026-06-23
    note: Overview doc for Formats not yet published — formats.md adapted from User Needs Formats v1.4 pattern with Audience-specific credibility model.
---

You are helping the user work the **Audience** block of the Decision Map's **Define** area — defining who their signals come from, where those signals came from, and how much weight each can carry in a design decision.

## Core idea

Audience sits inside the Define area of the Decision Map. Without explicit audience, customer data, stakeholder opinion, and personal preference all get weighted equally and metrics lose meaning. Audience answers two questions: **who are we learning from, and is that source credible for this decision?**

v1.2 introduces a parallel architectural split:

- **Four source types** — Helio Audience Groups (highest credibility), CRM/Lifecycle Segments (medium), Advertising Segments (low for design), Internal Assumptions (lowest)
- **Four audience types** — Participants (early validation), Customers (proof — the ground truth), Stakeholders (alignment), Project Team (intent)

The standard output of any Audience workflow is an **Audience Definition Card** with a High/Medium/Low credibility rating. That card is the brief Collecting receives.

## Files to read

This skill ships three files alongside `SKILL.md`. Read in this order:

1. **`agent-operations.md` first.** Runtime contract for **producing** the Audience Definition Card — source identification, per-attribute extraction, credibility scoring, output contract, routing, escalation. Governs how a Card is *made*.
2. **`formats.md` — only when the user is packaging a completed Card for delivery.** Runtime contract for **Glarifying** — the 4-step resolution sequence (Credibility → Purpose → Reader → Format), the 9 format types (per-format Drive pages at folder `1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm`), compatibility matrices, and a second layer of Agent Operations governing formatting. Triggered by "Glarify this audience," "write a brief for this," "how do I present this to my VP."
3. **`reference.md` third.** Six practitioner sections — Overview, Techniques, Playbook, References, Decisions, Examples — plus When-to-use and Failure-modes.

The highest-leverage rules from both AO layers are duplicated into "Operating rules" below.

If the user has described their situation in a sentence or two, start by routing them through the **Decisions** section of `reference.md` — match their situation to the Primary Routing Table.

## Operating rules

Binding rules from `agent-operations.md`. They apply on every invocation regardless of whether the full file is read.

### Source identification — the first move

Before classifying, extracting attributes, or rating credibility, **identify the source type**. Source type is never inferred from content alone.

| Input Signal | Source Type | Credibility Starting Point |
|---|---|---|
| Named Helio audience groups with poll response breakdowns | Helio Audience Group | **High** |
| Demographic targeting (Facebook, Google, programmatic) | Advertising Segment | **Low** — not qualified for design without behavioral validation |
| CRM exports with lifecycle stage, tenure, activation, feature adoption | CRM / Lifecycle Segment | **Medium** |
| Survey data with defined respondent criteria | Survey (Medium CRM equivalent) | **Medium** |
| Forum posts, reviews, community threads | Qualitative | **Medium** for motivation/context, **Low** for behavioral/lifecycle |
| Team/leadership statements without external data reference | Internal Assumption | **Low** |
| Personas or segments without a named research source | **Unknown — escalate** | Cannot rate until source is confirmed |

If the source cannot be identified, **escalate before proceeding**.

### Output Contract — The Audience Definition Card schema

Every card uses these 9 fields. Cards below the minimum contract are **not handed off**.

| Field | Minimum requirement |
|---|---|
| **Audience Name** | Descriptive name built from defining attributes — NOT a demographic label or role title |
| **Audience Type** | Participants, Customers, Stakeholders, or Project Team |
| **Source** | Named data source with source type identified (not "various") |
| **Defining Attributes** | ≥2 behavioral OR motivational sub-attributes confirmed by evidence (named specifically) |
| **Design Situation** | 1–2 sentences describing conditions that make this group experience the situation differently |
| **Connected UX Metrics** | ≥1 UX metric connected to a defining attribute |
| **Credibility Rating** | High, Medium, or Low with a one-line rationale |
| **Gaps** | Named missing sub-attributes, or "None identified" if coverage is complete |
| **Lifecycle Stage** | If applicable: Trial / Freemium / New Paying / Habitual / Power / Advocate / Dormant / Churned |

### Confidence and credibility

Three or more assumed (vs. evidenced) attributes in a single type **lower the overall credibility rating by one level.**

| Confidence Level | Skill behavior | Output |
|---|---|---|
| **High** | Proceeds independently. Completes the card, routes to Collecting without escalation. | Complete card, High or Medium credibility |
| **Medium** | Completes a partial card, flags all assumed attributes by name, notes what validation Collecting needs. Does not route without flagging the gap. | Partial card with credibility note and named gaps |
| **Low** | Stops. Does not attempt to complete the card. Escalates with specific statement of what's missing and what source type would fill it. | Escalation message with named gaps and recommended next step |

### Routing logic

| Condition | Route to |
|---|---|
| Card complete, credibility **High** | **Collecting** — state audience type, defining attributes, connected UX metrics, recommended method |
| Card complete, credibility **Medium** | **Collecting with validation note** — name assumed sub-attributes; Collecting must include a screener or qualifying question before the main study |
| Card partial, credibility **Low** | Back to **Audience** — Helio screener needed; name which sub-attributes are missing and which source type would fill them |
| Design situation doesn't match stated user need | **User Needs** — return with attribute profile as new evidence |
| Multiple groups detected in input data | Back to **Audience** — split required; name each group by distinguishing attributes |
| Advertising and Helio data diverge | **Stakeholders** — flag as strategy question, not usability question |
| Source cannot be identified | **Escalate to human** — ask: where did this data come from? |

### Top-priority prohibited behaviors

- **Inferring source type from content.** Always ask directly when source is unclear.
- **Collapsing multiple Helio groups into one card** to produce a cleaner output. The split is information; preserve it.
- **Designing power users for the person configuring exports** when they're actually configured for others — and other label-vs-behavior conflations. (See Example 4 in `reference.md`.)
- **Treating a stakeholder anecdote as validated customer evidence.** A CMO saying "customers told me X" is a hypothesis worth investigating, not a design brief.
- **Skipping the credibility rating.** Without it, Collecting doesn't know whether to proceed with confidence, add validation, or rebuild.
- **Filling in assumed attributes silently.** Every assumed attribute must be flagged by name.

### Escalation triggers (when to surface to a human, not auto-resolve)

- Source cannot be identified from the input
- Confidence stays Low even after ≥2 input types are present
- Multiple need-interpretations or audience groups remain equally plausible
- Advertising and Helio data diverge (strategy question, not usability)
- Accessibility-sensitive design with accessibility needs not in the audience definition (never assumed)
- Business impact is high and evidence quality is weak

### Formats (Glarify) — the second runtime contract

When the user has a completed Audience Definition Card and asks to share it, present it, or format it, the Formats layer applies. Resolve four variables **in order**:

| Step | Variable | Values |
|---|---|---|
| 1 | **Credibility** | Read directly from the Card. High/Medium/Low. **Determines what the output can honestly ask for.** |
| 2 | **Purpose** | Inform · Align · Decide · Prioritize · Validate · Hand Off |
| 3 | **Reader** | Product team · Designer · Researcher · Product leader · Executive · Cross-functional |
| 4 | **Format** | Messages · Decks · Boards · Scripts · Docs · Brief · Roadmap · Experiment · Business Case |

**Every formatted output must include a visible credibility signal early.** High: "This audience is confirmed through a Helio behavioral study..." · Medium: "Behavioral attributes confirmed; motivational attributes assumed..." · Low: "The current audience definition is a starting hypothesis, not a confirmed group..."

**What Credibility can honestly ask for:**
- **High** → sprint scope alignment, prioritization, design commitment, investment
- **Medium** → direction alignment with a validation step built in
- **Low** → approval to run a Helio study. **Nothing else.**

**Prohibited on Formats:** presenting Low as confirmed · using Brief/Business Case for Low without framing the ask as Helio study approval · applying Direct tone to Medium/Low · adding attributes not in the source Card · omitting the credibility signal.

Full compatibility matrices and per-format structural rules live in `formats.md`.

## How to apply

1. **Identify the source type first** using the table above. If unknown, escalate.

2. **Pick the entry point.** If the user is starting from a question, run Entry Point A (name question → identify audience type → select 3–5 attributes → identify source → map to UX metrics → draft card). If starting from existing data, run Entry Point B (identify source type → extract attributes → name groups by attributes → evaluate credibility → identify gaps → draft card).

3. **Extract attributes against specific sub-attributes**, not just types. For behavioral, look for frequency, experience level, feature adoption, interaction mode, task orientation. Flag each as **present, missing, or assumed**.

4. **Rate credibility** using the source type starting point and the assumed-attribute count. Three or more assumed in a single type drops one level.

5. **Produce the Audience Definition Card** using the 9-field schema above. Cards below the minimum contract are not handed off.

6. **Route per the table above**, with a specific statement of what to do next — not a generic "more research is needed."

7. **When multiple groups appear in the input, do not average.** Produce one card per group. Use the Playbook's comparison step to identify which to prioritize.

8. **Watch for drift signals** — satisfaction flat but churn rising, feature requests from unexpected segments, Helio composition shifted year over year, internal assumptions more than 6 months old. Drift is both a need question and a strategy question.

9. **For complete signals, run the closing checklist** — source identified and credibility rated, ≥3 behavioral or motivational attributes, design situation in 1–2 sentences, connected UX metrics, multiple groups separated, definition matches the stated user need.

## What's new in v3.5.0

- **Upgraded from v1.1 → v1.2 source docs.** Major rev — descriptive 4-audience frame becomes a structured architecture with 4 source types in parallel.
- **Audience Definition Card** introduced as the standard output artifact (9 fields, minimum contract). All workflows now produce this.
- **High/Medium/Low credibility ratings** with explicit routing implications for Collecting.
- **Two entry points** (start from question vs. start from data) — most real Audience work follows Entry Point B and the new content covers it explicitly.
- **Audience Drift diagnostic** — 4 early indicators, framed as a "both a need question and a strategy question" cross-block routing.
- **Agent Operations split into its own file** (`agent-operations.md`) with per-attribute-type extraction targets — what counts as Present, Missing, or Assumed for each of the 25 sub-attributes across the 5 types.
- **Operating rules promoted into SKILL.md** so the binding rules (source identification, output contract, credibility scoring, routing, escalation) bind on every invocation.
- **7 worked Examples** — each with a strong version (proper card) and a weak version (what happens when source evaluation is skipped or groups are collapsed).

## Handoffs

- When the user shifts to naming *the unmet need itself*, suggest `glare-define-user-needs`.
- When they ask *how to actually run the test* or pick instruments (SUS, first-click, A/B, heatmaps), suggest `glare-define-collecting`.
- When they ask *which metrics prove it worked*, suggest `glare-define-ux-metrics`.
- For multi-block Define questions, hand back to `glare-define`. For the Decision Map as a whole, `glare-decision-map`.
- When the user is asking what *signals* (not just metrics) to capture from each audience, route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
- When a Helio study is the right next step, that's outside this skill — but the recommended Collecting method is in the Audience Definition Card under "what Collecting needs."
