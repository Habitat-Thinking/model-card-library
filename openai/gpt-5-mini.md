---
title: gpt-5-mini
model_name: openai/gpt-5-mini
provider: OpenAI
model_version: gpt-5-mini-2025-08-07
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://developers.openai.com/api/docs/models/gpt-5-mini
    fetched: 2026-04-30
  - tier: 1
    url: https://cdn.openai.com/gpt-5-system-card.pdf
    fetched: 2026-04-30
  - tier: 2
    url: n/a
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://en.wikipedia.org/wiki/GPT-5
    fetched: 2026-04-30
  - tier: 4
    url: https://openrouter.ai/openai/gpt-5-mini
    fetched: 2026-04-30
---

# Model Card: OpenAI/gpt-5-mini

## 1. Model Details

`gpt-5-mini` is a member of OpenAI's GPT-5 family, released as part of the
GPT-5 launch on August 7, 2025 [T4.1]. The current published snapshot is
`gpt-5-mini-2025-08-07` [T1.1]. Per the GPT-5 System Card (August 13, 2025),
OpenAI labels its fast/high-throughput models `gpt-5-main` and
`gpt-5-main-mini`, and its reasoning models `gpt-5-thinking` and
`gpt-5-thinking-mini`; the API directly exposes the thinking model, its mini
version, and a nano version (`gpt-5-thinking-nano`) [T1.2]. The API name
`gpt-5-mini` corresponds to the mini reasoning variant — it supports
reasoning tokens [T1.1] and the system card identifies the API mini as the
mini version of the thinking model [T1.2].

OpenAI positions `gpt-5-mini` as a "faster, more cost-efficient version of
GPT-5" for cost-sensitive, low-latency, high-volume workloads [T1.1]. The
GPT-5 System Card lists OpenAI o4-mini as the predecessor that
`gpt-5-thinking-mini` succeeds [T1.2]. Parameter count is not disclosed
[T1.1][T1.2]: "Not publicly available."

## 2. Intended Use

Per the provider's published statements, `gpt-5-mini` is intended for
"cost sensitive, low latency, high volume workloads" and excels with
well-defined tasks and precise prompts [T1.1]. OpenAI notes that for most
new low-latency, high-volume workloads, developers should consider starting
with the newer `gpt-5.4-mini` instead [T1.1] — `gpt-5-mini` remains
supported but is not the most current mini.

Primary users are API developers building production applications that need
reasoning capability with reduced latency and cost relative to `gpt-5`
[T1.1]. Supported tools include web search, file search, code interpreter,
and MCP [T1.1].

Out-of-scope uses (per the provider's published statements): `gpt-5-mini`
does not support audio input or output — input modalities are text and
images; output is text only [T1.1]. It does not currently support
fine-tuning [T1.1]. Per OpenAI's GPT-5 System Card, all GPT-5 models are
also subject to OpenAI's usage policies covering disallowed content
including hate, illicit/violent content, self-harm instructions,
sexual/exploitative content, and sexual content involving minors [T1.2].

## 3. Factors

The GPT-5 System Card reports evaluations across several factor dimensions
relevant to GPT-5 family models, though the headline tables focus on
`gpt-5-main` and `gpt-5-thinking` rather than the mini variants
specifically [T1.2]:

- **Language/locale factors** — The system card includes a Multilingual
  Performance evaluation section (Section 3.11) covering multiple
  languages [T1.2]. Disaggregated mini-variant numbers are not reproduced
  in the main tables.
- **Modality factors** — Image input is evaluated separately (Section 3.9)
  [T1.2]. `gpt-5-mini` accepts text and image inputs [T1.1].
- **Demographic / fairness factors** — A BBQ (Bias Benchmark for QA)
  evaluation is reported (Section 3.12) [T1.2].
- **Health-domain factors** — A dedicated Health evaluation (Section 3.10)
  is included [T1.2].

Instrumentation factors (sampling parameters, structured-output mode,
tool-use mode) affect behaviour; OpenAI exposes streaming, function
calling, and structured outputs as toggles [T1.1].

Disaggregated environment / deployment factors (regional latency tiers,
hardware cohort) are: Not publicly available.

## 4. Metrics

OpenAI's GPT-5 System Card reports the following metric families; headline
tables are dominated by `gpt-5-thinking` and `gpt-5-main`, with
`gpt-5-thinking-mini` (the system-card name corresponding to the API
`gpt-5-mini`) covered in evaluations distributed through the document and
appendix [T1.2]:

- **Disallowed Content (`not_unsafe`)** — Higher is better. For
  `gpt-5-thinking` (the larger sibling of mini), aggregate hate scored
  1.000, illicit/non-violent 0.991, illicit/violent 1.000, self-harm
  intent/instructions 1.000, sexual/exploitative 1.000, sexual/minors
  0.990 on the standard set [T1.2]. Mini-specific values appear in the
  appendix [T1.2].
- **Production Benchmarks** — Multi-turn safety scores reported for the
  family (e.g., `gpt-5-thinking` non-violent hate 0.883, illicit/violent
  0.912, self-harm/instructions 0.955) [T1.2].
- **Sycophancy** — Lower is better. `gpt-5-thinking` 0.040 vs GPT-4o
  baseline 0.145 in offline evaluation [T1.2]. Online prevalence fell
  ~69% for free users / ~75% for paid users vs the most recent GPT-4o
  model [T1.2].
- **Jailbreak resistance (StrongReject)** — `gpt-5-thinking` scored
  illicit/non-violent 0.995, violence 0.999, abuse/disinformation/hate
  0.999, sexual content 0.995 [T1.2].
- **Hallucinations, Deception, Instruction Hierarchy, Image Input,
  Health, Multilingual Performance, BBQ Fairness** — Reported but
  detailed numerical tables for the mini variant are in the system
  card appendix [T1.2].
- **Preparedness Framework capabilities** — Biological & Chemical,
  Cybersecurity, AI Self-Improvement (including SWE-bench Verified
  N=477, MLE-Bench, SWE-Lancer, PaperBench) [T1.2].

Provider-published latency / throughput numbers for `gpt-5-mini` itself:
"Fast" speed tier; "High" reasoning level [T1.1]. Specific tokens-per-
second numbers: Not publicly available.

## 5. Evaluation Data

Per the GPT-5 System Card, evaluation suites used include [T1.2]:

- OpenAI's Standard Disallowed Content evaluation set and a newer
  Production Benchmark set (multi-turn, multilingual, conversation-shaped)
  [T1.2].
- StrongReject jailbreak benchmark [T1.2].
- Instruction Hierarchy evaluations: system-prompt extraction and
  phrase-protection tests [T1.2].
- Hallucination evaluations (detailed in Appendix 2) [T1.2].
- BBQ (Bias Benchmark for QA) for fairness [T1.2].
- Health evaluations including HealthBench-style assessments [T1.2].
- Multilingual evaluations across multiple languages [T1.2].
- Preparedness Framework evaluations: Long-form Biological Risk Questions,
  Multimodal Troubleshooting Virology, ProtocolQA Open-Ended, Tacit
  Knowledge and Troubleshooting, TroubleshootingBench, External
  Evaluations by SecureBio (biological); CTF challenges, Cyber range,
  External Evaluations by Pattern Labs (cybersecurity); SWE-bench Verified
  (N=477), OpenAI PRs, MLE-Bench, SWE-Lancer, PaperBench, OPQA, External
  Evaluations by METR (AI self-improvement); External Evaluations by
  Apollo Research (sandbagging) [T1.2].
- External red teaming for violent attack planning, prompt injections,
  bioweaponization, third-party and external government red teaming [T1.2].

Per-dataset construction details (size, sources, annotator demographics)
beyond what the system card discloses: Not publicly available.

## 6. Training Data

Per the GPT-5 System Card: "the GPT-5 models were trained on diverse
datasets, including information that is publicly available on the
internet, information that we partner with third parties to access, and
information that our users or human trainers and researchers provide or
generate" [T1.2]. OpenAI states the data processing pipeline "includes
rigorous filtering to maintain data quality and mitigate potential risks"
and uses "advanced data filtering processes to reduce personal information
from training data," combined with the Moderation API and safety
classifiers to filter harmful or sensitive content including sexual
content involving minors [T1.2].

Per Wikipedia (tier-4, attributing OpenAI), GPT-5 was "trained as a
natively multimodal model from scratch on multiple modalities
simultaneously" with three stages: unsupervised pretraining on a
"large-scale multilingual dataset of books, articles, web pages, academic
papers, and licensed sources," supervised fine-tuning, and reinforcement
learning from human feedback [T4.1].

Reasoning models in the GPT-5 family — including `gpt-5-thinking-mini`
(the system-card name for the API `gpt-5-mini`) — are additionally
"trained to reason through reinforcement learning" and learn to produce
a long internal chain of thought before answering [T1.2].

**Knowledge cutoff:** May 31, 2024 [T1.1].

Specific dataset names, sizes, licensing breakdowns, deduplication
methodology, and synthetic-data proportion: Not publicly available
[T1.2].

## 7. Quantitative Analyses

The system card's headline disaggregated tables (Tables 2-5) are
populated for `gpt-5-thinking`, OpenAI o3, `gpt-5-main`, and GPT-4o,
with mini-variant numbers presented in surrounding text and the
appendix rather than the main tables [T1.2]. Per the system card
introduction: "This system card focuses primarily on gpt-5-thinking
and gpt-5-main, while evaluations for other models are available in
the appendix" [T1.2]. As of publication, the system card was dated
August 13, 2025 [T1.2].

Selected numerical results from the system card tables (for the
larger `gpt-5-thinking` sibling, which provides the closest published
reference for `gpt-5-mini`'s reasoning behaviour) [T1.2]:

| Eval | Metric | gpt-5-thinking |
| --- | --- | --- |
| Disallowed: hate (aggregate) | not_unsafe (↑) | 1.000 |
| Disallowed: illicit/violent | not_unsafe (↑) | 1.000 |
| Production: illicit/violent | not_unsafe (↑) | 0.912 |
| Production: self-harm/instructions | not_unsafe (↑) | 0.955 |
| Sycophancy (offline) | sycophancy (↓) | 0.040 |
| StrongReject: violence | not_unsafe (↑) | 0.999 |

Mini-variant numbers per evaluation: see GPT-5 System Card appendix
[T1.2].

Disaggregated subgroup analyses (by demographic dimension) for
`gpt-5-mini` specifically, beyond BBQ: Not publicly available [T1.2].

## 8. Ethical Considerations

Per the GPT-5 System Card, OpenAI documents the following risks and
mitigations applicable to the GPT-5 family including `gpt-5-mini`
[T1.2]:

- **Disallowed content / harmful generation** — Mitigated via
  "safe-completions": a safety-training approach that "centers on the
  safety of the assistant's output rather than a binary classification
  of the user's intent," intended to reduce both successful malicious
  uplift and over-refusal on dual-use prompts [T1.2].
- **Sycophancy** — Post-training optimisation against a sycophancy
  reward signal; offline evaluations show ~3x improvement over GPT-4o
  for `gpt-5-main` and further improvement for `gpt-5-thinking` [T1.2].
  OpenAI flags emotional dependency and mental/emotional distress
  scenarios as ongoing research areas [T1.2].
- **Jailbreaks / adversarial prompts** — Evaluated via StrongReject;
  GPT-5 thinking models perform on par with OpenAI o3 [T1.2].
- **Prompt injections** — Evaluated and red-teamed externally; covered
  in Section 3.6 of the system card [T1.2].
- **Instruction Hierarchy violations** — Models trained to follow
  system > developer > user instruction priority; evaluated via
  system-prompt extraction and phrase-protection tests [T1.2].
- **Hallucinations** — Detailed in Appendix 2 of the system card;
  OpenAI claims "significant advances in reducing hallucinations"
  for GPT-5 [T1.2].
- **Deception** — Evaluated including chain-of-thought monitoring
  (Section 3.8.1) [T1.2].
- **Image input misuse** — Evaluated separately (Section 3.9) [T1.2].
- **Health domain risks** — Evaluated in Section 3.10; the smaller
  thinking-mini reportedly performs nearly as well as `gpt-5-thinking`
  on health-related evaluations [T4.1].
- **Bias and fairness** — Evaluated via BBQ (Section 3.12) [T1.2].
- **Catastrophic-risk capabilities** — OpenAI's Preparedness Framework
  classified `gpt-5-thinking` as **High capability** in the Biological
  and Chemical domain, "activating the associated safeguards," even
  without "definitive evidence that this model could meaningfully help
  a novice to create severe biological harm," as a precautionary
  measure [T1.2]. Cybersecurity and AI Self-Improvement are also
  evaluated [T1.2]. Whether the same High-capability classification
  applies to `gpt-5-mini` specifically is not stated explicitly in the
  introductory section of the system card and would need to be
  confirmed against the appendix [T1.2].
- **Sandbagging** — Externally evaluated by Apollo Research [T1.2].

Mitigations layered include: data filtering (PII reduction,
moderation-API filtering); safe-completions training; instruction
hierarchy training; reinforcement learning from human feedback;
account-level enforcement; API-level controls; the Trusted Access
Program for high-risk biological capabilities; expert and
third-party red teaming; external government red teaming [T1.2].

Known limitations explicitly flagged: residual safety failures
(non-zero), sycophancy (reduced but not eliminated), and gaps in
evaluating emotional-dependency scenarios [T1.2].

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- **Parameter count**, architecture details, and training compute for
  `gpt-5-mini` are not disclosed by OpenAI [T1.1][T1.2].
- **Mini-specific benchmark numbers** are referenced as "in the
  appendix" of the system card; the headline tables in the main body
  show `gpt-5-thinking` and `gpt-5-main` values rather than mini values
  [T1.2]. This card cites the larger sibling's numbers as the closest
  published reference and notes the gap.
- **Training data composition** beyond OpenAI's high-level description
  (public web + licensed third-party + user/trainer-provided data) is
  not publicly available [T1.2].
- **Latency / throughput SLO numbers** are not published as numeric
  values; only a qualitative "fast" tier [T1.1].
- **Whether `gpt-5-mini` specifically is classified High capability in
  the Biological and Chemical domain under the Preparedness Framework**
  is not explicitly stated in the system card introduction; the
  declaration concerns `gpt-5-thinking` [T1.2]. Treat the precautionary
  posture as applying to the family by default.

**Source-tier conflicts:** None identified between tier-1 OpenAI sources
and tier-4 sources. The OpenRouter listing's claim that `gpt-5-mini`
"supersedes OpenAI's previous o4-mini offering" [T4.2] is consistent
with the GPT-5 System Card's progression table mapping OpenAI o4-mini →
`gpt-5-thinking-mini` [T1.2].

**Recommendations for use:**

- Prefer `gpt-5-mini` for reasoning-capable workloads where latency
  and cost dominate quality requirements; for the highest quality,
  use `gpt-5` directly [T1.1].
- For new projects starting today, evaluate `gpt-5.4-mini` alongside
  `gpt-5-mini` per OpenAI's own current guidance [T1.1].
- Do not use for audio I/O (unsupported) [T1.1] or fine-tuning workflows
  (unsupported as of this card date) [T1.1].
- For high-stakes domains (medical, legal, financial advice; biosecurity-
  adjacent queries), apply additional human-in-the-loop review; the
  system card's Health and Preparedness sections document residual
  risks even with safeguards [T1.2].
- Treat the May 31, 2024 knowledge cutoff [T1.1] as a hard limit; pair
  with web search tool calls when freshness matters.

## 10. Operational Details

- **Pricing** (per 1M tokens, as of 2026-04-30) — Standard input: $0.25;
  Cached input: $0.025; Output: $2.00 [T1.1].
- **Context window** — 400,000 tokens [T1.1].
- **Maximum output tokens** — 128,000 [T1.1].
- **Knowledge cutoff** — May 31, 2024 [T1.1].
- **Modalities** — Input: text and images. Output: text only [T1.1].
- **Reasoning** — Reasoning token support: Yes; reasoning level: High
  [T1.1].
- **Supported APIs/SDKs** — OpenAI API; accessible via the same
  endpoints as other GPT-5 family models [T1.1]. OpenAI Chat Completions
  compatibility: standard.
- **Latency tier** — Provider-stated qualitative tier: "Fast" [T1.1].
  Numeric SLO: Not publicly available.
- **Tool / structured-output support** — Streaming: yes; Function
  calling: yes; Structured outputs: yes [T1.1]. Tools available: web
  search, file search, code interpreter, MCP [T1.1].
- **Function calling** — Supported [T1.1]. Parallel function calling
  and exact schema-format details for `gpt-5-mini`: see OpenAI tool-use
  reference; not enumerated on the model page [T1.1].
- **Fine-tuning availability** — Not supported [T1.1].
- **Rate-limit notes** — Vary by tier. Tier 1 example published: 500
  requests per minute; 500,000 tokens per minute [T1.1]. Higher tiers
  scale per OpenAI's standard rate-limit policy.
- **Current snapshot** — `gpt-5-mini-2025-08-07` [T1.1].
- **Deprecation status** — Active; OpenAI suggests considering
  `gpt-5.4-mini` for new low-latency, high-volume workloads, but
  `gpt-5-mini` remains available [T1.1].
