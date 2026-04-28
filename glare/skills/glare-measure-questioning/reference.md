# Reference — Glare Measure: Questioning

Verbatim extraction of the Questioning-relevant sections of `measure-compressed.md` (v1.0 and v1.1).

---

## Glare | Measure, Questioning v1.0

The first version of the Questioning module: a stepped process for creating research questions that produce useful UX measurement.

- **Why questioning matters**: Weak questions stall in indecision; strong questions expose where users struggle, what they value, and whether the design works. Questioning aligns metrics to intent.
- **What good questioning does**: surfaces hidden challenges; avoids bias; guides design with targeted insights; translates curiosity into measurable data.
- **STEP 1 — Clarify the Initiative**. Ask: what are we trying to learn/improve/validate? What decision will this inform? Where in the process are we (exploration, prototyping, post-launch)? Who needs the insight? What's the risk if we don't get it right?
- **Types of Questions** (4 categories): **People** (habits/preferences/behaviors — "How often do users complete this workflow?"); **Process** (steps + friction — "What steps do users take to upload a file?"); **Product** (clarity/usefulness — "Do users understand the purpose of this page?"); **Problem** (barriers — "What prevents users from completing checkout?").
- **STEP 2 — Identify Knowledge Gaps**: List unknowns important to the decision. Check user mindset/context — language they'll understand, what matters in the moment — to avoid jargon.
- **STEP 3 — Turn Gaps into Broad Learning Goals**: Define what to learn before drafting questions. Distinguish strategic (broad, long-term) vs. tactical (specific feature/flow).
- **STEP 4 — Write Open-Ended Research Questions**: Open-ended, user-focused, unbiased. Bias check: is it leading? Echoing internal assumptions? Emotionally loaded or too technical?
- **STEP 5 — Translate to Testable Questions**: Frame so each connects to a technique and yields actionable feedback. Examples: "Can users locate pricing within 5 seconds?" → First Click Testing; "Do users understand the page purpose?" → Survey + Heatmap; "What stops checkout?" → Clickstream + Task Success.
- **UX Metric Types table**: Behavioral (what users do — heatmaps, clickstream); Attitudinal (what they think/feel — surveys); Performance (how well they complete tasks — task success, time on task).
- **Testable question criteria**: Specific & focused; linked to measurable outcome; actionable; aligned with user goals (not just business). Weak: "Do people like our homepage?" Strong: "Can users find pricing info on the homepage within 5 seconds?"
- **STEP 6 — Align Questions with UX Metrics**: Mapping table — task success ↔ completion rate; time on task ↔ efficiency; survey + comprehension ↔ clarity; first click ↔ intuition/desirability.
- **STEP 7 — Prioritize and Refine**: by relevance to design decision, feasibility (timeline, resources), and impact on outcome.
- **STEP 8 — Match Questions to Techniques**: Observe action → behavioral techniques (Clickstream, Heatmaps); Measure performance → task-based metrics (Completion, Time); Understand opinions → attitudinal methods (Surveys).
- The Glare Questioning Canvas exists as a Figma-style React layout with form-style input boxes (light theme) for running this process.

---

## Glare | Measure, Questioning v1.1

Evolved version of Questioning. Adds a **Mode of Questioning** layer (Exploratory/Evaluative/Comparative), reframes the 8-step process around the Concepts→Hunches→Questions→Findings rhythm, and adds workflow-integration guidance.

- **Section structure**: Getting Started → Begin Questioning → Make It Practical → See It in Action → Apply and Evolve.
- **Element-to-Questioning mapping**: Concepts (initial ideas → questioning defines how they're evaluated); Hunches (early beliefs → questioning exposes whether they hold); Questions (focused prompts → questioning structures investigation); Findings (emerging patterns → questioning supplies the input).
- **4 Question Types** (same as v1.0): People, Process, Product, Problem. People + Process give context; Product + Problem give clarity.
- **What makes a question testable** (3 criteria): defines a gap in understanding; points to observable behavior or perception; can be measured and acted upon. ❌ "Do people like our homepage?" / ✅ "Can users find pricing info on the homepage within 5 seconds?" Pre-test by having teammates review and running a small dry test.
- **Modes of Questioning**:
  - **Exploratory** — early discovery, no firm hypotheses; "What should we learn or improve?"; yields patterns, context, unmet needs.
  - **Evaluative** — mid-cycle, designs exist; "Does this design work for users?"; yields clarity, comprehension, usability metrics.
  - **Comparative** — late-stage, choosing between directions; "Which version performs better?"; yields confidence and proof of improvement.
- **8-Step Process (v1.1 phrasing)**:
  1. **Clarify the concept** — surface assumptions; what success looks like if hunch is right.
  2. **Identify knowledge gaps** — what's untested, where confidence is weak, what would surprise you if false.
  3. **Define learning goals** — pick mode (Exploratory/Evaluative/Comparative) and frame the goal.
  4. **Write open-ended research questions** — explore perception/experience without assumption; bias check.
  5. **Translate into testable questions** — observable behavior/perception, point directly to data.
  6. **Align with UX metrics** — Behavioral (First Click Success), Attitudinal (Satisfaction/Sentiment), Performance (Time on Task), Perceptual (Comprehension).
  7. **Prioritize and refine** — filters: Gap Size, Impact, Feasibility, Confidence; questions at intersection of large-gap + high-impact + feasible rise to top.
  8. **Match questions to techniques** — Behavioral (first-click, task success), Attitudinal (surveys, desirability, satisfaction scoring), Performance (usability tests, time tracking, error rate).
- **Make It Practical — Worksheet** mirrors the 8 steps with action + output for each, becoming a roadmap for a questioning cycle. Pre-cycle checklist confirms one concept, identified gaps, clear learning mode, metric per question, prioritization, ready techniques, and connection to findings.
- **Integrate into Workflow** (repeatable routine):
  1. **Weekly Discovery Review** — identify assumptions/behaviors needing clarity.
  2. **Sprint Planning** — pair every major task with at least one measurable question on the board.
  3. **Post-Test Reflection** — review which questions produced usable signals; refine biased/broad ones.
  4. **Share the questions, not just the answers** — include the question that led to a finding.
  5. **Build a Question Library** — collect well-framed, tested questions for reuse.
- **Business impact**: Faster Focus (cuts discovery cycles to hours); Better Decisions (credible findings); Cross-Team Alignment (shared frameworks across product/design/marketing); Proven Value (measurable insight → conversion/churn impact).
- **Reflection prompts**: Did questions address biggest gaps? Which produced strong findings vs. stayed broad? Was each tied to a UX metric? How did answers change the next decision? What will we ask differently?
- **Next-step transitions table**: Concepts→Hunches (clarify belief & learning need) → Hunches→Questioning (turn beliefs into measurable prompts) → Questioning→Findings (collect & analyze through metrics) → Findings→Signals (combine metrics into patterns proving impact).

---

## Supporting framing (from Overview)

- *Questioning* call-outs: avoid biased framing; tie questions to outcomes; uncover the "why" behind behavior; refine each round.

---

## Key terms (Questioning-relevant)

- **Question (Research vs. Testable)** — Research questions are open-ended and user-focused; testable questions point to observable behavior/perception and a measurable outcome.
- **Question Types** — People, Process, Product, Problem. People+Process = context; Product+Problem = clarity.
- **Modes of Questioning** — Exploratory (discover), Evaluative (validate clarity/usability), Comparative (decide between options). v1.1 addition.
- **UX Metric Types** — Behavioral (what users do), Attitudinal (what they think/feel), Performance (how efficiently they succeed), Perceptual (what they understand) — last added in v1.1.
- **Bias check** — Pre-flight on questions: is it leading? echoing assumptions? emotionally loaded? too technical?
- **Question Library** — Reusable, well-framed, tested questions stored in a shared workspace for cross-project consistency.
- **Glare Questioning Canvas** — Figma-style React layout (light theme, form input boxes) that operationalizes the questioning steps.
