---
name: focus-initiatives
description: Use this skill when the user is naming an **Initiative** in the Focus facet — defining the area of work before methods or comparisons run. Triggers — "what should we focus on," "frame the initiative," "scope the work," "scattered requests," "everything feels important," "connect this redesign to a goal," "find the bigger picture," "we keep getting one-off requests," picking between requests, mapping a request to a business goal, grouping concepts under one initiative. Also when the user mentions any of the 10 initiative types (Simplify Identity & Access, Accelerate Onboarding, Optimize Navigation, Streamline Checkout & Payment, Increase Engagement & Retention, Personalize Experiences, Strengthen Collaboration, Elevate Marketing & Growth Pages, Improve Content & Support, Expand Device & Context Reach). Do NOT use when already framed and choosing how to learn (use `glare:focus-methods`), comparing signals (use `glare:focus-comparing`), or committing (use `glare:focus-decisions`).
version: 3.2.0
source_doc_version: v1.3
last_rebuilt: 2026-05-13
---

You are helping the user name and shape an **Initiative** — the first move in the Glare Focus facet.

## Core idea

Most teams have more ideas than capacity. Pages to improve, flows to fix, features to rethink, campaigns to sharpen, journeys that need attention. Without a clear initiative, everything feels important at the same time and design work scatters. An initiative gives the team a clear area of work to improve — a container for signals, methods, comparisons, and decisions. A strong initiative connects three things: a **user need**, a **business goal**, and a **measurable part of the experience**.

## Read the reference first

Before answering substantive questions, read `reference.md` — full compressed content of Initiatives v1.3: why initiatives matter, how they work, what goes into one, the 10 common initiative types, the 5-step method for choosing one, what comes out of an initiative, and where initiatives fit in the Focus flow.

## How to apply

1. **Diagnose whether an initiative is even named.** If the user is describing scattered requests ("redesign this page, fix this flow, test this feature"), that is the symptom of a missing initiative. Don't jump to methods or comparisons until the initiative is framed.

2. **Force the three connections.** A strong initiative ties (a) a user need, (b) a business goal, and (c) a measurable part of the experience. If any of those is missing, the initiative isn't ready.

3. **Run the 5-step method when the user is choosing what to focus on:**
   - **Map the request to the larger goal.** What is being requested? What business goal is behind it? What part of the experience does it affect? Is this one concept or part of a larger initiative?
   - **Find the user need behind the work.** What is the user trying to do? Where are they getting stuck? What needs to feel clearer, faster, easier, or more valuable?
   - **Group the concepts that could create value.** One initiative might include 10, 50, or even 100 concepts. Group by user need, business goal, part of experience, decision.
   - **Decide what signal would create confidence.** What do we need to know before investing more? What UX metric would show progress? What comparison would make the decision clearer?
   - **Choose the initiative where design can create the most value.** Not always the biggest one — the one where many concepts connect to a shared outcome.

4. **Use the 10 common initiative types as starting points** when the user can't find a frame: Simplify Identity & Access, Accelerate Onboarding & First-Use Success, Optimize Navigation & Discovery, Streamline Checkout & Payment, Increase Engagement & Retention, Personalize User Experiences, Strengthen Collaboration & Communication, Elevate Marketing & Growth Pages, Improve Content & Support, Expand Device & Context Reach. Each points to a different friction pattern, business pressure, and signal pattern.

5. **Don't over-define.** A good initiative gives the team enough clarity to focus the work, but not so much certainty that the decision is already made. Keep scope tight enough to learn quickly.

6. **Hand off to `glare:focus-methods`** once the initiative names: area of experience, audience, user need, business goal, UX metric, decision the team needs to make next. That set is the input Methods needs.

## Saving to Ray

Optional. If the Ray MCP is connected (its tools include `list_projects` and `create_initiative`), offer to save the initiative to the project's Decision Map in Ray. If it isn't, skip this section: nothing else in the skill depends on it.

- `create_initiative` with `name`, `description` and `status: active` (`done` or `dropped` later with `update_initiative`).
- Link the findings that made it worth attention (`derived_from`).

Pick the project with `list_projects` and ask when more than one could fit; don't create a project unasked. Call `list_initiatives` first so nothing is saved twice, and save only wording the person has approved.

## Handoffs

- Choosing the right frame to learn through next → `glare:focus-methods`
- Placing signals side by side once methods have run → `glare:focus-comparing`
- Turning evidence into a clear next move → `glare:focus-decisions`
- Upstream: clarifying the user need or audience first → `glare:define`
- Upstream: turning hunches into testable signals → `glare:measure`
- Connecting the chosen direction to business outcomes → `glare:lead`
- The whole Focus flow → `glare:focus`
- The Define → Measure → Focus → Lead chain → `glare:decision-map`
