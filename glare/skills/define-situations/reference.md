# Situations — Reference

**Block:** Define · Situations (4th and final block of Define — replaces the archived Patterns block)
**Template:** 7-doc (Overview · Techniques · Playbook · References · Decisions · Examples · Agent Operations) — built 2026-05-26 from v1.0/v1.1 source docs
**Source last synced:** 2026-05-26

This file contains the **6 practitioner sections** of the Situations block. The 7th — **Agent Operations** — is split into `agent-operations.md`. See `SKILL.md` for file-loading order.

**Situations replaces Patterns.** Bryan archived the Patterns block; Situations is the new 4th block in Define. The old `glare:define-patterns` skill is deprecated.

Sections sourced from Drive docs are marked `DERIVED`; sections added by the skill-builder (When to use, Failure modes) are marked `ADDED`.

---

<!-- DERIVED FROM: 1nWSOndBCKFkKafk1bZGA6Q-w__7EM1SQK_TJKOj4TOw — Glare | Define, Situations, Overview v1.0/v1.1 -->

## Overview

**Find recurring behaviors and friction shaping decisions.**

Most teams collect signals. Few understand the conditions that created them.

A metric might show high drop-off, rising effort, or weak retention. But a number alone cannot tell you why. It cannot tell you what was happening around the user when the friction appeared, what they were trying to accomplish, what forces were working against them, or why the same breakdown keeps showing up across different sessions, different audiences, and different product areas.

**That is what Situations does.**

Situations is the fourth block in Define. It sits after User Needs, Audience, and Collecting, and it is where those three converge. User Needs names what people are trying to accomplish. Audience identifies whose signals carry weight. Collecting gathers the evidence. **Situations is where recurring conditions become visible across all of it**, turning isolated signals into stable context that teams can design against.

### The seven sections of this block

| Section | File | What it does |
|---|---|---|
| **Overview** | `reference.md` | What Situations is, where it sits in Define, how it connects to User Needs, Audience, and Collecting |
| **Techniques** | `reference.md` | The four lenses for surfacing recurring situations: By Type, By Time, By Stage, By Engagement |
| **Playbook** | `reference.md` | Observe → Interpret → Name cadence with prompts, inputs, and outputs |
| **References** | `reference.md` | 9 situation types, signal-to-situation mapping, common situations by product context |
| **Examples** | `reference.md` | 4 realistic situations with near-miss versions; common traps |
| **Decisions** | `reference.md` | When situational evidence is strong enough to move forward, and what to do when it is not |
| **Agent Operations** | `agent-operations.md` | How AI Skills identify situation-level signals, evaluate pattern strength, route to the next step |

### What is a situation?

A situation is **a specific set of circumstances that gives behavior its meaning.** It captures the conditions surrounding what a user does, not just the action itself.

Behavior does not happen in isolation. Every action a user takes is shaped by what triggered it, what they are trying to accomplish, what stands in their way, what forces are working around them, and what success or failure means in that moment. Strip those conditions away, and a metric tells you what happened. Keep them, and you begin to understand why.

This is the distinction that makes Situations useful. **A pattern without context is just a trend. A situation gives that trend meaning**, because it explains the conditions that produced it.

### The four parts of a situation

Every situation can be understood through four elements:

| Element | What it captures |
|---|---|
| **What triggered it** | The condition, pressure, or goal that set the situation in motion |
| **What they are trying to do** | The progress the user is seeking in this specific context |
| **What stands in their way** | The friction, uncertainty, or constraint that shapes behavior |
| **What success means here** | How the user defines resolution, and what failure costs them |

When the same four-part pattern shows up repeatedly across different users, sessions, and audiences, a situation has emerged. **One data point is an observation. A recurring situation is a design signal.**

### Situations and User Needs are not the same thing

User Needs names what people are trying to accomplish at a **category level** — Basics, Trust, Personal, Impact, Feelings. Those categories are stable and broadly applicable.

Situations are **one level more concrete**. They capture how a need manifests inside a specific context, shaped by the circumstances surrounding it. The same user need can produce entirely different situations depending on who the person is, what they are dealing with, and where they are in the experience.

A physician who needs to learn and a product manager who needs to learn are both expressing the same user need. But the situations they find themselves in are different, shaped by different pressures, workflows, relationships, and stakes. **User Needs defines the category. Situations define the context inside it.**

### Situations vs Jobs to Be Done

JTBD focuses on the need itself — the functional job a person is trying to accomplish, expressed as a statement of motivation and intended outcome. It is a powerful framework for naming what users want, and it maps closely to the User Needs block.

But JTBD treats the situation as background. The circumstance that sets the job in motion, noted and then set aside. The need is the unit of analysis. Everything else is context.

**Situations inverts that priority.** A need is always a product of the circumstances surrounding it. You cannot fully understand what someone needs without understanding the forces shaping that need in this specific context. Those forces include environment, relationships, culture, constraints, habits, and pressure. Strip those away and you have a job statement that is true in the abstract but often too thin to design against.

In practical terms: **JTBD helps you write the User Needs block. Situations is what comes after you collect evidence and start seeing which conditions keep producing the same behaviors.** A situation is a job statement made visible through repeated, real signal.

### How patterns become situations

A situation becomes recognizable when a pattern repeats. One user hesitating during onboarding is an observation. Ten users hesitating in the same moment, across different sessions and different audience segments, is a situation. **The repetition is what gives it design credibility.**

This is why Situations sits after Collecting. You cannot name a situation from instinct alone. You need signals, gathered from the right people using the right methods. When those signals converge, recurring conditions become visible.

**Patterns are the evidence. Situations are the interpretation.** Together, they create the shared context that makes everything downstream more useful.

### Why context shapes what signals mean

The same behavior can mean completely different things depending on the situation surrounding it.

- Long session duration might signal engagement, or confusion, or comparison behavior, or cognitive overload.
- A drop in task completion from trial users points toward onboarding clarity. The same drop from habitual users points toward a workflow regression.
- Rising effort scores after a redesign might indicate that users are learning something new, or that the team introduced friction they did not intend.

Without situational context, teams optimize for the wrong thing. They celebrate completion rates while confidence quietly drops. They reduce time on task without realizing the task itself was the wrong one. They fix the symptom and leave the condition intact.

**Situations prevent that drift.** They keep teams anchored to what is actually happening around the behavior, not just the behavior itself.

### Where Situations sits in Define

| Block | What it focuses on |
|---|---|
| User Needs | The motivations, goals, and expectations that drive behavior |
| Audience | The people and contexts you learn from, and how much to trust each source |
| Collecting | Capturing behavior, perception, and reaction through the right methods |
| **Situations** | Synthesizing signals into recurring conditions that give behavior its meaning |

The first three blocks produce signals. Situations interprets them. **Situations is where Define closes** — the block that turns the signals gathered in User Needs, Audience, and Collecting into stable, shared context that Measure uses to test ideas worth testing.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1r3Jm5VGxd_CsQePq8uxUp3j0NatUmqv5wlEhm0g0Dfc — Glare | Define, Situations, Techniques v1.1 + techiques/ [sic] subfolder (4 lens deep-dives, folder ID 1fcELJO_gGTMRHPasDBfKJXt061iPubtm) -->

## Techniques

**Four lenses for surfacing situations from collected signals.**

Collecting produces signals. Techniques is where you read them for situations.

A signal on its own shows what happened. **A lens shows whether the same conditions keep producing the same result.** Each of the four lenses approaches that question from a different angle, revealing recurring patterns that individual metrics often hide.

None of the four lenses is better than the others. They ask different questions, surface different layers of context, and are most useful at different points in the work. **The strongest situation reads come from pairing at least two lenses and looking for where their findings converge.**

### The Four Lenses

| Lens | Core Question | Best used when… | What it reveals |
|---|---|---|---|
| **By Type** | Are users feeling, doing, and performing in ways that reinforce each other — or pulling in different directions? | You have signals from multiple sources and need to check whether they tell a consistent story | Mismatches between perception, behavior, and efficiency |
| **By Time** | Are early signals predicting what actually happens later — or pointing in the wrong direction? | You need to distinguish friction that is temporary from conditions that are structural | Whether a situation is emerging or already baked in |
| **By Stage** | Is the situation showing up in testing, in production, or in both — and does the signal hold across stages? | You want to know if a situation is validated or only visible in controlled conditions | How confident you can be that the situation is real at scale |
| **By Engagement** | Are users connecting with the product at the level of need, behavior, and sustained activity — or breaking down at one of those layers? | You are seeing adoption or retention signals that do not explain themselves | Where in the engagement progression the situation is creating friction |

### Deep-dive sub-pages

Each lens has a deeper page in the Drive `techiques/` [sic — Bryan's folder typo] subfolder (folder ID `1fcELJO_gGTMRHPasDBfKJXt061iPubtm`) with full explanations, examples, and per-lens checklists:

- **By Type** — attitudinal vs. behavioral vs. performance signals (7KB)
- **By Time** — leading vs. lagging indicators (99KB)
- **By Stage** — predictive vs. proxy vs. analytics signals (468KB)
- **By Engagement** — needs-based vs. behavior-based vs. activity-based metrics (162KB)

### How to choose a lens

Start with the question your team is actually asking, not the data you happen to have.

- **Use By Type** when your signals feel contradictory. High satisfaction alongside low completion, or strong performance alongside weak retention. Reveals whether users feel one thing, do another, and experience a third — almost always the shape of a real situation.
- **Use By Time** when you need to know whether a situation is getting better or worse, or whether an early signal is a reliable predictor of a later outcome. Leading and lagging indicators together show trajectory, not just state.
- **Use By Stage** when you have signals from testing but are not sure they reflect what will happen in production, or when you have analytics data but no predictive or proxy signal to explain it. Tells you how much confidence to carry into a situation statement.
- **Use By Engagement** when adoption or retention is the problem but the source is unclear. Separates situations that break at the point of relevance (does this meet a real need) from those that break at the point of habit (do users keep coming back).

### Pairing Lenses

A single lens surfaces a layer. **Two lenses surfacing the same recurring condition creates a situation worth naming.**

| Pairing | What it reveals together |
|---|---|
| **By Type + By Time** | Whether a mismatch between perception and behavior is a temporary learning curve or a structural condition |
| **By Stage + By Type** | Whether a signal seen in testing holds in production, and whether it appears across all three metric types or only one |
| **By Engagement + By Time** | Where in the engagement progression a situation creates friction, and whether that friction is early-stage or entrenched |
| **By Type + By Engagement** | Whether users who say they value the product actually use it, and whether those who use it keep coming back |

### What a strong situation read looks like

A situation is ready to name when **at least two lenses point to the same recurring condition across different users, sessions, or audience segments.**

For example: By Type shows high comprehension but low completion. By Time shows that early prototype signals predicted the drop-off accurately. The situation is not a usability problem. Users understand the interface. They are stopping for a different reason, one that the surrounding context can explain.

That convergence is what moves a signal from an observation to a situation. **And a named situation is what Measure can actually test.**

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1CBrqIA3Cw0qtWkATZn7358MOrKR72Vzjs5KoTBWqp60 — Glare | Define, Situations, Playbook v1.1 -->

## Playbook

The Situations Playbook helps teams move from collected signals to stable, shared context that can guide product and design decisions. Where Techniques covers how to read signals through four lenses, the Playbook covers **what to do with that reading** — how to organize evidence, move through the Observe → Interpret → Name cadence, and decide when a situation is ready to carry into Measure.

### Situation Inputs

Situations emerge from signals gathered across User Needs, Audience, and Collecting.

| Input | Format | What it reveals |
|---|---|---|
| UX Metrics | Dashboard, spreadsheet, exported report | Recurring friction, behavioral patterns, engagement breakdowns |
| Analytics | Dashboard, event logs, funnel reports | Where the same workflow conditions keep producing the same outcomes |
| Usability Findings | Notes, recordings, reports, screenshots | Comprehension gaps and repeated hesitation points |
| Customer Interviews | Transcript, notes, audio, video | Motivations, emotional context, forces shaping behavior |
| Support Tickets | Text threads, CRM exports, spreadsheets | Recurring operational conditions and workflow friction |
| Surveys | Forms, spreadsheets, exported reports | Expectations, satisfaction patterns, recurring concerns |
| Concept Testing | Screenshots, prototypes, reports, videos | Early comprehension, trust, and confidence signals |
| Workflow Observations | Notes, recordings, journey maps | Environmental and operational forces shaping behavior |
| Helio Audience Signals | Poll results, participant group data | Whether the same situation appears across different audience sources |
| Stakeholder Assumptions | Notes, workshop docs, presentations | Organizational blind spots and unvalidated situational framing |

Situations do not require perfect inputs. They require **enough recurring signal across enough sources to see the same conditions producing the same behaviors.**

### Observing for Situations

The first step in the cadence is **Observe**. Teams review signals not for isolated findings but for recurring conditions. The question is not *what happened in this session* — it is *whether the same circumstances keep producing the same behavior*.

| Condition | What teams should watch for | Situation type it may signal |
|---|---|---|
| **Repeated hesitation** | Users pausing, reconsidering, or stalling at the same point across sessions | Comprehension breakdown or trust gap |
| **Workflow avoidance** | Users skipping steps, finding workarounds, or abandoning predictable paths | Effort or relevance mismatch |
| **Contradictory signals** | Metrics and feedback pointing in different directions across the same workflow | Perception and behavior misalignment |
| **Confidence drop** | Delayed decisions, repeated revisiting, stalled progression despite task completion | Trust or reliability condition |
| **Engagement without retention** | Strong usage signals that do not convert to sustained return behavior | Needs-behavior gap |
| **Consistent drop-off point** | Users exiting at the same workflow stage across different sessions and audience segments | Friction or expectation mismatch |
| **Organizational blind spots** | Teams repeatedly missing or dismissing the same signals in stakeholder reviews | Decision loop weakness |
| **AI output noise** | AI-generated content accelerating production faster than teams can evaluate quality | Signal credibility condition |

The strongest situations usually become visible when **multiple signal sources reinforce the same condition, the same behavior repeats across different audience segments, metrics and stated feedback conflict in a consistent direction, friction appears at the same point across time and stage, or early signals accurately predict later outcomes.**

### Interpreting Signals

The second step is **Interpret**. Teams apply the four lenses to look for convergence — points where multiple signals, across multiple sources, point to the same underlying conditions.

| Lens | Interpretation Question | What convergence looks like |
|---|---|---|
| **By Type** | Are perception, behavior, and performance reinforcing each other or diverging? | High satisfaction with low completion consistently suggests a comprehension or trust condition, not a motivation failure |
| **By Time** | Are early signals predicting what happens later, or pointing in the wrong direction? | Leading indicators that consistently miss lagging outcomes suggest the situation is structural, not temporary |
| **By Stage** | Does the situation hold in production, or only in controlled testing? | A condition that appears in proxy tests but disappears in analytics suggests the testing environment is not capturing the real situation |
| **By Engagement** | Where in the progression from need to behavior to habit does the situation create friction? | Strong needs-based signals with weak activity signals consistently point to a habit-formation condition rather than a relevance failure |

**A situation is ready to name when at least two lenses point to the same recurring condition across different users, sessions, or audience segments.**

### AI Prompt Structure

| Focus | Example prompt |
|---|---|
| **Signal Review** | "Review these usability findings and interview transcripts and identify recurring conditions where the same friction appears across different users." |
| **Lens Application** | "Using the By Type lens, identify whether perception, behavior, and performance signals in these analytics are reinforcing or contradicting each other." |
| **Situation Drafting** | "Based on these signals, draft a situation statement that names the recurring condition, what triggers it, what users are trying to do, what stands in their way, and what success means here." |
| **Situation Validation** | "Does this situation statement hold for both trial users and habitual users based on these signals? Where does it break down?" |
| **Audience Cross-Check** | "Compare these signals from Helio participants against the analytics data and identify whether the same conditions appear in both sources." |
| **Stakeholder Framing** | "Summarize this situation and its business impact in terms a product leader or stakeholder could evaluate and act on." |
| **Pattern Grouping** | "Cluster these support tickets and session observations into recurring situational conditions rather than individual complaints." |

### Primary Situation Output

When a situation is ready to name, the output should be a structured description with these 11 fields:

| Field | What it should contain | Example |
|---|---|---|
| **Situation Name** | Short, descriptive label teams can use as shared vocabulary | "Onboarding confidence breakdown" |
| **Summary** | Concise explanation of the recurring condition and the context it appears in | "Users can technically complete onboarding but consistently leave uncertain and unsupported." |
| **Trigger** | The condition, pressure, or goal that sets the situation in motion | Users encounter the first decision point requiring product understanding before context has been established |
| **What users are trying to do** | The progress the user is seeking | Complete setup and feel confident enough to act on the product's recommendations |
| **What stands in their way** | The friction, uncertainty, or constraint shaping behavior | Recommendations appear before users understand the scoring system behind them |
| **What success means here** | How the user defines resolution, and what failure costs them | Completing setup with enough confidence to act, rather than completing it and still feeling uncertain |
| **Evidence** | The converging signals across lenses and sources | High completion rate (By Stage), low trust scores (By Type), drop in return visits after week one (By Engagement), support questions about score meaning (Collecting) |
| **Audience** | Which audience segments the situation appears in | Consistent across trial users and new paying users. Less pronounced in habitual users |
| **Why it matters** | The operational, user, or business impact | Users who do not understand the product early are less likely to return |
| **Lenses applied** | Which of the four lenses surfaced the situation and where they converged | By Type and By Engagement converged on the same confidence gap. By Time confirmed it is structural, not temporary |
| **UX Metrics** | Metrics most useful for validating whether the situation is improving over time | Comprehension, Trust, Completion Rate, Return Visits (week one to week two) |

### Example Situation Statement (short form)

**Situation:** Onboarding confidence breakdown

Users can technically complete onboarding but consistently leave uncertain about what the product is telling them and what they should do next. Evidence across By Type and By Engagement lenses shows high completion paired with low trust and weak return behavior in the first two weeks.

The trigger is the first decision point requiring product understanding before context has been established. Users are trying to complete setup and feel confident enough to act, but recommendations appear before they understand the system behind them. **Success would mean finishing setup with enough confidence to act, not just enough to finish.**

This situation is consistent across trial users and new paying users. If left unresolved, teams are likely to improve visual polish or completion flows instead of addressing the underlying comprehension condition.

Recommended UX metrics: Comprehension, Trust, Completion Rate, Return visits (week one to week two).

### Multiple Situations

When more than one situation becomes visible, start with a summary table before exploring each individually:

| Situation | Evidence | Lenses that converged |
|---|---|---|
| Onboarding confidence breakdown | High completion, low trust, weak return behavior in week one | By Type, By Engagement |
| Recommendation avoidance | Low recommendation CTR despite high engagement with score display | By Type, By Time |
| Workflow rework loop | Users repeatedly returning to earlier steps after progressing | By Stage, By Engagement |

**Three prioritization questions when multiple situations emerge:**

1. **Which situation is blocking the others?** A comprehension or trust breakdown usually needs to be resolved before workflow or engagement improvements will hold.
2. **Which situation has the strongest evidence?** Prioritize those supported by convergence across multiple lenses and multiple sources.
3. **Which situation connects most directly to a business outcome?** When evidence is roughly equal, the situation most tied to a measurable outcome is usually the right starting point.

### Next Steps

| Next step | Summary | Why it's useful |
|---|---|---|
| Collecting | Gather additional signals to strengthen the situation or test whether it holds across more sources | Useful when the situation is visible but not yet supported by enough converging evidence |
| Hunches | Form hypotheses about what is creating the conditions inside the situation | Useful when the situation is named but the cause is not yet clear enough to test |
| Concepts | Explore design directions that address the conditions inside the situation | Useful when the situation is well-evidenced and the team is ready to generate possible responses |
| Questioning | Design questions that surface attention, comprehension, and friction inside the situation | Useful when the team needs to measure how the situation is experienced before designing against it |
| Findings | Turn the situation into usable understanding that Measure can build on | Useful when the situation is strong enough to anchor a test or concept evaluation |
| Audience | Check whether the situation appears consistently across different audience segments | Useful when the situation is visible in one source but not yet confirmed across others |
| Workflows | Evaluate whether organizational or operational conditions are contributing to the situation | Useful when the situation has a systemic cause beyond the product experience itself |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1bMrKYQST1X3OlxtORMcrVZI0y1UNGydrtifedCSIH6c — Glare | Define, Situations, References v1.0 -->

## References

A catalog of situation types, signal-to-situation mappings, and common situations by product context. Use this as a lookup resource when reviewing signals or writing a situation statement.

### The 9 Situation Types

Situations cluster into recognizable types. Knowing the type helps teams apply the right lens, frame the right questions, and connect the situation to the right UX metrics.

| Situation Type | What it describes | Common Trigger | Primary Lenses |
|---|---|---|---|
| **Comprehension breakdown** | Users can interact with the product but cannot interpret what it is telling them or why | Information appears before users have the context to evaluate it | By Type (attitudinal vs. behavioral mismatch), By Stage |
| **Trust gap** | Users understand what the product is asking but do not believe it enough to act | Recommendations or decisions appear without sufficient evidence or explanation | By Type (satisfaction vs. completion), By Engagement (needs vs. behavior layer) |
| **Effort mismatch** | The cost of completing a task exceeds what users expect or are willing to absorb | A workflow requires more steps, decisions, or cognitive load than the user anticipated | By Type (performance), By Time (leading friction signals) |
| **Relevance failure** | Users engage with the product but do not see it as connected to their actual goal or situation | Product experience addresses a generic need rather than the specific context | By Engagement (needs layer), By Type |
| **Habit formation gap** | Users adopt the product initially but do not build it into their workflow over time | Early value is visible but not reinforced in subsequent sessions | By Engagement (activity layer), By Time (lagging indicators) |
| **Expectation mismatch** | What users expect the product to do and what it actually does diverge at a critical moment | Users arrive with a mental model the product does not match | By Type (attitudinal), By Stage (predictive vs. proxy gap) |
| **Decision loop** | Users reach a decision point and repeatedly return to it without progressing | Insufficient evidence, unclear options, or missing context at a high-stakes decision point | By Type (behavioral), By Time, By Stage (analytics) |
| **Organizational blind spot** | Teams consistently miss or dismiss the same signals across reviews | Stakeholder assumptions override collected signals at key decision points | By Stage (proxy vs. analytics), By Type (contradictory signals) |
| **Signal credibility breakdown** | AI-generated outputs, automated reports, or aggregated metrics move faster than teams can evaluate their quality | Production volume accelerates while evaluation capacity does not | By Stage (proxy vs. analytics), By Time (leading vs. lagging) |

### Signal-to-Situation Mapping

| Signal Pattern | Likely Situation Type | What to check next |
|---|---|---|
| High completion rate + low trust or satisfaction scores | Comprehension breakdown or trust gap | Apply By Type. Check whether users understand what they completed or are finishing mechanically without confidence |
| Strong desirability scores + low adoption or return visits | Habit formation gap or relevance failure | Apply By Engagement. Check whether the needs layer is holding but the activity layer is collapsing |
| Positive prototype results + weak production analytics | Expectation mismatch or effort mismatch | Apply By Stage. Check whether the controlled testing environment is not capturing real-world conditions |
| Leading indicators missed lagging outcomes consistently | Structural situation, not temporary friction | Apply By Time. The situation is baked into the experience, not a learning curve |
| Users repeatedly returning to earlier steps without progressing | Decision loop or trust gap | Apply By Type and By Stage. Check whether users lack evidence to move forward or whether the decision point itself is unclear |
| High engagement metrics + declining retention over time | Habit formation gap | Apply By Engagement and By Time. Check whether early engagement reflects genuine need alignment or novelty |
| Metrics and interview feedback pointing in opposite directions | Expectation mismatch or organizational blind spot | Apply By Type. Contradictory signals usually mean users say one thing and do another |
| Consistent drop-off at the same workflow point across segments | Effort mismatch or comprehension breakdown | Apply By Stage and By Type. Check whether the drop-off is a performance issue, a comprehension issue, or both |
| Low engagement despite relevant content or strong product-market fit signals | Relevance failure or effort mismatch | Apply By Engagement. Check whether the product is addressing the right need but in the wrong context or at the wrong moment |

### Situations by Product Context

#### Onboarding

| Situation | Recurring Condition | Common Misread |
|---|---|---|
| **Confidence breakdown at setup** | Users complete onboarding mechanically but leave without enough understanding to act on what the product is telling them | Teams improve completion flows instead of addressing the comprehension gap |
| **Premature recommendation exposure** | Recommendations or next steps appear before users have the context to evaluate them | Teams interpret low recommendation engagement as disinterest rather than insufficient setup context |
| **Value invisibility** | Users finish setup without understanding what the product will do for them or why it matters in their situation | Teams treat low early engagement as a product-market fit problem rather than a framing problem |

#### Adoption

| Situation | Recurring Condition | Common Misread |
|---|---|---|
| **First-session novelty collapse** | Users engage strongly in the first session but do not return because the product did not connect to a recurring need | Teams celebrate first-session engagement without checking whether early signals predict return |
| **Feature awareness gap** | Users repeatedly miss or ignore features that would address their situation because discovery is unclear or poorly timed | Teams add more features or notifications rather than addressing the situational context |
| **Workflow integration friction** | The product requires users to change existing workflows in ways that cost more effort than the product returns | Teams interpret slow adoption as a motivation problem rather than an effort mismatch |

#### Retention

| Situation | Recurring Condition | Common Misread |
|---|---|---|
| **Satisfied but non-returning** | Users rate the product positively but do not return because it does not connect to a recurring need in their situation | Teams treat high satisfaction scores as retention signals and miss the habit formation gap |
| **Re-entry friction** | Returning users face a reorientation cost each session that increases over time, eroding the habit before it forms | Teams focus on new user experience while the returning user experience quietly degrades |
| **Value decay** | The product delivered value early but has not grown or evolved with the user's situation | Teams attribute churn to pricing or competition rather than evolving context |

#### Decision and Evaluation

| Situation | Recurring Condition | Common Misread |
|---|---|---|
| **Comparison paralysis** | Users cannot move forward because the product presents options without giving them context to evaluate the difference | Teams add more options or personalization rather than addressing the information gap |
| **Evidence deficit** | Users want to act but do not have enough credible information to justify the decision | Teams improve visual design or messaging rather than the underlying evidence |
| **Stakeholder misalignment** | The user understands the product but cannot get organizational buy-in because the product does not speak to other decision-makers' concerns | Teams treat this as an individual user problem rather than a situational condition |

### Situation Strength Checklist

Before carrying a situation into Measure, teams should be able to answer yes to most of these. **A situation that cannot satisfy at least four of the five is an observation, not yet a named situation.**

| Question | Why it matters |
|---|---|
| Does the situation appear in signals from at least two different sources? | A single source can reflect a collection artifact. Convergence across sources increases confidence that the condition is real |
| Do at least two lenses point to the same underlying condition? | One lens showing a pattern is an observation. Two lenses converging is a situation |
| Does the situation appear across more than one audience segment? | A condition visible only in one segment may be an audience-specific finding |
| Can you name all four parts: trigger, goal, friction, and what success means? | A situation without all four parts is incomplete |
| Is the situation stable enough that a concept could be designed against it? | A named situation should be concrete enough to anchor a design response |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1vGYahVHTqOyjMJM_9ajIeEqHvJTzy2cCKdkdWAmFF70 — Glare | Define, Situations, Decisions v1.0 -->

## Decisions

Decisions helps teams identify whether Situations is the right place to be working and, once they are, which part of the block will be most useful given their situation.

### When to use Situations

Situations is the right place to be when signals exist but the conditions creating them are not yet clear, when the same friction keeps appearing across different users and sessions without a shared explanation, or when the team is ready to move into Measure but cannot yet name what they would be testing.

**If the team is reacting to individual data points rather than seeing recurring conditions, Situations is almost always the right place to begin.**

### Recognizing the situation

**1. We have signals but can't see a pattern.** Team has collected data from multiple sources but signals are not pointing in a consistent direction. Everyone draws different conclusions from the same evidence.
*What to do:* Start with Techniques. Apply at least two lenses to the same signals and look for convergence. Use the signal-to-situation mapping table in References to check what the converging signals typically indicate.

**2. We can see the pattern but can't name the situation.** Signals are converging. Team can see something recurring but cannot agree on what the situation actually is.
*What to do:* Use the Playbook's Interpret step and the situation types table in References. Check the signal pattern against the 9 known situation types. Use the four-part structure (trigger, goal, friction, what success means) to draft a situation statement.

**3. We're not sure if what we're seeing is a situation or just noise.** A signal is visible and recurring, but the team isn't confident it represents a real condition.
*What to do:* Use the situation strength checklist in References. A situation needs to appear in at least two sources, across at least two lenses, and across at least two audience segments before it is ready to name. By Time is particularly useful here — leading and lagging indicators together show whether a condition is structural or temporary.

**4. We have a situation statement but aren't sure it's strong enough to move into Measure.**
*What to do:* Apply the situation strength checklist before proceeding. Check whether all four parts are named, whether at least two lenses converged, whether the situation appears across more than one audience segment. If anything is missing, return to the Interpret step.

**5. Multiple situations are emerging at the same time and we don't know where to start.**
*What to do:* Use the Multiple Situations section in the Playbook and apply the three prioritization questions: which is blocking the others, which has the strongest evidence across lenses and sources, which connects most directly to a measurable business outcome.

**6. We need to present the situation to stakeholders who aren't convinced.**
*What to do:* Use the Primary Situation Output table to structure the presentation. The format — situation name, summary, trigger, what users are trying to do, what stands in their way, evidence, audience, why it matters — is designed to ground stakeholder conversations in observable conditions rather than opinion.

**7. We know the situation but aren't sure which UX metrics will tell us if it's improving.**
*What to do:* Go to the situation type in References and check which lenses surfaced it. The lenses point directly to the metric types most relevant. A trust gap surfaced by By Type and By Engagement connects to attitudinal metrics like Trust and Comprehension and activity metrics like return visits.

**8. We're setting up an AI Skill for this block.**
*What to do:* The Playbook is the primary source for the Observe → Interpret → Name cadence, input formats, prompt structure, and expected outputs. References provides the situation type catalog and signal-to-situation mapping the skill uses to classify conditions consistently. Examples provides worked cases and traps for output calibration. Use all three together. Agent Operations covers routing logic, confidence rules, and escalation handling specific to AI Skills.

### Quick Reference

| Situation | Start Here |
|---|---|
| Signals exist but no pattern is visible | Techniques — apply two lenses, check signal-to-situation mapping |
| Pattern visible but situation not named | Playbook — Interpret step, situation types table in References |
| Not sure if it's a situation or noise | References — situation strength checklist, Techniques — By Time |
| Situation named but not strong enough for Measure | References — strength checklist, Playbook — Interpret step |
| Multiple situations, unclear where to start | Playbook — Multiple Situations, References — product context catalog |
| Need to align stakeholders around the situation | Playbook — Primary Situation Output, Example Situation Statement |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1gJc_GGlM1__TjpQmPfRDNsW8dN3Nr3Ni9ylXIQYboc8 — Glare | Define, Situations, Examples v1.0 -->

## Examples

Each example follows the same format: **the signals the team saw, the lenses they applied, where they converged, and the named situation that resulted.** Near-miss versions show what teams initially concluded and why the situational framing changed the decision.

### Example 1: The Onboarding Completion Trap

*SaaS product, onboarding flow, new paying users*

A product team was preparing to launch a redesigned onboarding flow. Prototype testing had gone well. Completion rates in beta were above 80%. Stakeholders were satisfied. The team was ready to ship.

A researcher asked one question before launch: **what do users do in the first 48 hours after finishing onboarding?**

**Signals:**
- Completion rate: 82% finished all onboarding steps in beta testing (By Stage — proxy)
- Trust scores: post-onboarding trust rated 5.8 / 10 across beta participants (By Type — attitudinal)
- Return visits: only 31% of completers returned within 48 hours (By Engagement — activity layer)
- Support tickets: most common week-one question: *"What does my score mean and what should I do first?"* (Collecting — support)

**Lens application:** By Type showed an immediate mismatch — completion strong but trust weak. By Engagement showed the activity layer collapsing after the first session. **Two lenses converged on the same condition:** users were completing onboarding mechanically without building enough understanding to act.

**Named situation — Onboarding confidence breakdown:**
- **Trigger:** First product recommendation appears before users understand the scoring system behind it
- **What users are trying to do:** Complete setup and feel confident enough to act
- **What stands in their way:** Recommendations appear before users have context to evaluate them
- **What success means:** Finishing setup with enough understanding to take a first meaningful action

**Near-miss:** *Initial conclusion was "completion rate is strong, ship it and monitor week-one engagement."* By Type + By Engagement convergence shifted the decision. Team added a context layer before the first recommendation. **Return visits in week one rose from 31% to 58% after launch.**

### Example 2: The Satisfied Non-Returner

*Consumer product, retention, habitual and dormant users*

Consistently high satisfaction scores. Strong NPS. Positive post-session ratings. But retention quietly declining — month-three from 61% to 44% over two quarters. Team could not explain why. **Standard read: a competitor entered the market. Team preparing a feature response.**

**Signals:**
- Satisfaction: post-session 8.2 / 10 across active users (By Type — attitudinal)
- Return visits: month-three retention declining with no corresponding drop in satisfaction (By Time — lagging vs. attitudinal)
- Session behavior: returners completing primary task in under 3 minutes and leaving (By Type — behavioral)
- Interviews: users described the product as "useful when I think of it" but not opened habitually (Collecting)

**Lens application:** By Type showed satisfaction and behavior diverging. By Time showed the retention decline predated the competitor — building steadily for two quarters. By Engagement showed activity layer failing.

**Named situation — Satisfied but non-returning:**
- **Trigger:** Users complete their primary task and find no natural prompt to return
- **What users are trying to do:** Accomplish a specific task when it comes to mind
- **What stands in their way:** Nothing — the product works. But it does not connect to a recurring need in their workflow
- **What success means:** Finding the product useful enough to open without a specific trigger

**Near-miss:** *Initial conclusion was "a competitor is drawing users away — build features to match."* By Time confirmed the decline predated the competitor launch. Team shifted from feature development to habit-forming touchpoints. **Month-three retention recovered to 54% within two quarters.**

### Example 3: The Testing Environment Gap

*B2B product, adoption, trial users converting to paid*

A B2B team had strong concept testing — usability scores high, task completion 91% in controlled testing. Stakeholders approved the build. The feature launched. **Six weeks post-launch, feature adoption was 12%.** Team had no explanation.

**Signals:**
- Proxy completion: 91% in controlled usability testing (By Stage — proxy)
- Production analytics: 12% feature adoption six weeks post-launch, concentrated in power users (By Stage — analytics)
- Time on task: users who attempted the feature took 4× longer than testing suggested (By Type — performance)
- Drop-off: 67% who started the feature abandoned at the same configuration step (By Stage — analytics)

**Lens application:** By Stage showed an immediate gap between proxy and analytics — the controlled environment had removed the conditions making the feature difficult. By Type confirmed the production performance signal was far worse than testing revealed.

**Named situation — Testing environment gap at configuration:**
- **Trigger:** Users encounter the feature with their own data and existing account structures the testing environment did not replicate
- **What users are trying to do:** Set up the feature and integrate it into an existing workflow
- **What stands in their way:** Configuration requires decisions about data structures that users cannot make without guidance they were not given
- **What success means:** Completing configuration without needing to leave the product to find answers

**Near-miss:** *Initial conclusion was "adoption is a communication problem — users do not know the feature exists."* Drop-off data from By Stage showed users were finding it but abandoning at a specific point. The fix was contextual guidance at configuration, not marketing. **Adoption reached 47% within six weeks.**

### Example 4: The Stakeholder Override Loop

*Enterprise product, decision and evaluation, cross-functional team*

A team had been running the same research cycle for three quarters. Usability findings were consistent. **The same friction point appeared in every study.** Design proposed a solution twice. Both times, stakeholders redirected the team toward higher-visibility features before the solution was built.

**Signals:**
- Usability findings: same friction point in four consecutive studies across different user segments (By Stage — proxy, repeated)
- Analytics: drop-off at the corresponding workflow step increased 18% over three quarters (By Time — lagging)
- Stakeholder decisions: two design proposals redirected to lower-priority status at review (Collecting — workflow observations)
- Contradictory framing: stakeholders consistently framed the friction point as "edge case behavior" despite signals showing it across segments (By Type — contradictory)

**Lens application:** By Time showed the analytics signal worsening steadily while the team cycled through the same loop. By Type showed contradictory signals — research consistently pointed to a real friction condition while stakeholder framing dismissed it. **Two lenses converged on an organizational blind spot:** the decision loop itself was the situation.

**Named situation — Organizational blind spot, stakeholder override loop:**
- **Trigger:** A documented friction condition reaches stakeholder review without the organizational framing needed to compete with higher-visibility priorities
- **What the team is trying to do:** Move a well-evidenced design decision from proposal to implementation
- **What stands in their way:** The review process weights visibility and stakeholder intuition over documented user signal
- **What success means:** A friction condition supported by four studies and worsening analytics reaching implementation within one review cycle

**Near-miss:** *Initial conclusion was "this is a prioritization problem — the team needs to advocate more effectively."* Naming it as a situation shifted the frame from "convince stakeholders" to "the review process is creating an organizational blind spot." Team brought the situation statement and the By Time data to the next review. **Proposal approved and built within the quarter.**

### Common Traps

The most frequent ways teams misread signals and arrive at an observation instead of a situation.

| Trap | What it looks like | What to do instead |
|---|---|---|
| **Naming the symptom** | "Users are dropping off at step three" is an observation. The situation is the condition creating the drop-off | Apply By Type and By Stage. Look for the conditions surrounding the drop-off, not just the drop-off itself |
| **Trusting a single lens** | One lens showing a pattern feels convincing, especially with clean data. But a single lens is an observation, not a situation | Always apply at least two lenses. Look for convergence before naming |
| **Confusing testing with production** | Strong proxy results treated as proof. The gap between controlled testing and real-world conditions goes unexamined | Apply By Stage explicitly. Ask whether the conditions in testing match the conditions users actually face |
| **Treating satisfaction as retention** | High satisfaction scores used as evidence that the experience is working. Retention signals not checked | Apply By Engagement. Check whether satisfaction is connecting to return behavior |
| **Racing to solutions** | Signals visible, team jumps to design responses before the situation is named. Solution addresses a symptom instead of a condition | Use the situation strength checklist before moving to Measure |
| **Single-audience framing** | Situation named based on signals from one audience segment and assumed to apply broadly | Check whether the situation appears across at least two audience segments before naming |

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-26 -->

## When to use

- When the user is trying to understand recurring conditions behind their signals — not isolated metrics.
- When they mention the **four lenses** (By Type, By Time, By Stage, By Engagement) or the **Observe → Interpret → Name cadence**.
- When the user is drafting a situation statement (Situation Name + 4-part structure + lenses applied + evidence).
- When they're applying the **9 named situation types** (Comprehension breakdown, Trust gap, Effort mismatch, Relevance failure, Habit formation gap, Expectation mismatch, Decision loop, Organizational blind spot, Signal credibility breakdown).
- When the user has multiple signals and is trying to find convergence.
- When the user is debugging why a metric (drop-off, retention, satisfaction) means different things in different contexts.
- When the user is looking for the situational framing of a JTBD job statement — Situations is what comes after JTBD when real evidence converges.
- When the user is preparing a situation for stakeholder review.

**Don't use when** naming the underlying need (use `glare:define-user-needs`), defining who data comes from (use `glare:define-audience`), gathering the evidence (use `glare:define-collecting`), or picking specific UX metrics (use `glare:define-ux-metrics`).

**Note:** Situations replaces the deprecated `glare:define-patterns` skill. If the user mentions "patterns" in the Glare framework sense (recurring conditions), route here.

## Failure modes

- **Naming a symptom as a situation.** "Users drop off at step 3" is an observation. The situation is the condition creating the drop-off.
- **Trusting a single lens.** One lens is an observation. Two converging lenses is a situation. The whole point of the Techniques structure is convergence.
- **Confusing testing with production.** Strong proxy results treated as proof while By Stage isn't checked. The controlled testing environment often removes the conditions that make the feature difficult in real use.
- **Treating satisfaction as retention.** Two different things. Satisfied non-returners are a habit formation situation, not a satisfaction success.
- **Racing to solutions before the situation is named.** Design response without a stable situation statement addresses symptoms instead of conditions.
- **Single-audience framing.** Naming a situation from one audience segment and assuming it applies broadly. Cross-segment verification is required.
- **Collapsing multiple situations into one to reduce complexity.** Three concurrent conditions need three situation statements, not one composite. The Skill output contract enforces this — preserve them all.

<!-- /ADDED -->
