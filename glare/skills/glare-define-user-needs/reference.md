# User Needs — Reference

**Block:** Define · User Needs
**Template:** 6-doc (Overview · Techniques · Playbook · References · Decisions · Examples) — rebuilt 2026-05-22 from v1.4 source docs
**Source last synced:** 2026-05-22

This skill follows the 6-section block template Bryan established for User Needs in v1.4. The four original sections — Overview, Techniques, Playbook, References — were rev'd from v1.3 to v1.4. Two new sections — **Decisions** and **Examples** — were added. Sections sourced from Drive docs are marked `DERIVED`; sections added by the skill-builder (When to use, Failure modes) are marked `ADDED`.

---

<!-- DERIVED FROM: 1YBZeCMDzuYygl5F6iEvA6JTkLcjBgXXS85AjwO8iIS4 — Glare | Define, User Needs, Overview v1.4 -->

## Overview

User Needs help product and design teams understand what users are actually trying to accomplish and where experiences begin breaking down. Rather than treating research, UX metrics, usability findings, and feedback as disconnected signals, the framework helps organize recurring patterns into clearer, actionable understanding.

User needs act as operational anchors that help teams **interpret user behavior, evaluate workflows, guide measurement, compare concepts, and connect design decisions to business outcomes.**

### The six sections of this block

| Section | Purpose |
|---|---|
| **Overview** | Explains the core ideas, purpose, and role of User Needs inside the framework |
| **Techniques** | Covers needfinding methods, interpretation approaches, and ways of recognizing patterns |
| **Playbook** | Provides operational workflows, prompts, inputs, outputs, and execution guidance |
| **References** | Contains reusable definitions, behavioral examples, and per-need lookup material |
| **Examples** | Provides worked examples and a pattern library for practitioners and AI-assisted workflows |
| **Decisions** | Guides which next step to take based on evidence strength, friction type, and team context |

### Why teams get stuck without it

Teams have plenty of inputs — customer interviews, support tickets, usability findings, analytics, stakeholder requests, UX metrics, internal opinions. The challenge is figuring out what actually matters and connecting scattered data into a clearer understanding of:

- what users are trying to accomplish
- where friction is emerging
- why behavior keeps repeating
- what evidence supports the problem
- what decisions should happen next

A single usability issue rarely explains the full situation. A support request may point to a deeper trust problem. High engagement may hide confusion. Strong satisfaction scores may not mean users are succeeding.

### Move beyond surface feedback

User needs are rarely stated. They emerge through:

- repeated behavior · hesitation · confusion · workarounds · inconsistent decisions · recurring friction

The framework helps teams move from isolated observations toward structured understanding of behavior over time.

### Five Layers of User Needs

User needs are organized into five layers. Layers build on each other — foundational needs usually need to be supported before higher-level needs fully emerge — but they are not a rigid sequence. Most experiences contain several overlapping needs at once.

| Layer | Focus | User Needs |
|---|---|---|
| **Basics** | Foundational usability and access | Useful · Usable · Findable · Accessible |
| **Trust** | Reliability and confidence | Credible · Secure · Reliable · Intuitive |
| **Personal** | Relevance and contextual understanding | Inclusive · Adaptable · Connected · Insightful |
| **Impact** | Progress and meaningful outcomes | Valuable · Sustainable · Efficient · Scalable |
| **Feelings** | Emotion and long-term connection | Desirable · Delightful · Engaging · Empowering |

Examples of stacking:
- Users rarely trust workflows they do not understand
- Users struggle to feel confident in experiences that create friction
- Users are unlikely to feel delight if foundational usability problems still exist

### Applying needs across workflows

User needs are not static research artifacts. They act as operational signals that help teams continuously evaluate how workflows, concepts, and decisions are affecting the user experience over time. As teams collect feedback, measure behavior, and evaluate concepts, user needs help clarify what problems matter most, where friction is increasing, what tradeoffs are emerging, what signals deserve attention, what decisions may need to change.

### How user needs connect across the Decision Map

| Area | How user needs help |
|---|---|
| **Define** | Clarify what users are trying to accomplish, where friction is emerging, what problems deserve deeper evaluation |
| **Measure** | Guide UX metrics, concept evaluation, behavioral signals, and workflow validation |
| **Focus** | Help teams compare priorities, evaluate tradeoffs, identify where friction matters most |
| **Lead** | Connect user behavior, design decisions, workflows, and business outcomes over time |

### User needs across teams

As organizations grow, product and design decisions become distributed across multiple teams. Different groups collect different types of signals — analytics, research findings, customer feedback, support issues, stakeholder requests. Without a shared way to interpret those signals, organizations struggle with fragmented decisions, duplicated effort, inconsistent measurement, unclear ownership, opinion-driven discussions.

User needs provide shared language for discussing friction, evaluating workflows, interpreting UX metrics, prioritizing opportunities, explaining tradeoffs, and connecting decisions to outcomes.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 15P4dY3qhZ5rUgusxhrVLpWr5uLfvRTliFvdZsVBIHvA — Glare | Define, User Needs, Techniques v1.4 -->

## Techniques

Where the Playbook covers execution workflows, Techniques covers the thinking behind them: how to interpret behavior, evaluate signals, and recognize needs before jumping to solutions.

### Understanding needfinding

Needfinding is the process of identifying the deeper conditions shaping user behavior. Users describe what they want in terms of features, fixes, and preferences. Those descriptions rarely explain the underlying friction. A request for "better filters" may reflect decision overload. A request for "more AI features" may point to a need for confidence or reduced effort.

### Wants vs needs

| Wants (immediate, solution-oriented) | Needs (deeper, behavioral) |
|---|---|
| "Add dark mode" | confidence that the workflow will work |
| "Give me more filters" | clarity about what to do next |
| "Make the AI smarter" | trust that the information is accurate |
| "Add more notifications" | reduced effort to complete a task |

Users adapt to existing systems rather than imagining different ones. They describe solutions through the workflows they already know. Needfinding helps teams step back from the requested solution and ask what condition is actually creating the behavior.

### Four ways to evaluate user needs

Before choosing a method, teams benefit from knowing which type of question they are trying to answer. Most needfinding maps to one of four evaluation questions. These are not sequential — multiple questions often apply to the same workflow at the same time.

| Evaluation question | Focus area | Common user needs |
|---|---|---|
| Can users **complete** what they need? | Functional workflows, task completion, usability | Useful · Usable · Findable · Accessible · Efficient |
| Can users **rely on** this? | Trust, predictability, confidence | Credible · Secure · Reliable |
| Does this **make sense**? | Understanding, relevance, clarity | Intuitive · Insightful · Adaptable · Valuable |
| Do users **like** this? | Emotion, engagement, connection | Desirable · Delightful · Engaging · Empowering · Connected · Inclusive |

These questions help teams identify where experiences begin breaking down, structure interpretation during research, connect user behavior to user needs, and evaluate workflows more consistently.

### Needfinding methods

**Observation.** Surfaces behavioral signals users would never describe in words. Use when teams suspect friction exists but cannot locate it from feedback alone, or when stated feedback conflicts with what the data shows. Watch for repeated clicking, long pauses, reopening screens, verification behavior, abandoned workflows, workarounds that bypass the intended path.

Small behavioral moments often reveal larger conditions. Repeated scrolling may indicate uncertainty. Reopening screens may signal low confidence. Long pauses often suggest comprehension gaps. Skipping steps may point to workflow friction.

**Interviews.** Uncovers emotional context, motivations, and hidden tension that behavioral data cannot explain. Most useful early in a workflow or when a need is present but its cause is unclear. The goal is understanding what situations create friction, what outcomes matter most, what pressures influence decisions, what fears or uncertainties exist underneath the workflow. Questions that open up context:

- "What were you trying to accomplish?"
- "What made this difficult?"
- "What were you worried about?"
- "What happened next?"
- "How did you decide what to do?"

The most valuable signals appear when users explain moments of uncertainty, frustration, or hesitation in their own words — not when they evaluate a feature.

**Laddering and the Five Whys.** Moves a surface-level complaint or request toward the underlying condition driving it. Use when users give short, vague, or solution-framed answers, or when interviews stay at the feature level. Users start with surface explanations ("It's confusing," "I don't trust it," "It takes too long"). Each follow-up question takes the answer one level deeper:

- "Why was that frustrating?"
- "Why did that matter to you?"
- "What were you worried might happen?"
- "What would success have looked like?"

The conversation moves from interface feedback toward emotional tension, workflow pressure, confidence gaps, and the actual conditions shaping behavior.

**Process Mapping.** Makes friction visible across the full workflow rather than inside isolated screens. Use when individual screens seem to work but users still struggle — when needs only appear at transitions between steps, departments, or decisions. Especially common in onboarding, enterprise systems, AI-assisted workflows, financial products, and operational software.

### Recognizing patterns

Needs often become visible when signals from different sources start reinforcing the same underlying condition: a support issue connects to a usability finding, a UX metric reinforces an interview quote, a hesitation pattern reveals a trust problem. Individual signals are rarely enough on their own.

| Pattern | What teams often see | Emerging needs |
|---|---|---|
| Comprehension Gaps | Hesitation, rereading, clarification questions, uncertainty about next steps | Usable · Findable |
| Workflow Friction | Repeated effort, task failure, recovery behavior, slow progression | Efficient · Usable |
| Behavioral Drop-off | Abandonment midway through a workflow | Useful · Efficient |
| Workaround Behavior | Users creating alternate paths to complete tasks | Usable · Useful |
| Trust Breakdowns | Verification behavior, repeated checking, low confidence, abandonment | Reliable · Credible · Secure |
| Low Confidence | Delayed decisions, repeated revisiting, stalled progression | Reliable · Secure |
| Contradictory Signals | Metrics and stated feedback telling conflicting stories | Credible · Insightful |
| Relevance Gaps | Weak engagement, disconnected behavior, low perceived usefulness | Connected · Insightful |
| Expectation Mismatches | High satisfaction paired with low conversion or weak follow-through | Intuitive · Desirable |

When a pattern appears once, it may be an edge case. When it appears across multiple users, sessions, or signal types, it usually points to a real and recurring need.

### Characteristics of strong vs weak user needs

| Strong user needs | Weak user needs |
|---|---|
| Specific enough to guide decisions | Describe a feature or interface instead of a problem |
| Broad enough to remain useful across concepts | Assume solutions too early |
| Grounded in observable behavior | Rely on internal language or opinion |
| Connected to measurable signals | Too abstract to evaluate or measure |
| Focused on outcomes instead of interfaces | Cannot be validated with evidence |

**Strong examples:**
- "Users need clearer guidance connecting their financial score to meaningful next steps." — identifies the underlying situation, explains the missing connection, creates an opportunity for measurement.
- "Users need faster ways to evaluate options without manually comparing large amounts of information." — reframes the situation around effort and workflow challenge rather than the requested feature.

**Weak examples:**
- "Users need a better dashboard." — describes a solution space. Does not explain what users are struggling with, what behavior is breaking down, or what outcome they are trying to achieve.
- "Users want more AI features." — reflects a request, not a validated need. Does not explain the friction, the condition, or the expected outcome.

Stronger user need statements create stronger downstream decisions: signals interpreted more consistently, better UX metrics chosen, workflows prioritized, fewer opinion-driven discussions, more objective concept evaluation.

### From user needs to measurable signals

Identifying a user need is the starting point, not the finish line. Once a need is identified, teams can begin connecting it to UX metrics, behavioral observations, concept evaluations, usability findings, and workflow outcomes. For example, a team that identifies users needing clearer onboarding guidance can influence:

- what concepts are tested
- what UX metrics are selected
- what signals are monitored
- what workflows are evaluated
- what outcomes are prioritized

This avoids common situations where metrics become disconnected from user behavior, design improvements are difficult to explain, experimentation lacks direction, stakeholder conversations drift into opinion, or teams struggle to prioritize competing initiatives.

### Connecting Techniques to the Playbook

Techniques produces the structured understanding that the Playbook turns into outputs. Once a team has applied needfinding methods, recognized recurring patterns, and formed clear user-need statements, the Playbook provides the workflows, prompts, and output formats. If signals are still too thin or conflicting after applying these techniques, the next step is usually Collecting — gathering stronger evidence before moving to outputs.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1VrZ9kkiHmwXePQOpDvuko9q8Yn4MH806s-hq3vbUwb8 — Glare | Define, User Needs, Playbook v1.4 -->

## Playbook

The User Needs Playbook turns scattered observations into structured outputs that can guide product and design decisions. Where Techniques covers how to interpret behavior, the Playbook covers what to do with that understanding — how to organize signals, structure outputs, and decide what happens next.

### Inputs

Strong signals usually appear when multiple inputs reinforce the same underlying condition.

| Input | Artifact format | What it reveals |
|---|---|---|
| Customer Interviews | Transcript, notes, audio, video | Motivations, frustrations, emotional context |
| UX Metrics | Dashboard, spreadsheet, exported report | Measurable friction and behavioral patterns |
| Analytics | Dashboard, spreadsheet, event logs | Repeated workflow and engagement issues |
| Support Tickets | Text threads, CRM exports | Recurring operational friction |
| Usability Findings | Notes, recordings, reports, screenshots | Comprehension gaps and usability breakdowns |
| Surveys | Forms, spreadsheets | Expectations, satisfaction, recurring concerns |
| Stakeholder Assumptions | Notes, workshop docs | Organizational bias and unvalidated thinking |
| Workflow Observations | Notes, recordings, journey maps | Environmental and operational friction |
| Concept Testing | Screenshots, prototypes, reports | Early comprehension and trust signals |
| Forum Discussions | Text threads, comments | Repeated language and unmet expectations |
| Product Hunches | Notes, whiteboards, planning docs | Areas needing validation or deeper exploration |

The process does not depend on perfect inputs. It depends on gathering enough observable signals to begin identifying recurring patterns.

### Identifying emerging needs

| Pattern | Watch for | Emerging needs |
|---|---|---|
| Comprehension Gaps | Confusion, hesitation, clarification requests, repeated rereading | Usable · Findable |
| Workflow Friction | Repeated effort, task failure, recovery behavior, slow progression | Efficient · Usable |
| Behavioral Drop-off | Users abandoning workflows midway through completion | Useful · Efficient |
| Workaround Behavior | Users creating alternate paths to complete tasks | Usable · Useful |
| Trust Breakdowns | Verification behavior, abandonment, repeated checking | Reliable · Credible · Secure |
| Low Confidence | Delayed decisions, repeated revisiting, stalled progression | Reliable · Secure |
| Contradictory Signals | Metrics and feedback telling conflicting stories | Credible · Insightful |
| Low Relevance | Weak engagement, low perceived usefulness | Connected · Insightful |
| Expectation Mismatches | High satisfaction paired with low conversion | Intuitive · Desirable |
| Repeated Friction | Similar problems appearing across workflows | Usable · Reliable |

Strongest user needs usually emerge when multiple signals reinforce each other, behavior repeats across workflows, metrics conflict with stated feedback, or users struggle despite high engagement.

### AI prompt structure for user-needs analysis

Strong prompts explain the workflow or situation, include user behavior or evidence, reference UX metrics or findings, and focus on understanding rather than proving assumptions.

| Focus | Example prompt |
|---|---|
| User Behavior | "Review these onboarding interviews and identify repeated hesitation or confusion patterns." |
| Workflow Problems | "Analyze this signup flow and identify where users may be struggling to move forward." |
| Trust Issues | "Review these usability findings and identify possible trust or confidence gaps." |
| User Needs | "Separate requested features from the underlying user needs in these interviews." |
| UX Metrics | "Compare these UX metrics against possible comprehension or workflow problems." |
| Pattern Grouping | "Cluster these support tickets into recurring workflow or usability patterns." |
| Concept Evaluation | "Analyze these concept tests and identify where understanding or trust starts to break down." |
| Friction Mapping | "Map the friction points across this onboarding experience and explain what users may be struggling with." |
| Stakeholder Alignment | "Summarize the strongest user patterns from these findings that should guide stakeholder decisions." |
| Opportunity Finding | "Identify the biggest UX opportunities based on these user behaviors and workflow signals." |

Strong prompts usually provide real workflow context, include supporting evidence, focus on observable behavior, avoid jumping directly to solutions, and ask the system to explain why patterns may exist.

### Primary user need output template

When a primary user need is identified, the output should be a single structured table that clearly explains what need is emerging, what evidence supports it, how users are behaving, where friction is appearing, why the issue matters, and what UX metrics may help validate improvement.

| Output | Contents | Example |
|---|---|---|
| **Category** | Primary User Needs category where the experience is breaking down | Personal |
| **User Need** | Specific user need emerging inside the category | Insightful |
| **Summary** | What users are trying to accomplish and what is preventing progress | "Users need to understand why their Planning score is low and what action will improve it." |
| **Evidence** | Metrics, quotes, usability findings, workflow observations, or repeated signals supporting the need | Users repeatedly revisit the Planning score, recommendation CTR is low, and support questions ask "What does Planning mean?" |
| **User Behaviors** | Recurring behaviors users consistently demonstrate because of the unmet need | Users review their score but hesitate to choose a recommendation because they do not understand why it is being suggested |
| **User Roadblocks** | Where confidence, understanding, or workflow progression starts breaking down | Recommendations appear before users understand the meaning behind the Planning score |
| **Why It Matters** | Operational, user, or business impact created by the unmet need | Users are less likely to engage with financial recommendations they cannot evaluate or trust |
| **Why It Fails** | Common ways teams incorrectly respond to the problem or overlook the underlying need | Teams improve delight or personalization before solving the comprehension problem |
| **Suggestions** | Potential workflow, messaging, UX, or product directions worth exploring | Explain why the Planning score is low and connect recommendations directly to specific financial behaviors |
| **UX Metrics** | UX metrics most useful for validating whether the user need is improving over time | Comprehension · Trust · Completion Rate · Recommendation Engagement |

### Example user need summary (short form)

For decks, async reviews, or AI-assisted summaries, a paragraph form works:

**User Need:** Insightful · **Category:** Personal

Users need to understand why their Planning score is low and what specific action will improve it. Evidence shows users repeatedly revisit the score while avoiding recommendations like "Schedule Appointment." Support questions also suggest users do not fully understand what the Planning score actually represents. This creates hesitation and low confidence because recommendations appear before users understand why they matter. If left unresolved, teams may mistakenly improve visual polish or personalization instead of fixing the deeper comprehension gap. Suggested areas to explore include clearer explanations, stronger contextual guidance, and recommendations tied directly to user financial behavior.

Recommended UX metrics: Comprehension · Trust · Engagement · Completion Rate

### Multiple user needs

When several emerge at once, start with a higher-level summary table, then explore each need individually using the full output template.

| User Need | Evidence | User Behaviors |
|---|---|---|
| Insightful | Users revisit the Planning score repeatedly and avoid recommendations | Users hesitate to act because they don't understand what the score means |
| Reliable | Users repeatedly verify account balances before trusting recommendations | Users double-check information before committing to financial actions |
| Efficient | Users abandon workflows midway through onboarding | Users struggle to complete tasks without repeated effort |

**Three prioritization questions when multiple needs emerge:**

1. **Which need is blocking the others?** Comprehension and trust problems usually need to be resolved before engagement or efficiency improvements will hold. A user who does not understand the workflow cannot benefit from a faster one.
2. **Which need has the strongest evidence?** Prioritize needs supported by multiple signal types — behavioral data, interview quotes, and metrics all pointing in the same direction — over needs supported by a single source.
3. **Which need connects most directly to a business outcome?** When evidence is roughly equal across needs, the need most tied to a measurable outcome — conversion, retention, engagement — is usually the right starting point.

This helps teams avoid the common mistake of addressing the most visible need rather than the most foundational one.

### Next steps inside the Decision Map

| Next step | Why it's useful |
|---|---|
| Collecting | Gather stronger evidence — validates the emerging need |
| Hunches | Form clearer hypotheses around what may be causing the friction |
| Signals | Turn recurring observations into measurable signals |
| Metrics | Define how success or improvement should be measured |
| Experiments | Test workflows, concepts, messaging, or product changes |
| Reviews | Align stakeholders around evidence and decision direction |
| Workflows | Evaluate operational systems and handoffs affecting the experience |

The next step should always be driven by what the team most needs to reduce uncertainty, not by what comes next in a sequence.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1l6QiT4AKqrqrZms5Ue3B1wBVc1ap7vlPaKUwU_8rWsc — Glare | Define, User Needs, References v1.4 + Reference/ subfolder (20 individual need docs, IDs starting with 1BqIn1JaGvingyLUbicqebfOW9GvR7rLplHbSQOkpVxA et al.) -->

## References

The Reference layer is the durable lookup material for the 20 individual user needs across the 5 layers. Where Techniques covers how to interpret behavior and the Playbook covers how to organize outputs, References is the layer teams return to when they need to understand a specific need more precisely — during research synthesis, concept reviews, usability evaluations, stakeholder discussions, or AI-assisted workflows.

Each individual need has its own page in the Drive `Reference/` subfolder (folder ID `13Uozpeed7IQc0nYo8ccVsOQ2_m_55OWJ`) containing definition, where it fits in Glare, why it matters, common UX metrics, heuristics, summary insight, and what to do next.

### Category index

| Category | Core focus | User needs |
|---|---|---|
| **Basics** | Foundational usability and access | Useful · Usable · Findable · Accessible |
| **Trust** | Reliability and confidence | Credible · Secure · Reliable · Intuitive |
| **Personal** | Relevance and contextual understanding | Inclusive · Adaptable · Connected · Insightful |
| **Impact** | Progress and meaningful outcomes | Valuable · Sustainable · Efficient · Scalable |
| **Feelings** | Emotion and long-term connection | Desirable · Delightful · Engaging · Empowering |

### Needs at a Glance

A quick reference for all 20 needs, organized by layer, with the core behavioral signal teams should watch for and the primary UX metrics most likely to reveal whether the need is being met.

#### Basics — "Can users use it easily?"

The foundation every experience has to get right before anything else matters. Basics needs determine whether users can accomplish what they came to do, whether the product is worth using, easy enough to use, possible to navigate, and accessible to everyone who needs it.

| Need | Core behavioral signal | Primary UX metrics |
|---|---|---|
| **Useful** | Users complete tasks but question whether the outcome was worth the effort | Completion Rate · Comprehension · Satisfaction |
| **Usable** | Users hesitate, retry, or abandon steps they should be able to complete | Success Rate · Error Rate · Time on Task |
| **Findable** | Users search, scroll, or ask for help locating things they expect to be obvious | Time on Task · Comprehension · Abandonment Rate |
| **Accessible** | Users with different abilities, devices, or contexts cannot complete workflows others can | Completion Rate · Error Rate · Satisfaction |

#### Trust — "Do users believe it works?"

The layer that determines whether users believe the experience will work for them. Trust needs emerge when users question the accuracy of information, the security of their data, the consistency of the system, or whether the product will behave the way they expect.

| Need | Core behavioral signal | Primary UX metrics |
|---|---|---|
| **Credible** | Users verify information from external sources before trusting what the product shows | Trust · Comprehension · Satisfaction |
| **Secure** | Users hesitate to share information or complete transactions because of uncertainty about safety | Trust · Abandonment Rate · Sentiment |
| **Reliable** | Users encounter inconsistent behavior, errors, or unexpected outcomes across sessions | Trust · Error Rate · Completion Rate |
| **Intuitive** | Users can complete workflows but cannot explain how the system works or predict what comes next | Comprehension · Success Rate · Satisfaction |

#### Personal — "Does it fit their needs?"

The layer that determines whether the experience feels relevant to the individual user. Personal needs surface when the product works in general but fails to account for a user's specific context, role, goals, or situation.

| Need | Core behavioral signal | Primary UX metrics |
|---|---|---|
| **Inclusive** | Users from different backgrounds, roles, or contexts find the experience misaligned with their situation | Satisfaction · Completion Rate · Sentiment |
| **Adaptable** | Users repeatedly adjust settings, create workarounds, or abandon workflows that do not fit their context | Effort · Completion Rate · Satisfaction |
| **Connected** | Users engage with individual features but do not see how they relate to each other or to their goals | Engagement · Comprehension · Satisfaction |
| **Insightful** | Users receive information but cannot interpret what it means or what they should do with it | Comprehension · Trust · Engagement |

#### Impact — "Does it make a difference?"

The layer that determines whether the experience creates meaningful progress over time. Impact needs emerge when users can complete tasks but question whether the outcomes are worth the effort, or when workflows that work at small scale begin breaking down as demands increase.

| Need | Core behavioral signal | Primary UX metrics |
|---|---|---|
| **Valuable** | Users complete workflows but do not feel the outcome was worth the time or effort invested | Satisfaction · Completion Rate · Sentiment |
| **Sustainable** | Users experience fatigue, repetition, or increasing effort over time rather than improving efficiency | Effort · Retention Rate · Satisfaction |
| **Efficient** | Users accomplish goals but require more steps, time, or effort than the task should demand | Time on Task · Effort · Completion Rate |
| **Scalable** | Workflows that work for individual users break down as volume, complexity, or team size increases | Completion Rate · Error Rate · Effort |

#### Feelings — "Does it inspire them?"

The layer that determines whether users develop a lasting connection to the experience. Feelings needs are rarely the source of foundational friction, but they are what separates products users tolerate from products users prefer, return to, and recommend.

| Need | Core behavioral signal | Primary UX metrics |
|---|---|---|
| **Desirable** | Users find the experience functional but not one they prefer, recommend, or return to by choice | Desirability · Sentiment · Retention Rate |
| **Delightful** | Users complete tasks without any moment of unexpected pleasure, surprise, or positive emotion | Sentiment · Desirability · Satisfaction |
| **Engaging** | Users complete tasks but disengage quickly, return infrequently, or describe the experience as forgettable | Engagement · Retention Rate · Sentiment |
| **Empowering** | Users feel dependent on the product rather than more capable because of it | Satisfaction · Comprehension · Sentiment |

### How the needs work together

Individual needs rarely exist in isolation. Addressing one need often reveals or amplifies another.

- **Basics failures cascade upward.** When Useful, Usable, Findable, or Accessible needs are unmet, higher-layer needs cannot fully emerge. A user who cannot complete a workflow will not develop trust, feel a sense of personal relevance, or experience emotional connection. Resolving Basics needs first usually has the highest leverage.
- **Trust and Personal needs interact closely.** An experience that does not feel credible or reliable will rarely feel personally relevant. Users do not engage deeply with systems they do not trust. When both are flagged, Trust is usually the right starting point.
- **Impact and Feelings needs depend on earlier layers.** Users rarely feel an experience is valuable, empowering, or delightful if foundational usability or trust problems still exist. Optimizing Feelings before resolving Basics or Trust is one of the most common prioritization mistakes teams make.
- **Contradictory signals often point to layer mismatches.** High satisfaction paired with low completion, or strong engagement paired with low conversion, usually means a lower-layer need is unresolved while a higher-layer need is being addressed. The Recognizing Patterns table in Techniques is the right tool for diagnosing these situations.

### What each reference page contains

Each of the 20 individual need pages follows the same structure:

| Section | What it contains |
|---|---|
| **Definition** | What the need means, why it matters, what strong and weak versions look like |
| **Where It Fits in Glare** | How the need connects to other needs and where it sits in the Decision Map |
| **Why It Matters** | Operational, user, and business impact when the need is unmet |
| **Common UX Metrics** | Behavioral and attitudinal metrics most useful for evaluating this need |
| **Heuristics** | Specific evaluation criteria for assessing how well the experience is meeting the need |
| **Summary Insight** | A concise synthesis of what strong performance looks and feels like |
| **What to Do Next** | Recommended starting points for measurement, evaluation, or improvement |

### How to use the references

- **During research synthesis** — use behavioral signals and failure patterns to check whether observations map to a specific need or point to something adjacent.
- **During concept reviews** — use heuristics to evaluate whether a concept addresses the underlying need or only the surface symptom.
- **During UX metric selection** — use the metric guidance to choose signals that actually reflect whether the need is improving over time.
- **During stakeholder discussions** — use the definition and "why it matters" sections to ground conversations in shared language rather than opinion.
- **Inside AI Skills** — reference pages provide the definitional layer that helps skills classify needs consistently and produce outputs in the right structure.

References is a lookup layer, not a starting point. Teams typically arrive here after identifying a need through Techniques or receiving a structured output from the Playbook or an AI Skill. Once a specific need is understood more precisely, the natural next steps are selecting UX metrics in Measure, forming hypotheses in Hunches, or designing evaluation criteria for concept reviews.

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1SlEfUqlxmE0iNsvQgEN0a8pNV9ICBo4vLjfxKkCoTH4 — Glare | Define, User Needs, Decisions v1.4 -->

## Decisions

Decisions helps teams identify whether User Needs is the right place to be working and, once they are, which part of the block will be most useful given their situation. It is designed to be scanned quickly — find the situation that matches, follow the guidance, move forward.

### When to use User Needs

User Needs is the right starting point when a team has signals but cannot agree on what they mean, when decisions keep stalling because the underlying problem is unclear, or when research and metrics exist but are not connecting to action. If the team is debating solutions before the problem is clearly defined, User Needs is almost always the right place to begin.

### Recognizing the situation

**1. We have feedback but can't agree on what it means.** Teams have interviews, support tickets, analytics, or usability findings — but different people are drawing different conclusions from the same data. Stakeholder opinions are filling the gap that evidence should be filling.
*What to do:* Start with **Techniques** to build shared interpretation. Use the Four Ways to Evaluate and the Recognizing Patterns table to organize signals around recurring conditions rather than individual opinions. Then move to the **Playbook** to structure what you find into a user-need output the team can align around.

**2. We know something is wrong but can't locate the problem.** Metrics are weak, users are dropping off, or satisfaction is low — but the team cannot pinpoint what is actually causing it. The problem feels real but diffuse.
*What to do:* Use **Techniques** to apply observation and process mapping across the full workflow, not just the screens where drop-off appears. Look for the patterns table entries that match what you are seeing behaviorally. The problem is usually one layer below where the team is currently looking.

**3. We're reacting to feature requests instead of understanding what users actually need.** The team is fielding a backlog of user requests, stakeholder asks, and product hunches — but it is not clear which ones reflect a real underlying need.
*What to do:* Use **Techniques** — specifically Wants vs. Needs and the Laddering method — to reframe requests around the conditions driving them. Then use the Playbook prompt structure to separate features from needs, and the Characteristics of Strong User Needs to evaluate whether what the team has identified is operational enough to act on.

**4. We've identified a need but aren't sure if it's the right one.** The team has a user-need statement but it feels too broad, too solution-framed, or not grounded in enough evidence to confidently move forward.
*What to do:* Use the Characteristics of Strong User Needs in Techniques to evaluate the statement against the strong vs. weak criteria. If the need is too vague, return to the Playbook inputs table and check whether enough signal types are represented. A need supported by only one source usually needs more evidence before it can guide decisions.

**5. We have multiple needs emerging at the same time and don't know where to start.** Research has surfaced several legitimate user needs across different layers. The team is struggling to prioritize and risks spreading effort too thin or addressing the most visible need rather than the most foundational one.
*What to do:* Use the Playbook's Multiple User Needs section and the three prioritization questions — which need is blocking the others, which has the strongest evidence, which connects most directly to a business outcome. Then use References to understand how the competing needs relate to each other across layers before deciding where to focus first.

**6. We need to explain the problem to stakeholders.** The team understands the user need but is struggling to communicate it in a way that creates alignment rather than debate. Stakeholders are gravitating toward solutions before the problem is agreed on.
*What to do:* Use the Playbook's Primary User Need Output table to structure the problem clearly — evidence, behaviors, roadblocks, why it matters, why it fails. The structured output is designed to ground stakeholder conversations in observable evidence rather than opinion. The short-form Example User Need Summary works for presentations or async reviews.

**7. We know the need but aren't sure how to measure whether we're improving it.** A user need has been identified and the team is ready to move toward measurement, but it is not clear which UX metrics will actually reflect whether the experience is getting better.
*What to do:* Go to References and open the individual need page. Each page contains behavioral and attitudinal metrics selected specifically for that need, along with heuristics for evaluating current performance. Use the From User Needs to Measurable Signals section in Techniques to connect the need to a measurement approach before moving into the Metrics block.

**8. We're setting up an AI Skill for this block.** The team is building or refining an AI Skill that uses User Needs and needs to understand which parts of the block the skill should draw from.
*What to do:* The **Playbook** is the primary source for input formats, prompt structure, and expected outputs. **References** provides the definitional layer the skill uses to classify needs consistently. **Examples** provides the worked examples and pattern library the skill uses to calibrate output quality. Use all three together when configuring a skill for this block.

### Quick reference

| Situation | Start here |
|---|---|
| Can't agree on what signals mean | Techniques → Playbook |
| Can't locate where the problem is | Techniques — Observation, Process Mapping |
| Reacting to requests instead of needs | Techniques — Wants vs. Needs, Laddering |
| Need statement feels weak or too broad | Techniques — Characteristics, Playbook Inputs |
| Multiple needs, unclear where to start | Playbook — Multiple User Needs, References |
| Need to align stakeholders | Playbook — Primary Output, Example Summary |
| Don't know how to measure improvement | References — Individual Need Page, Techniques — Measurable Signals |
| Setting up an AI Skill | Playbook + References + Examples |

<!-- /DERIVED -->

---

<!-- DERIVED FROM: 1fZw7vIs2yRLVGN-7pxdr0NEZ4Jc2PIei-j3kvRqzBio — Glare | Define, User Needs, Examples v1.4 -->

## Examples

User Needs is the framing layer for the rest of Define. A clearly identified Hunch tells **Audience** who matters most right now, tells **Collecting** what evidence to prioritize, and tells **Patterns** what behavioral signals would confirm or refute it. The goal is not proving a need before acting — it is building enough structured understanding to make the next step purposeful rather than arbitrary.

Each example below uses the same shape: Situation → Inputs available → Hunch → What's not yet measured → What this orients → Decision.

### 1. Useful — Users are visiting but nothing is happening

**Situation:** A fintech product team notices that mobile dashboard sessions are frequent but nothing follows. Users open the app, view their scores, and leave. No recommendations are clicked. No actions are taken.

**Inputs available:**
- **Analytics** — session frequency and duration data showing repeated short visits with no downstream action
- **Support Tickets** — a pattern of questions asking what specific scores mean and what users should do about them
- **Customer Interviews** — two early interviews where users described scores as "interesting but not sure what to do with them"

**Hunch:** Users may need to understand what their scores *mean* before they can evaluate what to do next. Points toward a **Useful** need at the Basics layer — the dashboard is displaying information but not connecting it to outcomes users can act on. Not yet confirmed — a direction worth investigating before drawing conclusions or beginning any redesign.

**What's not yet measured:** Whether users are failing to comprehend the scores, failing to find the recommendations, or simply not motivated to act. These are different problems with different solutions. Comprehension, Recommendation Engagement, and Completion Rate are the right metrics to establish — but first the team needs to understand which failure is actually happening.

**What this orients:** Narrows **Audience** toward regular users rather than new ones. For **Collecting**, the priority is interviews and session observations that surface what users understand about the scores, not satisfaction surveys. The pattern to watch for is hesitation — users who dwell on information without moving forward.

**Decision:** Before any redesign or personalization work, the team sets up Comprehension measurement on the dashboard and runs 5–8 interviews focused on what users think their scores mean and what they expect to happen next. The Hunch is confirmed if users cannot explain what the scores mean in their own words. It is refuted if users understand the scores but choose not to act — which would point to a different need entirely.

### 2. Reliable — A booking flow that loses people at the last step

**Situation:** A B2B SaaS team sees consistent drop-off at the final confirmation step of their booking flow. Stakeholders assume pricing is the problem and are preparing a pricing display redesign.

**Inputs available:**
- **Analytics** — drop-off data concentrated at the confirmation step
- **Support Tickets** — a pattern of questions asking what happens after confirmation and whether bookings can be changed
- **Stakeholder Assumptions** — pricing is the cause of abandonment

**Hunch:** The support ticket language suggests something different from price sensitivity. Users are asking what happens after they confirm — not whether the price is fair. The Hunch is a **Reliable** need at the Trust layer. Users may be abandoning not because they object to the price but because they are uncertain whether the system will behave as expected once they commit.

**What's not yet measured:** Whether abandonment is driven by uncertainty about the outcome, distrust of the system, or a genuine pricing objection. Trust and Comprehension scores on the confirmation step do not yet exist. Abandonment Rate alone cannot distinguish between these causes.

**What this orients:** **Audience** narrows to users who reached the confirmation step and left — a specific behavioral segment worth recruiting for interviews before any changes are made. For **Collecting**, the priority is follow-up interviews with recent abandoners and session observation of the confirmation screen, not A/B tests on pricing display. Watch for verification behavior — users scrolling back, re-reading earlier steps, hovering without clicking.

**Decision:** Run 6 interviews with users who abandoned at confirmation, focused specifically on what information they felt was missing before they could commit. No redesign begins until the interviews either confirm the Reliable Hunch or surface a different need. If users consistently describe wanting to know what happens after submission, the intervention becomes about post-submission clarity — not pricing.

### 3. Insightful — Notifications that users open but don't act on

**Situation:** A fintech team sees declining notification engagement over three months. Open rates are dropping and post-open actions are nearly nonexistent. Internal debate has focused entirely on frequency. No one has talked to users.

**Inputs available:**
- **Analytics** — open rate and post-open action rate across three months showing consistent decline
- **Stakeholder Assumptions** — frequency is the cause of declining engagement

**Hunch:** The analytics pattern — users opening but not acting — suggests the problem may not be frequency. Users are willing to open. Something is breaking down after they do. The Hunch is an **Insightful** need at the Personal layer. Notifications may be informing users without helping them understand what the information means for their specific situation or what they should do next.

**What's not yet measured:** Comprehension on notification content. Open rates and post-open action rates exist, but no signal on whether users understand what they are being told or feel equipped to act on it. These are different failure modes with different solutions.

**What this orients:** **Audience** narrows to users who open notifications regularly but rarely take follow-on action. For **Collecting**, the priority is diary studies or brief post-open intercept interviews rather than additional analytics. Watch for users opening the same type of notification repeatedly without behavior changing — a signal that the notification is not producing understanding or intent.

**Decision:** Before changing frequency or targeting, run intercept interviews with users immediately after they open a notification, asking what they understood from it and what they considered doing next. The Hunch is confirmed if users consistently describe notifications as unclear about what they mean or what to do. It is refuted if users understood the notification but chose not to act — which would point toward a Desirable or Engaging need instead.

### 4. Efficient — Returning users abandoning a step they've completed before

**Situation:** An ecommerce team notices returning users abandoning at the address and payment step at a higher rate than new users. A/B tests on button copy and color have produced no meaningful change.

**Inputs available:**
- **Analytics** — abandonment rate segmented by new vs returning users, showing returning users abandoning significantly more at the address and payment step
- **Workflow Observations** — informal observation suggesting returning users may be re-entering previously submitted information

**Hunch:** **Efficient** need at the Impact layer. Returning users may be encountering repeated effort — re-entering information the system should already have — and abandoning because the experience is more work than they expect.

**What's not yet measured:** Effort scores for returning users. The team cannot yet distinguish between users who abandon because of effort, a technical error, or a change in intent. Effort measurement segmented by new vs returning users is the critical gap before any intervention is designed.

**What this orients:** **Audience** specifically returning users who have abandoned — a narrow and recruitable segment. For **Collecting**, session observation of returning-user checkout attempts is the priority, specifically watching whether users encounter pre-filled information or are asked to start from scratch. Watch for re-entry behavior — users typing information the system should already know.

**Decision:** Set up Effort measurement segmented by new and returning users before making any checkout changes. If Effort scores are significantly higher for returning users, the Efficient Hunch is confirmed and the intervention becomes about saved defaults — not copy, design, or pricing. Five session observations with returning users are also scheduled to confirm whether re-entry is actually happening before any build begins.

### 5. Desirable — An onboarding tour that users skip

**Situation:** A B2B team has built a detailed onboarding tour. 11% of users complete it. The rest skip or exit early. Leadership wants to make the tour mandatory. A researcher argues that making a low-desirability experience mandatory treats the symptom, not the cause.

**Inputs available:**
- **Analytics** — step-level completion data showing 67% of users exit at step three of nine; time-on-step data showing declining engagement across successive steps
- **Stakeholder Assumptions** — making the tour mandatory will solve the completion problem

**Hunch:** The drop-off pattern — steepest at step three — suggests users are making a judgment early that the tour is not worth their time. The Hunch is a **Desirable** need at the Feelings layer, compounded by an **Efficient** need. The tour may be comprehensive without being compelling — covering everything the team wants users to know rather than creating early moments of value users want to experience.

**What's not yet measured:** Desirability scores on the onboarding experience. Time-on-step data cannot distinguish between users who are engaged and moving slowly vs users who are disengaged and hesitating before exiting.

**What this orients:** **Audience** splits into two groups worth understanding separately — users who completed the tour and remained active at 30 days, and users who skipped and churned. For **Collecting**, interviews with both groups to understand what the tour did or did not create for them. Watch for the shift from active engagement to passive scrolling — a behavioral signal that interest has dropped before users formally exit.

**Decision:** Before any discussion of mandatory completion, run interviews with recent completers and recent skippers, focused on what the first three steps felt like and whether users experienced any moment of early value. The Hunch is confirmed if users consistently describe the tour as feeling like obligation rather than discovery. If confirmed, the intervention becomes restructuring around value moments — not enforcement.

### Pattern Library — tight input-output pairs for AI calibration

| Situation | Inputs available | Hunch | Orient toward | Confirmed if | Refuted if |
|---|---|---|---|---|---|
| **Post-Login Abandonment** | Post-login abandonment data; support tickets asking whether the account is set up correctly | **Secure** (Trust) — users may need confirmation that account and data are protected before engaging | Interviews with recent post-login abandoners; watch for verification behavior — users checking settings before engaging with core features | Users describe uncertainty about whether their account is configured correctly or their data is visible to others | Users describe the dashboard content as irrelevant or confusing → points to Insightful or Useful instead |
| **Filter Engagement Without Purchase** | Analytics showing users engaging with filters on a product browse page, then resetting and abandoning without purchasing | **Findable** (Basics) — users may be unable to locate products matching their criteria even after filtering | Session observation of filter interactions; watch for users applying filters, scanning briefly, and resetting rather than refining | Users describe filtered results as not matching what they were looking for | Users find relevant results but do not purchase → points to Credible or Desirable instead |
| **Enterprise Renewal Risk** | Renewal conversation notes describing the product as not fitting how enterprise teams work | **Adaptable** (Personal) — the product may work for standard workflows but not accommodate larger team contexts | Workflow observation with enterprise users in their actual environment; watch for workarounds — steps added outside the product to compensate for what it cannot do | Users consistently describe needing separate tools or manual coordination for tasks the product should handle | Users describe the product as capable but not valuable enough → points to Valuable instead |
| **High Traffic, Low Conversion** | High traffic analytics on a marketing landing page paired with low conversion; a full redesign is being planned | **Credible** (Trust) — users may be visiting but not trusting the claims enough to convert | Interviews with users who visited but did not convert; watch for language about claims being hard to verify or too vague to believe | Users describe wanting third-party validation or specific evidence before acting | Users found the claims credible but did not understand what the product does → points to Useful or Insightful instead |
| **Satisfied Users Who Don't Return** | High satisfaction survey scores; return purchase rate data showing quarter-over-quarter decline | **Engaging** (Feelings) — users may find the experience acceptable but not compelling enough to return voluntarily | Interviews with lapsed users; watch for language about the experience being fine but forgettable | Users describe no strong pull to return and no memorable moment from their last experience | Users describe a specific friction point that made returning feel like too much effort → points to Efficient instead |

### Near-Miss — What happens when a team forms a Hunch and skips validation

**Inputs available:**
- **Customer Interviews** — two participants describing recommendations as "not sure I trust them"
- **Analytics** — low recommendation engagement rate

**Hunch correctly formed:** **Credible** (Trust) — users may not trust the AI-powered budget recommendations enough to act on them.

**Wrong move:** The team treats two interview quotes as confirmation and immediately redesigns the recommendation cards — adding polish, cleaner typography, more prominent layout. Engagement remains flat after launch.

**Why it fails:** Two interview quotes are not enough to confirm a Hunch. The team skipped Collecting entirely — no research to understand *why* users did not trust the recommendations, no Patterns work to identify whether the trust problem was about credibility of the source, comprehension of the logic, or relevance to the user's situation. Each is a different intervention. The visual redesign addressed Desirability, not Credibility. Users did not distrust the recommendations because they looked unpolished — they distrusted them because they did not understand how the recommendations were generated or why they applied to their specific situation. A Comprehension failure sitting underneath the Trust need.

**Right move:** After forming the Credible Hunch, orient Collecting toward understanding specifically what users mean when they say they do not trust the recommendations. Five more focused interviews would have surfaced the Comprehension gap before any redesign began.

**What this teaches:** A Hunch is a starting point, not a brief. Two data points are inputs, not confirmation. Audience, Collecting, and Patterns exist precisely to validate or refute the Hunch before a team commits to a direction.

<!-- /DERIVED -->

---

<!-- ADDED 2026-05-13 (audit pass), refreshed 2026-05-22 -->

## When to use

- When the user is naming what users actually need before any solution exists.
- When distinguishing wants from needs ("faster horse" vs "faster travel").
- When picking among the five user-need categories (Basics, Trust, Personal, Impact, Feelings) or the 20 individual need types.
- When tying a need to a metric type (foundational needs → usability/completion; aspirational → desirability/loyalty).
- When the team is debating "what's the right feature" without agreement on which user need is unmet.
- When the user describes a stuck situation in plain language and needs routing to the right part of User Needs (use the Decisions section first).
- When evaluating whether a Hunch is strong enough to act on, or whether it needs more Collecting/Patterns work first (use the Near-Miss in Examples as a check).

**Don't use when** the question is about who to test with (use `glare-define-audience`), how to gather evidence (`glare-define-collecting`), or which numbers to track (`glare-define-ux-metrics`).

## Failure modes

These are common ways this skill goes wrong in practice:

- **Solving a want instead of a need.** Users say "make it faster" and the team optimizes performance — when the underlying need was Findable or Useful, not Performance. Translate the want into one of the 20 needs before designing.
- **Jumping straight to aspirational needs.** Teams chase Delight or Emotional Pull while users can't find the feature in the first place (Findable, Usable). The five categories are *ordered*; foundational needs earn the right to aspirational ones.
- **Treating every need as equally weighted.** Picking 6+ needs for one project guarantees none get served well. Pick 1–2 primary needs per initiative and let the rest serve as guardrails.
- **Skipping the credibility category.** Trust needs (Credible, Secure, Reliable, Intuitive) often go unnamed until users churn. They don't show up in feature requests; they show up in retention and trust metrics.
- **Treating a Hunch as confirmation.** Two interview quotes and a metric trend are inputs, not validation. The Near-Miss in Examples shows what happens when a team correctly identifies a Credible Hunch and then skips Collecting/Patterns — they redesign for Desirability and engagement stays flat. A Hunch tells the team what to investigate next, not what to ship.
- **Picking the most visible need instead of the most foundational one.** When multiple needs emerge at once, the loudest signal usually wins by default. Apply the three prioritization questions (blocking, evidence, business outcome) instead.

<!-- /ADDED -->
