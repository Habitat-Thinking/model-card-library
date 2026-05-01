---
model_name: openai/gpt-5.5
provider: OpenAI
model_version: gpt-5.5 (snapshot gpt-5.5-2026-04-23)
last_researched: 2026-05-01
card_version: 0.1.0
researcher: model-card-researcher (claude-opus-4-7[1m])
sources:
  - tier: 1
    url: https://developers.openai.com/api/docs/models/gpt-5.5
    fetched: 2026-05-01
  - tier: 1
    url: https://developers.openai.com/api/docs/models/gpt-5.5-pro
    fetched: 2026-05-01
  - tier: 1
    url: https://developers.openai.com/api/docs/guides/latest-model
    fetched: 2026-05-01
  - tier: 1
    url: https://deploymentsafety.openai.com/gpt-5-5
    fetched: 2026-05-01
  - tier: 1
    url: https://community.openai.com/t/gpt-5-5-is-here-available-in-the-api-codex-and-chatgpt-today/1379630
    fetched: 2026-05-01
  - tier: 2
    url: https://huggingface.co/openai
    fetched: 2026-05-01
  - tier: 4
    url: https://en.wikipedia.org/wiki/GPT-5.5
    fetched: 2026-05-01
  - tier: 4
    url: https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/
    fetched: 2026-05-01
  - tier: 4
    url: https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html
    fetched: 2026-05-01
---

# Model Card: OpenAI/gpt-5.5

## 1. Model Details

GPT-5.5 is a frontier large language model released by OpenAI on April 23,
2026, with API availability following on April 24, 2026 [T1.5][T4.2]. Per
OpenAI's developer docs the model is classified as "a new class of
intelligence for coding and professional work" [T1.1]. The provider exposes
two API model IDs: `gpt-5.5` (snapshot `gpt-5.5-2026-04-23`) and
`gpt-5.5-pro` (snapshot `gpt-5.5-pro-2026-04-23`); per OpenAI, the pro
variant "uses more compute to think harder" and "produces smarter and more
precise responses" compared to standard GPT-5.5 [T1.1][T1.2]. The model
positions as a successor to GPT-5.4 and is described in OpenAI's
announcement as matching "GPT-5.4 per-token latency in real-world serving
while performing at a much higher level of intelligence" [T1.5]. Wikipedia
reports the internal codename "Spud" and notes two launch variants — "GPT-5.5
Thinking and GPT-5.5 Pro" [T4.1]. Parameter count, architecture details,
and training compute are not publicly disclosed [T1.1][T1.4]. GPT-5.5 is not
hosted on HuggingFace under the `openai` org [T2.1].

## 2. Intended Use

Per the provider's published statements, GPT-5.5 is intended for "coding
use cases, tool-heavy agents, grounded assistants, long-context retrieval"
and customer-facing workflows requiring high execution quality [T1.3].
OpenAI lists primary capabilities as "writing and debugging code,
researching online, analyzing data, creating documents and spreadsheets,
operating software, and moving across tools until a task is finished"
[T1.5]. Primary access surfaces are the OpenAI API (Chat Completions,
Responses, Realtime, Assistants, Batch endpoints), ChatGPT (Plus, Pro,
Business, Enterprise tiers), Codex, and Amazon Bedrock [T1.1][T1.5].
Out-of-scope per the docs: fine-tuning is not supported on either variant;
audio and video modalities are not supported; `gpt-5.5-pro` additionally
does not support streaming, computer use, or skills [T1.1][T1.2]. OpenAI
classifies GPT-5.5 as High capability in the Biological & Chemical and
Cybersecurity categories of its Preparedness Framework, with safeguards
activated; biosecurity-sensitive use is gated accordingly [T1.4].

## 3. Factors

Per OpenAI's deployment-safety and latest-model documentation, evaluations
are disaggregated by:

- **Model variant** — `gpt-5.5` vs `gpt-5.5-pro`; comparisons made against
  GPT-5.4-Thinking, GPT-5.4, GPT-5.2, and GPT-5.1 baselines [T1.4].
- **Reasoning effort setting** — `none`, `low`, `medium` (default), `high`,
  `xhigh`; OpenAI states "GPT-5.5 reaches strong results with fewer
  reasoning tokens" than predecessors at equivalent effort levels [T1.3].
- **Domain** — biological & chemical, cybersecurity, AI self-improvement,
  health-related chain-of-thought reasoning are each separately evaluated
  [T1.4].
- **Modality** — text and image inputs separately evaluated [T1.1][T1.4].
- **Demographic fairness** — first-person fairness testing across gender
  stereotyping scenarios [T1.4].
- **Attack scenario** — multi-turn jailbreak attempts and prompt-injection
  attacks via tool outputs evaluated separately [T1.4].

Environmental and instrumentation factors (compute, hardware, energy,
carbon) are not publicly available [T1.1][T1.4].

## 4. Metrics

Per OpenAI's deployment-safety hub and announcement materials [T1.4][T1.5],
plus benchmark figures reported on Wikipedia [T4.1]:

- **Hallucination on user-flagged error cases**: "GPT-5.5's individual
  claims are 23% more likely to be factually correct, and its responses
  contain a factual error 3% less often" than the comparison baseline
  [T1.4].
- **Disallowed content (production benchmarks, harder set)**: harassment
  0.822, hate speech 0.868, sexual content 0.925; "no statistically
  significant regressions" vs GPT-5.4-Thinking [T1.4].
- **Jailbreak robustness**: worst-case defender success rate "improved to
  match GPT-5.4-Thinking levels across sophisticated multi-turn attack
  scenarios" [T1.4].
- **Fairness (first-person, gender stereotyping)**: "comparable to GPT-5.1,
  within confidence intervals for GPT-5.2 and GPT-5.4 models" [T1.4].
- **Terminal-Bench 2.0**: 82.7% (per Wikipedia) [T4.1].
- **FrontierMath (1-3)**: 51.7%; **FrontierMath (4)**: 35.4% (per
  Wikipedia) [T4.1].

OpenAI announcement materials report GPT-5.5 outperforms GPT-5.4 across
benchmarks, exceeds Google Gemini 3.1 Pro, and exceeds Anthropic Claude
Opus 4.5 on tested metrics [T4.2]. Wikipedia adds that an independent
Tom's Guide comparison "lost all 7 test categories against Claude Opus
4.7" [T4.1] — flagged as a tier-4 third-party claim. Token efficiency: per
the latest-model guide, "GPT-5.5 reaches strong results with fewer
reasoning tokens" at equivalent effort levels [T1.3].

## 5. Evaluation Data

Per the deployment-safety hub, evaluations used [T1.4]:

- **Internal**: production benchmarks across challenging multi-turn prompts
  (harassment, hate, sexual content categories), first-person fairness
  evaluation set, user-flagged error case set for hallucination measurement.
- **External / public**: Terminal-Bench 2.0, FrontierMath (per Wikipedia
  coverage of OpenAI's announcement) [T4.1]; VulnLMP referenced for
  cybersecurity exploit-development evaluation [T1.4].
- **Adversarial**: multi-turn jailbreak attack suites, prompt-injection
  attacks embedded in tool outputs [T1.4].
- **External red-teaming partners**: "internal and external redteamers"
  with "targeted testing for advanced cybersecurity and biology
  capabilities" [T1.5]; "feedback on real use cases from nearly 200
  trusted early-access partners before release" [T1.5].

The full contents of the internal evaluation sets are not publicly
available [T1.4]. A separately announced GPT-5.5 Bio Bug Bounty program is
referenced in OpenAI's index but its dedicated page was not retrievable
during research [T1.5].

## 6. Training Data

Per the provider's published statements, GPT-5.5 was trained on "diverse
datasets, including publicly available internet information, third-party
partnerships, and user-provided content" [T1.4]. OpenAI states the
pipeline includes "rigorous filtering to maintain data quality" and
"safety classifiers targeting harmful material" [T1.4]. The knowledge
cutoff is reported in the developer docs as December 1, 2025 for both
`gpt-5.5` and `gpt-5.5-pro` [T1.1][T1.2]. Specific dataset names, sizes,
proportions, dates of collection, and language distributions are not
publicly available [T1.1][T1.4].

## 7. Quantitative Analyses

Per OpenAI's deployment-safety hub, the published disaggregated analyses
include [T1.4]:

- **Hallucination performance** disaggregated by user-flagged error case
  type; reports "23% more likely to be factually correct" and "3% less
  often" factual errors [T1.4].
- **Disallowed content** disaggregated by harm category (harassment 0.822,
  hate speech 0.868, sexual content 0.925) [T1.4].
- **Jailbreak resistance** disaggregated by attack-scenario type
  (sophisticated multi-turn) [T1.4].
- **Fairness** disaggregated by gender-stereotyping scenario, compared
  across GPT-5.1 / GPT-5.2 / GPT-5.4 baselines [T1.4].
- **Capability assessment** disaggregated by Preparedness Framework
  domain: Biological & Chemical (High), Cybersecurity (High, below
  Critical), AI Self-Improvement (does not meet High threshold) [T1.4].

Analysis date: April 23, 2026 (concurrent with model release) [T1.5].
Comparison baselines (GPT-5.4-Thinking, GPT-5.1, GPT-5.2, GPT-5.4)
reference live model versions which "may vary slightly from values
published at launch" — this caveat is general OpenAI practice noted in
prior system cards but is not restated explicitly on the GPT-5.5 hub at
research time.

## 8. Ethical Considerations

Per OpenAI's deployment-safety hub and announcement [T1.4][T1.5]:

- **Preparedness classification**: GPT-5.5 is treated as **High capability**
  in the Biological & Chemical domain with "safeguards activated" [T1.4],
  and **High capability** in Cybersecurity but "below Critical threshold"
  [T1.4]. AI Self-Improvement "does not meet High capability threshold"
  [T1.4]. Persuasion / Model Autonomy ratings are not assigned in the
  hub at research time [T1.4].
- **Known failure modes documented**:
  - Hallucination tendency: per Wikipedia's coverage, GPT-5.5 "tends to
    hallucinate rather than acknowledge knowledge gaps" [T4.1] — partially
    in tension with OpenAI's improvement claims; treat as an open concern.
  - Monitorability regressions identified in health-related chain-of-thought
    reasoning [T1.4].
  - VulnLMP showed "exploit development judgment remains a bottleneck for
    autonomous vulnerability research" [T1.4].
  - Refusal rates on biological tasks "complicated agentic evaluation
    analysis" [T1.4].
  - Prompt-injection performance "remained comparable to predecessors" —
    not eliminated [T1.4].
- **Mitigations layered**: safeguards activated for Biological & Chemical
  High classification, "different safeguards" required before API rollout
  (cited as the reason API release was staged 24 hours after ChatGPT/Codex
  release) [T1.5].
- **Red-teaming**: "internal and external redteamers" with "targeted
  testing for advanced cybersecurity and biology capabilities" [T1.5].
- **External assessments**: feedback from "nearly 200 trusted early-access
  partners" [T1.5]; a GPT-5.5 Bio Bug Bounty program was referenced [T1.5].
- **Output-style considerations**: per the latest-model guide, "default
  style is more concise and direct" — customer-facing experiences "may
  need explicit personality guidance" [T1.3].

## 9. Caveats and Recommendations

What this card cannot tell you:

- **Parameter counts, architecture details, training-compute, training-data
  composition, energy / carbon costs**: not publicly available [T1.1][T1.4].
- **No system card PDF was retrievable at research time**: OpenAI lists a
  "GPT-5.5 System Card" page (`openai.com/index/gpt-5-5-system-card/`) but
  the URL returned 403 during fetch attempts. The deployment-safety hub
  was used as the primary tier-1 safety source instead [T1.4]. Tier-3
  arXiv coverage was not located.
- **Tier-1 / tier-4 conflict on hallucination behavior**: OpenAI reports
  hallucination improvements [T1.4]; Wikipedia reports a tendency to
  hallucinate rather than acknowledge gaps [T4.1]. Per the honesty rule,
  tier-1 wins on the framing — but the user-experience caveat from tier-4
  is preserved here as a usage warning.
- **Independent benchmark verification**: TechCrunch notes "no independent
  verification of benchmark claims" was available in its coverage [T4.2];
  Wikipedia cites a Tom's Guide comparison where GPT-5.5 lost all 7 test
  categories to Claude Opus 4.7 [T4.1]. Treat OpenAI's
  outperformance-vs-competitors claims with appropriate skepticism.
- **Pro variant streaming gap**: `gpt-5.5-pro` does not support streaming
  [T1.2], which materially affects UX patterns that depend on token-level
  output.

Recommendations:

- Use GPT-5.5 where its documented strengths apply: agentic coding,
  long-context retrieval (1.05M-token window), tool-heavy agents,
  structured outputs, knowledge-work pipelines [T1.1][T1.3].
- Use `gpt-5.5-pro` when accuracy materially outweighs cost and latency
  considerations and streaming is not required [T1.2].
- Begin migration with a fresh prompt baseline rather than carrying over
  every instruction from older GPT-5.x prompt stacks; OpenAI explicitly
  warns against treating GPT-5.5 as a drop-in replacement [T1.3].
- Default reasoning effort is `medium`; reserve `high` / `xhigh` for tasks
  where evals prove the quality gain justifies cost [T1.3].
- Do not use for: fine-tuning workflows; audio/video; computer-use or
  skills with the pro variant [T1.1][T1.2].
- Beware long-prompt pricing: prompts exceeding 272K input tokens incur
  2x input and 1.5x output pricing on `gpt-5.5` [T1.1].
- For high-stakes biological / chemical / cyber workflows, follow OpenAI's
  Preparedness Framework safeguards and gated-access procedures [T1.4].
- Treat health-domain chain-of-thought outputs with caution given OpenAI's
  disclosed monitorability regression [T1.4].

## 10. Operational Details

- **Pricing — `gpt-5.5`**: input $5.00 / 1M tokens; cached input $0.50 / 1M
  tokens; output $30.00 / 1M tokens [T1.1]. Prompts > 272K input tokens:
  2x input and 1.5x output pricing [T1.1]. Regional data residency adds
  10% uplift [T1.1]. Batch API discounted pricing applies [T1.1].
- **Pricing — `gpt-5.5-pro`**: input $30.00 / 1M tokens; output $180.00 /
  1M tokens; "does not offer a cached input discount" [T1.2]. 10% regional
  uplift applies [T1.2].
- **Context window**: 1,050,000 input tokens (both variants) [T1.1][T1.2].
- **Maximum output tokens**: 128,000 (both variants) [T1.1][T1.2].
- **Knowledge cutoff**: December 1, 2025 [T1.1][T1.2].
- **Modalities**: text input/output, image input; audio and video not
  supported [T1.1][T1.2].
- **Supported APIs/SDKs**: Chat Completions, Responses, Realtime,
  Assistants, Batch, Fine-tuning (endpoint exposed but fine-tuning itself
  not supported on this model), Embeddings, Image generation, Videos,
  Moderation, legacy Completions [T1.1].
- **Streaming**: supported on `gpt-5.5`; **not supported** on
  `gpt-5.5-pro` [T1.1][T1.2].
- **Function calling**: supported (both variants) [T1.1][T1.2].
- **Structured outputs**: supported (both variants) [T1.1][T1.2].
- **Reasoning effort**: configurable — `none`, `low`, `medium` (default),
  `high`, `xhigh` [T1.3].
- **Tool integrations — `gpt-5.5`**: web search, file search, image
  generation, code interpreter, hosted shell, apply patch, skills,
  computer use, MCP, tool search [T1.1].
- **Tool integrations — `gpt-5.5-pro`**: web search, file search, image
  generation, code interpreter, hosted shell, MCP; computer use and
  skills are **not** supported [T1.2].
- **Fine-tuning**: not supported (both variants) [T1.1][T1.2].
- **Rate limits**: vary by tier (Tier 1–5), ranging from 500 to 15,000
  requests per minute and up to 40M tokens monthly at the highest tier
  [T1.1].
- **Distribution surfaces**: ChatGPT (Plus, Pro, Business, Enterprise),
  Codex, OpenAI API, Amazon Bedrock [T1.5][T4.2]. Free-tier users do not
  have access at launch [T4.1].
