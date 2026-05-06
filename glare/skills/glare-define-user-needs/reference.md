# User Needs — Reference (Glare Define, v1.1, 2026-05-06)

## The five-category user-need stack

Glare organizes user needs into **five categories** ordered foundational → aspirational, with **22 individual need types** nested inside them. The categories are levels of confidence users build through design — function, then trust, then relevance, then results, then meaning. Each level earns the right to the next.

> **Compatibility note.** Earlier compressed versions of this skill described User Needs as a 7-layer UX Honeycomb (Findable → Desirable). The current Define source-of-truth (User Needs v1.1, Define Overview v1.1) restructures this into the five categories below. The 22 individual need-type pages are still consistent with their honeycomb-style framing; what changed is the category-level grouping. Each individual need (Findable, Reliable, Desirable, etc.) is preserved and still maps to its layered metrics.

| Category | User question | Design outcome | Sample metrics | Facet |
|---|---|---|---|---|
| **Basics** | "Can I use it easily?" | Flow, clarity, access | Task completion, error rate, time on task | Measure |
| **Trust** | "Do I believe it works?" | Predictability, consistency | Credibility, bounce rate | Define |
| **Personal** | "Does it fit my needs?" | Relevance, inclusion | Adaptability, comprehension | Define + Focus |
| **Impact** | "Does it make a difference?" | Efficiency, results | Conversion, retention | Show |
| **Feelings** | "Does it inspire me?" | Emotion, motivation | Sentiment, preference | Focus |

## Needfinding (Stanford-born)

Before naming a category- or need-level gap, surface it. Needfinding focuses on what drives behavior, not what people say.

1. **Distinguish needs from wants.** A want is a symptom; a need is the root cause. "Faster horse" → "faster travel."
2. **Observe before you ask.** Watch what users skip, repeat, or struggle with.
3. **Use multiple sources.** Interviews + surveys + behavioral tests. Each exposes a different layer.
4. **Capture contradictions.** When words and behavior diverge, an unmet need is hiding there.

**Validation rule:** if users say they need it but ignore it in practice, it's a *want masquerading as a need*.

---

## 1. Basics — "Can I use it easily?"

The foundation. Before trust, before emotion, before value, a product must simply work. When Basics fail, users rarely complain — they just leave.

### 1.1 Usable

**Definition:** Users can act on what they found, easily and confidently. Anchored in Nielsen's 10 heuristics — visibility of status, match between system and real world, user control and freedom, consistency, error prevention, recognition over recall, flexibility and efficiency, aesthetic minimalism, recover from errors, help and documentation.

**Signal types:** Behavioral (completion, errors, time, effort), Attitudinal (confidence, satisfaction).
**Example metrics:** Completion Rate, Error Rate, Time on Task, Effort, Satisfaction, Task Duration.
**Common failure:** Cognitive load too high — too much to remember, too many corrections, no clear status, no safe undo.

### 1.2 Useful

**Definition:** Solves the right problem and helps users complete meaningful tasks. A product can be polished without being useful, but it will not survive.

**Key signals of weakness:** users abandon halfway because outcomes don't help; feedback like "this doesn't solve my problem"; shallow engagement; users build workarounds.
**Example metrics:** Usefulness, Sentiment, Post-Task Satisfaction, Frequency, Helpfulness.
**Common failure:** Polish over purpose. Roadmap full, feature usage flat.

### 1.3 Findable

**Definition:** Users can locate the information, feature, or next step without search effort. The hidden first test every product fails before a click happens.

**Key questions:** Can users see where to go next from any screen? Is information grouped the way users think? Does search understand intent? Are labels in user vocabulary, not jargon?
**Signal types:** Behavioral (clicks, paths, search refinement, hesitations).
**Example metrics:** First-Click Success, Comprehension, Completion Rate, Time on Task, Search Refinement Rate, Bounce Rate.
**Common failure:** Information is on the page but buried under jargon, inconsistent placement, or unclear hierarchy. Users hesitate, refine searches, or leave.

### 1.4 Accessible

**Definition:** Everyone — regardless of ability, context, or device — can perceive, operate, and understand the product. Foundation of inclusion, not a compliance checkbox.

**Key questions:** Is content perceivable through more than one sense? Can every action be triggered by keyboard, mouse, touch, and assistive devices? Does layout survive 200% zoom? Does it work with NVDA, VoiceOver, JAWS?
**Signal types:** Behavioral (completion across input methods), Performance (assistive-tool task success), Attitudinal (sentiment from diverse users).
**Example metrics:** Completion Rate (across input methods), Comprehension, Effort, Error Rate, Error Recovery Rate, Satisfaction with assistive tech.
**Common failure:** Designed for the median user on a fresh laptop. Breaks under zoom, keyboard nav, or screen reader.

---

## 2. Trust — "Do I believe it works?"

Once something works, users need to *believe* it works. Trust is the bridge between function and confidence — earned through consistent design that behaves exactly as people expect.

### 2.1 Credible

**Definition:** Users believe the product will do what it promises. Trust formed before action through clarity, honesty, transparency, polish, social proof, and reliable feedback.

**Key questions:** Is purpose, benefit, and next step in plain language at first glance? Are claims backed by data, not hype? Are policies easy to find, not buried? Is social proof real (verified reviews, named brands)?
**Signal types:** Attitudinal (trust, sentiment, brand score), Behavioral (completion, engagement with proof sections), Performance (bounce, conversion, error frequency).
**Example metrics:** Trust, Comprehension, Sentiment, Brand Score, Bounce Rate, Conversion Rate, Load Time.
**Common failure:** Vague claims, inconsistent tone, hidden policies, or staged-feeling testimonials.

### 2.2 Secure

**Definition:** Users feel safe. Data is protected, risk is limited, and safety choices are clear and easy. Security in UX is trust made visible.

**Key questions:** Do users know what data is collected and why? Are defaults private and least-privilege? Is authentication strong but low-friction? Are sharing scopes and permissions predictable?
**Signal types:** Attitudinal (trust, sentiment), Behavioral (completion, abandonment at consent steps).
**Example metrics:** Trust, Comprehension, Completion Rate, Abandonment Rate, Error Rate, Error Recovery Rate.
**Common failure:** Vague consent, default-public sharing, recovery flows that lock users out or expose accounts to takeover.

### 2.3 Reliable

**Definition:** The product behaves the same under pressure as on a quiet day. Saves state, keeps data accurate, recovers safely. Not just uptime — *predictable progress users can repeat with confidence*.

**Key questions:** Do core flows work the same at peak load? Is progress autosaved? Are status messages accurate and human-readable? Are critical actions idempotent or clearly reversible?
**Signal types:** Behavioral (completion under load, error recovery), Attitudinal (trust, satisfaction).
**Example metrics:** Success Rate at peak, Completion Rate, Error Rate, Error Recovery Rate, Trust, Support Contact Rate.
**Common failure:** Works in the demo, breaks under real conditions. Lost drafts, conflicting data, duplicate charges on retry.

### 2.4 Intuitive

**Definition:** People see what it does, know what to do next, and feel confident as they move. Intuition comes from clear signals, familiar patterns, and feedback that confirms progress.

**Key questions:** Is purpose and primary action obvious? Are descriptive labels and microcopy used (not jargon)? Are familiar patterns reused? Is feedback immediate?
**Signal types:** Behavioral (comprehension, completion, time on task), Attitudinal (satisfaction, trust).
**Example metrics:** Comprehension, Completion Rate, Time on Task, Effort, Error Rate, Satisfaction.
**Common failure:** Purpose is unclear at a glance; users hesitate, scan for clues, backtrack.

---

## 3. Personal — "Does it fit my needs?"

When a product feels like it understands you, design becomes personal. This is where experience shifts from "this works" to "this works for me."

### 3.1 Inclusive

**Definition:** Respects differences and invites everyone in. Clear language, flexible choices, fair defaults, and representation that reflects real people.

**Key questions:** Is language plain and respectful? Do inputs fit real names and pronouns? Are examples and visuals diverse? Are defaults private and minimal until users opt in?
**Signal types:** Behavioral (completion across diverse users), Attitudinal (trust, sentiment).
**Example metrics:** Comprehension, Completion Rate, Sentiment, Abandonment Rate, Trust.
**Common failure:** Forms that erase identity (name fields too short, no pronoun option), examples that exclude common life situations, defaults that overshare by mistake.

### 3.2 Adaptable

**Definition:** Adjusts to different users, devices, and situations without adding friction. Reshapes layout, choices, and workflows to match goals and constraints.

**Key questions:** Does the product detect screen size and input method? Does layout reflow without overlap or truncation? Are preferences saved? Are alternative inputs supported (keyboard, paste, upload, voice)?
**Signal types:** Behavioral (success rate, time on task across contexts), Attitudinal (satisfaction).
**Example metrics:** Success Rate, Time on Task, Completion Rate, Effort, Satisfaction, Retention.
**Common failure:** One fixed path forces users into rework; mobile users can't reach the primary action one-handed.

### 3.3 Connected

**Definition:** Journeys link up, data stays in sync, and people can move between steps, devices, and teams without losing context.

**Key questions:** Does state and intent carry across screens, devices, sessions? Do deep links land at the exact place to act? Do roles hand off cleanly with full context?
**Signal types:** Behavioral (completion, time on task across handoffs), Attitudinal (trust, satisfaction).
**Example metrics:** Completion Rate, Time on Task, Effort, Support Contact Rate, Trust.
**Common failure:** Notifications dump users at generic pages; cross-role work loses context; data conflicts across screens.

### 3.4 Insightful

**Definition:** Turns raw data into meaning, explains why it matters, and points to a clear next step. If a chart does not change a decision, it is not an insight.

**Key questions:** Is the question and outcome clear? Does the recommended action come first, detail second? Are definitions and sources transparent? Are anomalies and drivers explained?
**Signal types:** Behavioral (comprehension, success rate on follow-up tasks), Attitudinal (trust).
**Example metrics:** Comprehension, Time on Task, Completion Rate (of follow-up action), Trust, Support Contact Rate.
**Common failure:** Dashboards full of charts that nobody acts on; "what" without "why."

---

## 4. Impact — "Does it make a difference?"

Where outcomes meet experience. The space between intention and achievement. A product that does not create progress eventually becomes noise.

### 4.1 Valuable

**Definition:** The outcome makes users feel their time was well spent. Not polish, features, or copy — the *result*.

**Key questions:** What problem does this solve? How does it change the user's day? Could they get the same benefit another way? Would they miss it if it disappeared?
**Signals of value slipping:** Users complete a task but never return; "I could do this faster in Excel"; engagement spikes week one, collapses week two.
**Signal types:** Attitudinal (feeling, sentiment, satisfaction), Behavioral (engagement, frequency, intent to continue).
**Example metrics:** Retention before/after release, Intent-to-reuse, NPS, Feature adoption, Frequency, Post-Task Satisfaction.
**Common failure:** Shipping activity instead of outcomes. Roadmap full, adoption flat.

### 4.2 Sustainable

**Definition:** Continues to create value over time. Balances efficiency, reliability, and respect for attention so trust compounds and fatigue fades.

**Key questions:** Does performance stay stable across releases? Is cognitive load low? Are user time and attention respected? Does what they learned once still work?
**Signal types:** Behavioral (success rate over time, retention), Attitudinal (satisfaction, trust).
**Example metrics:** Success Rate, Time on Task, Retention Rate, Satisfaction, Effort.
**Common failure:** Each release adds friction; familiar patterns get renamed without reason; notifications and confirmations multiply until users tune out.

### 4.3 Efficient

**Definition:** How quickly people reach value with the least effort. Fewer steps, less typing, clearer paths.

**Key questions:** Is the path to outcome clear? Are inputs minimized? Are defaults smart and prefilled? Are bulk and keyboard accelerators available without blocking beginners?
**Signal types:** Behavioral (time on task, effort, completion), Attitudinal (satisfaction).
**Example metrics:** Time on Task, Effort, Completion Rate, Success Rate, Abandonment Rate.
**Common failure:** Every screen asks for one more thing; users have to repeat work; no shortcuts for power users.

### 4.4 Scalable

**Definition:** Holds up as complexity, data, and users multiply. Performs reliably, stays clear under pressure, supports growth without adding friction.

**Key questions:** Does performance stay reliable as usage increases? Are bulk operations supported? Does navigation scale as content grows? Is collaboration safe and clear at volume?
**Signal types:** Behavioral (success rate at scale, time on task with large data), Attitudinal (satisfaction, trust).
**Example metrics:** Success Rate, Time on Task, Completion Rate, Error Rate, Trust.
**Common failure:** Demo data hides the bottleneck; the product feels fast at 10 items and slow at 1000; bulk work requires manual repetition.

---

## 5. Feelings — "Does it inspire me?"

The highest layer, where credibility, relevance, and value combine to create experiences that feel human. Feelings cannot be faked — they emerge naturally when every other layer is strong.

### 5.1 Desirable

**Definition:** The emotional pull that keeps people coming back. Clarity + craft + character producing a product that feels worth using again. Not decoration — fit and finish in service of the goal.

**Key questions:** Does visual design make the task easier? Does copy sound like a helpful human? Are alignment, states, and components tight and consistent? Does motion guide attention calmly (under ~500ms)?
**Signal types:** Attitudinal (satisfaction, desirability, sentiment, trust), Behavioral (retention, completion, time on task).
**Example metrics:** Satisfaction, Desirability, Sentiment, Trust, Retention/Return Rate, Completion Rate.
**Common failure:** Functional but flat. Inconsistent states, robotic copy, decorative motion, generic "Success" toasts.

### 5.2 Delightful

**Definition:** Care you can feel. Supports the goal, reduces effort, and adds small moments that lift the mood without getting in the way. Clarity plus craft.

**Key questions:** Does delight serve the outcome (not block it)? Is pace calm and the flow smooth? Is feedback clear and positive? Is motion purposeful, not decorative?
**Signal types:** Attitudinal (satisfaction, desirability, sentiment), Behavioral (completion, retention).
**Example metrics:** Satisfaction, Desirability, Sentiment, Completion Rate, Time on Task, Retention.
**Common failure:** Confetti for routine actions; motion that distracts; "fun" copy in stressful steps like payment or recovery.

### 5.3 Engaging

**Definition:** Steady interest with a purpose. A clear value loop, small wins that build momentum, and a comfortable rewarding pace.

**Key questions:** Is the value loop clear (what users get each session and why to come back)? Are goals and progress visible? Do users reach a fast first win? Are reminders thoughtful, not spammy?
**Signal types:** Behavioral (retention, completion, return rate), Attitudinal (satisfaction, desirability).
**Example metrics:** Retention/Return Rate, Completion Rate, Time on Task, Satisfaction, Desirability.
**Common failure:** Streaks for streaks' sake; "engagement" via dark patterns; reminders that ping but don't deliver value.

### 5.4 Empowering

**Definition:** Confidence in action. Clear control, visible consequences, easy try-learn-recover. Beginners succeed on day one; experts work at full speed.

**Key questions:** Is action clear and outcome obvious? Are consequences previewed before commit? Are undo, drafts, and version history available? Does power scale with skill?
**Signal types:** Behavioral (completion, error recovery, time on task), Attitudinal (trust, satisfaction).
**Example metrics:** Completion Rate, Success Rate, Error Rate, Error Recovery Rate, Trust, Satisfaction.
**Common failure:** Every change feels risky; no preview before commit; advanced users can't go faster.

---

## Quick checklist

1. List your top 3–5 user needs.
2. Pin each need to a category and a specific need type.
3. Match each to at least one metric.
4. Run a test to capture signals.
5. Share the evidence with your team.
6. Revisit and refine as users evolve.

If you can't list three concrete needs tied to a specific need type and a metric, you're not done.

## Related key terms

- **Five User-Need Categories** — Basics, Trust, Personal, Impact, Feelings.
- **22 Individual User-Need Types** — Usable, Useful, Findable, Accessible · Credible, Secure, Reliable, Intuitive · Inclusive, Adaptable, Connected, Insightful · Valuable, Sustainable, Efficient, Scalable · Desirable, Delightful, Engaging, Empowering.
- **Needfinding** — Stanford-born practice for surfacing real (not stated) needs.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Want masquerading as a need** — stated importance with no behavioral follow-through.
