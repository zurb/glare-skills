---
name: glare-ai-workflows
description: Use this skill when the user is asking about how Glare works alongside AI tools — phrases like "use Glare with ChatGPT," "how do I use AI with Glare," "what's the difference between a prompt and a Skill," "what is Ray," "how do AI agents fit into Glare," "we're moving fast with AI but losing alignment," or "how do I keep AI output trustworthy." Also use when the user wants the five-role AI workflow (prompts generate → Skills shape → agents coordinate → participant input creates signals → teams decide), or when they're confused about where humans stay in the loop. Do NOT use when the user wants the conceptual tour of Glare itself (use `glare-how-glare-works`) or when they're trying to make a specific decision right now (use `glare-create-first-signal`).
---

You are helping the user understand and apply **Glare's AI workflows** — the structure that turns AI-generated output into trustworthy decisions.

## Core idea

AI made it easy to generate output. Teams can now create more than they can confidently evaluate. Glare organizes AI-driven work into five connected roles: **prompts generate** possibilities, **Skills shape** how possibilities are evaluated, **agents coordinate** the process (Ray is Glare's orchestrator), **participant input creates** design signals, and **teams make** decisions. AI supports the work; people determine direction.

## Read the reference first

Before answering, read `reference.md` — the full role-by-role breakdown (prompts vs. Skills vs. agents vs. participant input vs. teams), the prompt/Skill distinction, what Ray does as orchestrator, the workflow loop, where the workflow works best vs. needs support, and the "try this now" five-step starter.

## How to apply

1. **Anchor on the prompt vs. Skill distinction first.** This is the most-misunderstood part:
   - **A prompt defines what to do once.** Fast, flexible, temporary — good for exploring ideas, generating variations, reframing questions, surfacing assumptions.
   - **A Skill defines how to do something consistently.** Reusable, versioned, shared — good for framing decisions, preparing concepts for testing, defining what to measure, structuring comparisons, guiding interpretation.
   - Prompts create momentum. Skills create consistency. Both are needed.

2. **Walk through the five roles in order**:
   - **Prompts generate** — possibilities, variations, reframing
   - **Skills shape** — turn output into something the team can evaluate the same way every time
   - **Agents coordinate** — manage the goal, sequence the steps, apply the right Skill at the right moment (Glare's agent is **Ray**)
   - **Participant input creates signals** — real users responding to UX metrics; this is what gives the system something real to compare against
   - **Teams make decisions** — interpret signals, weigh tradeoffs, decide what moves forward

3. **Reinforce the human-in-the-loop principle.** Signals come from real participants. Decisions are made by teams. AI supports the work; people determine direction. (The doc notes that agents will progressively be used to make decisions — but that future is gradual, not now.)

4. **When the user asks about Ray specifically**, explain it as the orchestrator: an agent that manages the overall goal, decides what needs to happen next, and applies the right Skills at the right time. Ray doesn't replace teams — it sequences the work so Skills get used consistently.

5. **Use the "Try This Now" starter** when the user wants to actually do something:
   - create a signal from collecting user input
   - choose a prompt to generate new insights
   - apply a Skill to structure how you evaluate them
   - collect a small set of user responses
   - decide what moves forward
   *You don't need the full system to start. One signal is enough.*

6. **Flag where the workflow works best vs. needs support** (multiple directions to compare + need for speed without losing clarity = ideal; missing access to participants or shared metrics = the workflow weakens).

## Handoffs

- Want to actually create your first signal → `glare-create-first-signal`
- Want the full system tour (four components) → `glare-how-glare-works`
- Confused about a term (prompt, Skill, agent, signal) → `glare-glossary`
- Leading a team adopting Glare + AI → `glare-coaching-advising`
- Need to gather participant input → `glare-define-collecting`
- Need to interpret signal results → `glare-measure-findings`
- Need to compare options against a signal → `glare-focus-comparing`
