---
title: Cohere
layout: default
nav_order: 4
has_children: true
parent:
---

# Cohere

Mitchell-extended cards for Cohere models.

| Model | Tier | Context | Knowledge cutoff |
| ----- | ---- | ------- | ---------------- |
| [command-r-plus]({% link cohere/command-r-plus.md %}) | RAG + multi-step tool use | 128k input / 4k output | June 1, 2024 |

Open-weights research release on HuggingFace (`c4ai-command-r-plus`)
discloses 104B parameters, auto-regressive transformer with Grouped
Query Attention; CC-BY-NC license — non-commercial only. Cohere now
recommends **Command A** for most modern use cases; Command R+
remains supported with a deprecated `04-2024` variant and a live
`08-2024` variant.
