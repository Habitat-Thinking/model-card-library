---
title: Google
layout: default
nav_order: 5
has_children: true
parent:
---

# Google

Mitchell-extended cards for Google DeepMind's Gemini 2.5 family.

| Model | Tier | Context | Knowledge cutoff |
| ----- | ---- | ------- | ---------------- |
| [gemini-2.5-pro]({% link google/gemini-2.5-pro.md %}) | flagship "thinking" model | 1,048,576 | January 2025 |
| [gemini-2.5-flash]({% link google/gemini-2.5-flash.md %}) | hybrid reasoning, price-performance | 1,048,576 | January 2025 |

Both models are sparse mixture-of-experts transformers with native
multimodal support. Architecture and parameter count are not
publicly disclosed. The Gemini 2.5 family has a published technical
report at [arXiv:2507.06261](https://arxiv.org/abs/2507.06261).
