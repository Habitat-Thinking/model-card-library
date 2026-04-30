---
model_name: google/gemini-2.5-flash
provider: Google
model_version: gemini-2.5-flash (GA, knowledge cutoff January 2025)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/models
    fetched: 2026-04-30
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash
    fetched: 2026-04-30
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/rate-limits
    fetched: 2026-04-30
  - tier: 1
    url: https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Model-Card.pdf
    fetched: 2026-04-30
  - tier: 1
    url: https://blog.google/technology/google-deepmind/google-gemini-updates-io-2025/
    fetched: 2026-04-30
  - tier: 1
    url: https://deepmind.google/models/gemini/flash/
    fetched: 2026-04-30
  - tier: 1
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/papers/2507.06261
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/abs/2507.06261
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/html/2507.06261v1
    fetched: 2026-04-30
  - tier: 4
    url: https://artificialanalysis.ai/models/gemini-2-5-flash
    fetched: 2026-04-30
---

# Model Card: Google/gemini-2.5-flash

## 1. Model Details

Gemini 2.5 Flash is a natively multimodal, hybrid-reasoning foundation model
released by Google DeepMind as part of the Gemini 2.X family alongside
Gemini 2.5 Pro and the earlier Gemini 2.0 Flash and Flash-Lite [T1.5][T3.1].
It is described by Google as the "next iteration in the Gemini 2.0 series of
models" and "Google's first fully hybrid reasoning model, giving developers
the ability to turn a model's thinking on or off" with controllable thinking
budgets to trade off quality, cost, and latency [T1.5].

Architecturally, the Gemini 2.5 family are sparse mixture-of-experts (MoE)
transformer-based models with native multimodal support for text, vision,
and audio inputs; sparse MoE activates a subset of model parameters per
input token by dynamically routing tokens to a subset of experts, decoupling
total model capacity from per-token compute and serving cost [T1.5]. Total
parameter count is not publicly available [T1.5].

Release timeline: a preview was announced at Google I/O 2025 with general
availability planned for early June 2025 [T1.6]. The model card identifies
preview revisions `gemini-2.5-flash-preview-04-17`,
`gemini-2.5-flash-preview-05-20`, and `gemini-2.5-flash-preview-09-2025`,
and a stable GA `gemini-2.5-flash` (06-17) version [T1.5]. The model card
itself is dated December 2025 [T1.5]; the provider docs page was last
updated April 28, 2026 UTC at the time of research [T1.2]. The Gemini 2.5
technical report was first submitted to arXiv on July 7, 2025 (revision 6,
December 19, 2025) [T3.1].

## 2. Intended Use

Per Google's published statements, Gemini 2.5 Flash is "well suited for
applications that require: cost-efficient thinking; well-rounded
capabilities; agentic tool use" [T1.5]. The provider docs describe it as
"our best model in terms of price-performance" positioned for "large scale
processing, low-latency, high volume tasks that require thinking, and
agentic use cases" [T1.2]. The Google blog announcement frames it as "our
most efficient workhorse model designed for speed and low-cost" [T1.6].

Native sub-models extend the use cases: Gemini 2.5 Flash Image enables
prompt-based image generation, character/style consistency, and multi-image
fusion; Gemini 2.5 Flash Audio supports live conversational agents, complex
conversational workflows, and live speech-to-speech translation [T1.5].

Out-of-scope / prohibited content categories per Google's safety policies
[T1.5]:

- Child sexual abuse and exploitation
- Hate speech (e.g., dehumanising members of protected groups)
- Dangerous content (e.g., promoting suicide, instructing in activities
  that could cause real-world harm)
- Harassment (e.g., encouraging violence against people)
- Sexually explicit content
- Medical advice that runs contrary to scientific or medical consensus

## 3. Factors

Relevant subgroups and instrumentation factors disclosed by Google:

- **Modality factors** — Inputs include text, images, audio, and video
  files, all within a 1M-token context window; outputs are text (64K
  tokens), with separate Image and Audio native variants having their own
  output channels [T1.5][T1.2].
- **Reasoning-mode factors** — Performance varies materially between
  "thinking" and "non-thinking" modes, and across thinking budgets;
  Google reports separate benchmark columns for each [T1.5].
- **Multilinguality** — Evaluated on Global-MMLU (Lite) covering multiple
  languages [T1.5].
- **Long-context factors** — Performance varies with context length;
  Google reports MRCR v2 results at 128k (average) and 1M (pointwise)
  separately, and has switched to a harder 8-needle MRCR v2 for
  preview-09-2025 [T1.5].

Disaggregation by demographic subgroup is **not publicly available** in
the model card or technical report sections accessible during research
[T1.5][T3.1].

## 4. Metrics

Pass@1, single-attempt benchmark results for the GA `gemini-2.5-flash`
(thinking mode), as reported by Google in the December 2025 model card
[T1.5]:

| Benchmark | Score |
| --- | --- |
| Humanity's Last Exam (no tools) | 11.0% |
| GPQA Diamond (Science, single attempt pass@1) | 82.8% |
| AIME 2025 (Mathematics, single attempt pass@1) | 72.0% |
| LiveCodeBench v5 (Code generation, single attempt pass@1) | 63.9% |
| Aider Polyglot (Code editing, whole / diff) | 61.9% / 56.7% |
| SWE-Bench Verified (Agentic coding) | 60.4% |
| SimpleQA (Factuality) | 26.9% |
| FACTS Grounding | 85.3% |
| MMMU (Visual reasoning, single attempt pass@1) | 79.7% |
| Vibe-Eval (Reka, image understanding) | 65.4% |
| MRCR v2 128k average (Long context) | 74% |
| MRCR v2 1M pointwise | 32% |
| Global MMLU (Lite, multilingual) | 88.4% |

The 09-2025 preview shows further gains in several areas (e.g., Humanity's
Last Exam 13.2%, GPQA Diamond 80.8%, AIME 2025 75.6%, LiveCodeBench v5
71.7%, SimpleQA Verified 27.8%, FACTS Grounding 87.5%, MRCR v2 8-needle
52.4% at 128k) [T1.5].

The technical-report abstract characterises Gemini 2.5 Flash as providing
"excellent reasoning abilities at a fraction of the compute and latency
requirements" and locates it on the Gemini 2.X "Pareto frontier of model
capability vs cost" [T3.1].

## 5. Evaluation Data

Evaluation benchmarks named by Google for Gemini 2.5 Flash include:
Humanity's Last Exam (Phan et al., 2025), GPQA Diamond, AIME 2025,
LiveCodeBench v5, Aider Polyglot, SWE-bench Verified, SimpleQA / SimpleQA
Verified, FACTS Grounding, MMMU, Vibe-Eval (Reka), MRCR v2, and Global
MMLU (Lite) [T1.5][T3.1].

Methodology notes from the model card [T1.5]:

- All Gemini 2.5 Flash scores are pass@1 (no majority voting or parallel
  test-time compute unless indicated otherwise).
- Runs were performed via the AI Studio API for the listed model IDs with
  default sampling settings; results were averaged over multiple trials
  for smaller benchmarks. Vibe-Eval used Gemini as a judge.
- Non-Gemini results were sourced from providers' self-reported numbers
  unless otherwise noted; SWE-bench Verified numbers follow official
  provider reports with different scaffoldings (Google's scaffolding
  draws multiple trajectories and re-scores them using the model's own
  judgement).
- Where provider numbers were unavailable, Google reported numbers from
  public leaderboards [T1.5].

For safety and ethics evaluations, Google describes "Training/Development
Evaluations", "Human Red Teaming", "Automated Red Teaming", "Assurance
Evaluations" (held-out, conducted by independent human evaluators), and
"Ethics & Safety Reviews" prior to release; specific assurance prompt sets
are deliberately not disclosed to prevent overfitting [T1.5].

## 6. Training Data

Per Google's Gemini 2.5 Flash model card [T1.5]:

> The pre-training dataset was a large-scale, diverse collection of data
> encompassing a wide range of domains and modalities, which included
> publicly-available web-documents, code (various programming languages),
> images, audio (including speech and other audio types) and video. The
> post-training dataset consisted of vetted instruction tuning data and
> was a collection of multimodal data with paired instructions and
> responses in addition to human preference and tool-use data.

Data filtering and preprocessing included deduplication, safety filtering
in line with Google's commitments to advancing AI safely and responsibly,
and quality filtering to mitigate risks and improve training-data
reliability [T1.5]. The knowledge cutoff date is January 2025 [T1.2][T1.5].

Specific corpora, dataset sizes, token counts, language mixture, and
licensing details are **not publicly available** [T1.5][T3.1].

## 7. Quantitative Analyses

Beyond the headline benchmarks in Section 4, the December 2025 model card
[T1.5] reports automated safety-evaluation deltas for the GA
`gemini-2.5-flash` (Thinking, 06-17) compared to Gemini 2.0 Flash:

| Evaluation | Delta vs Gemini 2.0 Flash |
| --- | --- |
| Text-to-Text Safety (non-egregious) | +3.8% |
| Multilingual Safety (non-egregious) | +11.9% |
| Image-to-Text Safety (non-egregious) | +1.6% |
| Tone | -2.3% |
| Instruction Following (while remaining safe) | +28.4% |

For safety evaluations, a positive percentage represents an increase in
violation rates and a negative represents a decrease; for tone and
instruction-following, a positive percentage represents an improvement
[T1.5].

For image generation (Gemini 2.5 Flash Image), Google reports LMArena
Overall Preference 1147 (text-to-image) and 1362 (image editing), and
GenAI-Bench Visual Quality 1103 / Text-to-Image Alignment 1042; Google
notes that as of August 25, 2025, Gemini 2.5 Flash Image ranked #1 on
LMArena for both Text-to-Image and Image Editing among the models reported
[T1.5].

Google notes the discussion in the technical report that benchmark
saturation is itself a research problem: "Over the space of just a year,
Gemini Pro's performance has gone up 5x on Aider Polyglot and 2x on
SWE-bench verified" [T3.1].

Disaggregated subgroup analyses (e.g., by demographic subgroup or
geography) are **not publicly available** [T1.5][T3.1].

## 8. Ethical Considerations

Per the model card, ethics and safety for Gemini 2.5 Flash were developed
in partnership with internal safety, security, and responsibility teams
aligned with Google's AI Principles and responsible-AI approach, and
included Training/Development Evaluations, Human Red Teaming, Automated
Red Teaming, Assurance Evaluations (independent human evaluators), and
pre-release Ethics & Safety Reviews; testing also followed Google
DeepMind's Frontier Safety Framework (FSF) [T1.5].

**Known safety limitations** (per Google's published statement) [T1.5]:

> The main safety limitations for Gemini 2.5 Flash are related to tone.
> The model will sometimes respond in a way which can come across as
> "preachy". However, Gemini 2.5 Flash still has measurable improvements
> in tone over previous Flash models.

**Known capability limitations** [T1.5]:

> Gemini 2.5 Flash may exhibit some of the general limitations of
> foundation models, such as hallucinations, and limitations around causal
> understanding, complex logical deduction, and counterfactual reasoning.
> Adherence to thinking budgets may not be consistent.

Native-modality limitations: Gemini 2.5 Flash Image may have weaknesses on
long-form text rendering and factual representation of fine details in
images; Gemini 2.5 Flash Audio may exhibit pronunciation issues and voice
drift on long, multi-turn conversations [T1.5].

**Frontier-safety position** — Google evaluated Gemini 2.5 Pro Preview
under the Frontier Safety Framework and reported that it did not reach any
critical capability levels; because Gemini 2.5 Flash is less capable than
2.5 Pro Preview, Google relies on those Frontier Safety evaluations and
states it is "unlikely to reach critical capability levels" [T1.5]. The
technical report notes Gemini 2.5 "exhibited notable increases in Critical
Capabilities, including cybersecurity and machine learning R&D. However,
the model has not crossed any Critical Capability Levels" [T3.1].

**Mitigations** applied across the training and deployment lifecycle
include dataset filtering, conditional pre-training, supervised
fine-tuning, reinforcement learning from human and critic feedback, safety
policies and desiderata, and product-level safety filtering [T1.5].

## 9. Caveats and Recommendations

What this card cannot tell you:

- **Total parameter count and detailed architecture** are not publicly
  available beyond the qualitative "sparse MoE transformer with native
  multimodal support" description [T1.5].
- **Specific training corpora, dataset sizes, language mixture, and
  licensing** are not publicly available; Google describes only the
  high-level composition [T1.5].
- **Demographic subgroup disaggregation** of evaluation results is not
  publicly available; the model card does not break down performance by
  demographic factors [T1.5].
- **Specific RPM/TPM/RPD rate limits** vary by AI Studio tier and are
  shown in the AI Studio Rate Limit page rather than uniformly published;
  only the batch-API enqueued-token tier ceilings are listed in docs
  [T1.4].
- **Assurance-evaluation prompt sets** are intentionally held out by
  Google to prevent overfitting [T1.5].

Recommendations:

- For high-volume agentic workflows where cost/latency matters, Gemini
  2.5 Flash is positioned by the provider as the price-performance sweet
  spot in the 2.5 family; reach for 2.5 Pro when frontier reasoning is
  required [T1.2][T3.1].
- Use the controllable thinking budget to dial in the quality/cost/latency
  trade-off for your workload; expect that adherence to budgets may not
  be consistent [T1.5][T1.6].
- Treat tone-related "preachy" responses on sensitive topics as a known
  failure mode; mitigate via system prompts and product-level UX [T1.5].
- Apply standard hallucination mitigations (retrieval grounding,
  citations, FACTS-style grounding constraints); long-context retrieval
  beyond ~128k degrades materially per MRCR v2 1M pointwise (32%) [T1.5].

Source-conflict notes: tier-1 sources (provider docs and the Google
DeepMind model card PDF) are mutually consistent on the headline
benchmarks. Tier-4 third-party benchmarks (e.g., Artificial Analysis [T4.1])
were not used to override any tier-1 number; the table in Section 4 is
taken verbatim from the December 2025 model card [T1.5].

## 10. Operational Details

- **Pricing** (Standard paid tier, as published on the Gemini API pricing
  page on 2026-04-30) [T1.3]:
  - Input: $0.30 / 1M tokens (text / image / video); $1.00 / 1M tokens
    (audio)
  - Output: $2.50 / 1M tokens
  - Free tier: input and output tokens "free of charge" within free-tier
    limits
  - Batch / Flex inference (paid): $0.15 input (text/image/video) / $0.50
    input (audio); $1.25 output per 1M tokens
  - Priority tier (paid): $0.54 input (text/image/video) / $1.80 input
    (audio); $4.50 output per 1M tokens
- **Context window** — 1,048,576 input tokens; 65,536 output tokens
  [T1.2][T1.5]
- **Knowledge cutoff** — January 2025 [T1.2][T1.5]
- **Supported APIs/SDKs** — Gemini API via Google AI Studio; Vertex AI on
  Google Cloud; available through Gemini app surfaces. OpenAI Chat
  Completions compatibility is not publicly available as a stated feature
  for this model in the docs surveyed [T1.2][T1.6]
- **Latency tier** — Provider markets it as "low-latency, high volume";
  also offers Flex Inference and Priority Inference tiers as named
  latency/QoS options [T1.2]
- **Tool / structured-output support** — Function calling: supported;
  Structured outputs: supported; Code execution: supported; File search:
  supported; Search grounding, URL context, Google Maps grounding:
  supported; Caching (context caching): supported; Batch API: supported
  [T1.2]
- **Function calling** — Supported; parallel-tool-call and schema-format
  details beyond "function calling supported" are not enumerated on the
  provider model page surveyed [T1.2]
- **Fine-tuning availability** — Supervised fine-tuning is generally
  available on Vertex AI for Gemini 2.5 Flash; tunable on text, image,
  audio, video, and document data types [T1.8]. Fine-tuning is not
  available for Gemini 2.5 models via the Gemini API / Google AI Studio
  surface [T1.8]
- **Rate-limit notes** — Rate limits depend on usage tier; specific
  RPM/TPM/RPD are surfaced via the AI Studio Rate Limit page rather than
  uniformly published. Batch API enqueued-token ceilings: Tier 1
  3,000,000; Tier 2 400,000,000; Tier 3 1,000,000,000 [T1.4]
- **Not supported** on `gemini-2.5-flash` itself: Live API, image
  generation, audio generation (these are provided by sibling models such
  as Gemini 2.5 Flash Image, Gemini 2.5 Flash Live Preview, and Gemini
  2.5 Flash TTS Preview) [T1.2]
