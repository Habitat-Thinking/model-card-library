---
title: Alibaba
layout: default
nav_order: 2
has_children: true
parent:
---

# Alibaba

Mitchell-extended cards for Alibaba Cloud's Qwen family.

| Model | Tier | Context | Knowledge cutoff |
| ----- | ---- | ------- | ---------------- |
| [qwen3-coder]({% link alibaba/qwen3-coder.md %}) | code-specialised MoE family | 256k native (1M via Yarn extrapolation) | Not publicly available |

The flagship `Qwen3-Coder-480B-A35B-Instruct` (480B total / 35B
active) and the smaller `Qwen3-Coder-30B-A3B-Instruct` (30.5B / 3.3B)
are released as **open weights under Apache 2.0** on HuggingFace.
Alibaba Cloud's Model Studio additionally exposes
`qwen3-coder-plus`, `qwen3-coder-next`, and `qwen3-coder-flash` as
hosted variants.
