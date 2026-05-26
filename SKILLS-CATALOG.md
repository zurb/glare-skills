# Glare Skills Catalog (v2.2.0)

Quick reference for the **65 skills** in the Glare plugin — the full framework across 6 sections plus a cross-section router.

After installing, you don't invoke skills by name — Claude loads the right one when your conversation matches its description. This catalog helps you scan what's available.

**Install once:**

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

All 60 skills become available.

---

## What you're feeling → which skill

A reverse index. If you can name your symptom, this table points to one skill. (For more exhaustive routing, see `glare-master/reference.md`.)

| Symptom | Use skill |
|---|---|
| "I'm stuck — don't know where to start" | `glare-master` |
| "What is Glare / how do I begin" | `glare-getting-started` |
| "We have data but no decision" | `glare-signals-quality` |
| "I have a Helio test result and don't know what to do with it" | `glare-measure-findings` |
| "Meeting ended with no decision" | `glare-review-lock` |
| "The call was just opinion ping-pong" | `glare-review-ground` |
| "Designs got pushed back without clear feedback" | `glare-review-ground` |
| "Team can't agree on what we're solving" | `glare-define-user-needs` |
| "Designers, PMs, engineers see different problems" | `glare-define-audience` |
| "We keep seeing the same situation across projects" | `glare-define-situations` *(replaces deprecated `glare-define-patterns`)* |
| "We're picking metrics and they're not landing" | `glare-define-ux-metrics` |
| "Which UX metric should we even pick" | `glare-ux-metrics` |
| "Our metrics don't work together" | `glare-ux-metrics-stack` |
| "We have v1 and v2 and can't choose" | `glare-focus-comparing` |
| "We have a roadmap but can't prove anything moved" | `glare-lead-results` |
| "We did the research but can't connect it to business" | `glare-lead-mapping` |
| "Leadership doesn't see what we're contributing" | `glare-getting-started` (proving-impact narrative) |
| "We keep relitigating the same decision" | `glare-assessment-guiding-decisions` |
| "We keep starting over on the same problem" | `glare-assessment-organizing-work` |
| "Every project feels overweight" | `glare-assessment-managing-complexity` |
| "Our proof stays local — leaders never see it" | `glare-assessment-scaling-influence` |
| "Output is exploding faster than we can decide" | `glare-getting-started` |
| "Use Glare with Claude / ChatGPT / agents" | `glare-getting-started` (AI workflows) |
| "We're pushing Glare across the company" | `glare-getting-started` (coaching/advising) |
| "What does [Glare term] mean" | `glare-getting-started` (glossary) |

---

## Navigation (1)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-router` | mid-flow and lost — need a pointer to one specific skill | "where should I go next" · "which Glare skill applies" · "I'm stuck and don't know where to start" |

---

## Get Started (7)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-get-started` | first-time onboarding, canonical tour of the framework | "what is Glare" · "where do I start" |
| `glare-create-first-signal` | creating your very first design signal | "my first signal" · "how do I create a signal" |
| `glare-how-glare-works` | understanding how the framework pieces fit together | "how does Glare work" · "explain the framework" |
| `glare-ai-workflows` | using AI within the Glare workflow | "AI + design research" · "how does Claude fit in" |
| `glare-coaching-advising` | coaching or advising mode for design teams | "coach me" · "advise on our process" |
| `glare-proving-design-impact` | proving design's business value to leadership | "prove design matters" · "design ROI" |
| `glare-glossary` | looking up Glare terminology | "what does [term] mean in Glare" |

---

## Design Review (12)

The SIGNAL framework for scoring design review conversations.

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-review` | running or scoring a design review (parent) | "design review" · "SIGNAL framework" |
| `glare-review-surface` | Surface step — what's visible | "what do users see first" |
| `glare-review-identify` | Identify step — name the patterns | "what patterns are emerging" |
| `glare-review-ground` | Ground step — anchor in evidence | "what data supports this" |
| `glare-review-navigate` | Navigate step — explore alternatives | "what else could we do" |
| `glare-review-align` | Align step — converge on direction | "are we aligned" |
| `glare-review-lock` | Lock step — commit to a decision | "let's lock this in" |
| `glare-review-techniques` | review techniques catalog | "which technique should I use" |
| `glare-review-scoring-model` | scoring model for reviews | "how do I score this review" |
| `glare-review-rubric` | evaluation rubric | "review rubric" |
| `glare-review-coach` | coaching mode for review facilitation | "coach me through this review" |
| `glare-review-run-transcript` | score an existing transcript | "score this transcript" · "analyze this call" |

---

## Design Signals (5)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-signals` | working with design signals broadly | "design signals" · "signal anatomy" |
| `glare-signals-components` | the 6-piece anatomy of a signal | "parts of a signal" · "signal structure" |
| `glare-signals-types` | signal types (Need / Use / Prefer / Adopt) | "what type of signal is this" |
| `glare-signals-quality` | signal quality and failure points | "is this signal good enough" |
| `glare-signals-capturing` | capturing signals (4-stage flow) | "how do I capture this signal" |

---

## Decision Map (21)

The four facets connect into one decision flow: Define → Measure → Focus → Lead, looping back to Define.

### Decision Map parent

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-decision-map` | working with the four-facet flow that connects user needs to outcomes | "Decision Map" · "trace a decision from problem to outcome" · "how do the four facets connect" |

### Define (5) — agree on what matters before building

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-define` | in the Define area, multi-block question | "Credibility" · "who are we designing for" · "what should we measure" |
| `glare-define-user-needs` | working on the User Needs block (what users actually need) | "what user need does this solve" · "is this a want or a need" · "5 categories × 4 needs" |
| `glare-define-audience` | defining WHO their signals come from (the four-voice frame) | "who are we designing for" · "design for everyone is design for no one" |
| `glare-define-collecting` | in the Collecting block (instruments, techniques, tools) | "how do we gather evidence" · "should we use a survey or A/B test" |
| `glare-define-ux-metrics` | in the UX Metrics block (Attitudinal / Behavioral / Performance / Intelligence) | "high satisfaction + low completion" · "vanity vs actionable metrics" |

### Measure (5) — turn intuition into evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-measure` | producing evidence within the Measure area | "we believe that [change] for [audience] will [impact]" |
| `glare-measure-concepts` | working on the Concepts move (anchor intent before solutioning) | the 5-minute test · "what's the user need + business goal + signal here" |
| `glare-measure-hunches` | forming a falsifiable Hunch | "we believe…" · "we believe that [change] for [audience] will [impact] because [reason]" |
| `glare-measure-questioning` | drafting, critiquing, or organizing research questions | "Do people like our homepage?" · "Can users find pricing within 5 seconds?" |
| `glare-measure-findings` | in the Findings move (translate data into signals) | "what does this data mean" · "I have a number but no decision" |

### Focus (5) — turn signals into directional clarity

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-focus` | working in the Focus area, broad question | "v1 vs v2" · "competitor review" |
| `glare-focus-initiatives` | choosing what to pursue (the 10 initiative types) | "what should we focus on" · "Simplify Identity & Access vs Streamline Checkout" |
| `glare-focus-methods` | picking how to measure (the 13 method frames) | "HEART" · "RICE" · "Kano" · "JTBD" · "what method should we use" |
| `glare-focus-comparing` | benchmarking versions, competitors, or segments | "how do we compare" · "is this an improvement or just a change" |
| `glare-focus-decisions` | making the call (Implement / Refine / Test / Revisit / Do Not Pursue) | "what's the decision" · "Decision Record" · "meeting ended without a decision" |

### Lead (5) — translate design work into business evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-lead` | connecting design to business impact, broad question | "prove design ROI" · "executive narrative" |
| `glare-lead-business-goals` | anchoring to the 9 business pressures and 20 measurable goals | "Reduce churn" · "Lower support costs" · "Growth / Retention / Efficiency" |
| `glare-lead-mapping` | drawing the Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Goal) | "Chain of Proof" · "ladder our metrics" |
| `glare-lead-results` | running the Initiatives → Findings → Decisions → Outcomes loop | "outputs vs outcomes" · "leadership doesn't see what we're contributing" |
| `glare-lead-workflows` | translating signals into Sales / Marketing / Product / Eng / Strategy / Ops / Finance / Legal language | "how do I tell sales this is working" · "design ROI for Finance" |

---

## Design Assessment (9)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-assessment` | assessing org design maturity (parent) | "design assessment" · "maturity model" |
| `glare-assessment-organizing-work` | Organizing Work dimension | "how organized is our design practice" |
| `glare-assessment-managing-complexity` | Managing Complexity dimension | "are we managing complexity well" |
| `glare-assessment-building-proof` | Building Proof dimension | "how strong is our evidence practice" |
| `glare-assessment-guiding-decisions` | Guiding Decisions dimension | "are we guiding decisions effectively" |
| `glare-assessment-scaling-influence` | Scaling Influence dimension | "how do we scale design influence" |
| `glare-assessment-scoring` | scoring the assessment | "score our assessment" |
| `glare-assessment-reading` | reading assessment patterns | "what do our scores mean" |
| `glare-assessment-using-results` | acting on assessment results | "what do we do with these results" |

---

## UX Metrics (10)

A full metric framework: the 4-type taxonomy plus 9 deep-dive sub-skills covering what metrics are, why they matter, the measurement system, three metric-type libraries (28 metrics total), metric stacks, mapping impact, and operational use cases.

### UX Metrics parent

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-ux-metrics` | broad UX metrics question — the framework + 4-type taxonomy | "UX metrics" · "what types of metrics exist" · "Attitudinal vs Behavioral vs Performance" |

### Foundations (3)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-ux-metrics-what-is` | defining what a UX metric actually is (User Attribute · Data Type · Collection Method · Benchmark) | "what is a UX metric" · "parts of a metric" |
| `glare-ux-metrics-why` | making the case for UX metrics (AI-acceleration, leading indicators) | "why do we need UX metrics" · "why can't we just use product analytics" |
| `glare-ux-metrics-system` | building a measurement system (Confusion Trap · Friction Wall · Trust Gap) | "measurement system" · "how do metrics work together" |

### Metric-type libraries (3)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-ux-metrics-attitudinal` | attitudinal metrics — 9-metric library (Appeal, Brand Score, Desirability, Expectations, Feeling, Loyalty, Satisfaction, Sentiment, Usefulness) | "satisfaction" · "how do users feel" · "attitudinal" |
| `glare-ux-metrics-behavioral` | behavioral metrics — 8-metric library (Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability) | "task success" · "can users do it" · "behavioral" |
| `glare-ux-metrics-performance` | performance metrics — 11-metric library (Abandonment Rate, Bounce Rate, CTR, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency) | "bounce rate" · "time on task" · "performance metrics" |

### Application (3)

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-ux-metrics-stack` | designing metric stacks (Design Stacks vs Research Stacks, four experience traps) | "metric stack" · "which metrics go together" |
| `glare-ux-metrics-mapping` | mapping metrics to impact (Situation → Intent → Outcomes → Results) | "map metrics to business impact" · "design impact mapping" |
| `glare-ux-metrics-applying` | operationalizing metrics (8 use cases) | "how do I use these metrics" · "metric playbook" |

---

## How activation works

Claude reads each skill's description (the YAML frontmatter `description:` field) and matches against the user's message. The richer the trigger phrasing in your message, the more reliably the right skill loads. Phrases in quotes above are pulled directly from each skill's description — using them in conversation is the fastest way to invoke a specific skill.

Parent skills (`glare-decision-map`, `glare-define`, `glare-measure`, `glare-focus`, `glare-lead`, `glare-ux-metrics`) handle multi-bucket questions and route to children. If you're not sure which child applies, just stay in the parent — it covers enough surface to keep going.

When you're lost across sections, use `glare-router` — it diagnoses entry state and recommends ONE specific skill.

## Versioning

- Plugin version: **2.2.0** (UX Metrics expanded to 10-skill cluster, 2026-05-10)
- Each `SKILL.md` carries `version`, `source_doc_version` (which Drive doc generation it was built from), and `last_rebuilt`. See `CHANGELOG.md` for the full history.
