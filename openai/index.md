---
title: OpenAI
layout: default
nav_order: 8
has_children: true
parent:
---

# OpenAI

Mitchell-extended cards for OpenAI models.

| Model | Tier | Context | Knowledge cutoff |
| ----- | ---- | ------- | ---------------- |
| [gpt-5.5]({% link openai/gpt-5.5.md %}) | next-gen frontier (Apr 2026), `gpt-5.5` + `gpt-5.5-pro` | 1.05M | December 1, 2025 |
| [gpt-5]({% link openai/gpt-5.md %}) | flagship unified system | 400k | September 30, 2024 |
| [gpt-5-mini]({% link openai/gpt-5-mini.md %}) | mini reasoning variant | 400k | May 31, 2024 |
| [o4-mini]({% link openai/o4-mini.md %}) | o-series reasoning, fast/cost-efficient | 200k | June 1, 2024 |

The seed list also included `openai/o4`, which the existence-check
rule **refused** because neither the OpenAI docs nor HuggingFace
confirm a full `o4` model exists — only `o4-mini` and
`o4-mini-deep-research`. See [About]({% link about.md %}#honesty-rules)
for why this matters.
