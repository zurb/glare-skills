# Behavioral Metrics — Reference (v1.32)

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

---

## The eight behavioral metrics (v1.32)

| Metric | Definition | When to use | Common mistakes |
|---|---|---|---|
| **Completion** | Whether users reach the end of a flow — both functional success and user follow-through. Combines Direct Success (ideal path) and Indirect Success (alternate path that still reached the end). | Onboarding, checkout, sign-up, multi-step workflows, task-specific features, any linear path where finishing matters. | Counting only Direct Success and ignoring Indirect (which would mask alternate-path users); using Completion as the only signal (a 90% completion can mask Confusion Trap if Confidence is also low); confusing it with Success (single interaction) or Completion Rate (analytics-funnel percentage). |
| **Comprehension** | How well users understand the product — purpose, how it works, value offered. Includes confidence and ability to explain what they've seen. | Onboarding, walkthroughs, new feature introductions, copy and messaging tests, anything novel or complex where mental model matters. | Using a self-rating alone without a free-response check (users say they understood while clearly missing the point); placing the question too late, after users have inferred the answer; treating "understood most" as good without examining the open responses. |
| **Effort** | How easy or difficult users find it to complete a task — using the Customer Effort Score (CES) on a 7-point scale. | Setup, checkout, navigation, support and self-service flows, post-launch performance checks, anywhere ease-of-use drives adoption. | Asking Effort during the task instead of immediately after; using high Effort as a proxy for failure when users may have completed successfully but resented it; not pairing Effort with Completion (low effort + low completion is a different story than high effort + high completion). |
| **Engagement** | How often and how long users interact with the product — interest and involvement. | Long-term value evaluation, feature adoption tracking, content engagement, dashboard health, retention questions. | Mistaking activity for value (engagement can rise on broken workflows users keep retrying); using Engagement alone for AI features (high activity may hide low confidence); not pairing with Trust or Comprehension. |
| **Frequency** | How often users return to engage with the product — habits, stickiness, ongoing relevance. | Retention assessment, feature adoption, long-term usage patterns, subscription products, account management features, notifications and alerts. | Using a self-reported frequency as a substitute for actual analytics frequency; conflating Frequency with Visit Frequency (Frequency is self-reported intent; Visit Frequency is observed behavior); ignoring why users return (qualitative follow-up matters). |
| **Intent** | Whether users plan to take a specific action — sign up, purchase, return — using a weighted multiple-choice formula on next-step preference. | Early concept testing, prototype validation, pre-launch studies, landing pages, pricing pages, CTA testing where behavior hasn't happened yet. | Treating Intent as proof of behavior (intent is forward-looking signal, not actual conversion); not weighting primary vs secondary actions; over-relying on Intent without an actual proxy or analytics follow-up. |
| **Success** | Whether users can complete a specific *interaction* — find a button, use a filter, reach the right page — usually via click test on a defined hotspot. | Usability tests, A/B comparisons, auditing known problem areas, validating that key actions are findable. | Confusing Success (single interaction) with Completion (whole flow) or Usability (multiple interactions averaged); reporting only the click count without response time (slow successes are hesitations); not investigating where the *unsuccessful* clicks landed (the wrong-place pattern is the signal). |
| **Usability** | How well users complete a *full series* of tasks within a flow — averages multiple Success scores (minimum of 3). | Checkouts, onboarding sequences, multi-step forms, anywhere several interactions must work together. | Averaging too few Success scores (the v1.32 source requires a minimum of 3); reporting an aggregate when one task is dragging the average down (unbundle the per-task scores); confusing it with the broader Usability *concept* — this is a specific multi-task averaged score. |

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
