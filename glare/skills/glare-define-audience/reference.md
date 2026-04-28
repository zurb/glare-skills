# Audience — Reference (extracted from define-compressed.md)

## Glare | Define, Audience v1.1 (and v1.0)

- **Audience defines who your signals come from and how much weight each voice should carry.** Without this, customer data, stakeholder opinion, and personal preference all get weighted equally and metrics lose meaning.
- **Four primary audiences:**
  1. **Project Team** — provides *intent* (what we think will work). Light but continuous signal weight.
  2. **Stakeholders** — provide *direction* (what matters most to the business). Medium-to-high weight.
  3. **Customers** — provide *proof* (how it works in real life). Highest weight.
  4. **Participants** — provide *clarity* (how it feels before release). High during testing cycles.
- **Internal voices guide; external voices validate.** Customers confirm what works; participants predict what will.
- **Five core attribute types** (the texture beyond labels): Behavioral, Motivational, Contextual, Lifecycle, Demographic. Use 3–5 attributes total — enough to separate noise from signal.
- **v1.0 attribute taxonomy** (slightly different framing): Targeting, Demographics, Geographics, Psychographics, Behavior.
- **How to define an external audience (6 steps):** start with a question → identify customer vs participant → choose 3–5 attributes → map each to UX metrics → collect and compare → check whether participant signals predict customer behavior.
- **Balance trap:** too much participant data = confident in theory, fragile in practice; too much customer data = solid but slow to iterate.
- **Traps:** designing for "everyone"; over-segmenting until samples are too small; assuming you already know.
- **Proof in practice:** a "customers" group gave contradictory feedback; splitting into *new paying users* (needed trust/reassurance) and *habitual users* (needed speed/control) made signals align and decisions obvious.
- **The flow:** Project Teams form intent → Stakeholders align impact → Participants validate direction → Customers prove outcomes.

## Glare | Define, Audience, Project Team v1.1

- **Project teams are the first audience in Glare** — designers, researchers, engineers translating vision into early versions. Their assumptions are starting signals that need to be made visible and tested.
- **Why it matters:** every prototype/test plan/script carries team bias (how the problem is framed, what success looks like, what feels intuitive). Capturing intent before testing creates a benchmark you can compare belief vs behavior against.
- **Try this:** before each test, have the team list three predictions; review them side by side with results — gaps are where learning lives.
- **Five internal signal types:**
  - **Intent Clarity** — kickoff sessions, design briefs → Alignment, Understanding
  - **Decision Context** — assumption mapping → Comprehension, Traceability
  - **Design Confidence** — confidence survey, pre-test poll → Confidence, Readiness
  - **Iteration Learning** — retros, iteration logs → Speed, Effectiveness
  - **Cross-Discipline Alignment** — team check-ins, alignment maps → Efficiency, Collaboration
- **5-step process:** document intent (one sentence per sprint) → list 3–5 assumptions → assign one metric per assumption → compare to results → share both wins and surprises.
- **Common traps:** Silent Assumptions ("we already know"); Overconfidence (mistaking internal alignment for user understanding); Rush to Output; Disconnected Roles (designers, PMs, engineers defining success differently).
- **Audience build sequence:** Project Teams form intent → Stakeholders align impact → Customers prove outcomes → Participants validate direction.

## Glare | Define, Audience, Stakeholders v1.1

- **Stakeholders = the alignment audience.** They bring influence, resources, and expectations and decide which ideas move forward. Internal (executives, sponsors, program leaders) focus on business outcomes/risk/strategy; External (partners, distributors, agencies, investors, board, analysts) focus on market reach, financials, credibility.
- **Three stakeholder signal types:**
  - **Trust & Confidence** — interviews, short surveys → Confidence Score, Alignment Rating
  - **Clarity of Value** — Glare assessments, review discussions → Comprehension, Satisfaction
  - **Business Readiness** — roadmap checkpoints, exec briefings → Adoption, Momentum, Support Rate
- **Connect design to business workflows** (mapping table):
  - Sales → Revenue/conversion/pipeline → tie usability and clarity to close rates
  - Marketing → Engagement/brand trust → tie satisfaction/sentiment to campaign success
  - Product → Adoption/retention/NPS → tie completion/effort to product outcomes
  - Engineering → Efficiency/stability → use task clarity, time-on-task to validate quality
  - Strategy & Ops → Alignment/process → map design research to org readiness
  - Finance & Legal → Risk/compliance/cost → use trust and comprehension to de-risk change
- **5-step capture process:** Map influencers → Understand workflows → Link metrics to value → Run alignment checks → Show trends, not just results.
- **Traps:** speaking only design language ("delight," "beauty"); skipping business context; ignoring external influence; over-promising signals beyond measurable outcomes.

## Glare | Define, Audience, Customers v1.1

- **Customers = the proof audience.** Their behavior tells the truth internal discussions can't. While teams predict and participants validate, customers *confirm*.
- **Eight customer lifecycle segments** with what to measure for each:
  - **Trial / Pilot Accounts** — first impressions, onboarding clarity → Comprehension, Time on Task, Activation
  - **Freemium Users** — conversion, motivation to upgrade → Completion, Satisfaction, Trust
  - **New Paying Users** — setup success, perceived effort → Completion Rate, Confidence, Error Rate
  - **Habitual Users** — efficiency, reliability → Task Success, Retention, Usability
  - **Power Users** — depth of use, customization → Efficiency, Feature Use, Satisfaction
  - **Advocates** — emotional connection → Sentiment, NPS, Referral Rate
  - **Dormant Accounts** — drop-off causes, reactivation → Frequency, Reactivation Rate, Trust
  - **Churned Accounts** — barriers, exit drivers → Churn Rate, Sentiment, Exit Feedback
- **Five attribute categories** (with what each is best at measuring):
  - **Behavioral** (frequency, tenure, feature adoption, channel, task orientation) → completion, effort, time on task
  - **Motivational** (motivation, risk tolerance, value orientation, decision style, confidence) → satisfaction, trust, sentiment
  - **Contextual** (device, environment, connectivity, workload, collaboration) → error rate, time on task, clarity
  - **Lifecycle** (stage, tenure, activation, frequency, renewal cycle) → retention, activation, loyalty
  - **Demographic** (role, industry, region, age, education) → comprehension, accessibility, inclusivity
- **Use 3–5 attributes** that align with the research goal — attributes structure signals, not describe people.
- **Four metric lenses for customer signals:** by Time (leading vs lagging), by Stage (lifecycle phase), by Type (attitudinal/behavioral/performance), by Engagement (low/medium/high).
- **6-step define-and-measure flow:** start with a question → identify audience type → select key attributes → map attributes to metrics → collect and compare → close the loop (do participant signals predict customer behavior?).

## Glare | Define, Audience, Participants v1.1

- **Participants = the validation audience.** They are the early signal — proxy for reality, helping teams learn faster, spot friction earlier, and replace assumption with evidence before customers see it.
- **Helio context:** over a million participants worldwide. Lesson learned: people are messy and don't fit neat labels — describe by *attribute* (what they do) not by *title*.
- **Three essential questions every participant test answers:** (1) Do people understand what this design is trying to do? (2) Can they complete the main task easily? (3) Does it feel trustworthy enough to continue using?
- **Try this:** invite five adjacent users to complete the main task; track Completion, Confidence, Time on Task; see clarity gaps within an hour.
- **Four phases of participant testing:**
  - **Exploration** — concept/preference testing → attitudinal signals (reactions, mental models)
  - **Definition** — prototype/usability testing → behavioral signals (clarity, flow)
  - **Refinement** — A/B or sequential studies → performance signals (efficiency, trust)
  - **Launch Prep** — benchmark/pilot testing → combined signals (confidence, satisfaction)
- **Four types of participants:** Target Users, Adjacent Users, Informed Outsiders, Internal Proxies. You don't need demographic perfection — you need functional perspectives.
- **Five attribute types** (same taxonomy as Customers, with deeper sub-categories): Behavioral, Motivational, Contextual, Lifecycle, Demographic. Each attribute type maps to a primary signal and a best early metric (e.g., Behavioral → action pattern → Completion Rate; Motivational → emotional driver → Satisfaction; Contextual → environment → Error Rate; Lifecycle → familiarity over time → Retention; Demographic → inclusion/access → Comprehension).
- **6-step study structure:** Start with Purpose → Select 3–5 Attributes → Segment the Group → Run Small Iterative Tests (~100 per round) → Map Results to Metrics → Visualize Insights.
- **Three signal-collection methods:** Attitudinal (surveys, post-task) → Trust/Satisfaction/Comprehension; Behavioral (recordings, heatmaps) → Completion/Effort/Error Rate; Performance (timed tasks, benchmarks) → Time on Task/Success Rate.

## Related key terms

- **Four Audiences** — Project Team (intent), Stakeholders (alignment), Participants (clarity/validation), Customers (proof).
- **Five Attribute Types** — Behavioral, Motivational, Contextual, Lifecycle, Demographic. Use 3–5 to define a testable group.
- **Customer Lifecycle Segments** — Trial, Freemium, New Paying, Habitual, Power, Advocates, Dormant, Churned.
