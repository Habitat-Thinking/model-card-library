---
title: gemini-2.5-pro
model_name: google/gemini-2.5-pro
provider: Google
model_version: gemini-2.5-pro
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/models
    fetched: 2026-04-30
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro
    fetched: 2026-04-30
  - tier: 1
    url: https://ai.google.dev/gemini-api/docs/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/
    fetched: 2026-04-30
  - tier: 2
    url: n/a
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/abs/2507.06261
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/html/2507.06261v1
    fetched: 2026-04-30
  - tier: 4
    url: https://en.wikipedia.org/wiki/Gemini_(language_model)
    fetched: 2026-04-30
  - tier: 4
    url: https://techcrunch.com/2025/05/06/google-debuts-an-updated-gemini-2-5-pro-ai-model-ahead-of-i-o/
    fetched: 2026-04-30
---

# Model Card: Google/gemini-2.5-pro

## 1. Model Details

Gemini 2.5 Pro is Google DeepMind's flagship "thinking" model in the Gemini
2.5 family, described by the provider as "our state-of-the-art thinking
model, capable of reasoning over complex problems in code, math, and STEM,
as well as analyzing large datasets, codebases, and documents using long
context" [T1.2]. The model identifier is `gemini-2.5-pro` and the release
stage is Stable [T1.2].

The Gemini 2.5 family is described in the Google DeepMind technical report
"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality,
Long Context, and Next Generation Agentic Capabilities" (arXiv:2507.06261)
[T3.1]. The 2.X series is built to be natively multimodal, with long
context support over 1 million tokens and native tool use [T3.1].

Release timeline:

- Gemini 2.5 Pro Experimental was first released on 25 March 2025 [T1.4].
- An updated "I/O edition" preview was announced on 6 May 2025 [T4.2].
- General Availability was reached in June 2025; the docs report a "latest
  update" of June 2025 [T1.2][T4.2].

Parameter count and architecture: Not publicly available. Google has not
published parameter counts for Gemini 2.5 Pro [T4.1], and the technical
report's architecture section does not disclose them in extracted content
[T3.1].

## 2. Intended Use

**Primary uses (per provider):** Complex reasoning tasks in code, math,
and STEM; analysis of large datasets, codebases, and long documents using
long context [T1.2]. Agentic code tasks (the provider cites a 63.8% score
on SWE-Bench Verified at launch) and multimodal applications including
text, audio, images, video, and PDF inputs [T1.2][T1.4].

**Primary users (per provider):** Developers and enterprises building on
Google AI Studio, the Gemini API, and Vertex AI [T1.4][T4.2].

**Out-of-scope uses:** The provider lists `Live API`, image generation, and
audio generation as not supported by `gemini-2.5-pro` [T1.2]; users
needing those modalities should select a different Gemini variant. Google
has not published an explicit out-of-scope list beyond unsupported
features; consult Google's published Acceptable Use / Generative AI
Prohibited Use Policy for restricted applications. Not publicly available
in this card's sources.

## 3. Factors

**Relevant subgroups:** Not publicly available. The technical report
extract reviewed does not include disaggregated subgroup performance
breakdowns [T3.1].

**Languages:** The Gemini 2.X series is described as natively multimodal
across text, audio, images, video, and code [T3.1]; specific
language-coverage tables were not visible in the extracted report content
[T3.1].

**Environmental factors:** Not publicly available in tier-1 or extracted
tier-3 sources.

**Instrumentation factors:** Per the provider, the model supports both
short-prompt (≤ 200k tokens) and long-prompt (> 200k tokens) operating
regimes which differ in price [T1.3], implying instrumentation choice
(prompt size) materially affects cost-per-call.

## 4. Metrics

The provider's launch announcement reports:

- **Humanity's Last Exam:** 18.8% (Gemini 2.5 Pro at launch, no tool use)
  [T1.4].
- **SWE-Bench Verified (agentic code):** 63.8% [T1.4].

The arXiv technical report (2507.06261) describes the family as achieving
"state-of-the-art performance on frontier coding and reasoning benchmarks"
[T3.1]; specific per-benchmark numbers from the report body were not
extractable from the HTML render reviewed [T3.2].

LMArena: At experimental launch, Gemini 2.5 Pro debuted at #1 on LMArena
by a significant margin, and the I/O-edition preview ranked #1 on LMArena
in Coding and #1 on the WebDev Arena Leaderboard [T4.2].

## 5. Evaluation Data

The technical report references "frontier coding and reasoning benchmarks"
and reports a knowledge cutoff of January 2025 for the 2.5 family [T3.1].
Specific evaluation dataset names cited at launch by the provider include
Humanity's Last Exam and SWE-Bench Verified [T1.4]. A full enumeration of
evaluation datasets in the technical report was not visible in the
extracted HTML content reviewed [T3.1][T3.2]. Beyond what is named here,
the comprehensive evaluation dataset list is: Not publicly available in
the extracts reviewed.

## 6. Training Data

Not publicly available. The technical report's "Model Architecture,
Training and Dataset" section is referenced but the actual content was
not visible in the HTML extracts reviewed [T3.1][T3.2]. Wikipedia notes
that Google has not published whitepapers with detailed architecture or
training-data disclosures for Gemini 2.0, 2.5, or 3 [T4.1]; this conflicts
with the existence of the arXiv 2.5 report (see Section 9).

The provider-stated **knowledge cutoff** is **January 2025** [T1.2][T3.1].

## 7. Quantitative Analyses

Per the technical report: "The Gemini 2.5 family of models maintain robust
safety metrics while improving dramatically on helpfulness and general
tone" [T3.1]. The report further states that Gemini 2.5 Pro "showed a
significant increase in some capabilities compared to previous Gemini
models, [but] it did not reach any of the Critical Capability Levels in
any area" — covering CBRN, cybersecurity, ML R&D, and deceptive alignment
[T3.1]. Disaggregated tables (e.g. by language, demographic subgroup) were
not visible in the extracts reviewed [T3.1]: Not publicly available in
this card's sources.

## 8. Ethical Considerations

**Frontier-risk evaluation (per release paper):** Google evaluated
Gemini 2.5 Pro against Critical Capability Levels in CBRN, cybersecurity,
ML R&D, and deceptive alignment, and reports that the model did not reach
any Critical Capability Level in any area despite capability gains over
prior Gemini models [T3.1].

**Safety vs. helpfulness:** The report claims robust safety metrics were
maintained while improving helpfulness and tone [T3.1].

**Known failure modes / specific risk taxonomy:** Detailed failure-mode
taxonomies were not visible in the extracts reviewed [T3.1]. Not publicly
available in this card's sources beyond the high-level Critical Capability
Level statement.

**Independent evaluations / red-team disclosures:** Not surfaced in the
sources reviewed for this card [T4.1].

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- Parameter count, architecture (e.g. dense vs. Mixture-of-Experts), and
  exact training-data composition for Gemini 2.5 Pro are not disclosed in
  the sources reviewed [T3.1][T4.1].
- Comprehensive benchmark tables from the technical report body were not
  extractable from the HTML render reviewed; only headline numbers from
  the launch blog (Humanity's Last Exam 18.8%, SWE-Bench Verified 63.8%)
  and arXiv abstract claims of SoTA are cited [T1.4][T3.1].
- Disaggregated performance (by language, subgroup, etc.) was not visible
  in the extracts reviewed [T3.1].

**Recorded conflict (T1/T3 vs. T4):** Wikipedia's Gemini article states
"No whitepapers were published for Gemini 2.0, 2.5, and 3" [T4.1]. This
conflicts with the existence of the arXiv 2.5 technical report
(2507.06261) [T3.1]. Per honesty rules, tier-1/tier-3 wins: a public
arXiv technical report exists, even if it is less detailed than earlier
Gemini whitepapers.

**Recommendations:**

- Use Gemini 2.5 Pro for tasks where its documented strengths apply: long
  context (up to ~1M input tokens), multimodal input across audio/image/
  video/PDF/text, and reasoning/coding workloads [T1.2][T3.1].
- For audio output, image generation, or low-latency live-streaming use
  cases, choose a different Gemini variant — these are explicitly
  unsupported by `gemini-2.5-pro` [T1.2].
- Budget around the two-tier prompt-size pricing: short prompts
  (≤ 200k tokens) are materially cheaper per token than long prompts
  (> 200k tokens) [T1.3].
- Treat the reported safety claims (no Critical Capability Levels reached)
  as the provider's own evaluation; supplement with independent red-team
  evidence before deploying in high-stakes settings [T3.1].

## 10. Operational Details

- **Pricing** (as-of date: docs fetched 2026-04-30) [T1.3]:
  - Input: $1.25 / 1M tokens for prompts ≤ 200k tokens; $2.50 / 1M tokens
    for prompts > 200k tokens [T1.3].
  - Output: $10.00 / 1M tokens for prompts ≤ 200k tokens; $15.00 / 1M
    tokens for prompts > 200k tokens [T1.3].
  - Context caching: $0.125 / 1M tokens (≤ 200k) and $0.25 / 1M tokens
    (> 200k); storage $4.50 / 1M tokens per hour [T1.3].
  - Free tier: not available for `gemini-2.5-pro` — paid tier required
    [T1.3].
- **Context window:** 1,048,576 input tokens; 65,536 output tokens
  [T1.2]. The launch announcement noted a 1M-token window with "2 million
  coming soon" [T1.4]; current docs reflect ~1M [T1.2].
- **Knowledge cutoff:** January 2025 [T1.2][T3.1].
- **Supported APIs/SDKs:** Google Gemini API (Google AI Studio) and
  Vertex AI; Google's published language SDKs for Gemini [T1.4][T4.2].
  OpenAI Chat Completions compatibility: Not publicly available in the
  sources reviewed for this card.
- **Latency tier:** The provider exposes Flex inference and Priority
  inference modes for `gemini-2.5-pro` [T1.2]; a discrete "latency tier"
  label is not publicly stated in the docs reviewed.
- **Tool / structured-output support:** Function calling, code execution,
  structured outputs, search grounding, Google Maps grounding, URL
  context, and file search are all listed as supported [T1.2].
- **Function calling:** Supported [T1.2]. Parallel function calling and
  schema-format details: Not publicly available in the docs page reviewed.
- **Thinking / reasoning mode:** Supported (the model is described by the
  provider as a "thinking model") [T1.2][T1.4].
- **Caching:** Supported (context caching, with separate pricing) [T1.2]
  [T1.3].
- **Batch API:** Supported [T1.2].
- **Live API:** Not supported [T1.2].
- **Image generation / audio generation:** Not supported by
  `gemini-2.5-pro` [T1.2].
- **Fine-tuning availability:** Not listed as supported on the
  `gemini-2.5-pro` model page [T1.2]. A dedicated tuning entry is absent
  from the supported-features list reviewed; treat as Not publicly
  available / not supported pending confirmation from the Vertex AI tuning
  docs.
- **Rate-limit notes:** Not publicly available in the model page reviewed
  [T1.2]; consult the Gemini API rate-limits page for tier-specific
  quotas.
