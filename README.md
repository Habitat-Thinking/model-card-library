# model-card-library

A first-version Mitchell-extended model card library — **13 frontier
LLMs** across Anthropic, OpenAI, Google, Meta, Mistral, xAI, Cohere,
and Alibaba, each documented with per-claim citations and tiered
source provenance.

Seeded on 2026-04-30 with the [`model-cards`](https://github.com/Habitat-Thinking/ai-literacy-superpowers/tree/main/model-cards)
plugin from the [`ai-literacy-superpowers`](https://github.com/Habitat-Thinking/ai-literacy-superpowers)
marketplace.

**📖 Browse the cards online:** <https://habitat-thinking.github.io/model-card-library/>

The site mirrors this repo's contents with searchable navigation,
provider-grouped indexes, and the full About / honesty-rules
explanation. Card sources of truth remain the markdown files in this
repo; the site is regenerated from them on every push to `main` via
the [Pages workflow](.github/workflows/pages.yml).

---

## What's in the library

Cards are organised by provider:

```text
.
├── anthropic/
│   ├── claude-opus-4-7.md
│   ├── claude-sonnet-4-6.md
│   └── claude-haiku-4-5.md
├── openai/
│   ├── gpt-5.md
│   ├── gpt-5-mini.md
│   ├── o4.md
│   └── o4-mini.md
├── google/
│   ├── gemini-2.5-pro.md
│   └── gemini-2.5-flash.md
├── meta/
│   └── llama-4.md
├── mistral/
│   └── mistral-large-3.md
├── xai/
│   └── grok-4.md
├── cohere/
│   └── command-r-plus.md
└── alibaba/
    └── qwen3-coder.md
```

The actual list of cards present is recorded in
[`SEEDING_LOG.md`](SEEDING_LOG.md). Some models in the seed list may
have been **refused** during research because tier-1 (provider docs)
and tier-2 (HuggingFace) were both silent on the model's existence —
the plugin's existence-check rule prevents authoritative-looking
cards for hallucinated models.

---

## Mitchell-extended? What's that?

Each card has **ten sections** — Mitchell et al.'s
[*Model Cards for Model Reporting*](https://arxiv.org/abs/1810.03677)
(2019) nine canonical sections plus a **tenth Operational Details
section** for the consumer-evaluator audience (pricing, context
window, knowledge cutoff, supported APIs/SDKs, function-calling
support, fine-tuning availability, rate limits).

The ten sections:

1. **Model Details** — what the model is
2. **Intended Use** — what it's for
3. **Factors** — subgroups, environmental factors, instrumentation
4. **Metrics** — performance measures the provider reports
5. **Evaluation Data** — datasets used to evaluate
6. **Training Data** — datasets used to train
7. **Quantitative Analyses** — disaggregated performance
8. **Ethical Considerations** — risks, mitigations, failure modes
9. **Caveats and Recommendations** — what the card cannot tell you
10. **Operational Details** — deployment-relevant facts

Sections that came up sparse are filled with `Not publicly available`
rather than fabricated or omitted.

---

## Citation discipline

Every factual claim ends with `[T<n>.<m>]` where:

- `n` is the source tier (1 = provider docs, 2 = HuggingFace,
  3 = arXiv release paper, 4 = web search).
- `m` is the source index within that tier (1, 2, 3, ...).

URLs resolve via each card's frontmatter `sources:` block.

Example:

```text
Knowledge cutoff: January 2026 [T1.1]. Context window: 1M tokens [T1.2].
Pricing: $5/$25 per million tokens (input/output) at standard tier [T1.3].
```

A reader can judge each claim by its tier without re-researching it. A
claim citing `[T1.3]` (provider pricing page) is trustworthy in a
different way than a claim citing `[T4.7]` (independent benchmark
blog post).

---

## Honesty rules at a glance

| Rule | What it means |
| ---- | ------------- |
| **Claim-level "Not publicly available"** | When tier-1 is silent and lower tiers cannot confirm, the canonical answer is `Not publicly available`. The agent never fabricates. |
| **Tier-1 wins on conflict** | If a tier-4 (web) claim conflicts with a tier-1 (provider docs) claim, tier-1 wins. The conflict is recorded in Section 9 (Caveats). |
| **Existence-check refusal** | If tier-1 (provider docs) AND tier-2 (HuggingFace) are both silent on the model's existence, the agent refuses to produce the card. No file is written. This prevents authoritative-looking cards for hallucinated models. |

These rules apply uniformly across the 14 cards in this library.

---

## How this library was generated

The `model-cards` plugin's `/model-card seed` command was run on
2026-04-30 against the shipped seed list of 14 frontier models. For
each model:

1. The `model-card-researcher` agent was dispatched with the model
   name and provider hint.
2. The agent applied the tiered source strategy section-by-section
   (each section's primary tier per the agent's charter).
3. The agent returned either a full card body (frontmatter + 10
   sections) or a `REFUSED:` string when the existence check failed.
4. The dispatcher validated the structure (frontmatter required keys,
   10 canonical section headings, citation resolution, Section 10
   field-level "Not publicly available") and wrote the card.

The agent has only `WebFetch`, `WebSearch`, `Read`, `Glob`, and
`Grep` — no `Write` access. The trust boundary is "research and emit
content"; persistence is the dispatcher's job. This separation
prevents hallucinated claims from landing on disk unreviewed.

---

## How to use this library

**Browse a card** to understand a model's documented profile, sources,
and gaps. Sections marked `Not publicly available` tell you where the
provider has not disclosed.

**Compare cards** by reading them side-by-side. Section 10
(Operational Details) is structured identically across cards, so
pricing, context window, knowledge cutoff, and API support are easy to
diff by eye. The future `/model-card compare <a> <b>` (issue
[#234](https://github.com/Habitat-Thinking/ai-literacy-superpowers/issues/234))
will automate this.

**Re-research a stale card** by cloning this repo and running
`/model-card create <model-name> --provider <provider>` from the
`model-cards` plugin. Choose `load-existing-as-base` when prompted to
preserve the existing card as a starting point.

---

## Refresh cadence

Model providers update their documentation regularly. A card
researched in April 2026 may be out of date by July.

### Scheduled quarterly refresh (automated)

A scheduled remote agent re-researches every card in this library
**quarterly** and opens a PR with the refreshed content for human
review.

- **Schedule**: 09:00 UTC on the 28th of January, April, July, and
  October.
- **Next firing**: **2026-07-28** (then 2026-10-28, 2027-01-28, ...).
- **Routine ID**: `trig_01LAodr397c1waBeo2wfLtSm` (managed at
  <https://claude.ai/code/routines>).
- **What the agent does**:
  1. Walks the repo to inventory existing cards (does **not** rely on
     the upstream seed list, so deprecated entries like the original
     `openai/o4` refusal don't get re-attempted each quarter).
  2. Re-researches each model via the same tiered source strategy
     used at seeding (provider docs → HuggingFace → arXiv → web).
  3. Preserves the same 10-section Mitchell-extended structure,
     citation discipline, and existence-check honesty rule.
  4. Opens a PR titled `refresh: quarterly card refresh YYYY-MM-DD`
     with per-card outcomes summarised.
  5. **Does not merge.** A maintainer reviews and merges manually,
     so any provider-side regression (e.g., a model moving from
     ASL-2 to ASL-3) is seen by a human before it lands on `main`.
- **Cards that disappear** (model retired, renamed, or moved): the
  refresh agent leaves the existing card in place and appends a
  `## Refresh status: REFUSED on YYYY-MM-DD` block under the
  frontmatter, so the historical record is preserved even when a
  model goes away.
- **Operating cost**: re-researching ~13 cards per quarter is the
  default scope. The schedule can be paused or scope adjusted by
  editing the routine in the dashboard.

### Manual refresh (anytime)

You can also refresh on demand without waiting for the quarterly
agent:

- **Per-model** — run `/model-card create <name> --provider <provider>`
  from the `model-cards` plugin with `load-existing-as-base` to
  refresh a single card. Best for spot-checks when a provider has
  just announced a major change.
- **Whole library** — re-run `/model-card seed --force --out .` from
  inside a clone of this repo. The `--force` flag overwrites every
  card; without it, existing cards are skipped.
- **Roadmap** — `/model-card refresh <name>` (issue
  [#235](https://github.com/Habitat-Thinking/ai-literacy-superpowers/issues/235))
  will provide a dedicated non-interactive refresh flow once
  shipped, replacing the `seed --force` pattern with something
  more granular.

---

## Site-specific frontmatter (Jekyll)

Cards in this repo carry **two layers of frontmatter**: the
Mitchell-extended model-card schema (`model_name`, `provider`,
`model_version`, `last_researched`, `card_version`, `researcher`,
`sources`) and a Jekyll-nav key (`title`) used by `just-the-docs` to
render the side-nav entry under the provider parent.

The upstream `model-cards` plugin emits only the model-card schema —
it doesn't know or care about Jekyll. After running
`/model-card create <name>` against this repo, **add `title: <model-name>`
to the new card's frontmatter** before committing, e.g.:

```yaml
---
title: gpt-5.5
model_name: openai/gpt-5.5
provider: OpenAI
...
```

A CI gate enforces this. The validator (also runnable locally) lives at
[`scripts/validate_cards.py`](scripts/validate_cards.py) and runs in
[`.github/workflows/validate-cards.yml`](.github/workflows/validate-cards.yml)
on every PR that touches a card. To check before pushing:

```bash
python3 scripts/validate_cards.py
```

If it fails, the error message tells you exactly which card is missing
which key.

---

## License

This library — the cards, the README, and the seeding log — is
released under the [Apache License 2.0](LICENSE).

The cards quote and cite content from each model provider's
documentation, release papers, and third-party sources. Those source
materials retain their own copyright; citations in the cards point at
the canonical URLs so readers can verify and reuse per the source's
own terms.

---

## See also

- [`model-cards` plugin](https://github.com/Habitat-Thinking/ai-literacy-superpowers/tree/main/model-cards) — the tool that produced this library
- [`model-cards` plugin docs](https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/model-cards/) — tutorials, how-to guides, reference, explanation
- [`ai-literacy-superpowers` marketplace](https://github.com/Habitat-Thinking/ai-literacy-superpowers) — the marketplace shipping this and other plugins
- [Mitchell et al. (2019)](https://arxiv.org/abs/1810.03677) — the original Model Cards paper this library extends
