---
name: glare-signals-types
description: Use this skill when the user asks about the **kinds** of Design Signals — "what are the four signal types," "Need Use Prefer Adopt," "what types of signals should we collect," "are we covering the full experience," "we only have one kind of signal," "how do I know which signal type is missing." Triggers also include questions about whether a direction holds up across the experience, signal coverage gaps, balancing credibility / usefulness / desirability / behavior, or mapping a particular question to the right signal type. Do NOT use for the six structural parts of a single signal (`glare-signals-components`), evaluating a single signal's trustworthiness (`glare-signals-quality`), or the capture workflow (`glare-signals-capturing`).
version: 1.3.0
source_doc_version: v1.3
last_rebuilt: 2026-05-04
---

You are helping the user **organize signals across the four Signal Types** so a decision is grounded in the full experience, not one moment.

## Core idea

Signals don't exist in isolation. Looking at one signal in one moment can be misleading — something may perform well in one area and fail in another. The four Signal Types are a **coverage check**, not steps. They show how an idea connects to users, how it works in practice, and whether it holds up over time.

The four types: **Need** (does this connect to a real user need), **Use** (does this make sense to users), **Prefer** (do users want this direction), **Adopt** (does this work in real behavior).

## Read the reference first

- `reference.md` — full content for each of the four types (definition, what to look for, what breaks), how to use signal types as coverage rather than sequence, and what the framing unlocks vs. where it breaks.

## How to apply

1. **Treat the four types as a coverage map.** Ask the user which types they currently have signals for and which are blank. The blank columns are usually where the next test should go. The doc is explicit: "Signal types are not steps. They are a way to check coverage."

2. **Match the user's question to the right type:**
   - "Are we solving the right problem?" → **Need**
   - "Does the experience make sense?" → **Use**
   - "Do users actually want this?" → **Prefer**
   - "Does it work in practice / over time?" → **Adopt**

3. **Use "what breaks" to diagnose.** When the user describes a failure mode, map it to the type whose break-pattern matches:
   - solving the wrong problem / users don't see the value → missing **Need** signal
   - users hesitate, get stuck, steps unclear → missing **Use** signal
   - users uncertain, no clear preference, lacks appeal → missing **Prefer** signal
   - drop-off, low follow-through, no behavior change → missing **Adopt** signal

4. **Push for all four when stakes are high.** When all four types are covered: gaps become easier to spot, tradeoffs become clearer, decisions feel more grounded, weak ideas surface earlier. When they aren't: teams rely on one metric, decisions are based on partial input, issues show up later, work needs to be revisited.

5. **Quick-use prompt for any direction:** does this connect to a real need → does it make sense to users → do users actually prefer it → does it hold up in behavior. If one is weak, that's where to focus next.

## Handoffs

- Top-level concept of Design Signals → `glare-design-signals`
- Building each individual signal's six parts → `glare-signals-components`
- Checking whether a specific signal is trustworthy → `glare-signals-quality`
- The end-to-end capture workflow that produces signals → `glare-signals-capturing`
- Need-type signals link tightly to the UX Honeycomb (Credible, Valuable, Desirable layers) → `glare-define-user-needs`
- Use-type and Adopt-type signals usually need behavioral / performance metrics → `glare-define-ux-metrics`
- Comparing how different directions perform across the four types → `glare-focus-comparing`
