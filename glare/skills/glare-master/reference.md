# Glare Master — Cross-Component Orchestration Reference (v3.0)

The master skill points users to the right component when they're lost, AND explains how the 6 components work together. This reference is the lookup the master uses to route fast and the map it uses to orchestrate.

---

## The 6 components, at a glance

| Component | What it covers | Parent skill | Sub-skills |
|---|---|---|---|
| **Getting Started** | Onboarding, framework tour, AI workflows, glossary, first signal, coaching, proving impact — all consolidated | `glare-getting-started` | (single consolidated skill) |
| **Decision Map** | The spine — Define → Measure → Focus → Lead, looping back. 22 skills: parent + Define (5, including new Patterns) + Measure (4) + Focus (4) + Lead (4) | `glare-decision-map` | 21 |
| **Design Review** | SIGNAL flow (Surface, Identify, Ground, Navigate, Align, Lock) plus scoring, rubric, coach, run-transcript. 12 skills | `glare-design-review` | 11 |
| **UX Metrics** | The 4-type taxonomy (Attitudinal · Behavioral · Performance · Intelligence) plus what-is, why, system, three metric libraries, stack, mapping, applying. 10 skills | `glare-ux-metrics` | 9 |
| **Design Signals** | What a signal is, anatomy (6 pieces), four types (Need / Use / Prefer / Adopt), quality, capturing. 5 skills | `glare-design-signals` | 4 |
| **Design Assessment** | 5-dimension org maturity diagnostic (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence) plus scoring, reading, using-results. 9 skills | `glare-design-assessment` | 8 |

Total: **60 skills** (master + 59 across the 6 components).

---

## How the components connect

The components are interconnected, not parallel. Work flows between them.

### Getting Started is the on-ramp

`glare-getting-started` is where new users land. It carries onboarding, framework tour, AI workflows, the glossary, the first-signal walkthrough, coaching/advising, and proving-design-impact narrative — all in one consolidated skill in v3. It hands off to the right component when the user is ready to do real work.

### Decision Map is the spine

`glare-decision-map` is the operational system that connects user needs, signals, decisions, and outcomes. Four facets in flow:

- **Define** (`glare-define`) — agree on what matters before building. Five building blocks: User Needs, Audience, **Patterns** (new in v1.34), Collecting Data, UX Metrics.
- **Measure** (`glare-measure`) — turn intuition into evidence. Four moves: Concepts → Hunches → Questioning → Findings. **This is where Design Signals get produced.**
- **Focus** (`glare-focus`) — turn signals into direction. Four moves: Initiatives → Methods → Comparing → Decisions.
- **Lead** (`glare-lead`) — translate decisions into business evidence. Four buckets: Business Goals → Mapping (Chain of Proof) → Results → Workflows.

The loop: Lead's outcomes feed back into the next Define cycle. **A loop, not a line.**

### Design Signals are produced inside Measure and consumed in Design Review

`glare-design-signals` is the evidence currency of the whole framework. A signal has six components — design intuition, UX metric, user need, context, business goal, direction. Signals come in four types: Need, Use, Prefer, Adopt. They are **created inside Decision Map's Measure facet** and **evaluated inside Design Review's Ground step** (where reviews are anchored in evidence). The signal is what travels between components.

### UX Metrics underpin everything

`glare-ux-metrics` isn't a parallel component — it's the unit of measure that shows up inside the other five.

- Inside **Decision Map's Define**, picking the right metric is the UX Metrics block.
- Inside **Design Signals**, the metric is one of the six pieces of every signal.
- Inside **Design Review's Ground step**, metrics are how the review is anchored in evidence.
- Inside **Design Assessment's Building Proof dimension**, metrics are how the team proves what changed.
- Inside **Decision Map's Lead**, metrics ladder into the Chain of Proof (Design KPI → Product KPI → Business KPI).

When the user is "picking a metric," they need `glare-ux-metrics`. When the user is "using a metric inside a signal/review/decision," they're inside one of the other components and UX Metrics is the supporting library.

### Design Review improves the conversations where decisions get made

`glare-design-review` is the SIGNAL flow that scores how well a design review converts insight to motion. Six steps in order: Surface → Identify → Ground → Navigate → Align → Lock. Reviews don't replace the Decision Map — they're **where Focus decisions actually get made out loud.** A Decision Map decision that doesn't survive a review wasn't really made.

### Design Assessment looks across all of this to diagnose org maturity

`glare-design-assessment` is the system-level diagnostic. Five dimensions — Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence — each scored Reactive → Developing → Functional → Strong → Leading. Assessment doesn't produce signals or run reviews; it tells the team **where the system is strong or breaking** so they know which other component to invest in.

### Master coordinates

`glare-master` (this skill) routes when users are lost, and explains the connections when users want to orchestrate. It is not a component — it is the disambiguator across them.

---

## Phrase → Skill lookup

Match what the user said to the leftmost trigger; route to the right skill. At least 30 rows.

### Getting Started

| Phrase the user uses | Route to |
|---|---|
| "what is Glare" / "explain Glare" / "how do we start" | `glare-getting-started` |
| "I have a decision in front of me — walk me through Glare" / "first signal" | `glare-getting-started` |
| "use Glare with ChatGPT / Claude / agents" / prompts vs Skills | `glare-getting-started` |
| "we want to roll Glare out" / "90-day pilot" / "coach us" | `glare-getting-started` |
| "prove design ROI" / "design impact to leadership" | `glare-getting-started` |
| "what does [Glare term] mean" / vocabulary | `glare-getting-started` |

### Decision Map

| Phrase the user uses | Route to |
|---|---|
| "Decision Map" / "trace a decision from problem to outcome" / "the chain is broken" / "how do the facets connect" | `glare-decision-map` |
| in Define area, broad / "Credibility" / "what should we measure" | `glare-define` |
| "what user need does this solve" / "is this a want or a need" | `glare-define-user-needs` |
| "who are we designing for" / "design for everyone is design for no one" | `glare-define-audience` |
| "we keep seeing the same situation" / "Patterns" / "recognize before momentum scales weak decision" | `glare-define-patterns` |
| "how do we gather evidence" / "survey or A/B test" | `glare-define-collecting` |
| "high satisfaction + low completion" / "vanity vs actionable" | `glare-define-ux-metrics` |
| Measure area broad / "we believe…" | `glare-measure` |
| 5-minute test / Concepts move | `glare-measure-concepts` |
| forming a falsifiable hunch | `glare-measure-hunches` |
| drafting research questions / "Do people like our homepage?" | `glare-measure-questioning` |
| "what does this data mean" / Findings move | `glare-measure-findings` |
| Focus area broad / "v1 vs v2" | `glare-focus` |
| 10 initiative types / "what should we focus on" | `glare-focus-initiatives` |
| "HEART" / "RICE" / "Kano" / "JTBD" | `glare-focus-methods` |
| "how do we compare" / benchmarking | `glare-focus-comparing` |
| "what's the decision" / Decision Record / Implement-Refine-Test-Revisit | `glare-focus-decisions` |
| Lead area broad / "executive narrative" | `glare-lead` |
| "Reduce churn" / "Lower support costs" / Growth-Retention | `glare-lead-business-goals` |
| "Chain of Proof" / ladder metrics | `glare-lead-mapping` |
| "outputs vs outcomes" / "leadership doesn't see what we contribute" | `glare-lead-results` |
| "tell sales this is working" / "design ROI for Finance" | `glare-lead-workflows` |

### Design Review

| Phrase the user uses | Route to |
|---|---|
| "SIGNAL framework" / "how do I run a better design review" | `glare-design-review` |
| "team is reacting before agreeing on the problem" / feedback scattered | `glare-review-surface` |
| feedback is all preference / "what does success look like here" | `glare-review-identify` |
| "conversation keeps looping on opinion" / "designs got pushed back without clear feedback" | `glare-review-ground` |
| "we keep exploring without choosing" / "team won't make a recommendation" | `glare-review-navigate` |
| "everyone agreed but no one owns it" / responsibility blurry | `glare-review-align` |
| "the call ended without next steps" / "we'll follow up" | `glare-review-lock` |
| "what techniques in a review" / shape feedback in real time | `glare-review-techniques` |
| "how do I score a review" / "what does a 3 mean for Surface" | `glare-review-scoring-model` |
| paste a transcript / "score this call" | `glare-review-rubric` |
| "prep me for a kickoff" / "what should I do better next time" | `glare-review-coach` |
| "I have a transcript — what do I do with it" | `glare-review-run-transcript` |

### Design Signals

| Phrase the user uses | Route to |
|---|---|
| "what is a design signal" / "signals vs feedback" | `glare-design-signals` |
| "anatomy of a signal" / 6 pieces | `glare-signals-components` |
| "Need / Use / Prefer / Adopt" / four signal types | `glare-signals-types` |
| "is this signal usable" / "is this a signal or just a metric" | `glare-signals-quality` |
| "how do I capture a signal" / fast capture loop | `glare-signals-capturing` |

### UX Metrics

| Phrase the user uses | Route to |
|---|---|
| "UX metrics" / Attitudinal vs Behavioral vs Performance vs Intelligence | `glare-ux-metrics` |
| "what is a UX metric" / parts of a metric | `glare-ux-metrics-what-is` |
| "why do we need UX metrics" / leading indicators / AI acceleration | `glare-ux-metrics-why` |
| "measurement system" / Confusion Trap / Friction Wall / Trust Gap | `glare-ux-metrics-system` |
| "satisfaction" / "how do users feel" / attitudinal | `glare-ux-metrics-attitudinal` |
| "task success" / "can users do it" / behavioral | `glare-ux-metrics-behavioral` |
| "bounce rate" / "time on task" / performance metrics | `glare-ux-metrics-performance` |
| "metric stack" / "which metrics go together" | `glare-ux-metrics-stack` |
| "map metrics to business impact" | `glare-ux-metrics-mapping` |
| "how do I use these metrics" / metric playbook | `glare-ux-metrics-applying` |

### Design Assessment

| Phrase the user uses | Route to |
|---|---|
| "design maturity" / "where is design impact breaking down" | `glare-design-assessment` |
| "design knowledge gets lost" / "we keep restarting from scratch" | `glare-assessment-organizing-work` |
| "work keeps getting tangled" / "every project feels overweight" | `glare-assessment-managing-complexity` |
| "we can't show what changed" / "design feels like opinion" | `glare-assessment-building-proof` |
| "we keep relitigating decisions" / "loudest voice wins" | `glare-assessment-guiding-decisions` |
| "proof stays local" / "leaders only see final outputs" | `glare-assessment-scaling-influence` |
| score bands / Reactive / Developing / Functional / Strong / Leading | `glare-assessment-scoring` |
| "what does our pattern mean" / "balanced but low" | `glare-assessment-reading` |
| "what do we do with our score" / 30-day next move | `glare-assessment-using-results` |

---

## Cross-component flows that recur

These are the 4 patterns where work moves across more than one component. When a user is asking about one of these, they need orchestration, not just navigation.

### 1. Decision flow — Define → Measure → Focus → Lead → back to Define

The full spine of the Decision Map. A decision starts in Define (user need clarified), moves through Measure (signals created), lands in Focus (direction chosen), proves out in Lead (outcomes connected to business), and the outcome feeds the next Define cycle. **A loop, not a line.** When the user describes work scattered across docs, meetings, tools, and reports — the chain is broken. Route to `glare-decision-map`; let it route into the specific facet they're stuck in.

### 2. Signal anatomy in practice — Signals captured in Measure, evaluated against UX Metrics, used in Decision Map decisions, scored in Reviews

A signal lives across four components at once:

- **Created** inside Decision Map's Measure (specifically `glare-measure-findings`, where data becomes a signal)
- **Built from** UX Metrics (the metric is one of the six anatomy pieces — see `glare-signals-components`)
- **Used to make** a Decision Map decision (in Focus — `glare-focus-decisions`)
- **Evaluated** during a Design Review (in the Ground step — `glare-review-ground`)

When the user is asking "is this signal good enough to act on," they're at the intersection of Design Signals (`glare-signals-quality`) and Decision Map. Route to `glare-signals-quality`.

### 3. Maturity diagnosis — Assessment across all 5 dimensions

`glare-design-assessment` doesn't produce signals or run reviews — it looks across the whole system. The 5 dimensions cover the system's mechanics: Organizing Work (does knowledge compound?), Managing Complexity (does structure match the problem?), Building Proof (does work connect to outcomes?), Guiding Decisions (does evidence shape decisions?), Scaling Influence (does proof travel?). Each dimension maps back to a component the team should invest in:

- Organizing Work weak → invest in Decision Map's Define
- Managing Complexity weak → invest in Decision Map's Focus
- Building Proof weak → invest in UX Metrics + Design Signals
- Guiding Decisions weak → invest in Design Review
- Scaling Influence weak → invest in Decision Map's Lead + Getting Started's proving-impact narrative

When the user has assessment results and is asking what to do, route to `glare-assessment-using-results`.

### 4. First-signal workflow — Getting Started → first signal → Decision Map decision

The on-ramp for a user with a real decision in front of them. `glare-getting-started` carries the first-signal walkthrough; from there the work moves into `glare-decision-map` (typically entering at Measure for hunch/signal work, or at Define if the user need isn't clear yet). When the user says "I have a real decision — walk me through it," route to `glare-getting-started` and let it hand off into the Decision Map.

---

## Stuck patterns → high-leverage entry point

These are the most-frequent "I'm lost" scenarios. Match the symptom, route to the skill, explain in one sentence.

| Symptom | Route to | Why |
|---|---|---|
| "We have data but no decision" | `glare-signals-quality` | The number isn't a signal yet — quality check tells you if it's usable as one |
| "Meeting ended with no decision" | `glare-review-lock` | Lock is the SIGNAL step that converts insight to motion |
| "Designs got pushed back without clear feedback" | `glare-review-ground` | Ground anchors the conversation in evidence so feedback isn't preference |
| "Team can't agree on what we're solving" | `glare-define-user-needs` | User-need block is where shared problem definition lives |
| "We keep seeing the same situation across projects" | `glare-define-patterns` | Patterns (v1.34) is the new Define block for recognizing recurrence before weak decisions scale |
| "We have a roadmap but can't prove anything moved" | `glare-lead-results` | Initiatives → Findings → Decisions → Outcomes loop is the proof structure |
| "We did the research but can't connect it to business" | `glare-lead-mapping` | Chain of Proof ladders user need → Design KPI → Product KPI → Business KPI |
| "Designers, PMs, engineers see different problems" | `glare-define-audience` | Four-voice frame forces alignment on whose voice the signal represents |
| "We keep relitigating the same decision" | `glare-assessment-guiding-decisions` | Guiding Decisions dimension symptom — diagnose before patching |
| "Output is exploding faster than we can decide" | `glare-getting-started` | The core problem Glare exists to solve — start with the framework |
| "We're picking metrics and they're not landing" | `glare-define-ux-metrics` | Attitudinal/Behavioral/Performance distinction usually fixes the mismatch |
| "Which UX metric should we even pick" | `glare-ux-metrics` | The 4-type taxonomy is the starting frame |
| "Our metrics don't work together" | `glare-ux-metrics-stack` | Stack design is how metrics combine into a measurement system |
| "We have v1 and v2 and can't choose" | `glare-focus-comparing` | Comparing is the move; turn it into a structured benchmark |
| "We keep starting over on the same problem" | `glare-assessment-organizing-work` | Knowledge is getting lost between projects |
| "The call was just opinion ping-pong" | `glare-review-ground` | Ground anchors the room in evidence |
| "Leadership doesn't see what we're contributing" | `glare-getting-started` | The proving-design-impact narrative is here in v3 |
| "I have a Helio test and don't know what to do with results" | `glare-measure-findings` | Findings is the move that turns data into a signal |
| "Use Glare with Claude / ChatGPT / agents" | `glare-getting-started` | AI workflows live inside the consolidated Getting Started skill in v3 |
| "We're pushing Glare across the company" | `glare-getting-started` | Coaching/advising and the 90-day pilot model are inside Getting Started |
| "What does [Glare term] mean" | `glare-getting-started` | Glossary lives inside Getting Started in v3 |
| "Our proof stays local — leaders never see it" | `glare-assessment-scaling-influence` | Scaling Influence dimension diagnoses why design evidence doesn't travel |
| "Every project feels overweight" | `glare-assessment-managing-complexity` | Managing Complexity diagnoses the structure-to-problem mismatch |

---

## When ambiguous — the one-question protocol

If diagnosis is genuinely 50/50 between two very different components, ask ONE question, then route. Don't ask twice.

- "Is this about a meeting you just ran, or a decision you're about to make?" — disambiguates `glare-design-review` vs. `glare-decision-map`
- "Do you have data already, or are you trying to figure out what to test?" — disambiguates `glare-measure-findings` vs. `glare-measure-questioning`
- "Are you trying to pick a direction, or trying to prove the direction worked?" — disambiguates Focus vs. Lead
- "Is this about your own decision, or about how the org handles decisions in general?" — disambiguates a Decision Map facet vs. `glare-design-assessment`
- "Are you picking a metric, or using one inside a signal/review/decision?" — disambiguates `glare-ux-metrics` vs. the component using the metric

---

## What the master never does

- Recommends a list of skills. (One.)
- Recommends a skill that isn't in the catalog of 60.
- Tries to do the destination skill's work itself.
- Re-routes a user who is already productive in their current skill.
- Lectures the framework before routing. If they want the framework tour, the right route is `glare-getting-started`.
- Describes a connection in the abstract without naming a destination skill the connection points toward.

---

## Outside this install

For v3, there is **no "outside"** — the marketplace ships all 6 components together, and every skill the master might reference lives inside this install. If a future v3.x adds new components or splits an existing one (e.g., promoting `glare-define-patterns` to its own top-level component, or splitting Getting Started back into its v2-era constituent skills), the master and this reference are the two files to update first — the master's description and the reference's component table and phrase lookup are the only places "the 6 components" and "60 skills" are asserted as facts. Treat this section as the future-proofing note: if those counts ever change, this file is the source of truth that needs to change with them.
