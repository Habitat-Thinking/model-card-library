---
title: claude-opus-4-7
parent: Anthropic
model_name: anthropic/claude-opus-4-7
provider: Anthropic
model_version: claude-opus-4-7
last_researched: 2026-04-30
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://platform.claude.com/docs/en/docs/about-claude/models
    fetched: 2026-04-30
  - tier: 1
    url: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
    fetched: 2026-04-30
  - tier: 1
    url: https://platform.claude.com/docs/en/about-claude/pricing
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/news/claude-opus-4-7
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/claude/opus
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/system-cards
    fetched: 2026-04-30
  - tier: 1
    url: https://www.anthropic.com/claude-opus-4-7-system-card
    fetched: 2026-04-30
  - tier: 2
    url: https://huggingface.co/Anthropic
    fetched: 2026-04-30
  - tier: 3
    url: n/a
    fetched: 2026-04-30
  - tier: 4
    url: https://aws.amazon.com/blogs/aws/introducing-anthropics-claude-opus-4-7-model-in-amazon-bedrock/
    fetched: 2026-04-30
  - tier: 4
    url: https://www.helpnetsecurity.com/2026/04/16/claude-opus-4-7-released/
    fetched: 2026-04-30
---

# Model Card: Anthropic/claude-opus-4-7

## 1. Model Details

Claude Opus 4.7 is Anthropic's most capable generally available model as of
this card's research date, positioned as a frontier model for complex
reasoning and agentic coding [T1.2]. The Claude API model ID is
`claude-opus-4-7`, with the same value used as both the canonical ID and
alias [T1.1]. It was announced as generally available on April 16, 2026
[T1.4][T4.1]. The model is part of the Claude 4 family, alongside Claude
Sonnet 4.6 and Claude Haiku 4.5, and replaces Claude Opus 4.6 as the
flagship Opus tier [T1.1]. Per the provider's published statements, Opus 4.7
uses a new tokenizer (distinct from earlier Claude models), which the
provider attributes as a contributor to its improved performance and which
may consume roughly 1x to 1.35x as many tokens for the same input text
compared with Opus 4.6 [T1.2][T1.3]. Parameter count is **Not publicly
available** — Anthropic does not disclose this for Claude models. The
HuggingFace `Anthropic` organization page lists no public models, so no
HuggingFace model card exists for this model [T2.1].

## 2. Intended Use

Per the provider's published statements, primary intended uses are complex
reasoning, agentic coding, long-horizon agentic work, knowledge work, vision
tasks, and memory tasks [T1.2]. Anthropic markets the model toward
"production-ready code with minimal oversight," complex AI agents, enterprise
workflows, and high-stakes tasks requiring frontier intelligence [T1.5].
Primary users include developers building AI applications via the Claude
API, business users on Pro/Max/Team/Enterprise plans, and enterprise
organizations running multi-day agentic workflows [T1.5]. The model is also
delivered through Amazon Bedrock, Google Cloud Vertex AI, and Microsoft
Foundry [T1.1].

Out-of-scope and restricted uses, per the provider's published statements,
include high-risk cybersecurity workflows that fall outside the Cyber
Verification Program — Opus 4.7 ships with real-time cybersecurity
safeguards that automatically detect and refuse such requests [T1.2][T1.4].
Legitimate security professionals (vulnerability research, penetration
testing, red-teaming) must apply to the Cyber Verification Program for
elevated access [T1.4]. The provider explicitly notes that Opus 4.7 is
"less broadly capable" than the separately offered Claude Mythos Preview
research model, which remains invitation-only under Project Glasswing
[T1.1][T1.4].

## 3. Factors

Anthropic does not publish a structured factors / disaggregated subgroup
analysis at the level of granularity Mitchell et al. propose. Per the
provider's published statements, the model supports text and image input,
text output, multilingual capabilities, and vision [T1.1]. Specific
subgroup performance breakdowns (by language, demographic, or domain) are
**Not publicly available** in the materials consulted. The system card PDF
referenced from the announcement is reported by third-party reviewers to
contain 232 pages including capability benchmarks, alignment testing,
welfare assessments, and Responsible Scaling Policy checks [T4.2]; that
PDF was not fetchable in full at research time due to size limits, so any
fine-grained factor analysis it contains is recorded here as
**Not publicly available within this card's research scope**.

Instrumentation factors documented by the provider include: tokenizer
change (new tokenizer increases token consumption ~1x–1.35x vs. Opus 4.6)
[T1.2][T1.3]; image resolution (high-resolution input up to 2576px /
3.75MP, with 1:1 pixel-to-coordinate mapping) [T1.2]; effort levels
(`xhigh` is newly recommended for coding/agentic; `high` is the recommended
floor for intelligence-sensitive uses) [T1.2]; and adaptive thinking on/off
(off by default; extended-thinking budgets are removed) [T1.2].

## 4. Metrics

Per the provider's published statements, the following headline metrics are
reported for Claude Opus 4.7 (vs. Claude Opus 4.6 unless stated):

- **Coding (93-task internal benchmark)**: +13% resolution rate over Opus
  4.6, including four tasks neither Opus 4.6 nor Sonnet 4.6 could solve
  [T1.4].
- **Rakuten-SWE-Bench**: 3x more production tasks resolved than Opus 4.6
  [T1.4].
- **Agent reliability**: 14% improvement over Opus 4.6 with fewer tool
  errors [T1.5].
- **Document reasoning (enterprise)**: 21% fewer errors [T1.5].
- **Visual benchmark accuracy**: 98.5% (vs. 54.5% for Opus 4.6) [T1.5].

Comparative charts in the launch announcement show state-of-the-art
positioning across office tasks, vision, document reasoning, long-context
reasoning, biology, long-term coherence, and coding — exact per-benchmark
numbers are reported in the accompanying system card [T1.4]. Per the
provider's published statements, on internal evaluations adaptive thinking
"reliably outperforms" the prior extended-thinking mode, which is why
extended-thinking budgets were removed in 4.7 [T1.2]. No tier-3 (arXiv)
release paper was located for this model.

## 5. Evaluation Data

Per the provider's published statements, evaluations referenced at launch
include an internal 93-task coding benchmark, Rakuten-SWE-Bench (a public
production-coding benchmark), and a suite of vision, document reasoning,
long-context, biology, and long-term coherence evaluations whose detailed
composition is described in the Claude Opus 4.7 system card [T1.4]. The
full evaluation dataset list and per-dataset construction notes are
contained in that 232-page system card PDF [T4.2]; those details are
**Not publicly available within this card's research scope** (the PDF
exceeded the fetch tool's size limit). For alignment and safety evaluations
specifically, Anthropic states the assessment was performed under its
Responsible Scaling Policy and ASL-3 deployment standard [T4.2].

## 6. Training Data

Specific training data sources and composition for Claude Opus 4.7 are
**Not publicly available** in the materials consulted. The closest analogue
is Anthropic's Transparency Hub statement for Claude Opus 4.6, which
describes that model as trained on "a proprietary mix of publicly available
information on the Internet … along with non-public third-party data and
internally generated data" [T1.6]; Anthropic has not (at this card's
research date) published an equivalent transparency entry for Opus 4.7
[T1.6]. Per the provider's published statements, Opus 4.7's **training
data cutoff is January 2026** and its **reliable knowledge cutoff is
January 2026** [T1.1].

## 7. Quantitative Analyses

Disaggregated, subgroup-level performance analyses are **Not publicly
available** in the materials consulted, except by reference to the system
card PDF [T4.2]. Per the provider's published statements, Anthropic's
internal alignment assessment concluded the model is "largely well-aligned
and trustworthy, though not fully ideal in its behavior," with low rates of
deception, sycophancy, and cooperation with misuse, improvements over Opus
4.6 on honesty and prompt-injection resistance, and a modest regression on
overly detailed harm-reduction advice for controlled substances [T1.4]
[T4.2]. Per the provider's published statements, Mythos Preview remains
the best-aligned model Anthropic has trained according to its evaluations,
and Opus 4.7's cyber capabilities are below Mythos Preview's by design
(Anthropic states it experimented with differentially reducing those
capabilities during training) [T1.4].

## 8. Ethical Considerations

Per the provider's published statements, Claude Opus 4.7 was deployed under
the AI Safety Level 3 (ASL-3) Deployment and Security Standard, the same
tier as Opus 4.6 [T4.2]. Real-time cybersecurity safeguards automatically
detect and block high-risk requests; legitimate defensive-security
practitioners must use the Cyber Verification Program for elevated access
[T1.2][T1.4]. Anthropic's own assessment, summarized in the launch
announcement and system card, identifies the following risks and mitigation
posture [T1.4][T4.2]:

- **Honesty / prompt-injection resistance**: improved over Opus 4.6.
- **Sycophancy, deception, cooperation with misuse**: low rates, similar
  profile to Opus 4.6.
- **Harm-reduction advice on controlled substances**: modestly weaker than
  Opus 4.6 — flagged as a known regression.
- **Cybersecurity capability uplift**: actively reduced during training;
  remains below Mythos Preview by design.
- **Behavioural shifts**: more literal instruction-following, fewer tool
  calls and fewer subagents by default, more direct/opinionated tone, and
  more frequent progress updates — these are not safety risks but can
  break prompts written for Opus 4.6 [T1.2].

The full system card (reported as 232 pages) covers welfare assessments
and additional alignment testing whose details are **Not publicly
available within this card's research scope** [T4.2].

## 9. Caveats and Recommendations

What this card cannot tell you:

- **Parameter count, architecture details, training compute**: Not publicly
  available for any Claude model.
- **Training data composition for Opus 4.7 specifically**: Not publicly
  available; the Transparency Hub had not been updated with Opus 4.7
  details at research time [T1.6].
- **Per-benchmark numeric scores beyond the headline percentages**: live
  inside the system card PDF [T4.2], which exceeded fetch-tool size limits.
- **Disaggregated subgroup performance**: Not publicly available in the
  materials consulted.
- **No tier-3 (arXiv) release paper** was located. Anthropic does not
  routinely publish arXiv release papers for Claude models; the system card
  is the closest equivalent.

Source-conflict notes:

- Tier-1 (`platform.claude.com`) and tier-4 (third-party blog summaries)
  agree on April 16, 2026 release date and on the headline benchmark gains.
  No tier-1/tier-4 conflicts were identified at this card's research date.
- The HuggingFace `Anthropic` organization page lists zero public models
  [T2.1]; this is consistent with Anthropic's API-only delivery model and
  is not a contradiction with tier-1 sources.

Recommendations for use:

- For migration from Opus 4.6, expect prompt-retuning effort: instruction-
  following is more literal, default verbosity differs, fewer tool calls
  and subagents are spawned by default, and `temperature`/`top_p`/`top_k`
  must be omitted from requests [T1.2].
- For agentic coding and long-horizon tasks, start at `effort: xhigh`
  [T1.2].
- Update `max_tokens` to provide headroom — the new tokenizer can increase
  token counts up to ~35% [T1.2][T1.3].
- For high-stakes domains (cybersecurity, biological, controlled-
  substances harm-reduction), apply human-in-the-loop review and consult
  the system card's domain-specific findings [T1.4][T4.2].

## 10. Operational Details

- **Pricing** (as of 2026-04-30, per Anthropic pricing page) [T1.3]:
  - Input: $5 / million tokens
  - Output: $25 / million tokens
  - 5-minute cache write: $6.25 / MTok; 1-hour cache write: $10 / MTok
  - Cache reads: $0.50 / MTok
  - Batch API: $2.50 input / $12.50 output per MTok (50% discount)
  - US-only inference (`inference_geo`) carries a 1.1x multiplier
- **Context window**: 1,000,000 tokens (1M), available at standard pricing
  with no long-context premium [T1.1][T1.2].
- **Maximum output**: 128,000 tokens on the Messages API; up to 300,000
  tokens on the Message Batches API with the `output-300k-2026-03-24`
  beta header [T1.1].
- **Knowledge cutoff**: Reliable knowledge cutoff January 2026; training
  data cutoff January 2026 [T1.1].
- **Supported APIs/SDKs**: Claude API (Messages API; Claude Managed Agents),
  AWS Bedrock (`anthropic.claude-opus-4-7`), Google Cloud Vertex AI
  (`claude-opus-4-7`), Microsoft Foundry [T1.1][T4.1]. OpenAI Chat
  Completions compatibility is **Not publicly available** as a documented
  feature for this model.
- **Latency tier**: "Moderate" per Anthropic's comparative-latency
  classification; Priority Tier supported [T1.1].
- **Tool / structured-output support**: Tool use supported (346 tool-use
  system-prompt tokens for `auto`/`none`; 313 for `any`/`tool`) [T1.3].
  Server-side tools include bash, code execution, text editor, web search
  ($10 / 1,000 searches), web fetch (no additional cost), and computer use
  [T1.3]. Adaptive thinking is the only thinking-on mode; extended-thinking
  budgets removed [T1.2]. Sampling parameters (`temperature`, `top_p`,
  `top_k`) are rejected with HTTP 400 [T1.2]. Thinking content is omitted
  from responses by default; opt in via `display: "summarized"` [T1.2].
- **Function calling**: Supported via the standard Claude tools schema;
  parallel tool use supported (per Claude 4 family conventions) [T1.3].
  Schema format: JSON Schema in the `tools` parameter [T1.3].
- **Task budgets (beta)**: Advisory token budget across an agentic loop
  via the `task-budgets-2026-03-13` beta header; minimum 20k tokens
  [T1.2].
- **Fine-tuning availability**: **Not publicly available** for Claude
  Opus 4.7; Anthropic does not currently expose first-party fine-tuning
  for Opus-tier models in the materials consulted.
- **Rate-limit notes**: Standard tier system (Tier 1 through Tier 4 plus
  Enterprise) per Anthropic's rate-limits documentation; specific quotas
  vary by tier and are not enumerated on the pricing page [T1.3].
- **Extended thinking**: No (removed for Opus 4.7) [T1.1][T1.2].
- **Adaptive thinking**: Yes; off by default [T1.1][T1.2].
- **Vision**: Yes; high-resolution images up to 2576px / 3.75MP with 1:1
  pixel-to-coordinate mapping [T1.2].
