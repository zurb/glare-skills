# Audience — Formats (Glarify)

**Block:** Define · Audience
**Audience:** AI Skills + practitioners (both)
**Source pattern:** Glare | Define, User Needs, Formats v1.4 (canonical structural pattern)
**Per-format pages:** Audience `formats/` subfolder — folder ID `1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm` (10 per-format docs at v1.4, all titled "Glare | Define, Audiences, Formats, [X] v1.4")
**Last synced:** 2026-06-23

This file is the **Formats section** for Audience — the output-delivery layer. Where `reference.md` covers *what* the block produces and `agent-operations.md` covers *how to produce it correctly*, this file covers **how to shape a produced output for a specific reader, purpose, and format.** The verb is **Glarify.**

The block's main Agent Operations governs artifact production (the Audience Definition Card). This file has its own Agent Operations governing formatting. Two layers of runtime contract — both apply.

> **Naming note.** All 10 per-format docs in Drive use "Audiences" (plural) in their titles — "Glare | Define, Audiences, Formats, [X] v1.4". The block itself and prior v1.2 docs use "Audience" (singular). The skill keeps `glare-define-audience` (singular) as the canonical name. If Bryan confirms this is a v1.4 rename to "Audiences," we'll rename in a future release. Flagged for source-doc clarification.

---

<!-- DERIVED FROM: 1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm — Glare | Define, Audiences, Formats/ subfolder (10 per-format docs at v1.4). Adapted from the User Needs Formats v1.4 pattern for the Audience block's outputs and credibility model. -->

## Overview

**Getting audience understanding to the right person, in the right form, at the right moment.**

The Audience block helps teams identify **who signals come from + how credible each source is** for a specific decision. That understanding only creates value when it reaches the right people in a form they can act on.

An audience definition that belongs in a designer's Figma annotation looks different from one going into an executive brief. A Low-credibility audience being surfaced for validation approval requires different structure than a High-credibility audience ready for sprint scope alignment. **The format shapes how clearly the audience situation lands and what the reader can do with it.**

**Glarify** is the process of taking an Audience Definition Card (or comparison across cards) and preparing it for a specific purpose, audience, and format.

### What Glarify is not

- Glarify does **not** upgrade credibility. A Low-credibility audience remains Low no matter how it's formatted.
- Glarify does **not** add attributes not present in the source card, resolve gaps that haven't been filled through Collecting, or make an inherited persona sound like a Helio behavioral group.
- Glarify is **not** a shortcut to producing outputs. It applies after an Audience Definition Card exists, not before.

### Audience definitions are not static

Audience definitions evolve as new Helio studies, CRM segmentation refinements, or Collecting cycles refine the picture. A group that started as a persona hypothesis can become a Helio-confirmed behavioral audience over time. **Formatting reflects the current credibility, not the aspirational state.**

### When to use Glarify

| Situation | What Glarify does |
|---|---|
| A High-credibility audience needs to reach a Head of Product before sprint scoping | Shapes it as a stakeholder brief with the ask made explicit |
| A Low-credibility audience needs validation before design proceeds | Frames it as a brief requesting Helio study approval |
| Two audience groups surfaced — team needs to align on prioritization | Structures the comparison as a deck or doc that surfaces the tradeoff |
| A designer needs to annotate a Figma frame with which audience it targets | Compresses the Card into a board annotation tied to the specific frame |
| An audience definition needs to live in the PRD | Expands the Card into a doc section that stands on its own |
| An audience needs to be presented in a client review | Shapes it as deck slides with the design situation front and center |
| An audience should connect to a Collecting study | Structures it as an experiment proposal targeting the specific validation gap |
| Team needs to build the investment case for a Helio study | Builds the Low-credibility audience into a business case for validation |

---

## Outputs Available

Glarify works with the structured outputs produced through the Audience Playbook.

### The Audience Definition Card (primary output)

The 9-field structured artifact — the source of truth for all other formats.

| Field | Contains |
|---|---|
| Audience Name | Descriptive name built from defining attributes (not a marketing label) |
| Audience Type | Participants · Customers · Stakeholders · Project Team |
| Source | Named data source with source type identified |
| Lifecycle Stage | If applicable: Trial · Freemium · New Paying · Habitual · Power · Advocate · Dormant · Churned |
| Defining Attributes | 3–5 attributes with types (Behavioral · Motivational · Contextual · Lifecycle · Demographic) |
| Design Situation | 1–2 sentences on conditions that make this group experience the situation differently |
| Connected UX Metrics | 2–3 metrics the defining attributes connect to |
| Credibility Rating | **High** · **Medium** · **Low** with one-line rationale |
| Gaps | Named missing sub-attributes, or "None identified" |

### The Multi-Group Comparison

When multiple groups have been separated into individual Cards, the Playbook produces a comparison surface (per-group attributes, credibility, connected metrics, and the divergence analysis). **This is a common Formats input** — most Audience work involves at least 2 groups worth comparing.

### Card Summary (short form)

A 1–3 paragraph narrative derived from the full Card — the starting point for most message, deck, board, and script formats where the full 9-field table is too dense.

### A note on Credibility in formatted outputs

**Credibility is the single most important thing Glarify must preserve accurately.** Every format has explicit rules for how Low, Medium, and High credibility outputs differ in what they can ask for and how they must signal source strength. Downstream decisions (design commitment vs. validation approval vs. sprint scope) hinge entirely on credibility being represented honestly.

---

## Purpose (6 types)

Before choosing a format, know why the output is being shared.

| Purpose | What the reader needs to do | What the format must do |
|---|---|---|
| **Inform** | Understand that this is the audience being designed for | Self-contained, clear about credibility |
| **Align** | Agree on which audience the work is scoped to | Invite perspective without reopening every attribute from scratch |
| **Decide** | Make a scope, funding, or approval call | Connect the audience directly to a business consequence |
| **Prioritize** | Compare this audience against others | Provide comparison structure across groups |
| **Validate** | Confirm whether the audience holds before design proceeds | Surface open questions and gaps honestly; often requests a Helio study |
| **Hand Off** | Pick up the audience and design/collect against it | Include full Card, comparison notes, credibility, open questions |

**Purpose ≠ Format.** A brief can serve Decide *or* Validate depending on the credibility of the source Card. **When purpose is unclear, default to Inform.**

---

## Credibility governs everything else

Where the User Needs Formats layer uses "Understanding Strength" (Emerging/Building/Stable) to govern tone and purpose fit, the Audience Formats layer uses the block's own **credibility ratings** — with much sharper implications because credibility directly gates what a formatted output can ask for.

| Credibility | Meaning | What the format can ask for | Signal phrase |
|---|---|---|---|
| **High** | Helio behavioral group with attributes confirmed through observed responses | Sprint scope alignment · Prioritization decisions · Design commitment · Investment | "This audience is confirmed through a Helio behavioral study. The group is defined by how they actually behave." |
| **Medium** | CRM/lifecycle segment with clear behavioral attributes but some assumed motivational/contextual | Direction alignment with a validation step built in · Early resourcing alongside Collecting | "Behavioral attributes are confirmed. Motivational attributes are assumed and will be validated in Collecting." |
| **Low** | Advertising segment · Internal assumption · Persona without named source | Approval to run a validation study — nothing else | "The current audience definition is a starting hypothesis, not a confirmed group. We need a Helio screener before design work proceeds." |

### Credibility governs tone

| Credibility | Default tone | Characteristic language |
|---|---|---|
| High | Direct | "The audience is..." · "Confirmed through..." · "Defined by..." |
| Medium | Collaborative | "Behavioral attributes confirmed; validation needed on..." · "The group appears to..." |
| Low | Exploratory | "Current hypothesis..." · "Assumed attributes..." · "Not yet confirmed..." |

### Marking credibility in every output

Every Glarify output must include a **visible credibility signal early** — usually in the first sentence or as a labeled field. It must **not** be buried, softened, or omitted.

### Credibility can move in either direction

A Helio screener can promote a Low-credibility audience to High. New behavioral evidence can also downgrade a previously High audience if the group composition has shifted (audience drift). **Formatted outputs reflect current credibility, not the state at time of Card creation.** Update outputs in circulation if credibility changes.

---

## Reader Types (6 audiences for the Glarified output)

| Reader | Cares about | Output should emphasize |
|---|---|---|
| **Product team** | Which group is being designed for and why | Attributes, design situation, connected UX metrics |
| **Designer** | Where friction appears for this specific group | Design situation, defining attributes, workflow moment |
| **Researcher** | Credibility, source, gaps, open questions | Credibility rationale, source type, missing attribute types |
| **Product leader** | Prioritization, sprint scope, tradeoffs | Which group first, business consequence, credibility |
| **Executive or stakeholder** | Business outcome, investment risk | Credibility (blunt), business consequence, ask |
| **Cross-functional team** | Handoff clarity | Full Card, comparison notes, next-step ownership |

---

## Format Pages (9 formats)

Each format has its own deep-dive page in the Audience `formats/` subfolder (`1TyquhFpgtyOVlC38DNdBMLuHERoAhyXm`). Each page includes: When to Use, Format Rules with word count, Credibility-specific handling, Writing for that audience, 2 worked examples at different credibility levels, Near-Miss failures, per-format Agent Operations.

| Format | Contains | Drive doc title (v1.4) |
|---|---|---|
| **Messages** | Slack, email, text | Glare \| Define, Audiences, Formats, Messages |
| **Decks** | Deck slide, presentation narration | Glare \| Define, Audiences, Formats, Decks |
| **Boards** | Figma quip, Miro cluster, workshop prompt | Glare \| Define, Audiences, Formats, Boards |
| **Scripts** | Loom, async video narration | Glare \| Define, Audiences, Formats, Scripts |
| **Docs** | PRD section, research handoff, AI brief | Glare \| Define, Audiences, Formats, Docs |
| **Brief** | Stakeholder brief, executive summary | Glare \| Define, Audiences, Formats, Brief |
| **Roadmap** | Roadmap item, planning entry | Glare \| Define, Audiences, Formats, Roadmap |
| **Experiment** | Helio study proposal, validation study proposal | Glare \| Define, Audiences, Formats, Experiment |
| **Business Case** | Business case for a Helio study or audience investment | Glare \| Define, Audiences, Formats, Business Case |

**Sample structural detail from the Brief per-format page** (for reference — full content in Drive):

- Stakeholder Brief: 120–200 words with elements Situation · Audience Finding · Business Consequence · Credibility Signal (required) · The Ask
- Executive Summary: 150–250 words with elements Business Context · Situation · Consequence · Credibility Signal (required) · Recommendation
- Two worked examples at High and Low credibility, showing the difference in what the brief can ask for

### Shared constraints across all formats

- Accurately reflect the **current credibility rating**
- Include a **visible credibility signal** (early, unambiguous)
- Use **only attributes present in the source Card** — never add invented attributes
- **Never** upgrade credibility through tone
- Support the stated purpose **without overclaiming** what the audience justifies
- Update if credibility changes after the output is shared

---

## Compatibility

### Output type × Format

| Output | Messages | Decks | Boards | Scripts | Docs | Brief | Roadmap | Experiment | Business Case |
|---|---|---|---|---|---|---|---|---|---|
| Full Audience Definition Card | ◎ | ◎ | ◎ | ◎ | ✓ | ✓ | ✓ | ◎ | ✓ |
| Card Summary (short form) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ◎ |
| Multi-Group Comparison | — | ✓ | — | ◎ | ✓ | ◎ | ✓ | ◎ | ◎ |

`✓ Recommended` · `◎ Works with adjustments` · `— Not recommended`

### Credibility × Purpose

| Credibility | Inform | Align | Decide | Prioritize | Validate | Hand Off |
|---|---|---|---|---|---|---|
| High | ✓ | ✓ | ✓ | ✓ | ◎ | ✓ |
| Medium | ✓ | ✓ | ◎ | ✓ | ✓ | ✓ |
| Low | ✓ | ◎ | — | — | ✓ | ◎ |

`✓ Recommended` · `◎ Works with explicit framing` · `— Not recommended`

### Adjustment notes

**Low-credibility audience into a Decide format (Brief or Business Case).** Only appropriate when the decision is about approving a Helio study — never appropriate for approving a design direction or sprint scope. The ask must be explicitly framed as investment in validation.

**Full Card into Messages, Decks, Boards, or Scripts.** The 9-field Card has too many fields for these formats. Use the Card Summary as the starting point and pull the most relevant fields: Audience Name, top 2–3 defining attributes, Credibility, and the design situation.

**Multi-Group Comparison into Messages or Boards.** Comparisons are too dense for a single message or annotation. Format each group separately, or use a Docs/Decks format designed for multi-group content.

**Low-credibility into a Hand Off.** Acceptable when the receiving team's role is to run the Helio study to promote credibility. Credibility must be the first labeled field in the handoff, and gaps must be explicit.

**Medium-credibility into a Decide purpose.** Possible when the decision is about resourcing further Collecting rather than committing to a design direction. Frame the ask as "commit to validation," not "commit to the design."

---

## Agent Operations (Formats runtime contract)

This is the **Formats-layer Agent Operations** — separate from and additional to the main block AO in `agent-operations.md`. Both apply.

### Trigger conditions

Invoke this file when the user has a completed Audience Definition Card (or Multi-Group Comparison) and is asking how to share, present, or communicate it. Trigger phrases:

- "Glarify this audience"
- "Format this Card as [X]"
- "Turn this into a slide for the VP"
- "How do I present this audience to my Head of Product"
- "Write a brief for this audience"
- "Make the case for a Helio study on this group"
- Any request naming a specific format or reader type

**Do not invoke Formats before an Audience Definition Card exists.** If the user asks to format raw audience data or personas without a completed Card, route to the Audience Playbook first.

### Required resolution sequence — before producing any output

The Skill must resolve **four variables in order.** If any is unclear from context, ask before proceeding.

| Step | Variable | How to resolve |
|---|---|---|
| 1 | **Credibility** | Read directly from the source Card. High/Medium/Low. **Required before any other decision** — determines what the output can honestly ask for. |
| 2 | **Purpose** | Ask or infer from context. What decision or action is this output supporting? |
| 3 | **Audience (reader)** | Ask or infer from context. Who is receiving this and what do they need to do? |
| 4 | **Format** | Select based on purpose × reader. Load the per-format page from the `formats/` subfolder for structural rules before producing output. |

### Output contract

Every formatted output must:

- **Stay within the word count** for the target format
- **Include a visible credibility signal** — the specific phrase depends on High/Medium/Low
- **Use only attributes present** in the source Card
- **Apply tone that matches** credibility (Direct/Collaborative/Exploratory)
- **Support the stated purpose** without overclaiming
- **Never** ask for design commitment or sprint scope alignment on a Low-credibility Card

### What a Skill must not do

- Present a Low-credibility audience as confirmed or ready for design commitment
- Add attributes not present in the source Card
- Use research method terminology without plain-language translation (executive/stakeholder formats)
- Omit or bury the credibility signal to make the output sound more authoritative
- Use Brief or Business Case format for a Low-credibility audience without framing the ask as Helio study approval
- Format Multi-Group Comparisons into Messages or Boards without splitting
- Apply Direct tone to a Medium or Low credibility Card
- Skip the resolution sequence and default to a format without confirming purpose and reader

### Routing after formatted output

- User asks how to gather more evidence to move Low → Medium/High → `glare-define-collecting` (Helio screener workflow)
- User asks which UX metrics to track for this audience → `glare-define-ux-metrics`
- Output is going into a review — user wants to prep for the conversation → suggest the **Decks** or **Brief** format specifically
- Audience drift detected between formatting cycles → route to `glare-define-situations` (drift is a situation, not just an audience gap)

<!-- /DERIVED -->

---

<!-- ADDED 2026-06-23 -->

## Which rules are promoted into SKILL.md

The following are duplicated into `SKILL.md` so they load on every invocation regardless of whether this file is consulted:

- **The 4-step resolution sequence** — Credibility → Purpose → Reader → Format
- **The 3-state credibility vocabulary** (High / Medium / Low) with required signal phrases and what each credibility can ask for
- **The 6-purpose taxonomy** and the credibility × purpose compatibility matrix
- **Top-priority prohibited behaviors** — presenting Low as confirmed, using Brief/Business Case for Low without validation framing, applying Direct tone to Medium/Low, splitting Multi-Group into single-group formats

The full 6-reader emphasis table, full compatibility matrices, adjustment notes, and per-format page references stay here and are consulted when the Skill is actively packaging an output.

<!-- /ADDED -->
