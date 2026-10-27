# Reference — Glare Measure: Questioning

> Refreshed 2026-05-11 from Drive doc *Glare | Measure, Questioning v1.1* (Oct 26, 2025).

> **Source-doc note (taxonomy):** This document preserves the **Behavioral / Attitudinal / Performance / Perceptual** UX-metric families as written in Questioning v1.1. The Glare marketplace **UX Metrics framework v1.32** has since moved to **Attitudinal · Behavioral · Performance · Intelligence** as the 4th type — the Perceptual content (comprehension, recognition, interpretation) has been folded into the Behavioral family. When a user crosses into the UX Metrics skills (`glare:ux-metrics`, `glare:define-ux-metrics`, `glare:ux-metrics-applying`, etc.), use the v1.32 taxonomy. When working strictly inside the Questioning step, the v1.1 wording (Perceptual) is fine.

---

## Canonical 28 Metrics

When a question is aligned to a **specific** UX metric (not just a family), recommend **only** from these 28. Anything else is "outside the canonical 28" and must be flagged with a reason.

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

> Note: the v1.1 STEP 6 table below uses shorthand like "First Click Success," "Satisfaction or Sentiment Score," and "Comprehension" — when you commit a question to a specific metric, snap to the canonical name (Success, Satisfaction or Sentiment, Comprehension respectively).

---

## When to use

- When the user is drafting, critiquing, or organizing research questions.
- When sorting questions into the four types — People (habits/behaviors), Process (steps/friction), Product (clarity/usefulness), Problem (barriers).
- When choosing a Mode — Exploratory, Evaluative, Comparative.
- When running the bias check — leading? loaded? jargon-heavy?
- When promoting open questions into testable ones (e.g., "Do people like our homepage?" → "Can users find pricing within 5 seconds?").
- When aligning questions to a UX metric family — Behavioral, Attitudinal, Performance, Perceptual.

**Don't use when** anchoring intent (use `glare:measure-concepts`), forming a hunch (`glare:measure-hunches`), translating data (`glare:measure-findings`), or asking about the loop (`glare:measure`). For Need / Use / Prefer / Adopt, use `glare:signals-types`.

## Turn curiosity into clarity

Every signal starts with a question. Questioning turns curiosity into measurable clarity. It transforms hunches into testable direction and helps teams prove whether their ideas truly make sense.

When questioning is strong, it reveals not just what people say but what they actually understand, expect, and value. Weak questions collect noise; strong ones expose truth — the gap between what users intend to do and what the design allows them to do.

Questioning is where ideas take shape. It links **Concepts** to **Hunches**, converts them into **Questions**, and produces **Findings** that become usable signals.

### What good questioning does

- Surfaces hidden user challenges.
- Avoids bias so feedback reflects reality, not team assumptions.
- Guides the design process with targeted insights.
- Translates raw curiosity into measurable data.

### 5-section structure of the source doc

1. **Getting Started**
2. **Begin Questioning** (the 8-step process)
3. **Make It Practical** (worksheet + checklist)
4. **See It in Action**
5. **Apply and Evolve**

---

## GETTING STARTED — Why questioning matters

Questioning gives shape to curiosity. It turns the first spark of an idea into something measurable. In Glare, Questioning lives in the **Measure** layer — it connects early hunches to evidence and makes sense of what users show and say.

Strong questioning is not about asking more. It is about asking with intent. Each question defines what you need to learn and what kind of evidence will make that learning useful.

### Element-to-Questioning mapping (Concepts → Hunches → Questions → Findings)

| Element  | What it focuses on                                            | How it connects to questioning                            |
| -------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| Concepts | The initial ideas or experiences that need understanding.     | Questioning defines how these ideas will be evaluated.    |
| Hunches  | Early beliefs about what might work for users.                | Questioning helps expose whether those beliefs hold true. |
| Questions | Focused prompts that clarify what to measure and why.        | Questioning turns curiosity into structured investigation.|
| Findings | Patterns that emerge from user responses and behaviors.       | Questioning provides the input that becomes measurable proof. |

### The 4 question types

| Type    | What it focuses on                                            | Purpose                                          | Example                                            |
| ------- | ------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------- |
| People  | The motivations, preferences, and habits of your users.       | Learn who users are and what drives behavior.    | "How often do users complete this workflow?"       |
| Process | The steps and decisions users take to reach a goal.           | Understand where friction occurs.                | "What steps do users take to upload a file?"       |
| Product | The clarity and usefulness of what has been designed.         | Evaluate how users understand and interact.      | "Do users understand the purpose of this page?"    |
| Problem | The barriers that prevent success or satisfaction.            | Uncover what breaks down, confuses, or frustrates. | "What prevents users from completing checkout?"  |

**People + Process** give context. **Product + Problem** give clarity.

### What makes a question testable

A testable question (1) defines a gap in understanding, (2) points to observable behavior or perception, and (3) can be measured and acted upon.

- ❌ "Do people like our homepage?"
- ✅ "Can users find pricing info on the homepage within 5 seconds?"

Before finalizing, pre-test: ask a colleague to review, run a small dry test, check if users understand what's being asked.

### Modes of Questioning

| Mode         | When to use                                          | Core question                                  | What you get                                  |
| ------------ | ---------------------------------------------------- | ---------------------------------------------- | --------------------------------------------- |
| Exploratory  | Early discovery, before firm hypotheses.             | What should we learn or improve?               | Patterns, context, unmet needs.               |
| Evaluative   | Mid-cycle, once ideas or designs exist.              | Does this design work for users?               | Clarity, comprehension, usability metrics.    |
| Comparative  | Later, when choosing between directions.             | Which version performs or communicates better? | Confidence and measurable proof of improvement. |

Exploratory work builds understanding. Evaluative work strengthens clarity. Comparative work provides confidence in what to move forward with.

---

## BEGIN QUESTIONING — The 8-step process

Each step follows the rhythm: **Concepts → Hunches → Questions → Findings**.

### STEP 1 — Clarify the concept

Strong questions begin with clarity. Your concept is the focus (the product, flow, or message). Your hunches are the beliefs that guide it.

- What assumptions are we making about how users will act or respond?
- What part of this concept do we most need to understand?
- What outcomes are we hoping to confirm or challenge?
- What would success look like if our hunch is correct?

### STEP 2 — Identify knowledge gaps

Turn hunches upside down — surface what you *don't* know.

- What assumptions haven't been tested?
- Where do we lack proof or confidence?
- What do we think we know but can't yet show with data?
- What would surprise us if it turned out to be false?

### STEP 3 — Define learning goals

Translate uncertainty into direction. Pick a mode and frame the goal.

| Mode         | When to use                                  | Learning goal                                          | Example                                                 |
| ------------ | -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| Exploratory  | Early stages, little is known.               | Discover unmet needs or behaviors.                     | "Understand how users choose between two plan types."   |
| Evaluative   | Mid-stage, testing an existing concept.      | Measure clarity, usability, or comprehension.          | "See if users can complete checkout without confusion." |
| Comparative  | Later stages, choosing between options.      | Decide which version performs better or builds trust.  | "Compare two headlines to see which drives more sign-ups." |

### STEP 4 — Write open-ended research questions

Open-ended questions explore user perception and experience without assumption. They help you understand behavior, language, and decision-making.

Examples:

- What do users expect when they first see this page?
- How do they describe the purpose of this feature in their own words?
- What steps do they take when they get stuck?

**Bias check:**

- Is this question leading users to say "yes"?
- Does it echo our internal assumptions?
- Is the language emotionally charged or too technical for real users?

Neutral questions surface what people actually experience. They turn curiosity into honest feedback.

### STEP 5 — Translate into testable questions

Turn research questions into measurable prompts that show observable behavior or perception.

- Can users find the pricing information within five seconds?
- Can users complete checkout without help?
- Do users understand what this feature does after reading the headline?

Testable questions point directly to data — not opinions.

### STEP 6 — Align questions with UX metrics

| UX Metric Type | What it reveals                  | Example question                                          | Example metric                  |
| -------------- | -------------------------------- | --------------------------------------------------------- | ------------------------------- |
| Behavioral     | What users do.                   | Where do users click first?                               | First Click Success             |
| Attitudinal    | What users think or feel.        | How satisfied are users after completing the task?        | Satisfaction or Sentiment Score |
| Performance    | How efficiently users succeed.   | How long does it take to complete checkout?               | Time on Task                    |
| Perceptual     | What users understand or interpret. | Do users understand the purpose of this page?          | Comprehension                   |

> **Source-doc note:** v1.1 still lists Perceptual as the 4th family. The marketplace v1.32 UX Metrics framework now uses **Intelligence** in that slot, and comprehension/recognition have moved into Behavioral. If you route to a UX-metric skill, expect the v1.32 mapping there.

Behavioral and attitudinal metrics can be collected directly in **Helio** as leading indicators. Run surveys and concept tests in Helio to capture what users do and how they feel — early enough to change direction.

### STEP 7 — Prioritize and refine

Most teams have more questions than time or budget. Prioritize:

| Factor      | What it reveals                                          | How to use it                                       |
| ----------- | -------------------------------------------------------- | --------------------------------------------------- |
| Gap Size    | The degree of uncertainty or risk in current understanding. | Focus on areas with the least clarity.           |
| Impact      | The potential value of answering the question.            | Prioritize questions tied to decisions that affect users or outcomes directly. |
| Feasibility | The time, cost, and resources available.                  | Choose what can realistically be tested this cycle. |
| Confidence  | The team's belief in current assumptions.                 | Address low-confidence areas first.                 |

Questions at the intersection of **large gap + high impact + feasible effort** rise to the top.

### STEP 8 — Match questions to techniques

| Technique Focus | Common methods                                         | Typical metrics                              | Example question                                    |
| --------------- | ------------------------------------------------------ | -------------------------------------------- | --------------------------------------------------- |
| Behavioral      | First-click tests, task success analysis               | Completion, engagement, navigation clarity   | "Where do users click first on this page?"          |
| Attitudinal     | Surveys, desirability studies, satisfaction scoring    | Trust, sentiment, satisfaction               | "How confident do users feel after completing this task?" |
| Performance     | Usability tests, time tracking, error rate             | Efficiency, error reduction                  | "How long does it take to complete checkout?"       |

For behavioral and attitudinal techniques, Helio is the platform for collecting these as leading indicators. First-click tests, surveys, desirability studies, and satisfaction scoring can all run in Helio before your product reaches real traffic.

The **Glare Questioning Canvas** is a full-featured Figma-style layout using React components with form-style input boxes and a light theme.

---

## MAKE IT PRACTICAL — Plan your questioning cycle

| Step                       | Action                                                  | Output                                              |
| -------------------------- | ------------------------------------------------------- | --------------------------------------------------- |
| 1. Clarify the Concept     | Identify the idea or assumption you want to explore.    | Clear articulation of what you believe and want to learn. |
| 2. Identify Gaps           | List the uncertainties or missing knowledge areas.      | Focused list of what you do not yet understand.     |
| 3. Define Learning Goals   | Choose exploring, evaluating, or comparing.             | Framed goals that define what success looks like.   |
| 4. Write Questions         | Draft open-ended questions that reveal user understanding. | Structured list of user-focused prompts.         |
| 5. Make Them Testable      | Translate each question into a measurable version.      | Test-ready questions linked to metrics.             |
| 6. Align With UX Metrics   | Assign metrics for clarity, satisfaction, and success.  | Consistent measurement plan across studies.         |
| 7. Prioritize              | Evaluate which questions are most valuable or feasible. | Ranked question list ready for testing.             |
| 8. Match to Techniques     | Select the right testing or research methods.           | Plan of which tools and techniques to use.          |

### Quick Checklist (before each round)

- We've defined a single concept or assumption to explore.
- We've identified what we don't understand yet.
- Our learning goal is clear — exploratory, evaluative, or comparative.
- Each question connects to a UX metric.
- We've prioritized based on gaps, impact, and feasibility.
- Our techniques and tools are ready to run.
- The results will connect to findings that move design forward.

Strong questioning is less about volume and more about precision.

---

## 5 routines for integrating questioning into workflow

1. **Weekly Discovery Review** — Begin each week by identifying which assumptions or user behaviors need clarity. Frame these into questions you can test or observe within the week.
2. **Sprint Planning** — Pair every major design or product task with at least one measurable question. Make it visible on the board: *"What do we need to learn before we move forward?"*
3. **Post-Test Reflection** — End each sprint or test cycle by reviewing which questions produced usable signals. Note which were too broad or biased, and refine them for the next round.
4. **Share the Questions, Not Just the Answers** — When findings are shared, include the questions that led to them. This helps others understand intent and replicate the method.
5. **Build a Question Library** — Over time, collect well-framed, tested questions in a shared workspace. Reuse them as templates for future projects to keep consistency.

### Workflow benefits

| Benefit       | What it delivers                                            |
| ------------- | ----------------------------------------------------------- |
| Focus         | Teams align around what to learn next instead of debating opinions. |
| Speed         | Clear questions shorten the time between testing and decisions. |
| Confidence    | Each question backed by metrics creates evidence leaders can trust. |
| Scalability   | Reusing question frameworks builds consistency across projects. |

---

## SEE IT IN ACTION

*How a single question turned confusion into clarity* — paired worked example showing weak ("Do people like our homepage?") vs. strong ("Can users find pricing within 5 seconds?") and how the testable form fed directly into a first-click test that produced an actionable signal.

---

## APPLY AND EVOLVE

### Business impact

| Benefit              | What it creates                                                   | Example impact                                              |
| -------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------- |
| Faster Focus         | Clear learning goals eliminate wasted research.                   | Teams cut discovery cycles to hours instead of weeks.       |
| Better Decisions     | Questions tied to metrics create credible findings.               | A single comprehension test clarifies layout choice, saving dev time. |
| Cross-Team Alignment | Shared questioning frameworks connect research, design, product.  | Product, design, and marketing test message clarity using the same questions. |
| Proven Value         | Measurable questions link user insight to business results.       | Improved comprehension leads to higher conversion and reduced churn. |

### Reflection prompts

- Did our questions address the biggest gaps in understanding?
- Which questions produced strong findings, and which stayed too broad?
- Did we link each question to a clear UX metric and measurable outcome?
- How did the answers change what we decided to do next?
- What will we ask differently next time?

### Next steps (transitions)

| If you are here          | Move to                                       | What you gain                                  |
| ------------------------ | --------------------------------------------- | ---------------------------------------------- |
| Concepts → Hunches       | Clarify what you believe and what to learn.   | Clear intent for what to test.                 |
| Hunches → Questioning    | Turn beliefs into measurable prompts.         | Defined questions linked to UX metrics.        |
| Questioning → Findings   | Collect results and analyze through metrics.  | Actionable insights grounded in data.          |
| Findings → Signals       | Combine metrics into patterns that prove impact. | Clear, comparable signals that build design credibility. |

### Closing thought

Good questions are the foundation of design measurement. They connect curiosity to clarity, intent to evidence, and intuition to influence. When your team questions well, design stops being opinion and becomes proof that earns trust.

---

## Key terms (Questioning-relevant)

- **Question (Research vs. Testable)** — Research questions are open-ended and user-focused; testable questions point to observable behavior/perception and a measurable outcome.
- **Question Types** — People, Process, Product, Problem. People + Process = context; Product + Problem = clarity.
- **Modes of Questioning** — Exploratory (discover), Evaluative (validate clarity/usability), Comparative (decide between options).
- **UX Metric Types (v1.1 doc)** — Behavioral, Attitudinal, Performance, Perceptual. (v1.32 framework swaps Perceptual for Intelligence; comprehension moves into Behavioral.)
- **Bias check** — Pre-flight: is it leading? echoing assumptions? emotionally loaded? too technical?
- **Question Library** — Reusable, well-framed, tested questions stored in a shared workspace for cross-project consistency.
- **Glare Questioning Canvas** — Figma-style React layout (light theme, form input boxes) that operationalizes the steps.

---

## Resources

- *User Research Questions* — UX Research Field Guide, User Interviews
  <https://www.userinterviews.com/ux-research-field-guide-chapter/user-research-questions>
- *The Best User Research Questions (+ How to Ask Them)* — Maze
  <https://maze.co/blog/research-questions/>
- *A Step-by-Step Guide to Writing Better Research Questions* — dscout
  <https://dscout.com/people-nerds/guide-better-questions>
- *How to ask good questions and level-up your user research skills* — Envoy Design
  <https://medium.com/envoy-design/how-to-ask-good-questions-and-level-up-your-user-research-skills-19fd28b275a4>
- *Crafting good UX research questions for qualitative research* — PlaybookUX
  <https://www.playbookux.com/crafting-good-ux-research-questions-for-qualitative-research/>
- *The NCredible Framework — UX research questions prioritised* — UX Insight
  <https://uxinsight.org/a-practical-tool-for-prioritising-research-questions-and-ensuring-that-they-dont-all-end-up-in-a-usability-test/>
- *How to ask the right UX questions and avoid the wrong ones* — Reddit r/userexperience
  <https://www.reddit.com/r/userexperience/comments/oorfjq/how_to_ask_the_right_ux_questions_and_avoid_the/>
- *How to write effective UX research questions (with examples)* — Hotjar
  <https://www.hotjar.com/ux-research/questions/>

## Failure modes

These are common ways this skill goes wrong in practice:

- **Leading questions.** "How much easier was this version?" presumes the answer. The bias check catches this — neutral wording produces neutral signals.
- **Open question that can't be measured.** "What did you think?" yields a thousand quotes but no signal. Promote open questions into testable, specific prompts tied to a UX metric.
- **Question type doesn't match decision type.** Asking People-type questions (habits) when the decision is about Product clarity. The four question types exist so the team aims at the right kind of evidence for the moment.
- **Mode confusion.** Mixing Exploratory and Comparative questions in one session — open enough to generate hypotheses, structured enough to mislead as comparison. Pick a Mode per study.
- **Jargon questions.** Using product or design vocabulary participants don't share ("How discoverable is this nav?"). The user's plain-language version is the only one that produces clean signal.

