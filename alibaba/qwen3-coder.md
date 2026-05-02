---
title: qwen3-coder
parent: Alibaba
model_name: alibaba/qwen3-coder
provider: Alibaba
model_version: qwen3-coder (family; flagship Qwen3-Coder-480B-A35B-Instruct, plus Qwen3-Coder-30B-A3B-Instruct, Qwen3-Coder-Flash, Qwen3-Coder-Plus, Qwen3-Coder-Next variants)
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://qwenlm.github.io/blog/qwen3-coder/
    fetched: 2026-04-30
  - tier: 1
    url: https://www.alibabacloud.com/help/en/model-studio/qwen-coder
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct
    fetched: 2026-04-30
  - tier: 3
    url: https://arxiv.org/abs/2603.00729
    fetched: 2026-04-30
  - tier: 4
    url: https://cloudprice.net/models/openrouter/qwen/qwen3-coder-flash
    fetched: 2026-04-30
  - tier: 4
    url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    fetched: 2026-04-30
---

# Model Card: Alibaba/qwen3-coder

## 1. Model Details

Qwen3-Coder is a family of code-specialised large language models released by the Qwen Team at Alibaba Cloud [T1.1]. The flagship variant, Qwen3-Coder-480B-A35B-Instruct, is a Mixture-of-Experts (MoE) causal language model with 480 billion total parameters and 35 billion active parameters per token, comprising 62 layers, 96 query heads / 8 KV heads (Grouped Query Attention), and 160 experts with 8 activated per token [T2.1]. The flagship was announced on the Qwen blog on July 22, 2025 [T1.1].

A smaller open-weight sibling, Qwen3-Coder-30B-A3B-Instruct, is also released: 30.5B total / 3.3B active parameters, 48 layers, 32 Q / 4 KV heads, 128 experts with 8 activated [T2.2]. Both flagship variants are distributed under the Apache 2.0 license on HuggingFace [T2.1][T2.2].

The Alibaba Cloud Model Studio product surface exposes the family under additional API names: `qwen3-coder-plus` (for highest-quality complex tasks), `qwen3-coder-next` (the recommended balance of quality, speed, and cost), and `qwen3-coder-flash` [T1.2][T4.1]. Qwen3-Coder-Next is described in a follow-up technical report (arXiv:2603.00729, submitted February 28, 2026) as an 80-billion-total / 3-billion-active-parameter MoE model targeted at coding agents, with both base and instruction-tuned open-weight versions released [T3.1].

The models operate in non-thinking mode only — they do not emit `<think></think>` blocks [T2.1][T2.2].

## 2. Intended Use

Per the provider's published statements, Qwen3-Coder is designed for agentic coding tasks: code generation and understanding, multi-turn tool calling, browser-based agent operations, and repository-scale code analysis [T1.1][T2.1]. The Qwen Team explicitly positions the flagship as achieving "state-of-the-art results among open models on Agentic Coding, Agentic Browser-Use, and Agentic Tool-Use, comparable to Claude Sonnet 4" [T1.1].

Primary integration paths called out by the provider are Qwen Code (their own CLI), Claude Code integration, and Cline support [T1.1]. The HuggingFace model cards additionally name CLINE, Ollama, LM Studio, MLX-LM, llama.cpp, KTransformers, and OpenAI-API-compatible endpoints as supported runtimes [T2.1][T2.2].

The Alibaba Cloud Model Studio guidance recommends "lower temperature for deterministic results" and limiting tools to no more than 20 per request [T1.2].

Out-of-scope uses are not explicitly enumerated in tier-1 documentation. "Not publicly available" for explicit out-of-scope statements.

## 3. Factors

Relevant subgroups, environmental factors, and instrumentation factors are not disclosed by the provider in the tier-1 blog or HuggingFace cards [T1.1][T2.1]. The flagship model card calls out "repository-scale understanding" as a deliberate optimisation factor enabled by the long context window [T2.1], and the Qwen3-Coder-Next paper notes that training emphasised "verifiable coding tasks paired with executable environments" so that the model learns from environment feedback [T3.1] — both are instrumentation factors at training time rather than disaggregated evaluation factors.

Disaggregated performance across programming languages, code domains, or developer subgroups: Not publicly available.

## 4. Metrics

The Qwen team reports the following provider-stated benchmarks for the flagship Qwen3-Coder-480B-A35B-Instruct:

- SWE-Bench Pro: 38.7 [T2.1]
- Terminalbench 2: 23.9 [T2.1]
- Evasion Bench: 78.16 [T2.1]
- Qualitative claim: "comparable to Claude Sonnet 4" on Agentic Coding, Agentic Browser-Use, and Agentic Tool-Use [T1.1]

For Qwen3-Coder-Next (80B-A3B), the technical report states the model "achieves competitive performance relative to its active parameter count" on SWE-Bench and Terminal-Bench, but does not publish numeric scores in the abstract [T3.1].

Per-variant pricing-tier latency / throughput metrics: Not publicly available.

## 5. Evaluation Data

Per the provider's published statements, evaluation was performed on:

- SWE-Bench (and SWE-Bench Verified / SWE-Bench Pro variants) [T1.1][T2.1][T3.1]
- Terminal-Bench / Terminalbench 2 [T2.1][T3.1]
- Evasion Bench [T2.1]
- Provider-described "Agentic Coding, Agentic Browser-Use, and Agentic Tool-Use" benchmark suites (specific datasets not enumerated in tier-1 blog) [T1.1]

Composition, license, and contamination-mitigation procedures for these benchmark sets beyond the public benchmark definitions: Not publicly available.

## 6. Training Data

Per the provider's published statements for the flagship Qwen3-Coder-480B-A35B-Instruct, pretraining used 7.5 trillion tokens with a 70% code ratio, with synthetic data cleaning performed via Qwen2.5-Coder [T1.1]. Post-training used Code RL and Long-Horizon RL across real-world tasks [T1.1].

For Qwen3-Coder-Next, the technical report describes "agentic training through large-scale synthesis of verifiable coding tasks paired with executable environments," with mid-training and reinforcement learning stages [T3.1]. Specific dataset names, source repositories, and licensing of training corpora: Not publicly available [T3.1].

The exact composition of the pretraining corpus (programming language mix, license filtering, deduplication, PII handling) is not disclosed [T1.1][T2.1].

## 7. Quantitative Analyses

The provider has published the headline benchmark scores cited in Section 4 [T2.1]. Disaggregated performance — by programming language, by problem domain, by repository size, or across other slices — is not published in the tier-1 blog, HuggingFace cards, or the Qwen3-Coder-Next arXiv abstract [T1.1][T2.1][T3.1].

Date of the Qwen3-Coder analysis: July 22, 2025 (flagship release) [T1.1]. Date of the Qwen3-Coder-Next analysis: February 28, 2026 (arXiv submission) [T3.1].

## 8. Ethical Considerations

The tier-1 blog post and HuggingFace model cards do not contain a dedicated ethical considerations section [T1.1][T2.1][T2.2]. The Qwen3-Coder-Next arXiv abstract similarly does not enumerate risks, mitigations, or known failure modes [T3.1].

Risks inherent to a code-specialised, agentic-tool-using LLM that the provider has not explicitly addressed include, but are not limited to: insecure-code generation, license-attribution loss when reproducing training data verbatim, prompt-injection in agentic browser-use scenarios, and tool-call privilege escalation. Per the honesty rules of this card, these are not provider-attested claims and are flagged as gaps rather than asserted as the provider's position. "Not publicly available" for provider-stated risk taxonomy and mitigations.

## 9. Caveats and Recommendations

What this card cannot tell you, and why:

- **Out-of-scope uses, ethical risk taxonomy, and mitigations** are not enumerated in any consulted tier-1 or tier-3 source [T1.1][T2.1][T3.1]. Operators integrating Qwen3-Coder into agentic workflows should run their own threat model rather than relying on a provider safety profile.
- **Training data composition** is described only at a tokens/code-ratio level [T1.1]. License auditability of generated code is the operator's responsibility.
- **Disaggregated benchmark performance** (per-language, per-domain) is not published [T2.1].
- **Knowledge cutoff** is not stated on the Qwen blog or the HuggingFace cards consulted [T1.1][T2.1][T2.2].

Conflicts between sources flagged for the reader: The flagship HuggingFace card lists "May 14, 2025 (arXiv: 2505.09388)" as a release date, but arXiv 2505.09388 is the **Qwen3 Technical Report** for the general Qwen3 family rather than a Qwen3-Coder-specific paper [T2.1]. The Qwen blog dates the Qwen3-Coder flagship announcement to July 22, 2025 [T1.1]. Per the honesty rules, tier-1 (blog) wins; readers should treat July 22, 2025 as the flagship release date and arXiv 2603.00729 (February 28, 2026) as the Qwen3-Coder-Next technical report rather than treating arXiv 2505.09388 as a Qwen3-Coder release paper.

Recommendations for use, given documented strengths:

- Strong choice for agentic coding scaffolds (tool calling, repo-scale context, multi-turn SWE-Bench-style work) [T1.1].
- For cost-sensitive scenarios, the provider explicitly recommends `qwen3-coder-next` as the default; reserve `qwen3-coder-plus` for highest-complexity tasks [T1.2].
- For self-hosted deployment, the 30B-A3B variant offers the same agentic-coding behavioural profile at a fraction of the activation cost [T2.2].

## 10. Operational Details

- **Pricing** — per third-party aggregators (tier 4, as the Alibaba Cloud Model Studio public pricing page does not publish exact qwen3-coder rates inline at fetch time):
  - `qwen3-coder-30b-a3b-instruct`: ~$0.07 / M input tokens; ~$0.27 / M output tokens [T4.1]
  - `qwen3-coder-flash`: ~$0.195 / M input tokens; ~$0.975 / M output tokens [T4.1]
  - `qwen3-coder-plus`: tiered pricing with context-cache support (implicit cache at 20% of standard rate, explicit cache at 10%) [T1.2]
  - As-of date: 2026-04-30 [T4.1][T4.2]
  - New users in the Singapore region receive a 90-day free quota of 1M tokens per Qwen-Coder model [T4.1]
- **Context window** — 262,144 tokens (256K) native; extendable to 1,000,000 tokens via Yarn extrapolation on the open-weight flagship [T2.1]. Qwen3-Coder-Flash advertises a 1.0M context window with up to 66K output tokens [T4.1]. Recommended max output: 65,536 tokens [T2.1][T2.2].
- **Knowledge cutoff** — Not publicly available [T1.1][T2.1].
- **Supported APIs/SDKs** — Alibaba Cloud Model Studio API; OpenAI-Chat-Completions-compatible endpoints; HuggingFace Transformers; Ollama, LM Studio, MLX-LM, llama.cpp, KTransformers for local inference [T1.2][T2.1][T2.2].
- **Latency tier** — Not publicly stated as a discrete tier; the Model Studio docs position `qwen3-coder-flash` and `qwen3-coder-next` as the lower-latency / lower-cost choices and `qwen3-coder-plus` as the highest-quality tier [T1.2][T4.1].
- **Tool / structured-output support** — Extensive tool-calling support is a primary design goal; multi-turn tool calling and agentic tool compatibility are explicitly called out [T1.2][T2.1]. The provider recommends limiting tools to ≤20 per request [T1.2].
- **Function calling** — Supported, including multi-turn and parallel agentic tool use; schema format follows OpenAI-compatible function-calling conventions on the Model Studio API [T1.2][T2.1].
- **Fine-tuning availability** — Open-weight variants (Apache 2.0) on HuggingFace can be fine-tuned by the operator [T2.1][T2.2]. Provider-managed fine-tuning offering on Alibaba Cloud Model Studio for the closed `-plus` / `-next` variants: Not publicly available from the consulted pages [T1.2].
- **Rate-limit notes** — Dual-threshold rate limiting (RPM and TPM); specific quotas vary by model and are documented in the Model Studio rate-limiting reference [T1.2]. Exact numeric quotas: Not publicly available from the consulted pages [T1.2].
