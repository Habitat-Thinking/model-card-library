# Seeding Log

A record of how this library was first populated.

## Run: 2026-10-28 (quarterly refresh)

**Agent:** `scheduled-quarterly-refresh-agent` (claude-sonnet-4-6).

**Scope:** All 14 cards in the library re-researched against the tiered source
strategy (T1 provider docs → T2 HuggingFace → T3 arXiv → T4 web search).

**Outcome summary:**

| Status | Count |
| ------ | ----- |
| REFUSED (model retired/removed) | 5 |
| Updated (active, content refreshed) | 9 |
| Total | 14 |

**REFUSED cards** (existing body preserved; `## Refresh status: REFUSED on 2026-10-28` block prepended):

| Provider | Model | Reason |
| -------- | ----- | ------ |
| xAI | grok-4 | API endpoint shut down May 15, 2026; replaced by grok-4-7 |
| Google | gemini-2.5-pro | Retired Oct 20, 2026 from Vertex AI; replaced by Gemini 3.x Pro |
| Google | gemini-2.5-flash | Retired Oct 20, 2026 from Vertex AI; deprecated on Developer API; replaced by Gemini 3.x Flash |
| Cohere | command-r-plus | Deprecated March 2026; AWS retired Aug 19, 2026; OCI retired July 30, 2026; replaced by Command A |
| OpenAI | o4-mini | API shut down Oct 23, 2026; replaced by GPT-5 mini |

**Updated cards** (card_version bumped to 0.2.0, body content refreshed):

| Provider | Model | Key changes |
| -------- | ----- | ----------- |
| Anthropic | claude-sonnet-4-6 | Marked legacy; Sonnet 5.5 released Sep 28, 2026; budget_tokens deprecated; retirement not before Feb 17, 2027 |
| Anthropic | claude-haiku-4-5 | Marked legacy; Haiku 5.5 released Oct 7, 2026; retirement not before Oct 15, 2026 |
| Anthropic | claude-opus-4-7 | Marked legacy; Opus 5.5 released Sep 22, 2026; fast mode deprecated Jul 24, 2026 |
| OpenAI | gpt-5 | Snapshot gpt-5-2025-08-07 retiring Dec 11, 2026; replacement gpt-5.6-sol |
| OpenAI | gpt-5.5 | Partially retired from ChatGPT/Codex Oct 14, 2026; API active; replacement gpt-5.6-sol for Codex |
| OpenAI | gpt-5-mini | Strengthened recommendation to evaluate gpt-5.4-mini (2x+ faster, $0.75/$4.50 per MTok) |
| Meta | llama-4 | Note Meta Muse proprietary brand launched mid-2026 (Muse Spark Jun 2026, Muse Glimmer Aug 10, 2026); Llama 4 open-weights remain active |
| Mistral | mistral-large-3 | Active; pricing and status confirmed ($0.50/$1.50 per MTok) |
| Alibaba | qwen3-coder | Qwen3-Coder-Next confirmed released Feb 4, 2026 (80B/3B, Apache 2.0, ~262K context) |

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
