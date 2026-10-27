# Collecting — Formats (Glarify)

**Block:** Define · Collecting
**Audience:** AI Skills + practitioners (both)
**Source pattern:** Glare | Define, User Needs, Formats v1.4 (canonical structural pattern)
**Per-format pages:** Collecting `formats/` subfolder — folder ID `17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs` (6 per-format docs at v1.4: Messages, Decks, Boards, Scripts, Docs, Experiment. Brief, Business Case, and Roadmap not yet published as of 2026-06-23)
**Last synced:** 2026-06-23

This file is the **Formats section** for Collecting — the output-delivery layer. Where `reference.md` covers *what* the block produces and `agent-operations.md` covers *how to produce it correctly*, this file covers **how to shape a Collection Brief (or the signals it produced) for a specific reader, purpose, and format.** The verb is **Glarify.**

The block's main Agent Operations governs Brief production. This file has its own Agent Operations governing formatting. Two layers of runtime contract — both apply.

---

<!-- DERIVED FROM: 17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs — Glare | Define, Collecting, Formats/ subfolder (6 per-format docs at v1.4). Adapted from the User Needs Formats v1.4 pattern for Collecting's Brief-based confidence model. -->

## Overview

**Getting collected signals to the right person, in the right form, at the right moment.**

The Collecting block turns intent + audience into evidence — the discipline that produces the Collection Brief and, ultimately, the signal that hands off to Situations. That signal only creates value when it reaches the right people in a form they can act on.

A study proposal going to a stakeholder for approval looks different from a Signal Produced going to Situations for pattern-matching. A Building-stage Brief being shared for methodology critique requires different structure than a completed Brief ready for cross-team learning. **The format shapes how clearly the collection story lands and what the reader can do with it.**

**Glarify** is the process of taking a Collection Brief (or the Signal Produced from a completed Brief) and preparing it for a specific purpose, audience, and format.

### What Glarify is not

- Glarify does **not** upgrade signal strength. A Signal Produced from a study with only one feedback type stays limited, no matter how it's formatted.
- Glarify does **not** add sources not documented in the source Brief, retroactively cite techniques not used, or make a signal sound more validated than the Show Your Sources data supports.
- Glarify is **not** a shortcut to producing outputs. It applies after a Collection Brief exists (partial or complete), not before intent is set.

### Collection Briefs evolve

A Brief starts at Step 1 (Intent) and matures through Steps 2–5. Formats can be produced at multiple stages:

- Before the study runs (Study Proposal / Experiment format)
- After partial data comes back (Interim findings)
- After the study is complete with Signal Produced (Handoff to Situations / Cross-team learning)

**Formatting reflects the current Brief completeness, not the aspirational state.**

### When to use Glarify

| Situation | What Glarify does |
|---|---|
| A study proposal needs stakeholder approval before running | Shapes it as an Experiment proposal or Business Case with the ask made explicit |
| A completed Brief needs to hand off to Situations | Structures the Signal Produced as a Docs handoff with full sources |
| A team wants to share methodology with another team | Compresses the technique/tool/sample-size into a Scripts or Docs format |
| A designer needs to annotate a Figma frame with what a study found | Compresses the signal into a Board annotation |
| A signal needs to be presented in a review | Shapes it as a Deck slide with the metric result and sources visible |
| A study needs to reach a Head of Product before sprint scoping | Frames it as a Brief with the recommendation and sources |
| A pattern of studies suggests a Situations candidate | Structures the multi-study synthesis for cross-block routing |

---

## Outputs Available

Glarify works with the outputs produced through the Collecting Playbook.

### The Collection Brief (primary artifact)

The 14-field structured document — the source of truth for all other formats.

| Field | Contains |
|---|---|
| User Need | Named need from the User Needs block |
| Business Goal | Measurable outcome connected to the need |
| Hypothesis | Specific testable statement pairing need and goal |
| Audience | Named audience with source type and credibility level |
| Mode | Exploratory · Evaluative · Comparative |
| Stack | Research Stack or named Design Stack |
| Approach | Exploring · Evaluating · Comparing (with testable question) |
| Technique(s) | Named technique or pair with sample size |
| Tool(s) | Named platform |
| UX Metrics | Named metrics the technique will produce |
| Feedback Types | ≥2 of: View · See · Sense · Hear |
| Sharing Level | Project-level · Cross-team · Leadership rollup |
| Signal Produced | UX metric result (not raw observation) |
| Hypothesis Resolved? | Confirmed · Refuted · Open (with next question) |

### The Signal Produced (the key exportable artifact)

The single most important field for formatting. This is what hands off to Situations. It **must** be expressed as a UX metric result with sources documented — "58% task success at the payment step, measuring Completion and Comprehension, Helio usability test, 30 new users" — never as a raw observation like "users struggled."

### The Study Proposal (pre-run form)

When formatting is happening before data collection, the source is a Brief with fields 1–12 complete but Signal Produced and Hypothesis Resolved still blank. This is the input for Experiment and Business Case formats.

### A note on Show Your Sources in every formatted output

**Every Glarify output must preserve technique + audience + metrics.** This is Collecting's non-negotiable — the same rule that governs the source Brief. Without those three, the finding is an opinion, not a signal. **Formatting cannot omit sources to save space.** If a format's word count can't accommodate them, use a Card Summary that names them briefly rather than dropping them entirely.

---

## Purpose (6 types)

| Purpose | What the reader needs to do | What the format must do |
|---|---|---|
| **Inform** | Understand what was studied and what it found | Self-contained; sources visible |
| **Align** | Agree on what the signal means before acting | Invite methodology critique without reopening the whole Brief |
| **Decide** | Make a ship / iterate / kill call based on the signal | Connect signal directly to the hypothesis and to a business consequence |
| **Prioritize** | Compare this signal against others (cross-study synthesis) | Provide comparison structure across Briefs |
| **Validate** | Confirm methodology or signal strength before committing resources | Surface Brief completeness and open methodological questions honestly |
| **Hand Off** | Pick up the signal and route to Situations or Measure | Include full Brief with all 14 fields |

**Purpose ≠ Format.** An Experiment proposal serves Decide (approve the study) or Validate (methodology critique). **When purpose is unclear, default to Inform.**

---

## Brief Confidence (governs what the format can honestly say)

Where User Needs Formats uses "Understanding Strength" and Audience Formats uses "Credibility," Collecting uses **Brief Confidence** — the same 3-level scheme from the block's main Agent Operations. It governs what a formatted output can honestly ask for.

| Confidence | Meaning | What the format can honestly do |
|---|---|---|
| **High** | All 14 Brief fields present, sequence followed, Signal Produced expressed as metric result, sources documented | Recommend ship/iterate/kill · Route to Situations · Present findings to any audience · Support any purpose |
| **Medium** | Hypothesis testability uncertain OR audience credibility ≤ Medium OR only one feedback type OR metrics not fully connected to signal | Share interim findings with flagged gaps · Request methodology critique · Support Inform/Align/Validate — do not route to Situations until gap resolved |
| **Low** | No hypothesis writable, no user need identified, no audience defined, sources missing on a completed study | Escalate. Do not produce ship-ready outputs. Only appropriate purpose is Validate — asking for help resolving the gap. |

### Confidence governs tone

| Confidence | Default tone | Characteristic language |
|---|---|---|
| High | Direct | "The signal shows..." · "58% task success at..." · "Confirmed through the [technique]..." |
| Medium | Collaborative | "Early findings suggest..." · "Pattern is forming, though we still need to..." · "Signal is directional; validation on [gap] pending" |
| Low | Exploratory | "We don't yet have..." · "The Brief is incomplete on..." · "We need help resolving..." |

### Marking Confidence in every output

Every Glarify output must include a **visible Brief Confidence signal**. It should appear early — usually the first sentence or a labeled field. It must **not** be buried, softened, or omitted.

### Confidence can move in either direction

A study that comes back with unexpected results can downgrade a previously High Brief if the Signal Produced doesn't connect to a UX metric. Additional validation can promote Medium → High. **Formatted outputs reflect current confidence, not the state at time of Brief drafting.**

---

## Reader Types (6 audiences for the Glarified output)

| Reader | Cares about | Output should emphasize |
|---|---|---|
| **Research team** | Methodology, sources, signal quality | Technique, sample size, feedback types, Brief completeness |
| **Product team** | What the signal means for next steps | Signal Produced, hypothesis resolution, recommendation |
| **Designer** | What the signal means for design decisions | Signal in context of the workflow moment, design implications |
| **Product leader** | Ship/iterate/kill call, sprint impact | Signal, business consequence, recommendation, sources briefly |
| **Executive or stakeholder** | Business outcome, investment ROI | Business consequence, signal in outcome language, sources (validation) |
| **Cross-functional team (Situations)** | Full Brief for pattern-matching | All 14 fields, especially Signal Produced with sources |

---

## Format Pages (9 formats)

Each format has its own deep-dive page. The `formats/` subfolder (`17IXrxO4NmYYPKeaYWfuo35jQKt6jPlTs`) currently contains 6 of the 9 canonical formats.

| Format | Contains | Drive doc (v1.4) |
|---|---|---|
| **Messages** | Slack, email, text | ✓ Published |
| **Decks** | Deck slide, presentation narration | ✓ Published |
| **Boards** | Figma quip, Miro cluster, workshop prompt | ✓ Published |
| **Scripts** | Loom, async video narration | ✓ Published |
| **Docs** | PRD section, research handoff, AI brief for Situations | ✓ Published |
| **Experiment** | Study proposal, methodology writeup | ✓ Published |
| **Brief** | Stakeholder brief, executive summary | ⚠ Not yet published — use Audience Brief pattern as interim reference |
| **Roadmap** | Roadmap item, planning entry | ⚠ Not yet published |
| **Business Case** | Business case for a study or research investment | ⚠ Not yet published |

### Shared constraints across all formats

- Accurately reflect the **current Brief Confidence**
- Include a **visible confidence signal** (early, unambiguous)
- **Show Your Sources** — every shared finding includes technique + audience + metrics
- Use **only findings present in the source Brief** — never invent methodology or add sources
- **Never** upgrade Confidence through tone
- Support the stated purpose **without overclaiming** what the signal justifies
- Update if Confidence changes after the output is shared

---

## Compatibility

### Output type × Format

| Output | Messages | Decks | Boards | Scripts | Docs | Brief | Roadmap | Experiment | Business Case |
|---|---|---|---|---|---|---|---|---|---|
| Full Collection Brief | — | ◎ | — | ◎ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Signal Produced (short form) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ◎ | ◎ |
| Study Proposal (pre-run) | — | ✓ | — | ✓ | ✓ | ◎ | ✓ | ✓ | ✓ |
| Multi-Study Synthesis | — | ✓ | — | ◎ | ✓ | ◎ | ✓ | ◎ | ✓ |

`✓ Recommended` · `◎ Works with adjustments` · `— Not recommended`

### Confidence × Purpose

| Confidence | Inform | Align | Decide | Prioritize | Validate | Hand Off |
|---|---|---|---|---|---|---|
| High | ✓ | ✓ | ✓ | ✓ | ◎ | ✓ |
| Medium | ✓ | ✓ | ◎ | ✓ | ✓ | ◎ |
| Low | ✓ | ◎ | — | — | ✓ | — |

`✓ Recommended` · `◎ Works with explicit framing` · `— Not recommended`

### Adjustment notes

**Low Brief Confidence into a Decide format.** Not recommended. Only Validate purpose is appropriate — asking for methodology help to resolve the gap. Never format a Low Brief as a ship/iterate recommendation.

**Full 14-field Brief into Messages or Boards.** The Brief is too dense. Use the Signal Produced (short form) as the starting point and pull the most relevant fields: Hypothesis, Signal Produced (with sources), and Hypothesis Resolved.

**Multi-Study Synthesis into Messages or Boards.** Comparisons across studies are too dense. Use Docs or Decks for the synthesis; break each study into its own message if fielding them individually.

**Medium Confidence into a Decide purpose.** Possible when the decision is about resourcing further Collecting rather than committing to design. Frame the ask as "commit to validation," not "commit to the design direction."

**Study Proposal into a Brief format.** Only appropriate when asking for approval to run — never appropriate for asking for design commitment based on a study that hasn't happened yet.

---

## Agent Operations (Formats runtime contract)

This is the **Formats-layer Agent Operations** — separate from and additional to the main block AO in `agent-operations.md`. Both apply.

### Trigger conditions

Invoke this file when the user has a completed Collection Brief (or a partial Brief they want to format) and is asking how to share, present, or communicate it. Trigger phrases:

- "Glarify this study"
- "Format this signal for [X]"
- "Turn this Brief into a slide"
- "Write a Slack message about what we found"
- "How do I present these findings to my Head of Product"
- "Write a study proposal for stakeholder approval"
- "Make the case for a Helio study on this"
- Any request naming a specific format or reader type

**Do not invoke Formats before a Collection Brief exists.** If the user has raw data without a Brief, route to the Collecting Playbook first — write intent + hypothesis + audience before formatting.

### Required resolution sequence — before producing any output

The Skill must resolve **four variables in order.** If any is unclear from context, ask before proceeding.

| Step | Variable | How to resolve |
|---|---|---|
| 1 | **Brief Confidence** | Assess from the source Brief. Are all 14 fields present? Is the Signal Produced a UX metric result with sources? High/Medium/Low. **Required before any other decision.** |
| 2 | **Purpose** | Ask or infer from context. What decision or action is this output supporting? |
| 3 | **Audience (reader)** | Ask or infer from context. Who is receiving this and what do they need to do? |
| 4 | **Format** | Select based on purpose × reader. Load the per-format page from the `formats/` subfolder (or use the Audience Brief pattern as interim for Brief/Business Case/Roadmap until published). |

### Output contract

Every formatted output must:

- **Stay within the word count** for the target format
- **Include a visible Brief Confidence signal** — the specific phrase depends on High/Medium/Low
- **Show Your Sources** — technique + audience + metrics, always
- **Use only findings present** in the source Brief
- **Apply tone that matches** Confidence (Direct/Collaborative/Exploratory)
- **Support the stated purpose** without overclaiming
- **Never** ship a Low-Confidence Brief as a design recommendation

### What a Skill must not do

- Present a Medium or Low Confidence Brief as ship-ready
- Add methodology not documented in the source Brief
- Retroactively cite techniques or tools that weren't used
- Omit or bury sources to save word count (use a shorter Card Summary format instead)
- Use Direct tone on a Medium or Low Confidence Brief
- Present a Signal Produced as fact when it's stated as an observation (rewrite as metric result or flag)
- Format a Multi-Study Synthesis without preserving per-study sources
- Skip the resolution sequence and default to a format without confirming Confidence and purpose

### Routing after formatted output

- User asks how to resolve gaps in a Medium Brief → return to Playbook Step [X] where the gap sits
- User asks whether the signal is strong enough to hand off → route to `glare:signals-quality` (usable/not-usable filter)
- Output is going into a design review → suggest the **Decks** or **Docs** format specifically
- Signal + Brief is complete and ready for pattern-matching → route to `glare:define-situations` (the Signal Produced becomes an input to Situations' 4-lens analysis)
- User asks how to translate the signal into a business case for further investment → suggest the **Business Case** format (interim: use Audience Business Case pattern)

<!-- /DERIVED -->

---

<!-- ADDED 2026-06-23 -->

## Which rules are promoted into SKILL.md

The following are duplicated into `SKILL.md` so they load on every invocation regardless of whether this file is consulted:

- **The 4-step resolution sequence** — Brief Confidence → Purpose → Reader → Format
- **The 3-state Brief Confidence vocabulary** (High / Medium / Low) with required signal phrases and what each Confidence can honestly ask for
- **The Show Your Sources rule** — technique + audience + metrics, non-negotiable in every formatted output
- **The 6-purpose taxonomy** and the Confidence × Purpose compatibility matrix
- **Top-priority prohibited behaviors** — presenting Low/Medium as ship-ready, omitting sources, applying Direct tone to Medium/Low, retroactively citing methodology, formatting Multi-Study without per-study sources

The full 6-reader emphasis table, full compatibility matrices, adjustment notes, and per-format page references stay here and are consulted when the Skill is actively packaging an output.

<!-- /ADDED -->
