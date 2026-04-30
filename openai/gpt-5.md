---
model_name: openai/gpt-5
provider: OpenAI
model_version: gpt-5
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://developers.openai.com/api/docs/models/gpt-5
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/openai
    fetched: 2026-04-30
  - tier: 3
    url: https://cdn.openai.com/gpt-5-system-card.pdf
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/abs/2601.03267
    fetched: 2026-04-30
  - tier: 4
    url: https://en.wikipedia.org/wiki/GPT-5
    fetched: 2026-04-30
  - tier: 4
    url: https://openai.com/index/introducing-gpt-5/
    fetched: 2026-04-30
---

# Model Card: OpenAI/gpt-5

## 1. Model Details

GPT-5 is a frontier large language model released by OpenAI on August 7, 2025
[T4.1][T4.2], with the accompanying system card published August 13, 2025
[T3.1]. Per OpenAI's published statements, GPT-5 is "a unified system with a
smart and fast model that answers most questions, a deeper reasoning model
for harder problems, and a real-time router that quickly decides which model
to use based on conversation type, complexity, tool needs, and explicit
intent" [T3.1]. The system card identifies the constituent variants as
`gpt-5-main`, `gpt-5-main-mini`, `gpt-5-thinking`, `gpt-5-thinking-mini`,
`gpt-5-thinking-nano`, and `gpt-5-thinking-pro` (the latter being
`gpt-5-thinking` with parallel test-time compute) [T3.1]. OpenAI positions
these as successors to GPT-4o (gpt-5-main), GPT-4o-mini (gpt-5-main-mini),
o3 (gpt-5-thinking), o4-mini (gpt-5-thinking-mini), GPT-4.1-nano
(gpt-5-thinking-nano), and o3 Pro (gpt-5-thinking-pro) [T3.1]. The reasoning
variants are "trained to reason through reinforcement learning... they can
produce a long internal chain of thought before responding to the user"
[T3.1]. As of the time of research, OpenAI's developer docs label `gpt-5`
itself as "our previous model for coding, reasoning, and agentic tasks
across domains" and recommend GPT-5.1 instead [T1.1]. Parameter count is
not publicly disclosed [T1.1][T3.1]. GPT-5 is not available on HuggingFace
[T2.1].

## 2. Intended Use

Per the provider's published statements, GPT-5 is intended for "coding,
reasoning, and agentic tasks across domains" [T1.1]. OpenAI describes
"significant advances in reducing hallucinations, improving instruction
following, and minimizing sycophancy, and have leveled up GPT-5's
performance in three of ChatGPT's most common uses: writing, coding, and
health" [T3.1]. Primary access surfaces are the OpenAI API (Chat
Completions, Responses API, and Realtime endpoints) and ChatGPT
[T1.1][T4.2]. Out-of-scope: the developer docs explicitly note GPT-5 "does
not support fine-tuning or computer use features" [T1.1]. The system card
treats `gpt-5-thinking` as High capability in the Biological and Chemical
domain under OpenAI's Preparedness Framework, with associated safeguards
activated as a precautionary measure [T3.1]. Use that risks novice uplift
for biological or chemical harm is treated as out-of-scope and gated by
account-level enforcement, API access controls, and a Trusted Access
Program [T3.1].

## 3. Factors

The system card reports evaluations disaggregated by:

- **Model variant** — `gpt-5-thinking`, `gpt-5-main` (compared to predecessors
  o3 and GPT-4o respectively) [T3.1].
- **User tier** — sycophancy measured separately for free vs paid ChatGPT
  users [T3.1].
- **Language / multilingual performance** — reported in section 3.11 of the
  system card [T3.1].
- **Demographic fairness** — BBQ (Bias Benchmark for QA) evaluation reported
  in section 3.12 [T3.1].
- **Modality** — text and image inputs separately evaluated; image-input
  safety reported in section 3.9 [T3.1][T1.1].
- **Domain** — health, biological/chemical, cybersecurity, AI
  self-improvement separately evaluated [T3.1].

Environmental and instrumentation factors (compute, hardware, energy) are
not publicly available [T1.1][T3.1].

## 4. Metrics

Reported in the system card and OpenAI announcements [T3.1][T4.2]:

- **Hallucinations on challenging conversations**: reduced approximately 8x
  between OpenAI o3 and gpt-5-thinking [T4.2].
- **Errors in potentially urgent situations**: reduced over 50x from GPT-4o
  and over 8x from OpenAI o3 [T4.2].
- **Sycophancy (offline evaluation, lower is better)**: GPT-4o baseline
  0.145; gpt-5-main 0.052; gpt-5-thinking 0.040 [T3.1].
- **Sycophancy (online A/B vs GPT-4o)**: prevalence fell 69% for free users
  and 75% for paid users [T3.1].
- **Standard Disallowed Content (not_unsafe, higher is better, selected)**:
  gpt-5-thinking scores 1.000 on hate (aggregate), illicit/violent,
  self-harm, sexual/exploitative; 0.991 illicit/non-violent; 0.881
  personal-data [T3.1].
- **Jailbreak robustness (StrongReject not_unsafe)**: gpt-5-thinking 0.995
  illicit/non-violent-crime, 0.999 violence, 0.999 abuse/disinformation/hate,
  0.995 sexual-content [T3.1].
- **Production benchmarks (multi-turn, harder set)**: gpt-5-thinking
  outperforms o3 in most categories; gpt-5-main shows mixed results vs
  GPT-4o [T3.1].

Additional Preparedness Framework evaluations are reported across SWE-bench
Verified (N=477), MLE-Bench, SWE-Lancer, PaperBench, OPQA, ProtocolQA
Open-Ended, TroubleshootingBench, and Capture-the-Flag challenges; specific
numeric scores appear in the system card [T3.1].

## 5. Evaluation Data

Per the system card, evaluations used [T3.1]:

- **Internal**: Standard Disallowed Content evaluation set, Production
  Benchmarks (multi-turn, multi-language), OpenAI PRs, sycophancy offline
  set, BBQ.
- **External / public**: StrongReject (jailbreak), SWE-bench Verified
  (N=477), MLE-Bench, SWE-Lancer, PaperBench, OPQA, ProtocolQA Open-Ended.
- **Third-party / external evaluators**: SecureBio (biological-risk
  external evaluations), Pattern Labs (cyber-range external evaluations),
  METR (AI self-improvement external evaluations), Apollo Research
  (sandbagging evaluations).

OpenAI also conducted internal and government red-teaming exercises for
the High-capability Biological and Chemical risk category [T3.1]. The full
contents of the internal evaluation sets are not publicly available [T3.1].

## 6. Training Data

Per the provider's published statements, "the GPT-5 models were trained on
diverse datasets, including information that is publicly available on the
internet, information that we partner with third parties to access, and
information that our users or human trainers and researchers provide or
generate" [T3.1]. OpenAI states the data processing pipeline "includes
rigorous filtering to maintain data quality and mitigate potential risks.
We use advanced data filtering processes to reduce personal information
from training data. We also employ a combination of our Moderation API and
safety classifiers to help prevent the use of harmful or sensitive content,
including explicit materials such as sexual content involving a minor"
[T3.1]. The reasoning variants (`gpt-5-thinking`, `-mini`, `-nano`) are
additionally trained via reinforcement learning to produce internal
chain-of-thought reasoning [T3.1]. Specific dataset names, sizes, dates,
and proportions are not publicly available [T3.1][T1.1].

## 7. Quantitative Analyses

The system card publishes disaggregated tables [T3.1]:

- **Table 2 (Standard Disallowed Content)** — `not_unsafe` rates across
  eight harm categories for gpt-5-thinking, OpenAI o3, gpt-5-main, GPT-4o
  [T3.1].
- **Table 3 (Production Benchmarks)** — same model comparison across eleven
  multi-turn harm categories [T3.1].
- **Table 4 (Sycophancy)** — offline scores plus online A/B preliminary
  measurement disaggregated by free vs paid user tier [T3.1].
- **Table 5 (Jailbreak / StrongReject)** — `not_unsafe` rates across four
  prompt categories [T3.1].
- **Section 3.11 (Multilingual Performance)** — disaggregated by language
  [T3.1].
- **Section 3.12 (BBQ)** — disaggregated by demographic group [T3.1].
- **Section 5.1 (Capabilities Assessment)** — disaggregated by domain
  (Biological & Chemical, Cybersecurity, AI Self-Improvement) [T3.1].

Analysis date: August 13, 2025 [T3.1]. The system card notes that
comparison values from live models (e.g., OpenAI o3) "are from the latest
versions of those models, so may vary slightly from values published at
launch" [T3.1].

## 8. Ethical Considerations

Per the system card [T3.1]:

- **Preparedness classification**: `gpt-5-thinking` is treated as High
  capability in the Biological and Chemical domain. OpenAI states "we do
  not have definitive evidence that this model could meaningfully help a
  novice to create severe biological harm... we have chosen to take a
  precautionary approach" [T3.1].
- **Safe-completions**: OpenAI moved from binary refusal training to
  "safe-completions: a safety-training approach that centers on the safety
  of the assistant's output rather than a binary classification of the
  user's intent" — motivated by brittleness on dual-use prompts [T3.1].
- **Known failure modes documented**: hallucinations (Section 3.7 and
  Appendix 2), deception including chain-of-thought monitoring (3.8),
  prompt injection vulnerabilities (3.6), instruction-hierarchy violations
  (3.5), jailbreak susceptibility (3.4), sycophancy (3.3), regressions on
  hate/threatening and sexual/exploitative for gpt-5-main vs GPT-4o
  (statistically significant per the card) [T3.1].
- **Mitigations layered**: model-level training (safe-completions,
  instruction hierarchy), system-level protections, account-level
  enforcement, gated API access, and the Trusted Access Program for
  high-risk biological capabilities [T3.1].
- **Red teaming**: expert red teaming for violent attack planning,
  bioweaponization, prompt injection (expert + automated); third-party red
  teaming and external government red teaming for the High-capability
  category [T3.1].
- **External assessments**: SecureBio (biology), Pattern Labs (cyber),
  METR (AI self-improvement), Apollo Research (sandbagging) [T3.1].

OpenAI also published an addendum on sensitive conversations (mental-health
contexts) and a separate addendum for GPT-5.1 [T4.1].

## 9. Caveats and Recommendations

What this card cannot tell you:

- **Parameter counts, architecture details, training-compute, training-data
  composition, and energy/carbon costs**: not publicly available; OpenAI
  does not disclose these for GPT-5 [T1.1][T3.1].
- **Training cutoff sources**: OpenAI's developer docs state a knowledge
  cutoff of September 30, 2024 [T1.1]; the system card itself does not
  restate a specific cutoff date.
- **Lifecycle status conflict**: the system card (Aug 2025) presents GPT-5
  as the current frontier system [T3.1], while the developer docs at
  research time describe `gpt-5` as "our previous model" and recommend
  GPT-5.1 [T1.1]. Per the honesty rule (tier-1 wins on conflicts), the
  current operational status is "superseded by GPT-5.1 in OpenAI's
  recommended-model lineup" — but GPT-5 remains available via the API
  [T1.1].
- **`gpt-5` vs `gpt-5-thinking` / `gpt-5-main` mapping in the API**: the
  developer-facing `gpt-5` model ID is the unified router product; the
  internal sub-variants named in the system card are not all separately
  exposed as API model IDs [T1.1][T3.1].

Recommendations:

- Use GPT-5 where its documented strengths apply: coding, agentic tasks,
  long-context reasoning (400K-token window), structured outputs, tool use
  [T1.1].
- Do not use for: fine-tuning workflows or computer-use scenarios — neither
  is supported [T1.1].
- For the latest frontier capabilities, OpenAI's docs now point users to
  GPT-5.1; treat this card as describing the original GPT-5 release [T1.1].
- Treat health-domain outputs cautiously despite OpenAI's reported
  improvements; the system card's "errors in potentially urgent situations
  reduced 50x" is an improvement claim, not a sufficiency claim [T3.1][T4.2].
- For high-stakes biological / chemical / cyber workflows, follow OpenAI's
  Preparedness Framework safeguards and Trusted Access Program gates
  [T3.1].

## 10. Operational Details

- **Pricing** (as of the developer docs at research time): input $1.25 per
  million tokens; output $10.00 per million tokens; cached input $0.125 per
  million tokens [T1.1].
- **Context window**: 400,000 input tokens; 128,000 maximum output tokens
  [T1.1].
- **Knowledge cutoff**: September 30, 2024 [T1.1].
- **Supported APIs/SDKs**: Chat Completions, Responses API, Realtime
  endpoints; streaming supported [T1.1].
- **Latency tier**: configurable reasoning effort levels — minimal, low,
  medium, high [T1.1].
- **Tool / structured-output support**: structured outputs supported; tool
  integrations include web search, file search, image generation, code
  interpretation [T1.1].
- **Function calling**: supported [T1.1]. Parallel-call support and exact
  schema-format details not separately confirmed in the source consulted
  [T1.1].
- **Modalities**: text and image input; text-only output [T1.1].
- **Fine-tuning availability**: not supported [T1.1].
- **Computer-use availability**: not supported [T1.1].
- **Rate-limit notes**: not publicly available at the model-overview level
  consulted; OpenAI publishes tier-based rate limits separately on its
  pricing/limits pages [T1.1].
