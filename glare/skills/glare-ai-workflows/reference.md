# AI Workflows — Compressed (v1.3)

## Why this exists

Product and design work now happens inside fast loops. AI makes it easy to create output — prompts can generate ideas, flows, and variations quickly. Teams can explore more directions in less time. **What becomes harder is turning that output into something the team can evaluate, align on, and move forward with confidence.**

Ian Batterbee: *"AI has made it easy to generate work quickly, but much harder to know what to trust."*

The gap shows up between creation and decision. **Teams can generate faster than they can decide.**

Glare provides structure for that gap. It organizes AI-driven work so generation, evaluation, and decision-making connect — teams can move quickly without losing clarity.

---

## The AI Workflow — five roles

| Role | What it does |
|---|---|
| **Prompts generate** | Possibilities |
| **Skills shape** | How those possibilities are evaluated |
| **Agents coordinate** | The process |
| **Participant input creates** | Design signals |
| **Teams make** | Decisions with signals |

Each part has a defined role. Together, they create a repeatable way to move from idea to decision without losing structure.

---

## Prompts Generate

Prompts are a simple entry point for beginners. They are simple ways to use AI with very little setup.

A prompt can:
- turn a rough idea into a concept
- generate variations
- reframe a problem in seconds

They work with tools like ChatGPT or Gemini and expand the space of possible directions. **Prompts are fast, but they are temporary.** Each prompt is a one-time instruction.

Best used for:
- exploring ideas
- generating variations
- reframing questions
- surfacing assumptions

They create momentum, but not consistency.

---

## Skills Structure

Skills bring structure to that output. **A Skill is a reusable, versioned way of working.** It defines how a task should be performed so it can be repeated across sessions, teams, and workflows.

The distinction:
- **A prompt defines what to do once**
- **A Skill defines how to do it consistently**

Skills shape the work by:
- framing questions as decisions
- preparing concepts for testing
- defining what should be measured
- structuring how options are compared
- guiding how results are interpreted

They turn exploration into something the team can rely on.

---

## Agents Orchestrate

Agents coordinate how the work moves. **In Glare, Ray acts as the orchestrator.** It manages the overall goal, determines what needs to happen next, and applies the right Skills at the right time.

The relationship:
- **Agents** manage the goal and sequence of work
- **Skills** provide the repeatable steps to execute it

Example: an agent working toward evaluating a product direction might:
- apply a Skill to structure a test
- use another Skill to analyze responses
- compare outcomes across options

This allows the system to move from intent to execution without losing structure.

---

## Human in the Loop

Signals and decisions are grounded in people.

**Design signals are created from participant input using UX metrics.** They reflect how real users respond to concepts, flows, and experiences. This input gives the system something real to evaluate and compare.

**Decisions are made by teams.** Product, design, and engineering interpret those signals, weigh tradeoffs, and decide what moves forward. *In the future, agents will progressively be used to make decisions.* For now, they support.

Decisions define:
- what moves forward
- what gets refined
- what gets stopped

Signals make those tradeoffs visible so teams can commit with confidence.

The flow is direct:
- participants provide input
- signals make that input visible
- teams interpret what it means
- decisions determine what happens next

**AI supports the work. People determine direction.**

---

## How it comes together

When these parts connect, the workflow becomes repeatable. Work moves through a clear structure that turns exploration into action:

```
prompt    →  generates an idea or direction
Skill     →  shapes that idea into something testable
agent     →  coordinates the steps needed to evaluate it
participant input  →  creates a signal
team      →  uses that signal to decide what moves forward
```

Each step builds on the last. The output of one step becomes the input to the next. This loop can run within a single session or extend across a larger cycle. As it repeats, decisions become easier to make and easier to carry forward.

---

## What this produces

This workflow produces outputs that are immediately usable:
- signals tied to real user behavior
- consistent comparisons between options
- decisions teams can align around
- clear next steps that can be executed

These outputs do more than summarize the work. They:
- reduce uncertainty
- make tradeoffs visible
- give the team a shared reference point
- keep work moving with direction

---

## Where this works best vs. where it needs support

| Where the workflow works best | Where it needs support |
|---|---|
| Multiple directions need to be explored and compared | Access to participants or realistic user feedback |
| Decisions need to be made quickly without losing clarity | Clear metrics or criteria for evaluation |
| User input can be gathered to inform direction | Consistent use of Skills across the team |
| Teams need a shared way to evaluate options | (when missing, output continues but signals weaken) |

In ideal conditions, the workflow helps teams move forward without relying on opinion or fragmented feedback. When conditions are missing, the system still produces output, but the connection to decisions weakens — comparisons become less reliable, alignment becomes harder to maintain.

---

## Try This Now

Start with a single decision:

1. **Create a signal** from collecting user input
2. **Choose a prompt** to generate new insights
3. **Apply a Skill** to structure how you evaluate them
4. **Collect a small set** of user responses
5. **Decide what moves forward**

You don't need the full system to start. **One signal is enough.**

---

## Quick reference: prompt vs. Skill vs. agent

| | Prompt | Skill | Agent |
|---|---|---|---|
| **Defines** | What to do once | How to do something consistently | What goal to pursue and what sequence |
| **Reusability** | Single use | Reusable, versioned, shareable | Persistent across goal |
| **Best for** | Exploration, variation, reframing | Decision framing, evaluation, comparison, interpretation | Multi-step coordination across Skills |
| **Glare's example** | "Generate three layout variations of this dashboard" | User Needs Skill, Business Goals Skill, Comparing Skill | Ray |
| **Risk if missing** | Slow start | Inconsistent evaluation | Steps don't connect |
