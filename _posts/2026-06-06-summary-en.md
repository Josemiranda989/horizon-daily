---
layout: default
title: "Horizon Summary: 2026-06-06 (EN)"
date: 2026-06-06
lang: en
---

> From 13 items, 6 important content pieces were selected

---

1. [GrapheneOS user reported to authorities for using privacy-focused OS](#item-1) ⭐️ 8.0/10
2. [DeepSeek V4 Flash Support in llama.cpp via Early PR](#item-2) ⭐️ 8.0/10
3. [Big week for open AI: 25+ notable open-weight model releases across modalities](#item-3) ⭐️ 8.0/10
4. [S&P 500 rejects SpaceX, OpenAI, Anthropic fast-track entry](#item-4) ⭐️ 7.0/10
5. [Comparison of Latest Local LLMs on 3x3090 Hardware](#item-5) ⭐️ 6.0/10
6. [Merged Uncensored Qwen Model with Claude 4.6 Reasoning Released](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GrapheneOS user reported to authorities for using privacy-focused OS](https://discuss.grapheneos.org/d/36134-grapheneos-user-reported-to-authorities-for-using-grapheneos) ⭐️ 8.0/10

A user of GrapheneOS, a hardened Android-based OS, was reportedly reported to law enforcement for using the operating system, sparking debate about surveillance and OS restrictions. This incident highlights growing societal suspicion toward privacy-enhancing technologies and raises concerns about the chilling effect on users who prioritize digital security. The report appears to be based on boilerplate response from forum administrators, leaving the veracity of the police involvement unclear. The discussion has garnered over 90 comments and high engagement on Hacker News.

hackernews · Cider9986 · Jun 6, 08:43 · [Discussion](https://news.ycombinator.com/item?id=48422798)

**Background**: GrapheneOS is an open-source mobile operating system based on Android Open Source Project, focused on security and privacy hardening. It is often used by privacy-conscious individuals and has approximately 400K active users as of 2026. In some jurisdictions, using such specialized privacy tools may be viewed with suspicion by authorities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discussion**: The community expressed outrage and sarcasm, with comments mocking the situation (e.g., asking for a 'loicense' for the OS) and comparing it to authoritarian practices. Some questioned the credibility of the report, noting the response appeared to be boilerplate, while others highlighted the irony that such surveillance happens in the West despite criticism of China.

**Tags**: `#GrapheneOS`, `#privacy`, `#surveillance`, `#OS security`, `#HN discussion`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash Support in llama.cpp via Early PR](https://www.reddit.com/r/LocalLLaMA/comments/1tyb3np/deepseek_v4_flash_is_amazing_wip_llamacpp_pr_24162/) ⭐️ 8.0/10

An early-stage pull request (#24162) has been opened to add support for the DeepSeek V4 Flash model in llama.cpp, enabling local inference with impressive intelligence and robustness to quantization. This integration brings frontier-class AI to local deployment, making DeepSeek V4 accessible to users who prioritize privacy and offline use. It also demonstrates superior quantization resilience compared to other models like MiniMax M2.7. The PR is still very early and runs slowly (5-6 tokens per second), with GPU and Flash Attention support needing work. However, the model's native FP4-FP8 hybrid quantization allows it to maintain quality even at low bit widths.

reddit · r/LocalLLaMA · /u/Lowkey_LokiSN · Jun 6, 07:56

**Background**: llama.cpp is an open-source C/C++ library for running large language models locally on consumer hardware, often used with GGUF format quantized models. DeepSeek V4 Flash is a recent frontier model from DeepSeek that uses a mixture-of-experts architecture and hybrid FP4-FP8 quantization, making it efficient for inference.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>

</ul>
</details>

**Tags**: `#DeepSeek V4`, `#llama.cpp`, `#local inference`, `#quantization`, `#open source`

---

<a id="item-3"></a>
## [Big week for open AI: 25+ notable open-weight model releases across modalities](https://www.reddit.com/r/LocalLLaMA/comments/1tyd1zc/big_week_for_open_ai_with_25_notable_openweight/) ⭐️ 8.0/10

This week saw over 25 notable open-weight AI model releases, led by NVIDIA Nemotron 3 Ultra (550B hybrid Mamba-MoE), Google Gemma 4 12B (any-to-any multimodal), Ideogram 4 (first-ever open weights, top open image gen), and four new TTS models. This wave of releases demonstrates accelerating progress in open AI, narrowing the gap with proprietary models and making cutting-edge capabilities across LLMs, image, audio, and video generation accessible to the broader community. Notable technical highlights include the first openly-weighted 550B hybrid Mamba-Transformer MoE (Nemotron 3 Ultra), NVFP4 precision for ~5x throughput on Blackwell, a 23-checkpoint QAT wave for Gemma 4, and Ideogram 4's flow-matching DiT trained from scratch achieving #2 overall on LMArena.

reddit · r/LocalLLaMA · /u/Nunki08 · Jun 6, 09:53

**Background**: Open-weight models are AI models whose trained parameters are publicly released, enabling community-driven research, fine-tuning, and deployment. Hybrid architectures like Mamba-MoE combine state-space layers with transformers to improve efficiency, while flow matching is a generative modeling technique that transforms noise into data via a learned vector field.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/">Introducing Nemotron 3 Super: An Open Hybrid Mamba-Transformer MoE for Agentic Reasoning | NVIDIA Technical Blog</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision ...</a></li>
<li><a href="https://www.ai21.com/blog/rise-of-hybrid-llms/">Attention was never enough: Tracing the rise of hybrid LLMs | AI21</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#AI`, `#LLM`, `#image generation`, `#machine learning`

---

<a id="item-4"></a>
## [S&P 500 rejects SpaceX, OpenAI, Anthropic fast-track entry](https://arstechnica.com/tech-policy/2026/06/sp-500-blocks-fast-spacex-entry-wont-waive-rule-for-unprofitable-ai-firms/) ⭐️ 7.0/10

The S&P 500 index committee has rejected requests to waive profitability rules for SpaceX, OpenAI, and Anthropic, maintaining that they cannot be added to the index until they demonstrate consistent earnings. This decision upholds the credibility of the S&P 500 as a benchmark for established, profitable companies and prevents special treatment for high-growth but unprofitable firms, reassuring passive investors that index funds will maintain their disciplined strategy. The S&P 500 requires companies to report positive GAAP earnings over the most recent quarter and the trailing four quarters; SpaceX, OpenAI, and Anthropic have not yet achieved consistent profitability and thus do not qualify.

hackernews · maltalex · Jun 6, 04:38 · [Discussion](https://news.ycombinator.com/item?id=48421442)

**Background**: The S&P 500 is a stock market index that tracks 500 large publicly traded U.S. companies. Inclusion criteria include a market capitalization over $13 billion, public trading for at least one year, and demonstrated profitability. The index is widely used as a benchmark for passive investment funds.

**Discussion**: Commenters largely support the S&P 500's decision, with many passive investors expressing relief that the index will not make exceptions. Some note the decision preserves the trust and reputation of the index. A few critical comments about 'propaganda pushing bottom feeders' were also present.

**Tags**: `#S&P 500`, `#SpaceX`, `#OpenAI`, `#index funds`, `#financial policy`

---

<a id="item-5"></a>
## [Comparison of Latest Local LLMs on 3x3090 Hardware](https://www.reddit.com/r/LocalLLaMA/comments/1tya05j/aa_comparison_of_the_latest_local_models/) ⭐️ 6.0/10

A Reddit user shared a comparison of local LLMs that can run on a 3x3090 setup, highlighting MiniMax and Step models in Q3 quantization while noting the absence of Gemma-4 12B. This comparison is timely for the local LLM community as it helps users choose models for consumer hardware and reflects the trend of running larger models at lower quantization levels. The post excludes models over 300B parameters and suggests skipping 200B models, but notes that MiniMax and Step are fast in Q3. Gemma-4 12B is still missing from the comparison.

reddit · r/LocalLLaMA · /u/jacek2023 · Jun 6, 06:53

**Background**: Local LLMs are large language models that run on personal hardware, often using quantization to reduce memory. Quantization lowers the precision of weights (e.g., Q3 is a very low-precision format that saves VRAM but may affect accuracy). A 3x3090 setup provides 72 GB of VRAM, enabling models up to ~70B parameters at high quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://engineeredai.net/llm-quantization-explained/">LLM Quantization Explained: What Q4, Q5, and Q8 Actually Mean</a></li>
<li><a href="https://mljourney.com/quantized-llms-explained-q4-vs-q8-vs-fp16/">Quantized LLMs Explained: Q4 vs Q8 vs FP16 - ML Journey</a></li>
<li><a href="https://minimax-ai.chat/models/">Models - Minimax Ai</a></li>

</ul>
</details>

**Tags**: `#local LLM`, `#model comparison`, `#LLM benchmarks`, `#open source`

---

<a id="item-6"></a>
## [Merged Uncensored Qwen Model with Claude 4.6 Reasoning Released](https://www.reddit.com/r/LocalLLaMA/comments/1tyb6u7/qwen3635ba3buncensoredclaude46genesisapexgguf/) ⭐️ 6.0/10

A new merged uncensored LLM called Qwen3.6-35B-A3B-Uncensored-Claude-4.6-Genesis-APEX-GGUF has been released, featuring Claude 4.6 Opus reasoning, both thinking and non-thinking modes, and improved coding stability and function calling. This release offers an uncensored model with advanced reasoning and coding improvements, making it valuable for local deployment and specialized use cases such as roleplay and autonomous tool calling. The model is built from a delta merge of a previous Qwen-based release and uses APEX quantization. It requires a specific system prompt initial line ('You are a helpful AI assistant') for optimal performance, and recommended temperature settings vary for coding (0.7) and roleplay (1.0).

reddit · r/LocalLLaMA · /u/EvilEnginer · Jun 6, 08:01

**Background**: Model merging combines multiple LLMs to leverage their strengths. Delta merge is a technique that applies only the differences between models. APEX is a mixed-precision quantization method that improves efficiency while maintaining quality. Thinking modes refer to mechanisms in some LLMs that allow them to engage in deeper reasoning or step-by-step thought processes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mudler/apex-quant">GitHub - mudler/ apex -quant: Adaptive Precision for EXpert Models...</a></li>
<li><a href="https://www.onyxgs.com/blog/how-thinking-modes-work-modern-llms">How “ Thinking ” Modes Work in Modern LLMs | Onyx</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#model merging`, `#uncensored`, `#local deployment`, `#Qwen`

---