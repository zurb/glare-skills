# Getting Started with Glare — Consolidated Reference (v3.0)

This reference consolidates the seven previous Get Started topics (introduction, conceptual tour, first-signal walkthrough, AI workflows, coaching/advising, proving design impact, glossary) into a single document. Refreshed for the v3 marketplace, where Glare is organized into **six connected components**, the Define area carries **five blocks** (including Patterns), UX Metrics uses **four types** (Attitudinal · Behavioral · Performance · Intelligence), and a top-level `glare-master` skill orchestrates the system.

---

## 1. What Glare is

### The framing

Glare is **a decision framework for product and design**, built around the observation that teams can now generate work faster than they can decide what to do with it. AI, prompts, and modern tools made flows, interfaces, and variations cheap to produce. Engineering can move from concept to implementation quickly. The bottleneck shifted: work now depends on how quickly that output can be **understood, evaluated, and turned into a decision the team can move forward with confidence**.

Most teams already have the inputs:
- Designers bring intuition
- Researchers bring early signals
- Product and engineering bring constraints and goals

These inputs are valuable but rarely come together as direction. Glare brings structure to that moment by turning inputs into design signals.

A **design signal** connects:
- a decision the team needs to make
- a measurable user response
- the outcome that decision is meant to influence

### Why Glare exists

Product and design slow at the point a team needs to decide what to do next. A concept is introduced, feedback comes in, something feels right and something feels off — but it's hard to explain why in a way the whole team can align around. Different parts of the team work from different inputs (intuitive judgment, broader insights, constraints, outcomes, risk) and those inputs don't naturally resolve into a clear decision.

Voices from the field:
- Jake Johnson — "We'll have a solid idea, plenty of discussion, and then someone asks what the next step is. That's usually where things fall apart because no one feels confident enough to say, 'this is the direction.'"
- Tim Banks — "The biggest challenge to measuring impact is the typical length of the feedback loop… so to shorten the loop we compromise with a mix of progress metrics and data from user studies to evaluate potential impact early."
- Ian Batterbee — "AI has made it easy to generate work quickly, but much harder to know what to trust."

Without structure, concepts expand without comparison, feedback accumulates without direction, output grows without shared understanding. Glare addresses that friction.

### Problems Glare solves

- data is messy or disconnected
- decisions drift toward opinion instead of evidence
- design impact is difficult to show clearly
- teams struggle to align on real user needs
- work moves quickly, but confidence lags behind

### Who Glare is for

| Role | What Glare gives them |
|---|---|
| Design Leaders | Defensible direction; show how design choices influence behavior and outcomes |
| Product Leaders | Evaluate multiple directions; reduce roadmap debate; tie behavior to priorities |
| Engineers / Technical Teams | Clearer inputs on what to build and why; fewer mid-stream changes |
| Research Leaders | Connect findings directly to decisions in the moment they matter |
| Founders / Executives | Fast, directional evidence on how ideas may perform before committing |
| Designers | Show how work performs with users; reasoning visible and grounded |

### When decisions matter most

Glare is most useful in moments that shape what moves forward: concept reviews, roadmap discussions, prioritization conversations, feature validation, release decisions. When clarity is missing, work continues but direction becomes unstable — decisions get revisited, alignment drifts, momentum slows.

### Built from work

Glare was built by ZURB after 25+ years and **50,000 hours of testing** across thousands of projects. The pattern: teams that made consistent progress weren't doing more research or following stricter processes — they were better at turning insight into decisions others could understand and act on.

---

## 2. How Glare works — the six-component system

The v3 framework organizes Glare into **six connected components**, orchestrated together by the top-level `glare-master` skill. The previous `glare-router` is gone; cross-component navigation is handled by `glare-master` and by the entry-point handoffs each component skill carries.

### The six components

| # | Component | Role | Top-level skill |
|---|---|---|---|
| 1 | **Get Started** | On-ramp — introduction, first signal, AI workflows, coaching, impact, glossary | `glare-getting-started` (this skill) |
| 2 | **Decision Map** | How decisions take shape — Define → Measure → Focus → Lead (loop) | `glare-decision-map` |
| 3 | **Design Review** | The conversations where decisions get made — SIGNAL framework | `glare-design-review` |
| 4 | **UX Metrics** | The measurement layer underneath everything — 4 metric types, 28 canonical metrics | `glare-ux-metrics` |
| 5 | **Design Signals** | The unit of clarity — anatomy, types, quality, capturing | `glare-design-signals` |
| 6 | **Design Assessment** | How the system holds across the org — 5-dimension diagnostic | `glare-design-assessment` |

`glare-master` is the orchestrator. It places a user's situation against the six components, routes them to the right entry point, and keeps the chain visible as work moves between components.

### 2.1 Get Started

The component you're inside right now. The on-ramp for a first-time user: what Glare is, how the parts fit, how to try it on a real decision, how AI fits in, how to roll it out, how to prove impact, and what terms mean.

### 2.2 Decision Map

The spine of Glare. Connects Define, Measure, Focus, and Lead into one continuous decision flow. Not a linear process — a loop.

| Facet | What it asks | Building blocks |
|---|---|---|
| **Define** | What problem are we solving? What matters? | User Needs · Audience · Collecting · UX Metrics · **Patterns** (5 blocks in v1.34) |
| **Measure** | How is this performing? What are users showing us? | Concepts · Hunches · Questioning · Findings |
| **Focus** | Which direction is stronger? What should move forward? | Initiatives · Methods · Comparing · Decisions |
| **Lead** | What do we commit to? How does it connect to outcomes? | Business Goals · Mapping · Workflows · Results |

**Patterns** is the v1.34 addition to Define — it helps teams recognize recurring situations before weak decisions gain momentum, especially as AI accelerates output faster than evaluation.

### 2.3 Design Review

Where signals are applied — the moment work is presented and a decision is expected. The SIGNAL framework structures the conversation in six moves: **Surface · Identify · Ground · Navigate · Align · Lock**. Each is scored 1–5 on the SIGNAL rubric for /30 total. Strong reviews keep attention on the decision, make tradeoffs visible, and let the team commit to a direction.

### 2.4 UX Metrics

The measurement layer underneath signals, reviews, decisions, and assessments. v3 uses **four types**:

- **Attitudinal — how users feel.** 9 metrics: Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness.
- **Behavioral — what users actually do.** 8 metrics: Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability.
- **Performance — efficiency, reliability, operational friction.** 11 metrics: Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency.
- **Intelligence — AI-assisted experience quality.** Whether intelligence is actually improving outcomes instead of simply generating more output. Scope — recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance.

Total: **28 canonical metrics** across the first three types, plus the Intelligence family (still expanding).

Version note — v1.0 used 3 types. v1.1 briefly added a "Perceptual" type, then removed. The canonical taxonomy is the four-type model above. Comprehension and recognition (which v1.1 grouped under Perceptual) now live inside Behavioral.

### 2.5 Design Signals

The unit of clarity. A signal connects six pieces — UX metric · intuition · direction · context · user need · business goal — into something a team can act on. Sub-areas: Components (the six-piece anatomy), Types (Need · Use · Prefer · Adopt), Quality (usable vs. not-usable filter), Capturing (Frame → Ground → Measure → Use).

### 2.6 Design Assessment

How decisions move through the org over time, across **five dimensions**:

| Dimension | What it diagnoses |
|---|---|
| Organizing Work | Is the work structured clearly, or scattered? |
| Managing Complexity | Can teams handle multiple directions, or does complexity slow decisions? |
| Building Proof | Are signals strong and consistent, or does work rely on assumption? |
| Guiding Decisions | Are signals actually used, or do conversations drift? |
| Scaling Influence | Do decisions carry across teams and time, or get revisited? |

Score bands — Reactive · Developing · Functional · Strong · Leading. The assessment is about patterns over time, not single moments.

### How it comes together (the loop)

```
prompts/conversations  →  ideas
                ↓
         AI Skills  →  shape how those ideas are evaluated
                ↓
    UX metrics + signals  →  show how users respond
                ↓
       Design Review  →  uses signals to guide decisions
                ↓
       Decision Map  →  keeps decisions moving (Define → Measure → Focus → Lead)
                ↓
   Design Assessment  →  shows how well it's all holding together
```

Each step feeds the next. **The loop repeats but doesn't reset — it builds.** `glare-master` keeps the chain visible as work crosses component boundaries.

### What this produces

- design signals that clearly reflect user behavior
- decisions people can align around
- visible tradeoffs between options
- direction that holds as work moves forward
- a clear connection between design work and outcomes

The team spends less time circling decisions and more time moving them forward.

### Where Glare works best vs. needs support

| Where Glare works best | Where it needs support |
|---|---|
| Decisions are unclear or evolving | Access to users or meaningful feedback |
| Multiple options need to be compared | Shared understanding of metrics |
| User behavior needs to inform direction | Consistent use of signals in decisions |
| Teams are moving quickly and need structure | (when missing, signals weaken) |

---

## 3. Creating your first signal — the six-move walkthrough

The fastest on-ramp into Glare. Used when a real decision is on the table.

### The trigger pattern

A typical situation:
- You have two directions for a flow
- Design prefers one, Product leans another, Engineering is thinking about complexity
- There's some feedback and a bit of data, but nothing clearly points to a decision
- The work has to keep moving, but the decision isn't sharp
- Things start to **Frankenstein** — revisited, loses clarity across teams, confidence drops

### The six pieces a signal connects

| Piece | What it is |
|---|---|
| UX metric | What you're trying to understand or improve |
| Intuition | What the team is noticing |
| Direction | The option(s) being considered |
| Context | Where the work sits within a concept |
| Business goal | What outcome you're trying to move |
| User need | What users are trying to satisfy |

Once these connect, the team has something concrete to work from.

### Move 1 — Start with a Hunch

Every signal starts with something the team is already reacting to. It usually shows up in conversation, not in a deck:
- "this direction feels cleaner"
- "users might get stuck here"
- "this could improve conversion"

That's the hunch. The seed. Don't skip past it — make it clear enough that the team is aligned on what they're actually reacting to.

### Move 2 — Make It Clear

Write the hunch down. Keep it to one sentence. Focus on **what you think is happening, not why it's right**.

Templates:
- "users may not understand what to do on this screen"
- "this version may make the next step clearer"
- "users may not understand what action to take here"
- "this version may improve completion of the next step"

Then connect the hunch to two grounding pieces:
1. **What the user needs** (the User Needs Skill) — what they're trying to do, what they expect, where the experience might break.
2. **What the business is trying to move** (the Business Goals Skill) — what outcome matters, what success looks like.

The work is no longer just team perspective — it's grounded.

### Move 3 — Shape the Signal

Tighten the signal so it can guide a decision. Focus on **one** thing to understand, then anchor it to a UX metric. The four most useful metrics at this stage:

| Metric | When to use it |
|---|---|
| Comprehension | Does the work make sense at a glance? Are users understanding what's shown? |
| Usability | Can users move through the experience without friction? |
| Confidence | Do users feel sure enough about the next step to take it? |
| Desirability | Is the work landing emotionally? Are users drawn to it? |

This gives the team a shared lens. Instead of just reacting, they're looking for something specific.

### Move 4 — Use the Signal

Place the signal next to the directions being considered. Two questions:
- What is the signal telling us to look for?
- How does each option respond to that?

Patterns surface — sometimes one direction is clearly stronger, sometimes both reveal gaps, sometimes the signal itself needs refining. If the signal feels thin, bring in a small amount of input:
- show both directions to a few users
- ask a focused question tied to the metric
- review existing feedback or behavior

The signal brings tradeoffs into view so the team can move.

### Move 5 — Decide What Moves Forward

The decision becomes easier. The team can choose one direction, refine what's there, or stop something that isn't working. The signal gives a shared way to commit.

### Move 6 — Make Decisions Hold

The moment the work moves forward, the decision starts to meander. New people get involved. Details change. Constraints show up.

**The signal is what helps the decision hold.** Keep it visible — not as documentation, but as a shared reference for *why*. When questions come up, bring it back:
- what was the team trying to understand?
- what did the signal show?
- what direction did that lead to?

### What this looks like over time

As the loop repeats — decisions land faster, conversations stay focused, the team builds on what's already been learned, decisions carry across teams, signals connect across decisions, direction holds.

**Start with one decision. Run the loop. Then repeat where it matters.**

### Common stalls and how to unstick

| Stall | What to do |
|---|---|
| Team can't agree on the hunch | Pick the loudest one in conversation; write it as a sentence; iterate |
| Hunch feels too vague | Force one UX metric (comprehension/usability/confidence/desirability) — that's what tightens it |
| Signal points in two directions | The signal needs more refining; or the directions are solving different problems — call that out |
| No real users available | Use the smallest possible input — even 3-5 responses surface a pattern |
| Decision keeps coming back | The signal isn't visible enough — pin it where the work lives, not in a deck |

### Sentence templates

- "We need to understand whether users *[user need]* with this design, because *[business goal]*. We'll use *[UX metric]* to read it."
- "Two directions on *[the work]*. Hunch: *[one-sentence hunch]*. We'll compare them on *[UX metric]* to decide."
- "*[Direction A vs. Direction B]* — testing *[UX metric]* against *[user need]* to inform *[decision being made]*."

---

## 4. Glare + AI workflows

### Why this matters

Product and design work now happens inside fast loops. AI makes it easy to create output — prompts can generate ideas, flows, and variations quickly. Teams can explore more directions in less time. What becomes harder is turning that output into something the team can evaluate, align on, and move forward with confidence.

The gap shows up between creation and decision. **Teams can generate faster than they can decide.** Glare provides structure for that gap.

### The AI workflow — five roles

| Role | What it does |
|---|---|
| **Prompts generate** | Possibilities |
| **Skills shape** | How those possibilities are evaluated |
| **Agents coordinate** | The process |
| **Participant input creates** | Design signals |
| **Teams make** | Decisions with signals |

### Prompts generate

Prompts are the simple entry point. They turn a rough idea into a concept, generate variations, reframe a problem in seconds. They work with ChatGPT, Gemini, etc., and expand the space of possible directions. **Prompts are fast, but they are temporary.** Each prompt is a one-time instruction. Best for exploring ideas, generating variations, reframing questions, surfacing assumptions. They create momentum, but not consistency.

### Skills structure

A Skill is a **reusable, versioned way of working**. The distinction:
- **A prompt defines what to do once.**
- **A Skill defines how to do it consistently.**

Skills shape the work by framing questions as decisions, preparing concepts for testing, defining what should be measured, structuring how options are compared, guiding how results are interpreted. They turn exploration into something the team can rely on.

### Agents orchestrate

Agents coordinate how the work moves. **In Glare, Ray acts as the orchestrator.** It manages the overall goal, determines what needs to happen next, and applies the right Skills at the right time.

- **Agents** manage the goal and sequence of work
- **Skills** provide the repeatable steps to execute it

Example — an agent working toward evaluating a product direction might apply a Skill to structure a test, use another Skill to analyze responses, then compare outcomes across options.

### Human in the loop

Signals and decisions are grounded in people. **Design signals are created from participant input using UX metrics** — they reflect how real users respond to concepts, flows, and experiences. **Decisions are made by teams.** Product, design, and engineering interpret those signals, weigh tradeoffs, and decide what moves forward.

Future direction — agents will progressively be used to make decisions. For now, they support.

**AI supports the work. People determine direction.**

### How it comes together

```
prompt    →  generates an idea or direction
Skill     →  shapes that idea into something testable
agent     →  coordinates the steps needed to evaluate it
participant input  →  creates a signal
team      →  uses that signal to decide what moves forward
```

This loop can run within a single session or extend across a larger cycle. As it repeats, decisions become easier to make and carry forward.

### Try this now

1. Create a signal from collecting user input
2. Choose a prompt to generate new insights
3. Apply a Skill to structure how you evaluate them
4. Collect a small set of user responses
5. Decide what moves forward

You don't need the full system to start. **One signal is enough.**

### Quick reference — prompt vs. Skill vs. agent

| | Prompt | Skill | Agent |
|---|---|---|---|
| Defines | What to do once | How to do something consistently | What goal to pursue and what sequence |
| Reusability | Single use | Reusable, versioned, shareable | Persistent across goal |
| Best for | Exploration, variation, reframing | Decision framing, evaluation, comparison, interpretation | Multi-step coordination across Skills |
| Glare example | "Generate three layout variations of this dashboard" | User Needs Skill, Business Goals Skill, Comparing Skill | Ray |
| Risk if missing | Slow start | Inconsistent evaluation | Steps don't connect |

---

## 5. Coaching and advising — rolling Glare out

### What this is

ZURB's offering for product and design leaders applying Glare inside active work, so teams can turn signals into decisions and decisions into measurable impact. Tagline — *"Level up how your product and design organization makes decisions."*

### Why teams need support now

Most teams are shipping, reviewing, testing, iterating. AI adds even more motion. Teams can explore more options than before. **The harder part is keeping the work connected.**

As output increases, teams need a stronger way to answer — what are we actually deciding? what signal tells us this direction is stronger? how does this connect to user needs? how does it support a business goal? how do we carry the decision forward?

Without structure, teams end up with more output, more feedback, and more meetings, but not stronger decisions. **Coaching helps leaders build the rhythm to keep work moving with clarity.**

### How coaching fits into Glare

Glare gives teams a framework. Coaching helps teams use that framework inside the work they already have. **Not a separate training track** — work happens on active initiatives, real reviews, live decisions, the pressure already sitting inside the team.

Goal — build the muscle to:
- shape hunches into signals
- use AI Skills to structure the work
- bring signals into reviews
- connect decisions to outcomes
- explain design impact in leadership language

This is how Glare moves from documentation into operating rhythm.

### The six components, applied in coaching

- **Design Signals** — connect UX metrics, intuition, direction, context, user needs, business goals into a shared reference point
- **Decision Map** — show where work is getting stuck across Define / Measure / Focus / Lead (with Patterns as the 5th Define block)
- **Design Review** — turn reviews into decision moments instead of feedback meetings
- **UX Metrics** — anchor the team to shared measurement (Attitudinal / Behavioral / Performance / Intelligence)
- **Design Assessment** — surface where the system breaks across the five dimensions

### The 90-day pilot

The starting move — **one team, one initiative, one signal.** A focused 90-day pilot gives leaders enough time to apply the framework, build the rhythm, and show visible progress without turning it into a large transformation program.

**Month 1 — Establish the signal.** Start with one high-leverage initiative. Clarify the business goal, the user need, the decision that needs to be made, the UX metric that helps read the work, and the first signal loop. *Goal — create the first usable signal and show how it can guide a real decision.*

**Month 2 — Build the rhythm.** Coach leaders through the moments where decisions usually fall apart: design reviews, stakeholder conversations, signal interpretation, quality measurement, decision framing. *Goal — make signals part of how the team works, not something that sits outside the process.*

**Month 3 — Scale the model.** Turn what worked into a repeatable model — a quality scorecard, signal patterns, decision review practices, executive-ready proof stories, a roadmap for scaling across more teams. *Goal — help leaders keep using the system after the pilot ends.*

### What your team gets

By the end of the pilot:
- a clearer way to measure design quality
- stronger decision reviews
- faster signal loops
- a simple quality scorecard
- better alignment across product, design, engineering, and leadership
- executive-ready proof narratives
- a repeatable model for turning signals into decisions

**The outcome is not more process. The outcome is a stronger decision system the team can keep using.**

### Who this is for

Heads of Design · Product Design Directors · Product Leaders · UX Research Leaders · DesignOps and ResearchOps leaders · Transformation teams.

Especially useful for teams trying to improve design maturity, introduce AI without creating more noise, reduce rework, prove design impact, build executive trust, or scale design quality across many projects.

### The starting move

**Start with one team, one initiative, and one signal.** You don't need to change the whole organization to start. Pick a team with an important decision. Apply Glare. Create signals. Guide reviews. Build a proof story leaders can use. From there, the model can expand.

---

## 6. Proving design impact

### The thesis

**Design impact becomes visible when decisions connect to outcomes.**

Most teams have no problem showing the work — screens, flows, prototypes, concepts. What's harder is showing what changed *because* of those decisions. That's where design loses leverage.

Rebecca Salerno — *"The hardest part for us right now is connecting design to conversions."*

Glare closes that gap by using design signals to connect the **decision**, the **user response**, and the **outcome the business cares about**. A signal gives the team an early read on whether the decision is creating the change they expected.

**Goal — show how design decisions shape user behavior *before* the final business metric catches up.**

### Start with the decision

Design impact starts when a decision is made. A team chooses one direction. That decision carries an expectation — something should improve for the user, and that improvement should support something the business needs.

Mirjam Amoah — *"The biggest challenge is figuring out together what design is actually supposed to achieve and how to measure that in a meaningful way."*

A strong decision should make these pieces visible:
- what direction was chosen
- what user need it supports
- what UX metric helps read the change
- what business goal it connects to

When those pieces are clear early, impact becomes easier to explain later.

### Make the connection visible

Most teams struggle to prove impact because the parts stay disconnected — design decision in one place, user response in another, business result in a later report. Glare brings them into one chain.

Pablo Zárate — *"Connecting design outcomes to business metrics in a way that isolates design's contribution from other factors."*

Isolation will rarely be perfect. Product work is shared across teams, systems, timing, and market conditions. **But the connection can still be made visible.**

### Use signals as early proof

Business metrics usually move late. Revenue, retention, conversion, cost-to-serve often show up after the work has shipped. By then, it's hard to know which decisions helped.

**Signals give teams something earlier to work with.**

Karline Segan — *"Revenue is a lagging indicator and design needs to articulate our contribution to leading indicators."*

UX metric signals show whether the experience is moving in the right direction *before* the final business outcome appears:

| Leading UX signal | Likely lagging direction |
|---|---|
| Better comprehension | Fewer drop-offs |
| Stronger confidence | Higher completion |
| Improved usability | Less support burden |
| Stronger desirability | Deeper engagement |

**Signals do not replace business metrics. They help explain how design decisions may influence them.**

### Track what design actually changes

Design often changes things that are real but hard to explain in business language — users understand something faster, feel more confident, take less effort, find a choice clearer.

Oluwatobi Okedairo — *"Qualitative value is harder to quantify… These are real improvements, but translating them into KPIs executives care about takes effort and storytelling."*

Useful UX metric signals often show changes in comprehension, confidence, usability, desirability, trust, completion.

### The chain of proof

```
[ DECISION ]
       ↓ informed by
[ DESIGN SIGNAL ]                  ← UX metric + intuition + direction + context + user need + business goal
       ↓ shapes
[ USER BEHAVIOR ]                  ← comprehension, confidence, usability, desirability, trust, completion
       ↓ feeds
[ PRODUCT OUTCOME ]                ← adoption, activation, time on task, engagement
       ↓ moves
[ BUSINESS IMPACT ]                ← revenue, retention, conversion, cost-to-serve, loyalty
```

Worked examples:
- Users understand the onboarding step faster → comprehension improves → fewer users hesitate or abandon → activation has a better chance to increase.
- Users feel more confident choosing a plan → confidence improves → plan comparison becomes easier → conversion has a better chance to improve.

The chain helps leaders understand how design contributes to results without forcing design to claim full ownership of every business metric.

### Tell the impact story — the five-beat narrative

Impact does not become useful just because the data exists. It becomes useful when the team can explain it in a way others can use.

- what decision was made
- what user signal supported it
- what changed in the experience
- what outcome it was meant to influence
- what the team should do next

This moves the conversation away from taste and toward impact.

### Use it in the room

Design impact matters most when decisions are being made. Bring signals into design reviews, roadmap discussions, leadership updates, release decisions, planning conversations.

Emanuele Milella — *"Even if you have data showing design made a difference, convincing others can be harder than producing the results themselves."*

**Proof needs to be usable in the room, not buried in a report.**

### Build proof over time

One signal can guide a decision. Multiple signals create a pattern. As signals build across decisions, design impact becomes easier to explain.

Karline Segan — *"Design creates value across systems and over time, but organizations try to measure it in silos and on an individual basis."*

**Over time, this creates a proof system.** The team is no longer defending one isolated decision — it's showing how design decisions compound into better outcomes.

### What this changes

When design impact is clear, design decisions become easier to defend, signals make tradeoffs visible, outcomes are easier to explain, leadership conversations become more grounded, design gains influence because the value is clearer.

**Proving design impact is not about claiming credit for everything.** It's about showing how design decisions shape user behavior, and how that behavior connects to product and business outcomes. That's how design moves from output to impact.

---

## 7. Glossary

Glare uses a small set of terms to explain how product and design decisions move from uncertainty to impact. This glossary gives each term a simple meaning so teams, leaders, and AI systems can use the same language.

### Core terms

**AI Agent** — An AI system that can manage a goal, choose steps, and use Skills to complete work. In Glare, **Ray** is the orchestrator — it applies Skills, structures input, and coordinates parts of the workflow.

**AI Skill** — A reusable way of working that gives AI and teams a consistent structure to complete a task. A prompt tells AI what to do in one moment; a Skill defines how to do something repeatedly. Skills help teams frame decisions, clarify user needs, connect business goals, shape signals, and interpret results.

**AI Workflow** — The way prompts, Skills, agents, signals, and teams work together to move from idea to decision. Simple flow — prompt generates an idea → Skill structures the work → agent coordinates the steps → participant input creates a signal → team makes the decision.

**Business Goal** — The outcome the team or organization wants to move. Gives the signal direction. Connects design work to what the company cares about — conversion, activation, retention, trust, efficiency, growth.

**Decision** — A clear choice about what moves forward. Might mean choosing one direction, refining an idea, stopping something that's not working, changing scope, or creating another signal. In Glare, decisions are supported by signals.

**Decision Map** — The part of Glare that shows how design signals are strengthened through the work. Organizes decision activity into four facets — Define, Measure, Focus, Lead — connected as a loop.

**Define** — The facet of the Decision Map focused on **clarifying what matters**. Helps teams understand the user need, audience, context, **patterns**, and what success should mean. Five blocks in v1.34 — User Needs · Audience · Collecting · UX Metrics · Patterns.

**Design Assessment** — A way to see how well design decisions move through an organization. Looks across **five dimensions** — Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence. Helps teams see where signals are strong, where decisions break down, where the system needs support.

**Design Impact** — The change created by a design decision. Becomes clearer when a decision connects to a user need, a UX metric, a design signal, and a product or business outcome.

**Design Review** — The moment where work is discussed, evaluated, and expected to move toward a decision. In Glare, Design Review is **where signals are applied** so conversations stay focused and decisions can land. Scored using the SIGNAL rubric — Surface · Identify · Ground · Navigate · Align · Lock.

**Design Signal** — The smallest unit of clarity a team can use to move a decision forward. Connects a UX metric, intuition, direction, context, a user need, and a business goal. Signals help teams understand what users are showing and how that should shape a decision.

**Five dimensions** — The Design Assessment lens — Organizing Work · Managing Complexity · Building Proof · Guiding Decisions · Scaling Influence. Scored across five bands — Reactive · Developing · Functional · Strong · Leading.

**Focus** — The facet of the Decision Map focused on **comparing options and choosing direction**. Helps teams use signals to decide what should move forward. Four blocks — Initiatives · Methods · Comparing · Decisions.

**Hunch** — An early read on the work, **before evidence is clear**. Sounds like "users might get stuck here," "this direction feels stronger," "this could improve conversion." In Glare, a hunch becomes useful when shaped into a signal.

**Intelligence metrics** — The fourth UX metric type. Measure AI-assisted experience quality — recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance. (Note — v1.0 used three metric types; v1.1 briefly added a Perceptual type, then removed; the v3 canonical set is four — Attitudinal, Behavioral, Performance, Intelligence.)

**Intuition** — What the team is noticing based on experience, judgment, and pattern recognition. **Glare does not remove intuition.** It gives intuition structure so teams can connect it to user needs, metrics, and decisions.

**Lead** — The facet of the Decision Map focused on **connecting decisions to outcomes**. Helps teams show how design decisions influence product direction, business goals, and design impact. Four blocks — Business Goals · Mapping · Workflows · Results.

**Master skill** — `glare-master` is the v3 orchestrator across the six components. Replaces the old `glare-router`.

**Measure** — The facet of the Decision Map focused on **understanding how the work performs**. Helps teams choose the UX metrics and input needed to strengthen a signal. Four blocks — Concepts · Hunches · Questioning · Findings.

**Participant Input** — Responses from people who interact with a concept, flow, message, or experience. Helps create or strengthen signals by showing how real users respond.

**Patterns** — The fifth block of Define, added in v1.34. Helps teams recognize recurring situations before weak decisions gain momentum, especially as AI accelerates output faster than evaluation.

**Prompt** — A one-time instruction used with an AI tool. Useful for generating ideas, reframing questions, creating variations, or exploring directions quickly. **Prompts are flexible, but temporary.** Skills make that work repeatable.

**Signal Loop** — The repeatable flow of turning a hunch into a signal and applying it to a decision. Start with a hunch → connect it to user needs and business goals → anchor to a UX metric → apply to a decision → carry the signal forward.

**Six components** — The v3 architecture of Glare — Get Started · Decision Map · Design Review · UX Metrics · Design Signals · Design Assessment. Orchestrated by `glare-master`.

**Tradeoff** — What the team gains or gives up when choosing one direction over another. Signals make tradeoffs easier to see because they show how different options perform against what matters.

**User Need** — What a user is trying to do, understand, feel, or accomplish. Gives the signal its **human anchor**. Without a clear user need, signals can drift toward internal opinion or business-only goals.

**UX Metric** — A measure that helps the team understand how well the experience is working. Organized into four types — Attitudinal (9 metrics — Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness), Behavioral (8 — Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability), Performance (11 — Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency), Intelligence (AI-assisted experience quality). UX metrics help turn user input into signals that can guide decisions.

### Most common term-pair confusions

| Confusion | Resolution |
|---|---|
| Prompt vs. Skill | Prompt = once. Skill = repeatable. |
| Hunch vs. Signal | Hunch = early read. Signal = hunch shaped with UX metric + user need + business goal. |
| Signal vs. UX metric | UX metric = measurement. Signal = metric + intuition + direction + context + user need + business goal. |
| Agent vs. Skill | Agent = manages goal and chooses Skills. Skill = does the repeatable step. |
| Decision Map vs. Design Assessment | Map = how a single decision takes shape. Assessment = how decisions move through the org over time. |
| Decision Map vs. Design Review | Map = the four facets decisions evolve through. Review = the moment signals get applied to land a decision. |
| Define / Measure / Focus / Lead | Facets of the Decision Map. Not stages — teams move back and forth. |
| `glare-master` vs. `glare-getting-started` | Master orchestrates across the six components. Getting Started is the on-ramp inside the Get Started component. |

### Section-level vocabulary — where each term lives

| Term lives in | Skill |
|---|---|
| Design Signal, Hunch, Signal Loop, Intuition, signal types, signal quality | `glare-design-signals` (and nested) |
| Decision Map, Define, Measure, Focus, Lead, Patterns | `glare-decision-map` (and nested facet skills) |
| Design Review, Tradeoff, SIGNAL rubric | `glare-design-review` (and nested) |
| Design Assessment, five dimensions, score bands | `glare-design-assessment` (and nested) |
| UX Metric, four metric types, 28 canonical metrics | `glare-ux-metrics` (and nested) |
| Prompt, AI Skill, AI Agent (Ray), AI Workflow, Participant Input, Business Goal, Design Impact, 90-day pilot | `glare-getting-started` (this skill) |
| Orchestration across all six components | `glare-master` |

---

## How this reference connects to the rest of Glare

This reference is the **on-ramp**. It introduces every component but doesn't go deep on any one. When the user goes deeper, route them out of `glare-getting-started` into the relevant component's skill — and from there, into a nested skill if they're working on a specific facet, dimension, or technique. `glare-master` keeps the chain visible as work moves between components.
