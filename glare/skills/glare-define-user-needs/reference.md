// User Needs — Reference (Glare Define, v1.1)

## The UX Honeycomb

Glare's User Needs model adapts the **UX Honeycomb** lineage (Morville-style facets of user experience) into seven connected layers of confidence. They are ordered **foundational → aspirational**: Findable is the floor, Desirable is the ceiling. Each layer earns the right to the next. If a lower layer breaks, higher layers can't compensate — a beautiful product no one can find is still invisible; a delightful product that loses your work is still untrustworthy.

Use the layers as a diagnostic ladder: walk from Findable upward and stop at the first one that breaks. That's where the unmet need lives.

| # | Layer | Question users ask | Outcome design must produce |
|---|---|---|---|
| 1 | Findable | "Where is it?" | Locatable structure, clear pathways |
| 2 | Accessible | "Can I get to it?" | Perceivable, operable, understandable, robust |
| 3 | Usable | "Can I act on it?" | Frictionless, forgiving, learnable |
| 4 | Credible | "Do I believe it?" | Honest, transparent, professional |
| 5 | Reliable | "Will it hold up?" | Consistent state, accurate data, safe recovery |
| 6 | Valuable | "Is it worth my time?" | Real outcome, reduced effort |
| 7 | Desirable | "Do I want to come back?" | Polish, voice, small rewards |

## Needfinding (Stanford-born)

Before naming a layer-level need, surface it. Needfinding focuses on what drives behavior, not what people say.

1. **Distinguish needs from wants.** A want is a symptom; a need is the root cause. "Faster horse" → "faster travel."
2. **Observe before you ask.** Watch what users skip, repeat, or struggle with.
3. **Use multiple sources.** Interviews + surveys + behavioral tests. Each exposes a different layer.
4. **Capture contradictions.** When words and behavior diverge, an unmet need is hiding there.

**Validation rule:** if users say they need it but ignore it in practice, it's a *want masquerading as a need*.

---

## 1. Findable

**Definition:** Users can locate the information, feature, or next step without search effort. The hidden first test every product fails before a click happens.

**Key questions:**
- Can users see where to go next from any screen?
- Is information grouped the way users think, not the way teams are organized?
- Does search understand intent, not just literal strings?
- Are navigation and key controls in consistent, predictable locations?
- Does visual hierarchy point to what matters most first?
- Are labels in user vocabulary (not internal jargon)?
- Can users recover and backtrack without losing state?

**Signal types:** Behavioral (clicks, paths, search queries, hesitations).

**Example metrics:** Comprehension, Completion Rate, Success Rate, First-Click Success, Time on Task, Error Rate, Search Refinement Rate, Bounce Rate, Abandonment Rate.

**Common failure mode:** Information is on the page but buried under jargon, inconsistent placement, or unclear hierarchy. Users hesitate, refine searches, or leave.

---

## 2. Accessible

**Definition:** Everyone — regardless of ability, context, or device — can perceive, operate, and understand the product. Foundation of inclusion, not a compliance checkbox.

**Key questions:**
- Is content perceivable through more than one sense (alt text, contrast, semantic structure)?
- Can every action be triggered by keyboard, mouse, touch, and assistive devices?
- Is language plain, with error messages that explain the fix?
- Does feedback come through multiple channels (visual, text, ARIA, haptic)?
- Does layout survive zoom (200%), orientation changes, and small screens?
- Is recovery forgiving — input persists, errors are described, undo is offered?
- Does it work with NVDA, VoiceOver, JAWS?

**Signal types:** Behavioral (completion across input methods), Performance (assistive-tool task success), Attitudinal (sentiment from diverse users).

**Example metrics:** Completion Rate (across input methods), Comprehension, Effort, Error Rate, Error Recovery Rate, Satisfaction, Task Success with assistive tech.

**Common failure mode:** Designed for the median user on a fresh laptop. Breaks under zoom, keyboard nav, or screen reader, silently excluding a significant share of the audience.

---

## 3. Usable

**Definition:** Users can act on what they found, easily and confidently. Anchored in Nielsen's 10 heuristics, extended in Glare by tying each heuristic to a measurable signal.

**Key questions (from Nielsen's 10):**
- Visibility of system status — do users always know what's happening?
- Match between system and real world — does language match user vocabulary?
- User control and freedom — can users undo, redo, cancel without fear?
- Consistency and standards — do similar things behave similarly?
- Error prevention — are mistakes prevented before they happen?
- Recognition over recall — is what users need visible, not memorized?
- Flexibility and efficiency — are there shortcuts for experienced users?
- Aesthetic and minimalist design — is every element pulling weight?
- Help users recognize, diagnose, and recover from errors — are messages in plain language with clear next steps?
- Help and documentation — is help available inline, where users need it?

**Signal types:** Behavioral (completion, errors, time, effort), Attitudinal (confidence, satisfaction).

**Example metrics:** Completion Rate, Error Rate, Time on Task, Effort, Satisfaction, Task Duration, Error Recovery, Time to Resolution.

**Common failure mode:** Users can find it and reach it, but cognitive load is too high — too much to remember, too many corrections, no clear status, no safe undo.

---

## 4. Credible

**Definition:** Users believe the product will do what it promises. Trust formed before action — through clarity, honesty, transparency, polish, social proof, and reliable feedback.

**Key questions:**
- Is purpose, benefit, and next step in plain language at first glance?
- Are claims backed by data, not hype? Any dark patterns?
- Are design patterns, tone, and structure consistent across screens and channels?
- Is authorship, data use, and policy easy to find — not buried?
- Do visual polish, fast load, and lack of typos signal care?
- Is social proof real (verified reviews, named brands, data-backed quotes)?
- Does the system reliably confirm action, surface errors, and close loops?
- Does microcopy reassure during high-stakes moments (checkout, signup, data entry)?
- Does accessibility itself signal integrity?

**Signal types:** Attitudinal (trust, sentiment, brand score, perceived quality), Behavioral (completion, engagement with proof sections), Performance (bounce, abandonment, conversion, error frequency).

**Example metrics:** Trust, Comprehension, Sentiment, Satisfaction, Perceived Quality, Bounce Rate, Abandonment Rate, Conversion Rate, Brand Score, Load Time.

**Common failure mode:** Vague claims, inconsistent tone, broken visuals, hidden policies, or staged-feeling testimonials. Doubt creeps in and users bail before the product gets a chance.

---

## 5. Reliable

**Definition:** The product behaves the same under pressure as on a quiet day. Saves state, keeps data accurate, recovers safely, signals what's happening in human language. Not just uptime — *predictable progress users can repeat with confidence*.

**Key questions:**
- Do core flows work the same at peak load as off-hours?
- Is progress autosaved? Does state survive refresh, navigation, app updates?
- Are status messages accurate, timestamped, and human-readable (no false success bars)?
- Do numbers and records match across screens and sessions, with a single source of truth?
- Does validation prevent common mistakes early and preserve correct entries on partial failure?
- Are critical actions idempotent or clearly reversible — no double charges on retry?
- Do updates preserve backward compatibility and familiar patterns?
- Is there a visible audit trail — who did what, when, with rollback?
- Does the system degrade gracefully offline or under outage, queueing for later sync?
- When something fails, do alerts say what happened, why it matters, and how to fix it?

**Signal types:** Behavioral (completion under load, error recovery, abandonment), Attitudinal (trust, satisfaction, sentiment, comprehension).

**Example metrics:** Success Rate at peak, Completion Rate, Error Rate, Error Recovery Rate, Time on Task, Abandonment Rate, Retention/Return Rate, Trust, Support Contact Rate.

**Common failure mode:** Works in the demo, breaks under real conditions. Lost drafts, conflicting data across screens, duplicate charges on retry, vague error codes — every failure forces rework and erodes trust.

---

## 6. Valuable

**Definition:** The outcome makes users feel their time was well spent. Not polish, features, or copy — the *result*. Without value, every click is a debt the product can't repay.

**Key questions:**
- What problem does this solve?
- How does it change the user's day?
- Could they get the same benefit another way?
- Does the payoff happen immediately, or only over time?
- Would they miss it if it disappeared tomorrow?

**Signals of value slipping:**
- Users complete a task but never return.
- Feedback sounds like "I could do this faster in Excel."
- Engagement spikes week one, collapses week two.
- Customers ask "why does this matter?" instead of "how do I use it?"
- Support tickets circle benefits, not functions.

**Signal types:** Attitudinal (feeling, sentiment, post-task satisfaction), Behavioral (usefulness, engagement, frequency, intent to continue), Performance (helpfulness toward outcomes).

**Example metrics:** Retention before/after release, Intent-to-reuse, NPS, Feature adoption (outcome-driven, not cosmetic), Frequency, Engagement, Post-Task Satisfaction, Helpfulness.

**Validation moves:** Compare retention before/after release. Ask directly: "Would you pay for this if it wasn't included?" Match satisfaction to behavior.

**Common failure mode:** Shipping activity instead of outcomes. Roadmap full, adoption flat, users polite but unmoved.

---

## 7. Desirable

**Definition:** The emotional pull that keeps people coming back. Clarity + craft + character producing a product that feels worth using again. Not decoration — fit and finish in service of the goal.

**Key questions:**
- Does visual design make the task easier, with one clear path to the primary action?
- Does copy sound like a helpful human — calm for errors, warm for success, no hype?
- Are alignment, states (hover/focus/loading/disabled), and components tight and consistent?
- Does motion guide attention and confirm cause/effect, calmly and quickly (under ~500ms)?
- Do microinteractions confirm success meaningfully — what changed, not just "Success"?
- Is the visual system coherent (limited palette, consistent type scale, small icon set)?
- Is personalization light, explained, and reversible?
- Do empty states teach instead of blame, with one starter action?
- Are sensitive moments (payment, data sharing) calmed with clarity cues?
- Are memorable moments tasteful, quick, and tied to the goal?

**Signal types:** Attitudinal (satisfaction, desirability, sentiment, trust), Behavioral (retention, completion, time on task, effort, abandonment).

**Example metrics:** Satisfaction, Desirability, Sentiment, Trust, Retention/Return Rate, Completion Rate, Time on Task, Abandonment Rate, Comprehension.

**Common failure mode:** Functional but flat. Inconsistent states, robotic copy, decorative motion that distracts, generic "Success" toasts. People finish once and don't return.

---

## Quick checklist

1. List your top 3–5 user needs.
2. Locate each on the Honeycomb (Findable → Desirable).
3. Match each to at least one metric.
4. Run a test to capture signals.
5. Share the evidence with your team.
6. Revisit and refine as users evolve.

If you can't list three concrete needs tied to a layer and a metric, you're not done.

## Related key terms

- **UX Honeycomb** — the seven facets of user experience, ordered foundational → aspirational.
- **Needfinding** — Stanford-born practice for surfacing real (not stated) needs.
- **Signal** — a measurable, trustworthy piece of evidence. The unit of credibility in Glare.
- **Want masquerading as a need** — stated importance with no behavioral follow-through.
