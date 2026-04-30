---
title: About
layout: default
nav_order: 10
---

# About this library

This is a **public reference** of Mitchell-extended model cards for
frontier large language models. It exists to give engineers,
evaluators, and procurement teams a structurally consistent, citable
view of what providers have actually disclosed about their models —
and where they have stayed silent.

The library was first seeded on **2026-04-30** using the
[`model-cards`](https://github.com/Habitat-Thinking/ai-literacy-superpowers/tree/main/model-cards)
plugin from the
[`ai-literacy-superpowers`](https://github.com/Habitat-Thinking/ai-literacy-superpowers)
marketplace, and is **automatically refreshed quarterly** by a
scheduled agent.

---

## What "Mitchell-extended" means

Each card has **ten sections**:

1. **Model Details** — what the model is
2. **Intended Use** — what it's for
3. **Factors** — subgroups, environmental factors, instrumentation
4. **Metrics** — performance measures the provider reports
5. **Evaluation Data** — datasets used to evaluate
6. **Training Data** — datasets used to train
7. **Quantitative Analyses** — disaggregated performance
8. **Ethical Considerations** — risks, mitigations, failure modes
9. **Caveats and Recommendations** — what the card cannot tell you
10. **Operational Details** — pricing, context window, knowledge cutoff, supported APIs/SDKs, latency tier, tool/structured-output support, function calling, fine-tuning availability, rate limits

Sections 1–9 are Mitchell et al.'s original
[*Model Cards for Model Reporting*](https://arxiv.org/abs/1810.03677)
(2019). Section 10 is this library's extension for the
**consumer-evaluator audience** — engineers picking which model to
integrate, evaluators comparing options, procurement making
decisions. Every Section 10 field appears in every card; missing
values are written as `Not publicly available` rather than omitted,
so cards are diff-friendly across providers.

---

## Citation discipline

Every factual claim ends with `[T<n>.<m>]`:

- `n` is the source tier:
  - **T1** — provider docs (most authoritative for what the producer
    claims about their own model)
  - **T2** — HuggingFace (authoritative for open-weight / fine-tuned
    models; secondary for proprietary)
  - **T3** — arXiv release paper (authoritative for training and
    evaluation data)
  - **T4** — web search (independent evaluations, third-party
    benchmarks; valuable for reality-check, lowest tier)
- `m` is the source index within that tier (1, 2, 3, …).

URLs resolve via each card's frontmatter `sources:` block. A reader
can judge each claim by its tier without re-researching it. A claim
citing `[T1.3]` (provider pricing page) is trustworthy in a different
way than a claim citing `[T4.7]` (independent benchmark blog post).

---

## Honesty rules

Three rules govern what does and does not land in this library:

1. **Claim-level "Not publicly available."** When tier-1 is silent and
   lower tiers cannot confirm, the canonical answer is `Not publicly
   available`. The agent never fabricates.

2. **Tier-1 wins on conflict.** If a tier-4 (web) claim conflicts with
   a tier-1 (provider docs) claim, tier-1 wins. The conflict is
   recorded in Section 9 (Caveats), not resolved by majority vote.

3. **Existence-check refusal.** If tier-1 (provider docs) AND tier-2
   (HuggingFace) are both silent on the model's existence, the agent
   refuses to produce the card. **No file is written.** This rule
   prevents authoritative-looking cards for hallucinated or
   non-existent models.

The third rule is the most consequential. LLMs hallucinate model
names: ask about `gpt-7-ultra-pro` and you'll get plausible details
("OpenAI's most advanced reasoning model, released in 2027, with a
5M token context window…") for a model that doesn't exist. If the
plugin produced cards for hallucinated models, those cards would
inherit the structural authority of every other card in the library
and a reader would have no signal that one was fabricated. The
existence check breaks that loop.

This is why the library has **13 cards** rather than 14: the seed
list contained `openai/o4`, but neither OpenAI's docs nor HuggingFace
list a model with that exact name (only `o4-mini` and
`o4-mini-deep-research`). The agent refused, no card was written,
and `o4-mini` is in the library instead.

---

## Quarterly refresh

A scheduled remote agent re-researches every card in this library
quarterly and opens a PR for human review.

| Field | Value |
| ----- | ----- |
| Cron | `0 9 28 1,4,7,10 *` (09:00 UTC on the 28th of Jan/Apr/Jul/Oct) |
| Next firing | **2026-07-28** |
| Routine ID | `trig_01LAodr397c1waBeo2wfLtSm` |
| Output | A PR titled `refresh: quarterly card refresh YYYY-MM-DD` |

The agent **does not merge.** A maintainer reviews each refresh PR
before it lands on `main`, so any provider-side regression (e.g., a
model moving from ASL-2 to ASL-3) is caught by a human before it
overwrites the prior card.

If a model is **retired, renamed, or moved** between refreshes
(tier-1 + tier-2 both silent on it at refresh time), the agent does
**not** overwrite the existing card. Instead it appends a
`## Refresh status: REFUSED on YYYY-MM-DD` block under the
frontmatter, preserving the historical record of what was last true.
Cards become time-capsules rather than disappearing.

The full refresh history lives in the repo's
[`SEEDING_LOG.md`](https://github.com/Habitat-Thinking/model-card-library/blob/main/SEEDING_LOG.md).

---

## How to use this library

**Browse a card** to understand a model's documented profile,
sources, and gaps. Sections marked `Not publicly available` tell you
where the provider has not disclosed.

**Compare cards** by reading them side-by-side. Section 10
(Operational Details) is structured identically across cards, so
pricing, context window, knowledge cutoff, and API support are easy
to diff by eye.

**Cite this library in your own work.** Every claim in every card
points at a URL in the frontmatter `sources:` block — you can pull
the original source and cite it directly, treating this library as a
provenance-aware index rather than a primary source.

**Refresh on demand.** If a card looks stale or a provider has just
shipped major changes, you can either wait for the next quarterly
refresh or run the plugin's `/model-card create <name> --provider <provider>`
manually with `load-existing-as-base`. See the
[plugin docs](https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/model-cards/)
for the full flow.

---

## License

The library — the cards, this site, and the seeding log — is
released under the [Apache License 2.0](https://github.com/Habitat-Thinking/model-card-library/blob/main/LICENSE).

The cards quote and cite content from each model provider's
documentation, release papers, and third-party sources. Those source
materials retain their own copyright; citations in the cards point
at canonical URLs so readers can verify and reuse per the source's
own terms.

---

## Related

- [`model-cards` plugin](https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/model-cards/) — the tool that produced this library
- [`ai-literacy-superpowers` marketplace](https://github.com/Habitat-Thinking/ai-literacy-superpowers) — the marketplace shipping this and other plugins
- [Mitchell et al. (2019)](https://arxiv.org/abs/1810.03677) — the original Model Cards paper
- [Library repository](https://github.com/Habitat-Thinking/model-card-library) — source, history, and refresh log
