---
title: Home
layout: default
nav_order: 1
---

# Model Card Library

A first-version Mitchell-extended model card library — **13 frontier
LLMs** across Anthropic, OpenAI, Google, Meta, Mistral, xAI, Cohere,
and Alibaba, each documented with per-claim citations and tiered
source provenance.

{: .fs-6 .fw-300 }

[Browse cards](#cards-by-provider){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[About this library]({% link about.md %}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Cards by provider

The library currently contains **13 cards**. One model from the
seed list (`openai/o4`) was legitimately refused at seeding because
neither tier-1 (provider docs) nor tier-2 (HuggingFace) could confirm
the model exists — see [About]({% link about.md %}) for why this
matters.

### Anthropic

- [claude-opus-4-7]({% link anthropic/claude-opus-4-7.md %}) — flagship reasoning + agentic coding
- [claude-sonnet-4-6]({% link anthropic/claude-sonnet-4-6.md %}) — mid-tier hybrid reasoning, 1M context (beta)
- [claude-haiku-4-5]({% link anthropic/claude-haiku-4-5.md %}) — fast, cost-efficient with extended thinking

### OpenAI

- [gpt-5]({% link openai/gpt-5.md %}) — flagship unified system (router + thinking + main)
- [gpt-5-mini]({% link openai/gpt-5-mini.md %}) — cost-efficient mini variant of the GPT-5 reasoning family
- [o4-mini]({% link openai/o4-mini.md %}) — reasoning model in the o-series; ChatGPT-retired Feb 2026, API-available

### Google

- [gemini-2.5-pro]({% link google/gemini-2.5-pro.md %}) — flagship "thinking" model with 1M context
- [gemini-2.5-flash]({% link google/gemini-2.5-flash.md %}) — price-performance hybrid reasoning model

### Meta

- [llama-4]({% link meta/llama-4.md %}) — Scout / Maverick / Behemoth MoE family, open weights

### Mistral

- [mistral-large-3]({% link mistral/mistral-large-3.md %}) — open-weight MoE (41B active / 675B total), Apache 2.0

### xAI

- [grok-4]({% link xai/grok-4.md %}) — frontier reasoning + tool use, API and consumer surfaces

### Cohere

- [command-r-plus]({% link cohere/command-r-plus.md %}) — RAG + multi-step tool use specialist

### Alibaba

- [qwen3-coder]({% link alibaba/qwen3-coder.md %}) — code-specialised MoE family, agentic coding

---

## At a glance

Every card in this library:

- Follows the **10-section Mitchell-extended structure** (the original 9 sections plus an Operational Details section for pricing, context windows, knowledge cutoffs, supported APIs, and other deployment-relevant facts).
- Carries **per-claim citations** in the form `[T<n>.<m>]` where `n` is the source tier (1 = provider docs, 2 = HuggingFace, 3 = arXiv, 4 = web) and `m` is the index within that tier.
- Resolves every citation via a **frontmatter `sources:` block** so any reader can audit a claim against its original URL.
- Uses **"Not publicly available"** rather than fabrication when a tier-1 source is silent and lower tiers cannot confirm.

The library is **automatically refreshed quarterly** by a scheduled
agent that opens a PR for human review. See
[About]({% link about.md %}) for the schedule and the existence-check
honesty rule that keeps fabricated cards out of the library.
