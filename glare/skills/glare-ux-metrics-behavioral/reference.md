# Behavioral Metrics — Reference (v1.32, per-metric pages added)

## When to use

- When the user is working with what users actually *do* — hesitation, abandonment, navigation breakdowns, click patterns, completion.
- When real behavior diverges from the path designed for users (scanning, hesitating, looping, skipping).
- When picking among the eight canonical behavioral metrics (Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability).
- When behavioral signals matter most — onboarding, navigation, AI-assisted workflows, search, dashboards, enterprise experiences.
- When the team needs to move beyond scoreboards toward what is actually changing user behavior.

**Don't use when** the user wants the broader framework (`glare-ux-metrics`), Attitudinal or Performance metrics specifically, or Define-stage picking on a specific decision (`glare-define-ux-metrics`).

## What behavioral metrics measure

Behavioral metrics measure what users actually do while interacting with a product, workflow, or system. They help teams understand:

- where users hesitate
- how people move through workflows
- where navigation breaks down
- where users abandon tasks
- what actions create momentum
- how people actually behave inside the experience

Product teams often assume users will follow the path that was designed for them. Real behavior often looks very different — users may repeatedly scan navigation, hesitate before clicking, skip important content, abandon onboarding halfway through, loop through the same screens multiple times, complete tasks slowly while feeling unsure.

Behavioral metrics catch what users are *actually* doing inside the workflow, not what teams hoped users would do. They often reveal friction, hesitation, and confusion that users may never directly describe themselves.

## The canonical eight behavioral metrics (v1.32)

This skill recommends ONLY from this canonical list of eight behavioral metrics. Do not invent or borrow behavioral metric names from other frameworks.

Completion · Comprehension · Effort · Engagement · Frequency · Intent · Success · Usability

Per-metric pages follow alphabetical order.

---

### Completion

**What it measures:** Whether users reach the end of a flow — both functional success and user follow-through. Combines Direct Success (ideal path) and Indirect Success (alternate path that still reached the end).

**When to use:** Linear, multi-step paths where finishing matters — onboarding, checkout, sign-up, application processes, multi-step workflows, task-specific features. Use Completion in prototype testing where you can observe whether each participant reached the end and whether they took the ideal path or wandered.

**How it's calculated / collected:** Prototype directive with a defined ideal path. Classify each participant as Direct Success (followed the ideal path), Indirect Success (took an alternate path but still finished), or Failed (didn't finish). `Completion Score = Direct Success Rate + Indirect Success Rate`.

**Example values:** Very Good >90%, Good 70–89%, Average 50–69%, Poor 30–49%, Very Poor <30%. Glare's Advent campaign-targeting example landed at 87% (Good) — 76% Direct, 11% Indirect, 13% failed.

**Common mistakes:**
- Counting only Direct Success and ignoring Indirect (masking alternate-path users who still finished).
- Using Completion as the only signal — a 90% completion can mask a Confusion Trap if Confidence is also low.
- Confusing Completion (whole flow, prototype-tested) with **Success** (single interaction) or with Performance **Completion Rate** (analytics-funnel percentage at scale).

**Related metrics / pairings:** Pairs with **Effort** (was it hard?), **Confidence**/**Satisfaction** (did they feel sure?), and Performance **Completion Rate** (does it hold at scale?). When Completion is high but Indirect is dominant, look for layout-hierarchy problems.

**Signal pattern:** "76% of users completed the targeting task directly, 11% via alternate path — overall Completion 87% (Good). The 13% who failed clustered on overlooking the 'Edit' button. Direction: increase visibility of the edit action and clarify step order, then re-test before pushing to production."

---

### Comprehension

**What it measures:** How well users understand the product — its purpose, how it works, and the value it offers. Includes both self-rated confidence and ability to explain what they've seen.

**When to use:** Anytime something is novel or complex — onboarding, walkthroughs, new feature introductions, copy and messaging tests, mental-model checks. Critical at first-impression moments where confusion compounds into drop-off.

**How it's calculated / collected:** 4-point Likert (Did not understand=1 → Understood very well=4) plus a free-response "explain it in your own words" question. `Comprehension Score = (Σ Likert ratings / number of responses) ÷ 4`. The free response is the diagnostic — check whether the words match the design's intent.

**Example values:** Same bands. Glare's Getup outfit-suggestion example landed at 91% (Very Good) — 62% "understood very well," 33% "understood most of it," 0% "did not understand," and open responses accurately summarized the tool.

**Common mistakes:**
- Using the self-rating alone without the free-response check — users say they understood while clearly missing the point.
- Placing the question too late, after users have inferred the answer from later screens.
- Treating "understood most" as good without examining the open responses for misconceptions.

**Related metrics / pairings:** Pairs with **Expectations** (what they assumed) and **Success** (could they act on it). High Comprehension + low Success = users understood but the UI blocked them. Low Comprehension + high Engagement = users clicking without knowing what they're doing — risky for AI features.

**Signal pattern:** "Comprehension on the new feature is 91% — 62% understood very well, and open responses accurately describe the tool as 'a smart wardrobe assistant based on event type.' Direction: skip the planned tutorial overlay; users grasp the concept without it. Move budget to polishing the closet-suggestion ambiguity."

---

### Effort

**What it measures:** How easy or difficult users find it to complete a task — Customer Effort Score (CES) on a 7-point scale capturing perceived friction.

**When to use:** Setup, checkout, navigation, support and self-service flows, post-launch performance checks — anywhere ease-of-use drives adoption or conversion. Especially useful for catching friction that doesn't show up in pure completion data.

**How it's calculated / collected:** 7-point Likert immediately after the task (Very Difficult=1 → Very Easy=7). `Effort Score = Σ (count × scale value) / number of responses ÷ 7`. Always pair with the task itself — Effort alone has no anchor.

**Example values:** Same bands. Glare's Getup e-commerce navigation example landed at 87% (Good) — 55% rated the task a 7, 25% a 6, only 6% scored it 3 or below.

**Common mistakes:**
- Asking Effort during the task instead of immediately after.
- Using high Effort as a proxy for failure when users may have completed successfully but resented the experience.
- Not pairing Effort with **Completion** — low effort + low completion is a different story than high effort + high completion.

**Related metrics / pairings:** Pairs with **Completion**, **Success**, and **Satisfaction**. The combination "high Satisfaction + high Effort = users grinding through" is a classic hidden-friction signal.

**Signal pattern:** "Navigation Effort is 87% — most users found finding a shirt easy, but 6% scored it 3 or below, clustered on the filtering experience. Direction: keep the category navigation; rework filter labeling for edge-case audiences and re-test."

---

### Engagement

**What it measures:** Whether users interact with the key calls to action on a page — captured via first-click on predefined hotspots covering the priority CTAs.

**When to use:** Layout, landing-page, and CTA decisions where the first interaction sets the tone — testing variants, comparing CTA placement, validating new features. Especially useful in concept testing where you want to know what draws attention first.

**How it's calculated / collected:** First-click test on a page with predefined hotspots. `Engagement Score = Σ (% who clicked in each hotspot) / number of responses`. Often reported as an overall score plus per-hotspot click rates.

**Example values:** Same bands. Glare's HelloFresh landing-page example landed at 56% (Average) — Hero Offer pulled 36%, Pricing Plans 20%, Footer Offer 0%.

**Common mistakes:**
- Mistaking activity for value — Engagement can rise on broken workflows users keep retrying.
- Using Engagement alone for AI features — high activity may hide low confidence in the output.
- Not pairing with **Comprehension** or trust signals (clicks without understanding aren't conversion).

**Related metrics / pairings:** Pairs with **Intent** (was the click the right next step?), **Success** (did they click in the right place?), and **Comprehension**. When Engagement is high but Intent is misaligned, the page is grabbing attention for the wrong actions.

**Signal pattern:** "Landing-page Engagement is 56% — Hero Offer drove 36% of first-clicks; Footer Offer pulled 0%. Direction: pull the footer offer earlier in the page hierarchy or kill it; the current placement isn't earning its space."

---

### Frequency

**What it measures:** How often users say they would return to engage with the product — habits, stickiness, ongoing relevance, captured as self-report.

**When to use:** Retention assessment, feature adoption, long-term usage patterns, subscription products, account management features, notification effectiveness. Use Frequency when you want a forward-looking signal *before* the analytics show actual return behavior.

**How it's calculated / collected:** 5-point Likert (Very Rarely=1 → Very Frequently=5), often phrased as "how often would you use this?" `Frequency Score = (Σ Likert ratings / number of responses) ÷ 5`. Pair with a "why this rate?" qualitative follow-up.

**Example values:** Same bands. Glare's Banko credit-score-check example landed at 51% (Average) — "Once per month" dominated at 43%, with weekly checks at 19%.

**Common mistakes:**
- Using self-reported Frequency as a substitute for actual analytics Visit Frequency — Frequency is intent, **Visit Frequency** is behavior.
- Conflating Frequency (self-reported, behavioral type) with Performance **Visit Frequency** (observed, performance type).
- Ignoring *why* users return — the qualitative follow-up usually carries the actionable signal.

**Related metrics / pairings:** Pairs with **Visit Frequency** (observed counterpart) and **Usefulness**. High Frequency + low Usefulness = habit usage masking churn risk. Pairs with **Recency** for retention storytelling.

**Signal pattern:** "Stated Frequency for the credit-check feature is 51% — users mostly check once a month, tied to monthly bill cycles. Direction: surface the tool inside monthly bill workflows; educate on weekly use cases (fraud catch, goal tracking) before expecting the cadence to rise."

---

### Intent

**What it measures:** Whether users plan to take a specific action — sign up, purchase, return — using a weighted multiple-choice formula on the next step they'd take.

**When to use:** Early concept testing, prototype validation, pre-launch studies, landing pages, pricing pages, CTA testing — anywhere behavior hasn't happened yet but interest can be probed. Intent is the forward-looking partner of Engagement.

**How it's calculated / collected:** Multiple-choice question listing primary, secondary, tertiary, and non-engagement actions. `Intent = (primary % × 3 + secondary % × 2 + tertiary % × 1) / 300%`. Weight rewards primary-action selection.

**Example values:** Same bands. Glare's Getup homepage example landed at 61% (Average) — 65% selected "Shop this look" (primary), 19% video, 11% calendar sync, 5% leave.

**Common mistakes:**
- Treating Intent as proof of behavior — it's a forward-looking signal, not actual conversion.
- Not weighting primary vs secondary actions; reporting raw percentages instead of the weighted score.
- Over-relying on Intent without an actual proxy or analytics follow-up after launch.

**Related metrics / pairings:** Pairs with **Engagement** (did they click) and **Desirability** (do they want it). When Desirability is high but Intent is split across non-primary actions, the design is dispersing attention.

**Signal pattern:** "Homepage Intent is 61% — 65% of users chose the primary 'Shop this look' CTA, but 30% scattered across secondary actions, dragging the weighted score. Direction: reduce visual emphasis on secondary actions; tighten the primary path."

---

### Success

**What it measures:** Whether users can complete a specific *interaction* — find a button, use a filter, reach the right page — usually via a click test on a defined hotspot.

**When to use:** Usability tests, A/B comparisons, audits of known problem areas, validating that key actions are findable. Success is the single-interaction sibling of Completion (which is whole-flow).

**How it's calculated / collected:** Click test with a single "correct" hotspot. `Success Rate = participants who clicked the right place / total participants`. Often paired with response-time data and a heatmap.

**Example values:** Same bands. Glare's Getup "Try On in Store" example landed at 84% (Good) with 10.38s average response time — moderate scannability.

**Common mistakes:**
- Confusing Success (single interaction) with **Completion** (whole flow) or **Usability** (multiple Successes averaged).
- Reporting only the click count without response time — slow successes are hesitations.
- Not investigating where the *unsuccessful* clicks landed — the wrong-place pattern is the actionable signal.

**Related metrics / pairings:** Pairs with **Usability** (averages Success across 3+ interactions), **Engagement** (does the right hotspot pull attention), **Comprehension** (did they understand what to click). Conflict warning: do not use Success alone to evaluate multi-step flows.

**Signal pattern:** "Success for finding 'Try On in Store' is 84% with 10.4s response time — users find it but slowly. Heatmap shows competing attention on 'Add to Cart.' Direction: increase visibility of the Try-On label or repositon it as a clear secondary action."

---

### Usability

**What it measures:** How well users complete a *full series* of tasks within a flow — averages multiple Success scores (minimum of 3).

**When to use:** Checkouts, onboarding sequences, multi-step forms, anywhere several interactions must work together. Usability is the right metric when you want a rolled-up read on a page or flow rather than a single interaction.

**How it's calculated / collected:** Run 3 or more click-based directives on the same design. Calculate Success for each. `Usability = average of Success scores (minimum 3 tasks)`.

**Example values:** Same bands. Glare's Getup product-details-page example landed at 89% (Good) — Action 1 92%, Action 2 90%, Action 3 (Add to Cart) 85% dragged the average.

**Common mistakes:**
- Averaging too few Success scores — the v1.32 source requires a minimum of 3.
- Reporting the aggregate when one task is dragging the average; always unbundle per-task.
- Confusing the *Usability metric* (this multi-task averaged score) with the broader *usability concept* (the whole field).

**Related metrics / pairings:** Built on **Success**. Pairs with **Completion** (whole-flow path) and **Effort** (how it felt). Conflict warning: a high Usability score on three minor actions can mask a low score on the one that actually matters — choose tasks that reflect the critical path.

**Signal pattern:** "Product-details Usability is 89% — strong on size and color (92%, 90%) but Add-to-Cart drags at 85%. Direction: increase contrast and clarity on the Add-to-Cart CTA; keep the size/color UI as-is."

---

## Behavioral metrics help teams find real growth levers

Behavioral metrics help teams move beyond simple scoreboards and better understand what is actually changing user behavior. For example:

- stronger clarity may improve onboarding completion
- reduced effort may improve engagement
- clearer navigation may improve discoverability
- fewer workflow steps may reduce abandonment

The behavior helps explain which parts of the experience are actually helping users move forward.

Over time, teams can build behavioral patterns across:

- onboarding
- navigation
- AI-assisted workflows
- search systems
- dashboards
- enterprise experiences

These patterns help teams compare workflows, benchmark improvements, and identify where friction keeps repeating.

---

## How behavioral metrics work together

Different behavioral metrics reveal different problems and often work together to expose larger workflow patterns:

- **high completion + repeated hesitation** → confusion
- **strong engagement + low discoverability** → navigation friction
- **successful onboarding + weak comprehension** → hidden usability problem

The behavioral signals begin explaining how the workflow actually behaves underneath the surface. Over time, these patterns help teams identify confusion traps, friction walls, navigation breakdowns, weak onboarding experiences, AI workflow hesitation, and feature-discoverability problems.

---

## Combining behavioral with other metrics

Behavioral metrics become much more valuable when paired with attitudinal and performance metrics:

- **high engagement + low trust** → hesitation
- **strong completion + rising frustration** → workflow fatigue
- **repeated navigation loops + weak confidence** → confusion

The combined signals help teams understand both *what* users are doing and *how* the experience feels while they are doing it. Over time, these connected patterns help teams compare workflows, improve onboarding, strengthen usability, and guide product decisions with stronger evidence.

---

## Helio path

Helio collects behavioral metrics as **leading indicators** before analyzing post-launch performance. Use Helio to capture Completion, Comprehension, Success, Effort, and Usability during prototype and concept testing — these scores serve as both predictive signals and proxy metrics, validating the workflow in a controlled environment before launch.

## Source

Drafted from *Glare | UX Metrics, Behavioral Metrics v1.32* (Drive doc `116rGaIqNYzu5Qerx3iSvh1rHPg_wtb3gjlMwti3GEBw`, May 10, 2026 — internal banner reads v1.3, treated as cosmetic), plus per-metric subfolder docs (`1ONtVbgAl8GSwSQniin6IvJhOLdrPTH1x`):

- Completion (`1t3Y3iMbKB2tuLLxgk6oxQbAKD8pu59axaduuy04_Ars`)
- Comprehension (`1R3AISlxmDqpx_IY16yX9fFk-CHx65C7i3JDvudPoRbw`)
- Effort (`1eANnM5jZHYHCWFDR9co6yg4698rUy8fkBm33LypFuKc`)
- Engagement (`1gadgpKoxJ_vrcue61kCTlBLV7RRoQfEIP6QoGWg5EN0`)
- Frequency (`1AzBdRW7wVtm0H6AzAlCk4Fqh4gVHXwBg-ACQinX1sSk`)
- Intent (`1mLCGElVJH_TYTxBKeLufe1EGk15jvyzcA6biY7gJ_p8`)
- Success (`15xWiC-_d_on6izXwYpYvlXgbTEJEM-E1U25i_eZtzX8`)
- Usability (`1yaxxUayhTH9mcKiwY17W_vDMhWY7e61n8wK8LzYgCYA`)

## Failure modes

These are common ways this skill goes wrong in practice:

- **Inventing behavioral metrics.** Borrowing "stickiness," "viral coefficient," or other engagement names that aren't in the canonical eight. Stick to Completion, Comprehension, Effort, Engagement, Frequency, Intent, Success, Usability — or route to another type.
- **Behavioral-only stacks.** Tracking only what users do without checking how they feel (attitudinal) or how efficiently the system works (performance). Behavioral alone shows the path without the cost or the trust.
- **Measuring behavior on the wrong workflow.** High engagement on a sub-workflow doesn't mean the primary task succeeded. Anchor behavioral metrics to the workflow tied to the decision, not the surface that's easiest to instrument.
- **Confusing high engagement with good behavior.** Users repeatedly scanning the nav can look like engagement; it's actually friction. Pair engagement with effort or hesitation to read what the behavior means.

