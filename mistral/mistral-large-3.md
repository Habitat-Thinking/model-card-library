---
title: mistral-large-3
parent: Mistral
model_name: mistral/mistral-large-3
provider: Mistral
model_version: Mistral Large 3 (v25.12 / 2512)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://docs.mistral.ai/getting-started/models/models_overview/
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.mistral.ai/models/mistral-large-3-25-12
    fetched: 2026-04-30
  - tier: 1
    url: https://mistral.ai/news/mistral-3
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.mistral.ai/capabilities/finetuning/finetuning_overview/
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/collections/mistralai/mistral-large-3
    fetched: 2026-04-30
  - tier: 3
    url: n/a (no dedicated arXiv technical report published for Mistral Large 3 as of 2026-04-30)
    fetched: 2026-04-30
  - tier: 4
    url: https://artificialanalysis.ai/models/mistral-large-3
    fetched: 2026-04-30
---

# Model Card: Mistral/Mistral Large 3

## 1. Model Details

Mistral Large 3 is a state-of-the-art, open-weight, general-purpose multimodal
model released by Mistral AI [T1.1]. The version string is `v25.12` (also
referred to as the "2512" build) [T1.1][T1.2]. The launch announcement names a
release date of December 2, 2025 [T1.2][T1.3]. Architecturally it is a
"granular Mixture-of-Experts" language model with **41B active parameters and
675B total parameters**, paired with a 2.5B vision encoder for the multimodal
configuration [T1.3][T2.1]. Per the provider's published statements, the model
was "trained from the ground up with 3000 H200s" [T1.3][T2.1]. Weights are
released under the Apache 2.0 license [T1.3][T2.1]. Open-weight artifacts are
published on Hugging Face in BF16, FP8, and NVFP4 formats, alongside an EAGLE
speculator variant for speculative decoding [T2.1][T2.2].

## 2. Intended Use

Per the provider's published statements, primary intended uses include
[T2.1][T1.3]:

- Long-document understanding (leveraging the 256k-token context window)
- "Powerful daily-driver AI assistants"
- Agentic / tool-use workflows ("state-of-the-art agentic and tool-use
  capabilities")
- Enterprise knowledge work
- General coding assistance
- Multilingual conversation
- Image-understanding tasks combined with text reasoning

Primary users, per provider framing, are developers and enterprises building
"frontier-capability" applications via Mistral AI Studio, Amazon Bedrock,
Azure Foundry, IBM watsonx, NVIDIA NIM, or self-hosted deployments
[T1.3][T2.1].

Out-of-scope uses called out by the provider [T2.1]:

- Strict reasoning workloads where dedicated reasoning models (e.g.,
  Magistral, Ministral 3 reasoning variants) are recommended over Mistral
  Large 3
- Vision-first tasks where dedicated vision models outperform Mistral
  Large 3
- Resource-constrained or at-scale deployments where the 675B-total-parameter
  footprint is "challenging to deploy efficiently"
- Any use that "infringes, misappropriates, or otherwise violates any third
  party's rights, including intellectual property rights" [T2.1]

## 3. Factors

Relevant subgroups and instrumentation factors are largely **not publicly
available** at the granularity Mitchell et al. recommend. The provider does
disclose:

- **Languages evaluated / supported**: "dozens of languages, including
  English, French, Spanish, German, Italian, Portuguese, Dutch, Chinese,
  Japanese, Korean, Arabic" [T2.1]
- **Modalities**: text input, image input, text output [T2.1][T1.2]
- **Deployment hardware factors**: FP8 weights target B200/H200 nodes;
  NVFP4 weights target H100/A100 nodes; the full model is intended to be
  served from a single multi-GPU node [T2.1]

Disaggregated performance across demographic subgroups, dialects, or
domain-specific cohorts: **Not publicly available**.

## 4. Metrics

Per the provider's published statements [T1.3]:

- **LMArena ranking** (at launch): "#2 in the OSS non-reasoning models
  category (#6 amongst OSS models overall)" [T1.3]
- **General-task quality**: "parity with the best instruction-tuned
  open-weight models" [T1.3]
- **Multilingual conversation**: "best-in-class performance" claim [T1.3]

Independent third-party evaluation [T4.1]:

- **Artificial Analysis Intelligence Index v4.0**: 23 [T4.1]
- **Output throughput**: 46.4 tokens/second [T4.1]
- **Time to first token**: 6.59s [T4.1]

The Hugging Face model card references benchmark comparison charts but the
specific numerical scores are embedded in images rather than text and are not
quoted in the textual model card [T2.1]. No dedicated technical report
disclosing per-benchmark scores (MMLU, GPQA, HumanEval, MATH, MMMU, etc.) has
been published as of 2026-04-30 [T3.1].

## 5. Evaluation Data

Specific evaluation datasets are **not publicly named** in the provider's
model card or release announcement. The Hugging Face card refers generally to
comparisons against "similar sized models" without naming the benchmark
suites used [T2.1]. The launch announcement cites LMArena as one external
leaderboard [T1.3]. Component evaluations underlying the Artificial Analysis
Intelligence Index (a tier-4 source) include GDPval-AA, SciCode, and GPQA
Diamond, but per-component scores for Mistral Large 3 are not broken out
[T4.1]. Beyond these, evaluation-data details are: **Not publicly available**.

## 6. Training Data

Per the provider's published statements, training data composition,
provenance, and filtering procedures are **not publicly available**. The
provider discloses only that the model was "trained from the ground up" using
~3000 NVIDIA H200 GPUs [T1.3][T2.1]. No data-card, dataset list, cutoff date,
or data-filtering description is included in the public model card or
announcement as of 2026-04-30 [T1.2][T1.3][T2.1].

## 7. Quantitative Analyses

Disaggregated performance analyses (by language, by domain, by demographic
subgroup, or by safety category) have **not been publicly released** by the
provider as of 2026-04-30 [T1.2][T1.3][T2.1]. The benchmark comparison
plots in the Hugging Face card show Mistral Large 3 against "similar sized
models" but the underlying tables are not provided in machine-readable form
[T2.1]. No dedicated arXiv technical report exists at this time [T3.1].

## 8. Ethical Considerations

The provider's public statements on risks and mitigations are limited. Stated
considerations [T2.1]:

- **Licensing constraint**: "You must not use this model in a manner that
  infringes, misappropriates, or otherwise violates any third party's rights,
  including intellectual property rights" [T2.1]

Stated limitations that carry ethical/operational implications [T2.1]:

- "Not a dedicated reasoning model" — strict-reasoning use cases are
  better served by dedicated reasoning models
- "Behind vision-first models in multimodal tasks"
- "Complex deployment" at constrained or scaled-up resource levels

Independent or red-team safety evaluation reports, jailbreak resistance
metrics, bias audits, or refusal-rate analyses are **not publicly available**
as of 2026-04-30 [T1.3][T2.1]. No dedicated safety / responsible-AI
technical report accompanies the release [T3.1].

## 9. Caveats and Recommendations

What this card cannot tell you, and why:

- **No dedicated technical report**: Unlike Magistral (arXiv:2506.10910) or
  the broader Mistral research line, Mistral Large 3 was released without an
  accompanying arXiv paper as of 2026-04-30. Per-benchmark numbers, training
  data, ablations, and safety evaluations that would normally live in a
  technical report are absent [T3.1].
- **Benchmark scores are chart-only**: The Hugging Face model card includes
  benchmark comparison charts but no machine-readable scores; the LMArena
  ranking (#2 OSS non-reasoning, #6 OSS overall) is the only quantitative
  claim that the provider states in text [T1.3][T2.1].
- **Knowledge cutoff is undisclosed**: No knowledge-cutoff date is listed in
  any tier-1 source consulted [T1.2][T1.3].
- **Fine-tuning availability is ambiguous**: The Mistral fine-tuning
  documentation page is presently inaccessible (HTTP 404 on the overview URL
  consulted), and the Mistral Large 3 model page does not list fine-tuning
  among its supported capabilities [T1.2]. Treat fine-tuning as
  unconfirmed-via-managed-API; open weights under Apache 2.0 do permit
  self-hosted fine-tuning [T2.1].
- **Tier-1 vs. tier-4 conflicts**: None observed. Independent
  Artificial-Analysis throughput/latency numbers [T4.1] are complementary,
  not contradictory, to provider claims.

Recommendations for use:

- Prefer Mistral Large 3 for long-context (up to 256k tokens) general
  knowledge work, multilingual chat, and tool-using agentic workflows
  [T1.3][T2.1].
- Route hard reasoning workloads (math, multi-step logic, strict chain-of-
  thought benchmarks) to a dedicated reasoning model; the provider explicitly
  flags this limitation [T2.1].
- For production deployments, plan for a multi-GPU node (B200/H200 in FP8 or
  H100/A100 in NVFP4) — single-GPU serving is not in scope [T2.1].
- Treat undocumented attributes (training data, knowledge cutoff,
  per-benchmark scores, safety eval) as unknowns; do not infer them from
  marketing text.

## 10. Operational Details

- **Pricing** (Mistral first-party API, as of 2026-04-30):
  - Input: $0.50 per 1M tokens [T1.2][T4.1]
  - Output: $1.50 per 1M tokens [T1.2][T4.1]
- **Context window**: 256,000 tokens (input + output combined) [T1.2][T2.1]
- **Knowledge cutoff**: Not publicly available [T1.2][T1.3]
- **Supported APIs/SDKs**: Available via Mistral AI Studio (`/v1/chat/
  completions`, `/v1/agents`, `/v1/ocr`, `/v1/fim/completions`,
  `/v1/embeddings`, `/v1/moderations`, `/v1/audio/transcriptions`,
  `/v1/audio/speech`, `/v1/batch`) [T1.2]; also distributed via Amazon
  Bedrock, Azure Foundry, IBM watsonx, OpenRouter, Fireworks, Together AI,
  Modal, and Unsloth, with NVIDIA NIM and AWS SageMaker noted as "coming
  soon" at launch [T1.3]. The Hugging Face card identifier
  `mistral-large-2512+1` appears alongside the model record [T1.2].
- **Latency tier**: Not assigned a named latency tier by the provider; an
  independent measurement reports 6.59s time-to-first-token and ~46.4
  output tokens/second [T4.1].
- **Tool / structured-output support**: Function calling, JSON-structured
  outputs, agent orchestration, and tool-use are supported; the provider
  describes the model as offering "best-in-class agentic capabilities with
  native function calling and JSON outputting" [T2.1][T1.2]. Open-weight
  deployment flags include `--enable-auto-tool-choice` and
  `--tool-call-parser mistral` [T2.1].
- **Function calling**: Supported. Parallel-tool-call support is implied by
  the agent-orchestration framing but not explicitly stated in tier-1
  sources [T2.1][T1.2].
- **Fine-tuning availability**: Not publicly available as a managed Mistral
  API capability per the consulted documentation; the Mistral Large 3 page
  does not list fine-tuning among its capabilities, and the fine-tuning
  overview page returned HTTP 404 at time of research [T1.2]. Self-hosted
  fine-tuning on the open weights is permitted by the Apache 2.0 license
  [T2.1].
- **Rate-limit notes**: Not publicly available in the consulted tier-1
  sources [T1.2].
