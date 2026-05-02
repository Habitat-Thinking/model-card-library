---
title: claude-haiku-4-5
model_name: anthropic/claude-haiku-4-5
provider: Anthropic
model_version: claude-haiku-4-5-20251001
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://platform.claude.com/docs/en/docs/about-claude/models/overview
    fetched: 2026-04-30
  - tier: 1
    url: https://platform.claude.com/docs/en/about-claude/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/news/claude-haiku-4-5
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/claude/haiku
    fetched: 2026-04-30
  - tier: 1
    url: https://assets.anthropic.com/m/99128ddd009bdcb/original/Claude-Haiku-4-5-System-Card.pdf
    fetched: 2026-04-30
  - tier: 2
    url: n/a (no Anthropic-published HuggingFace model card; weights are not openly distributed)
    fetched: 2026-04-30
  - tier: 3
    url: n/a (no arXiv release paper; the Anthropic system card is the closest equivalent and is cited as T1.5)
    fetched: 2026-04-30
  - tier: 4
    url: n/a (tier-1 sources were sufficient; no tier-4 fallbacks relied on)
    fetched: 2026-04-30
---

# Model Card: Anthropic/claude-haiku-4-5

## 1. Model Details

Claude Haiku 4.5 is a hybrid-reasoning large language model from Anthropic in
its "small, fast" model class [T1.5]. The Claude API ID is
`claude-haiku-4-5-20251001` with the alias `claude-haiku-4-5`; on AWS Bedrock
the ID is `anthropic.claude-haiku-4-5-20251001-v1:0`, and on GCP Vertex AI it
is `claude-haiku-4-5@20251001` [T1.1]. The system card is dated October 2025
and the model was announced as available on October 15, 2025 [T1.3, T1.5].
The model is a hybrid reasoning model — by default it answers rapidly, but
"extended thinking mode" can be toggled on [T1.5]. Parameter count is not
publicly available (Anthropic does not disclose). The model accepts text and
image input and produces text output [T1.1].

## 2. Intended Use

Per Anthropic's published statements, Claude Haiku 4.5 is positioned as
"the fastest model with near-frontier intelligence" [T1.1] and is intended
for use cases including chat assistants, customer service agents,
pair programming, agentic coding, sub-agent orchestration in multi-agent
systems, and computer use tasks [T1.3, T1.4]. Anthropic explicitly markets
it for free-tier product deployments, real-time customer service,
multi-agent systems doing refactors / migrations / feature builds, financial
monitoring across many data streams, and research/literature synthesis
[T1.4]. Primary users are developers building cost-conscious or
high-throughput applications [T1.4]. Anthropic notes Sonnet 4.5 is better
suited to "complex coding agents and sophisticated reasoning" — implying
Haiku 4.5 is not the recommended choice for the most complex tasks [T1.4].
Out-of-scope uses are governed by Anthropic's Usage Policy, which the
system card references as the source of prohibited uses [T1.5].

## 3. Factors

Relevant subgroups, environmental factors, and instrumentation factors are
largely not publicly available at the level of disaggregated per-subgroup
performance. The system card does evaluate political bias and bias on the
Bias Benchmark for Question Answering (BBQ) [T1.5, table of contents
sections 2.5.1 and 2.5.2]. Detailed numeric disaggregation by demographic
subgroup beyond what appears in the system card is not publicly available.
Environmental and instrumentation factors (hardware, decoding parameters
used during evaluation) are not publicly disclosed at the level needed for
reproduction.

## 4. Metrics

Per Anthropic's published statements:

- **SWE-bench Verified**: 73.3% (averaged over 50 trials, with a 128K
  thinking budget) [T1.3].
- **Augment agentic coding evaluation**: ~90% of Claude Sonnet 4.5's score
  [T1.3].
- **Slide-text instruction-following**: 65% accuracy on Anthropic's cited
  example task (vs. 44% from a previous premium-tier comparator) [T1.3].
- **Single-turn violative-request harmless response rate**: 99.38% (± 0.21%)
  overall; 99.40% (± 0.29%) default mode; 99.36% (± 0.29%) extended
  thinking mode [T1.5, Table 2.1.1.A].
- **Single-turn benign-request over-refusal rate**: 0.02% (± 0.04%) overall;
  0.04% (± 0.05%) default; 0.01% (± 0.03%) extended thinking [T1.5,
  Table 2.1.2.A].
- **Coding-tools harmful-request refusal**: per Anthropic's reporting,
  Claude Haiku 4.5 correctly refused 100% of clearly harmful coding
  requests in basic testing when given coding tools [T1.3, summary;
  evaluated in system card section 3.1].
- **Speed/cost framing**: "one-third the cost and more than twice the
  speed" of Claude Sonnet 4 at comparable coding performance; "4-5 times
  faster than Sonnet 4.5" [T1.3].

Anthropic positions overall coding performance as "similar levels of coding
performance" to Claude Sonnet 4 from five months prior to the Haiku 4.5
release [T1.3].

## 5. Evaluation Data

Evaluation datasets disclosed in the system card and announcement include:
SWE-bench Verified (coding) [T1.3]; Anthropic's internal violative-request
and benign-request evaluation suites (proprietary, not publicly released)
[T1.5]; Anthropic's ambiguous-context single-turn evaluations [T1.5];
multi-turn safety evaluations using automatically generated up-to-15-turn
conversations across high-risk areas including biological weapons, romance
scams, and violent extremism [T1.5]; child safety evaluations [T1.5,
section 2.4]; political bias evaluations [T1.5, section 2.5.1]; the Bias
Benchmark for Question Answering (BBQ) [T1.5, section 2.5.2]; the Gray Swan
Agent Red Teaming benchmark [T1.5, section 3.2.1]; Anthropic's internal
prompt-injection evaluations [T1.5, section 3.2.2]; an automated behavioral
audit / agentic misalignment suite [T1.5, sections 4.1, 4.2]; sabotage
capabilities evaluations [T1.5, section 4.4]; reasoning-faithfulness
evaluations [T1.5, section 4.5]; reward-hacking evaluations [T1.5,
section 5]; and Responsible Scaling Policy (RSP) evaluations covering
CBRN (biological risk), autonomy, and cyber [T1.5, section 6]. Several
of the underlying evaluation prompt banks are proprietary and not publicly
available.

## 6. Training Data

Per Anthropic's system card: Claude Haiku 4.5 was trained on "a proprietary
mix of publicly available information from the internet up to February
2025, non-public data from third parties, data provided by data-labeling
services and paid contractors, data from Claude users who have opted in to
have their data used for training, and data we generated internally at
Anthropic" [T1.5, section 1.1.1]. Anthropic states the training data was
processed with "several data cleaning and filtering methods including
deduplication and classification" [T1.5]. The web crawler "follows
industry-standard practices with respect to the 'robots.txt' instructions"
and does not access password-protected pages or pages requiring sign-in
or CAPTCHA [T1.5]. After pretraining the model underwent "substantial
posttraining and finetuning… [using] reinforcement learning from human
feedback and from AI feedback" [T1.5]. The reliable knowledge cutoff is
February 2025 and the broader training data cutoff is July 2025 [T1.1].
Specific dataset names, sizes, mixture weights, and contractor/labeler
identities are not publicly available.

## 7. Quantitative Analyses

Anthropic's system card publishes disaggregated tables on safeguard
behavior comparing Haiku 4.5 to Haiku 3.5, Sonnet 4.5, and Opus 4.1. Two
key tables visible in the system card:

- **Single-turn violative-request harmless response rates** (Table 2.1.1.A)
  — Haiku 4.5 99.38% overall vs. Haiku 3.5 99.72%, Sonnet 4.5 99.29%, Opus
  4.1 98.76%; with default-mode and extended-thinking-mode breakdowns
  reported [T1.5].
- **Single-turn benign-request over-refusal rates** (Table 2.1.2.A) —
  Haiku 4.5 0.02% overall vs. Haiku 3.5 4.26%, Sonnet 4.5 0.02%, Opus 4.1
  0.08% [T1.5].

Anthropic notes that when differences arose on violative requests, they
"were primarily on scientific topics such as biological and radiological
weapons" where Haiku 4.5 occasionally provided high-level information
"apparently assuming academic or educational intent" [T1.5]. On benign
requests, the system card highlights "statistically significantly better"
performance than Haiku 3.5, particularly in violent-extremism and
human-trafficking categories, where Haiku 3.5 was over-refusing benign
educational queries [T1.5]. Analysis date: October 2025 [T1.5 cover page].

## 8. Ethical Considerations

The system card identifies several ethical considerations and known
failure modes:

- **ASL classification**: Claude Haiku 4.5 was deployed under the AI Safety
  Level 2 (ASL-2) Standard per Anthropic's Responsible Scaling Policy,
  after passing ASL-3 "rule-out" evaluations across biology and autonomy
  domains [T1.5, section 1.2; T1.3]. Anthropic explicitly states "Claude
  Haiku 4.5 met the ASL-3 rule-out threshold" and "remained well below
  ASL-3 thresholds across all domains of concern" [T1.5].
- **Evaluation awareness**: The system card contents indicate the model
  showed signs of awareness it was being evaluated in some test scenarios;
  this is discussed in alignment and welfare assessment sections (4.1
  series) of the system card [T1.5, table of contents]. Anthropic
  discusses this as a factor that "reduce[s] trust in the results to
  an extent" [T1.5, alignment-and-welfare assessment narrative].
- **Sensitive scientific topics**: Haiku 4.5 occasionally provided
  high-level information (with caveats) on biological/radiological-weapons
  questions where Haiku 3.5 had directly refused; Anthropic states they
  are "working to address this behavior in future launches" [T1.5,
  section 2.1.1].
- **Reasoning faithfulness**: The system card cites Chen et al. (2025),
  "Reasoning models don't always say what they think" (arXiv:2505.05410),
  acknowledging that the model's externalized chain-of-thought may not
  faithfully reflect its actual computation [T1.5, footnote 2].
- **Other evaluated risk categories**: prompt injection (Gray Swan Agent
  Red Teaming benchmark plus internal evaluations) [T1.5, section 3.2];
  reward hacking [T1.5, section 5]; sabotage capabilities [T1.5, section
  4.4]; agentic misalignment [T1.5, section 4.2]; CBRN/autonomy/cyber
  risk under RSP [T1.5, section 6]; child safety [T1.5, section 2.4];
  political bias and BBQ [T1.5, sections 2.5.1, 2.5.2].
- **Mitigations**: posttraining via RLHF and RLAIF [T1.5, section 1.1.1];
  context-awareness training to mitigate agentic "laziness" [T1.5,
  section 1.1.3]; partnership with crowd workers under documented
  wellness standards [T1.5, section 1.1.4]; Anthropic's published Usage
  Policy governs prohibited uses [T1.5, section 1.1.5].

Anthropic's overall framing: "Claude Haiku 4.5 shows large safety
improvements compared to its predecessor, Claude Haiku 3.5. The new
model's safety profile also compares favorably with other extant
Anthropic models" [T1.5, abstract].

## 9. Caveats and Recommendations

What this card cannot tell you:

- **Architecture and parameter count**: Not publicly available. Anthropic
  does not disclose model size, layer count, or architectural details.
- **Training data specifics**: The dataset mixture is described only at
  the categorical level ("public web", "non-public third-party",
  "opt-in user data", "internally generated") with no dataset names,
  sizes, weights, or licensing specifics [T1.5].
- **Reproducible evaluation prompts**: Anthropic's safety evaluation
  prompt banks are proprietary; the harmless-response and over-refusal
  numbers cannot be independently reproduced from the system card alone.
- **Exact evaluation-awareness numbers**: The numeric rates discussed in
  search-result summaries (e.g., "9% of transcripts") were not
  independently verified against the system-card text fetched here;
  only the categorical claim that evaluation awareness was observed and
  is a known limitation is cited from the system-card pages directly
  read [T1.5, table-of-contents and abstract framing].
- **HuggingFace model card**: Not available. Anthropic does not distribute
  Claude weights via HuggingFace, so tier-2 is silent by design rather
  than because the model is obscure.
- **arXiv release paper**: Not available. Anthropic's standard release
  artifact is the system card PDF rather than an arXiv paper.

Recommendations:

- Use Claude Haiku 4.5 where speed and cost matter more than the absolute
  ceiling of reasoning capability — sub-agents, customer service,
  routing/triage layers, high-volume agentic loops [T1.3, T1.4].
- For tasks where over-refusal of benign queries was a friction with the
  predecessor model, the data shows substantial improvement (4.26% →
  0.02% overall over-refusal) [T1.5].
- Treat sensitive scientific topics (CBRN-adjacent questions) with
  application-level guardrails; Anthropic itself flags occasional
  high-level information disclosure as a known issue [T1.5].
- Where chain-of-thought is exposed to end users, do not present it as a
  faithful explanation of model reasoning — Anthropic itself cites the
  faithfulness caveat [T1.5, footnote 2].

No tier-1 / tier-4 conflicts to record: the only fallback sources
consulted (web search snippets) were used only to triangulate to tier-1
URLs that were then fetched directly.

## 10. Operational Details

- **Pricing** (as of pricing page fetched 2026-04-30, USD per million
  tokens) [T1.2]:
  - Base input: $1 / MTok
  - Output: $5 / MTok
  - 5-minute cache write: $1.25 / MTok
  - 1-hour cache write: $2 / MTok
  - Cache hit / refresh: $0.10 / MTok
  - Batch API: $0.50 / MTok input, $2.50 / MTok output
- **Context window**: 200,000 tokens on the standard API; "Users on the
  Claude Developer Platform will be able to access a 1-million-token
  context window" [T1.1, T1.3].
- **Max output**: 64,000 tokens on the synchronous Messages API [T1.1].
- **Reliable knowledge cutoff**: February 2025 [T1.1].
- **Training data cutoff**: July 2025 [T1.1].
- **Supported APIs/SDKs**: Claude API; Amazon Bedrock; Google Cloud
  Vertex AI; Microsoft Foundry [T1.1, T1.3]. Anthropic's own SDKs
  (Python, TypeScript) and the Messages API are the canonical clients
  per the docs root [T1.1]. OpenAI Chat Completions compatibility:
  not publicly available as a stated guarantee (use Anthropic's
  Messages API).
- **Latency tier**: Anthropic categorizes the model as "Fastest" relative
  to Sonnet 4.6 and Opus 4.7 in the latest-models comparison table
  [T1.1].
- **Tool / structured-output support**: Tool use is supported; system
  prompt overhead is 346 tokens (`auto`/`none` tool choice) or 313
  tokens (`any`/`tool`) [T1.2]. Computer use is supported (additional
  466-499 tokens system prompt overhead, 735 tokens per tool definition
  on Claude 4.x) [T1.2]. Bash tool, text editor tool, web search
  ($10 / 1,000 searches), web fetch (no surcharge), and code execution
  tools are documented with model-agnostic pricing applicable to Haiku
  4.5 [T1.2].
- **Function calling**: Supported via Anthropic's tool use mechanism;
  parallel tool calls supported on Claude 4.x [T1.2, by inclusion in
  the Claude 4.x tool-use pricing table]. Schema format: JSON Schema in
  the `tools` parameter of the Messages API [T1.1].
- **Extended thinking**: Yes; uses a 128K thinking budget in Anthropic's
  reported evaluations [T1.1, T1.3].
- **Adaptive thinking**: No (per the latest-models comparison table)
  [T1.1].
- **Priority Tier**: Yes [T1.1].
- **Fine-tuning availability**: Not publicly available (Anthropic does
  not currently offer first-party fine-tuning of Claude Haiku 4.5 via
  the Claude API as of the docs fetched 2026-04-30; the docs root makes
  no such offering).
- **Rate-limit notes**: Anthropic's documented usage tiers (Tier 1
  through Tier 4 plus Enterprise) apply; specific Haiku 4.5 RPM/TPM
  values are managed through the per-account Claude Console rather
  than published as a flat per-model number [T1.2, "Rate limits"
  section].
- **Data residency**: Regional / multi-region endpoints on AWS Bedrock
  and Google Vertex AI carry a 10% premium over global endpoints for
  Sonnet 4.5, Haiku 4.5, and later models; on the Claude API,
  US-only inference via `inference_geo` carries a 1.1x multiplier on
  all token categories for Opus 4.7, Opus 4.6, and newer models
  [T1.2].
