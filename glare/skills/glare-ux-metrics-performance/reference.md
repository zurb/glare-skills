# Performance Metrics — Reference (v1.32)

## What performance metrics measure

Performance metrics measure how efficiently a workflow, system, or experience actually functions. They help teams understand:

- how long tasks take
- where users drop off
- where errors increase
- how much effort workflows require
- whether systems perform reliably under real usage

Product teams often focus heavily on whether users completed a task. But completion alone rarely explains how difficult the experience actually was. Users may finish onboarding while struggling the entire time, complete checkout after repeated errors, use AI recommendations while constantly double-checking results, or finish tasks successfully while moving much slower than expected.

Performance metrics help teams understand the operational health of the experience underneath the workflow itself.

---

## The eleven performance metrics (v1.32)

| Metric | Definition | When to use | Common mistakes |
|---|---|---|---|
| **Abandonment Rate** | Percentage of users who start but do not finish a task — checkout, form, multi-step process. | Checkout flows, onboarding, application processes, anywhere users start but may not finish. | Confusing Abandonment Rate (started-then-stopped) with Drop-off Rate (left at a specific step) or Bounce Rate (left after only one page); not segmenting by step (the abandonment cluster is the actionable signal); celebrating low abandonment when users are also reporting low confidence. |
| **Bounce Rate** | Percentage of users who leave after viewing just one page without further action. | Landing pages, entry points, content meant to drive further exploration; hero CTAs; campaign-effectiveness checks. | Treating low Bounce as automatically good (the page may be working but the wrong audience is arriving); ignoring source/intent (bounce on an unrelated query is different from bounce on a target query); using Bounce as a usability metric (it is closer to a relevance metric). |
| **Click-Through Rate (CTR)** | Percentage of users who click a link or CTA after seeing it. | Navigation, buttons, marketing copy, A/B tests, email campaigns, hero CTAs, feature-announcement evaluation. | Conflating CTR with intent (a click is not an intent confirmation); reporting CTR without impressions denominator; not pairing with a downstream Completion or Conversion to see if the click led anywhere useful. |
| **Completion Rate** | Percentage of users who fully complete a defined process — checkout, sign-up, form. Funnel-level analytics percentage. | Onboarding flows, form submissions, checkout process, any defined start-to-finish journey at scale. | Confusing Completion Rate (analytics percentage of started-vs-finished) with Behavioral Completion (whether a single tested user reached the end via direct or indirect path); not segmenting by step (the drop is more useful than the average); using Completion Rate alone as the launch signal. |
| **Drop-off Rate** | Percentage of users who exit at a specific step within a flow. | Multi-step processes — onboarding, checkout, setup wizards, form submissions; comparing per-step impact of design changes. | Reporting an aggregate drop-off (the per-step pattern is the signal); treating high drop-off as a design problem when it may be an audience-fit problem; not investigating *why* users dropped off (qualitative follow-up). |
| **Error Frequency** | Average number of errors per session — how often users encounter errors during a session. | High-importance flows (login, checkout, data entry); live monitoring; spike detection; usability tests on stable prototypes. | Confusing Error Frequency (errors per session) with Error Rate (percentage of users who hit an error); treating all errors as equal (recoverable typo vs hard system failure are very different); not categorizing errors by type. |
| **Error Rate** | Percentage of users who encounter errors while performing tasks. | Stability checks for critical workflows; identifying friction points; reliability evaluation; pre-launch QA verification. | Reporting Error Rate without Error Frequency (you may have a few users hitting many errors); not investigating recovery (did users recover, or did they abandon?); using Error Rate alone for AI-recommendation quality (some "errors" are really comprehension breakdowns). |
| **Recency** | Time since a user's last visit — freshness of engagement with the platform or product. | Retention analysis, re-engagement campaigns, churn-risk scoring, segment comparisons over time. | Confusing Recency with Frequency (Recency is "how long since last," Frequency is "how often"); treating high Recency as automatically bad (some products have legitimate long-tail visit patterns); not pairing with a re-engagement signal. |
| **Session Duration** | Average time users spend during a session — depth of engagement with the content or platform. | Content engagement, dashboard health, longer-form experiences, comparing engagement across versions. | Treating long Session Duration as automatically good (it can mean engagement OR confusion); not pairing with task completion (long session + low completion is a Friction Wall); using it as a usability metric (it is closer to engagement). |
| **Time on Task** | Average time users spend completing a specific task — efficiency and ease of task completion. | Specific tasks within a workflow, A/B comparisons, identifying friction within onboarding or checkout, post-launch performance checks. | Treating short Time on Task as automatically good (users may be guessing); not setting a benchmark target time; ignoring the variance (a tight cluster vs a long tail tell different stories). |
| **Visit Frequency** | How often users return to the platform within a given time frame — observed behavior. | Engagement and retention analysis, feature stickiness, segment comparisons. | Confusing Visit Frequency (observed) with Behavioral Frequency (self-reported intent); treating visits as value (visits to fix something are different from visits to use something); not segmenting by user type. |

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

The v1.32 Performance Metrics subfolder ships 11 docs but the type-level Overview's example list and the type-level Performance doc table use slightly different sets. This reference uses the **Overview list** as the canonical taxonomy: Abandonment Rate · Bounce Rate · Click-Through Rate · Completion Rate · Drop-off Rate · Error Frequency · Error Rate · Recency · Session Duration · Time on Task · Visit Frequency. The subfolder doc named "Completion" duplicates the Behavioral Completion metric and is treated here as Performance Completion Rate (the Performance type-level doc table refers to it that way).

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
