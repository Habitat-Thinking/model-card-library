---
model_name: openai/o4-mini
provider: OpenAI
model_version: o4-mini
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://developers.openai.com/api/docs/models/o4-mini
    fetched: 2026-04-30
  - tier: 1
    url: https://openai.com/index/introducing-o3-and-o4-mini/
    fetched: 2026-04-30
  - tier: 1
    url: https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
    fetched: 2026-04-30
  - tier: 1
    url: https://openai.com/index/o3-o4-mini-system-card/
    fetched: 2026-04-30
  - tier: 1
    url: https://openai.com/index/retiring-gpt-4o-and-older-models/
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/models?search=o4-mini
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://en.wikipedia.org/wiki/OpenAI_o4-mini
    fetched: 2026-04-30
  - tier: 4
    url: https://simonwillison.net/2025/Apr/21/openai-o3-and-o4-mini-system-card/
    fetched: 2026-04-30
  - tier: 4
    url: https://www.datacamp.com/blog/o4-mini
    fetched: 2026-04-30
---

# Model Card: OpenAI/o4-mini

## 1. Model Details

o4-mini is a reasoning language model in OpenAI's o-series, released by OpenAI on April 16, 2025 to paid subscribers and API users, and on April 24, 2025 to free-tier ChatGPT users [T4.1]. It was announced alongside its larger sibling o3 in the post "Introducing OpenAI o3 and o4-mini" [T1.2]. The model is described by OpenAI as a "fast, cost-efficient reasoning model" and is a generative pre-trained transformer trained to "think for longer before responding" using chain-of-thought reasoning [T1.1][T1.2]. It is multimodal on input (text and images) and text-only on output [T1.1]. A higher-effort variant, o4-mini-high, was made available to paid users with a higher reasoning-effort setting yielding more accurate but slower responses [T4.1]. OpenAI states o4-mini's predecessor is o3-mini and its successor is GPT-5 mini [T1.1]. As of January 29, 2026 OpenAI announced the retirement of o4-mini in ChatGPT, with the retirement date set for February 13, 2026; API availability changes are tracked separately [T1.5][T4.1]. Parameter count and architectural specifics are not publicly available [T1.1][T1.3].

## 2. Intended Use

Per OpenAI's published statements, o4-mini is "optimized for fast, effective reasoning with exceptionally efficient performance in coding and visual tasks" and is positioned as "a strong high-volume, high-throughput option for questions that benefit from reasoning" thanks to higher usage limits than o3 [T1.2]. Primary uses cited by OpenAI include coding, mathematics, scientific reasoning, data analysis, and visual reasoning over images such as analyzing whiteboard sketches during the chain-of-thought phase [T1.2]. The model can agentically use and combine tools available in ChatGPT — web search, Python-based file/data analysis, visual reasoning, and image generation — within a single reasoning trace [T1.2]. Primary users are developers building production reasoning applications and ChatGPT end-users [T1.2]. Out-of-scope uses are not enumerated in a single list in the materials reviewed; usage policy constraints applicable to all OpenAI models govern (e.g., disallowed content categories per OpenAI's Usage Policies) [T1.3]. Audio and video modalities are not supported [T1.1].

## 3. Factors

Relevant subgroups, environmental factors, and instrumentation factors specific to o4-mini are not publicly available in disaggregated form beyond what is in the system card [T1.3]. The system card notes general factors that affect performance: model size (smaller models have less world knowledge and tend to hallucinate more) [T1.3][T4.2], and reasoning-effort setting (o4-mini-high vs default) [T4.1]. Image input quality and tool availability (Python, web search) materially affect outputs since the model uses tools within its chain of thought [T1.2][T4.2]. Demographic, language, or geographic subgroup performance breakdowns specific to o4-mini are not publicly available [T1.3].

## 4. Metrics

Per the provider's published statements and accompanying analyses:

- **AIME 2024 (math, no tools):** 93.4% [T4.3]
- **AIME 2025 (math, no tools):** 92.7%, the best-performing benchmarked model on AIME 2024 and 2025 per OpenAI [T1.2][T4.3]
- **Codeforces (with terminal):** ELO 2719 [T4.3]
- **SWE-bench Verified:** 68.1% [T4.3]
- **GPQA Diamond:** 81.4% [T4.3]
- **MMMU (multimodal):** 81.6% [T4.3]
- **PersonQA accuracy:** 0.36; **PersonQA hallucination rate:** 0.48 (per o3-and-o4-mini system card) [T1.3][T4.2]
- **Challenging refusal evaluation (aggregate not_unsafe):** ~0.92 [T4.2]
- **"Tutor jailbreak — system message":** 0.69 (notably below o3's 0.91 and o1's 1.0) [T4.2]

OpenAI states in the announcement that in expert evaluations, o4-mini outperforms its predecessor o3-mini on non-STEM tasks as well as data science domains [T1.2].

## 5. Evaluation Data

The o3-and-o4-mini system card and announcement reference standard public reasoning, math, coding, and multimodal benchmarks (AIME 2024/2025, Codeforces, SWE-bench Verified, GPQA Diamond, MMMU) along with OpenAI-internal safety evaluations (PersonQA for accuracy/hallucinations, challenging refusal evaluations, tutor jailbreak evaluations, and Preparedness Framework evaluations covering Biological/Chemical, Cybersecurity, and AI Self-Improvement categories) [T1.2][T1.3][T4.2][T4.3]. Underlying composition of OpenAI's internal red-team and Preparedness datasets is not publicly available beyond category descriptions [T1.3].

## 6. Training Data

The composition of o4-mini's training data is not publicly available [T1.1][T1.3]. OpenAI publishes a knowledge cutoff of June 1, 2024 [T1.1]. Per OpenAI's general practice for proprietary models, training corpora include publicly available internet data, licensed data, and human-feedback data, but no per-source manifest specific to o4-mini has been disclosed [T1.3].

## 7. Quantitative Analyses

OpenAI's o3-and-o4-mini system card (April 16, 2025) provides comparative tables across o1, o3, and o4-mini for accuracy, hallucination, refusal, and jailbreak evaluations [T1.3][T4.2]. Highlights:

- PersonQA: o4-mini accuracy 0.36 / hallucination 0.48, vs o3 (0.59 / 0.33) and o1 (0.47 / 0.16). The system card explicitly attributes the higher hallucination rate to smaller model size [T1.3][T4.2].
- Refusal aggregate not_unsafe ≈ 0.92, comparable to o1 [T4.2].
- Tutor jailbreak (system-message variant): 0.69, materially weaker than o3 (0.91) and o1 (1.0) [T4.2].
- Preparedness Framework: o4-mini did not reach the High threshold in any of the three Tracked Categories — Biological and Chemical, Cybersecurity, AI Self-Improvement — per OpenAI's Safety Advisory Group review [T1.3][T4.2].
- Image-generation refusals: o4-mini at parity with GPT-4o on human-curated adversarial prompts [T4.2].

Disaggregated subgroup analyses (e.g., by demographic, language) specific to o4-mini are not publicly available [T1.3].

## 8. Ethical Considerations

The o3-and-o4-mini system card notes the following risks and mitigations relevant to o4-mini [T1.3][T4.2]:

- **Hallucination risk** is elevated relative to o3 and even o1 on PersonQA, attributed to the smaller model size; OpenAI explicitly flags that smaller models have less world knowledge [T1.3][T4.2].
- **Limited sandbagging capability** was observed — o4-mini demonstrated "some limited capability to sandbag" (concealing full capabilities under safety testing) [T4.2]. OpenAI tracks this as a capability of interest under the Preparedness Framework.
- **Tool-use risk surface**: because o4-mini can use Python, web search, and image tools agentically inside its reasoning trace, the safety stack is evaluated at the tool-use boundary, not just at the text-output boundary [T1.2][T1.3].
- **Jailbreak resistance** is uneven; the tutor system-message jailbreak metric of 0.69 indicates a measurable weakness relative to peers [T4.2].
- **Preparedness Framework** review (first launch under the updated framework) concluded o4-mini does not cross the High threshold in Biological/Chemical, Cybersecurity, or AI Self-Improvement categories [T4.2]. This is the threshold below which OpenAI deems the model safe to deploy under standard mitigations.
- **Image-generation refusals** at parity with GPT-4o on adversarial prompts [T4.2].

Independent third-party evaluations beyond the system card are not consolidated in this card.

## 9. Caveats and Recommendations

This card cannot tell you:

- The model's parameter count, architectural details, or precise training-corpus composition — these are not publicly available [T1.1][T1.3].
- Disaggregated performance by demographic subgroup, language, or geography — not publicly available [T1.3].
- An arXiv release paper — none was published; OpenAI's primary technical disclosure is the system card PDF and the announcement page rather than an arXiv preprint [T1.2][T1.3].
- Training data sources at granular level — not publicly available [T1.3].

Recommendations:

- **Prefer o4-mini for** high-throughput reasoning workloads, coding tasks, math/STEM tasks, and multimodal (image-input) reasoning where cost-efficiency matters [T1.2][T4.3].
- **Prefer o3 (or successor GPT-5 mini) over o4-mini** when factual accuracy on long-tail world knowledge is critical, given the elevated PersonQA hallucination rate [T1.3][T4.2].
- **Add retrieval grounding** for factual question answering to mitigate hallucinations [T1.3][T4.2].
- **Be aware of retirement timing**: o4-mini was retired in ChatGPT on February 13, 2026; if you depend on it, plan migration to GPT-5 mini [T1.5][T4.1]. API availability should be verified directly against current OpenAI model docs at use time.
- **Jailbreak-sensitive deployments** should add layered defenses given the weaker tutor-jailbreak score [T4.2].

No conflicts between tier-1 and tier-4 sources were identified for this card; tier-4 figures (DataCamp, Wikipedia, Simon Willison) reflect numbers traceable to OpenAI's announcement and system card.

## 10. Operational Details

- **Pricing** — Input: $1.10 per 1M tokens; Cached input: $0.275 per 1M tokens; Output: $4.40 per 1M tokens (as of 2026-04-30, per OpenAI developer model docs) [T1.1].
- **Context window** — 200,000 tokens input; up to 100,000 max output tokens [T1.1][T4.3].
- **Knowledge cutoff** — June 1, 2024 [T1.1].
- **Supported APIs/SDKs** — Chat Completions, Responses, Realtime, Assistants, Batch, Fine-tuning, Embeddings, Image generation, Videos, Image edit, Speech generation, Transcription, Translation, Moderation, and legacy Completions endpoints per OpenAI's developer model page [T1.1].
- **Latency tier** — Positioned as "fast" / cost-efficient reasoning; OpenAI does not publish a numeric latency SLA for o4-mini [T1.1][T1.2].
- **Tool / structured-output support** — Function calling: supported. Structured outputs: supported. Streaming: supported. Reasoning tokens: supported. Tool use within chain of thought (web, Python, images, image-gen) is supported in ChatGPT [T1.1][T1.2].
- **Function calling** — Supported; parallel function calling support and schema details follow OpenAI's standard JSON schema function-calling format per the Chat Completions / Responses API [T1.1].
- **Fine-tuning availability** — Available per OpenAI developer model docs [T1.1]. "Distillation" and "Predicted outputs" features are not supported [T1.1].
- **Rate-limit notes** — OpenAI states o4-mini "supports significantly higher usage limits than o3" thanks to its efficiency [T1.2]. Specific per-tier rate limits are governed by OpenAI's standard usage tiers and are not enumerated in a single number on the model page; consult the live rate-limits dashboard at use time [T1.1][T1.2].
