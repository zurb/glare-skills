# Collecting Data — Reference (extracted from define-compressed.md)

## Glare | Define, Collecting v1.1 (and v1.0)

- **Collecting = turn raw input into usable signals.** It is the discipline that prevents drift back into "loudest voice wins."
- **5-section process structure:** Getting Started → Begin Collecting Data → Make It Practical → See It in Action → Apply and Evolve.
- **Cadence pattern across all "-ing" pages:** Define → Capture → Connect.
- **Four feedback types** (use to balance quantitative and qualitative):
  - **View user data** — analytics, clickstream, heatmaps
  - **See what users do** — task success, first-click, tree testing, time on task
  - **Sense what users like** — desirability, emotion tagging, satisfaction surveys
  - **Hear what users say** — surveys, interviews, in-product prompts, video feedback
- **Five-step collection process:**
  1. **Start with Intent** — pair user needs with business goals to create the tension that determines what data matters. Example hypothesis: "Users abandon checkout due to unclear pricing"; goal: "Reduce abandonment by 15% this quarter."
  2. **Choose Your Stack** — Research Stacks are reference; Design Stacks are practical. Three modes: Exploratory ("What should we be solving?"), Evaluative ("Does this design work?"), Comparative ("Which performs better?"). Five Design Stacks: Website, Mobile App, Product, E-commerce, Marketing.
  3. **Identify the Approach** — confirm question reveals a knowledge gap, points to observable behavior, and is measurable. Map to Exploring, Evaluating, or Comparing.
  4. **Apply the Techniques** — match to UX metrics: Exploratory (interviews, journey maps, diary studies, card sorting, surveys → usefulness, satisfaction, effort, trust); Evaluative (first-click, task success, time on task, heatmaps, clickstream, usability tests → completion, comprehension, efficiency, usability); Comparative (A/B, preference, multivariate, conversion, web analytics, eye tracking → conversion, engagement, desirability, confidence).
  5. **Connect and ready your data** — share at three levels: project (in the same tool), cross-team (Findings or Glare workspace by concept/metric), leadership (roadmap reviews/KPI). Always cite techniques + audience + metrics in any shared finding.
- **Build a consistent UX Metric Stack:** Behavioral (Completion, Time on Task, Error Rate); Attitudinal (Satisfaction, Trust, Desirability); Performance (Comprehension, Usability, Efficiency).
- **Transitions out:** Collecting → Measuring (calibrated benchmarks) → Compare (validate signals against outcomes). A "Design Signal" is the moment data starts to make sense — evidence becomes direction.
- **Practical worksheet:** Define Stack → Choose Technique → Select Tools → Identify Audience → Link to UX Metrics.
- **Proof in practice:** university navigation case — Evaluative stack + preference test + Helio = 14% usability lift in hours; signals beat opinions.

## Glare | Define, Collecting, Research Stacks v1.0

- **Research stacks turn familiar methods (NPS, SUS, A/B) into UX-metric-aligned signals** instead of isolated scores.
- **Three stack types:**
  - **Exploratory Stacks** — surface needs/opportunities → attitudinal metrics (satisfaction, usefulness). Examples: interviews, diary studies, journey mapping.
  - **Evaluative Stacks** — test if a design works → behavioral and performance metrics (task success, time on task, usability). Examples: SUS, first-click testing.
  - **Comparative Stacks** — show what works better → outcome metrics (preference, comprehension, engagement). Examples: preference tests, benchmarking, A/B testing.
- **Common research stacks (named instruments):**
  - **Usability & Ease:** SUS (System Usability Scale → usability/engagement/usefulness); SEQ (Single Ease Question → completion/success/satisfaction); PURE (expert-rated difficulty → completion/satisfaction/feeling); SUMI (efficiency/control → completion/usability/satisfaction)
  - **Effort & Workload:** CES (Customer Effort Score → completion/effort); CASTLE (task load/efficiency → task load/efficiency/usability/comprehension); NASA-TLX (workload → usability/usefulness/feeling/satisfaction)
  - **Satisfaction & Experience:** WAMMI (website satisfaction → appeal/usability/helpfulness/comprehension); PSSUQ (post-task satisfaction → engagement/usability/usefulness/feeling); QUIS (interface satisfaction); UEQ (emotional experience → usability/sentiment/reaction/loyalty); UX-Lite (quick UX snapshot → usefulness); SUPR-Q (website benchmark → usability/loyalty/sentiment/reaction)
  - **Trust & Loyalty:** NPS (likelihood to recommend → loyalty); L-DERLY (learnability/expectation gap → expectations/usability/usefulness/comprehension)
- **5-step usage:** start with the decision (explore/validate/compare) → choose matching stack → map methods to Glare metrics → pair stacks when needed → share results as signals tied to metrics leaders trust.
- **Traps:** treating methods in isolation; overusing one stack (interviews can't validate usability; A/B can't uncover unmet needs); skipping alignment.
- **Proof in practice:** retail team ran SUS aligned to usability/task success; SUS dropped below 50; redesign became urgent because the data was undeniable.

## Glare | Define, Collecting, Techniques v1.0

- **Techniques = repeatable research methods anchored to UX metrics.** They sit beneath stacks and tools as the tactical layer.
- **Five categories with examples → metrics tracked:**
  - **Navigation:** Card Sorting, Tree Testing → comprehension, expectations
  - **Task:** Task Success, Time on Task, SEQ → completion, effort, efficiency
  - **Comparison:** A/B Testing, Preference, Multivariate → conversion, desirability, comprehension
  - **Behavior:** Heatmaps, Clickstream, Web Analytics → attention, engagement, frequency
  - **Feedback:** Surveys, Questionnaires, Eye Tracking → satisfaction, sentiment, loyalty
- **Master technique table (verbatim mapping):**
  - First Click Testing → Success Rate, Comprehension, Desirability
  - Task Success Rate → Completion, Comprehension, Drop-Off
  - Time on Task → Efficiency, Success Rate
  - A/B Testing → Conversion Rate, Bounce Rate, Engagement
  - Multivariate Testing → CTR, Comprehension, Desirability
  - Heatmaps → Desirability, CTR, Comprehension
  - Clickstream Analysis → Drop-Off, Efficiency, Frequency
  - Web Analytics → Session Duration, Bounce Rate, Conversion Rate
  - Conversion Rate Analysis → Success Rate, Drop-Off, Desirability
  - Eye Tracking → Comprehension, Efficiency, Visual Attention
  - Card Sorting → Comprehension, Expectations
  - Surveys & Questionnaires → Usefulness, Satisfaction, Loyalty
  - Quantitative Template → custom mapping
- **5-step usage:** pick the metric → choose the technique → run lean (small samples) → pair techniques (Task Success + Time on Task) → frame results as signals not raw output.
- **Traps:** running techniques without metrics ("a card sort is just boxes" without a comprehension/usability target); overcomplicating; one-and-done.
- **Proof in practice:** university first-click test (Helio) → 14% comprehension lift in hours, ending weeks of debate.

## Glare | Define, Collecting, Tools v1.0

- **Start with the metric, not the tool.** Tools are infrastructure for capturing UX metrics; the wrong tool buries teams in noise.
- **Four-axis framework for tool selection:** View user data (analytics) → See what users do (recordings, heatmaps) → Sense what users like (eye tracking, appeal) → Hear what users say (surveys, in-product feedback).
- **Four tool categories (with named platforms):**
  - **Attitudinal Tools:** Surveys (Typeform, SurveyMonkey, Qualtrics); In-product feedback (Sprig, Delighted, Qualaroo); Preference testing (UsabilityHub, Helio); Benchmarking (NPS, CES, CSAT) → satisfaction, trust, desirability, sentiment, brand score
  - **Behavioral Tools:** Analytics (Google Analytics, Mixpanel, Amplitude); Session replay & heatmaps (Hotjar, FullStory, CrazyEgg, Smartlook); Clickstream (Pendo, Heap); Navigation testing (Treejack, Optimal Workshop) → completion, engagement, navigation paths, usability
  - **Performance Tools:** Usability platforms (UserTesting, Maze, UserZoom); A/B & multivariate (Optimizely, VWO, Google Optimize); Task timing & error (Helio, Lookback); System monitoring (Pingdom, New Relic, Load Impact) → time on task, error rate, drop-off, task success
  - **Specialized Tools:** Eye tracking (Tobii, RealEye); Biometrics & emotion (iMotions, Affectiva); Privacy-first analytics (Fathom, Plausible); Emerging (AR/VR usability, AI-driven sentiment) → attention, emotional response, advanced trust/performance
- **4-step usage:** start with the metric → match the tool → pair tools (survey + heatmap to see what users say *and* where they click) → stay lean.
- **Traps:** collecting everything; tool sprawl; over-relying on one type (e.g., analytics without attitudinal).
- **Proof in practice:** fintech tracked onboarding with analytics only; saw 70% completion and assumed success. Pairing with Helio surveys revealed users felt confused even while finishing — the fix came from combining tools.

## Related key terms

- **Three Modes of Learning** — Exploratory, Evaluative, Comparative.
- **Research Stacks vs Design Stacks** — Research = reference instruments (SUS, NPS, etc.); Design = practical layers where concepts get measured (Website, Mobile App, Product, E-commerce, Marketing).
- **Define → Capture → Connect** — the cadence pattern across all "-ing" pages in Glare.
- **Design Signal** — what data becomes when patterns make sense; evidence turning into direction.
- **Helio** — the in-house testing platform referenced throughout (used for first-click tests, preference tests, surveys, usability tests; gives signals in hours not weeks; 1M+ participants run through it).
- **Four named research instruments worth knowing:** SUS, SEQ, NPS, CES (plus PURE, SUMI, CASTLE, NASA-TLX, WAMMI, PSSUQ, QUIS, UEQ, UX-Lite, SUPR-Q, L-DERLY).

## Techniques deep dive

Source: *Glare | Define, Collecting, Techniques v1.0* (Sept 20, 2025). Techniques are the tactical layer beneath stacks and tools. Each one must be anchored to a UX metric or it is "just boxes." Below is the full catalog with usage guidance synthesized from the doc; audience sizes and constraints are noted where the doc specifies them or where the "run lean" guidance applies.

- **First Click Testing** — *When:* evaluative; you suspect users get confused at the first action. *Produces:* Success Rate, Comprehension, Desirability. *Audience:* lean (often 30–100; Helio runs in hours). *Constraint:* needs a single starting screen and one defined task; best for surfacing confusion before it compounds.
- **Task Success Rate** — *When:* evaluative; checking whether a flow works at all. *Produces:* Completion, Comprehension, Drop-Off. *Audience:* moderate (works at 5+ for qualitative, scale up for benchmarks). *Constraint:* requires a clearly defined task with a binary success criterion.
- **Time on Task** — *When:* evaluative; pair with Task Success to see *if* users finish and *how hard* it felt. *Produces:* Efficiency, Success Rate. *Audience:* moderate to large for stable averages. *Constraint:* must be timed in a controlled environment; useless without a baseline.
- **A/B Testing** — *When:* comparative; choosing between two live versions. *Produces:* Conversion Rate, Bounce Rate, Engagement. *Audience:* large (statistical power needed; typically thousands of sessions). *Constraint:* requires live traffic, a single variable change, and an experimentation tool (Optimizely, VWO, Google Optimize).
- **Multivariate Testing** — *When:* comparative; testing combinations of elements (headline + image + CTA). *Produces:* CTR, Comprehension, Desirability. *Audience:* very large (more variants = more traffic needed). *Constraint:* exponential sample-size growth with each variable; only viable on high-traffic surfaces.
- **Heatmaps** — *When:* behavioral; you want to see where attention and clicks land on a page. *Produces:* Desirability, CTR, Comprehension. *Audience:* moderate to large (needs enough sessions to form a pattern, ~1,000+). *Constraint:* requires a tracking script (Hotjar, FullStory, CrazyEgg); shows *where* not *why*.
- **Clickstream Analysis** — *When:* behavioral; mapping how users move through a multi-step flow. *Produces:* Drop-Off, Efficiency, Frequency. *Audience:* large (needs enough flow completions to see patterns). *Constraint:* requires event instrumentation (Pendo, Heap, Mixpanel).
- **Web Analytics** — *When:* behavioral; site-wide health and trends. *Produces:* Session Duration, Bounce Rate, Conversion Rate. *Audience:* whole-site traffic. *Constraint:* lagging signal; never use alone — pair with attitudinal.
- **Conversion Rate Analysis** — *When:* comparative/behavioral; measuring whether users complete the goal action. *Produces:* Success Rate, Drop-Off, Desirability. *Audience:* large. *Constraint:* needs a defined funnel and goal event.
- **Eye Tracking** — *When:* specialized; you need to know what users *see vs. miss*. *Produces:* Comprehension, Efficiency, Visual Attention. *Audience:* small (10–30, expensive per session). *Constraint:* requires hardware (Tobii, RealEye) or webcam-based eye tracking; lab or remote-controlled environment.
- **Card Sorting** — *When:* exploratory; designing or auditing IA, taxonomy, or labeling. *Produces:* Comprehension, Expectations. *Audience:* 15–30 typical (Optimal Workshop / Treejack). *Constraint:* needs a stable content inventory; open vs. closed sort changes what you learn.
- **Surveys & Questionnaires** — *When:* exploratory or feedback; capturing what users think and feel at scale. *Produces:* Usefulness, Satisfaction, Loyalty. *Audience:* flexible — 30 for directional, hundreds for benchmarks. *Constraint:* question-writing discipline matters more than sample size; pair with behavioral data.
- **Quantitative Template** — *When:* you need a custom technique for a metric not covered above. *Produces:* varies (custom UX-metric mapping). *Audience:* depends on technique. *Constraint:* must declare the metric mapping up front, otherwise it falls into the "boxes without comprehension target" trap.

**Five-category grouping (use to plan a balanced stack):** Navigation (Card Sorting, Tree Testing) · Task (Task Success, Time on Task, SEQ) · Comparison (A/B, Preference, Multivariate) · Behavior (Heatmaps, Clickstream, Web Analytics) · Feedback (Surveys, Questionnaires, Eye Tracking).

**Five-step usage discipline:** pick the metric → choose the technique → run lean (small samples often surface clear signals) → pair techniques (Task Success + Time on Task; Survey + Heatmap) → frame results as signals tied to a UX metric, never as raw output.

**Traps:** running techniques without metrics; overcomplicating sample sizes; one-and-done research; reporting raw counts instead of signals.

## v1.1 deltas

Source: *Glare | Define, Collecting v1.1* (Oct 26, 2025) compared to v1.0. The five-step process (Intent → Stack → Approach → Techniques → Connect), the three modes, the four feedback types, the Design Stacks list, the worksheet, and the university/Helio proof-in-practice are all unchanged. Meaningful additions in v1.1:

- **New "Within the Define Layers" table** — explicitly positions Collecting alongside User Needs, Audience, and UX Metrics, showing how each Define block feeds Collecting. Reinforces handoffs to the sibling skills.
- **Named instruments now appear inside the Modes of Learning table** — Exploratory mode now lists CASTLE and NASA-TLX as example techniques; Evaluative lists SUS, SEQ, CES, WAMMI; Comparative lists NPS and SUPR-Q. v1.0 kept these in the Research Stacks doc only; v1.1 surfaces them at the mode-selection step.
- **Step 3 now cites *Measure: What Makes a Question Testable*** — adds three explicit principles for a testable question: defines a knowledge gap, points to observable behavior/perception, can be measured (result must change what you do next). Step 3 is now an upstream gate rather than a label-the-approach step.
- **Step 5 expanded into a three-tier sharing model** — Project-Level Feedback / Cross-Team Insights / Leadership Rollups, with explicit "Show Your Sources" guidance (always cite techniques + audience + metrics). v1.0 mentioned the three levels; v1.1 makes them a table with credibility rationale.
- **New "Next Steps" transition table** — Questioning → Collecting → Findings → Mapping, replacing the looser v1.0 transition prose. This positions Collecting between Questioning (upstream) and Findings (downstream), which is a slightly different framing than v1.0's Collecting → Measuring → Compare flow.
- **No new instruments, modes, or techniques introduced** — the Research Stacks and Techniques catalogs are unchanged in scope; v1.1 is mostly structural and pedagogical refinement.
