---
model_name: cohere/command-r-plus
provider: Cohere
model_version: command-r-plus-08-2024 (latest live); command-r-plus-04-2024 (original, deprecated 2025-09-15)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://docs.cohere.com/docs/command-r-plus
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.cohere.com/docs/models
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.cohere.com/docs/responsible-use
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.cohere.com/docs/rate-limits
    fetched: 2026-04-30
  - tier: 1
    url: https://cohere.com/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://cohere.com/blog/command-r-plus-microsoft-azure
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.cohere.com/changelog/commandr-082024-ft
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/CohereForAI/c4ai-command-r-plus
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/CohereLabs/c4ai-command-r-plus-08-2024
    fetched: 2026-04-30
  - tier: 3
    url: n/a (no dedicated Command R+ release paper on arXiv; arXiv 2404.06654 is RULER, unrelated)
    fetched: 2026-04-30
  - tier: 4
    url: https://docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-command-r-plus-08-2024.htm
    fetched: 2026-04-30
---

# Model Card: Cohere/command-r-plus

## 1. Model Details

Command R+ is a large language model released by Cohere and Cohere Labs, optimised for conversational interaction, long-context tasks, retrieval-augmented generation (RAG), and multi-step tool use [T1.1][T2.1]. The original release (`command-r-plus-04-2024`) was announced on April 4, 2024, first available on Microsoft Azure [T1.6]. An updated version, `command-r-plus-08-2024`, was released in August 2024 and delivers "roughly 50% higher throughput and 25% lower latencies" relative to the predecessor on the same hardware, alongside improved tool-use decisions and instruction-following [T1.1].

The open-weights research release on Hugging Face (`c4ai-command-r-plus`) discloses **104 billion parameters**, an **auto-regressive transformer** architecture, and **Grouped Query Attention (GQA)** for inference efficiency [T2.1][T2.2]. Inputs and outputs are text-only [T2.1]. Training combined Supervised Fine-Tuning (SFT) with preference training aligned to human preferences [T2.1].

API model identifiers per Cohere docs: `command-r-plus-08-2024` (live), `command-r-plus-04-2024` (deprecated September 15, 2025), and the alias `command-r-plus` (deprecated September 15, 2025) [T1.2]. Cross-platform identifiers include `cohere.command-r-plus-v1:0` on Amazon Bedrock and `cohere.command-r-plus v1.2` on Oracle OCI [T1.2][T4.1].

## 2. Intended Use

Per Cohere's published statements, Command R+ is designed for "complex RAG workflows and multi-step tool use" and is recommended for sophisticated enterprise applications requiring advanced retrieval and agent-based reasoning [T1.1]. The Cohere docs note that **Command A** is now recommended for most modern use cases, positioning Command R+ as a still-supported but no-longer-flagship enterprise model [T1.1].

Primary intended uses (per provider): conversational AI, retrieval-augmented generation with citations, single-step and multi-step tool/function calling, multilingual applications, code interaction (explanation and rewriting), reasoning, summarisation, and question answering [T1.1][T2.1][T2.2].

Out-of-scope uses (per Cohere's responsible-use guidance): high-impact individual decisions in financial services, employment, or housing; astroturfing; generation of misinformation to manipulate public opinion; consequential decisions about people without human oversight [T1.3]. The Hugging Face release is licensed CC-BY-NC and additionally requires adherence to Cohere Lab's Acceptable Use Policy — the open weights are explicitly **not for commercial use** [T2.1].

## 3. Factors

**Language coverage as an instrumentation factor.** The model is *optimised and evaluated* in 10 languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Arabic, and Simplified Chinese [T2.2]. An additional 13 languages are present in pre-training data: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, and Persian [T2.2]. Cohere's responsible-use docs explicitly warn that performance "degrades" in those 13 languages and is "unreliable in unlisted languages" [T1.3].

**Subgroup factors.** Cohere's responsible-use page states that Command R+ "tends to display slightly less bias than Command R" across measured categories (evaluated on the BOLD dataset, ~24,000 prompts), but does not publish disaggregated subgroup performance numbers per demographic factor [T1.3]. Detailed disaggregation is **not publicly available**.

**Environmental / deployment factors.** Available via Cohere's Chat API, Amazon Bedrock, Azure AI Foundry, and Oracle OCI [T1.2]. Hardware requirements for self-hosting the open-weights variant are not enumerated in the model card beyond a note that quantised 4-bit and 8-bit variants exist [T2.1].

## 4. Metrics

Per the Hugging Face model card (T2.1), Command R+ scores on the Open LLM Leaderboard (zero-shot averaged across the standard suite) [T2.1]:

| Metric | Score |
| --- | --- |
| Average | 74.6 |
| ARC (Challenge) | 70.99 |
| HellaSwag | 88.6 |
| MMLU | 75.7 |
| TruthfulQA | 56.3 |
| Winogrande | 85.4 |
| GSM8k | 70.7 |

Cohere notes explicitly that "these metrics don't capture RAG, multilingual, or tooling performance where the model is considered state-of-the-art" — i.e. the published headline numbers under-represent the model's intended-use strengths [T2.1].

**Safety metric:** Evaluated on the BOLD dataset (~24,000 prompts) for bias; Cohere reports Command R+ exhibits "slightly less bias than Command R" but does not publish numeric scores in the responsible-use page [T1.3].

**Throughput / latency metric (08-2024 update):** ~50% higher throughput and ~25% lower latency vs. the 04-2024 release on identical hardware [T1.1]. No absolute tokens/sec figure published.

## 5. Evaluation Data

The Open LLM Leaderboard suite — ARC, HellaSwag, MMLU, TruthfulQA, Winogrande, GSM8k — is named explicitly on the Hugging Face card [T2.1]. The BOLD dataset is named for bias evaluation [T1.3]. Multilingual evaluation covers the 10 optimised languages listed in §3 [T2.2].

Beyond these named benchmarks, **dataset-level details for RAG, tool-use, and multilingual evaluations are not publicly available** — Cohere has not released an arXiv paper for Command R+ specifically (per Tier-3 search; arXiv 2404.06654 returned by search is the unrelated RULER benchmark paper) [T3.1].

## 6. Training Data

Training methodology disclosed: Supervised Fine-Tuning (SFT) followed by preference training aligned to human preferences [T2.1][T2.2]. Pre-training data is described only at the language-coverage level (the 23 languages enumerated in §3) [T2.2]. **Specific corpora, dataset sources, dataset sizes, token counts, and data-filtering procedures are not publicly available.** Cohere's responsible-use docs note that the model "learns from diverse internet sources," with the implied risks of toxic or biased content ingestion [T1.3].

Knowledge cutoff (per Cohere docs for `command-r-plus-08-2024`): training data through February 2023, with a stated knowledge cutoff date of June 1, 2024 [T1.1]. The discrepancy between "training data through Feb 2023" and "knowledge cutoff June 1, 2024" is reproduced verbatim from the Cohere docs page; reconciliation is not given there.

## 7. Quantitative Analyses

Disaggregated performance is **not publicly available** at the level Mitchell et al. recommend (per-subgroup, per-factor breakdowns). The publicly reported numbers (§4) are aggregate Open LLM Leaderboard scores and a qualitative bias comparison between Command R+ and Command R on BOLD [T1.3][T2.1]. There is no published evaluation paper for Command R+ providing per-language, per-subgroup, or per-task disaggregation comparable to a release paper [T3.1].

The 08-2024 update has not been re-benchmarked against the Open LLM Leaderboard in the publicly visible model card; the scores in §4 are from the original 04-2024 open-weights release [T2.1].

## 8. Ethical Considerations

**Documented risks (per Cohere's responsible-use docs):** Command R+ "can generate toxic content" since it learns from diverse internet sources; developers should be "especially attuned to risks presented by toxic degeneration and the reinforcement of historical social biases," particularly in extended multi-turn conversations [T1.3]. Toxic output may include obscenities, explicit content, and harmful stereotyping [T1.3].

**Bias evaluation:** BOLD dataset (~24,000 prompts) used; Command R+ reported as showing slightly less bias than Command R [T1.3]. Numeric BOLD scores are not published in the responsible-use page.

**Mitigations disclosed:**

- Safeguards built into the model to limit harmful outputs (unspecified mechanism) [T1.3]
- "Safety modes" with granular output control exposed at the API level [T1.1]
- Citations / grounded generation, which Cohere positions as a hallucination-reduction mechanism for RAG workflows [T1.1][T2.1]
- A `directly_answer` built-in tool for tool-use workflows, allowing the model to abstain from invoking external tools when appropriate [T2.1]

**Prohibited uses (per Cohere):** high-impact individual decisions (financial services, employment, housing); astroturfing; misinformation generation; consequential decisions about people without human oversight [T1.3].

**Independent paper-level evaluation:** No dedicated Command R+ release paper exists on arXiv [T3.1], so independent third-party evaluation is sparse in the academic literature relative to peer flagship models from Anthropic, OpenAI, and Google.

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- Detailed training corpora, dataset sizes, token counts, or data-filtering procedures (not publicly available — common for proprietary frontier models).
- Per-subgroup disaggregated performance (no release paper; only aggregate leaderboard scores).
- Per-language quantitative performance numbers (only "optimised in 10, degraded in 13" qualitative framing).
- Numeric BOLD bias scores (only a qualitative comparison vs. Command R).
- Whether the 08-2024 update has been re-benchmarked against Open LLM Leaderboard (publicly visible scores are for the 04-2024 release).

**Conflicts between sources:**

- Cohere docs state "training data through February 2023" and "knowledge cutoff June 1, 2024" on the same page [T1.1]. These are not internally reconciled; a reader should treat the cutoff conservatively.
- Tier-1 docs (`https://docs.cohere.com/docs/command-r-plus`) report pricing as $2.50/1M input and $10.00/1M output for the 08-2024 model expressed as "$2.50 per 1K input tokens" — that wording in the doc page appears to be a units error (the pricing page T1.5 confirms $2.50/1M and $10.00/1M). T1.5 (the dedicated pricing page) wins on this conflict.

**Recommendations for use:**

- Strong fit: enterprise RAG with citations, multi-step agentic tool use, multilingual chat in the 10 optimised languages, code interaction (low temperature recommended).
- Weaker fit: long-tail languages outside the 23 trained languages; high-stakes individual decisions (explicitly prohibited by Cohere); domains requiring per-subgroup fairness guarantees (no published disaggregation).
- Migration note: the alias `command-r-plus` and `command-r-plus-04-2024` were deprecated September 15, 2025 [T1.2]. Production users should pin `command-r-plus-08-2024` explicitly; for new builds, Cohere now recommends Command A for most modern use cases [T1.1].
- For self-hosting: use the Hugging Face release `CohereLabs/c4ai-command-r-plus-08-2024`; note CC-BY-NC license — non-commercial only [T2.1][T2.2].

## 10. Operational Details

- **Pricing (as of 2026-04-30):** `command-r-plus-08-2024` — $2.50 / 1M input tokens, $10.00 / 1M output tokens. `command-r-plus-04-2024` (deprecated) — $3.00 / 1M input, $15.00 / 1M output [T1.5].
- **Context window:** 128,000 tokens input; 4,000 tokens maximum output (both 04-2024 and 08-2024 variants) [T1.1][T1.2].
- **Knowledge cutoff:** Cohere docs list June 1, 2024 (with a separate statement that training data goes through February 2023; see §9 caveat) [T1.1].
- **Supported APIs/SDKs:** Cohere Chat endpoint (native API); Amazon Bedrock (`cohere.command-r-plus-v1:0`); Azure AI Foundry; Oracle OCI Generative AI (`cohere.command-r-plus v1.2`) [T1.2][T4.1]. Cohere provides Python, TypeScript, Java, and Go SDKs (per Cohere docs site nav). OpenAI Chat Completions compatibility: not publicly available as a documented surface.
- **Latency tier:** No formal latency tier published; Cohere reports the 08-2024 update achieves ~25% lower latency than the 04-2024 release on identical hardware [T1.1].
- **Tool / structured-output support:** Single-step tool use (function calling) with JSON action lists; multi-step tool use (Action → Observation → Reflection cycles for agents); a built-in `directly_answer` tool for abstaining; structured outputs supported [T1.1][T2.1][T2.2].
- **Function calling:** Supported. Multi-step tool use supported. Parallel tool calling: not explicitly documented in the publicly visible Cohere docs (treat as not publicly confirmed). Schema format: JSON-formatted action lists per the HF model card [T2.2].
- **Fine-tuning availability:** Fine-tuning was announced for **Command R 08-2024** (LoRA-based, with MultiLoRA and 16,384-token training context) [T1.7]. Fine-tuning for Command R+ specifically is **not publicly confirmed** in the Cohere docs surveyed; treat as not available unless Cohere documentation states otherwise [T1.7].
- **Rate-limit notes (Chat endpoint):** Trial tier: 20 req/min. Production tier: 500 req/min. Higher production limits available via sales contact [T1.4].
