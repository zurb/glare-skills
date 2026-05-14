# Audience — Reference (Glare Define, v1.1, 2026-05-06)

## When to use

- When the user is defining WHO their signals should come from before collecting data.
- When customer data, stakeholder opinion, and personal preference are being weighted equally and metrics lose meaning.
- When picking among the four audiences (Project Team, Stakeholders, Customers, Participants) or the eight Customer lifecycle segments.
- When choosing 3–5 attributes (Behavioral, Motivational, Contextual, Lifecycle, Demographic) to turn a vague group into a testable one.
- When balancing fast participant signals against slow customer evidence.

**Don't use when** naming the underlying need (use `glare-define-user-needs`), choosing techniques/instruments (`glare-define-collecting`), or picking metrics (`glare-define-ux-metrics`).

## The four-voice frame

Audience defines who your signals come from and how much weight each voice should carry. Without it, customer data, stakeholder opinion, and personal preference all get weighted equally — and metrics lose meaning. Glare extends "audience" beyond marketing-style segments to include anyone whose perspective influences design decisions.

| Audience | Provides | Feedback type | Collection method | Signal weight |
|---|---|---|---|---|
| **Project Team** | Intent (what we think will work) | Design intent, feasibility, internal reflection | Design reviews, retrospectives, pre-test alignment | Light but continuous |
| **Stakeholders** | Direction (what matters most to the business) | Business alignment, trust, impact expectations | 1-on-1s, Glare assessments, exec reviews | Medium to high |
| **Customers** | Proof (how it works in real life) | Real behavior, satisfaction, adoption | Usability tests, analytics, surveys, feedback loops | Highest |
| **Participants** | Clarity (how it feels before release) | Prototype validation, early testing | Concept tests, audience panels, research studies | High during testing cycles |

**Internal voices guide; external voices validate.** Customers confirm what works; participants predict what will.

**Audience-build sequence:** Project Teams form intent → Stakeholders align impact → Participants validate direction → Customers prove outcomes.

---

## 1. Project Team — the intent audience

**Why they matter:** Every prototype, test plan, and research script carries team bias — how problems are framed, what success looks like, what feels intuitive. Capturing intent before testing creates a benchmark you can compare belief vs. behavior against.

**Try this:** Before each test, have the team list three predictions; review side by side with results. The gaps are where learning lives.

### Five internal signal types

| Feedback | What it reveals | Example activity | Related metrics |
|---|---|---|---|
| **Intent Clarity** | Whether goals and definitions are shared | Kickoff sessions, design briefs | Alignment, Understanding |
| **Decision Context** | How rationale and trade-offs are documented | Assumption mapping | Comprehension, Traceability |
| **Design Confidence** | How the team rates confidence before validation | Confidence survey, pre-test poll | Confidence, Readiness |
| **Iteration Learning** | How fast insights lead to changes | Retros, iteration logs | Speed, Effectiveness |
| **Cross-Discipline Alignment** | Whether roles and ownership are clear | Team check-ins, alignment maps | Efficiency, Collaboration |

### 5-step capture process

1. Document Intent (one sentence per sprint).
2. List 3–5 Assumptions about what users will do or value.
3. Assign Metrics — link each assumption to one measurable outcome.
4. Compare to Results — evaluate predictions vs. reality.
5. Share Learnings — both wins and surprises.

### Common traps

- **Silent Assumptions** — "we already know."
- **Overconfidence** — mistaking internal alignment for user understanding.
- **Rush to Output** — launching tests before clarifying what the team hopes to learn.
- **Disconnected Roles** — designers, PMs, engineers defining success differently.

---

## 2. Stakeholders — the alignment audience

Stakeholders bring influence, resources, and expectations and decide which ideas move forward. They are not just "approvers" — they connect design signals to business priorities.

**Internal stakeholders:** executives, project sponsors, program leaders. Focus: business outcomes, risk, alignment with strategy.
**External stakeholders:** partners, distributors, agencies, consultants, investors, board members, analysts. Focus: market reach, financial results, credibility, competitive standing.

### Three stakeholder signal types

| Signal type | What it reveals | Collection method | Example metrics |
|---|---|---|---|
| **Trust & Confidence** | Whether design progress feels credible | Stakeholder interviews, short surveys | Confidence Score, Alignment Rating |
| **Clarity of Value** | How well design impact is understood | Glare assessments, review discussions | Comprehension, Satisfaction |
| **Business Readiness** | If leadership feels prepared to act on outcomes | Roadmap checkpoints, exec briefings | Adoption, Momentum, Support Rate |

### Connect design to business workflows

| Workflow | Stakeholder priority | How design connects |
|---|---|---|
| **Sales** | Revenue, conversion, pipeline | Show how usability and clarity improve close rates |
| **Marketing** | Engagement, brand trust | Connect satisfaction and sentiment to campaign success |
| **Product** | Adoption, retention, NPS | Tie completion and effort to product outcomes |
| **Engineering** | Efficiency, stability | Use task clarity, time-on-task to validate quality |
| **Strategy & Operations** | Alignment, process | Map design research to org readiness |
| **Finance & Legal** | Risk, compliance, cost | Use trust and comprehension signals to de-risk change |

### 5-step capture process

1. Map the influencers (internal + external).
2. Understand their workflows (revenue, retention, satisfaction, risk).
3. Link metrics to value (translate UX signals into business impact).
4. Run alignment checks (Glare assessments, short interviews).
5. Show trends, not just results.

### Common traps

- Talking only in design terms ("delight," "beauty") that don't translate to stakeholder goals.
- Skipping context — presenting results without showing how they fit existing workflows.
- Ignoring external influence — partners and investors shape internal approval.
- Over-promising signals beyond measurable outcomes.

---

## 3. Customers — the proof audience

Customer behavior tells the truth internal discussions can't. While teams predict and participants validate, customers *confirm*.

### Eight customer lifecycle segments

| Segment | Role in lifecycle | What to measure | Key metrics |
|---|---|---|---|
| **Trial / Pilot Accounts** | Early exploration of fit | First impressions, onboarding clarity | Comprehension, Time on Task, Activation |
| **Freemium Users** | Sampling value without commitment | Conversion behavior, motivation to upgrade | Completion, Satisfaction, Trust |
| **New Paying Users** | First experience after purchase | Setup success, perceived effort | Completion Rate, Confidence, Error Rate |
| **Habitual Users** | Regular consistent use | Efficiency, reliability | Task Success, Retention, Usability |
| **Power Users** | Advanced use, mastery | Performance, depth, customization | Efficiency, Feature Use, Satisfaction |
| **Advocates** | Loyal promoters | Emotional connection, advocacy | Sentiment, NPS, Referral Rate |
| **Dormant Accounts** | Decreased activity | Drop-off causes, reactivation | Frequency, Reactivation Rate, Trust |
| **Churned Accounts** | Former users who left | Barriers, unmet needs | Churn Rate, Sentiment, Exit Feedback |

### Five attribute categories

| Type | Examples | Best at measuring |
|---|---|---|
| **Behavioral** | Frequency, tenure, feature adoption, channel | Completion, effort, time on task |
| **Motivational** | Motivation, risk tolerance, value orientation | Satisfaction, trust, sentiment |
| **Contextual** | Device, environment, connectivity, workload | Error rate, time on task, clarity |
| **Lifecycle** | Stage, tenure, activation, frequency | Retention, activation, loyalty |
| **Demographic** | Role, industry, region, age | Comprehension, accessibility, inclusivity |

Use 3–5 attributes that align with the research goal.

### Four metric lenses for customer signals

- **By Time** — leading vs. lagging
- **By Stage** — lifecycle phase
- **By Type** — attitudinal/behavioral/performance
- **By Engagement** — needs/behavior/activity

### 6-step define-and-measure flow

1. Start with a question.
2. Identify the audience type (customer vs. participant).
3. Select key attributes (3–5).
4. Map attributes to metrics.
5. Collect and compare signals.
6. Close the loop — do participant signals predict customer behavior?

---

## 4. Participants — the validation audience

Participants are the early signal — proxy for reality, helping teams learn faster, spot friction earlier, and replace assumption with evidence before customers see it.

**Helio context:** over a million participants worldwide. Lesson learned: people are messy and don't fit neat labels. Describe by *attribute* (what they do) not by *title*. "Manager" tells you little. "Manages budgets and makes hiring decisions" tells you exactly how the person works.

### Three essential questions every participant test answers

1. Do people understand what this design is trying to do?
2. Can they complete the main task easily?
3. Does it feel trustworthy enough to continue using?

**Try this:** Invite five adjacent users to complete the main task. Track Completion, Confidence, Time on Task. See clarity gaps within an hour.

### Four phases of participant testing

| Phase | Purpose | Participant signal | Example method |
|---|---|---|---|
| **Exploration** | Discover what users expect | Attitudinal — reactions, mental models | Concept or preference testing |
| **Definition** | Identify friction, test comprehension | Behavioral — clarity, flow | Prototype or usability testing |
| **Refinement** | Compare alternatives | Performance — efficiency, trust | A/B or sequential studies |
| **Launch Prep** | Confirm readiness and alignment | Combined — confidence, satisfaction | Benchmark or pilot testing |

### Four types of participants

| Category | Description | When to use |
|---|---|---|
| **Target Users** | Match your core audience | When validating primary experiences |
| **Adjacent Users** | Use similar tools/workflows | For early concepts or competitor insights |
| **Informed Outsiders** | Bring unbiased perspectives | When testing comprehension or messaging |
| **Internal Proxies** | Team members as structured stand-ins | When external access is limited |

You don't need demographic perfection. You need functional perspectives.

### Attribute and metric summary

| Attribute type | Primary signal | Best early metric |
|---|---|---|
| **Behavioral** | Action pattern | Completion Rate |
| **Motivational** | Emotional driver | Satisfaction |
| **Contextual** | Environment | Error Rate |
| **Lifecycle** | Familiarity over time | Retention |
| **Demographic** | Inclusion and access | Comprehension |

### 6-step study structure

1. Start with Purpose — what decision will this test inform?
2. Select Attributes — 3–5 that reflect your learning goal.
3. Segment the Group — recruit participants representing those traits.
4. Run Small, Iterative Tests — 100 per round is usually enough.
5. Map Results to Metrics — compare across segments to identify friction.
6. Visualize Insights — Glare signal charts to show clarity over time.

### Three signal-collection methods

| Signal type | What it reveals | Collection method | Example UX metrics |
|---|---|---|---|
| **Attitudinal** | First impressions, confidence | Surveys, post-task reflections | Trust, Satisfaction, Comprehension |
| **Behavioral** | Observable actions, pathways | Screen recordings, heatmaps | Completion, Effort, Error Rate |
| **Performance** | Efficiency, task fluency | Timed tasks, success benchmarks | Time on Task, Success Rate |

---

## Balance trap (between participants and customers)

| Over-reliance | What happens | Signal impact |
|---|---|---|
| Too much participant data | Fast insights, limited real-world validation | Confident in theory, fragile in practice |
| Too much customer data | Accurate proof, slower iteration | Solid performance, slow improvement |

Collect fast signals from participants to guide direction, then slow signals from customers to confirm results.

## Failure modes

These are common ways this skill goes wrong in practice:

- **"Designing for everyone."** When the audience is "all users," signals end up too generic to act on and stakeholders fill the gap with their own version. Pick a primary audience, name it explicitly, then check adjacent users.
- **Over-relying on participant data.** Fast, recruited testing produces clean signals but doesn't validate against real-world friction. Pair participant signals with customer behavior data before committing.
- **Over-relying on customer data.** Existing customer behavior reflects what users already do, not what users are trying to do — so it can lock the team into improving the wrong thing. Pair with participant signals from target and adjacent users.
- **Picking too many attributes.** Beyond 5 attributes the audience becomes unrecruitable and the signals stop comparing. 3–5 is the working range.
- **Ignoring the lifecycle stage.** Treating a Trial user and a Power user as the same audience erases the most important context. Always name which of the eight lifecycle segments the audience sits in.

## Related key terms

- **Four Audiences** — Project Team (intent), Stakeholders (alignment), Participants (clarity/validation), Customers (proof).
- **Five Attribute Types** — Behavioral, Motivational, Contextual, Lifecycle, Demographic. Use 3–5 to define a testable group.
- **Customer Lifecycle Segments** — Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned.
- **Four Participant Phases** — Exploration, Definition, Refinement, Launch Prep.
- **Four Participant Types** — Target, Adjacent, Informed Outsiders, Internal Proxies.
