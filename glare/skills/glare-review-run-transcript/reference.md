# Run a Transcript — Reference

Compressed source: Glare | Design Review, Run a Transcript v1.3.

## Why run a transcript

Most teams run design reviews, but few have a consistent way to learn from them. After a call, people leave with different versions of:

- what problem was actually discussed
- what success was supposed to mean
- what evidence shaped the direction
- why a decision felt weak
- who owned the next step
- whether anything was truly locked

Running a transcript turns a conversation into something the team can review, score, and improve. The goal is to learn from the conversation, not just react to memory.

## What you need before starting

One design review transcript. Best when it includes:

- speaker names
- the full discussion
- the design problem being reviewed
- any signals, data, or feedback mentioned
- the closing conversation around ownership and next steps

You don't need a perfect transcript. You need enough of the conversation to see how the review moved from problem to action.

## How the transcript is reviewed

Through the SIGNAL flow:

**Surface → Identify → Ground → Navigate → Align → Lock**

| Step | Question |
|---|---|
| Surface | Was the real problem made clear? |
| Identify | Did the group define what success should look like? |
| Ground | Were signals used to shape the discussion? |
| Navigate | Did a clear direction start to form? |
| Align | Was ownership made clear? |
| Lock | Were next steps confirmed? |

The review shows where the conversation created clarity and where it broke down.

## Three ways to run a transcript

### 1. Use the Skill

**Best for fast, repeatable analysis using your AI tool of choice.**

The Skill applies the SIGNAL framework directly on a transcript using AI. It applies the rubric automatically and gives you structured feedback across all six sections.

Use when you want:
- quick analysis
- consistent output
- repeatable results across multiple calls
- a faster way to review design conversations

How to use:
1. Copy your transcript
2. Run the SIGNAL Skill (`glare-review-rubric` in this plugin)
3. Review the output across Surface → Lock
4. Choose one area to improve in the next review

### 2. Use the AI Prompt

**Best for quick learning and understanding.**

The prompt gives you a guided way to run the rubric yourself. It walks through each section step by step.

Use when you want:
- to understand SIGNAL more deeply
- to train your thinking
- to review an important call manually
- to see how the rubric works before using it at scale

How to use:
1. Download the prompt PDF
2. Paste your transcript into your preferred AI tool
3. Follow the structure across each SIGNAL section
4. Review where the conversation gained or lost strength

### 3. Use the Ray Application

**Best for team workflows and ongoing analysis.**

Ray is in the Glare app for uploading transcripts, running SIGNAL analysis, and tracking patterns across calls. Use Ray when you want to review more than one conversation and see where the team keeps getting stuck.

Use when you want:
- team-level insight
- ongoing review of calls
- consistent evaluation across projects
- patterns across multiple design reviews

How to use:
1. Upload your transcript
2. Run the SIGNAL analysis
3. Review patterns and results across calls
4. Use the results to improve future reviews

## What the output should produce

After running a transcript:

- how each SIGNAL step showed up
- where the conversation created clarity
- where the review lost strength
- how decisions formed
- what weak point needs attention next
- what to improve in the next review

Use the output to find where clarity first dropped. That's usually the best place to improve before the next call.

## How to use the results

Look for the step that needs the most help.

| If… | Do this in the next review |
|---|---|
| Surface is weak | Clarify the real problem earlier |
| Identify is weak | Define success before debating the design |
| Ground is weak | Bring stronger signals into the review |
| Navigate is weak | Make tradeoffs and recommendations clearer |
| Align is weak | Confirm who owns the next move |
| Lock is weak | Close with clearer actions and timing |

You don't need every call to be perfect. You need a clear read on where the conversation lost strength and what to improve next.

## How this connects to the rest of Design Review

- **The rubric** (`glare-review-rubric`) shows what to look for.
- **The scoring model** (`glare-review-scoring-model`) shows where the conversation gained or lost strength.
- **The techniques** (`glare-review-techniques` + the six dimension skills) show what to improve next time.
- **The coach** (`glare-review-coach`) turns the result into prep or behavioral change.

Take one real conversation and run it through the system. Find where the flow broke down. Use that step to improve the next review. Over time, this creates clearer conversations, stronger decisions, and design reviews that keep moving forward.
