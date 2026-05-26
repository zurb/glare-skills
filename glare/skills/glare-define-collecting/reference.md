# Collecting — Reference

**Block:** Define · Collecting
**Template:** 7-doc (Overview · Techniques · Playbook · References · Decisions · Examples · Agent Operations) — rebuilt 2026-05-26 from v1.2 source docs
**Source last synced:** 2026-05-26

This file contains the **6 practitioner sections** of the Collecting block. The 7th — **Agent Operations** — is split into `agent-operations.md` because it's a runtime contract for AI Skills, not practitioner reference content. See `SKILL.md` for the file-loading order.

Sections sourced from Drive docs are marked `DERIVED`; sections added by the skill-builder (When to use, Failure modes) are marked `ADDED`.

v1.1 → v1.2 is a structural rev. The 12-technique catalog is now organized into **5 technique groups** (Navigation, Task, Comparison, Behavior, Feedback). The standard output of any Collecting workflow is now the **Collection Brief** (14 fields). The 11 named instruments (SUS, NPS, CES, SEQ, etc.) and 4 tool categories (Attitudinal, Behavioral, Performance, Specialized) have moved into a more navigable References structure with a 5-Design-Stack overlay (Website / Mobile App / Product / E-commerce / Marketing).

> **Heads up on downstream routing:** The Patterns block has been archived by Bryan. Situations replaces it. Where the source docs say "hand off to Patterns," route to **`glare-define-situations`** in the canonical marketplace.

---

<!-- DERIVED FROM: 1EVxEz0UXcGnRoHvb52Lk-7JMmnCLOKlCFFL9k6t7qrk — Glare | Define, Collecting, Overview v1.2 -->

## Overview

Every design decision needs something to stand on. Collecting is where that foundation gets built.

User Needs names what users are trying to do. Audience defines who you are learning from. **Collecting is the step that turns both into actual evidence — behavior observed, reactions captured, perceptions recorded.** Without it, the room fills with opinions. The loudest voice wins. Decisions get made on instinct instead of signal.

Collecting is the discipline that prevents that drift. It is not about gathering more data. It is about gathering **the right data, from the right people, at the right time** — and connecting it to the metrics and decisions that move work forward.

### The seven sections of this block

| Section | File | What it does |
|---|---|---|
| **Overview** | `reference.md` | What Collecting is, where it sits in Define, how it connects to User Needs, Audience, and Situations |
| **Techniques** | `reference.md` | The 12 collection techniques organized into 5 groups; when to use each; UX metrics they produce; pairing rules |
| **Playbook** | `reference.md` | The 5-step collection process; decision prompts; the Collection Brief; the Define → Capture → Connect cadence |
| **References** | `reference.md` | Research Stacks catalog; Tools 4-axis framework; named instruments; Design Stacks by context |
| **Examples** | `reference.md` | 5 worked situations with strong/weak versions; Near-Miss Pattern Library |
| **Decisions** | `reference.md` | Identify the situation, find the next step that reduces uncertainty |
| **Agent Operations** | `agent-operations.md` | How AI Skills behave operationally — routing, confidence, escalation, output contract, ambiguity |

### What Collecting solves

Most teams collect too much, too late, or for the wrong reasons. They fill dashboards no one reads or run interviews that sound insightful but never shape a decision. The result: more activity, less clarity.

Collecting with intent is different. It starts with a clear question, connects to a specific user need and business goal, and uses a method that produces a signal you can act on. The tension between what users need and what the business requires makes the right technique obvious.

**One signal can stop wasted effort. Ten can create confidence. A hundred can battle-test a strategy until it holds.**

### Four feedback types

Different feedback types serve different purposes. A strong collection approach mixes several so you can see the whole picture — what users do, think, feel, and say.

| Feedback Type | What it captures | Techniques and Tools |
|---|---|---|
| **View user data** | Behavior patterns and usage metrics | Analytics, clickstream, heatmaps |
| **See what users do** | Task flows and completion outcomes | Task success testing, first-click, tree testing, time on task |
| **Sense what users like** | Visual attention and emotional response | Desirability studies, emotion tagging, satisfaction surveys, post-task reflection |
| **Hear what users say** | Opinions, expectations, and reactions | Surveys, interviews, in-product prompts, video feedback |

**Pair at least two types on any collection effort.** Behavioral evidence tells you *what* happened. Attitudinal evidence tells you *why*.

### The Define → Capture → Connect cadence

Every collection effort in Glare follows the same rhythm:

- **Define.** Clarify what you need to learn and why. Pair the user need with the business goal. Write the hypothesis.
- **Capture.** Choose the right stack, approach, and technique. Run it lean. Collect observable behavior, perception, or performance.
- **Connect.** Share findings in the right format for the right audience. Show your sources. Link signals to UX metrics and decisions.

This cadence appears across all the "-ing" blocks in Glare. It creates a consistent path from curiosity to clarity and makes every collection effort traceable back to a decision.

### Three modes of learning

| Mode | When to use | Core question | What you get |
|---|---|---|---|
| **Exploratory** | Early discovery, before clear hypotheses | What should we be solving or improving? | Patterns, context, and unmet needs |
| **Evaluative** | Mid-cycle, once ideas or designs exist | Does this design work for users? | Clarity, comprehension, and usability signals |
| **Comparative** | Later, when choosing between options | Which version performs or communicates better? | Directional proof and confidence in a decision |

Modes define the *type* of learning. Stacks define *where* you collect it. Techniques define *how*.

### Proof in practice

A university team was stuck on a navigation decision. Meetings circled for weeks. Everyone had an opinion. Nothing moved.

The team defined their intent, paired it with a business goal around reducing support requests, and chose an Evaluative stack. They ran a preference test using Helio. Within hours, they had a signal: the hamburger menu improved usability by 14% and positive impressions by 41%.

**One technique, paired with the right metric, ended weeks of debate.** That is what Collecting does.

### Where Collecting sits in Define

Collecting is the third block in the Define area. User Needs and Audience tell you what to learn and who to learn it from. Collecting is how you actually go get it. **Situations** (formerly Patterns) is where those signals get synthesized into direction.

| Block | What it focuses on |
|---|---|
| User Needs | The motivations, expectations, and goals that drive behavior |
| Audience | The people and contexts you learn from |
| **Collecting** | Capturing behavior, perception, and reaction |
| Situations | Synthesizing signals into repeatable findings that guide decisions |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1aOi9vwu3nZe2Ri_4DAwQUHQp6RcmIb6R6v_T-t-Dm8c — Glare | Define, Collecting, Techniques v1.2 + techniques/ subfolder (11 per-technique pages, folder ID 131iQFlfwSviNaXhgfqd-bBDzjEnLHPL9) -->

## Techniques

Design debates often stall when teams argue opinions. **Techniques break that cycle.** They are the tactical moves that turn assumptions into signals you can trust.

Most teams already know the names — card sorting, first-click tests, usability studies. The problem is they run them as one-offs, disconnected from UX metrics. Findings sound interesting but rarely change a decision. **Glare fixes this by anchoring each technique to the metrics it produces.** That connection is what makes findings credible and decisions traceable.

Each named technique below has a deeper per-page in the Drive `techniques/` subfolder (folder ID `131iQFlfwSviNaXhgfqd-bBDzjEnLHPL9`) with examples and step-by-step instructions.

### How to choose a technique

Start with the mode, not the method.

| Mode | When | Technique groups to use |
|---|---|---|
| **Exploratory** | Early discovery, before clear hypotheses | Navigation, Feedback |
| **Evaluative** | Mid-cycle, testing ideas or designs | Task, Behavior |
| **Comparative** | Choosing between versions or directions | Comparison, Behavior |

Once the mode is clear, match the specific question to the technique that is built to answer it.

### Five-step usage discipline

Apply this to every technique:

- **Pick the metric first.** What do you want to measure — completion, comprehension, desirability?
- **Choose the technique.** Match the method to the metric, not the other way around.
- **Run lean.** Small samples often surface clear signals. Five users can reveal major friction.
- **Pair techniques.** Task Success plus Time on Task shows both whether users finish and how hard it felt.
- **Share signals.** Frame results in terms of the UX metric, not raw output.

### Navigation techniques

Reveal how users understand and move through information. Use when designing or auditing structure, labels, or taxonomy.

| Technique | What it measures | UX Metrics |
|---|---|---|
| **Card Sorting** | How users group and label content. Reveals mental models and expectations about information structure | Comprehension, Expectations |
| **Tree Testing** | Whether users can find content within a defined navigation structure, without visual design as a cue | Comprehension, Success Rate, Expectations |

### Task techniques

Measure whether users can complete specific goals. The most direct signal of whether a design works.

| Technique | What it measures | UX Metrics |
|---|---|---|
| **First Click Testing** | Whether users instinctively start a task in the right place. Correct first click predicts 87% task completion | Success Rate, Comprehension, Desirability |
| **Task Success Rate** | Whether users complete the intended task. Successful completions / total attempts | Completion, Comprehension, Drop-Off |
| **Time on Task** | How long users take to complete a task. Paired with Task Success Rate, reveals effort alongside completion | Efficiency, Success Rate |

### Comparison techniques

Measure which version, message, or direction performs better. Use when a decision between options needs proof, not preference.

| Technique | What it measures | UX Metrics |
|---|---|---|
| **A/B Testing** | Which of two live versions performs better on a single variable change | Conversion Rate, Bounce Rate, Engagement |
| **Multivariate Testing** | Which combination of page elements performs best together | CTR, Comprehension, Desirability |
| **Conversion Rate Analysis** | Whether users complete the goal action at the end of a defined funnel | Success Rate, Drop-Off, Desirability |

### Behavior techniques

Show what users actually do at scale. Reveal patterns that individual sessions miss but cannot explain the reasoning behind them.

| Technique | What it measures | UX Metrics |
|---|---|---|
| **Heatmaps** | Where users focus attention and click on a page. Reveals what draws engagement and what gets missed | Desirability, CTR, Comprehension |
| **Clickstream Analysis** | How users navigate through a multi-step flow, including where they detour, backtrack, or drop off | Drop-Off, Efficiency, Frequency |
| **Web Analytics** | Site-wide health and trends at scale. Reveals what is happening across the full experience over time | Session Duration, Bounce Rate, Conversion Rate |

### Feedback techniques

Capture what users say, feel, and perceive. The attitudinal layer that behavioral data alone cannot provide.

| Technique | What it measures | UX Metrics |
|---|---|---|
| **Surveys & Questionnaires** | What users think, feel, and expect at scale. Works across discovery, post-task, and longitudinal tracking | Usefulness, Satisfaction, Loyalty |
| **Eye Tracking** | Where users look, what they see first, and what they miss entirely. Reveals visual attention that click data cannot | Comprehension, Efficiency, Visual Attention |

### Traps to avoid

- **Running without a metric.** A card sort is just boxes unless it's tied to comprehension or usability.
- **One-and-done.** Techniques work best in layers. A single test rarely tells the whole story.
- **Overcomplicating sample sizes.** More participants do not always mean more signal. Match sample size to the confidence the decision requires.
- **Reporting raw counts.** A percentage is a signal. A list of observations is not.

### Quick checklist

- Did you start with a metric, not just a method?
- Did you choose the technique that matches your mode?
- Did you pair techniques where one alone is not enough?
- Did you run lean to keep speed?
- Did you report results as signals tied to a UX metric, not raw data?

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1LTpFv9_vtn82w3Jak0aOZWpQZwA3AQZVBHOld6q6wts — Glare | Define, Collecting, Playbook v1.2 -->

## Playbook

The Playbook provides the operational structure for Collecting — the inputs, five-step workflow, decision prompts, and output format that turn a vague research question into a structured signal ready for Situations.

Collecting begins in one of two places: a team has a question and needs to choose the right method, or a team has existing data and needs to structure it into a usable signal. **The Playbook covers both.**

### Inputs and entry points

| Input Type | Examples | Enter process at |
|---|---|---|
| A question to answer | "Why are users dropping off at checkout?" or "Does the new onboarding flow work?" | **Step 1** — Start with Intent |
| Existing behavioral data | Analytics exports, clickstream reports, heatmap captures, session recordings | **Step 2** — Choose Your Stack |
| Existing attitudinal data | Survey results, NPS responses, in-product feedback, interview notes | **Step 2** — Choose Your Stack |
| A design or prototype to test | Wireframe, mockup, live feature, or redesigned flow | **Step 3** — Identify the Approach |
| Raw unstructured signals | Support tickets, forum posts, app store reviews, sales call notes | **Step 1** — Start with Intent |
| A completed study | Helio study results, UserTesting session, Maze test output | **Step 5** — Connect and Ready Your Data |

If the input is raw unstructured data without a clear question attached, start at Step 1 to establish intent before interpreting the data.

### The Five-Step Workflow

Complete each step before moving to the next. **The most common failure mode is skipping Step 1 and opening a tool before intent is established.**

#### Step 1 — Start with Intent

- **Purpose:** Pair the user need with a business goal to establish what data actually matters. Without intent, the right technique is impossible to identify.
- **Prompts:** What user need is this connected to? What business goal does this impact — adoption, engagement, retention, satisfaction? What's the hypothesis? What would change if the hypothesis is confirmed? If not?
- **Output:** A written hypothesis and a paired user need + business goal. *If these cannot be stated, stop and return to User Needs.*
- **Trap:** Skipping this step and choosing a tool first. Tools are infrastructure. Intent is the decision.

#### Step 2 — Choose Your Stack

- **Purpose:** Determine the mode of learning and the stack type that matches the current stage of the work.
- **Prompts:** Is the team exploring, evaluating, or comparing? Research Stack (established frameworks) or Design Stack (measuring a real concept in context)? Which Design Stack: Website, Mobile App, Product, E-commerce, or Marketing? Does the audience definition from Audience clearly identify who will be studied?
- **Output:** A named mode and stack type. *If the audience is not defined, pause and resolve Audience first.*
- **Trap:** Selecting a stack based on familiarity or tool availability rather than the mode the work actually requires.

#### Step 3 — Identify the Approach

- **Purpose:** Confirm that the question is testable — reveals a knowledge gap, points to observable evidence, can be measured.
- **Prompts:** Does the question reveal something the team does not yet know? Can the answer be observed in behavior or perception? Will the result change what the team does next? Is the approach Exploring, Evaluating, or Comparing?
- **Output:** A confirmed testable question and a named approach. *If the question cannot be answered with observable evidence, rewrite it before selecting a technique.*
- **Trap:** Proceeding with a question that is too broad ("What do users think of the app?") or too narrow ("Do users notice the blue button?").

#### Step 4 — Apply the Techniques

- **Purpose:** Match the technique to the approach and connect it to the UX metrics that will show movement.
- **Prompts:** Which technique matches this approach? Which UX metrics will it produce? What sample size? Should techniques be paired? Are at least two feedback types represented? Which tool, and is it available at the required speed and fidelity?
- **Output:** A named technique (or pair), the UX metrics it will produce, the sample size, and the tool. Document in the Collection Brief.
- **Trap:** Choosing a technique because it's familiar rather than because it matches the question. Running a single technique type without an attitudinal pair.

#### Step 5 — Connect and Ready Your Data

- **Purpose:** Share findings at the right level, document sources clearly, and connect signals back to UX metrics and decisions.
- **Prompts:** Who needs to see these findings? Are sources documented (technique, audience, metrics)? Are results expressed as signals tied to UX metrics, not raw counts? Have findings been posted where they can accumulate with future studies? Does this data answer the hypothesis from Step 1, or generate a new question?
- **Output:** A shared finding that includes technique used, audience studied, metrics measured, and signal produced. If the hypothesis is not resolved, document what was learned and what still needs to be answered.
- **Trap:** Sharing a deck of screenshots without sources. Treating a single study as conclusive. Letting findings sit in a tool no one else can access.

### The Collection Brief

The output format for Collecting. Captures everything Situations needs to interpret findings and everything a Skill needs to evaluate whether the effort was complete. Fill it out as you move through the five steps.

| Field | What to document | Comes from |
|---|---|---|
| **User Need** | The need this collection effort is connected to | User Needs block |
| **Business Goal** | The business outcome this effort is expected to impact | Step 1 |
| **Hypothesis** | The specific assumption being tested or explored | Step 1 |
| **Audience** | Who will be studied. Source type and credibility level | Audience block |
| **Mode** | Exploratory, Evaluative, or Comparative | Step 2 |
| **Stack** | Research Stack or Design Stack. Named stack if Design | Step 2 |
| **Approach** | Exploring, Evaluating, or Comparing. Testable question confirmed | Step 3 |
| **Technique(s)** | Named technique or pair. Sample size | Step 4 |
| **Tool(s)** | Platform used to capture data | Step 4 |
| **UX Metrics** | The metrics this effort will produce | Step 4 |
| **Feedback Types** | Which of the four types are covered: View, See, Sense, Hear | Step 4 |
| **Sharing Level** | Project-level, cross-team, or leadership rollup | Step 5 |
| **Signal Produced** | What the data showed, expressed as a UX metric signal | Step 5 |
| **Hypothesis Resolved?** | Confirmed, refuted, or still open. If open, what is the next question? | Step 5 |

A Collection Brief that reaches Situations with all fields complete gives Situations a structured signal. A brief missing intent, audience, or metrics leaves Situations with raw data it cannot reliably interpret.

### Show Your Sources

Every shared finding must include three things: **the technique used, the audience studied, and the metrics measured.** This is the minimum for a finding to be credible to people who were not in the room.

Example: *"Task success rate from a Helio usability test with 100 mobile app users, measuring Completion and Comprehension."*

Without sources, findings become opinions. With sources, they become signals.

### Handoff Contract

| Condition | Action | Goes to |
|---|---|---|
| Collection Brief is complete. Signal is documented | Hand off the brief and findings | **Situations** (formerly Patterns) |
| Intent cannot be established — no clear user need or business goal | Stop. Establish intent before collecting | User Needs |
| Audience is not defined or credibility is too low for the decision | Stop. Resolve audience before collecting | Audience |
| Question is not testable — too broad or not observable | Rewrite the question before selecting a technique | Step 3 |
| Findings generate a new question rather than resolving the hypothesis | Document what was learned. Start a new Collection Brief | Step 1 |
| Data is collected but sources are not documented | Do not share. Document technique, audience, and metrics first | Step 5 |

### Quick checklist (before sharing any findings)

- Is the user need and business goal documented?
- Is the hypothesis stated clearly?
- Is the audience defined with source and credibility level?
- Is the mode, stack, and approach named?
- Are the technique, tool, sample size, and UX metrics documented?
- Are at least two feedback types represented?
- Are findings expressed as signals tied to UX metrics, not raw data?
- Are sources visible to everyone who will see the findings?
- Is the hypothesis resolved, or is the next question documented?

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1y1EAqBw_HeoRRT4UrStJ1CRqw1ZKmHRS3DfVktxCPGI — Glare | Define, Collecting, References v1.2 + references/ subfolder (Research Stacks, Tools, folder ID 1MhJY427fy5k4viRJFDkITOTH_weRYq5g) -->

## References

Definitions, catalogs, and lookup tables for Research Stacks, Tools, and Design Stacks. Use this section to identify the right instrument, platform, or context for a collection effort.

### Research Stacks

Align established methods with the UX metrics they produce. Answer: given the type of decision, which instruments give you data you can actually act on?

| Stack Type | When to use | Maps to |
|---|---|---|
| **Exploratory** | Early discovery before clear hypotheses. Surface needs, opportunities, emotional context | Attitudinal metrics: Satisfaction, Usefulness, Feeling, Trust |
| **Evaluative** | Mid-cycle testing of designs, flows, or content. Confirm whether users can succeed | Behavioral and performance metrics: Completion, Usability, Efficiency, Comprehension |
| **Comparative** | Choosing between versions or directions. Prove which option performs better | Outcome metrics: Preference, Engagement, Conversion, Loyalty |

#### Usability & Ease

| Instrument | What it measures | UX Metrics |
|---|---|---|
| **SUS** (System Usability Scale) | Overall ease of use and learnability across a system | Usability, Engagement, Usefulness |
| **SEQ** (Single Ease Question) | Single-question post-task difficulty on a 7-point scale. Scores below 5 signal friction | Completion, Success, Satisfaction |
| **PURE** (Practical Usability Rating by Experts) | Expert-rated task difficulty without live participants | Completion, Satisfaction, Feeling |
| **SUMI** (Software Usability Measurement Inventory) | Efficiency, control, and learnability across software interfaces | Completion, Usability, Satisfaction |

#### Effort & Workload

| Instrument | What it measures | UX Metrics |
|---|---|---|
| **CES** (Customer Effort Score) | How much effort users feel they expended to complete a task | Completion, Effort |
| **CASTLE** | Cognitive task load and interface efficiency | Task Load, Efficiency, Usability, Comprehension |
| **NASA-TLX** | Multi-dimensional cognitive and physical workload across six dimensions | Usability, Usefulness, Feeling, Satisfaction |

#### Satisfaction & Experience

| Instrument | What it measures | UX Metrics |
|---|---|---|
| **WAMMI** (Website Analysis and Measurement Inventory) | Website satisfaction across attractiveness, controllability, helpfulness, learnability | Appeal, Usability, Helpfulness, Comprehension |
| **PSSUQ** (Post-Study System Usability Questionnaire) | Post-task satisfaction across system usefulness, information quality, interface quality | Engagement, Usability, Usefulness, Feeling |
| **QUIS** (Questionnaire for User Interface Satisfaction) | Overall interface satisfaction across multiple dimensions | Engagement, Usability, Satisfaction |
| **UEQ** (User Experience Questionnaire) | Emotional and pragmatic experience quality | Usability, Sentiment, Reaction, Loyalty |
| **UX-Lite** | Quick two-question UX snapshot for fast-cycle testing | Usefulness |
| **SUPR-Q** (Standardized User Experience Percentile Rank Questionnaire) | Website benchmarking across usability, trust, loyalty, appearance | Usability, Loyalty, Sentiment, Reaction |

#### Trust & Loyalty

| Instrument | What it measures | UX Metrics |
|---|---|---|
| **NPS** (Net Promoter Score) | Likelihood to recommend. A leading indicator of retention and loyalty | Loyalty |
| **L-DERLY** | Learnability and the gap between user expectations and actual system behavior | Expectations, Usability, Usefulness, Comprehension |

#### How to use Research Stacks

- **Start with the decision type.** Exploratory, evaluative, or comparative.
- **Choose the instrument that matches.** Do not run SUS when you need NPS, or NPS when you need task completion.
- **Map to Glare UX metrics.** Align the instrument output to the metric it produces, not the score it generates.
- **Pair stacks when one is not enough.** Exploratory interviews to surface needs, then evaluative SUS to validate fixes.
- **Share as signals, not scores.** A SUS score of 68 is less useful than "usability is below benchmark for this task group."

### Tools

Tools are the platforms that capture UX metrics. Choose them based on the metric you need, not based on familiarity or availability.

| Feedback Type | What it captures | Tool category |
|---|---|---|
| View user data | Behavior patterns, usage trends, funnel performance | Behavioral Tools |
| See what users do | Task flows, recordings, heatmaps, navigation paths | Behavioral / Performance Tools |
| Sense what users like | Visual attention, desirability, emotional response | Attitudinal / Specialized Tools |
| Hear what users say | Opinions, satisfaction, expectations, open-ended feedback | Attitudinal Tools |

#### Attitudinal Tools — *capture what users say, feel, or prefer*

- **Surveys:** Typeform, SurveyMonkey, Qualtrics
- **In-product feedback:** Sprig, Delighted, Qualaroo
- **Preference testing:** UsabilityHub, Helio
- **Benchmarking surveys:** NPS, CES, CSAT
- **Aligned Metrics:** Satisfaction, Trust, Desirability, Sentiment, Brand Score

#### Behavioral Tools — *show what users actually do*

- **Analytics suites:** Google Analytics, Mixpanel, Amplitude
- **Session replay & heatmaps:** Hotjar, FullStory, CrazyEgg, Smartlook
- **Clickstream tracking:** Pendo, Heap
- **Navigation testing:** Treejack, Optimal Workshop
- **Aligned Metrics:** Completion Rate, Engagement, Navigation Paths, Usability

#### Performance Tools — *measure efficiency, accuracy, and reliability*

- **Usability testing platforms:** UserTesting, Maze, UserZoom
- **A/B & multivariate testing:** Optimizely, VWO, Google Optimize
- **Task timing & error tracking:** Helio task flows, Lookback
- **System performance monitoring:** Pingdom, New Relic, Load Impact
- **Aligned Metrics:** Time on Task, Error Rate, Drop-Off, Task Success

#### Specialized Tools — *advanced or niche research methods*

- **Eye tracking:** Tobii, RealEye
- **Biometrics & emotion tracking:** iMotions, Affectiva
- **Privacy-first analytics:** Fathom, Plausible
- **Emerging methods:** AR/VR usability platforms, AI-driven sentiment analysis
- **Aligned Metrics:** Attention, Emotional Response, Advanced Trust or Performance Signals

#### How to choose a tool

- **Start with the metric.** Define what you need to measure before opening any platform.
- **Match the tool to the metric.** Surveys for sentiment. Usability platforms for task success. Analytics for adoption trends.
- **Pair tools.** A survey plus a heatmap reveals both what users say and where they actually click.
- **Stay lean.** Too many tools fragment the story. Choose the minimum needed to answer the question.
- **Avoid over-reliance on one type.** Analytics without attitudinal data tells you what happened, not why.

### Design Stacks

The five contextual layers where real concepts get measured. Unlike Research Stacks (reference instruments), Design Stacks define the part of the experience you are collecting data from.

| Design Stack | Focus Area | Concept Examples | Common Metrics |
|---|---|---|---|
| **Website** | Information architecture, messaging, and conversion paths | Homepages, pricing pages, signup flows, landing pages | Comprehension, Conversion Rate, Bounce Rate, Desirability |
| **Mobile App** | Core interactions and task flows on small screens | Onboarding, task completion, push notifications, in-app navigation | Completion, Time on Task, Usability, Engagement |
| **Product** | Functional clarity and feature engagement inside a product | Dashboards, filters, search, account management, settings | Efficiency, Usability, Drop-Off, Comprehension |
| **E-commerce** | Purchase confidence and payment clarity | Product pages, cart, checkout flows, recommendations | Conversion Rate, Drop-Off, Trust, Desirability |
| **Marketing** | Communication clarity and emotional appeal | Headlines, visuals, ad creatives, CTAs, email campaigns | Desirability, CTR, Satisfaction, Engagement |

#### How to use Design Stacks

- **Identify which stack the work lives in.** A checkout redesign is E-commerce. A dashboard improvement is Product.
- **Use the stack to focus the technique choice.** Mobile App work favors task-based evaluative techniques. Marketing work favors preference and desirability testing.
- **Combine with a Research Stack when needed.** Exploratory interviews (Research Stack) to surface needs, then an E-commerce Design Stack test to evaluate the fix.
- **Connect findings to the stack context.** A 72% task success rate means different things on a Product dashboard versus a Mobile App onboarding flow.

### Per-Technique Pages

The Drive `techniques/` subfolder (folder ID `131iQFlfwSviNaXhgfqd-bBDzjEnLHPL9`) contains deep-dive pages for 11 named techniques: Card Sorting, Tree Testing, First Click Testing, Task Success Rate, Time on Task, A/B Testing, Multivariate Testing, Conversion Rate Analysis, Heatmaps, Clickstream Analysis, Web Analytics, Surveys, Eye Tracking. Reach for those when a team needs step-by-step instructions for a specific technique.

### Key Terms

| Term | Definition |
|---|---|
| **Research Stack** | A category of research instruments aligned to a specific type of UX metric. Organized by decision type: Exploratory, Evaluative, or Comparative |
| **Design Stack** | The contextual layer of the product or experience being measured. Five types: Website, Mobile App, Product, E-commerce, Marketing |
| **Three Modes of Learning** | Exploratory (what to solve), Evaluative (does this work), Comparative (which is better). Modes determine which stack and technique apply |
| **Define → Capture → Connect** | The cadence all Collecting efforts follow. Define intent, capture signal, connect findings to metrics and decisions |
| **Feedback Types** | Four lenses for collection: View user data (analytics), See what users do (recordings/heatmaps), Sense what users like (eye tracking/appeal), Hear what users say (surveys/interviews) |
| **Collection Brief** | The output format for a completed collection effort. Contains intent, audience, mode, technique, metrics, and signal produced. See Playbook |
| **Design Signal** | What data becomes when patterns make sense. The moment evidence becomes direction |
| **Show Your Sources** | The requirement to document technique, audience, and metrics in every shared finding. Without sources, findings are opinions |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 11gGTw6Ya5SpyqVY8XPhe5UuGi6g_1touyfwV3VHz6RU — Glare | Define, Collecting, Decisions v1.2 -->

## Decisions

Decisions helps teams recognize their situation inside the Collecting block and identify the most useful next move. The goal is not to produce perfect collection plans — it is to take the step that reduces the most uncertainty given what is currently known.

Most Collecting decisions hinge on three questions: **Is intent established? Is the collection effort structured correctly? Are findings ready to hand off?** The routing tables below map common situations to specific next steps.

### Primary Routing Table

| Situation | What it signals | Next step | Goes to |
|---|---|---|---|
| A question exists, a user need is identified, an audience is defined | Intent is established. Collecting can begin | Enter Step 1. Write the hypothesis. Choose the stack | Playbook — Step 1 |
| Existing data is available but no hypothesis has been written | The data has value but no framing. Without intent, it cannot be interpreted as a signal | Write the hypothesis first. Identify the user need and business goal. Re-enter the Playbook at the appropriate step | Playbook — Step 1 |
| A technique has been chosen but the question has not been confirmed as testable | Step 3 was skipped. The question may be too broad, not observable, or unable to change what happens next | Return to Step 3. Confirm the question reveals a knowledge gap, points to observable behavior, and can be measured | Playbook — Step 3 |
| A collection effort is complete but findings have not been documented with sources | The signal is real but not defensible. Without technique, audience, and metrics, findings cannot be shared | Complete the Collection Brief before sharing. Apply the Show Your Sources rule | Playbook — Step 5 |
| A collection effort produced a clear signal tied to a UX metric. The Brief is complete | Collecting is done. The signal is ready to enter Situations | Hand off the Collection Brief and findings | **Situations** |
| The effort raised a new question rather than resolving the hypothesis | The Hunch was directional, not conclusive. The new question is the next unit of work | Document what was learned. Start a new Collection Brief for the new question. Re-enter at Step 1 | Playbook — Step 1 |
| No user need has been identified | Collecting without a user need produces data, not signals. The Define chain is broken | Stop. Return to User Needs. Identify the need before choosing a method | User Needs |
| Audience is not defined, or audience credibility is too low for the decision | Collecting without a defined audience produces ungrouped data that Situations cannot interpret | Stop. Return to Audience. Resolve the definition before collecting | Audience |
| Multiple collection efforts exist on the same topic with different techniques, audiences, or metrics | Fragmented collection. Findings cannot be compared or accumulated. Each effort is isolated | Align on a shared user need, audience definition, and metric stack. Reframe efforts under a common Collection Brief structure | Playbook — Step 1, then Situations |

### Collection Readiness Guide

Use this guide when it is unclear whether a collection effort is ready to run. **Each row represents a minimum condition. If any row shows "No," the effort is not ready.**

| Condition | If No — do this first |
|---|---|
| A user need is identified and named | Return to User Needs |
| A business goal is paired to the user need | Write the business goal. Connect it to a measurable outcome |
| A hypothesis is written | Write the hypothesis before opening any tool |
| An audience is defined with source type and credibility level | Return to Audience |
| The question is confirmed as testable (observable, measurable, decision-changing) | Rewrite the question using Step 3 criteria |
| A mode is named: Exploratory, Evaluative, or Comparative | Identify the mode before selecting a technique |
| A technique is chosen that matches the mode | Use the Techniques section to select the right method |
| At least two feedback types are represented | Add a second technique from a different feedback type |
| UX metrics are named that the technique will produce | Connect each technique to its UX metrics before running |

### Step-Level Decision Guide

Use when a collection effort is in progress and a specific step feels unclear or stuck.

| If the team is stuck here… | The most likely issue is… | The decision is… |
|---|---|---|
| **Step 1** — Cannot write a hypothesis | No user need or business goal has been identified. The team is collecting for general awareness, not a decision | Stop collecting. Return to User Needs. A hypothesis cannot be written without a need to ground it |
| **Step 2** — Cannot choose a stack | The mode is unclear. The team does not know if they are exploring, evaluating, or comparing | Identify the mode first. The mode determines the stack. If the mode is genuinely unclear, default to Exploratory and narrow from there |
| **Step 3** — Cannot confirm the question is testable | The question is too broad or describes a feeling rather than an observable behavior | Rewrite the question to name a specific behavior in a specific context. Test it against the three criteria: knowledge gap, observable evidence, measurable result |
| **Step 4** — Cannot choose between two techniques | Both techniques seem relevant but the team is not sure which produces the right signal | Match each technique to its UX metric. Choose the technique whose metric answers the hypothesis. If both are needed, pair them |
| **Step 5** — Cannot agree on how to frame the finding | Results are being shared as raw data or session observations rather than as a signal tied to a metric | Restate the finding as a UX metric result. Name the technique, audience, metric, and what the data showed. If this cannot be done, the collection was not connected to a metric at Step 4 |

### Cross-Block Routing

| Situation | Route to | Why |
|---|---|---|
| No user need is identified. The team cannot write a hypothesis | User Needs | Collecting requires a need to orient the effort. Without one, any technique chosen is arbitrary |
| The audience is undefined, or the source credibility is insufficient | Audience | Situations cannot interpret findings that are not tied to a defined group |
| The collection effort confirms a signal. The signal needs to be interpreted against a pattern | **Situations** | Receives completed Collection Briefs and interprets signals across multiple efforts |
| The effort surfaces a finding that challenges the current roadmap or strategy | Stakeholders / Leadership | Design findings with strategic implications need to be surfaced. Collecting can document the signal but cannot resolve the strategic question |
| A validated signal is ready to move toward measurement and concept testing | Measure | Once Situations confirms a signal, the work moves out of Define toward Measure. Collecting does not initiate that move — Situations does |
| The hypothesis cannot be confirmed with behavioral data, only attitudinal, and the decision requires behavioral evidence | Techniques — re-evaluate method | Attitudinal signals alone are insufficient for behavioral decisions. A different technique is needed before the effort can produce a defensible signal |

### Signals that Collecting is complete

- **The Collection Brief is fully completed.** All 14 fields documented
- **The finding is expressed as a signal tied to a UX metric.** Not "users struggled with Step 4" but "58% task success at the payment step, measuring Completion and Comprehension, Helio usability test, 30 new users"
- **Sources are documented.** Technique, audience, and metrics are visible to anyone who will read the finding
- **The hypothesis is resolved or the next question is named.** Confirmed, refuted, or open — all valid. What is not valid is a finding with no position on the hypothesis
- **The finding is shared at the right level.** Project-level, cross-team, or leadership rollup
- **At least two feedback types were used.** Behavioral and attitudinal signals are both present

Collecting does not need to be exhaustive to be complete. It needs to be **structured enough that Situations has a signal to work with and a question to evaluate it against.**

### What Decisions doesn't resolve

- **Which user need to investigate.** That's a User Needs decision, made before Collecting begins
- **Which audience segment to prioritize when multiple are valid.** That's an Audience decision
- **Whether a signal is strong enough to act on.** That's a Situations decision
- **Which Measure concept applies to a validated finding.** Collecting points toward Situations; Situations points toward Measure
- **Whether the product should change based on what was found.** Collecting surfaces evidence; product decisions belong to the teams responsible

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1y2AGbaWxUHVcSlfLAlHvBCAfWKJH4NfNm8m7Js1Oo50 — Glare | Define, Collecting, Examples v1.2 -->

## Examples

These examples show Collecting in practice — how teams identify the right method, avoid common traps, and produce signals that move decisions forward. Each includes the situation, the Hunch, a **strong version** showing the right approach, and a **near-miss version** showing where teams typically go wrong.

### Example 1 — The Question That Looked Testable

*Mode: Evaluative · Technique: Task Success Rate · Trap: Untestable question · Stack: Product*

**Context:** A B2B SaaS team redesigned their dashboard filter system after complaints that users couldn't find what they were looking for. They want to validate the redesign before shipping.

- **User Need:** Useful — users need the product to surface relevant information without manual effort
- **Business Goal:** Reduce support tickets related to data visibility by 30% this quarter
- **Audience:** Power users of the analytics dashboard. Helio panel, high credibility
- **Existing Data:** 12 support tickets flagging filter confusion in past 30 days. No prior usability study
- **Hunch:** The redesigned filter system will be easier to use than the original, reducing the time users spend finding their target data set

**✓ Strong version:** Team writes a testable question — "Can users locate a specific data set using the new filter system in under 90 seconds?" Chooses Task Success Rate paired with Time on Task (Evaluative, Product stack). 20 power users. Results: 85% task success, average 72 seconds. Complete Collection Brief. Situations receives a structured finding. The result confirms the redesign is functional — Situations evaluates whether to ship or run a second round on edge cases.

**✕ Near-Miss version:** Team writes question as "Do users like the new filter design better?" Runs a 5-point preference survey. 78% positive. **Why it fails:** The question is not testable in the Glare sense — it captures preference, not observable behavior. The 78% satisfaction cannot connect to the support ticket goal. Step 3 was skipped.

### Example 2 — Collecting Before the Question Exists

*Mode: Exploratory · Technique: Surveys · Trap: No intent established · Stack: Mobile App*

**Context:** A fintech mobile app team is preparing for a quarterly planning cycle. Leadership wants "user research to inform the roadmap." Team is not sure what to study.

- **User Need:** Not yet identified
- **Business Goal:** Stated as "improve the app" — no specific metric defined
- **Audience:** Existing app users. No segment defined
- **Existing Data:** App store reviews (mixed). NPS of 32
- **Hunch:** Not yet formed

**✓ Strong version:** Team recognizes they are missing Step 1. Returns to User Needs. After clustering app store review language, they surface a Hunch — users feel the app is not helping them act on the information it shows (need = Useful). With a Hunch, they return to Collecting. Hypothesis: "Users open the app frequently but do not complete any goal-oriented action during the session." Exploratory stack — short survey paired with session analytics. Audience defined as habitual users (weekly active, 90+ days). Brief completed. Effort enters Situations with structured inputs.

**✕ Near-Miss version:** Team sends a broad survey: "What features would you like to see improved?" 340 responses. Results: a list of feature requests with no pattern and no metric attached. Leadership picks the most-mentioned items, adds them to the roadmap. **Why it fails:** Skipped Step 1 entirely. No user need identified. No hypothesis. No UX metric. The survey produced requests, not signals. Findings cannot connect to NPS, retention, or any measurable outcome.

### Example 3 — Comparing When You Should Be Evaluating

*Mode: Comparative vs. Evaluative · Technique: A/B Testing · Trap: Wrong mode for the stage · Stack: E-commerce*

**Context:** An e-commerce team is redesigning checkout after a drop in conversion. They have two design directions and want to know which performs better.

- **User Need:** Confident — users need to feel certain that completing the purchase is safe and correct
- **Business Goal:** Recover 8% of checkout conversion lost over past two months
- **Audience:** Returning customers, 30–55, desktop-primary. CRM segment, behavioral attributes only — Medium credibility
- **Existing Data:** Conversion dropped from 74% → 66% following a UI update. No usability study on either design
- **Hunch:** Users are abandoning at the payment step due to clarity and trust issues, not the overall flow structure

**✓ Strong version:** Team recognizes that neither design has been validated as usable. Running A/B on unvalidated designs risks amplifying the problem. They step back to Evaluative mode — run Task Success Rate on the current checkout with 30 users, measuring Completion and Comprehension at the payment step. Results: 61% task success at the payment step, most failures at CVV and billing address. **Comprehension is the issue, not trust.** With the usability problem located, they redesign the payment step specifically and A/B test only the payment screen. Brief documents the two-stage approach.

**✕ Near-Miss version:** Team runs A/B immediately across the full checkout. Version B wins by 3 percentage points over four weeks. Ship B. Conversion recovers slightly but not to 74%. Team does not know why. **Why it fails:** Comparative mode applied before either design was validated for usability. A/B tells you which version performs better, not whether either works. The underlying Comprehension failure at the payment step persisted into Version B. Step 3 was skipped.

### Example 4 — The Analytics Trap

*Mode: Behavioral · Technique: Web Analytics + Heatmaps · Trap: No attitudinal pair · Stack: Website*

**Context:** A SaaS marketing team notices that pricing page traffic is high but conversion to free trial is low.

- **User Need:** Confident — users need to understand what they are signing up for and trust the pricing is fair
- **Business Goal:** Increase free trial starts from the pricing page by 15% this quarter
- **Audience:** Prospective buyers, mid-market B2B, first visit, desktop. Google Analytics segment — Medium credibility
- **Existing Data:** 18,000 visits/month. Free trial conversion 2.1%. Bounce 64%. Heatmap data available
- **Hunch:** Visitors are not converting because the pricing page is not communicating value clearly enough to support a trial decision

**✓ Strong version:** Heatmap shows most users do not scroll past pricing tiers to the FAQ. Click patterns cluster on plan names, not feature lists. Team pairs behavioral data with a one-question exit survey ("What stopped you from starting a free trial today?") using Sprig for two weeks. Results: 41% of respondents cite confusion about what is included in each plan. **Behavioral data showed where attention went. Attitudinal data explains why conversion did not follow.** Brief documents both techniques, both feedback types (View + Hear), combined signal: Comprehension failure at the plan differentiation layer.

**✕ Near-Miss version:** Team reviews heatmap, sees low scroll depth, concludes the page is too long, redesigns shorter with CTA higher. After launch, conversion improves 0.4 percentage points — within noise. Team cannot tell if the change helped. **Why it fails:** Acted on a single behavioral signal without an attitudinal pair. Heatmaps show *where* attention goes, not *why* conversion does not follow. The four-feedback-types rule exists precisely to prevent this.

### Example 5 — Findings Without Sources

*Mode: Evaluative · Technique: Usability Test · Trap: Sources not documented · Stack: Product*

**Context:** A product team completed a usability study on a new onboarding flow two weeks ago. A designer is presenting to the product director to get approval for the next iteration.

- **User Need:** Confident — users need to understand what the product does and feel ready to use it
- **Business Goal:** Improve 7-day activation from 54% to 70%
- **Audience:** New paying users, first week. Helio panel — High credibility
- **Existing Data:** Usability study completed. Task success measured. Findings in a slide deck. **Sources not recorded in the deck**
- **Hunch:** New users are not completing onboarding because two steps require information they do not have ready

**✓ Strong version:** Before the presentation, designer completes the Collection Brief — Task Success Rate from a Helio usability study, 40 new paying users, measuring Completion and Comprehension. Finding restated as a signal: "58% task success at the API key setup step, with 34% of failures occurring because users did not have their API key accessible during onboarding. **Comprehension was not the issue — task readiness was.**" Director can trace the finding, understand the sample, connect to the 7-day activation goal.

**✕ Near-Miss version:** Deck shows screenshots and a slide saying "Users struggled with Step 4." No sample size, technique, or metric listed. Director asks: "How many users? Was this representative?" Designer cannot answer precisely. Session inconclusive. Iteration delayed pending "more research." **Why it fails:** Step 5 was incomplete. Without technique, audience, and metrics, the finding cannot be defended. **The Show Your Sources rule is not bureaucracy — it is what separates a signal from an opinion in the room.**

### Near-Miss Pattern Library

The most common collection failures across all modes and stages. Each has a recognizable signal a team or Skill can detect *before* the effort runs.

| Pattern | What it looks like | What it signals | Corrective step |
|---|---|---|---|
| **Tool before intent** | Team opens Helio, GA, or a survey builder before writing a hypothesis | Step 1 was skipped. No user need or business goal paired to the effort | Return to Step 1. Write the hypothesis first. Choose the tool last |
| **Question too broad** | "What do users think of the app?" or "What should we improve?" | Question doesn't reveal a knowledge gap and cannot be measured. Results will be feature requests, not signals | Rewrite to target a specific behavior or perception in a specific context |
| **Single feedback type** | Only analytics, or only a survey, with no pairing | Behavioral data without attitudinal context tells you what but not why. Attitudinal alone may not reflect actual behavior | Add a second technique from a different feedback type. Pair View with Hear, or See with Sense |
| **Comparative mode too early** | A/B launched on a design that has not been evaluated for usability | Comparative requires both versions to be functional. Testing broken designs against each other produces a false winner | Run Evaluative first. Validate that the design works before testing which version works better |
| **Sources missing from the finding** | "Users struggled with X" with no technique, sample, or metric cited | The finding cannot be defended, built on, or accumulated. It is an opinion, not a signal | Complete the Collection Brief before sharing |
| **One-and-done research** | A single study is treated as conclusive. No follow-up planned | A single technique at a single moment is directional, not definitive. Situations requires accumulation across multiple signals | Document what the study answered and what it did not. Identify the next question. Plan the next effort |

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-26 -->

## When to use

- When the user is moving from intent to evidence — pairing a user need with a business goal and choosing a method to capture signal.
- When the user mentions one of the **three modes** (Exploratory, Evaluative, Comparative) or the **five technique groups** (Navigation, Task, Comparison, Behavior, Feedback).
- When the user is picking among the 12 techniques (Card Sorting, Tree Testing, First Click, Task Success, Time on Task, A/B, Multivariate, Conversion Rate, Heatmaps, Clickstream, Web Analytics, Surveys, Eye Tracking).
- When the user is choosing between named instruments (SUS, NPS, SEQ, CES, PURE, SUMI, WAMMI, NASA-TLX, UEQ, SUPR-Q, etc.).
- When the user is building or completing a **Collection Brief**.
- When the user mentions one of the five **Design Stacks** (Website, Mobile App, Product, E-commerce, Marketing).
- When the user is applying the **Define → Capture → Connect** cadence or the **Four Feedback Types** (View / See / Sense / Hear) rule.
- When the user is debugging why a study produced no usable signal — usually Step 1 (intent) or Step 4 (technique-metric mismatch) or Step 5 (sources missing).

**Don't use when** naming the underlying need (`glare-define-user-needs`), defining who data comes from (`glare-define-audience`), or picking metrics (`glare-define-ux-metrics`).

## Failure modes

- **Tool before intent.** Opening Helio, GA, or a survey builder before writing a hypothesis. The #1 source of "we have a lot of data but no signal." Step 1 first, always.
- **Question too broad to be testable.** "What do users think of X?" is not a question — it's a survey topic. Rewrite to name a specific behavior in a specific context that observable evidence can confirm or refute.
- **Single feedback type.** Analytics without attitudinal data tells you *what* happened, not *why*. Surveys without behavioral data tell you what users *say*, not what they *do*. Pair at least two.
- **Comparative mode applied to unvalidated designs.** Running A/B on two versions before either has been evaluated for usability produces a false winner — the worse-comprehension version may still win on whatever variable is being tested while the underlying friction persists.
- **Sources missing from findings.** "Users struggled with X" without technique, sample, or metric is an opinion, not a signal. The Show Your Sources rule is the difference between a defensible finding and a forgotten one.
- **One-and-done research.** A single study at a single moment is directional, not definitive. Plan for accumulation across multiple efforts so Situations can interpret signals against each other.
- **Patterns confusion.** Source docs still reference "Patterns" as the downstream block. The Patterns block has been **archived by Bryan and replaced with Situations** (`glare-define-situations`). When routing, always use Situations.

<!-- /ADDED -->
