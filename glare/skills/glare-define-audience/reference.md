# Audience — Reference

**Block:** Define · Audience
**Template:** 7-doc (Overview · Techniques · Playbook · References · Decisions · Examples · Agent Operations) — rebuilt 2026-05-26 from v1.2 source docs
**Source last synced:** 2026-05-26

This file contains the **6 practitioner sections** of the Audience block. The 7th section — **Agent Operations** — is split into `agent-operations.md` because it's a runtime contract for AI Skills, not practitioner reference content. See `SKILL.md` for the file-loading order.

Sections sourced from Drive docs are marked `DERIVED`; sections added by the skill-builder (When to use, Failure modes) are marked `ADDED`.

This is a major rev from v1.1 → v1.2. v1.1 was descriptive (the 4 audience voices: Project Team, Stakeholders, Customers, Participants). v1.2 adds a parallel architectural split — **the 4 source types** (Helio, Advertising, CRM, Internal Assumption) — and introduces the **Audience Definition Card** as the standard output, with High/Medium/Low credibility ratings, two distinct entry points (start from a question vs. start from existing data), and an Audience Drift diagnostic.

---

<!-- DERIVED FROM: 1aAepKOT5eyKwn-xXHByVyIycqXE3wI_qHB4klYomig8 — Glare | Define, Audience, Overview v1.2 -->

## Overview

Every design decision starts with people. But not all people experience the same situation the same way.

Audience helps teams understand **who those people are, where their user signals come from, and how much to trust what those signals say.** Without that clarity, customer behavior, stakeholder opinions, advertising data, and internal assumptions are all weighted equally — and the work drifts toward whoever speaks loudest.

In Glare, Audience is one half of the UX Research foundation inside Define. Paired with Collecting, it answers two questions that shape everything downstream: **who are we learning from, and is that the right source for this decision?**

### The seven sections of this block

| Section | File | Purpose |
|---|---|---|
| **Overview** | `reference.md` | Core ideas, purpose, role of Audience inside the framework |
| **Techniques** | `reference.md` | How to read, evaluate, and work with audience data from different sources |
| **Playbook** | `reference.md` | Operational workflows, prompts, inputs, and outputs |
| **References** | `reference.md` | Deep-dive guides for each of the 4 audience types + Helio structure |
| **Examples** | `reference.md` | Realistic situations showing how audience source changes what signals mean |
| **Decisions** | `reference.md` | When audience clarity is strong enough to move to Collecting |
| **Agent Operations** | `agent-operations.md` | How AI Skills receive, evaluate, and route user signals by source |

### Audience as the Research Foundation

In the Glare Assessment, Audience sits in the **Research column of the Building Proof dimension**. When Audience work is strong, every downstream block inherits that credibility. Collecting knows who to study. Patterns reflect real behavior. Hunches in Measure are grounded in a defined group rather than a demographic guess. When weak, the proof chain carries hidden uncertainty all the way to business decisions in Lead.

A low Research score in the Glare Assessment is frequently an Audience problem — wrong source type used for the decision, attributes defined by label rather than behavior, or multiple groups averaged into a finding that serves none of them.

### The source problem

Most teams think they know their audience. They have personas, customer segments, advertising targets, and research participant pools. The problem is that these come from very different places, and they don't mean the same thing for a design decision.

A Facebook audience is built from interest targeting and demographic data. A Helio participant group is built from behavioral and motivational questions. A CRM segment is built from purchase history. An internal assumption is built from team experience and instinct. **Each is a real source. None is interchangeable with the others.**

Audience in Glare is built around one clarifying question:

> ***Where did this user signal come from, and what kind of decision is it actually qualified to support?***

### The Four Source Types

| Source | How it's built | What it's good for | Design credibility |
|---|---|---|---|
| **Helio Audience Groups** | Poll-based questions that assign people to groups by behavior and motivation | Validation testing, predicting how real users will experience a design | **Highest** — built from behavioral data, closest to real use |
| **Advertising Segments** | Demographic and interest-based targeting (Facebook, Google, programmatic) | Reach and conversion — who sees the product, not how they experience it | **Low** for design — built for targeting, not understanding |
| **CRM / Lifecycle Segments** | Purchase history, tenure, activation milestones | Identifying which customer stage to prioritize or measure | **Medium** — useful context, but transactional not experiential |
| **Internal Assumptions** | Team expertise, instinct, stakeholder belief | Setting hypotheses and framing tests before external data exists | **Lowest** — starting point only, must be validated |

Understanding which source you're working with is the first step in every Audience workflow. It tells you what questions to ask, what collecting methods are appropriate, and how much confidence to carry into Measure.

### How Helio structures audiences

In Helio, audiences are not defined manually. They are built through poll questions that sort participants into groups based on how they actually behave and what they actually value. This removes the most common source of audience error: **designing for a label instead of a behavior.** A title like "Manager" tells you little. An attribute like "make budget decisions for a team of ten or more" tells you exactly how that person works and what they need from an interface.

### The Four Audience Types

| Audience | Role | Signal Type | Weight |
|---|---|---|---|
| **Participants** | Early validation — predict how designs will perform before launch | Attitudinal, behavioral, performance | High during testing cycles |
| **Customers** | Proof — confirm how design performs in real use over time | Behavioral, lifecycle, performance | **Highest** — the ground truth |
| **Stakeholders** | Alignment — connect design signals to business priorities and direction | Strategic, organizational | Medium to high |
| **Project Team** | Intent — surface assumptions and frame what gets tested | Internal, directional | Light but continuous |

**The sequence matters:** Project Teams form intent, Stakeholders align on impact, Participants validate direction, Customers confirm outcomes. Internal voices guide. External voices validate. Skipping ahead in this sequence is where most audience errors begin.

### Audience and Collecting work together

Audience answers: **who are we learning from, and is that source credible for this kind of decision?**
Collecting answers: **how do we get that user signal, and what method fits the audience we've defined?**

Without a clear audience, Collecting becomes unfocused. Without Collecting, Audience stays theoretical. Together they feed Patterns. When audience is clearly defined and signals are properly collected, recurring behaviors become visible. Those patterns carry into Measure with enough credibility to test against.

### Audience shapes what patterns mean

The same user signal reads differently depending on who it came from. A drop in task completion from trial users points to an onboarding clarity problem. The same drop from habitual users points to a workflow regression. An advertising segment showing low engagement doesn't tell you why; only a Helio participant study can surface that.

Audience source is not metadata. It is the interpretive frame that determines what a pattern actually means and what decision it supports.

### What Audience doesn't do

- It does not replace research. It frames who research should involve and how much to trust what comes back.
- It does not define the user need. User Needs is a separate block. Audience answers whose experience is shaping the situation; User Needs answers what those people are trying to accomplish.
- It does not tell you what to build. It tells you whether the user signals you're working with are qualified to support a design decision.

### What Audience supports across the Decision Map

| Stage | How Audience clarity helps |
|---|---|
| Measure → Concepts | Knowing your audience source tells you which concept tests are credible and which participant groups to recruit |
| Measure → Hunches | Clear audience framing separates a validated user signal from a stakeholder assumption |
| Focus → Initiatives | Audience lifecycle data tells you which customer segment an initiative is actually serving |
| Lead → Workflows | Stakeholder user signals connect design evidence to the business workflows that drive approval |

When audience is unclear, every downstream decision carries hidden uncertainty. When clear, the decision map compounds — each block builds on user signal quality established here.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1Ski3LJdIeBnGA6vaHs9yrAMnsbCaueFctilvJfgL72Q — Glare | Define, Audience, Techniques v1.2 -->

## Techniques

Techniques covers the thinking behind Audience work — how to read the groups Helio surfaces, how to use attributes to clarify the situation, and how to recognize when the user signals you have are strong enough to act on. Where the Playbook covers execution, Techniques covers interpretation.

### Reading Helio Audience Groups

When Helio runs a poll, it assigns participants to named groups based on their responses. **Those group names are the starting point, not the conclusion.** The real interpretive work is understanding what the attributes behind each group reveal about the design situation.

A group called "High-frequency mobile users" tells you something about behavior. But the attributes that built that group — daily task frequency, mobile-first context, short session length — tell you what the situation actually looks like for those people and where friction is most likely to appear.

#### Three questions for every Helio group

| Question | What it surfaces |
|---|---|
| What attributes define this group? | The behavioral, motivational, or contextual traits that distinguish this group — not just the label |
| How does this group's situation differ from others? | The specific conditions — workflow, environment, experience — that make this group experience the design differently |
| What user need is most likely active for this group? | The connection between the group's attributes and the underlying need they're trying to meet |

If you cannot answer all three, the audience group is not yet legible enough to carry into a design decision. Go deeper into the attributes before moving to Collecting.

#### When groups surprise you

Sometimes Helio surfaces a group you didn't expect — a segment that behaves differently from assumptions, or a split that reveals the audience is less uniform than the team believed. These surprises usually mean one of three things: internal assumptions were wrong, the product is attracting an adjacent audience it wasn't designed for, or the design situation is more complex than the problem statement captured.

In all three cases, examine the attributes of the unexpected group before deciding how to respond. **Don't collapse the surprise back into existing framing.** Let it sharpen the situation first.

### Attributes as situation clarifiers

Attributes describe the real conditions — what people do, what drives them, where they work, where they are in their relationship with the product — that shape how a design is experienced. Glare uses five canonical attribute types:

| Attribute Type | What it reveals about the situation | When it matters most |
|---|---|---|
| **Behavioral** | What people actually do — frequency, task patterns, feature adoption, interaction habits | Understanding usage patterns or identifying where behavior diverges across groups |
| **Motivational** | Why people engage — goals, values, risk tolerance, confidence | When similar behaviors produce different experiences, or when trust and satisfaction signals conflict |
| **Contextual** | Where and how people interact — device, environment, connectivity, time pressure | When environmental conditions are shaping usability or comprehension in ways task data doesn't reveal |
| **Lifecycle** | Where people are in their relationship with the product — trial, active, habitual, dormant, churned | When the same friction means different things at different stages |
| **Demographic** | Background context affecting comprehension or accessibility — role, region, language, experience | When clarity or accessibility breaks down across specific groups |

#### Choosing the right attributes

**Three to five attributes is the working range.** Fewer leaves too much of the situation unexplained. More creates over-segmentation. Start with **behavioral** because they are observable and directly tied to design decisions. Add motivational or contextual when behavior alone doesn't explain the gap. Demographic attributes support the others — they add context but rarely explain a design situation on their own.

#### Attributes connect Audience to User Needs

The strongest use of attributes is the connection they create between an audience group and a user need. When you know that a group's defining attributes are high time pressure, mobile context, and low prior familiarity, you can see directly which user needs are most likely active — speed, clarity, and low effort to get started.

### Evaluating user signal credibility

Not all user signals are equally qualified to support a design decision. The source determines how much weight it can carry — and how it should be used. Credibility evaluation is **not about dismissing data**. It is about matching the signal to the decision it is being asked to support.

#### Four credibility questions

| Question | What a weak signal looks like | What a strong signal looks like |
|---|---|---|
| Was this built from behavior or assumption? | Demographic data, team instinct, or stakeholder belief | Observed behavior, poll responses, or measured interaction |
| Does the source match the decision? | Using a targeting segment to validate a usability hypothesis | Using a Helio participant group to predict how users will experience a flow |
| Is the group defined by attributes or labels? | "Women 25–34 in urban markets" — a label without behavioral grounding | "Users who complete onboarding in under five minutes and return within 48 hours" |
| Has this signal been validated by a closer source? | CRM segment used as a proxy for participant behavior without testing | CRM segment used to frame a Helio study that validates the behavior |

**Credibility is relative to the decision.** Internal assumptions are low credibility for a launch decision but appropriate for framing an early hypothesis. CRM lifecycle data is medium credibility for understanding experience quality but high credibility for identifying which customer stage to prioritize.

### Recognizing audience gaps

Audience gaps appear when the signals a team is working with don't cover the full situation. Gaps are often invisible because teams don't know what they're missing. The most reliable indicators:

- **All signals come from one source type.** Every piece of data is from advertising, or from internal assumptions, or from a single Helio study. No cross-source comparison has happened.
- **The audience is defined by demographics, not behavior.** The team knows who their users are in marketing terms but not what those users actually do or need.
- **Lifecycle stages are missing.** Data on active users but nothing on trial, dormant, or churned — friction at the edges of the lifecycle is invisible.
- **Conflicting signals are being averaged.** Different audience groups are producing different results, but the team is combining them into a single finding rather than treating the difference as information.
- **The audience hasn't been tested recently.** The participant groups or customer segments being used were defined months or years ago and may no longer reflect who is actually using the product.

When any of these appear, the right response is not to gather more data from the same source. It is to identify which attribute type is missing and find a Collecting method that can fill it.

### Comparing signals across sources

Most teams have audience data from more than one source. The challenge is using them together without letting weaker sources contaminate stronger ones.

| Situation | What it means | What to do |
|---|---|---|
| Helio group and CRM segment align | Behavioral validation is consistent with lifecycle data — high confidence | Carry into Collecting with confidence |
| Helio group and advertising segment diverge | The people who see the product are not the same as the people who find it useful — a targeting or positioning gap | Surface to stakeholders before designing; this is a strategy question, not a usability question |
| Internal assumptions and Helio groups conflict | The team's mental model of the user is wrong in at least one dimension | Treat Helio data as ground truth; use the assumption as a hypothesis to test |
| Multiple Helio groups produce different results | The audience is not uniform — different segments have different needs | Do not average; treat each group as a separate design situation and identify priority |

### Spotting audience drift

Audience drift happens when the people a team is designing for quietly shift away from the audience the product was originally built for. It is one of the most common and least-noticed problems in product design. Drift usually appears gradually. By the time it's visible in metrics, the team has been designing for the wrong audience for months.

**Early indicators of drift:**

- **Satisfaction scores are flat but churn is rising.** Users say the product is fine but they're leaving — usually means the product is still serving the original audience but not the audience that's actually growing.
- **Feature requests are coming from an unexpected segment.** The requests don't fit the original use case.
- **Helio group compositions have changed across studies.** The attributes that define the largest group in recent studies look different from a year ago.
- **Internal assumptions are more than six months old.** The team is still designing for a mental model that predates recent growth or product changes.

Audience drift is not always a problem. Sometimes the new audience represents a better opportunity. But it is always a decision — and teams can only make that decision consciously if they can see the drift happening.

### Connecting Techniques to the Playbook

Techniques produces the interpretive clarity that the Playbook turns into structured outputs. Once a team has read their Helio groups, evaluated attribute coverage, assessed credibility, and identified gaps or drift, the Playbook provides the workflows and prompts for organizing that understanding into a usable audience definition. If signals are still too thin or conflicting, the next step is **Collecting** — gathering stronger evidence from a more appropriate source before moving forward.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1Qc-UrF3tcMz-nRqOHywnjK33N3S_V6SGq9DZkmFqFhg — Glare | Define, Audience, Playbook v1.2 -->

## Playbook

The Playbook provides the operational structure for Audience work — the inputs, workflows, prompts, and outputs that turn raw audience data into a definition clear enough to guide Collecting.

Audience work begins in one of two places: a team has a question they need to answer and needs to find the right audience, or a team has existing data and needs to interpret what it says about who is experiencing the situation. **The Playbook covers both.**

### Inputs

| Input Type | Examples | What it can reveal |
|---|---|---|
| Helio study results | Named audience groups, poll response breakdowns, attribute distributions | Behavioral and motivational attributes, how groups differ, which needs are active |
| Survey data | Customer satisfaction surveys, onboarding feedback, NPS responses | Attitudinal attributes, lifecycle stage signals, patterns across segments |
| CRM or analytics exports | Lifecycle stage breakdowns, feature adoption, churn cohorts | Lifecycle and behavioral attributes, which customer segments to prioritize |
| Advertising audience data | Facebook segment definitions, Google audience lists, programmatic targeting | Demographic context, reach composition — not experience quality |
| Existing personas or segments | Marketing personas, product personas, customer archetypes | Starting hypotheses about attributes — must be validated before use |
| Forum or community posts | Support threads, community discussions, app store reviews | Contextual and motivational attributes, friction patterns in natural language |
| Stakeholder assumptions | Leadership beliefs about the customer, product team mental models | Internal framing and bias — useful for surfacing what needs to be tested |

A Skill receiving raw data runs the same process: identify what source type this is, extract which attributes are present, and evaluate whether the data is strong enough to support a design decision or needs validation first.

### Two entry points

#### Entry Point A — Starting from a question

The team knows what they need to learn and needs to identify the right audience.

| Step | Action | Output |
|---|---|---|
| 1 | Name the learning question | A single question specifying what the team needs to understand |
| 2 | Identify the audience type | Which of the four types is the right source for this question |
| 3 | Select 3–5 attributes | The behavioral, motivational, contextual, lifecycle, or demographic traits |
| 4 | Identify the source | How this audience will be reached — Helio study, CRM pull, existing survey, stakeholder interviews |
| 5 | Map attributes to UX metrics | Which measurable outcomes each attribute connects to |
| 6 | Draft the Audience Definition Card | A completed card (see Output section) |

#### Entry Point B — Starting from existing data

The team has raw data and needs to interpret what it says about the audience.

| Step | Action | Output |
|---|---|---|
| 1 | Identify the source type | Which of the four source types this data came from — and what that means for credibility |
| 2 | Extract the attributes present | Which of the five attribute types are represented, which are missing |
| 3 | Name the audience groups | If data contains multiple groups, name each by its defining attributes rather than its label |
| 4 | Evaluate credibility | Run the four credibility questions from Techniques |
| 5 | Identify gaps | Which attribute types are missing and whether those gaps need to be filled |
| 6 | Draft the Audience Definition Card | A completed card with credibility rating and any gaps noted |

### Prompts

**Prompts for starting from a question:**

- What do we need to learn from this audience? Name one specific thing — not a list of goals.
- Who is most likely to experience the friction or situation we're investigating?
- What do we know about how this group behaves? Frequency, task type, channel, experience level.
- What drives this group? What are they trying to accomplish, and what do they value most?
- Where are they in their relationship with the product?
- What context shapes how they interact with this design? Device, environment, time pressure, collaboration mode.
- What would we measure to know if this audience found the design clear, trustworthy, and usable?

**Prompts for interpreting existing data:**

- Where did this data come from? Helio poll, CRM export, survey, advertising platform, forum, or internal assumption?
- What attributes are visible in this data?
- What attributes are missing?
- Are the groups defined by behavior or by label?
- Does this data source match the decision it's being used to support?
- If there are multiple groups, how do their attributes differ?
- What user need is most likely active for each group?

### The Audience Definition Card

The standard output of any Audience workflow. Compact enough to hand directly to Collecting as a brief, structured enough for a Skill to interpret and act on.

| Field | What to fill in | Example |
|---|---|---|
| **Audience Name** | Short descriptive name built from defining attributes, not a marketing label | High-frequency mobile users with short session windows |
| **Audience Type** | Participants, Customers, Stakeholders, or Project Team | Customers |
| **Source** | Where this audience came from | Helio study — behavioral poll, April 2025 |
| **Lifecycle Stage** | Trial, Freemium, New Paying, Habitual, Power, Advocate, Dormant, or Churned (if applicable) | Habitual |
| **Defining Attributes** | 3–5 attributes with their type noted | **Behavioral:** Daily task frequency, mobile-first<br>**Contextual:** Short session windows, high time pressure<br>**Motivational:** Efficiency-oriented |
| **Design Situation** | One or two sentences describing how this group's attributes shape the situation | This group needs to complete core tasks in under two minutes on mobile. Any added steps or unclear navigation creates abandonment. |
| **Connected UX Metrics** | 2–3 UX metrics that the defining attributes connect to most directly | Time on Task, Completion Rate, Effort |
| **Credibility Rating** | High, Medium, or Low based on source type and behavioral definition | High — Helio behavioral poll, attributes validated through responses |
| **Gaps** | Any attribute types missing from the current definition | No lifecycle data — unclear whether these are new or long-term users |

**Minimum viable card** (for Collecting to begin):

- Audience type identified
- Source named and credibility rated
- At least two behavioral or motivational attributes defined
- One connected UX metric
- The design situation described in one sentence

A card below this minimum signals the audience isn't defined clearly enough to move to Collecting.

**How the card maps to Organizing Work** (the documentation maturity dimension): **Objectives** = learning question + audience type. **Drivers** = defining attributes + design situation. **Learnings** = credibility rating + gaps. **Outputs** = completed card handed to Collecting with UX metrics.

### Working with multiple audience groups

Most real-world Audience work involves more than one group. Multiple groups are not a problem to resolve — they are information about the design situation. The Playbook handles them through repetition: one card per group, then a comparison step.

| Comparison | What it reveals |
|---|---|
| Where do the attribute profiles diverge most? | The dimension of the situation creating the biggest difference in experience across groups |
| Which group has the weakest credibility rating? | Where validation is most needed before Collecting |
| Which group's situation is most urgent for the current decision? | Which group to prioritize in Collecting and which to address later |
| Do any groups share the same connected UX metrics? | Where a single Collecting method might serve multiple groups |

The comparison step often reveals that two apparently different groups have more in common than the labels suggested — or that a group the team treated as secondary is actually the one whose situation matters most.

### Handoff to Collecting

The Audience Definition Card is the handoff artifact. When Collecting receives it, the card tells the team or Skill three things:

- **Who to recruit or query** — the audience type, source, and attributes define the group precisely enough to build a study or query a dataset
- **What to measure** — the connected UX metrics define what Collecting needs to capture
- **How much to trust what comes back** — the credibility rating tells Collecting how much validation is already in place

### Handoff back to User Needs

When the defining attributes of an audience group point to a need that wasn't captured — or reveal that the stated need is specific to one group but not others — the handoff goes back to User Needs before Collecting begins. The signal: the design situation in the card doesn't match the user need the team is trying to address.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1yGaaGU21proQusWcFDt76fgId-Itc6vRvWFZ1ibwlQI — Glare | Define, Audience, References v1.2 + references/ subfolder (4 audience type pages, folder ID 1ltirJSpS70QOA-DONNlHA3dtxAciWchq) -->

## References

Reach for this section when you need to look up a definition, check attribute categories, evaluate lifecycle stage meanings, or understand how source credibility is rated.

### The Four Audience Type Pages

Each audience type has its own deep-dive page in the Drive `references/` subfolder (folder ID `1ltirJSpS70QOA-DONNlHA3dtxAciWchq`).

| Audience Type | Role in the signal system | What the page covers | Reach for it when… |
|---|---|---|---|
| **Participants** | Early validation — predict how designs perform before launch | Four testing phases, four participant types, attribute selection for studies, signal collection methods, structuring participant studies in Helio | Planning a research study, interpreting early testing results, selecting participants for a concept or usability test |
| **Customers** | Proof — confirm how design performs in real use over time | Eight lifecycle segments with metrics, attribute types, connecting customer signals to UX metrics through four lenses | Analyzing customer behavior, connecting UX performance to business outcomes, identifying which lifecycle stage to prioritize |
| **Stakeholders** | Alignment — connect design signals to business priorities | Internal vs external types, three stakeholder signal types, design's connection to six business workflows, how to capture and present | Preparing for a stakeholder review, translating UX into business language, mapping evidence to organizational workflows |
| **Project Team** | Intent — surface assumptions and frame what gets tested | Five internal signal types, capturing team intent before testing, common traps in internal audience work | Starting a new project, capturing assumptions before a study, identifying internal bias |

#### How the four types work together

The four audience types form a sequence that compounds signal credibility:

| Stage | Audience Type | What it contributes |
|---|---|---|
| 1 | Project Team | Intent — assumptions, predictions, internal framing |
| 2 | Stakeholders | Direction — business priorities and strategic context |
| 3 | Participants | Clarity — early validation that surfaces friction and tests comprehension |
| 4 | Customers | Proof — real-world confirmation that decisions hold up in actual use |

**Internal voices guide. External voices validate.** Skipping a stage doesn't make it go away — it turns into a gap that surfaces later as misalignment or unexplained friction.

### Source Type Definitions

| Source Type | Definition | Built from | Design Credibility | Legitimate Uses |
|---|---|---|---|---|
| **Helio Audience Groups** | Named groups produced by Helio poll questions sorting participants by behavioral and motivational responses | Poll-based behavioral and motivational questions | **Highest** — grounded in observed responses | Validation testing, participant recruitment, predicting experience quality |
| **Advertising Segments** | Targeting groups built for paid media reach | Platform demographic data, interest categories, browsing/purchase signals | **Low for design** — built for reach, not experience understanding | Contextual background, reach composition analysis, hypothesis framing only |
| **CRM / Lifecycle Segments** | Customer groups defined by transactional and engagement data | Purchase history, tenure, activation milestones, feature adoption | **Medium** — behaviorally grounded but transactional | Lifecycle stage prioritization, retention analysis, identifying which segment to study next |
| **Internal Assumptions** | Beliefs about the audience held by team members or stakeholders | Team expertise, instinct, organizational memory, stakeholder belief | **Lowest** — starting point only | Forming hypotheses, framing early studies, identifying what needs to be tested |

#### Credibility Rating Guide

| Rating | When to use it | What it means for Collecting |
|---|---|---|
| **High** | Helio audience group built from behavioral poll responses; customer data from direct behavioral measurement | Proceed with confidence using this definition |
| **Medium** | CRM or lifecycle segment with clear behavioral attributes; survey data with a defined respondent group | Proceed but include a validation step — at least one method that confirms the segment behaves as the data suggests |
| **Low** | Advertising segment used as proxy for experience; internal assumption without external validation; persona not grounded in recent research | Establish the audience before studying the design — a screener, qualifying poll, or Helio study to build the group first |

### The Five Attribute Types

| Attribute Type | Definition | What it describes | Strongest metric connections | When to prioritize |
|---|---|---|---|---|
| **Behavioral** | What people actually do | Usage frequency, experience level, feature adoption, channel of access, task orientation | Task Completion, Time on Task, Effort, Usability | **Start here** — behavioral attributes are observable and directly tied to design decisions |
| **Motivational** | Why people engage | Primary motivation, value orientation, risk tolerance, decision style, confidence level | Satisfaction, Trust, Sentiment, Loyalty | When similar behaviors produce different experiences, or when attitudinal metrics conflict with behavioral |
| **Contextual** | Where and how people interact | Device/platform, physical environment, connectivity, workload/time pressure, collaboration mode | Error Rate, Comprehension, Time on Task, Completion Rate | When environmental conditions affect usability or comprehension in ways task data doesn't surface |
| **Lifecycle** | Where people are in their relationship with the product | Lifecycle stage, tenure, activation milestone, engagement frequency, renewal/purchase cycle | Retention, Activation, Frequency, Churn Rate | When the same friction means different things at different stages |
| **Demographic** | Background context affecting comprehension or accessibility | Job role, industry/domain, region/language, age/education when relevant, accessibility needs | Comprehension, Accessibility, Inclusivity | When role, language, or accessibility needs are genuinely shaping interpretation. **Use as supporting, not foundational** |

**Attribute selection rules:**

- **Use 3–5 attributes.** Fewer leaves the situation underspecified. More creates over-segmentation.
- **Start with behavioral.** Add other types to explain gaps behavioral data doesn't cover.
- **Use demographics as support, not foundation.**
- **Attributes describe conditions, not people.** Specify the conditions that make a group experience the situation differently — not a marketing persona.
- **Different attribute profiles mean different situations.** When two groups have meaningfully different attributes, treat them as separate design situations rather than averaging them.

### Customer Lifecycle Segments

| Segment | Role in lifecycle | Design situation | Key UX metrics |
|---|---|---|---|
| **Trial / Pilot** | Early exploration of product fit | First impressions dominate. Clarity and value communication critical — confusion creates immediate abandonment | Comprehension, Time on Task, Activation |
| **Freemium** | Sampling value without commitment | Conversion behavior is the signal. Design needs to make value tangible enough to motivate upgrade | Completion, Satisfaction, Trust |
| **New Paying** | First experience after purchase | Setup success and perceived effort define the relationship. Difficult onboarding creates early churn even among motivated users | Completion Rate, Confidence, Error Rate |
| **Habitual** | Regular, consistent use | Efficiency and reliability are what this group measures the design against. Regressions are felt immediately | Task Success, Retention, Usability |
| **Power** | Advanced use and mastery | Depth and customization matter more than simplicity. High expectations, low tolerance for constraints | Efficiency, Feature Use, Satisfaction |
| **Advocates** | Loyal promoters | Emotional connection already established. Design decisions here affect whether advocacy continues or erodes | Sentiment, NPS, Referral Rate |
| **Dormant** | Decreased activity | Something broke the habit. The situation is about identifying what created distance and whether it can be bridged | Frequency, Reactivation Rate, Trust |
| **Churned** | Former users who left | Product failed to meet a need or created enough friction to justify leaving. Exit signals are the highest-value learning | Churn Rate, Sentiment, Exit Feedback |

### Key Terms

| Term | Definition |
|---|---|
| **Audience** | Anyone whose perspective influences a product decision — internally or externally |
| **Audience Definition Card** | The standard output of an Audience workflow. Documents source, audience type, defining attributes, lifecycle stage, design situation, connected UX metrics, credibility rating, and gaps |
| **Audience Type** | One of the four groups Glare works with: Participants, Customers, Stakeholders, Project Team |
| **Attribute** | A trait describing a condition shaping how a group experiences a design. Behavioral, motivational, contextual, lifecycle, or demographic |
| **Audience Drift** | The gradual shift of the actual user base away from the audience the product was originally designed for, usually unnoticed until metrics diverge |
| **Credibility Rating** | A High, Medium, or Low assessment of how much weight a user signal source can carry for a specific design decision |
| **Design Situation** | The specific conditions — described through attributes — that make a group experience a design differently |
| **Helio Audience Group** | A named audience group produced by Helio poll questions sorting participants by behavioral and motivational responses |
| **Lifecycle Segment** | A stage in the customer relationship: Trial, Freemium, New Paying, Habitual, Power, Advocate, Dormant, Churned |
| **Source Type** | Where audience data came from: Helio, advertising platform, CRM/analytics, or internal assumption. Source type determines credibility |
| **User Signal** | Feedback, behavior, or data from an audience group used to inform a design decision |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1-GljLFEIjXRieBq-PfIhO-V4N_XygP8qao3QeqKa0RY — Glare | Define, Audience, Decisions v1.2 -->

## Decisions

Decisions help teams recognize which situation they are in and identify the next step that moves the work forward with more confidence. Audience decisions are not about whether the definition is perfect — they are about whether it is clear enough to support what needs to happen next.

### Recognizing the complexity of your audience situation

- **Simple:** One audience source, Helio-defined, High credibility, attributes clear. Move directly to Collecting.
- **Complicated:** Multiple sources, mixed credibility, or two groups that need to be separated and compared. Requires structured work through the Playbook. **This is where most Audience work lives.**
- **Complex:** Conflicting sources pointing to a strategy question, audience drift detected, or no external data exists. Requires stakeholder alignment or a foundational Helio study before any design work proceeds.

When the situation feels more complex than the Primary Routing Table covers, escalate rather than approximate.

### Primary Routing Table

| Situation | What it signals | Next step | Where it goes |
|---|---|---|---|
| Audience defined, source is Helio, credibility High, attributes cover the situation | The definition is strong enough to support Collecting | Complete the card and hand off with connected UX metrics | Collecting → choose method that fits the audience type and attributes |
| Audience defined, source is CRM or survey, credibility Medium, behavioral attributes present but motivational/contextual assumed | The definition is usable but incomplete | Proceed to Collecting with a credibility note; include at least one method that validates assumed attributes | Collecting → include a screener or attitudinal question |
| Audience source is an advertising segment or demographic label, credibility Low | Not qualified to support a design decision | Run a Helio screener poll to establish a behaviorally defined group | Back to Audience → Helio screener, re-evaluate credibility |
| Audience source is internal assumptions only, no external data | The team is working from instinct | Document assumptions as hypotheses, rate Low, run a Helio study to validate | Back to Audience → Helio validation study |
| Helio or data reveals two or more distinct groups treated as one | The audience is not uniform; averaging will serve neither | Complete a separate card for each group, then use the comparison step | Back to Audience → multiple cards |
| Audience definition reveals a design situation that doesn't match the stated user need | Audience work has surfaced a need that wasn't captured | Return to User Needs with the audience definition as new evidence | User Needs → refine the need statement |
| Advertising audience data and Helio audience data point in different directions | The people who see the product are not the same as those who find it useful — targeting/positioning gap | Surface the divergence to stakeholders before designing | Stakeholders → alignment on target audience |
| No audience data exists and no study has been run | The team has no user signal to work from | Pause design work. Run a Helio audience poll or screener | Back to Audience → Helio study |

### Credibility Decision Guide

| Credibility Rating | Can Collecting begin? | What Collecting needs | When to stop and rebuild |
|---|---|---|---|
| **High** | Yes — proceed with confidence | The Audience Definition Card as the brief | Only if the Collecting method surfaces a group composition that doesn't match the definition |
| **Medium** | Yes — with a validation step | A screener or qualifying question that confirms assumed attributes before the main study | If validation reveals assumed attributes were wrong, return to Audience and rebuild |
| **Low** | **No** — establish the audience first | A Helio screener or behavioral poll to build a group qualified for the decision | After the Helio study, return to Decisions and re-evaluate |

### When the audience is more than one group

| Group comparison situation | Decision |
|---|---|
| One group High credibility, other Medium or Low | Prioritize High credibility group for current Collecting; plan a follow-up to strengthen the other |
| Both groups High credibility but different connected UX metrics | Run separate Collecting studies — do not combine; the metrics differ because the situations differ |
| Both groups same UX metrics but different attributes | A single Collecting study with a screener split may work. Flag attribute differences so results can be analyzed separately |
| One group represents the stated need, other represents an unexpected situation | Complete current work for the stated need group. Document the unexpected group as a new finding and return to User Needs |
| Groups so different that no single Collecting method serves both | Treat as separate workstreams. Each gets its own card, brief, and path through Measure |

### Cross-Block Routing

| Situation | Block | Why |
|---|---|---|
| Audience definition reveals a user need not yet named | User Needs | Attributes have illuminated the situation well enough to identify a need |
| Audience definition complete, credibility High or Medium with validation | Collecting | The definition is the brief; Collecting chooses the method |
| Audience definition points to a specific design situation that maps to a Measure concept | Measure → Concepts | The situation is clear enough to identify the relevant Measure concept |
| Advertising and Helio data diverge, suggesting a targeting gap | Stakeholders | This is a strategy question; design cannot resolve who the product is actually for |
| Audience drift detected | User Needs + Stakeholders | Drift is both a need question and a strategy question |
| Audience work surfaces a lifecycle stage gap | Collecting | Design a study that reaches the missing stage — often a Helio poll targeting dormant or churned users |

### Signals that Audience work is complete

- **Source is identified and credibility is rated.**
- **At least three behavioral or motivational attributes are defined.** Described by what they do and why, not by a demographic label.
- **The design situation is described in one or two sentences.**
- **Connected UX metrics are identified.** Collecting knows what to measure.
- **Multiple groups are separated into individual cards.** No averaging.
- **The audience definition matches the stated user need** (or the mismatch has been returned to User Needs).

**Clarity over comprehensiveness.** Audience work does not need to be exhaustive to be complete — it needs to be precise enough that Collecting has a clear group and Measure has a clear situation to test against.

### Audience lives in Exploratory territory

In the Glare Assessment's Guiding Decisions dimension, Audience sits in the **Exploratory quadrant** — Abstract and Effectual. Audience work produces directional signals, not causal proof. The shift to Analytical happens in Collecting. The shift to Evidential happens in Measure. **When Audience work feels inconclusive, that is usually appropriate** — the goal is a definition clear enough to move into territory where certainty can be built.

### What Decisions doesn't resolve

- Which user need to prioritize — that's a User Needs decision
- Which Collecting method to use — that's Collecting's job
- Which Measure concept applies — Measure makes the final determination
- Whether the product should serve a new audience — stakeholder/strategy decision
- How to reconcile competing stakeholder views — alignment is a leadership decision

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 14d22zJTUp2UbVrGCQpj5mV8Sdxckil6JUshKar-oIbs — Glare | Define, Audience, Examples v1.2 -->

## Examples

Each example follows the same arc: a team has data, the source shapes how much they can trust it, and the audience definition determines where they go next. Each includes a **strong version** (proper Audience Definition Card) and a **weak version** (what happens when teams skip source evaluation or collapse groups prematurely).

### Example 1 — Helio Groups Reveal a Split the Team Didn't Expect

*B2B / Onboarding*

A B2B product team is redesigning onboarding after noticing new paying users activating more slowly than expected. A Helio behavioral poll surfaces **two distinct groups**: administrators who set up the workspace for their team, and individual contributors who are invited in after setup. The team assumed onboarding was a single experience. It is two separate situations.

**Strong version — Card for the administrator group:**

- **Audience Name:** Workspace administrators setting up for a team
- **Type:** Customers — New Paying · **Source:** Helio behavioral poll, Q3 2025 · **Lifecycle:** New Paying
- **Attributes:** *Behavioral:* High task volume, setting up permissions before inviting others. *Motivational:* Completion-oriented, needs to feel ready. *Contextual:* Desktop, high time pressure, often during a work transition.
- **Design Situation:** Administrators need to complete multi-step setup without losing track of progress. Ambiguity in sequence or missing confirmation states creates anxiety that slows activation.
- **UX Metrics:** Completion Rate, Time on Task, Confidence · **Credibility:** High · **Gaps:** No motivational data on anxiety triggers

**⚠ Weak version:** Team combines both Helio groups into "new paying users going through onboarding," designs a single flow trying to serve both. **What breaks down:** Different tasks, different success criteria, different friction. Completion rates stay low across the board; team can't tell why because the data is mixed. The Helio split was the signal — collapsing it discarded the most valuable information.

### Example 2 — CRM Segment Used to Design a Feature

*Ecommerce / Loyalty*

A team is designing a loyalty dashboard. Their data team pulls a CRM segment of customers who earned loyalty points in the last 90 days (4,200 users) and treats this as their audience.

**Strong version:**

- **Audience Name:** Active loyalty earners who have redeemed at least once in 90 days
- **Type:** Customers — Habitual/Advocate mix · **Source:** CRM export, loyalty activity · **Lifecycle:** Habitual / Advocate
- **Attributes:** *Behavioral:* Frequent purchasers, redeemed points at least once, return within 30 days. *Lifecycle:* Habitual trending advocacy. *Motivational:* Value-oriented, motivated by recognition (assumed — needs Helio).
- **Design Situation:** Group already understands the program and has invested in it. Dashboard needs to surface progress and reward value clearly — not explain how the program works.
- **UX Metrics:** Satisfaction, Engagement, Comprehension · **Credibility:** **Medium** — CRM behavioral data solid for lifecycle but motivational attributes assumed · **Gaps:** No attitudinal data on what motivates redemption

The Medium rating flags that Collecting needs a validation step before designing for motivation. A Helio attitudinal poll confirms which reward signals matter most before the dashboard hierarchy is set.

**⚠ Weak version:** Team treats CRM segment as fully validated and designs the dashboard. **What breaks down:** CRM data confirms behavior but not motivation. Dashboard prominently features points balance — but Helio data would have revealed this segment cares most about tier status and upcoming reward eligibility. The behavioral data was credible; the motivational design was assumed.

### Example 3 — Advertising Segment Brought Into a Usability Decision

*Fintech / Landing Page*

A fintech team is about to use a Facebook audience segment (women 28–42, interested in personal finance apps, major metros) to define recruits for a Helio usability study.

**Strong version:**

- **Audience Name:** Prospective users actively evaluating personal finance apps
- **Type:** Participants — Target and Adjacent Users · **Source:** Helio screener built from behavioral criteria — NOT the Facebook segment · **Lifecycle:** Pre-trial / Prospective
- **Attributes:** *Behavioral:* Currently using at least one finance app, actively comparing options. *Motivational:* Trust-seeking, wants clarity on fees and security. *Contextual:* Mobile-first, evaluating during personal time.
- **Design Situation:** Group is making a **trust decision, not a task completion decision**. Landing page needs to communicate credibility and reduce fee ambiguity before any feature comparison.
- **UX Metrics:** Trust, Comprehension, Intent · **Credibility:** High — Helio screener replaces demographic targeting · **Gaps:** None at this stage

**⚠ Weak version:** Team uses Facebook audience definition directly — filtering Helio participants by demographics. **What breaks down:** Facebook targeting identifies people who engaged with personal finance content — not people actively evaluating apps. Participant group includes many casual browsers with no purchase intent. Trust and comprehension scores come back artificially high. Design launches with overconfident signals and underperforms in acquisition.

### Example 4 — Internal Assumptions Treated as Customer Evidence

*B2B / Feature Design*

A product team is designing a data export feature. The team lead has three years of enterprise customer experience and a strong mental model: large CSV exports, scheduled delivery, email notifications. The team uses this as the audience definition.

**Strong version:**

- **Audience Name:** Power users managing recurring data workflows across teams
- **Type:** Customers — Power Users · **Source:** Internal assumption (team lead experience) — requires Helio validation · **Lifecycle:** Power
- **Attributes:** All **assumed** — *Behavioral:* Exports weekly+. *Motivational:* Reliability and predictability. *Contextual:* Desktop, larger data workflows.
- **Design Situation:** If assumptions hold, this group needs automation and scheduling more than a better export UI. **But all attributes are assumed** — a Helio study is required before designing.
- **UX Metrics:** Task Success, Efficiency, Error Rate · **Credibility:** **Low** — all assumed · **Gaps:** Everything

The Low rating stops design against assumptions. A short Helio study validates which attributes are real and surfaces one the team missed: many power users **don't receive the exports themselves — they configure them for others who do**. This changes the design direction entirely.

**⚠ Weak version:** Team treats team-lead experience as customer evidence, skips Audience entirely, runs a usability study on an export UI already designed around the internal assumption. **What breaks down:** The usability study tests the wrong thing — measures whether users can complete the UI (they can) but never surfaces whether automation and scheduling were the right features to build. Feature ships with good usability scores and low adoption. Expert instinct is a valuable hypothesis. Without external validation it is not a design input.

### Example 5 — Dormant Users Misread as an Activation Problem

*Product / Mobile Navigation*

A mobile team sees users who were active six months ago and have stopped opening the app. They classify these as users who never fully activated and plan a re-engagement campaign focused on onboarding content. A pre-launch Helio poll reveals something different: most of these users **activated fully**. They used the app regularly for 2–3 months before stopping.

**Strong version:**

- **Audience Name:** Previously habitual users who disengaged after 2–3 months of active use
- **Type:** Customers — Dormant · **Source:** Helio behavioral poll + CRM lifecycle data · **Lifecycle:** Dormant (previously Habitual)
- **Attributes:** *Lifecycle:* Was Habitual, now Dormant — **not a failed activation**. *Behavioral:* Used core features regularly before stopping. *Motivational:* Loss of perceived value or relevance — habit broke when the use case changed.
- **Design Situation:** This group **doesn't need onboarding content**. They need a reason to return that matches a current use case. Re-engagement should surface value relevant now, not reintroduce basics they already know.
- **UX Metrics:** Frequency, Reactivation Rate, Satisfaction · **Credibility:** High · **Gaps:** No data yet on what changed in the use case

**⚠ Weak version:** Team classifies dormant users as failed activations based on CRM lifecycle stage alone, without running the Helio poll. **What breaks down:** Previously habitual users receiving beginner onboarding content feel patronized, not re-engaged. Campaign sees low open rates and near-zero reactivation. CRM lifecycle data tells you where someone is; it doesn't tell you how they got there.

### Example 6 — Stakeholder Signal Treated as Customer Evidence

*Website / Company Claims*

In a review meeting, the CMO shares that customers have told her the homepage "doesn't communicate trust." The design team takes this as a validated customer signal and begins redesigning trust messaging.

**Strong version:**

- **Audience Name:** Prospective B2B buyers evaluating vendor credibility
- **Type:** Participants — Target Users (for validation); Stakeholders — source of original signal · **Source:** Stakeholder anecdote (CMO) — **Low credibility, requires Helio validation**
- **Attributes:** All assumed — *Motivational:* Trust-seeking, evaluating multiple vendors. *Behavioral:* Decision-makers in a B2B purchase. *Contextual:* Desktop, work hours, likely multi-tab.
- **Design Situation:** The CMO's signal may be real but came through a stakeholder filter — not direct measurement. A Helio comprehension and trust study is required before redesigning credibility elements.
- **UX Metrics:** Trust, Comprehension, Intent · **Credibility:** Low · **Gaps:** All attributes assumed

The Helio study confirms trust is an issue — but the gap is different from what the CMO described: **buyers can't find case studies relevant to their industry**, not that the overall tone feels untrustworthy. Redesign becomes targeted rather than wholesale.

**⚠ Weak version:** Team treats the CMO's anecdote as validated customer signal. Redesigns trust elements — more testimonials, security badges, award logos — without external validation. **What breaks down:** Redesign improves what the CMO valued — visual credibility signals — but doesn't address the actual gap prospective buyers experience. Conversion rates stay flat. **Stakeholder signals are real inputs. They are not customer evidence.**

### Example 7 — Near-Miss: Demographic Label Passed Off as Behavioral Definition

*Ecommerce / Product Browse*

An ecommerce team defines their audience as "women 35–54 who purchase home décor" — from their advertising segment. No one has questioned whether this is the right definition for a usability study.

**Strong version:**

- **Audience Name:** Intentional home goods shoppers comparing multiple items before purchasing
- **Type:** Participants — Target Users · **Source:** Helio screener built from browse behavior — replacing inherited advertising segment · **Lifecycle:** Habitual / Active purchaser
- **Attributes:** *Behavioral:* Browses multiple categories before committing, returns to compare across sessions. *Motivational:* Decision-quality oriented. *Contextual:* Mobile and desktop across sessions.
- **Design Situation:** Browse behavior is **deliberate and multi-session**. Page needs to support comparison and return — not just discovery. Filter and sort UI, saved items, and cross-session continuity matter more than first-impression aesthetics.
- **UX Metrics:** Completion Rate, Engagement, Satisfaction · **Credibility:** High · **Gaps:** No data on mobile-to-desktop transition

The behavioral definition reveals that the team had been optimizing for first-impression aesthetics when the actual friction is in comparison and return.

**⚠ Weak version:** Team keeps the advertising segment definition and recruits Helio participants matching the demographic profile. **What breaks down:** The demographic profile includes both deliberate comparison shoppers AND impulse buyers, who behave completely differently. Study produces noisy results. Team iterates on aesthetics because that's what the mixed group responds to most consistently — which is not the friction causing abandonment. **A demographic label describes who might be in the room. It doesn't describe what they are trying to do.**

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-26 -->

## When to use

- When the user is defining **who** their signals come from — picking and weighting audiences.
- When the user has audience data and needs to evaluate its credibility before acting on it.
- When the user mentions the four source types (Helio, Advertising, CRM, Internal Assumption) or the four audience types (Participants, Customers, Stakeholders, Project Team).
- When the user needs to pick 3–5 attributes from the five categories (Behavioral, Motivational, Contextual, Lifecycle, Demographic).
- When the user is building or interpreting an Audience Definition Card.
- When the user mentions audience drift — feature requests from unexpected segments, satisfaction flat but churn rising, Helio composition shifting.
- When customer lifecycle segments (Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned) need to be applied to a decision.

**Don't use when** naming the underlying need (use `glare-define-user-needs`), choosing collecting techniques/instruments (use `glare-define-collecting`), or picking metrics (use `glare-define-ux-metrics`).

## Failure modes

- **Treating an advertising segment as a behavioral audience.** Facebook interest targeting and behavioral evidence are not the same thing. Match source type to decision.
- **Designing for a label instead of a behavior.** "Women 35–54 who purchase home décor" tells you nothing about how they shop. Translate labels to attributes before designing.
- **Averaging multiple groups into one.** When Helio surfaces a split, that's information about the design situation — not noise to smooth out. Two cards, not one.
- **Treating a stakeholder anecdote as customer evidence.** A CMO saying "customers told me X" is a hypothesis worth investigating, not a design brief. Validate before redesigning.
- **Skipping the credibility rating.** Without High/Medium/Low on the card, downstream Collecting doesn't know whether to proceed with confidence, add a validation step, or rebuild the audience first.
- **Missing the drift.** Satisfaction flat but churn rising; feature requests from unexpected segments; Helio composition shifted year over year. These are early indicators the team is designing for an audience that no longer matches the actual user base.

<!-- /ADDED -->
