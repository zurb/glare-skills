# What Is a UX Metric? — Reference (v1.32)

## The working definition

A UX metric is a way to measure how people experience a product, workflow, or system. Product teams make decisions every day — changing onboarding, updating navigation, redesigning dashboards, adding AI recommendations, launching new workflows. Many teams still struggle to clearly understand what users are actually experiencing underneath those decisions. A workflow may technically succeed while users quietly feel confused. Engagement may increase while trust weakens. Users may finish onboarding while still feeling unsure about what to do next.

Without measurement, teams rely on opinions, assumptions, stakeholder reactions, gut feelings, or surface-level analytics. A UX metric replaces "this feels confusing" / "users probably like it" / "the workflow seems better" with measurable trust, usability, confidence, comprehension, effort, and satisfaction. The metric becomes valuable because it explains what is happening underneath the experience, not just what happened on the surface.

## UX metrics turn fuzzy ideas into clearer signals

Most product teams already collect lots of information — analytics, support tickets, interviews, usability tests, AI feedback, surveys, feature usage. But raw numbers alone rarely explain the full experience. A completion score may look healthy while users quietly struggle underneath the workflow. Engagement may rise while trust slowly weakens over time. Users may finish onboarding while still feeling confused about what happens next.

A UX metric gives structure to what users are actually experiencing. Over time, the metric becomes more than a number — it becomes a signal teams can use to compare workflows, validate ideas, identify friction, improve onboarding, and guide product direction.

---

## When to use

- When the user asks what a UX metric actually IS or how one is structured.
- When walking through the four parts — User Attribute, Data Type, Collection Method, Benchmark.
- When distinguishing a UX metric from a raw analytics number or a business KPI.
- When the user is writing their first UX metric or debugging one that feels incomplete.
- When asking "70% completion — is that good?" (the missing piece is benchmark).
- When turning a fuzzy reaction like "this feels confusing" into something measured.

**Don't use when** the user wants the four metric TYPES at the framework level (`glare:ux-metrics`), Define-stage metric picking (`glare:define-ux-metrics`), or stacking metrics together (`glare:ux-metrics-stack`).

## The four parts of a UX metric

In Glare a UX metric is built from four connected parts. These layers turn raw information into something measurable and actionable.

### 1. User Attribute

The part of the experience being measured. What are you measuring? This aligns back to your audience and their needs. The attribute helps teams decide what they want to learn about the experience.

Examples by workflow type:

- Onboarding redesign — confidence, comprehension, trust
- Checkout workflow — effort, completion, clarity
- AI recommendation surface — confidence calibration, recommendation quality, trust
- Dashboard redesign — comprehension, discoverability, time on task

Different workflows need different types of measurement.

### 2. Data Type

The type of signal being collected. UX Metrics usually fall into three main groups (the v1.32 Four Parts doc uses three at this level; the broader UX Metrics framework adds Intelligence as a fourth type for AI-assisted experience quality):

| Data Type | What it captures | Examples |
|---|---|---|
| **Attitudinal** | How users feel | confidence, trust, satisfaction, desirability |
| **Behavioral** | What users do | clicks, navigation behavior, engagement, hesitation, completion patterns |
| **Performance** | How well the workflow functions | completion rate, time on task, error rate, abandonment, workflow efficiency |

Each type reveals a different part of the experience. When used together, they help teams understand the larger pattern forming across the workflow.

### 3. Collection Method

Where the information comes from. Examples — usability testing, surveys, analytics, interviews, session recordings, AI-assisted evaluations.

Different collection methods reveal different kinds of problems. Analytics may reveal abandonment, slower onboarding, repeated navigation loops. Interviews may reveal hesitation, confusion, low confidence, trust concerns. The collection method shapes the type of understanding teams gain from the metric.

### 4. Benchmark

A number by itself usually does not mean very much. Teams need comparison points to understand whether something is improving or getting worse. Benchmarks may include:

- previous versions
- industry averages
- competitor comparisons
- internal targets
- earlier test results

This gives the metric context. A 70% completion score may sound strong — but not if the earlier workflow scored 88%, or if competitors consistently score higher. Benchmarks help teams understand whether the experience is actually improving over time.

---

## The trust-during-onboarding example

A team may want to understand whether users feel confident during onboarding. The team could measure:

- **Attribute** — Trust
- **Data Type** — Attitudinal
- **Collection Method** — Post-test survey
- **Benchmark** — Compare against previous onboarding flow, competitor onboarding, target confidence score

At first, the onboarding flow may appear successful because completion remains high. But the UX metric may reveal lower confidence, weaker trust, rising hesitation, confusion during setup. Without the metric, the team may assume the onboarding experience is healthy simply because users finished the workflow. The metric helps explain how the experience actually felt while users moved through it.

---

## UX metrics become more valuable together

A single metric only explains one small part of the experience. But when metrics begin working together, larger patterns start appearing:

- high completion + low confidence may reveal a trust problem
- strong engagement + rising effort may reveal friction
- low errors + weak comprehension may reveal hidden confusion

The metrics begin explaining each other. Over time, teams begin seeing patterns that isolated dashboards often miss — confusion traps, friction walls, trust gaps, repeated hesitation.

In Glare, these connected groups of metrics are called **UX Metric Stacks**. An onboarding stack may combine completion, confidence, comprehension, time on task, and satisfaction. Together, these metrics help teams understand whether users are moving smoothly through onboarding or quietly struggling underneath the workflow. See `glare:ux-metrics-stack`.

---

## Why this matters operationally

UX metrics help teams compare workflows, evaluate onboarding, validate ideas earlier, identify friction before launch, improve stakeholder alignment, and benchmark progress over time. They also help product, design, research, and leadership teams work from the same signals instead of disconnected opinions or scattered dashboards.

Over time, UX metrics become part of how organizations build confidence in product direction, reduce uncertainty, and improve experiences through repeated learning and clearer evidence.

---

## Common failure modes (write the metric correctly the first time)

| Failure | What it looks like | Fix |
|---|---|---|
| **No Benchmark** | Reporting "we got 73%" with no comparison point | Always state previous-version, competitor, internal-target, or earlier-test number alongside the score |
| **Wrong Data Type** | Using engagement to answer a trust question | Match Data Type to the question — Attitudinal for "how feel," Behavioral for "what do," Performance for "how efficiently" |
| **Drifted Attribute** | The metric is no longer connected to the user need or audience | Re-anchor to `glare:define-user-needs` and the audience attributes from `glare:define-audience` |
| **Wrong-stage Collection Method** | Live analytics for a pre-launch concept | Use Helio / prototype tests / surveys as Predictive or Proxy collection methods before launch |
| **Single metric reported alone** | One number making a launch / no-launch call | Move to a stack — see `glare:ux-metrics-stack` |

## Source

Drafted from *Glare | UX Metrics, What is a UX Metric? v1.32* (Drive doc `1-teouWMYjBy2sltDWjVvP5BXfolBfZe5dzp_zf9qGHk`, May 10, 2026). The four-part structure and the trust-during-onboarding example come directly from that source.

## Failure modes

These are common ways this skill goes wrong in practice:

- **Metric without a benchmark.** "70% completion" without a comparison means nothing — it could be excellent or terrible. Always include the benchmark in the metric.
- **Confusing analytics numbers with UX metrics.** "Page views" or "session length" off an analytics tool aren't UX metrics until they have a User Attribute, Data Type, Collection Method, and Benchmark.
- **Skipping User Attribute.** Reporting a number ("85% finished") without naming what user experience attribute it ties to (Comprehension? Trust? Effort?). The attribute is what makes the metric interpretable.
- **Made-up data types.** Using categories that don't fit the three (Attitudinal, Behavioral, Performance) or the v1.32 fourth (Intelligence). Stick to the canonical types so metrics combine cleanly into stacks.

