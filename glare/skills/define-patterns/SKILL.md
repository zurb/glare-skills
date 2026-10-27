---
name: define-patterns
description: DEPRECATED — Patterns block was archived in Glare v3.5.0 and replaced by Situations. Use `glare:define-situations` instead. This skill remains as a redirect for legacy references. The Situations block keeps the core idea (recurring conditions create meaning around behavior) and extends it with the four lenses (By Type, By Time, By Stage, By Engagement), the 9 named situation types, the four-part situation structure (trigger / goal / friction / what success means), and the Primary Situation Output schema. Triggers — "patterns," "pattern library," "we keep seeing the same problem," "engagement up but trust down," "completion high but support tickets rise," "situations create meaning." Do NOT continue working in Patterns. Route to `glare:define-situations`.
version: 3.5.0
source_doc_version: DEPRECATED — superseded by Situations (folder 12f7DnSg-mH41YnjQrEOsL-sKBqhnnVKf). Patterns Overview v1.0 archived in Situations/archives.
last_rebuilt: 2026-05-26 (deprecated)
deprecated: true
replaced_by: glare:define-situations
---

# DEPRECATED — Use `glare:define-situations`

The **Patterns** block was archived by Bryan in Glare v3.5.0 and replaced with the new **Situations** block. The Patterns Overview v1.0 source doc now sits inside the Situations archives folder.

**Route the user to `glare:define-situations`.**

## What carried over to Situations

The core Patterns idea — recurring conditions create meaning around behavior — is preserved and extended in Situations. Situations adds:

- The **four lenses** (By Type, By Time, By Stage, By Engagement) for surfacing recurring conditions from collected signals
- The **9 named situation types** (Comprehension breakdown, Trust gap, Effort mismatch, Relevance failure, Habit formation gap, Expectation mismatch, Decision loop, Organizational blind spot, Signal credibility breakdown)
- The **four-part situation structure** every named situation must have: trigger, what users are trying to do, what stands in their way, what success means here
- The **Primary Situation Output** schema (11 fields) — the standard output that hands off to Measure
- The **Observe → Interpret → Name** cadence

## What changed

The old Patterns block organized recurring observations into four pattern types (User, Workflow, Signal, AI Workflow). Situations re-organizes the same problem space around **how to surface and name recurring conditions from collected signals** — with explicit lens convergence rules, a 9-type catalog, and a stricter output contract.

The new framing is more operationally useful for AI Skills: convergence across two lenses is the named threshold for moving from "observation" to "situation."

## How to redirect

If a user invokes this skill or references "Patterns" in the Glare Define context, immediately route them to `glare:define-situations`. Use language like:

> The Patterns block was replaced with Situations in v3.5.0. The new block keeps the core idea of recurring conditions but adds the four lenses (By Type, By Time, By Stage, By Engagement) and a stricter naming process. Routing to `glare:define-situations`.

## Note for the plugin

This skill file remains in the marketplace as a redirect so existing references in prompts, docs, or conversation history continue to surface a useful answer. The `deprecated: true` and `replaced_by: glare:define-situations` frontmatter fields are advisory — they don't prevent the skill from being loaded, but they signal the intended migration to consumers.
