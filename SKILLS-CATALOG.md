# Glare Skills Catalog (v1.5.0)

Quick reference for all **55 skills** in the Glare plugin. Each row shows what the skill is for and the kinds of phrases that auto-trigger it. After installing the plugin, you don't invoke skills by name — Claude loads the right one when your conversation matches its description. This catalog helps you scan what's available.

**Install once:**

```
/plugin marketplace add ~/Desktop/zurb.nosync/skills/glare-marketplace
/plugin install glare@glare-marketplace
```

All 55 skills become available. Sections below group them by role.

---

## Navigation

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-router` | mid-flow and lost — need a cross-section pointer to one specific skill | "where should I go next" · "which Glare skill applies" · "I'm stuck and don't know where to start" |

---

## Get Started (7)

Onboarding, framework tour, AI workflows, glossary.

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-get-started` | new to Glare or asking introductory questions | "what is Glare" · "how do we start using Glare" |
| `glare-create-first-signal` | trying Glare on a real decision they're sitting in front of right now | "create my first signal" · "I have a decision and don't know what to do" |
| `glare-how-glare-works` | wants the conceptual tour of how Glare works as a system | "how does Glare work" · "what are the parts of Glare" |
| `glare-ai-workflows` | asking how Glare works alongside AI tools (ChatGPT, Claude, Ray) | "use Glare with ChatGPT" · "what's the difference between a prompt and a Skill" |
| `glare-coaching-advising` | a leader weighing how to roll Glare out across their org | "how do I roll out Glare" · "we want coaching on Glare" |
| `glare-proving-design-impact` | trying to show, defend, or measure the impact of design | "prove design impact" · "show design's contribution" |
| `glare-glossary` | asking what a Glare term means or wants a precise definition | "what's a design signal" · "what's the difference between a prompt and a Skill" |

---

## Design Review (12)

The SIGNAL flow (Surface · Identify · Ground · Navigate · Align · Lock) plus scoring, rubric, coaching, and transcript evaluation. Supersedes the old standalone `signal-call-rubric` and `signal-call-coach` skills.

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-review` | asking about Design Review as a top-level concept | "what is the SIGNAL framework" · "how do I run a better design review" |
| `glare-review-surface` | working on the Surface step (expose the real tension) | "team is reacting to the design before agreeing on the problem" · "feedback is scattered" |
| `glare-review-identify` | working on the Identify step (define what "better" means) | feedback is all preference · "what does success look like here" |
| `glare-review-ground` | working on the Ground step (anchor in evidence not opinion) | "conversation keeps looping on opinion" · "people are defending preferences" |
| `glare-review-navigate` | working on the Navigate step (lead the decision) | "we keep exploring without choosing" · "the team won't make a recommendation" |
| `glare-review-align` | working on the Align step (clarity around ownership) | "everyone agreed but no one owns it" · "responsibility is blurry" |
| `glare-review-lock` | working on the Lock step (convert insight to motion) | "the call ended without next steps" · "we always end with 'we'll follow up'" |
| `glare-review-techniques` | wants the cross-cutting view of Design Review techniques | "what techniques can I use in a design review" · "how do I shape feedback in real time" |
| `glare-review-scoring-model` | wants the SIGNAL scoring rubric itself | "how do I score a design review" · "what does a 3 mean for Surface" |
| `glare-review-rubric` | evaluating a real design review or client call against the full rubric | paste a transcript · "score this call" |
| `glare-review-coach` | preparing for an upcoming review or coaching someone after one | "prep me for a kickoff" · "what should I do better next time" |
| `glare-review-run-transcript` | wants the end-to-end workflow for evaluating a transcript | "I have a transcript — what do I do with it" · "how do I run a transcript through SIGNAL" |

---

## Design Signals (5)

What a Design Signal is, what makes one usable, how to capture them.

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-signals` | asking about Design Signals as a top-level concept | "what is a design signal" · "why do signals matter" |
| `glare-signals-components` | building or strengthening an individual signal | "what goes into a signal" · "anatomy of a signal" (the 6-piece model) |
| `glare-signals-types` | asking about the kinds of Design Signals | "what are the four signal types" · "Need / Use / Prefer / Adopt" |
| `glare-signals-quality` | evaluating whether a signal is good enough to act on | "is this signal usable" · "is this a signal or just a metric" |
| `glare-signals-capturing` | wants the end-to-end workflow for creating signals inside the work | "how do I capture a signal" · "how do we run a fast signal-capture loop" |

---

## Decision Map (21)

Define → Measure → Focus → Lead, the spine of Glare. Decision Map parent + 4 areas, each with 4 sub-skills.

### Decision Map parent

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-decision-map` | working with the four-area flow that connects user needs to outcomes | "Decision Map" · "trace a decision from problem to outcome" |

### Define (5) — agree on what matters before building

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-define` | in the Define area, multi-block question | "Credibility" · "who are we designing for" |
| `glare-define-user-needs` | working on the User Needs block (what users actually need) | "what user need does this solve" · "is this a want or a need" |
| `glare-define-audience` | defining WHO their signals come from (the four-voice frame) | "who are we designing for" · "design for everyone is design for no one" |
| `glare-define-collecting` | in the Collecting block (instruments, techniques, tools) | "how do we gather evidence" · "should we use a survey or A/B test" |
| `glare-define-ux-metrics` | in the UX Metrics block (Attitudinal / Behavioral / Performance) | "high satisfaction + low completion" · "vanity vs actionable metrics" |

### Measure (5) — turn intuition into evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-measure` | producing evidence within the Measure area | "we believe that [change] for [audience] will [impact]" |
| `glare-measure-concepts` | working on the Concepts move (anchor intent before solutioning) | the 5-minute test · "what's the user need + business goal + signal here" |
| `glare-measure-hunches` | forming a falsifiable Hunch | "we believe…" · "we believe that [change] for [audience] will [impact] because [reason]" |
| `glare-measure-questioning` | drafting, critiquing, or organizing research questions | "Do people like our homepage?" · "Can users find pricing within 5 seconds?" |
| `glare-measure-findings` | in the Findings move (translate data into signals) | "what does this data mean" · "how do I share what we learned" |

### Focus (5) — turn signals into directional clarity

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-focus` | working in the Focus area, broad question | "v1 vs v2" · "competitor review" |
| `glare-focus-initiatives` | choosing what to pursue (the 10 initiative types) | "what should we focus on" · "Simplify Identity & Access vs Streamline Checkout" |
| `glare-focus-methods` | picking how to measure (the 13 method frames) | "HEART" · "RICE" · "Kano" · "JTBD" · "what method should we use" |
| `glare-focus-comparing` | benchmarking versions, competitors, or segments | "how do we compare" · "is this an improvement or just a change" |
| `glare-focus-decisions` | making the call (Implement / Refine / Test / Revisit / Do Not Pursue) | "what's the decision" · "Decision Record" · "tactical vs strategic decision" |

### Lead (5) — translate design work into business evidence

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-lead` | connecting design to business impact, broad question | "prove design ROI" · "executive narrative" |
| `glare-lead-business-goals` | anchoring to the 9 business pressures and 20 measurable goals | "Reduce churn" · "Lower support costs" · "Growth / Retention / Efficiency" |
| `glare-lead-mapping` | drawing the Chain of Proof (User Need → Design KPI → Product KPI → Business KPI → Goal) | "Chain of Proof" · "ladder our metrics" |
| `glare-lead-results` | running the Initiatives → Findings → Decisions → Outcomes loop or maturity diagnostic | "where is design impact breaking down" · "outputs vs outcomes" |
| `glare-lead-workflows` | translating signals into Sales / Marketing / Product / Eng / Strategy / Ops / Finance / Legal language | "how do I tell sales this is working" · "design ROI for Finance" |

---

## Design Assessment (9)

Diagnose where design impact is breaking down across 5 dimensions, scored 0-100.

### Parent + dimension skills

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-design-assessment` | wants the broader assessment, multiple dimensions in play | "what's our team's design maturity" · "where is design impact breaking down" |
| `glare-assessment-organizing-work` | Organizing Work dimension (4 layers: Objectives → Drivers → Learning → Outputs) | "where does design knowledge get lost" · "we keep restarting from scratch" |
| `glare-assessment-managing-complexity` | Managing Complexity dimension (3 levels: Simple → Complicated → Complex) | "our work keeps getting tangled" · "every project feels overweight" |
| `glare-assessment-building-proof` | Building Proof dimension (4 layers: Research → Intent → Outcome → Impact) | "we can't show what changed" · "design feels like opinion" |
| `glare-assessment-guiding-decisions` | Guiding Decisions dimension (4 areas: Exploratory / Operational / Analytical / Evidential) | "we keep relitigating decisions" · "loudest voice wins" |
| `glare-assessment-scaling-influence` | Scaling Influence dimension (3 levels: Contributors → Experts → Leaders) | "our proof stays local" · "leaders only see final outputs" |

### Scoring + interpretation

| Skill | Use when… | Example triggers |
|---|---|---|
| `glare-assessment-scoring` | asking how the assessment is scored or measured | "what do the score bands mean" · "Reactive vs Developing vs Functional vs Strong vs Leading" |
| `glare-assessment-reading` | interpreting the shape of results across dimensions | "what does our pattern mean" · "we're balanced but low" · "strong proof weak influence" |
| `glare-assessment-using-results` | choosing the 30-day next move from results | "what do we do with our score" · "where should we start" |

---

## How activation works

Claude reads each skill's description (the YAML frontmatter `description:` field) and matches against the user's message. The richer the trigger phrasing in your message, the more reliably the right skill loads. Phrases in quotes above are pulled directly from each skill's description — using them in conversation is the fastest way to invoke a specific skill.

Parent skills (`glare-define`, `glare-measure`, `glare-focus`, `glare-lead`, `glare-design-review`, `glare-design-signals`, `glare-design-assessment`, `glare-decision-map`) handle multi-bucket questions and can route to children. If you're not sure which child applies, just stay in the parent — it covers enough surface to keep going.

## Versioning

- Plugin version: **1.4.0** (most recent: 2026-05-06 Define refresh)
- Each `SKILL.md` carries `version`, `source_doc_version` (which Drive doc generation it was built from), and `last_rebuilt`. See `CHANGELOG.md` for the full history.

## Outside Claude Code

Each skill folder also contains a `prompt_chatgpt.md` — a portable system prompt you can paste into ChatGPT, Gemini, Claude.ai, or any other chat tool. The master combined prompt at `glare-framework-prompt.md` (marketplace root) covers the whole framework in one shot.
