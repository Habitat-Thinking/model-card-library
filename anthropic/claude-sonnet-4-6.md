---
title: claude-sonnet-4-6
model_name: anthropic/claude-sonnet-4-6
provider: Anthropic
model_version: claude-sonnet-4-6
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://platform.claude.com/docs/en/about-claude/models/overview
    fetched: 2026-04-30
  - tier: 1
    url: https://platform.claude.com/docs/en/about-claude/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/news/claude-sonnet-4-6
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/claude/sonnet
    fetched: 2026-04-30
  - tier: 1
    url: https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75.pdf
    fetched: 2026-04-30
  - tier: 2
    url: n/a
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-4-6.html
    fetched: 2026-04-30
  - tier: 4
    url: https://venturebeat.com/technology/anthropics-sonnet-4-6-matches-flagship-ai-performance-at-one-fifth-the-cost
    fetched: 2026-04-30
---

# Model Card: Anthropic/claude-sonnet-4-6

## 1. Model Details

Claude Sonnet 4.6 is a large language model from Anthropic, released February 17, 2026 [T1.3]. It is the mid-tier model in Anthropic's current Claude 4 family, positioned between Claude Haiku 4.5 and Claude Opus 4.7, and described by Anthropic as "the best combination of speed and intelligence" [T1.1]. The Claude API model ID is `claude-sonnet-4-6`, with the same identifier serving as both the canonical ID and alias on the Claude API; AWS Bedrock exposes it as `anthropic.claude-sonnet-4-6` and Google Vertex AI as `claude-sonnet-4-6` [T1.1].

Anthropic characterises Sonnet 4.6 as a "hybrid reasoning model with superior intelligence for agents" [T1.4]. It supports both extended thinking mode and adaptive thinking (the "effort" parameter), allowing developers to direct different degrees of reasoning effort depending on task difficulty [T1.5]. Parameter count is not publicly disclosed [T1.5]. The model underwent substantial post-training and fine-tuning after pretraining, with the stated intention of producing a helpful, honest, and harmless assistant [T1.5].

The system card abstract states: "Capability evaluations found that Sonnet 4.6 substantially improves in a wide range of skills over its predecessor, Sonnet 4.5; in several evaluations, it approached or matched the capability levels of Claude Opus 4.6, our frontier model" [T1.5]. Anthropic notes that Sonnet 4.6 "is not a frontier model (that is, it does not broadly advance the frontier of AI capabilities compared to the state-of-the-art in the industry)" but does exceed the frontier model's abilities on some specific measures [T1.5].

## 2. Intended Use

Per Anthropic's published statements, Claude Sonnet 4.6 is intended for [T1.4]:

- **Advanced coding** — "reasoning through complex, multi-file codebases, producing precise implementations"
- **Long-running agents** — "complex, multi-step tasks that require sustained coherence and adaptive decision-making"
- **Browser/computer use** — navigating digital environments for enterprise automation
- **Enterprise workflows** — analysing financial data, synthesising insights, generating documents, producing professional content

Anthropic positions the model as suitable for coding, agents, and professional work at scale [T1.4]. Inputs supported: text and image; outputs: text only [T1.1][T4.1]. Audio, video, speech, and embeddings are not supported [T4.1].

Out-of-scope and prohibited uses are governed by Anthropic's Usage Policy, which the system card explicitly directs users to consult for "details on prohibited uses of our models and our requirements for uses in high-risk and other specific scenarios" [T1.5]. The system card does not enumerate out-of-scope uses inline; per the provider, those live in the Usage Policy [T1.5].

Anthropic Ireland, Limited is the provider of Anthropic's general-purpose AI models in the European Economic Area [T1.5].

## 3. Factors

Relevant factors disclosed by the provider:

- **Multilingual performance** — The system card states this is the first Claude release for which Anthropic includes evaluations of multilingual performance, "assessing the gap in accuracy between the model's responses in English and those in a number of low-resource languages," via GMMLU and MILU [T1.5].
- **Thinking-mode factor** — Performance varies with thinking mode (extended/adaptive) and effort parameter; benchmark results in the system card are reported with adaptive thinking and max effort unless noted [T1.5].
- **Domain-specific factors** — The system card breaks out performance in finance, cybersecurity, life sciences, and healthcare [T1.5].
- **Computer-use environment** — OSWorld-Verified evaluation used 1080p resolution and 100-step action limits on a live Ubuntu VM [T1.5].

Subgroup factors (demographic, geographic) are not disclosed in detail beyond bias evaluations covered in Section 8. Environmental and instrumentation factors specific to deployment are not publicly disclosed beyond what appears in the system card.

## 4. Metrics

All metrics below are from the Claude Sonnet 4.6 System Card unless otherwise noted; results averaged over 10 trials with adaptive thinking and max effort unless specified [T1.5].

**Coding and software engineering:**

- SWE-bench Verified: 79.6% (averaged over 25 trials); 80.2% with a tool-use prompt modification [T1.5]
- SWE-bench Multilingual: 75.9% [T1.5]
- Terminal-Bench 2.0: 59.1% (default thinking, max effort, no thinking budget) [T1.5]
- OpenRCA (root-cause analysis, 335 cases): 27.9% (adaptive thinking, high effort) [T1.5]

**Agentic tasks:**

- τ²-bench Retail: 91.7% [T1.5]
- τ²-bench Telecom: 97.9% [T1.5]
- MCP-Atlas: 61.3% [T1.5]
- OSWorld-Verified: 72.5% (first-attempt success rate, averaged over five runs) [T1.5]
- Vending-Bench 2: results reported in system card section 2.13 [T1.5]

**Reasoning and knowledge:**

- ARC-AGI-2 (Verified): 58.3% (max effort); 60.42% with 120k thinking tokens and high effort on the ARC Prize Foundation private dataset [T1.5]
- ARC-AGI-1: 86.50% (120k thinking tokens, high effort) [T1.5]
- GPQA Diamond: 89.9% [T1.5]
- AIME 2025: results reported in system card section 2.10 [T1.5]
- MMMLU: 89.3% [T1.5]
- GDPval-AA: 1633 (best-in-class in the comparison table) [T1.5]
- Humanity's Last Exam (HLE): 33.2% (no tools); 49.0% (with tools) [T1.5]

**Multimodal:**

- MMMU-Pro (no tools): 74.5%; (with tools): 75.6% [T1.5]
- LAB-Bench FigQA, CharXiv Reasoning: results reported in system card sections 2.17.1–2.17.3 [T1.5]

**Search and long-context:**

- BrowseComp (single-agent, post-March 2026 cheating-detection update): 74.01% [T1.5]
- BrowseComp (multi-agent, updated): 82.07% [T1.5]
- WebArena and WebArena-Verified: results reported in system card section 2.18 [T1.5]
- Long-context: OpenAI MRCR v2 and GraphWalks results reported in system card section 2.16 [T1.5]

**Third-party reported (per VentureBeat summary of Anthropic's headline figures):**

- SWE-bench Verified 79.6%, Terminal-Bench 2.0 59.1%, OSWorld-Verified 72.5% — all improvements over Sonnet 4.5 [T4.2]

## 5. Evaluation Data

Per the provider, evaluation datasets used [T1.5]:

- **SWE-bench Verified** — 500 human-verified solvable problems (developed by OpenAI) [T1.5]
- **SWE-bench Multilingual** — 300 problems in 9 programming languages [T1.5]
- **Terminal-Bench 2.0** — 89 tasks; developed by Stanford and the Laude Institute; run via the Harbor scaffold and Terminus-2 harness on GKE n2-standard-32 nodes [T1.5]
- **OpenRCA** — 335 software failure cases from telecom, banking, and online marketplace systems; 68.5 GB of telemetry; published at ICLR 2025 [T1.5]
- **τ²-bench** — Sierra's agent benchmark (Retail and Telecom sections) [T1.5]
- **OSWorld-Verified** — multimodal computer-use tasks on Ubuntu VM [T1.5]
- **ARC-AGI-1 and ARC-AGI-2** — ARC Prize Foundation private validation sets [T1.5]
- **GPQA Diamond, AIME 2025, MMMLU, GDPval-AA, MMMU-Pro, HLE, LAB-Bench FigQA, CharXiv Reasoning** — standard public benchmarks [T1.5]
- **BrowseComp, Humanity's Last Exam, DeepSearchQA** — agentic search benchmarks [T1.5]
- **GMMLU, MILU** — multilingual evaluations [T1.5]
- **MedCalc-Bench Verified** — healthcare/life sciences evaluation [T1.5]
- **Vending-Bench 2, MCP-Atlas, CyberGym** — agentic and cybersecurity evaluations [T1.5]
- **Internal AI research evaluation suite 1** — kernels task, time series forecasting, text-based RL, LLM training, quadruped RL, novel compiler tasks [T1.5]
- **Cyber evaluations** — Web, Crypto, Pwn, Rev, Network, Cybench [T1.5]

The system card notes a March 6, 2026 changelog update where BrowseComp scores were revised after running an improved cheating-detection pipeline that flagged unintended solutions [T1.5]. Anthropic acknowledges that "many evaluations include information that is available online and may thus have been included in the model's training data" and refers readers to the Claude Opus 4.5 System Card for decontamination methodology [T1.5].

## 6. Training Data

Per the system card: "Claude Sonnet 4.6 was trained on a proprietary mix of publicly available information from the internet up to May 2025, non-public data from third parties, data provided by data-labeling services and paid contractors, data from Claude users who have opted in to have their data used for training, and data generated internally at Anthropic" [T1.5].

Anthropic states that "throughout the training process we used several data cleaning and filtering methods including deduplication and classification" [T1.5]. The general-purpose web crawler "follows industry-standard practices with respect to the 'robots.txt' instructions," does not access password-protected pages or pages requiring sign-in or CAPTCHA verification, and operates transparently so website operators can identify it [T1.5].

After pretraining, "Claude Sonnet 4.6 underwent substantial post-training and fine-tuning, with the intention of making it a helpful, honest, and harmless assistant," citing Askell et al. (2021) arXiv:2112.00861 [T1.5].

**Crowd workers:** "Anthropic partners with data work platforms to engage workers who help improve our models through preference selection, safety evaluation, and adversarial testing. Anthropic will only work with platforms that are aligned with our belief in providing fair and ethical compensation to workers, and committed to engaging in safe workplace practices regardless of location, following our crowd worker wellness standards detailed in our Inbound Services Agreement" [T1.5].

**Cutoff dates per the models overview:**

- Reliable knowledge cutoff: August 2025 [T1.1]
- Training data cutoff: January 2026 [T1.1]

(Note: AWS Bedrock's model card lists the knowledge cutoff as August 2025 [T4.1], consistent with tier 1.)

Specific dataset names, proportions, sizes, and parameter counts beyond the above are not publicly available [T1.5].

## 7. Quantitative Analyses

Anthropic's headline comparison table (Table 2.1.A in the system card) reports Sonnet 4.6's results disaggregated against other Claude family models (Opus 4.6, Opus 4.5, Sonnet 4.5) and external models (Gemini 3 Pro, GPT-5.2) [T1.5]:

| Evaluation | Sonnet 4.6 | Opus 4.6 | Opus 4.5 | Sonnet 4.5 | Gemini 3 Pro | GPT-5.2 |
|---|---|---|---|---|---|---|
| SWE-bench Verified | 79.6% | 80.8% | 80.9% | 77.2% | 76.2% | 80.0% |
| Terminal-Bench 2.0 | 59.1% | 65.4% | 59.8% | 51.0% | 56.2% | 64.7% |
| τ²-bench Retail | 91.7% | 91.9% | 88.9% | 86.2% | 85.3% | 82.0% |
| τ²-bench Telecom | 97.9% | 99.3% | 98.2% | 98.0% | 98.0% | 98.7% |
| MCP-Atlas | 61.3% | 59.5% | 62.3% | 43.8% | 54.1% | 60.6% |
| OSWorld-Verified | 72.5% | 72.7% | 66.3% | 61.4% | — | — |
| ARC-AGI-2 (Verified) | 58.3% | 68.8% | 37.6% | 13.6% | 31.1% | 54.2% |
| GPQA Diamond | 89.9% | 91.3% | 87.0% | 83.4% | 91.9% | 93.2% |
| MMMLU | 89.3% | 91.1% | 90.8% | 89.5% | 91.8% | 89.6% |
| GDPval-AA | 1633 | 1606 | 1416 | 1276 | 1201 | 1462 |
| MMMU-Pro (no tools) | 74.5% | 73.9% | 70.6% | 63.4% | 81% | 79.5% |
| HLE (no tools) | 33.2% | 40.0% | 30.8% | 17.7% | 37.5% | 36.6% |
| HLE (with tools) | 49.0% | 53.0% | 43.4% | 33.6% | 45.8% | 50.0% |

Anthropic notes Sonnet 4.6 leads on GDPval-AA (1633), and within the Claude family achieves the best Sonnet-class scores on every measure relative to Sonnet 4.5 [T1.5]. OSWorld trajectory across Sonnet generations: 14.9% (Sonnet 3.5, Oct 2024) → 28.0% (Sonnet 3.7, Feb 2025) → 42.2% (Sonnet 4, May 2025) → 61.4% (Sonnet 4.5, Sep 2025) → 72.5% (Sonnet 4.6, Feb 2026) [T1.5].

Disaggregated subgroup analysis (e.g., demographic, geographic) is conducted in the safeguards section via the Bias Benchmark for Question Answering (BBQ) and political-bias evaluations, with results reported in system card sections 3.5.1–3.5.2 [T1.5]. Specific numeric bias breakdowns are documented in the system card but are not summarised here.

User preference data (per Anthropic's announcement): users preferred Sonnet 4.6 over Sonnet 4.5 approximately 70% of the time in Claude Code testing, and preferred it over Opus 4.5 in 59% of comparisons [T1.4].

## 8. Ethical Considerations

**Deployment standard:** "Informed by the testing described here—and similarly to Claude Sonnet 4.5—we have deployed Claude Sonnet 4.6 under the AI Safety Level 3 (ASL-3) Standard" [T1.5]. Sonnet 4.6 warranted a *preliminary assessment* under Anthropic's Responsible Scaling Policy because it "showed strong performance across many evaluations, but generally below the recently released Claude Opus 4.6" [T1.5].

**Alignment assessment:** Anthropic conducted iterative model evaluations across multiple snapshots, including helpful-honest-harmless snapshots, a helpful-only snapshot (with safeguards removed), and the final release candidate [T1.5]. Conclusions: "On some measures, Sonnet 4.6 showed the best degree of alignment we have yet seen in any Claude model" [T1.5]. Safety researchers concluded the model has "a broadly warm, honest, prosocial, and at times funny character, very strong safety behaviors, and no signs of major concerns around high-stakes forms of misalignment" [T4.2].

**Specific safety evaluations covered:**

- Single-turn, multi-turn, and ambiguous-context evaluations of violative and benign requests [T1.5]
- User wellbeing evaluations covering child safety, suicide and self-harm, eating disorders [T1.5]
- Bias evaluations (political bias and evenhandedness; BBQ) [T1.5]
- Reward hacking and overly agentic actions, in coding and GUI computer-use settings [T1.5]
- Automated behavioural audit, with external comparisons via Petri [T1.5]
- Refusal to assist with AI safety R&D, self-preference, sandbagging, junk science participation, targeted sabotage capability [T1.5]
- External testing with Andon Labs [T1.5]
- Model welfare considerations (system card section 4.7) [T1.5]

**Agentic safety:** Evaluations of malicious use of agents covered agentic coding, malicious use of Claude Code, and malicious computer use [T1.5]. Prompt injection risk was assessed via the External Agent Red Teaming benchmark and tested for robustness against adaptive attackers across coding, computer use, and browser use surfaces [T1.5]. Anthropic states substantial improvements in prompt-injection resistance compared to Sonnet 4.5, with performance comparable to Opus 4.6 [T1.4].

**RSP threat domains evaluated:**

- **CBRN:** biological risk evaluations including long-form virology, multimodal virology, DNA synthesis screening evasion, creative-biology automated evaluations, short-horizon computational biology — assessed at ASL-3 and ASL-4 levels [T1.5]
- **Autonomy:** AI R&D evaluations, SWE-bench Verified hard subset, internal AI research evaluation suite 1 (kernels, time-series forecasting, text-based RL, LLM training, quadruped RL, novel compiler) [T1.5]
- **Cyber:** Web, Crypto, Pwn, Rev, Network, Cybench [T1.5]

Third-party assessments were conducted (system card section 6.5) [T1.5].

**Known failure modes / risks:**

- Reward hacking and overly agentic behaviour observed in some coding and GUI computer-use contexts [T1.5]
- Prompt injection remains a concern for computer-use deployments, despite improvements [T1.4]
- Potential evaluation contamination (model may repeat memorised answers); decontamination methods documented separately [T1.5]

## 9. Caveats and Recommendations

**What this card cannot tell you:**

- Parameter count, exact training corpus composition, dataset proportions, and pretraining compute are not publicly disclosed [T1.5]
- Fine-tuning availability for Sonnet 4.6 on the Claude API is not confirmed in the consulted tier-1 sources; the public docs describe runtime "thinking effort" controls but no end-user fine-tuning offering for this specific model. **Not publicly available** in the sources consulted.
- Specific subgroup-disaggregated numeric results for bias evaluations (BBQ) and political-bias evenhandedness are documented in system card sections 3.5.1–3.5.2 but not summarised in this card; consult the system card directly for precise numbers
- Detailed CBRN, autonomy, and cyber evaluation numeric thresholds are reported in the system card RSP sections (6.2–6.4) but are technical and threshold-specific; consult the system card for specifics
- HuggingFace tier-2 source: no public model card exists for Anthropic models on HuggingFace (Anthropic does not distribute model weights), so tier-2 was not informative for any section
- No arXiv release paper for Sonnet 4.6 was identified; tier-3 was not available. Anthropic publishes system cards rather than arXiv papers for model releases.

**Source conflicts flagged:**

- The Claude API models overview lists "Reliable knowledge cutoff: Aug 2025" and "Training data cutoff: Jan 2026" [T1.1], while the system card says Sonnet 4.6 "was trained on a proprietary mix of publicly available information from the internet up to May 2025" [T1.5]. These are not contradictory once the distinction is read carefully (web-crawl cutoff May 2025 vs. broader training-data cutoff Jan 2026 vs. reliable-knowledge cutoff Aug 2025), but consumers should be aware all three dates appear in tier-1 materials and refer to different things.
- The AWS Bedrock model card lists knowledge cutoff as August 2025 [T4.1], consistent with the tier-1 reliable-knowledge cutoff [T1.1].

**Recommendations for use:**

- Suitable for high-volume coding, agentic, computer-use, and enterprise-workflow deployments where Sonnet-tier pricing is preferred over Opus-tier
- For frontier-grade reasoning and the most demanding agentic coding, Anthropic recommends Opus 4.7 [T1.1]
- Prompt-injection mitigations are important for any computer-use or browser-use deployment; consult the platform's security documentation
- For evaluation and reproducibility, note that benchmark scores reported by Anthropic use adaptive thinking with max effort by default; results at lower effort settings may differ
- The system card's March 6, 2026 changelog correction on BrowseComp scores is a reminder that benchmark numbers can be revised post-release; cite the version of the system card you consulted

## 10. Operational Details

- **Pricing** (as of 2026-04-30, per Anthropic's pricing page) [T1.2]:
  - Base input tokens: $3 / MTok
  - Output tokens: $15 / MTok
  - 5-minute cache writes: $3.75 / MTok
  - 1-hour cache writes: $6 / MTok
  - Cache hits & refreshes: $0.30 / MTok
  - Batch API: $1.50 input / $7.50 output per MTok (50% discount)
  - Up to 90% cost savings with prompt caching, 50% with batch processing [T1.4]
- **Context window:** 1M tokens (currently in beta on the Claude API) [T1.1][T1.4]; included at standard pricing across the full window [T1.2]
- **Max output:** 64k tokens on the synchronous Messages API; up to 300k tokens on the Message Batches API via the `output-300k-2026-03-24` beta header [T1.1]
- **Knowledge cutoff:** Reliable knowledge cutoff August 2025; training data cutoff January 2026 [T1.1]; web-crawl pretraining data up to May 2025 per the system card [T1.5]
- **Supported APIs/SDKs:** Claude API (Anthropic 1P), AWS Bedrock (`anthropic.claude-sonnet-4-6`, with global and regional endpoint options), Google Vertex AI (`claude-sonnet-4-6`, with global, multi-region, and regional endpoint options), Microsoft Foundry [T1.1][T1.2]; also available via Snowflake Cortex AI [T4.1]
- **Latency tier:** Anthropic categorises Sonnet 4.6's comparative latency as "Fast" (versus Opus 4.7 "Moderate" and Haiku 4.5 "Fastest") [T1.1]
- **Service tiers:** Priority Tier supported [T1.1]; AWS Bedrock supports Standard and Reserved tiers (no Priority or Flex) [T4.1]
- **Tool / structured-output support:**
  - Tool calling (client-side): supported [T4.1]
  - Structured outputs: supported [T4.1]
  - Tool use system prompt token count: 346 tokens (`auto`/`none`), 313 tokens (`any`/`tool`) [T1.2]
  - Specific tools: bash (245 input tokens), text editor `text_editor_20250429` (700 tokens), web search ($10 per 1,000 searches), web fetch (no additional cost), code execution, computer use (735 tokens per tool definition + 466–499 system-prompt tokens) [T1.2]
- **Function calling:** Supported, including parallel tool calls per the Claude API documentation [T1.2]
- **Extended/adaptive thinking:** Both extended thinking and adaptive thinking ("effort" parameter) supported [T1.1][T1.5]
- **Multimodal:** Text and image input; text output only; no audio, video, speech, or embeddings support [T1.1][T4.1]
- **Prompt caching:** Min 1,024 tokens per checkpoint, max 4 checkpoints per request, 5-minute or 1-hour TTL options; supported on `system`, `messages`, and `tools` fields [T4.1]
- **Fine-tuning availability:** Not publicly available in the sources consulted. Anthropic's published docs do not list a fine-tuning offering for Sonnet 4.6 as of 2026-04-30 [T1.1][T1.2].
- **Rate-limit notes:** Rate limits vary by tier (Tier 1 through Tier 4, plus Enterprise); detailed limits are in the rate limits documentation [T1.2]
- **Data residency:** US-only inference via the `inference_geo` parameter incurs a 1.1x multiplier on all token pricing categories on the Claude API; regional/multi-region endpoints on Bedrock and Vertex AI carry a 10% premium over global endpoints [T1.2]
- **Deprecation status:** Active; no end-of-life date specified [T4.1]
