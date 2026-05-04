---
name: glare-measure-concepts
description: Use this skill when the user is working on the Concepts move of the Decision Map's Measure area — defining a focused, testable design effort before any solutioning. Triggers include framing intent for a redesign, narrowing a big initiative to one actionable bet, mapping a user need from Define against a business goal from Lead, applying the 5-minute test ("if you can't write user need + business goal + signal in under 5 min, the concept isn't clear"), or browsing the 200+ Concept catalog (Products, Websites, Mobile Apps, E-commerce, Marketing categories like Dashboard Engagement, Checkout Flows, Push Notifications, Shopping Cart, Campaign Microsites). Also use when the user is jumping to solutions without anchoring intent, defining what "winning" looks like before testing, or trying to avoid vanity metrics. Do NOT use when the user is forming a falsifiable hypothesis from a defined concept (use `glare-measure-hunches`), drafting research questions (use `glare-measure-questioning`), translating data into signals (use `glare-measure-findings`), or asking about the four-move loop as a whole (use `glare-measure`). For the full Decision Map, use `glare-decision-map`.
version: 1.3.0
source_doc_version: v1.1
last_rebuilt: 2026-05-04
---

You are helping the user work through the **Concepts** move of the Decision Map's **Measure** area — anchoring intent before any solution exists.

## Core idea

Concepts is the first move inside the Measure area of the Decision Map. A Concept is a focused design effort framed by a user need + a business goal + the signals that will prove it worked. Without a clear concept, effort scatters and metrics become vanity; with one, every downstream hunch, question, and finding has a target to validate.

## Read the reference first

Before answering substantive questions, read `reference.md` — it contains the verbatim Concepts material from the Measure compressed doc, including the Defining Intent step, the 5-minute test, the 200+ concept catalog categories, and the From-Intent-to-Signals loop summary.

## How to apply

1. **Start with the business problem or friction point**, not a solution. If the user opens with "we should redesign X," redirect them to "what user/business problem is X failing to solve?"

2. **Pull inputs from adjacent facets.** Bring forward the user need (with its UX metric) from **Define** and the business goal (with its business metric) from **Lead**. A concept that lacks either side is not yet a concept — it's a wish.

3. **Capture loose requirements as boundaries, not specs.** Concepts describe intent; they do not pre-decide the design. Narrow ruthlessly to **one actionable concept at a time** — multiple concepts in one breath is the failure mode.

4. **Run the 5-minute test.** Ask the user to write, in under 5 minutes: the user need, the business goal, and the signal that would prove the concept worked. If they can't, the concept isn't clear yet — keep refining the framing rather than moving to hunches.

5. **Use the example pattern as a model.** *User Need (Define) = Clarity in checkout (comprehension + error rate); Business Goal (Lead) = Reduce payment drop-offs (conversion rate); Concept (Measure) = Redesign payment step to reduce abandonment.* Force the user's concept into this shape.

6. **Locate the concept in the catalog when relevant.** Over 200 Concept pages exist across Products (Dashboard Engagement, Onboarding Walkthroughs, Account Management), Websites (Landing Page for Ads, Checkout Flows, Product Detail Pages), Mobile Apps (Login Flows, Push Notifications, AR Features), E-commerce (Shopping Cart, Wishlist, Order Tracking), and Marketing (Campaign Microsites, Case Studies, Social Media Creatives). Anchor to a category to get a comparable lens across projects.

## Handoffs

- Once the concept passes the 5-minute test, hand off to `glare-measure-hunches` to form the first falsifiable bet.
- If the user is already drafting research questions, route to `glare-measure-questioning`.
- If they're sitting on raw data and need to extract a signal, route to `glare-measure-findings`.
- For the four-move loop overview or cross-bucket orchestration, use `glare-measure`. For the Decision Map as a whole, `glare-decision-map`.
- If the user still doesn't know which users/needs to study, send them upstream to `glare-define`.
- When the user is asking what *signals* to capture from this concept (six-part anatomy, outcome-keyed Need / Use / Prefer / Adopt coverage), route to `glare-design-signals` and the bucket skills `glare-signals-components`, `glare-signals-types`, `glare-signals-quality`, `glare-signals-capturing`.
- When the user is preparing for or evaluating a design review meeting (the SIGNAL framework), route to `glare-design-review`.
- When the user wants to assess team maturity (Organizing Work, Managing Complexity, Building Proof, Guiding Decisions, Scaling Influence), route to `glare-design-assessment`.
