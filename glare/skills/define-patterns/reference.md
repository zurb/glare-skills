# Patterns — Compressed (v1.0, 2026-05-11)

## What this block is about

Patterns is the fifth building block of Define, joining User Needs, Audience, Collecting Data, and UX Metrics. Its job is to help teams **recognize recurring situations before weak decisions gain momentum**. Most teams already have analytics, feedback, UX metrics, research, dashboards, and AI-generated outputs — yet they still struggle to understand what is actually happening inside the experience. Metrics alone can't explain why users hesitate, what created the friction, or why the same breakdown keeps repeating. Patterns reconnect numbers to the situation surrounding the behavior, so teams stop reacting to isolated data points and start understanding the conditions creating the behavior in the first place.

## Core definition

**A pattern is a recurring situation where similar conditions repeatedly produce similar behaviors and signals.**

Patterns are NOT:
- single metrics
- dashboards
- trends
- personas
- isolated observations

Patterns emerge when teams repeatedly see the same friction, hesitation, workflow breakdowns, or signal relationships appearing across experiences.

## When to use

- When the user is recognizing recurring situations before weak decisions gain momentum.
- When the same problem keeps showing up — engagement up but trust down, completion high but support tickets rise, AI produces more but the team trusts it less.
- When the team needs to slow down enough to interpret a signal before momentum scales a weak decision.
- When sorting observations into the four pattern types (User, Workflow, Signal, AI Workflow).
- When the same metric (e.g., long session duration) could mean strong engagement OR confusion — the situation creates the meaning.

**Don't use when** naming user needs (use `glare:define-user-needs`), picking audience (`glare:define-audience`), gathering evidence (`glare:define-collecting`), or picking metrics (`glare:define-ux-metrics`).

## Why this matters now (situations create meaning)

People do not act in isolation. Behavior emerges from situations shaped by pressure, uncertainty, goals, workflows, habits, incentives, and emotional conditions. Because of that, the same behavior can mean completely different things depending on the situation.

Example — long session duration might signal:
- strong engagement
- confusion
- hesitation
- comparison behavior
- cognitive overload

Without the surrounding situation, teams misread the signal and optimize for the wrong outcome. Patterns help teams interpret behavior within the conditions that created it. That gives metrics meaning instead of just visibility.

## What patterns help teams see

Patterns reveal what isolated metrics hide. A single metric exposes a symptom; a pattern shows the larger situation surrounding it. Over time, teams begin recognizing recurring conditions earlier:

- confidence dropping during high-complexity onboarding
- stakeholders bypassing evidence when deadlines tighten
- AI accelerating production faster than teams can properly evaluate the work
- usability improving while comprehension quietly weakens underneath it

Patterns make these conditions visible before they scale into larger operational, product, or organizational failures.

## The four pattern types

### 1. User Patterns

Recurring situations people experience while trying to make progress. Teams repeatedly see:
- hesitation during onboarding
- abandoning high-effort flows
- comparison paralysis
- repeated misunderstanding
- low-confidence purchasing

These patterns help teams understand motivation, friction, emotional conditions, and unmet needs surrounding the experience.

### 2. Workflow Patterns

Patterns inside the organization itself. Teams often encounter:
- endless review cycles
- late validation
- siloed optimization
- repeated decision reopening
- weak cross-functional alignment

These patterns reveal where the workflow, communication structure, or decision system is creating friction long before users ever experience the product.

### 3. Signal Patterns

Patterns through relationships between UX metrics. For example:
- engagement rises while trust declines
- usability improves while retention weakens
- completion increases while effort grows
- AI adoption rises while confidence falls

These situations expose hidden tradeoffs that isolated metrics often fail to reveal.

### 4. AI Workflow Patterns

Operational patterns emerging as AI integrates into product workflows:
- faster production with weaker evaluation
- shallow iteration loops
- overproduction without prioritization
- AI-generated consistency masking weak thinking

As output accelerates, recognizing these early matters more — otherwise teams scale weak decisions faster than they can evaluate them.

## Patterns and UX Metrics

UX metrics help reveal patterns, but metrics alone rarely create understanding. A number can show that something changed, but it usually cannot explain why the behavior happened, what conditions shaped it, or what constraints influenced the outcome. Patterns reconnect the measurement back to the situation surrounding the behavior.

The four UX metric lenses each expose a different part of the experience and reveal a different kind of pattern:
- **By Type** — perception vs behavior gaps (e.g., users say they trust the product but bounce at checkout)
- **By Stage** — when friction appears (predictive / proxy / analytics)
- **By Time** — leading vs lagging conditions (a pattern that's already visible upstream)
- **By Engagement** — alignment and loyalty gaps (high activity, low loyalty)

Patterns help teams organize those signals into usable understanding instead of treating metrics like isolated observations on a dashboard.

## Why patterns matter more now

AI is increasing the amount of output teams can generate. Concepts, experiments, workflows, variations, and prototypes are created faster than ever. But faster output does not automatically create better understanding. AI is not automatically increasing:
- judgment
- alignment
- prioritization
- confidence
- shared understanding

Teams now face a different kind of pressure — more ideas, more experiments, and more signals moving through the organization than they can properly evaluate. That creates:
- weak validation
- fragmented workflows
- disconnected signals
- decision fatigue

Patterns help teams slow down just enough to understand the situation before momentum carries weak decisions forward. The goal is **not perfect certainty, but stronger directional confidence while the work is still evolving.**

## Worked example: the "completion is fine" trap

A team is shipping onboarding optimizations. The dashboard shows:
- onboarding completion stays high
- trust scores continue dropping
- support requests increase after setup
- users repeatedly revisit help content

The real problem is not "completion." The pattern is that users can technically finish onboarding, but they leave uncertain and unsupported. The decision shifts — the team stops optimizing for task completion alone and starts addressing the confidence breakdown happening inside the situation itself.

## Key terms

- **Pattern** — a recurring situation where similar conditions repeatedly produce similar behaviors and signals.
- **Situation** — the surrounding forces (pressure, uncertainty, goals, workflows, habits, incentives, emotion) that shape how people think, react, and move through an experience.
- **Symptom vs Situation** — a metric exposes a symptom; a pattern exposes the situation creating the symptom.
- **User Pattern / Workflow Pattern / Signal Pattern / AI Workflow Pattern** — the four pattern types covering user behavior, organizational behavior, metric relationships, and AI-accelerated production.
- **Directional confidence** — the goal of pattern recognition; not certainty, but enough clarity to act while work is still evolving.
- **Situations create meaning** — the foundational rule: the same behavior means different things in different situations.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Naming a one-off as a pattern.** A single observation isn't a pattern. Patterns require *recurrence* — similar conditions repeatedly producing similar behaviors. Naming an isolated event as a pattern leads the team to over-correct on noise.
- **Reading the metric without the situation.** "Long session duration" gets reported as engagement and the team doubles down — when the actual pattern is users stuck and re-scanning. The pattern reconnects the metric to the situation; skipping that reverses the diagnosis.
- **Letting AI overproduce before pattern recognition.** AI generates output faster than the team can evaluate it; without pattern checks, the team builds on top of weak ideas because they shipped quickly. Patterns are the slow-down that protects strong ideas.
- **Confusing pattern naming with library building.** A pattern library is useful only when patterns are detected in live work. Cataloging patterns no team actually checks during decisions produces vocabulary without behavior change.

## Cross-references inside Glare

- Patterns feeds Measure — once a pattern is named, the team forms a Hunch around it ("we believe this recurring situation is caused by X") and routes through `glare:measure-hunches` and `glare:measure-questioning`.
- Signal Patterns overlap with `glare:signals-quality` and `glare:signals-types` — when a metric improves while another weakens, that's a signal-quality / signal-type coverage gap.
- Workflow Patterns overlap with `glare:design-assessment` (Organizing Work, Managing Complexity, Guiding Decisions) — recurring decision-quality breakdowns at the org level often surface here first.
- AI Workflow Patterns overlap with `glare-ai-workflows` — the pattern is the operational symptom; the AI Workflows skill is the corrective frame.
