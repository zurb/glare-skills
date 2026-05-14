# Focus — Methods — Compressed (v1.3)

## Canonical 28 Metrics

When a method calls out a UX metric — either as the target of the comparison or as the output of the frame — recommend **only** from these 28. Anything else is "outside the canonical 28" and must be flagged with a reason. Method names (Kano, RICE, HEART, SUS, etc.) are scoring or framing models, not metrics; name the canonical metric the method's number maps to.

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

## What a Method is

Methods help teams frame the data inside an initiative. Once an initiative is clear, design needs a way to bring signals into the work. This is not only about testing a prototype or running another study — those are useful techniques, but methods are broader.

A method gives the team a **frame** for looking at the work:
- An onboarding initiative may need a journey frame to see where users lose momentum.
- A pricing initiative may need a comparison frame to see which message creates more trust.
- A navigation initiative may need an information structure frame to see how people expect content to be grouped.
- A product adoption initiative may need a workflow frame to see how signals affect product, marketing, sales, and support.

Each initiative creates different framing needs.

Designers often reach for iterative testing and prototyping because they are close to the craft. But Focus methods also include comparing competitors, benchmarking progress, mapping journeys, segmenting audiences, reviewing workflows, evaluating tradeoffs, and connecting findings back to business decisions.

The method should match the initiative. The goal is not to use every method — it is to choose the frame that helps the team understand the data, compare the right options, and decide what should move forward.

## When to use

- When the user is choosing how to *frame* the data inside an initiative.
- When asking "what method should we use" or "how should we test this."
- When choosing among the 13 method frames (Competitors, Iterations, Timeline, Journeys, Platforms/Devices, User Goals/Tasks, Geographies, User Lifecycle, Behavioral Triggers, Segments, Feature Usage, Risk and Proof, Frameworks).
- When the user lists named methods (Journey mapping, JTBD, A/B, Kano, RICE, ICE, HEART, MoSCoW, Eisenhower, Service blueprint, Empathy mapping) and needs to know which frame they belong to.
- When the team has data but doesn't know what frame would make sense of it.

**Don't use when** the initiative isn't framed (use `glare-focus-initiatives`), data is ready to compare (use `glare-focus-comparing`), or team is ready to commit (use `glare-focus-decisions`).

## Why methods matter

Most teams have more data than clarity. They may have user comments, analytics, survey results, stakeholder feedback, support tickets, research findings, and prototype reactions. Without a method, that evidence stays scattered — people see different things in the same data.

Methods help teams look at the work through a shared frame. They help design and product:
- bring the right data into the initiative
- organize signals around the decision
- compare ideas, moments, audiences, or competitors
- understand which tradeoffs matter
- connect design evidence to business workflows
- decide what deserves more investment

A strong method does not just collect data — it helps the team **use** data.

## What goes into a method

A method starts with the **objective**. Before choosing a frame, the team needs to know what they are trying to understand. The same data can lead to different conclusions depending on the method used to organize it.

- A journey frame might show where momentum breaks across steps.
- A competitor frame might show where the experience feels weaker in the market.
- A concept frame might show which ideas create the strongest signal.
- A benchmark frame might show whether the work is improving over time.

The objective shapes the method. It affects what data gets pulled in, which signals matter most, what gets compared, which audience or context matters, what tradeoff needs to be understood, what decision the method should support.

A strong method usually starts with:
- the initiative being shaped
- the objective for the work
- the signals already collected
- the UX metrics that matter
- the concepts, moments, or competitors being compared
- the decision the team needs to make next

Without a clear objective, methods become a loose activity. With one, the team can frame the data, compare ideas fairly, and explain why one direction deserves more energy.

## The 13 method frames

### Competitors
Use when the initiative needs market context. Helps teams understand where competitors feel stronger, where your experience creates more value, and what expectations users may already bring from other products.
**Example methods:** Competitive analysis · Competitor UX benchmark · Reverse impact mapping · Feature comparison matrix · Positioning comparison · Competitor journey review · Competitive desirability scoring.
*Use when the team needs to see how the work performs beyond its own product.*

### Iterations
Use when the team needs to improve an idea through repeated cycles. Helps teams compare versions, track lift, and see which changes create stronger signals over time.
**Example methods:** A/B testing · Design test loop · Rapid concept testing · MVP prototype · Assumption mapping · Variant comparison · Before-and-after testing · Iterative usability review · Concept refinement loop.
*Use when the team has a direction but needs to sharpen it before investing more.*

### Timeline
Use when the team needs to decide sequence, urgency, or timing. Helps teams understand what should happen now, what can wait, and what needs to be solved before other work can move.
**Example methods:** Eisenhower Matrix · MoSCoW Method · Opportunity Solution Tree · Now/Next/Later · Roadmap sequencing · Impact vs. effort mapping · Release readiness review · Decision deadline mapping.
*Use when the team needs to manage priority without losing the larger direction.*

### Journeys
Use when the initiative spans multiple steps or touchpoints. Helps teams see where users lose momentum, where friction builds, and which moments deserve more attention.
**Example methods:** Journey mapping · Shopping cart flow · Onboarding flow · Service blueprint · Funnel review · Drop-off mapping · Moment mapping · Touchpoint analysis · End-to-end experience review.
*Use when the problem is bigger than one screen, page, or feature.*

### Platforms / Devices
Use when the experience changes across devices, channels, or contexts. Helps teams understand whether the design holds up across the places users actually interact with it.
**Example methods:** Device comparison · Mobile vs. desktop review · Cross-platform experience mapping · Responsive behavior review · Channel comparison · Accessibility device review · Context-of-use review · Platform constraint mapping.
*Use when the same experience needs to work across different environments.*

### User Goals / Tasks
Use when the initiative depends on what users are trying to accomplish. Helps teams compare how well the experience supports real tasks, goals, and moments of progress.
**Example methods:** Task analysis · Importance and satisfaction framework · Interaction matrix · Gravity score · Jobs-to-be-Done mapping · Goal friction mapping · Task success review · Outcome prioritization · User intent mapping.
*Use when the team needs to understand whether the work helps users get something done.*

### Geographies / Regions
Use when the experience needs to work across locations, markets, or cultures. Helps teams understand where expectations, language, behavior, or constraints change by region.
**Example methods:** Regional experience comparison · Localization review · Market readiness review · Cultural context mapping · Regional benchmark · Language clarity review · Compliance and regional constraint review · Geo-segmented signal comparison.
*Use when the same product or message may not land the same way everywhere.*

### User Lifecycle
Use when the initiative affects different stages of the customer relationship. Helps teams understand how needs change from awareness to onboarding, adoption, retention, and expansion.
**Example methods:** User metrics · Simple, Lovable, and Complete framework · MVO (Minimum Viable Offer) · MMP (Minimum Marketable Product) · MLP (Minimum Lovable Product) · Lifecycle stage mapping · Adoption path review · Retention moment analysis · Activation signal review.
*Use when the work needs to support users at a specific stage, not just improve a single interaction.*

### Behavioral Triggers
Use when the team needs to understand what causes users to act. Helps teams see what prompts action, what creates hesitation, and what conditions need to be in place for behavior to change.
**Example methods:** Behavioral Triggers (EAST Framework) · UX impact mapping · Trigger mapping · Motivation/ability review · Friction and prompt analysis · Habit loop mapping · Moment-of-action review · Nudge analysis.
*Use when the initiative depends on getting users to start, continue, or complete an action.*

### Segments
Use when different audiences may respond differently to the same experience. Helps teams compare user groups, roles, cohorts, or need states so the signal is not averaged into something too vague to use.
**Example methods:** Empathy mapping · Jobs-to-be-Done · Competence matrix · Segment comparison · Role-based journey review · Audience priority matrix · Needs-based segmentation · Cohort signal review.
*Use when one experience needs to serve different types of users.*

### Feature Usage
Use when the initiative depends on which features users value, adopt, or ignore. Helps teams compare feature ideas, prioritize product changes, and understand which parts of the product create real use.
**Example methods:** Opportunity scoring · Kano Model · Feature prioritization via weighted scoring · Feature adoption review · Usage pattern analysis · Feature value mapping · Frequency vs. importance matrix · Retention by feature review.
*Use when the team needs to decide what to build, improve, reduce, or remove.*

### Risk and Proof
Use when the team needs to reduce uncertainty before making a larger investment. Helps teams understand what could break, what needs proof, and what level of evidence is enough to move forward.
**Example methods:** Four Big Risks · HATS survey · Proof of Concept · Video testing · Risk mapping · Smoke test · Pilot review · Expert review · Stakeholder signal review.
*Use when the cost of being wrong is high.*

### Frameworks
Use when the team needs a structured model to organize thinking, compare options, or explain tradeoffs. Frameworks help teams make the work easier to discuss, especially when many people are involved in the decision.
**Example methods:** 5Ds · 5W1H Framework · Assumption mapping · Content testing · Copywriting frameworks · Full Loop Analytics Framework · Gap analysis · GIST Framework · Google HEART Framework · ICE Scoring Model · KPI Trees · LNO · Measure & Analyze Data · Product Market Fit · RICE Framework · Spotlight Framework · SUS Testing · Value vs. Complexity Quadrant · Weighted scoring prioritization · XYZ Hypothesis · Zenko Mapping.

## How to choose a method — 5 steps

Start with the decision the team needs to make. Do not ask "What test should we run?" — ask "What frame would help us understand this work clearly?"

### 1. Name the initiative objective
Clarify what the initiative is trying to improve (increase adoption, reduce friction, improve trust, sharpen positioning, simplify a journey, decide which concept deserves more investment). Keeps the method tied to the larger business and user outcome.

### 2. Identify the decision
Name what the team needs to decide next. This might be: which concept deserves more investment · which part of the journey needs attention · which version creates a stronger signal · which audience should be prioritized · which competitor gap matters most · which direction helps the business move forward. The clearer the decision, the easier it is to choose the frame.

### 3. Look at the data you already have
Review the signals, findings, UX metrics, user comments, analytics, and stakeholder input already available. The team may already have enough evidence to frame the decision.
Ask: What signals do we already have? Which UX metrics are relevant? What user comments add context? What business data matters? What is still unclear? Keeps the team from collecting more data before using what it already knows.

### 4. Choose the frame that fits the decision
Pick the method frame that best organizes the data around the decision.
- Issue spans steps → journey frame
- Market context matters → competitor frame
- Timing matters → timeline frame
- Different users respond differently → segment frame
- Choosing between ideas → iteration or comparison frame

The method should make the data easier to interpret.

### 5. Define what gets compared
Make the comparison explicit. The team might compare: concepts, versions, audiences, journey moments, competitors, lifecycle stages, platforms/devices, features, risks, time periods. Keeps the method from becoming vague.

## What comes out of a method

The output is a clearer frame for action. A strong method gives the team:
- a way to organize the data
- a clear comparison
- a stronger interpretation of the signal
- a tradeoff the team can explain
- a finding that supports a decision
- a next move for the initiative

The value is not just the data — it is the frame that helps the team see what the data means and what to do next.

## Where methods work best

Methods work best when the initiative is clear enough to compare something. Use methods when the team has signals, findings, concepts, or business input but needs a better frame for making sense of it. Especially useful when the team has many possible concepts, competing stakeholder views, or a decision that needs clearer evidence.

Methods work less well when the team has not clarified the initiative. If the user need, business goal, audience, or objective is still unclear, go back to Define or Initiatives first. A method can organize evidence, but it cannot fix a poorly framed problem.

## Where methods fit in Glare

Methods sit inside the Focus facet. Initiatives define the area of work that needs attention. Methods give the team a frame for bringing data into that work. Comparing places the signals side by side. Decisions turn the evidence into action.

In the Focus flow:
- **Initiatives** define what needs attention.
- **Methods** frame the data.
- **Comparing** shows what is stronger.
- **Decisions** move the work forward.

Methods are how Focus makes data usable.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Defaulting to A/B testing.** Designers reach for iterative testing because it's familiar — but if the initiative is about understanding the journey or matching user lifecycle, A/B can't see the right thing. Match the frame to the initiative, not to comfort.
- **Mixing frames inside one method run.** Trying to compare competitors AND segments AND iterations in one study produces data that points everywhere. Pick one frame per cycle; layer frames across cycles.
- **Method without a clear handoff to Comparing.** Choosing a method that produces beautiful artifacts (journey maps, personas) but doesn't feed into a comparable signal. The method's job is to *set up the comparison* — if the output can't be compared, the frame was wrong.
- **Treating frameworks (RICE, MoSCoW, Eisenhower) as decision engines.** They're prioritization frames, not decisions. A RICE score informs Focus but the team still has to make the call.

