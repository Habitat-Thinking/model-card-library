---
model_name: meta/llama-4
provider: Meta
model_version: Llama 4 (Scout 17B-16E, Maverick 17B-128E; Behemoth in preview)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
    fetched: 2026-04-30
  - tier: 1
    url: https://www.llama.com/docs/model-cards-and-prompt-formats/llama4/
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://huggingface.co/blog/llama4-release
    fetched: 2026-04-30
  - tier: 4
    url: https://arxiv.org/abs/2510.12178
    fetched: 2026-04-30
---

# Model Card: Meta/llama-4

## 1. Model Details

Llama 4 is a family of natively multimodal, mixture-of-experts (MoE) language
models released by Meta on April 5, 2025 [T1.1][T2.1]. The family announced at
launch comprises three variants:

- **Llama 4 Scout** — 17B active parameters across 16 experts, 109B total
  parameters; designed to fit on a single NVIDIA H100 GPU with INT4
  quantization [T1.1][T2.1].
- **Llama 4 Maverick** — 17B active parameters across 128 experts, 400B total
  parameters; runs on a single H100 DGX host [T1.1][T2.2].
- **Llama 4 Behemoth** — 288B active parameters across 16 experts, nearly 2T
  total parameters; described by Meta as still training at launch and used
  as a teacher model for distilling the smaller variants [T1.1].

Both Scout and Maverick are auto-regressive language models that use early
fusion to integrate text and image modalities natively [T2.1][T2.2]. Scout
uses a novel iRoPE architecture with interleaved attention layers and no
positional embeddings to enable enhanced length generalisation [T1.1].

Models are released under the **Llama 4 Community License Agreement**, a
custom commercial license effective April 5, 2025 [T2.1].

## 2. Intended Use

Per Meta's published statements [T2.1][T2.2]:

**Primary intended uses:**

- Commercial and research applications in multiple supported languages
- Assistant-like chat and visual reasoning
- Natural language and code generation
- Visual recognition, image reasoning, and captioning
- Synthetic data generation and model distillation
- Powering agentic systems via tool calling [T1.2]

**Primary intended users:** developers and researchers building commercial
or research applications, subject to the Llama 4 Community License [T2.1].

**Out-of-scope uses:**

- Uses violating applicable laws or trade compliance regulations [T2.1]
- Use in languages beyond the 12 supported languages without further
  developer responsibility/testing [T2.1]
- Image understanding beyond 5 input images per request without additional
  testing and tuning [T2.1][T1.2]
- Any use prohibited by Meta's Acceptable Use Policy [T2.1]
- Commercial deployment by entities with 700M+ monthly active users without
  an explicit license from Meta [T2.1]

## 3. Factors

**Languages:** 12 languages officially supported for text — Arabic, English,
French, German, Hindi, Indonesian, Italian, Portuguese, Spanish, Tagalog,
Thai, and Vietnamese [T2.1][T1.2]. Image understanding is **English-only**
per Meta's official documentation [T1.2].

**Modalities:** input is multilingual text + up to 5 images; output is
text-only (multilingual text and code) [T1.2][T2.1].

**Environmental factors / training compute:**

- Scout: 5.0M H100-80GB GPU hours; 1,354 tons CO2eq location-based
  emissions; 0 tons market-based (Meta states 100% renewable energy
  procurement) [T2.1].
- Maverick: 2.38M H100-80GB GPU hours; 645 tons CO2eq location-based; 0
  tons market-based [T2.2].

**Instrumentation factors:** Not publicly available beyond benchmark-suite
descriptions in section 4.

## 4. Metrics

Performance figures published by Meta for instruction-tuned variants
[T2.1][T2.2]:

**Llama 4 Scout (17B-16E-Instruct):**

- MMLU Pro (reasoning): 74.3 [T2.1]
- GPQA Diamond (knowledge): 57.2 [T2.1]
- MMMU (image reasoning): 73.4 [T2.1]
- MMMU Pro: 59.6 [T2.1]
- MathVista (image reasoning): 73.7 [T2.1]
- ChartQA (image understanding): 88.8 [T2.1]
- Pre-trained: MMLU 79.6 (5-shot), MATH 50.3 (4-shot), MBPP 67.8 (3-shot),
  ChartQA 83.4 (0-shot), DocVQA 89.4 (0-shot) [T2.1]

**Llama 4 Maverick (17B-128E-Instruct):**

- MMLU Pro (reasoning): 80.5 macro avg [T2.2]
- GPQA Diamond: 69.8 [T2.2]
- MMMU: 73.4 [T2.2]
- MMMU Pro: 59.6 [T2.2]
- ChartQA (image understanding): 90.0 relaxed accuracy [T2.2]
- DocVQA: 94.4 ANLS [T2.2]
- LiveCodeBench (coding): 43.4 pass@1 [T2.2]
- MGSM (multilingual): 92.3 average exact match [T2.2]
- LMArena (experimental chat version): ELO 1417 [T1.1]

Meta states that Maverick "beats GPT-4o and Gemini 2.0 Flash on broad
benchmarks" and achieves "comparable results to the new DeepSeek v3" on
reasoning and coding at half the active parameters [T1.1]. Scout is stated
to outperform "Gemma 3, Gemini 2.0 Flash-Lite, and Mistral 3.1" across
multiple benchmarks [T1.1]. Behemoth is stated to outperform GPT-4.5,
Claude Sonnet 3.7, and Gemini 2.0 Pro on STEM-focused assessments such as
MATH-500 and GPQA Diamond [T1.1].

## 5. Evaluation Data

Meta names the following evaluation benchmarks in published model cards:
MMLU, MMLU Pro, MATH, MATH-500, MBPP, GPQA Diamond, MMMU, MMMU Pro,
MathVista, ChartQA, DocVQA, LiveCodeBench, MGSM, and LMArena
[T2.1][T2.2][T1.1]. Specific evaluation-set splits, sample counts, or
internal eval-data composition beyond these benchmark names are not
publicly available.

## 6. Training Data

Per Meta's published statements [T1.1][T2.1][T2.2]:

- **Volume:** Over 30 trillion tokens across the family — "more than
  double the Llama 3 pre-training mixture" [T1.1]. Per HuggingFace model
  cards: Scout was pretrained on ~40 trillion tokens; Maverick on ~22
  trillion tokens [T2.1][T2.2][T4.1].
- **Modalities:** text, images, and video [T1.1].
- **Multilinguality:** pre-trained on 200 languages, including over 100
  with 1B+ tokens each — described as "10x more multilingual tokens than
  Llama 3" [T1.1].
- **Sources:** "a mix of publicly available, licensed data and information
  from Meta's products and services," explicitly including "publicly
  shared posts from Instagram and Facebook" and "people's interactions
  with Meta AI" [T2.1][T2.2][T4.1].
- **Knowledge cutoff:** August 2024 [T2.1][T2.2][T1.2].

**Post-training pipeline (Meta-stated):** lightweight supervised
fine-tuning, followed by online reinforcement learning with adaptive
difficulty filtering, then lightweight direct preference optimisation;
for Behemoth, 95% of supervised fine-tuning data was pruned versus 50%
for the smaller models [T1.1].

The full training-data composition (e.g., specific licensed corpora,
weighting, deduplication strategy) is **Not publicly available**.

## 7. Quantitative Analyses

Meta has not published disaggregated per-subgroup benchmark performance
(e.g., by demographic, language sub-group beyond aggregate multilingual
benchmarks, or geographic factor) for Llama 4 in the sources reviewed —
this is **Not publicly available**.

Meta does publish one disaggregated bias measurement: Llama 4 "refuses
less on debated political and social topics overall (from 7% in Llama 3.3
to below 2%)" and shows "dramatically more balanced" refusal patterns
relative to Llama 3.3 [T1.1]. Date of analysis: April 2025 (release).

## 8. Ethical Considerations

Per Meta's published statements [T1.1][T2.1][T2.2]:

**Risk areas explicitly assessed:**

1. **CBRNE proliferation** — chemical, biological, radiological, nuclear,
   and explosive weapons assistance evaluations [T2.1].
2. **Child safety** — data filtering, expert evaluation, multi-image and
   multilingual testing [T2.1].
3. **Cyber-attack enablement** — vulnerability discovery, exploitation,
   and attack-automation testing [T2.1].

**System-level mitigations released alongside the model:**

- **Llama Guard** — input/output safety filtering [T1.1][T2.1].
- **Prompt Guard** — adversarial / jailbreak prompt detection [T1.1].
- **Code Shield** — code-security evaluation [T2.1].
- **CyberSecEval** — cybersecurity risk-assessment suite [T1.1].

**Red-teaming approach:** Meta describes a novel **Generative Offensive
Agent Testing (GOAT)** framework simulating "multi-turn interactions of
medium-skilled adversarial actors" to identify vulnerabilities at scale,
together with recurring adversarial exercises and partnerships with
cybersecurity, ML-adversarial, and multilingual content specialists
[T1.1][T2.1].

**Known failure modes / limitations stated by Meta:**

- Image understanding limited to ≤5 input images without additional
  testing/tuning [T2.1].
- Image understanding evaluated only in English [T1.2].
- Static model with August 2024 knowledge cutoff — no built-in awareness
  of post-cutoff events [T2.1].

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- **No dedicated Meta-authored Llama 4 arXiv release paper** was found
  during research; the survey paper at arXiv:2510.12178 references Llama
  4 but is not the official release paper [T4.2]. Tier-3 is therefore
  effectively unavailable, and tier-1 (Meta blog + llama.com docs) and
  tier-2 (HuggingFace model cards) carry the technical claims.
- Full training-data composition (licensed corpora, weighting,
  deduplication) is not disclosed.
- Disaggregated per-subgroup performance is not published beyond the
  aggregate refusal-rate comparison cited in section 7.

**Conflicts between sources flagged:**

- The HuggingFace blog reports Scout pretraining at "~40 trillion tokens"
  and Maverick at "~22 trillion tokens" [T4.1], which matches the
  HuggingFace model cards [T2.1][T2.2]. Meta's own blog states the family
  uses "over 30 trillion tokens" without breaking out per-variant figures
  [T1.1]. These are not in direct contradiction (the higher Scout figure
  is consistent with "over 30T" at family level), but readers should
  prefer the per-variant model-card figures when citing one specific
  variant.
- The official Meta docs (`llama.com`) state Scout context window as
  10M tokens and Maverick as 1M tokens [T1.2]. The Meta blog and Scout's
  HuggingFace card both state Scout's 10M-token context window
  [T1.1][T2.1]; this is consistent. Use 1M for Maverick and 10M for
  Scout.

**Recommendations:**

- For commercial deployments, consult the Llama 4 Community License
  Agreement directly — the 700M MAU threshold imposes a hard cap that
  affects deployment planning [T2.1].
- For non-English image understanding, treat performance as unverified
  and conduct your own evaluation — Meta restricts image-understanding
  language support to English [T1.2].
- Pair model deployment with the system-level safeguards Meta ships
  alongside (Llama Guard, Prompt Guard, Code Shield) rather than relying
  on the model's tuning alone [T1.1][T2.1].
- Treat the August 2024 knowledge cutoff as a hard limit; augment with
  retrieval for time-sensitive use cases [T2.1].

## 10. Operational Details

- **Pricing** — Not publicly available as a Meta-operated API price.
  Llama 4 is released as open-weights under the Llama 4 Community License
  [T2.1]; pricing depends on the cloud or self-host deployment chosen by
  the user.
- **Context window** —
  - Scout: 10,000,000 tokens [T1.2][T1.1][T2.1]
  - Maverick: 1,000,000 tokens [T1.2][T2.2]
- **Knowledge cutoff** — August 2024 [T2.1][T2.2][T1.2].
- **Supported APIs/SDKs** — HuggingFace `transformers` ≥ v4.51.0
  (`Llama4ForConditionalGeneration` for Maverick; standard text-generation
  pipeline for Scout) [T2.1][T2.2]. Native integration with HuggingFace
  TGI from day one [T4.1]. Cloud-platform availability was described as
  "forthcoming" at launch [T1.1].
- **Latency tier** — Not publicly available as a Meta-stated tier (Meta
  ships open weights, not a tiered API).
- **Tool / structured-output support** — Models support tool-calling and
  are positioned for agentic systems [T1.2]; the official docs include
  function-calling formatting examples in Python and JSON [T1.2].
- **Function calling** — Supported per official model-card-and-prompt-
  formats documentation, with provided special tokens and prompt
  templates [T1.2]. Parallel-call semantics: Not publicly available in
  the documentation reviewed.
- **Fine-tuning availability** — Yes, weights are open under the
  Llama 4 Community License [T2.1]; the survey at arXiv:2510.12178
  describes parameter-efficient fine-tuning approaches for the Llama
  family [T4.2].
- **Rate-limit notes** — Not applicable — Meta distributes weights, not a
  rate-limited API. Rate limits depend on the chosen cloud or self-host
  deployment.
- **Quantization** — BF16 native; FP8 and INT4 quantization options
  available; Scout fits on a single H100 with INT4 [T2.1][T2.2].
