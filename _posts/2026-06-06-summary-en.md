---
layout: default
title: "Horizon Summary: 2026-06-06 (EN)"
date: 2026-06-06
lang: en
---

> De 12 artículos, 5 fueron seleccionados por relevancia

---

1. [DeepSeek V4 Flash Gets Early Support in llama.cpp](#item-1) ⭐️ 8.0/10
2. [GrapheneOS user reported to authorities for using privacy OS](#item-2) ⭐️ 7.0/10
3. [Local LLM Comparison Highlights MiniMax, Step Speed](#item-3) ⭐️ 7.0/10
4. [User asks for cheaper off-site backup options than Backblaze](#item-4) ⭐️ 6.0/10
5. [Repurposed digital signage touchscreen as Home Assistant dashboard](#item-5) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Flash Gets Early Support in llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1tyb3np/deepseek_v4_flash_is_amazing_wip_llamacpp_pr_24162/) ⭐️ 8.0/10

A work-in-progress pull request (#24162) adds support for DeepSeek V4 Flash in llama.cpp, enabling local inference. Early testing shows strong intelligence and robustness to quantization, though performance is currently slow (5-6 tokens per second) and GPU/Flash Attention support is incomplete. DeepSeek V4 Flash represents a significant step for local LLM deployment, offering frontier-model intelligence in a size that fits consumer hardware. Its native FP4-FP8 hybrid quantization makes it exceptionally quantization-tolerant, addressing a major pain point for users who run models locally. The model natively uses a hybrid FP4-FP8 format, making it more resilient to quantization than models like MiniMax M2.7. The current implementation runs at only 5-6 tps without GPU acceleration, and flash attention support is still being developed.

reddit · r/LocalLLaMA · /u/Lowkey_LokiSN · jun 6, 07:56

**Contexto**: llama.cpp is an open-source C/C++ library for running large language models locally on various hardware, including CPUs and GPUs. It has become the de facto standard for local LLM inference, powering tools like Ollama and LM Studio. DeepSeek V4 Flash is a state-of-the-art model from DeepSeek that uses a mixture-of-experts architecture and native low-precision training. Its Flash variant is optimized for efficient inference.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>

</ul>
</details>

**Etiquetas**: `#DeepSeek`, `#llama.cpp`, `#local LLM`, `#quantization`, `#model inference`

---

<a id="item-2"></a>
## [GrapheneOS user reported to authorities for using privacy OS](https://discuss.grapheneos.org/d/36134-grapheneos-user-reported-to-authorities-for-using-grapheneos) ⭐️ 7.0/10

A GrapheneOS user was reported to authorities solely for using the privacy-focused operating system, sparking debate about surveillance and operating system freedom. This incident highlights growing tensions between privacy-enhancing technologies and government surveillance, potentially chilling the adoption of security-focused operating systems like GrapheneOS. The report appears to be triggered by the user's use of GrapheneOS, an open-source Android-based OS focused on privacy and security, available for Google Pixel devices.

hackernews · Cider9986 · jun 6, 08:43 · [Discusión](https://news.ycombinator.com/item?id=48422798)

**Contexto**: GrapheneOS is an open-source mobile operating system built on the Android Open Source Project, designed with extensive security hardening and privacy features. It is developed by the nonprofit GrapheneOS Foundation and has around 400K active users. The OS is known for its defense-in-depth approach and attack surface reduction.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discusión**: Comments are largely skeptical, with some parodying the situation as requiring a 'license' for the OS, and others expressing concerns about UK surveillance. A few users draw comparisons to China, suggesting that such reporting is more common in the West.

**Etiquetas**: `#GrapheneOS`, `#privacy`, `#security`, `#operating system`, `#surveillance`

---

<a id="item-3"></a>
## [Local LLM Comparison Highlights MiniMax, Step Speed](https://www.reddit.com/r/LocalLLaMA/comments/1tya05j/aa_comparison_of_the_latest_local_models/) ⭐️ 7.0/10

A Reddit post compares local LLMs suitable for 3×3090 GPU setups, noting that MiniMax and Step models run fast with Q3 quantization, while Gemma-4 12B is still missing. This comparison helps practitioners select efficient models for common hardware configurations, highlighting the impact of quantization on performance and the absence of anticipated models like Gemma-4. The comparison excludes very large models (over 200B parameters) and focuses on those usable on three NVIDIA RTX 3090 GPUs. MiniMax and Step models are noted for their speed when quantized to Q3.

reddit · r/LocalLLaMA · /u/jacek2023 · jun 6, 06:53

**Contexto**: Local LLMs are large language models that run on consumer-grade hardware. Quantization reduces model size and speeds up inference by lowering the precision of weights; Q3 is a 3-bit quantization method. The 3×3090 setup refers to three NVIDIA RTX 3090 GPUs with 24GB VRAM each, totaling 72GB, suitable for models up to around 100B parameters.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group - Wikipedia</a></li>
<li><a href="https://huggingface.co/stepfun-ai/Step-3.5-Flash">stepfun- ai / Step -3.5-Flash · Hugging Face</a></li>
<li><a href="https://aihaberleri.org/en/news/unsloth-q3-quantization-outperforms-q4-and-mxfp4-in-groundbreaking-ai-benchmark">Unsloth Q 3 Quantization Outperforms Q4 and MXFP4 in...</a></li>

</ul>
</details>

**Etiquetas**: `#local models`, `#LLM comparison`, `#benchmarking`, `#3090`, `#GPU setup`

---

<a id="item-4"></a>
## [User asks for cheaper off-site backup options than Backblaze](https://www.reddit.com/r/selfhosted/comments/1tya8o4/currently_using_backblaze_for_backups_but_its/) ⭐️ 6.0/10

A Reddit user with ~4TB of data on TrueNAS is seeking more affordable off-site backup alternatives due to Backblaze's £50/month cost, proposing a garage-based NAS and a USB drive in a fireproof safe. This underscores the common challenge for home users and small businesses of balancing backup cost with data security, and the discussion offers practical self-hosted solutions that may help others with large backups. The user stores company documents, 30 years of family photos, and other data totaling 3-4TB on a TrueNAS HP Microserver with 4x6TB disks, and proposes a second HP Microserver in the garage plus a USB drive in a fireproof safe.

reddit · r/selfhosted · /u/CrappyTan69 · jun 6, 07:06

**Contexto**: TrueNAS is a free, open-source NAS operating system based on OpenZFS, widely used for self-hosted storage. Off-site backups protect against local disasters like fire or theft. USB passthrough allows a virtual machine to directly access a USB device, useful for connecting external drives to a backup system.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TrueNAS">TrueNAS - Wikipedia</a></li>
<li><a href="https://www.truenas.com/truenas-community-edition/">TrueNAS Community Edition | Free Open Source Storage</a></li>

</ul>
</details>

**Etiquetas**: `#backups`, `#selfhosted`, `#backblaze`, `#TrueNAS`, `#offsite`

---

<a id="item-5"></a>
## [Repurposed digital signage touchscreen as Home Assistant dashboard](https://www.reddit.com/r/homeassistant/comments/1tyd5xc/i_repurposed_an_old_digital_signage_touchscreen/) ⭐️ 6.0/10

A Reddit user repurposed an old digital signage touchscreen as a physical Home Assistant dashboard and created a custom Lovelace card for controlling their home cinema. This project showcases creative repurposing of commercial hardware for smart home use, providing a large, dedicated touch interface for Home Assistant and inspiring similar DIY projects. The touchscreen likely runs a full-screen web browser pointing to a Home Assistant Lovelace view, with the custom card built using HACS and card-mod for CSS styling.

reddit · r/homeassistant · /u/Nerdaxic · jun 6, 09:59

**Contexto**: Home Assistant's Lovelace UI is a customizable dashboard composed of cards. Custom Lovelace cards, often installed via HACS (Home Assistant Community Store), allow users to extend functionality and appearance with community-made or self-developed cards. Card-mod is a popular frontend extension that permits CSS styling of any card. Digital signage touchscreens are commercial-grade displays designed for continuous operation in public spaces, making them suitable for a dedicated kiosk interface.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/thomasloven/lovelace-card-mod">GitHub - thomasloven/lovelace-card-mod: Add CSS styles to ... Mastering Home Assistant Custom Lovelace Cards: Elevating ... Images Top 8 Home Assistant Thermostat Cards - SmartHomeScene Lovelace Cards System | home-assistant/frontend | DeepWiki Helios , 3D solar card for Home Assistant + LiDAR conversion Five new and popular Home Assistant Lovelace custom cards</a></li>
<li><a href="https://www.beetronics.ie/c-digital-signage/touchscreen">Digital signage touchscreens | 7 to 27 inches | Beetronics</a></li>

</ul>
</details>

**Etiquetas**: `#home assistant`, `#DIY`, `#dashboard`, `#touchscreen`, `#home cinema`

---