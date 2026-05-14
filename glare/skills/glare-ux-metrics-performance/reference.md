# Performance Metrics — Reference (v1.32, per-metric pages added)

## When to use

- When the user is working with how efficiently a workflow actually functions — time, errors, abandonment, reliability.
- When workflows technically work but users finish slowly, struggle the whole time, or repeat errors.
- When picking among the eleven canonical performance metrics (Abandonment Rate, Bounce Rate, Click-Through Rate, Completion Rate, Drop-off Rate, Error Frequency, Error Rate, Recency, Session Duration, Time on Task, Visit Frequency).
- When measuring the *cost* of friction that other metric types miss.
- When pairing performance signals with attitudinal and behavioral metrics in a full stack.

**Don't use when** the user wants the broader framework (`glare-ux-metrics`), Attitudinal or Behavioral metrics specifically, or Define-stage picking (`glare-define-ux-metrics`).

## What performance metrics measure

Performance metrics measure how efficiently a workflow, system, or experience actually functions. They help teams understand:

- how long tasks take
- where users drop off
- where errors increase
- how much effort workflows require
- whether systems perform reliably under real usage

Product teams often focus heavily on whether users completed a task. But completion alone rarely explains how difficult the experience actually was. Users may finish onboarding while struggling the entire time, complete checkout after repeated errors, use AI recommendations while constantly double-checking results, or finish tasks successfully while moving much slower than expected.

Performance metrics help teams understand the operational health of the experience underneath the workflow itself.

## The canonical eleven performance metrics (v1.32)

This skill recommends ONLY from this canonical list of eleven performance metrics. Do not invent or borrow performance metric names from other frameworks.

Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency

Per-metric pages follow alphabetical order.

---

### Abandonment Rate

**What it measures:** The percentage of users who start a task or process but do not finish it — checkout, form submission, multi-step application, onboarding flow.

**When to use:** Anywhere users start something they may not finish — checkout flows, application processes, onboarding, multi-step forms, free trials. Abandonment Rate is the right metric when you want to know *whether* users finished, separately from *where* they dropped off (use **Drop-off Rate** for the per-step pattern).

**How it's calculated / collected:** Funnel analytics tracking entry into the flow and completion at the end. `Abandonment Rate = (Started − Completed) / Started × 100`. Equivalent to `100% − Completion Rate`. Most product analytics platforms calculate this directly via funnel reports.

**Example values:** Lower is better. Industry benchmarks for e-commerce checkout sit around 60–70% Abandonment Rate (industry-wide); a well-designed checkout flow targets <40%; >80% is a serious problem. Onboarding typically targets <50%.

**Common mistakes:**
- Confusing Abandonment Rate (started-then-stopped) with **Drop-off Rate** (left at a specific step) or **Bounce Rate** (left after only one page with no interaction).
- Reporting an aggregate Abandonment Rate instead of segmenting by step — the abandonment cluster is the actionable signal.
- Celebrating low abandonment when users who *did* finish are also reporting low confidence or high effort (completed-but-frustrated).

**Related metrics / pairings:** Inverse of **Completion Rate**. Pairs with **Drop-off Rate** to localize the problem and with **Time on Task** / **Effort** to explain it. When Abandonment is rising and Time on Task is also rising, investigate the longest-step first.

**Signal pattern:** "Checkout Abandonment is 54%, well above our 40% target. Drop-off concentrates between shipping and payment (32-point drop), and qualitative feedback shows hesitation around return policy clarity. Direction: surface return policy and security badges before payment entry; re-test."

> *Source-doc note: Abandonment Rate is referenced in the v1.32 Performance Overview as a canonical performance metric but does not have a dedicated subfolder doc. The page above is synthesized from the Overview content plus the inverse-of-Completion-Rate convention.*

---

### Bounce Rate

**What it measures:** The percentage of users who leave after viewing just one page without taking any further action.

**When to use:** Landing pages, entry points, any content meant to drive further exploration — hero CTAs, campaign-effectiveness checks, content evaluation, feature-page testing. Bounce Rate is closer to a *relevance* metric than a usability metric.

**How it's calculated / collected:** Web analytics (GA4, Mixpanel, etc.) automatically counts bounces as single-page sessions with no follow-up event. `Bounce Rate = Single-Page Sessions / Total Sessions × 100`.

**Example values:** Lower is better. Glare's Banko landing page example landed at 28% (Good). Industry varies wildly: marketing landing pages often target <40%; content sites can run 40–60%; entry points to deep flows aim for <30%.

**Common mistakes:**
- Treating low Bounce as automatically good — the page may be working but the wrong audience is arriving.
- Ignoring source/intent — a bounce on an unrelated query is different from a bounce on a target query.
- Using Bounce as a usability metric — it's closer to a relevance metric. Pair with **Time on Task** or **Click-Through Rate** for usability reads.

**Related metrics / pairings:** Pairs with **Click-Through Rate** (do users act?), **Session Duration** (do they stay?), and **Engagement** (which CTA pulls them?). When Bounce is high but Engagement on a few CTAs is also high, the page polarises — some users find what they need, others bail.

**Signal pattern:** "Landing-page Bounce Rate is 28% (Good). The 28% who bounce skew toward existing customers who misclicked or undecided visitors. Direction: keep the modular CTA structure; explore lighter-weight personalization based on referrer to push bounce below 20%."

---

### Click-Through Rate (CTR)

**What it measures:** The percentage of users who click a link, button, or CTA after seeing it.

**When to use:** Navigation, buttons, marketing copy, A/B tests, email campaigns, hero CTAs, feature-announcement evaluation. CTR is the workhorse metric for "did the design earn the click."

**How it's calculated / collected:** Event-tracked impressions and clicks via analytics or tag manager. `CTR = Clicks / Impressions × 100`.

**Example values:** Wildly context-dependent. Glare's Banko hero CTA example landed at 4% (Good for that placement). Email CTAs commonly target 2–5%; primary product-page CTAs target 10–25%; search-result CTRs are scored on a curve.

**Common mistakes:**
- Conflating CTR with intent — a click is not an intent confirmation; the user may have clicked then bounced.
- Reporting CTR without the impressions denominator (a raw click count is not a rate).
- Not pairing with a downstream **Completion Rate** or **Conversion Rate** to see if the click led anywhere useful.

**Related metrics / pairings:** Pairs with **Bounce Rate** (clicked but left), **Completion Rate** (clicked and finished), and **Engagement** (which CTA wins first-click). Always report CTR alongside what happens *after* the click.

**Signal pattern:** "Hero CTA CTR is 4% — within Good range, but heatmap shows users are bypassing the hero entirely for the lower-row offers. Direction: reduce visual emphasis on the hero or rewrite it to better match where attention is actually landing."

---

### Completion Rate

**What it measures:** The percentage of users who fully complete a defined process — checkout, sign-up, form submission. Funnel-level analytics percentage at scale.

**When to use:** Onboarding flows, form submissions, checkout process, any defined start-to-finish journey at scale where you have analytics tracking entry and exit. Completion Rate is the production-analytics version of behavioral **Completion**.

**How it's calculated / collected:** Funnel tracking in analytics — count users who entered the flow and users who reached the end. `Completion Rate = Total Task Completions / Total Task Starts × 100`.

**Example values:** Same scoring bands. Glare's Getup checkout example landed at 64% (rated Very Good in their context — checkout completion benchmarks are notoriously low). Onboarding targets 60–80%; form submissions on lead-gen often run 30–50%.

**Common mistakes:**
- Confusing Completion Rate (analytics percentage of started-vs-finished) with behavioral **Completion** (whether a single tested user reached the end via direct or indirect path in a prototype).
- Not segmenting by step — the drop is more useful than the average.
- Using Completion Rate alone as the launch signal without pairing it with **Drop-off Rate** or **Time on Task** for *why*.

**Related metrics / pairings:** Inverse of **Abandonment Rate**. Pairs with **Drop-off Rate** (where), **Time on Task** (how long), and **Error Rate** (did errors block them). Behavioral **Completion** is the prototype-stage cousin.

**Signal pattern:** "Checkout Completion Rate is 64% (Good in context). Drop-off concentrates at payment input (~22% loss). Direction: experiment with inline validation and one-click payment to lift the payment step; expect 4–6 points of Completion Rate improvement."

---

### Drop-off Rate

**What it measures:** The percentage of users who exit at a *specific* step within a flow.

**When to use:** Multi-step processes — onboarding, checkout, setup wizards, form submissions. Use Drop-off Rate when you need to localize *where* users are abandoning, not just whether (use **Abandonment Rate** or **Completion Rate** for that).

**How it's calculated / collected:** Per-step funnel tracking. `Drop-off Rate (Step i) = Users who exit at Step i / Users who entered Step i × 100`. Most analytics tools render this as a funnel visualization with per-step drops.

**Example values:** Per-step thresholds vary by flow complexity. Glare's Getup checkout example landed at 54% drop-off after shipping (Poor). A healthy multi-step flow keeps per-step drop-off below 15–20%; >40% at any step is a serious problem.

**Common mistakes:**
- Reporting an aggregate drop-off across the whole flow — the per-step pattern is the signal.
- Treating high drop-off as a design problem when it may be an audience-fit problem (users not in target segment).
- Not investigating *why* users dropped off — qualitative follow-up or session replay matters.

**Related metrics / pairings:** Pairs with **Completion Rate** (whole-flow), **Abandonment Rate** (whole-flow inverse), **Error Rate** (per-step), and **Effort** / **Comprehension** for the *why*. Drop-off is the localizer; the others explain.

**Signal pattern:** "Checkout Drop-off concentrates after shipping (54% drop entering payment), with feedback flagging confusion over the 'Ship to Store' toggle and security concerns. Direction: simplify the toggle; add return-policy and security signals immediately before payment entry."

---

### Error Frequency

**What it measures:** The average number of errors per session — how often users encounter errors during a typical session.

**When to use:** High-importance flows (login, checkout, data entry); live monitoring; spike detection; usability tests on stable prototypes where you can count distinct error events.

**How it's calculated / collected:** Error event tracking via product analytics, error monitoring (Sentry, etc.), or session replay. `Error Frequency = Total Number of Errors / Total Number of User Interactions (or sessions)`.

**Example values:** Lower is better. Glare's Advent audience-targeting example landed at 2.28 errors per session (rated Poor). A healthy critical workflow targets <0.5 errors per session; >2 signals systemic confusion or breakage.

**Common mistakes:**
- Confusing Error Frequency (errors *per session*) with **Error Rate** (percentage of *users* who hit an error). They tell different stories.
- Treating all errors as equal — a recoverable typo correction is very different from a hard system failure.
- Not categorizing errors by type (validation vs system vs user-input) — the breakdown is where the action is.

**Related metrics / pairings:** Pairs with **Error Rate** (same data, different denominator). Pairs with **Time on Task** (errors usually inflate it), **Completion Rate** (do users still finish?), and **Effort** (do they perceive the friction).

**Signal pattern:** "Audience targeting has Error Frequency of 2.28 — most errors cluster on dropdown misclicks and segment selection. Direction: redesign segmented controls and improve dropdown labeling; expect Error Frequency to drop below 1.0 after fix."

---

### Error Rate

**What it measures:** The percentage of users who encounter at least one error while performing a task or session.

**When to use:** Stability checks for critical workflows; identifying friction points; reliability evaluation; pre-launch QA verification. Error Rate is the right read when you want to know *how widespread* errors are; **Error Frequency** tells you *how heavy* the error load is on those affected.

**How it's calculated / collected:** Session-level error event tracking. `Error Rate = Sessions with at least one error / Total Sessions × 100`. Some implementations measure at the user level instead of the session level.

**Example values:** Lower is better. Glare's Getup checkout example landed at 8% (Very Good) — most users navigated cleanly with mistakes clustered on a single toggle. Critical workflows target <5%; >15% indicates user-facing instability.

**Common mistakes:**
- Reporting Error Rate without **Error Frequency** — you may have a small percentage of users hitting many errors each.
- Not investigating recovery — did users recover from the error, or did they abandon?
- Using Error Rate alone for AI-recommendation quality — some "errors" are really comprehension breakdowns or trust failures, not system errors.

**Related metrics / pairings:** Pairs with **Error Frequency** (depth) and **Abandonment Rate** (did errors push users out). When Error Rate is low but Abandonment Rate is high, errors aren't the story — friction or motivation is.

**Signal pattern:** "Checkout Error Rate is 8% (Very Good). The errors cluster on the 'Ship to Store' toggle confusion; everything else is clean. Direction: redesign the toggle; otherwise, current checkout flow is stable."

---

### Recency

**What it measures:** The time since a user's last visit — the freshness of engagement with the platform or product.

**When to use:** Retention analysis, re-engagement campaigns, churn-risk scoring, segment comparisons over time. Recency is the "how long since last seen" half of the Recency-Frequency-Monetary (RFM) framework.

**How it's calculated / collected:** Per-user timestamp of last interaction. `Recency = Current Date − Last Interaction Date` (in days). Often reported as the average across a cohort or as a percentage of users active within a recent window.

**Example values:** Context-dependent. Glare's Banko mobile-banking example landed at 44% (Average) — many users active within the past week, fewer daily. Daily-utility products target high recency (most users within 1–7 days); episodic products tolerate longer windows.

**Common mistakes:**
- Confusing Recency with **Frequency** / **Visit Frequency** — Recency is "how long since last," Frequency is "how often."
- Treating high Recency (long time since last visit) as automatically bad — some products have legitimate long-tail visit patterns (annual taxes, seasonal tools).
- Not pairing with a re-engagement signal (notification CTR, returning-user rate) to know whether interventions are working.

**Related metrics / pairings:** Pairs with **Visit Frequency** (cadence) and **Loyalty** (would they come back). RFM analysis combines Recency + Frequency + monetary value for segmentation.

**Signal pattern:** "Mobile-banking Recency is 44% within last 7 days — solid but not daily. Most users return for balance checks and bill pay. Direction: introduce light alert flows (low balance, bill due) to convert weekly users to daily; track whether Recency lifts to >60% within 60 days."

---

### Session Duration

**What it measures:** The average time users spend during a single visit — a depth-of-engagement signal.

**When to use:** Content engagement, dashboard health, longer-form experiences, comparing engagement across versions. Session Duration is more of an engagement metric than a usability metric — interpret with intent in mind.

**How it's calculated / collected:** Analytics-tracked timestamps from first to last interaction. `Session Duration = End Time − Start Time` averaged across sessions.

**Example values:** Wildly context-dependent. Glare's Getup homepage example landed at 54.3 seconds (Average for an e-commerce homepage). Content sites target several minutes; dashboards may target shorter sessions (efficient use). Longer is not always better.

**Common mistakes:**
- Treating long Session Duration as automatically good — it can mean engagement OR confusion.
- Not pairing with task completion — long session + low completion is a Friction Wall.
- Using Session Duration as a usability metric — it's closer to engagement; use **Time on Task** for usability reads.

**Related metrics / pairings:** Pairs with **Time on Task** (the targeted version), **Bounce Rate** (the inverse), **Completion Rate** (did long sessions land), and **Frequency**. Conflict warning: do not optimize Session Duration alone — it can rise on broken UX.

**Signal pattern:** "Homepage Session Duration is 54.3 seconds — users browse but don't go deep. Few engage past the first scroll. Direction: introduce interactive elements (outfit configurator, reviews) above the fold; target 90+ seconds with a corresponding lift in product-page CTR."

---

### Time on Task

**What it measures:** The average time users spend completing a *specific* task — efficiency and ease of task completion.

**When to use:** Specific tasks within a workflow (checkout, form submission, search), A/B comparisons, identifying friction within onboarding or checkout, post-launch performance checks. Time on Task is the targeted, task-bounded sibling of Session Duration.

**How it's calculated / collected:** Event-tracked task start and end timestamps. `Time on Task = End Time − Start Time`, averaged across successful task attempts only.

**Example values:** Set a benchmark target before measuring. Glare's Getup checkout example landed at 32.8 seconds (Very Good) — fast and clean. Form submissions often target <60 seconds; checkout <2 minutes; complex setup flows <5 minutes.

**Common mistakes:**
- Treating short Time on Task as automatically good — users may be guessing or skipping required reading.
- Not setting a benchmark target time before measuring — without one, the number is uninterpretable.
- Ignoring the variance — a tight cluster around 30 seconds vs a long tail to 5 minutes tell different stories.

**Related metrics / pairings:** Pairs with **Completion Rate** (did they finish), **Error Rate** (did errors slow them), and **Effort** (did it feel hard). Conflict warning: optimizing Time on Task alone can compromise Comprehension if users start skipping.

**Signal pattern:** "Checkout Time on Task is 32.8 seconds (Very Good) with low variance. Users move quickly without backtracking. Direction: keep the flow; consider lightweight upsell or reassurance modules without breaking the speed."

---

### Visit Frequency

**What it measures:** How often users return to the platform within a given time frame — observed behavior, not self-report.

**When to use:** Engagement and retention analysis, feature stickiness, segment comparisons. Visit Frequency is the analytics-observed counterpart of behavioral **Frequency** (which is self-reported).

**How it's calculated / collected:** Per-user session counts over a defined window. `Visit Frequency = Total Number of Visits / Number of Unique Users` (often expressed as visits per week or visits per month).

**Example values:** Context-dependent. Glare's Banko mobile-banking example landed at 2 visits/week (Good). Daily-utility apps target 5+/week; weekly-utility apps target 1–2/week; monthly-utility apps may consider 1/month healthy.

**Common mistakes:**
- Confusing Visit Frequency (observed) with behavioral **Frequency** (self-reported intent).
- Treating visits as value — visits to fix a problem are different from visits to use a product.
- Not segmenting by user type — power users and casual users have very different healthy cadences.

**Related metrics / pairings:** Pairs with **Recency** (RFM together), **Loyalty** (advocacy follow-on), and **Usefulness** (perceived value). When Visit Frequency holds but Usefulness drops, suspect habit usage masking churn risk.

**Signal pattern:** "Mobile-banking Visit Frequency is 2/week, driven by balance checks and bill pay. Direction: introduce budgeting insights and goal tracking to push toward 3+/week; pair with a Loyalty re-test in 60 days to track downstream advocacy lift."

---

## Why performance metrics matter

Performance metrics help teams understand how efficiently workflows actually function during real usage. They reveal the operational side of the experience — where friction slows users down, where workflows become harder to complete, where systems quietly create extra effort underneath the surface.

These metrics help teams identify workflow problems earlier — before frustration spreads, onboarding weakens, adoption slows, support requests increase, or operational friction becomes harder to unwind.

Over time, performance metrics help teams understand not just whether users completed the experience, but how difficult the experience was to successfully move through.

---

## Performance metrics measure the cost of friction

Behavioral metrics explain what users do. Attitudinal metrics explain how users feel. Performance metrics explain how efficiently the system actually functions underneath the experience. This includes:

- time
- effort
- errors
- reliability
- workflow efficiency
- operational breakdowns

For example:

- users may complete onboarding successfully but take far too long
- AI-assisted workflows may increase activity while slowing decision-making
- users may repeatedly recover from small errors during checkout
- dashboards may create cognitive overload that slows task completion

Performance metrics help teams understand the *hidden operational cost* of friction.

---

## Performance metrics help teams see hidden problems

Performance metrics often reveal problems that isolated success metrics fail to explain clearly:

- **high completion + long time on task** → friction
- **low error rates + weak confidence** → hidden confusion
- **strong engagement + high effort** → workflow fatigue
- **successful onboarding + repeated recovery behavior** → usability breakdowns

The metrics begin explaining how efficiently the workflow actually performs underneath the surface. Over time, these patterns help teams identify operational friction, workflow inefficiency, reliability problems, AI workflow slowdowns, onboarding bottlenecks, dashboard overload, and repeated recovery behavior.

---

## Combining performance with other metrics

Performance metrics become much more valuable when paired with behavioral and attitudinal metrics. A workflow may technically perform well while users still feel frustrated, hesitate repeatedly, lose confidence, or struggle to understand what to do next.

For example:

- **high completion + low trust** → a fragile workflow
- **low errors + rising frustration** → exhausting interactions
- **fast onboarding + weak comprehension** → shallow understanding

The combined signals help teams understand:

- how the workflow performs
- how users behave inside it
- how the experience feels while using it

Over time, these connected patterns help teams compare workflows, reduce operational friction, improve onboarding, and strengthen product decisions across the system.

---

## Source-doc note

The v1.32 Performance Metrics subfolder ships 10 docs but the type-level Overview's example list and the type-level Performance doc table use slightly different sets. This reference uses the **Overview list** as the canonical 11-metric taxonomy: Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency. The subfolder doc named "Completion" duplicates the Behavioral Completion metric and is treated here as Performance Completion Rate (the Performance type-level doc table refers to it that way). Abandonment Rate has no dedicated subfolder doc and is synthesized from the Overview content plus the inverse-of-Completion-Rate convention.

## Source

Drafted from *Glare | UX Metrics, Performance Metrics v1.32* (Drive doc `1uLK-Q-W3C4-vpCe6QZF_4h8VtCKd6_x3e9si_ZFd6yU`, May 9-10, 2026), plus per-metric subfolder docs (`1xbDqmajyMYYIHegBExjaj-ALh66QrA-0`):

- Bounce Rate (`197mciKl_U9Hv1oKLRjzS1qAeS_ym8gNFtPTR8hl2qo4`)
- Click-Through Rate (`1rF2U82wpXigRLfX2AccQwwebwSnBxPov3dC77bKEpvA`)
- Completion (`1EpA7hj2V8GB-Bt7DIsTuRix9KpdKfUGum3pQcj-ntOc`) — *treated as Completion Rate*
- Completion Rate (`1DbztX2lljIXBiQOGobDIBwHKuBGx-zCWfs-jCPkYtyI`)
- Drop-off Rate (`1OmQEBWSj8zqGV5QnWZL7bkyQ1-U_uR6kqLkbSmWqykA`)
- Error Frequency (`1KLxEOqutHZE7CiWjp0FGBmU5ROVeh7Q8ARVgpQs9DAA`)
- Error Rate (`1fDn46fPfq7x22rMMMeFGKbqU6FLFHIAWoEUa-VCZFrU`)
- Recency (`1ffZNAIASF0PwuJTKsgo8-b-inD_nhUpY68Tpw-Tp-e0`)
- Session Duration (`13dDCOWi4nV3-zHOO-M8cphyBvoEgTenoFubD-jEQsJk`)
- Time on Task (`1Ua3Gz-2Jo6Uhr27s8KLi3kLeWfpR2VSmxixHMZeKo7o`)
- Visit Frequency (`1SzQekKWOB5KZn2iuQjBiCzcYO81CfkTxhUL_bf1RHVQ`)
- Abandonment Rate — no dedicated subfolder doc; synthesized from Overview content

## Failure modes

These are common ways this skill goes wrong in practice:

- **Inventing performance metrics.** Borrowing names like "engagement velocity," "friction score," or other made-up names. Stick to the canonical eleven — or route to another type.
- **Performance-only stacks.** Reading time-on-task and error rate without trust or comprehension. The workflow may be fast but emotionally exhausting, or efficient but confusing.
- **Confusing speed for ease.** Fast completion doesn't mean low effort — users may be powering through high friction. Pair performance with effort and hesitation to read what the speed means.
- **Treating completion rate as the headline.** Completion alone doesn't tell you how difficult the experience was. Two 80% completion rates can be very different experiences underneath; performance metrics need each other to read clearly.

