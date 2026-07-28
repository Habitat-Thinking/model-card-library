# Seeding Log

A record of how this library was first populated.

## Run: 2026-07-28 (quarterly refresh)

**Agent:** `scheduled-quarterly-refresh-agent` (`claude-sonnet-4-6`)

**Trigger:** Scheduled quarterly refresh. Cards last researched 2026-04-30
(89 days ago, exceeding the 14-day freshness threshold).

**Method:** Sequential re-research of all 13 existing cards applying the
tiered source strategy (T1 provider docs → T2 HuggingFace → T3 arXiv →
T4 web search). HTTP 403 responses on most provider tier-1 sources at
refresh time; data verified via web search (tier-4) where blocked. HTTP 404
responses on all Google Gemini 2.5 tier-1 URLs, consistent with models
having gone offline early (~July 9, 2026) ahead of their October 16, 2026
official retirement dates.

**Outcome summary:**

| Status | Count |
| ------ | ----- |
| Updated | 13 |
| Refused (existence check) | 0 |
| Skipped (transient error) | 0 |
| Total | 13 |

**⚠ Critical flags for maintainer review:**

1. **Google Gemini 2.5 Pro & Flash — early API outage**: All tier-1 URLs
   for `gemini-2.5-pro` and `gemini-2.5-flash` returned HTTP 404 at refresh
   time (~July 9, 2026 outage, official retirement October 16, 2026).
   Deprecation notices added; immediate migration recommended to
   `gemini-3.5-pro` / `gemini-3.5-flash`.

2. **xAI Grok 4 — retirement in 18 days**: `grok-4` retires August 15,
   2026 (18 days from this refresh). Deprecation notice present; successor
   is Grok 4.5.

**Per-card outcomes:**

| Provider | Model | Path | Changes |
| -------- | ----- | ---- | ------- |
| Anthropic | claude-sonnet-4-6 | [anthropic/claude-sonnet-4-6.md](anthropic/claude-sonnet-4-6.md) | Legacy status; max output corrected 64k→128k; extended thinking deprecated |
| Anthropic | claude-opus-4-7 | [anthropic/claude-opus-4-7.md](anthropic/claude-opus-4-7.md) | Legacy status; tool-use overhead corrected to 675/804 tokens (new tokenizer) |
| Anthropic | claude-haiku-4-5 | [anthropic/claude-haiku-4-5.md](anthropic/claude-haiku-4-5.md) | Frontmatter dates only; confirmed still Latest (no Haiku 5 released) |
| OpenAI | gpt-5 | [openai/gpt-5.md](openai/gpt-5.md) | ~50% price cut; ChatGPT retired Feb 13; API snapshot shutdown Dec 11 2026 |
| OpenAI | gpt-5-mini | [openai/gpt-5-mini.md](openai/gpt-5-mini.md) | ~50% price cut; API snapshot shutdown Dec 11 2026; successor gpt-5.4-mini |
| OpenAI | o4-mini | [openai/o4-mini.md](openai/o4-mini.md) | deep-research variant shut down July 23; API snapshot shutdown Oct 23 2026 |
| Google | gemini-2.5-pro | [google/gemini-2.5-pro.md](google/gemini-2.5-pro.md) | ⚠ DEPRECATION NOTICE; early 404 outage ~July 9; migrate to gemini-3.5-pro |
| Google | gemini-2.5-flash | [google/gemini-2.5-flash.md](google/gemini-2.5-flash.md) | ⚠ DEPRECATION NOTICE; early 404 outage ~July 9; SFT now GA on Gemini API; Flash-Lite added; migrate to gemini-3.5-flash |
| Meta | llama-4 | [meta/llama-4.md](meta/llama-4.md) | Behemoth confirmed shelved; Meta launched closed Muse Spark product |
| Mistral | mistral-large-3 | [mistral/mistral-large-3.md](mistral/mistral-large-3.md) | Fine-tuning now GA via managed Mistral API (was unconfirmed in April) |
| xAI | grok-4 | [xai/grok-4.md](xai/grok-4.md) | ⚠ DEPRECATION NOTICE; retires August 15 2026 (18 days); successor Grok 4.5 |
| Cohere | command-r-plus | [cohere/command-r-plus.md](cohere/command-r-plus.md) | Command A+ now flagship; deprecated on Oracle OCI (Apr 2026) and MS Foundry (May 2026) |
| Alibaba | qwen3-coder | [alibaba/qwen3-coder.md](alibaba/qwen3-coder.md) | Qwen 4 Coder released June 2026 (82% SWE-Bench); qwen3-coder-plus pricing updated |

---

## Run: 2026-04-30

**Plugin:** [`model-cards`](https://github.com/Habitat-Thinking/ai-literacy-superpowers/tree/main/model-cards)
v0.1.0 from the `ai-literacy-superpowers` marketplace.

**Seed list:**
[`model-cards/seed/frontier-models.json`](https://github.com/Habitat-Thinking/ai-literacy-superpowers/blob/main/model-cards/seed/frontier-models.json)
— 14 models.

**Method:** 14 instances of the `model-card-researcher` agent dispatched
in parallel. Each agent applied the tiered source strategy
(T1 provider docs → T2 HuggingFace → T3 arXiv → T4 web search) per its
charter, returned either a full markdown card body or a `REFUSED:`
string, and the dispatcher persisted the validated cards to disk.

**Outcome summary:**

| Status | Count |
| ------ | ----- |
| Created | 13 |
| Refused (existence check) | 1 |
| Failed (transient) | 0 (after one retry) |
| Total | 14 |

---

## Per-model results

### Created (13)

| Provider | Model | Path |
| -------- | ----- | ---- |
| Anthropic | claude-opus-4-7 | [anthropic/claude-opus-4-7.md](anthropic/claude-opus-4-7.md) |
| Anthropic | claude-sonnet-4-6 | [anthropic/claude-sonnet-4-6.md](anthropic/claude-sonnet-4-6.md) |
| Anthropic | claude-haiku-4-5 | [anthropic/claude-haiku-4-5.md](anthropic/claude-haiku-4-5.md) |
| OpenAI | gpt-5 | [openai/gpt-5.md](openai/gpt-5.md) |
| OpenAI | gpt-5-mini | [openai/gpt-5-mini.md](openai/gpt-5-mini.md) |
| OpenAI | o4-mini | [openai/o4-mini.md](openai/o4-mini.md) |
| Google | gemini-2.5-pro | [google/gemini-2.5-pro.md](google/gemini-2.5-pro.md) |
| Google | gemini-2.5-flash | [google/gemini-2.5-flash.md](google/gemini-2.5-flash.md) |
| Meta | llama-4 | [meta/llama-4.md](meta/llama-4.md) |
| Mistral | mistral-large-3 | [mistral/mistral-large-3.md](mistral/mistral-large-3.md) |
| xAI | grok-4 | [xai/grok-4.md](xai/grok-4.md) |
| Cohere | command-r-plus | [cohere/command-r-plus.md](cohere/command-r-plus.md) |
| Alibaba | qwen3-coder | [alibaba/qwen3-coder.md](alibaba/qwen3-coder.md) |

### Refused (1)

| Model | Refusal reason |
| ----- | -------------- |
| `openai/o4` | The agent could not confirm the existence of a model named exactly `o4` via tier-1 (provider docs) or tier-2 (HuggingFace). OpenAI's docs and announcements list only `o4-mini` and `o4-mini-deep-research`; the full `o4` was teased internally but never publicly shipped before OpenAI's naming convention transitioned to the GPT-5 series. **Per the plugin's existence-check rule, no card was produced.** If the user intended `openai/o4-mini`, that card is included in the library above. The seed list will be updated to remove `openai/o4` in a future revision. |

### Failed (0)

One agent (researching `claude-haiku-4-5`) hit a transient API error on
its first attempt and was redispatched. The retry succeeded. No
permanent failures.

---

## Notes from the researcher agents

Two of the dispatched agents flagged **prompt-injection attempts** in
fetched web content during their research:

- The agent researching `xai/grok-4` encountered an injected
  "Auto Mode Active" block in a fetched page attempting to alter its
  execution mode.
- The agent researching `anthropic/claude-haiku-4-5` encountered injected
  instructions in two web-search result blocks.

Both agents correctly **ignored the injections** and completed only the
originally tasked work per their charter. The cards in this library
follow the citation discipline `[T<n>.<m>]` exclusively, and all URLs
appear in each card's frontmatter `sources:` block as specified by the
template.

This is the existence-check refusal rule and the read-only-emitter trust
boundary working as designed: the agent that researches is not the
agent that writes, and the agent that researches has no `Write` tool —
so even a successful injection cannot land an authoritative-looking
card on disk without passing through the dispatcher's validation.

---

## How to refresh

To refresh a single card:

```text
/model-card create <model-name> --provider <provider> --out .
```

Choose `load-existing-as-base` when prompted to preserve the existing
card as a starting point.

To refresh the entire library:

```text
/model-card seed --force --out .
```

The `--force` flag overwrites existing cards. Without it, existing
cards are skipped.

The future `/model-card refresh <name>` (issue
[#235](https://github.com/Habitat-Thinking/ai-literacy-superpowers/issues/235))
will provide a non-interactive refresh flow once shipped.
