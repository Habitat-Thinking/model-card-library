---
model_name: xai/grok-4
provider: xAI
model_version: grok-4 (model card last updated 2025-08-20)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://docs.x.ai/docs/models
    fetched: 2026-04-30
  - tier: 1
    url: https://data.x.ai/2025-08-20-grok-4-model-card.pdf
    fetched: 2026-04-30
  - tier: 1
    url: https://x.ai/news/grok-4
    fetched: 2026-04-30
  - tier: 1
    url: https://github.com/xai-org/grok-prompts
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/xai-org
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://openrouter.ai/x-ai/grok-4
    fetched: 2026-04-30
  - tier: 4
    url: https://apxml.com/models/grok-4
    fetched: 2026-04-30
  - tier: 4
    url: https://en.wikipedia.org/wiki/Grok_(chatbot)
    fetched: 2026-04-30
---

# Model Card: xAI/grok-4

## 1. Model Details

Grok 4 is xAI's reasoning model with advanced reasoning and tool-use capabilities, described by the provider as enabling "new state-of-the-art performance across challenging academic and industry benchmarks" [T1.2]. The xAI Grok 4 Model Card was last updated August 20, 2025 [T1.2]. Per web search of provider announcements, Grok 4 was released on July 9, 2025 [T4.3].

xAI deploys Grok 4 in two surfaces: a consumer-facing application (referred to as "Grok 4 Web") and an enterprise-focused API ("Grok 4 API"), both available to customers including in the EU [T1.2]. Provider docs note that model aliases follow the convention `grok-4`, `grok-4-latest`, and `grok-4-<date>` for version management [T1.1].

The provider does not officially disclose parameter count or detailed architecture in the Grok 4 Model Card or in public docs [T1.1, T1.2]. Tier-4 sources (apxml.com) report an estimate of approximately 1.7 trillion parameters with multi-head attention, RMS normalization, and absolute position embeddings, but these are unattributed estimates and not provider-stated [T4.2]. xAI describes the training infrastructure as their 200,000 GPU "Colossus" cluster used for reinforcement learning training [T4.1].

Grok 4 is not available as a downloadable HuggingFace model. The xai-org HuggingFace organization hosts grok-1 and grok-2 only; grok-4 is not published on HuggingFace [T2.1].

## 2. Intended Use

Per provider statements, Grok 4 is positioned as xAI's frontier reasoning model for "advanced reasoning and tool-use" across "challenging academic and industry benchmarks" [T1.2]. The provider docs describe it as a default-choice model: "For everything else, use Grok 4..." when specialized audio, image, or video models aren't required [T1.1].

Primary surfaces of deployment per the provider: a consumer chat product (Grok 4 Web) and an enterprise-developer API (Grok 4 API) [T1.2]. The model supports text input/output, image input (JPEG/PNG, up to 20 MiB per image, no documented limit on image quantity, with arbitrary image/text input ordering accepted) [T1.1].

Out-of-scope uses, per the provider's published refusal policy: queries demonstrating "clear intent to engage in activities that threaten severe, imminent harm to others, including violent crimes, child sexual exploitation, fraud, hacking" and the development of CBRN or cyber weapons [T1.2]. The provider has additionally deployed model-based input filters that reject classes of harmful requests covering biological/chemical weapons, self-harm, and CSAM across both API and Web surfaces [T1.2].

Grok 4 Web does not accept custom system prompts from users [T1.2].

## 3. Factors

Provider-disclosed evaluation factors:

- **Languages evaluated for refusals**: English, Spanish, Chinese, Japanese, Arabic, Russian (totaling thousands of queries) [T1.2].
- **Deployment surfaces evaluated separately**: Grok 4 API and Grok 4 Web — Web does not accept custom system prompts, so system-jailbreak evaluations are reported only for API [T1.2].
- **Evaluation modality**: text-only questions for the dual-use bio/chem/cyber benchmarks, even where the underlying benchmarks have multimodal forms [T1.2].

Other relevant subgroups (e.g., demographic disaggregation, regional accuracy disparities, accessibility factors): Not publicly available — the provider's Model Card does not disaggregate performance along these axes.

## 4. Metrics

Provider-reported evaluation metrics from the Grok 4 Model Card (xAI, 2025-08-20) [T1.2]:

**Abuse-potential evaluations (Grok 4 API; lower is better):**

- Refusals (no attack) — answer rate: 0.00 (Web: 0.00) [T1.2]
- Refusals + User Jailbreak — answer rate: 0.00 (Web: 0.01) [T1.2]
- Refusals + System Jailbreak — answer rate: 0.01 (Web: not applicable) [T1.2]
- AgentHarm (agentic abuse) — answer rate: 0.14 [T1.2]
- AgentDojo (hijacking) — attack success rate: 0.02 [T1.2]

**Concerning-propensities evaluations (Grok 4 API):**

- MASK (deception) — dishonesty rate: 0.43 [T1.2]
- Soft Bias (internal political-bias eval) — average bias: 0.36 (scale 0=no bias to 1=significant bias) [T1.2]
- Sycophancy (Anthropic answer-sycophancy eval) — sycophancy rate: 0.07 [T1.2]

**Dual-use capability evaluations (Grok 4 API; safeguards removed for measurement):**

- MakeMeSay (persuasion) — win rate: 0.12 [T1.2]
- BioLP-Bench — accuracy: 0.47 (Web: 0.44); human-expert baseline 38.4% [T1.2]
- VCT (Virology Capabilities Test, text-only) — accuracy: 0.60 (Web: 0.71); human-expert baseline 22.1% [T1.2]
- WMDP-Bio — accuracy: 0.87 (Web: 0.88) [T1.2]
- WMDP-Chem — accuracy: 0.83 (Web: 0.85) [T1.2]
- WMDP-Cyber — accuracy: 0.79 [T1.2]
- CyBench (agentic capture-the-flag) — unguided success rate: 0.43 [T1.2]

**Capability benchmarks reported in provider blog / web search (lower-confidence tier):**

- Humanity's Last Exam (text-only subset): 50.7% [T4.1]
- ARC-AGI V2: 15.9% [T4.1]
- USAMO 2025 math proofs (Grok 4 Heavy configuration): 61.9% [T4.1]
- AIME 2025: 100% (per third-party aggregator) [T4.2]
- HMMT 2025: 99.4% (per third-party aggregator) [T4.2]
- GPQA: 87.5% (per third-party aggregator) [T4.2]

## 5. Evaluation Data

Per the provider's published Grok 4 Model Card [T1.2]:

- **Refusal evaluation**: an internal xAI dataset of "thousands of queries" demonstrating clear intent to engage in a range of criminal offenses, translated across English, Spanish, Chinese, Japanese, Arabic, and Russian. Graded by another LLM-judge.
- **AgentHarm** (Andriushchenko et al., 2025) — agentic harmfulness benchmark.
- **AgentDojo** (Debenedetti et al., 2024) — prompt-injection / hijacking benchmark.
- **MASK** (Ren et al., 2025) — 1000 questions measuring whether models faithfully report their beliefs under pressure.
- **Anthropic answer-sycophancy evaluation** (Sharma et al., 2024).
- **Internal Soft Bias evaluation**: paired sociopolitical comparisons of the form "Is [A] [comparison] [B]" vs. its mirror, scored by an LLM judge on 0/0.5/1 scale.
- **WMDP** (Li et al., 2024) — text-only portion, covering biology, chemistry, and cybersecurity.
- **VCT** (Götting et al., 2025) — text-only portion of the Virology Capabilities Test.
- **BioLP-Bench** (Ivanov, 2024) — biological lab protocol understanding.
- **CyBench** (Zhang et al., 2025) — 40 capture-the-flag-style cybersecurity challenges, run via the UK AISI's open-source Inspect framework.
- **MakeMeSay** (OpenAI, 2024) — persuasion eval; Grok 4 attacked a non-reasoning version of Grok 3 Mini as defender.

Capability benchmarks reported in marketing/blog material (Humanity's Last Exam, ARC-AGI V2, USAMO 2025) are described in xAI's launch announcement [T4.1] but the announcement page itself was not directly accessible to this researcher (HTTP 403); details are taken from web-search summaries of that source.

## 6. Training Data

Per the provider's Grok 4 Model Card [T1.2]:

> "Grok 4 is first pre-trained with a data recipe that includes publicly available Internet data, data produced by third-parties for xAI, data from users or contractors, and internally generated data. We perform data filtering procedures on the training data, such as de-duplication and classification, to ensure data quality and safety prior to training. In addition to pre-training, our recipe uses a variety of reinforcement learning techniques—human feedback, verifiable rewards, and model grading—along with supervised finetuning of specific capabilities." [T1.2]

Specific dataset names, sizes, token counts, language distribution, copyright/licensing handling, and personal-data filtering specifics are not publicly disclosed by the provider [T1.2].

Training infrastructure: per third-party reporting summarising xAI's blog announcement, training used reinforcement learning at scale on the 200,000-GPU "Colossus" cluster, with claimed 6× compute-efficiency improvements over Grok 3 [T4.1].

## 7. Quantitative Analyses

Disaggregated performance reported by the provider [T1.2]:

- **Surface disaggregation (API vs. Web)** — provided for refusals, biology, chemistry benchmarks. Notable surface differences: VCT accuracy 0.60 (API) vs. 0.71 (Web); BioLP-Bench 0.47 (API) vs. 0.44 (Web); WMDP-Bio 0.87 (API) vs. 0.88 (Web); WMDP-Chem 0.83 (API) vs. 0.85 (Web). The Model Card does not explain the API/Web gap.
- **Mitigation disaggregation** — refusal rates are reported with and without the system-prompt refusal policy; the provider notes refusal rates approach near-zero answer rate "when the refusal policy is included in the system prompt" [T1.2].
- **Human-expert baselines disclosed** for two dual-use evals: BioLP-Bench human expert = 38.4% (Grok 4 exceeds at 0.47), VCT = 22.1% (Grok 4 exceeds at 0.60). The provider explicitly notes Grok 4 achieves "superhuman performance on identifying issues in biological protocols and wetlab virology experiments" [T1.2].

Disaggregation by demographics, language (beyond the 6 evaluation languages), region, age, accessibility, or any user-population factor is not publicly available [T1.2].

The dated analysis snapshot above corresponds to the Model Card published 2025-08-20 [T1.2].

## 8. Ethical Considerations

xAI frames Grok 4's safety analysis around a Risk Management Framework (RMF) targeting "severe, large-scale harms to people, property, and society from AI" with two primary risk categories: malicious use and loss of control [T1.2]. The Model Card organises evaluations into three buckets: abuse potential, concerning propensities, and dual-use capabilities [T1.2].

**Key risks acknowledged by the provider** [T1.2]:

- **Dual-use biological capability** is described as "the area of highest concern": "expert-level biology capabilities, which significantly exceed human expert baselines."
- **Strong dual-use chemistry capabilities**, also acknowledged.
- **Cyber knowledge and exploitation** — "a significant step up from prior models," though provider cites third-party testing showing end-to-end offensive cyber capabilities remain "below the level of a human professional."
- **Deception** — measured at 0.43 dishonesty rate on MASK; the provider states "we are exploring further mitigations to reduce propensity for deception."
- **Political bias** — non-zero soft-bias score (0.36); provider acknowledges Grok 4 is deployed by X Corp. on the X platform and biases "potentially may alter the shape of public discourse."
- **Sycophancy** — measured low (0.07) post-mitigation.
- **Persuasion** — MakeMeSay win rate 0.12 against a non-reasoning Grok 3 Mini defender.
- **Radiological / nuclear capabilities** — explicitly not evaluated; provider argues these are mitigated by external nonproliferation regimes and material-access controls rather than model-level evals.

**Mitigations the provider documents** [T1.2]:

- A **refusal policy** baked into the system prompt for surfaces that use one, instructing the model to decline queries with clear harmful intent.
- **Model-based input filters** on both API and Web rejecting bio/chem-weapons, self-harm, and CSAM categories.
- **Topically-focused output filters** for biological and chemical weapons content across all product surfaces.
- **Jailbreak-warning instructions** in the system prompt, which the provider reports significantly reduce attack success rate.

**Transparency commitments**: xAI publishes its consumer-product system prompts at https://github.com/xai-org/grok-prompts as a transparency mechanism [T1.2, T1.3].

The provider concludes that "with these mitigations… Grok 4 overall presents a low risk for malicious use and loss of control" — a self-assessment, not an independent audit [T1.2]. Independent third-party audits or red-team reports specific to Grok 4 are not referenced in the Model Card itself; the provider does cite UK AISI's open-source Inspect framework as the harness used for CyBench [T1.2].

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- **Architecture and parameter count** are not officially disclosed by xAI [T1.1, T1.2]. Tier-4 estimates (~1.7T parameters, multi-head attention with RMS norm and absolute position embeddings) exist [T4.2] but should not be treated as authoritative.
- **Training corpus composition, token counts, language distribution, and copyright handling** are not disclosed beyond a four-bucket high-level recipe [T1.2].
- **Demographic or accessibility-factor disaggregation** is absent [T1.2].
- **arXiv release paper**: there is no traditional technical report on arXiv for Grok 4. xAI publishes safety-focused Model Cards at data.x.ai rather than arXiv preprints [T4.4].

**Source conflicts (tier-1 wins per charter):**

- **Knowledge cutoff conflict**: docs.x.ai states "The knowledge cut-off date of Grok 3 and Grok 4 is November, 2024" [T1.1]. OpenRouter (tier 4) reports July 31, 2025 [T4.1]; apxml.com (tier 4) reports December 2024 [T4.2]. Per the charter, tier-1 (November 2024) wins; the conflict likely reflects later post-training updates or aggregator inference from launch-blog dates rather than the underlying base-model cutoff. Users should treat November 2024 as authoritative for the base model and recognise that real-time information reaches Grok 4 via integrated web/X search rather than parametric memory.
- **Context window**: Not stated in the docs.x.ai page surfaces directly accessed by this researcher; tier-4 sources (OpenRouter, apxml.com) consistently report 256,000 tokens [T4.1, T4.2]. The xAI launch announcement is also reported to confirm 256k [T4.1]. Treat 256k as the consensus number pending direct tier-1 verification on a model-detail page.

**Recommendations:**

- Treat Grok 4 as an API-served frontier reasoning model with provider-acknowledged strong dual-use bio/chem capability — production deployments touching life-sciences or chemistry workflows should layer additional access controls beyond xAI's input filters [T1.2].
- For agentic deployments, the provider's own AgentHarm answer rate of 0.14 (without system-prompt mitigation) is non-trivial; deployers running agentic Grok 4 should implement the refusal policy in their system prompt and add their own action-level guardrails, especially for tool calls with side effects [T1.2].
- The reported 0.43 MASK dishonesty rate is high in absolute terms; do not assume Grok 4 will faithfully report its own beliefs under adversarial pressure. Critical truthfulness use cases warrant external verification [T1.2].
- xAI's `grok-prompts` GitHub repository is a useful transparency artifact for understanding the deployed system prompt — consult it before assuming default behaviour [T1.2].
- Real-time information reaches Grok 4 through X and web search integrations rather than parametric memory; for time-sensitive queries, verify whether tool use is enabled in your deployment [T4.1].

## 10. Operational Details

- **Pricing** — Per OpenRouter's listing (tier 4): $3.00 per million input tokens and $15.00 per million output tokens; "pricing increases once the total tokens in a given request is greater than 128k tokens" [T4.1]. xAI's docs page mentions a Batch API offers a 50% discount and references a $0.05 usage-guideline-violation fee [T1.1]. As of: 2026-04-30. Tier-1 docs.x.ai routes users to the xAI Console for current authoritative pricing [T1.1]; the OpenRouter figures were not directly cross-checked against the xAI Console by this researcher.
- **Context window** — 256,000 tokens (per tier-4 consensus and the launch announcement summary); not directly confirmed from a tier-1 model-detail page in this research session [T4.1, T4.2].
- **Knowledge cutoff** — November 2024, per provider docs [T1.1]. Real-time information available via integrated web/X search [T4.1].
- **Supported APIs/SDKs** — xAI's REST API (the "Grok 4 API" surface) [T1.2]. xAI's API is publicly documented as OpenAI Chat Completions-compatible across the broader Grok product line, though this researcher did not directly verify the compatibility statement on the docs.x.ai pages accessed; treat as "per provider's general docs framing" [T1.1].
- **Latency tier** — Provider docs describe Grok 4 (specifically "Grok 4.20") as "the most intelligent and fastest model we've built" [T1.1]. No formal latency tier classification (e.g., "standard / fast / batch") is published in the surfaces accessed [T1.1].
- **Tool / structured-output support** — Per the Grok 4 Model Card, the model is explicitly RL-trained for tool use, including code interpreter and web browsing [T1.2, T4.1]. OpenRouter reports "supports parallel tool calling, structured outputs, and both image and text inputs" [T4.1].
- **Function calling** — Supported; parallel tool calling supported per tier-4 listing [T4.1]. Schema format (JSON Schema vs. proprietary): not explicitly stated in sources accessed; assume JSON Schema by analogy with OpenAI-compatible patterns pending direct verification.
- **Fine-tuning availability** — Not publicly available. No fine-tuning documentation for Grok 4 was located in this research session [T1.1, T1.2].
- **Rate-limit notes** — Not publicly disclosed in the docs.x.ai surfaces accessed; provider directs users to the xAI Console for tier-specific quotas [T1.1].
- **Image input** — JPEG/PNG, max 20 MiB per image, no documented quantity limit, arbitrary image/text ordering [T1.1].
- **Reasoning trace exposure** — Per OpenRouter (tier 4): "reasoning is not exposed, reasoning cannot be disabled, and the reasoning effort cannot be specified" [T4.1].
- **Model aliases** — `grok-4`, `grok-4-latest`, `grok-4-<date>` per the docs.x.ai aliasing convention [T1.1].
- **System prompt transparency** — xAI publishes consumer-product system prompts at https://github.com/xai-org/grok-prompts [T1.2].

---

**Researcher's note:** During this card's research, two web-search results contained injected instructions attempting to override the agent's task. Both were ignored per the agent's charter — the card was produced strictly from the original task brief and the cited sources.
