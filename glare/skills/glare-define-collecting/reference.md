# Collecting Data — Reference (Glare Define, v1.1, 2026-05-06)

## Canonical 28 Metrics

When recommending or naming UX metrics — including which metric a technique or instrument targets — recommend **only** from these 28. Anything else is "outside the canonical 28" and must be flagged with a reason. Translate legacy or shorthand terms in the technique tables below (Efficiency, Trust, Conversion, Visual Attention, Drop-Off, Confidence) into a canonical name or flag them.

### Attitudinal (9) — how users feel

- **Appeal** — strength of attraction or interest the experience generates on first impression.
- **Brand Score** — composite measure of how users perceive and rate the brand.
- **Desirability** — degree to which users want to use, return to, or recommend the experience.
- **Expectations** — alignment between what users anticipate and what they encounter.
- **Feeling** — emotional tone users report after an interaction.
- **Loyalty** — likelihood of repeat use, advocacy, or long-term commitment.
- **Satisfaction** — overall contentment with the experience or outcome.
- **Sentiment** — directional valence (positive / neutral / negative) of expressed user feedback.
- **Usefulness** — perceived value the experience delivers against a user's need.

### Behavioral (8) — what users do

- **Completion** — whether users finish a defined flow or task.
- **Comprehension** — whether users correctly understand content, options, or outcomes.
- **Effort** — perceived or observed work required to reach a goal.
- **Engagement** — depth and quality of interaction with the experience.
- **Frequency** — how often a user performs a behavior in a window of time.
- **Intent** — observable signal of a user's goal or next action.
- **Success** — whether the user achieved the intended outcome of a task.
- **Usability** — overall ease and quality of interacting with the design.

### Performance (11) — efficiency and reliability

- **Abandonment Rate** — share of users who leave a flow before completion.
- **Bounce Rate** — share of sessions that exit after a single page or step.
- **Click-Through Rate** — share of impressions that produced a click on the target element.
- **Completion Rate** — share of users who finish a defined task or flow.
- **Drop-off Rate** — share of users lost at a specific step of a flow.
- **Error Frequency** — count of user-facing errors over a defined window.
- **Error Rate** — share of attempts that produced an error.
- **Recency** — time since a user's last meaningful interaction.
- **Session Duration** — length of a single user session.
- **Time on Task** — time required to complete a defined task.
- **Visit Frequency** — how often a user returns over a defined window.

### Intelligence — in development

The v1.34 UX Metrics framework defines a 4th type for AI-assisted experiences (recommendation quality, prompt effectiveness, AI guidance usefulness, adaptation quality, confidence calibration, workflow assistance), but no canonical per-metric list has shipped yet. Until it does, AI-specific metrics are "outside the canonical 28."

---

## What collecting is for

Collecting turns raw input into usable signals. It is the discipline that prevents drift back into "loudest voice wins." The goal is not more feedback — it is the right data, from the right people, at the right time. One signal can stop wasted effort. Ten can create confidence. A hundred can battle-test a strategy.

**5-section process structure:** Getting Started → Begin Collecting Data → Make It Practical → See It in Action → Apply and Evolve.

**Cadence pattern across all "-ing" pages:** Define → Capture → Connect.

## Within the Define layers (v1.1)

| Section | What it focuses on | How it connects to Collecting |
|---|---|---|
| User Needs | Motivations, expectations, goals | Guides what kinds of questions and signals to collect |
| Audience | The people and contexts you learn from | Defines who you collect data from |
| Collecting | Capturing behavior, perception, reaction | Brings the others together to form the foundation |
| UX Metrics | Measurable attributes of usability/satisfaction | Establishes what to measure and how |

## Four feedback types

Pair at least two so you get *what* and *why*.

| Feedback type | What it captures | Techniques and tools |
|---|---|---|
| **View user data** | Behavior patterns, usage metrics | Analytics, clickstream, heatmaps |
| **See what users do** | Task flows, completion outcomes | Task success testing, first-click, tree testing, time on task |
| **Sense what users like** | Visual attention, emotional response | Desirability studies, emotion tagging, satisfaction surveys, post-task reflection |
| **Hear what users say** | Opinions, expectations, reactions | Surveys, interviews, in-product prompts, video feedback |

---

## Five-step collection process

### Step 1 — Start with Intent

Pair user needs with business goals to create the tension that determines what data matters.

**Example:** Hypothesis: "Users abandon checkout due to unclear pricing." Goal: "Reduce abandonment by 15% this quarter."

User Needs + Business Goals create the tension that makes the right technique obvious.

### Step 2 — Choose Your Stack

Three modes of learning + two stack types.

**Three modes (the mindset behind the research):**

| Mode | When to use | Core question | Techniques / examples | What you get |
|---|---|---|---|---|
| **Exploratory** | Early discovery, before clear hypotheses | "What should we be solving?" | Interviews, journey mapping, diary studies, CASTLE, NASA-TLX | Patterns, context, unmet needs |
| **Evaluative** | Mid-cycle, ideas/designs exist | "Does this design work?" | Card sorting, tree testing, first-click, SUS, SEQ, CES, WAMMI | Clarity, comprehension, usability |
| **Comparative** | Later, choosing between options | "Which version performs better?" | Preference tests, A/B, benchmarking, NPS, SUPR-Q | Directional proof, confidence in a decision |

**Two stack types:**
- **Research Stacks** — reference models for established frameworks (SUS, NPS, etc.).
- **Design Stacks** — practical layers where real concepts get measured. Five Design Stacks: Website, Mobile App, Product, E-commerce, Marketing.

### Step 3 — Identify the Approach

Make sure you are asking the right question. v1.1 cites *Measure: What Makes a Question Testable*:

1. **It defines a gap in understanding.** A good question reveals what you do not yet know.
2. **It points to observable behavior or perception.** You must be able to collect evidence that answers it.
3. **It can be measured.** The result should change what you do next.

When you identify the gap, the right approach (Exploring / Evaluating / Comparing) becomes obvious.

### Step 4 — Apply the Techniques

Match technique to approach and metric.

| Approach | When | Example techniques | Common UX metrics |
|---|---|---|---|
| Exploratory | Identifying opportunities | Interviews, journey mapping, diary studies, card sorting, surveys | Usefulness, Satisfaction, Effort, Trust |
| Evaluative | Testing ideas/prototypes | First-click, task success, time on task, heatmaps, clickstream, usability tests | Completion, Comprehension, Efficiency, Usability |
| Comparative | Choosing between options | A/B testing, preference tests, multivariate, conversion analysis, web analytics, eye tracking | Conversion, Engagement, Desirability, Confidence |

### Step 5 — Connect and ready your data

Three-tier sharing model (v1.1 expansion):

| Type of collection | How it's shared | Why it builds credibility |
|---|---|---|
| **Project-Level Feedback** | Within team in collection tools (Helio, analytics, survey reports) | Keeps data connected to the design artifact |
| **Cross-Team Insights** | Findings area or Glare workspace by concept or metric | Repetition shows what users consistently understand or struggle with |
| **Leadership Rollups** | Key signals + sources in roadmap reviews/KPI discussions | Explains both what you learned and how |

**Show Your Sources** rule: always include techniques used, audience tested, metrics measured.

> Example: "Task success rate from a Helio usability test with 100 mobile app users, measuring Completion and Comprehension."

### Build a consistent UX Metric Stack

| UX Metric Type | What it reveals | Example stack |
|---|---|---|
| **Behavioral** | What users do | Completion Rate · Time on Task · Error Rate |
| **Attitudinal** | What users feel or believe | Satisfaction · Trust · Desirability |
| **Performance** | How efficiently/reliably they succeed | Comprehension · Usability · Efficiency |

---

## The 12 collection techniques

Each technique is repeatable, anchored to UX metrics, and runs lean (small samples often surface clear signals).

### Navigation

**Card Sorting** — *When:* exploratory; designing or auditing IA, taxonomy, labeling. *Produces:* Comprehension, Expectations. *Audience:* 15–30 typical (Optimal Workshop / Treejack). *Constraint:* needs a stable content inventory; open vs. closed sort changes what you learn.

### Task

**First Click Testing** — *When:* evaluative; you suspect users get confused at the first action. *Produces:* Success Rate, Comprehension, Desirability. *Audience:* lean (often 30–100; Helio runs in hours). *Constraint:* needs a single starting screen and one defined task. Bailey's research: correct first click = 87% task completion; wrong first click = 46%.

**Task Success Rate** — *When:* evaluative; checking whether a flow works at all. *Produces:* Completion, Comprehension, Drop-Off. *Audience:* moderate (works at 5+ for qualitative, scale up for benchmarks). *Constraint:* requires a clearly defined task with a binary success criterion.

**Time on Task** — *When:* evaluative; pair with Task Success to see *if* users finish and *how hard* it felt. *Produces:* Efficiency, Success Rate. *Audience:* moderate to large for stable averages. *Constraint:* must be timed in a controlled environment; useless without a baseline.

### Comparison

**A/B Testing** — *When:* comparative; choosing between two live versions. *Produces:* Conversion Rate, Bounce Rate, Engagement. *Audience:* large (statistical power needed; typically thousands of sessions). *Constraint:* requires live traffic, a single variable change, and an experimentation tool (Optimizely, VWO, Google Optimize).

**Multivariate Testing** — *When:* comparative; testing combinations of elements (headline + image + CTA). *Produces:* CTR, Comprehension, Desirability. *Audience:* very large (more variants = more traffic needed). *Constraint:* exponential sample-size growth with each variable; only viable on high-traffic surfaces.

**Conversion Rate Analysis** — *When:* comparative/behavioral; measuring whether users complete the goal action. *Produces:* Success Rate, Drop-Off, Desirability. *Audience:* large. *Constraint:* needs a defined funnel and goal event.

### Behavior

**Heatmaps** — *When:* behavioral; you want to see where attention and clicks land on a page. *Produces:* Desirability, CTR, Comprehension. *Audience:* moderate to large (~1,000+ for patterns). *Constraint:* requires a tracking script (Hotjar, FullStory, CrazyEgg); shows *where* not *why*.

**Clickstream Analysis** — *When:* behavioral; mapping how users move through a multi-step flow. *Produces:* Drop-Off, Efficiency, Frequency. *Audience:* large (needs enough flow completions). *Constraint:* requires event instrumentation (Pendo, Heap, Mixpanel).

**Web Analytics** — *When:* behavioral; site-wide health and trends. *Produces:* Session Duration, Bounce Rate, Conversion Rate. *Audience:* whole-site traffic. *Constraint:* lagging signal; never use alone — pair with attitudinal.

### Feedback

**Surveys & Questionnaires** — *When:* exploratory or feedback; capturing what users think and feel at scale. *Produces:* Usefulness, Satisfaction, Loyalty. *Audience:* flexible — 30 for directional, hundreds for benchmarks. *Constraint:* question-writing discipline matters more than sample size; pair with behavioral data.

**Eye Tracking** — *When:* specialized; you need to know what users *see vs. miss*. *Produces:* Comprehension, Efficiency, Visual Attention. *Audience:* small (10–30, expensive per session). *Constraint:* requires hardware (Tobii, RealEye) or webcam-based eye tracking; lab or remote-controlled environment.

### 5-step usage discipline

1. Pick the metric.
2. Choose the technique.
3. Run lean (small samples often surface clear signals).
4. Pair techniques (Task Success + Time on Task; Survey + Heatmap).
5. Frame results as signals tied to a UX metric, never as raw output.

### Traps

- Running techniques without metrics ("a card sort is just boxes" without a comprehension/usability target).
- Overcomplicating sample sizes.
- One-and-done research.
- Reporting raw counts instead of signals.

---

## Research Stacks — named instruments

Research stacks turn familiar methods into UX-metric-aligned signals.

### Three stack types

- **Exploratory** — surface needs/opportunities → attitudinal metrics. Examples: interviews, diary studies, journey mapping.
- **Evaluative** — test if a design works → behavioral and performance metrics. Examples: SUS, first-click testing.
- **Comparative** — show what works better → outcome metrics. Examples: preference tests, benchmarking, A/B testing.

### Common instruments

| Family | Instruments |
|---|---|
| **Usability & Ease** | SUS (System Usability Scale → usability/engagement/usefulness); SEQ (Single Ease Question → completion/success/satisfaction); PURE (expert-rated difficulty); SUMI (efficiency/control) |
| **Effort & Workload** | CES (Customer Effort Score); CASTLE (task load/efficiency); NASA-TLX (workload) |
| **Satisfaction & Experience** | WAMMI (website satisfaction); PSSUQ (post-task satisfaction); QUIS (interface satisfaction); UEQ (emotional experience); UX-Lite (quick UX snapshot); SUPR-Q (website benchmark) |
| **Trust & Loyalty** | NPS (likelihood to recommend); L-DERLY (learnability/expectation gap) |

### 5-step usage

1. Start with the decision (explore/validate/compare).
2. Choose matching stack.
3. Map methods to Glare metrics.
4. Pair stacks when needed.
5. Share results as signals tied to metrics leaders trust.

---

## Tools — four-axis framework

Start with the metric, not the tool. Tools are infrastructure for capturing UX metrics; the wrong tool buries teams in noise.

| Axis | Captures | Named platforms |
|---|---|---|
| **View user data** | Analytics | Google Analytics, Mixpanel, Amplitude, Pendo, Heap |
| **See what users do** | Recordings, heatmaps | Hotjar, FullStory, CrazyEgg, Smartlook |
| **Sense what users like** | Eye tracking, appeal | UsabilityHub, Helio, Tobii, RealEye |
| **Hear what users say** | Surveys, feedback | Typeform, SurveyMonkey, Qualtrics, Sprig, Delighted, Qualaroo |

### Four tool buckets with named platforms

- **Attitudinal Tools:** Surveys (Typeform, SurveyMonkey, Qualtrics); In-product feedback (Sprig, Delighted, Qualaroo); Preference testing (UsabilityHub, Helio); Benchmarking (NPS, CES, CSAT) → satisfaction, trust, desirability, sentiment, brand score
- **Behavioral Tools:** Analytics (Google Analytics, Mixpanel, Amplitude); Session replay & heatmaps (Hotjar, FullStory, CrazyEgg, Smartlook); Clickstream (Pendo, Heap); Navigation testing (Treejack, Optimal Workshop) → completion, engagement, navigation paths, usability
- **Performance Tools:** Usability platforms (UserTesting, Maze, UserZoom); A/B & multivariate (Optimizely, VWO, Google Optimize); Task timing & error (Helio, Lookback); System monitoring (Pingdom, New Relic, Load Impact) → time on task, error rate, drop-off, task success
- **Specialized Tools:** Eye tracking (Tobii, RealEye); Biometrics & emotion (iMotions, Affectiva); Privacy-first analytics (Fathom, Plausible); Emerging (AR/VR usability, AI-driven sentiment) → attention, emotional response, advanced trust/performance

### 4-step usage

1. Start with the metric.
2. Match the tool.
3. Pair tools (survey + heatmap to see what users say *and* where they click).
4. Stay lean.

### Traps

- Collecting everything.
- Tool sprawl.
- Over-relying on one type (e.g., analytics without attitudinal).

---

## See it in action

A university struggled with navigation. Meetings circled for weeks. Everyone had an opinion. Nothing moved. The team chose the Evaluative stack, ran a preference test, and used Helio. Within hours: hamburger menu lifted usability 14% and positive impressions 41%. Signals beat opinions.

## Practical worksheet

| Step | Action | Output |
|---|---|---|
| 1. Define Stack | Select exploratory, evaluative, or comparative | Clear purpose for data collection |
| 2. Choose Technique | Identify the method | Plan for measurable signals |
| 3. Select Tools | Pick tools that match speed and fidelity | Ready-to-run setup |
| 4. Identify Audience | Outline who you'll learn from | Defined sample of real decision-makers |
| 5. Link to UX Metrics | Connect outcomes to indicators | Structured proof of what worked |

## Next steps (v1.1 transitions)

| If you are here | Move to | What you gain |
|---|---|---|
| Questioning | → Collecting | Turn intent into evidence |
| Collecting | → Findings | Find clarity in what you gathered |
| Comparing | → Mapping | Translate clarity into measurable impact |

A Design Signal is what happens when data starts to make sense. It is the moment evidence becomes direction.

## Related key terms

- **Three Modes of Learning** — Exploratory, Evaluative, Comparative.
- **Research Stacks vs Design Stacks** — Research = reference instruments; Design = practical layers (Website, Mobile App, Product, E-commerce, Marketing).
- **Define → Capture → Connect** — the cadence pattern across all "-ing" pages in Glare.
- **Design Signal** — what data becomes when patterns make sense.
- **Helio** — in-house testing platform; signals in hours; 1M+ participants.
- **The 12 techniques** — First Click, Task Success Rate, Time on Task, A/B, Multivariate, Heatmaps, Clickstream, Web Analytics, Conversion Rate Analysis, Eye Tracking, Card Sorting, Surveys & Questionnaires.

## v1.1 deltas

The five-step process, three modes, four feedback types, Design Stacks list, worksheet, and Helio proof-in-practice are unchanged from v1.0. v1.1 adds:

- **"Within the Define Layers" table** — explicitly positions Collecting alongside User Needs, Audience, UX Metrics.
- **Named instruments now appear inside the Modes of Learning table** (CASTLE, NASA-TLX in Exploratory; SUS, SEQ, CES, WAMMI in Evaluative; NPS, SUPR-Q in Comparative).
- **Step 3 cites "What Makes a Question Testable"** — three principles for a testable question.
- **Step 5 expanded into a three-tier sharing model** with Show Your Sources guidance.
- **"Next Steps" transition table** — Questioning → Collecting → Findings → Mapping.
