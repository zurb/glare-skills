# Audience — Agent Operations

**Block:** Define · Audience
**Audience:** AI Skills (not practitioners)
**Source:** Glare | Define, Audience, Agent Operations v1.2 (Drive doc `1n3O9f8n7eGdF7DgOiC4WkHawPQ61w20jsEgLUWWkMKw`)
**Last synced:** 2026-05-26

This file is operating instructions for a Skill working with the Audience block, **not** practitioner reference content. The Skill is expected to load and respect this file on every invocation. The highest-leverage rules (Source Identification, Output Contract for the Audience Definition Card, Confidence Thresholds, Routing Logic, Escalation triggers) are duplicated into `SKILL.md` so they load even if this file is not consulted; the full prescriptive detail (including the per-attribute-type extraction targets) lives here.

Practitioner reference content (Overview, Techniques, Playbook, References, Decisions, Examples) lives in `reference.md`.

---

<!-- DERIVED FROM: 1n3O9f8n7eGdF7DgOiC4WkHawPQ61w20jsEgLUWWkMKw — Glare | Define, Audience, Agent Operations v1.2 -->

## How AI Skills operate in Audience work

Skills operate against **specific sub-attributes** — not just attribute type labels. When a Skill evaluates behavioral coverage, it checks for frequency of use, experience level, feature adoption, interaction mode, and task orientation. Missing sub-attributes are flagged by name, not by type.

Confidence thresholds govern when a Skill proceeds independently and when it escalates to a human. Everything below threshold requires clarification before the Skill continues.

---

## 1. Intake and Source Identification

The first thing a Skill does when receiving audience data is identify the source type. **Source identification is non-negotiable** — it determines credibility, which determines every subsequent step.

| Input Signal | Source Type | Credibility Starting Point |
|---|---|---|
| Named Helio audience groups with poll response breakdowns | Helio Audience Group | **High** — confirm attributes are behavioral before finalizing |
| Demographic targeting criteria from Facebook, Google, or programmatic platforms | Advertising Segment | **Low** — not qualified for design decisions without behavioral validation |
| CRM exports with lifecycle stage, tenure, activation milestones, or feature adoption | CRM / Lifecycle Segment | **Medium** — confirm behavioral attributes are present before proceeding |
| Survey data with defined respondent criteria and behavioral screening | Survey (treat as Medium CRM equivalent) | **Medium** — validate assumed attributes before drawing conclusions |
| Forum posts, app store reviews, community threads | Qualitative — contextual and motivational signals only | **Medium** for motivation and context, **Low** for behavioral and lifecycle |
| Statements from team members, stakeholders, leadership without external data reference | Internal Assumption | **Low** — document as hypothesis, do not proceed to design without validation |
| Existing personas or segments without a named research source | **Unknown — escalate** | Cannot rate until source is confirmed. Ask: where did this come from? |

If the source cannot be identified from the input, the Skill **escalates before proceeding**. Source type is never inferred from content alone.

---

## 2. Attribute Extraction

After source identification, the Skill extracts attributes against the specific sub-attributes within each of the five types. The Skill identifies which sub-attributes are **present, missing, or assumed** (rather than evidenced).

### Behavioral attributes — extraction targets

| Sub-attribute | Present signal | Missing signal | Assumed signal |
|---|---|---|---|
| Frequency of use | Data states daily/weekly/monthly usage rate explicitly | No usage frequency mentioned | Described in general terms ("regular users") |
| Experience level | Distinguishes first-time, returning, advanced | No experience level mentioned | Assigned by role label, not behavior |
| Feature adoption | Names specific features used or not used | No feature use mentioned | Assumed from product tier or plan |
| Interaction mode | Specifies device or input method explicitly | No device or input mentioned | Assumed from demographic/market segment |
| Task orientation | Describes goal-driven, exploratory, transactional | No task approach mentioned | Described without behavioral evidence |

### Motivational attributes — extraction targets

| Sub-attribute | Present signal | Missing signal | Assumed signal |
|---|---|---|---|
| Primary motivation | States outcome users seek (speed, trust, mastery, discovery, recognition) | No motivation mentioned | Inferred from product category without asking users |
| Value orientation | Describes trade-offs users accept (efficiency vs. creativity, reliability vs. savings) | No value orientation mentioned | Assumed from target market positioning |
| Risk tolerance | Distinguishes early adopters from cautious users | No risk posture mentioned | Assumed from lifecycle stage without attitudinal data |
| Decision style | Describes guided vs. exploratory preference | No decision style mentioned | Assumed from role or seniority |
| Confidence level | Captures perceived competence or self-reported difficulty | No confidence data mentioned | Assumed from experience level |

### Contextual attributes — extraction targets

| Sub-attribute | Present signal | Missing signal | Assumed signal |
|---|---|---|---|
| Device or platform | Names specific device, OS, or platform | No device context mentioned | Assumed from demographic/market segment |
| Environment | Describes physical setting (workplace, home, field, transit) | No environment mentioned | Assumed from role without contextual evidence |
| Connectivity | Addresses online, offline, low-bandwidth explicitly | No connectivity mentioned | Assumed from environment |
| Workload and time pressure | Describes competing priorities or session length constraints | No workload data mentioned | Assumed from role or frequency |
| Collaboration mode | Distinguishes solo from team or shared system use | No collaboration mode mentioned | Assumed from org size or product tier |

### Lifecycle attributes — extraction targets

| Sub-attribute | Present signal | Missing signal | Assumed signal |
|---|---|---|---|
| Stage of relationship | Explicitly names trial / active / habitual / power / dormant / churned | No lifecycle stage mentioned | Inferred from activity level without explicit segmentation |
| Tenure | States duration of product use in days/months/years | No tenure mentioned | Inferred from plan type or cohort date |
| Activation milestone | Identifies specific actions completed: onboarded, upgraded, first purchase | No milestone mentioned | Assumed from account status |
| Frequency of engagement | States daily/weekly/monthly active cadence | No engagement frequency mentioned | Assumed from subscription tier |
| Renewal or purchase cycle | Describes subscription, one-time, or recurring pattern | No purchase cycle mentioned | Assumed from product category |

### Demographic attributes — extraction targets

| Sub-attribute | Present signal | Missing signal | Assumed signal |
|---|---|---|---|
| Role or profession | States job function explicitly | No role mentioned | Inferred from company size or industry |
| Industry or discipline | Names specific industry or domain | No industry mentioned | Assumed from company type |
| Region or language | Specifies region or language of participants | No region or language mentioned | Assumed from CRM or billing address |
| Age or education | Includes range/level when relevant to comprehension or accessibility | Not mentioned — acceptable if not relevant | Assumed from demographic targeting criteria |
| Accessibility needs | Identifies assistive tech use or accommodation requirements | Not mentioned — flag if accessibility-sensitive | **Never assumed — escalate if relevant and missing** |

### Extraction output

The Skill produces an attribute summary with three lists:

- **Present attributes** — confirmed by evidence, named specifically
- **Missing attributes** — not mentioned or measurable, named specifically
- **Assumed attributes** — described without evidenced source, named specifically with a flag

**Three or more assumed attributes in a single type lower the overall credibility rating by one level.**

---

## 3. Confidence Thresholds and Credibility Rating

### Confidence scoring model

| Factor | Full credit | Partial credit | No credit |
|---|---|---|---|
| Source type | Helio Audience Group | CRM / Survey / Qualitative | Advertising Segment or Internal Assumption |
| Behavioral attributes | 3+ sub-attributes present with evidence | 1–2 present; remainder missing/assumed | None present |
| Motivational attributes | 2+ present with evidence | 1 present; remainder missing/assumed | None present |
| Contextual attributes | 2+ present with evidence | 1 present; remainder missing/assumed | None present |
| Lifecycle attributes | Stage + at least one additional sub-attribute | Stage only, no supporting sub-attributes | None present |
| Assumed attribute count | 0–1 total | 2–3 total | 4+ total |
| Group definition | Defined by behavior or motivation, not by label | Partially behavioral with some label dependence | Defined entirely by demographic label or role title |

### Confidence thresholds

| Confidence Level | Score range | Skill behavior | Output |
|---|---|---|---|
| **High Confidence** | Full credit on source + 4–7 factors at full or partial credit | Proceeds independently. Completes the Audience Definition Card, assigns credibility rating, routes without escalation. | Complete card, High or Medium credibility |
| **Medium Confidence** | Partial credit on source + 3–4 factors at full or partial credit | Completes partial card, flags all assumed attributes by name, notes what validation Collecting needs. Does not route to Collecting without flagging the gap. | Partial card with credibility note and named gaps |
| **Low Confidence** | No credit on source, OR fewer than 3 factors at any credit level | Stops. Does not attempt to complete the card. Escalates with specific statement of what's missing and what source type would fill it. | Escalation message with named gaps and recommended next step |

---

## 4. Output Contract — The Audience Definition Card

Every completed Audience Definition Card must meet the minimum output contract before handoff.

| Field | Minimum requirement | What fails the contract |
|---|---|---|
| **Audience Name** | Descriptive name built from defining attributes | Marketing label, job title, or demographic category without behavioral grounding |
| **Audience Type** | One of: Participants, Customers, Stakeholders, Project Team | Missing or "Unknown" without escalation |
| **Source** | Named data source with source type identified | "Various" or blank |
| **Defining Attributes** | Minimum 2 behavioral or motivational sub-attributes confirmed by evidence, named specifically | Only demographic or lifecycle attributes present with no behavioral/motivational evidence |
| **Design Situation** | 1–2 sentences describing conditions that make this group experience the situation differently | Absent or restates the audience name without interpretive content |
| **Connected UX Metrics** | Minimum 1 UX metric connected to a defining attribute | No UX metric present |
| **Credibility Rating** | High / Medium / Low with one-line rationale | Missing or stated without rationale |
| **Gaps** | Named missing sub-attributes, or "None identified" if coverage complete | Blank when assumed attributes are present |

A card that fails the minimum contract is **not handed off**. The Skill flags incomplete fields, states what input is needed, holds the card until gaps are resolved or escalation is acknowledged.

---

## 5. Routing Logic

| Condition | Route to | What the Skill communicates |
|---|---|---|
| Card complete, credibility **High** | Collecting | State audience type, defining attributes, connected UX metrics, recommended Collecting method. Flag any gaps for follow-up. |
| Card complete, credibility **Medium** | Collecting **with validation note** | State what validation step Collecting needs before drawing conclusions from assumed attributes. Name assumed sub-attributes specifically. |
| Card partial, credibility **Low** | Back to **Audience** — Helio study needed | State which sub-attributes are missing, which source type would fill them, what kind of Helio study or screener would establish a behaviorally defined group. |
| Design situation doesn't match stated user need | **User Needs** | State the mismatch clearly. Return with the attribute profile as new evidence. |
| Multiple groups detected in input data | Back to **Audience** — split required | Name each group by distinguishing attributes. Flag that averaging will produce unreliable findings. Request confirmation on which group to prioritize. |
| Advertising and Helio data diverge | **Stakeholders** | State the divergence specifically. Flag as a strategy question, not a usability question. |
| Source cannot be identified | **Escalate to human** | State that source type could not be determined. Ask: where did this data come from? Do not rate credibility or proceed until source is confirmed. |

### Routing across role tiers

Most Audience work operates at the **Contributor** tier — practitioners completing Audience Definition Cards for use in Collecting. Two situations signal that work has crossed into Expert or Leader territory:

- **Expert crossover.** When signals from different sources conflict and resolution requires interpreting what the divergence means for design direction. The Skill flags the conflict, names diverging sources, routes to a human for interpretation before proceeding.
- **Leader crossover.** When the audience definition surfaces a strategy question — who should the product serve, does current targeting reflect the actual user base, is drift significant enough to change product direction. The Skill names the question explicitly, states a leadership decision is required, holds the workflow until that decision is communicated back.

---

## 6. Ambiguity Handling

### Source ambiguity

The input contains audience data but origin is unclear (persona deck without research citation, segment labeled by team without naming source, spreadsheet without column headers).

- **Rule:** Do not infer source from content. Ask directly: where did this data come from? Do not rate credibility until source is confirmed.
- **Escalation trigger:** Any input containing audience definitions without a named source.

### Attribute ambiguity

A description could map to more than one sub-attribute, or the same language is used for both evidence and assumption ("active users" — frequency? lifecycle? both?).

- **Rule:** Extract all plausible matches, flag each as "possibly present — confirm." Do not collapse ambiguous descriptions into a single attribute without confirmation.
- **Escalation trigger:** More than two ambiguous sub-attributes in the same type, or ambiguity in the behavioral type specifically.

### Group boundary ambiguity

Input data appears to describe more than one audience but has not been formally split (Helio results showing bimodal distributions, CRM segments containing both habitual and dormant users).

- **Rule:** Flag the potential split. Name the distinguishing attribute that suggests two groups. Do not produce a single card that spans both. Ask: should these be treated as separate groups?
- **Escalation trigger:** Any dataset where variance in a single behavioral or motivational sub-attribute is high enough that a single design situation cannot cover both ends.

---

## 7. Escalation Rules

Escalation is not a failure state. It is the Skill correctly identifying that a human decision is required. **Escalation messages are specific, not generic.**

| Trigger | What the Skill says | What it does NOT say |
|---|---|---|
| Source cannot be identified | "I can see audience data here but I can't determine where it came from. Before I can rate credibility or extract attributes, I need to know: is this from a Helio study, a CRM export, an advertising platform, or an internal assumption?" | "I don't have enough information to proceed." |
| Confidence score is Low | "This audience definition doesn't have enough behavioral evidence to support a design decision. Specifically, [name the missing sub-attributes]. To move forward, the team needs a Helio [poll / screener / usability study] that establishes [name the group] by behavior rather than [label / assumption]." | "More research is needed." |
| Multiple groups detected | "The data appears to contain two distinct groups: [name Group A by distinguishing attributes] and [name Group B by distinguishing attributes]. Combining them will produce unreliable findings. Which group should I build the card for first?" | "Your audience may need further segmentation." |
| Design situation doesn't match stated user need | "The audience attributes point to [describe situation]. The current user need statement describes [describe stated need]. These don't align. Before Collecting begins, the team should return to User Needs with this attribute profile." | "There may be a mismatch between your audience and your user need." |
| Accessibility needs relevant but absent | "This design situation involves [name the accessibility-sensitive element]. The audience definition doesn't include accessibility needs as an attribute. This can't be assumed — should this be added, and if so, what accommodation requirements apply to this group?" | "Accessibility attributes may be missing." |

---

## 8. Skill Boundaries

The Audience Skill does **not** replace human judgment in these situations:

- **Strategic decisions about who the product should serve.** The Skill can surface drift or signal divergence. It cannot decide which audience the product should prioritize — that's a leadership decision.
- **Choosing a Collecting method.** The Skill routes to Collecting with a brief. Collecting makes the method decision based on the audience type, attributes, and connected UX metrics.
- **Resolving stakeholder disagreement about the customer.** The Skill can show where signals conflict. Alignment requires a human conversation with the evidence the Skill has surfaced.
- **Determining whether a new audience represents a better opportunity.** The Skill can detect drift and document the new group. Whether to pursue it is a product strategy decision.
- **Interpreting qualitative data without behavioral evidence.** Forum posts and reviews surface motivational and contextual signals. The Skill flags these as Medium credibility for those types only and does not elevate overall credibility without behavioral evidence from a separate source.

When the Skill reaches a boundary, it names what it has surfaced, states a human decision is required, and holds the workflow at that point. It does not proceed past a boundary by filling in assumptions.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-26 -->

## Which rules are promoted into SKILL.md

The following rules are duplicated into `SKILL.md` so they load on every invocation:

- **Source Identification** — the 7-row source type → credibility starting point table
- **Audience Definition Card schema** — the 9 required fields and minimum contract
- **Confidence thresholds** — High / Medium / Low scoring and Skill behavior at each level
- **Top-priority routing rules** — High credibility → Collecting; Medium → Collecting with validation; Low → back to Audience; multiple groups → split required; source unknown → escalate
- **Top-priority escalation triggers** — source unidentifiable, confidence Low, multiple groups not split, accessibility needs missing for accessibility-sensitive designs

Everything else in this file (full per-attribute-type extraction targets with the Present/Missing/Assumed signal columns, full scoring model, role-tier crossover logic, three forms of ambiguity handling, full Skill Boundaries) is consulted when the Skill needs to extract specific sub-attributes, evaluate ambiguity, or handle a multi-Skill workflow. Practitioners should treat this file as a behavioral contract for what they can expect Skills to produce.

<!-- /ADDED -->
