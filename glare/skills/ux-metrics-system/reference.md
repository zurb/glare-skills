# Measurement System — Reference (v1.32)

## The system framing

UX Metrics work best when they operate as a connected system, not as isolated scores inside dashboards. A single metric can show one small part of the experience. But when metrics work together, teams begin to see patterns:

- where users get confused
- where trust breaks down
- where workflows create friction
- where ideas gain momentum
- where experiences improve over time

Many organizations still struggle to clearly understand what the product experience actually looks like across the system. Different teams often measure different things — product teams may focus on delivery speed, leadership on revenue, design on usability, researchers on user behavior, engineering on implementation quality. Each group may have useful information, but the signals often stay disconnected. One dashboard may show high engagement while another reveals lower trust, slower onboarding, rising frustration, and growing confusion.

Over time, teams begin reacting to isolated numbers instead of understanding the larger experience forming underneath the product.

## UX Metrics work together as a system

Most teams already have dashboards full of numbers. Individual metrics rarely explain the full experience on their own. A completion score may look healthy while users quietly struggle. Engagement may rise while confidence weakens. Users may technically finish a task while still feeling confused.

The chain:

> metrics → form patterns → create signals → help teams interpret what is happening → guide stronger decisions

Examples (the v1.32 canonical pairs):

- **high completion + long time on task** may reveal friction
- **strong engagement + weak trust** may reveal hesitation
- **low errors + low confidence** may reveal hidden confusion

The metrics begin explaining each other. Instead of looking at isolated scores, teams begin seeing the *shape* of the experience. A workflow may technically succeed while confidence drops. Engagement may rise while hesitation quietly increases underneath. These combined patterns help teams understand not just what users did, but how the experience actually felt while they were moving through it.

---

## When to use

- When the user is treating UX metrics as a connected operational system, not isolated scores.
- When organizations measure differently across teams (product on speed, leadership on revenue, design on usability) and signals stay disconnected.
- When the team has lots of dashboards but no clarity, and measurement breaks down across the org.
- When metrics need to form patterns — Confusion Trap, Friction Wall, Trust Gap, "high completion long time on task."
- When evolving from isolated dashboards to a shared measurement system that the org argues from.

**Don't use when** the user wants the four metric types at the framework level (`glare:ux-metrics`), per-metric definitions (use the type sub-skills), or stacking specific metrics (`glare:ux-metrics-stack`).

## The three recurring patterns

As teams compare metrics together, certain patterns begin repeating across workflows and experiences. These patterns often reveal deeper problems that isolated dashboards miss.

### Confusion Traps

Users may complete a task successfully while still feeling lost or unsure. Completion remains high, but comprehension, clarity, and confidence weaken underneath the experience.

Often appears during:

- onboarding
- navigation changes
- dashboard redesigns
- AI-assisted workflows

### Friction Walls

Users understand what they are trying to do, but the workflow slows them down. Time on task increases, effort rises, frustration quietly builds.

Often appears when:

- workflows become too complex
- navigation becomes harder to scan
- onboarding asks for too much information
- AI recommendations create extra steps

### Trust Gaps

The workflow technically functions, but users stop feeling safe or confident in the experience. Especially important in:

- fintech
- AI systems
- healthcare
- onboarding flows
- automation workflows

Users may continue using the product while trust slowly weakens underneath the experience.

---

## Measurement breaks down across organizations

As products grow, measurement often becomes harder to interpret. Different teams collect different signals, track different goals, optimize for different outcomes. Over time, organizations slowly lose a shared understanding of what a healthy experience actually looks like.

Different teams often:

- use different dashboards
- interpret success differently
- compare different benchmarks
- optimize for local goals
- measure different parts of the experience

This creates tension during roadmap planning, launch reviews, prioritization discussions, onboarding redesigns, and AI workflow evaluations. One team may believe a release performed well because engagement increased. Another team may see lower confidence, rising support requests, slower task completion, and more hesitation during onboarding.

Without shared measurement, teams can end up arguing over different versions of the same experience. Reviews become harder to navigate because nobody fully trusts how success is being measured.

---

## UX Metrics help teams build shared visibility

Measurement systems help teams create shared visibility across the product. Instead of isolated dashboards and disconnected opinions, teams begin looking at the experience through connected signals and recurring patterns.

This helps teams:

- compare workflows more clearly
- identify friction earlier
- spot repeating problems
- understand tradeoffs
- align around user behavior
- strengthen reviews and prioritization

Especially important in AI-assisted workflows where recommendations change dynamically, experiences adapt constantly, outputs scale quickly, and teams test more ideas than they can easily evaluate. Without stronger measurement systems, teams can struggle to understand whether AI is actually improving the experience or simply increasing activity.

---

## The four measurement areas

Inside Glare, UX Metrics are organized into four measurement areas:

| Area | What it measures | Examples |
|---|---|---|
| **Attitudinal** | How users feel | trust, satisfaction, desirability, sentiment, expectations |
| **Behavioral** | What users do | completion, engagement, effort, comprehension, usability |
| **Performance** | Outcomes and efficiency | completion rate, error rate, drop-off rate, click-through rate, time on task |
| **Intelligence** | Whether AI helps users move forward | recommendation quality, prompt effectiveness, AI guidance usefulness, workflow assistance, confidence calibration |

Attitudinal signals often reveal emotional friction before larger problems appear. Behavioral signals reveal where users hesitate, struggle, or abandon. Performance signals show whether workflows are functioning successfully. Intelligence signals show whether AI improves understanding instead of simply creating more output.

---

## The system builds understanding over time

Strong measurement systems are not one-time reports. Over time they become part of how teams repeatedly evaluate product direction together. The system begins acting more like operational memory across the organization.

Teams start recognizing:

- recurring friction
- repeated hesitation
- weak onboarding patterns
- trust breakdowns
- workflows that consistently perform better

As more reviews, launches, onboarding flows, and AI-assisted experiences get measured, larger patterns become easier to see. The system becomes more valuable because teams are no longer reacting to isolated moments. They begin understanding how the product behaves over time. That visibility helps organizations make clearer product decisions with more confidence across the system.

---

## Quick diagnostic — system vs scoreboard

| Symptom | What it signals | Move |
|---|---|---|
| Each team has its own dashboard, no cross-team review | Scoreboard mode | Build a shared review surface across Attitudinal / Behavioral / Performance / Intelligence |
| Metrics reported in isolation, no patterns named | Scoreboard mode | Pair metrics together — see Confusion / Friction / Trust patterns above |
| Engagement up + trust down argued as "we're fine" | Misread Trust Gap | Surface the explicit trust signal alongside the engagement number |
| Completion rising + time-on-task rising | Possible Friction Wall | Investigate effort and recovery behavior; check `glare:ux-metrics-performance` |
| Onboarding completes but support tickets rise weeks later | Likely Confusion Trap | Investigate comprehension and confidence in the same window |

## Source

Drafted from *Glare | UX Metrics, Measurement System v1.32* (Drive doc `1Ll6Z-4NiIBDu6jBpMQGgKx_SR21YWtRnC1ptsO4KUNU`, May 10, 2026).

## Failure modes

These are common ways this skill goes wrong in practice:

- **System as another dashboard.** Building a "UX metrics dashboard" alongside the product and revenue dashboards instead of integrating with them. The system has to rebuild *shared visibility*, not add another window.
- **Forcing one definition on every team.** Insisting product, design, and research use identical metrics. Each function has reasons for its definitions; the system rebuilds connections, not uniformity.
- **System without pattern recognition.** Pulling metrics together but never naming the recurring patterns (Confusion Trap, Friction Wall, Trust Gap). The patterns are what turn metrics into operating memory.
- **Skipping the org-language layer.** Building the system inside design tools without ever translating into product or business vocabulary. The system needs to surface in the meetings where decisions happen, not in research repos.

