---
title: Anthropic
layout: default
nav_order: 3
has_children: true
---

# Anthropic

Mitchell-extended cards for Anthropic models in the Claude 4 family.

| Model | Tier | Context | Knowledge cutoff |
| ----- | ---- | ------- | ---------------- |
| [claude-opus-4-7]({% link anthropic/claude-opus-4-7.md %}) | flagship | 1M | January 2026 |
| [claude-sonnet-4-6]({% link anthropic/claude-sonnet-4-6.md %}) | mid-tier | 1M (beta) | August 2025 (reliable) |
| [claude-haiku-4-5]({% link anthropic/claude-haiku-4-5.md %}) | small/fast | 200k (1M on developer platform) | February 2025 (reliable) |

Anthropic does not distribute Claude weights; cards are built from
provider docs (T1) and system card PDFs. No HuggingFace tier-2
sources for these models.
