# Horizon Diario - 2026-06-07

> De 48 artículos, 27 fueron seleccionados por relevancia

---

1. [Inferencia de LLM en CPU alcanza 7 tokens/s con Gemma-4-26B-A4B](#item-1) ⭐️ 9.0/10
2. [La cuantización KVarN del KV cache iguala precisión de mayor bit con menor memoria](#item-2) ⭐️ 9.0/10
3. [Ganadores del 29º IOCCC: emulador de Game Boy y de 366 bytes para Linux/Doom](#item-3) ⭐️ 8.0/10
4. [Científicos expulsados de conferencia por reimpresiones de un editorial crítico](#item-4) ⭐️ 8.0/10
5. [Estudio de tokenomía revela uso dominante de tokens de entrada en ingeniería de software agéntica](#item-5) ⭐️ 8.0/10
6. [Ntsc-rs: Emulación open-source de artefactos de TV analógica y VHS](#item-6) ⭐️ 8.0/10
7. [Diseño con Claude más que con Figma ahora](#item-7) ⭐️ 8.0/10
8. [Más allá de fork() y exec() para la creación de procesos](#item-8) ⭐️ 8.0/10
9. [Aprendizaje autosupervisado en grafos sin entrenamiento iguala GCN con 5× menos etiquetas](#item-9) ⭐️ 8.0/10
10. [Cohere ofrece acceso anticipado a modelo de codificación no lanzado](#item-10) ⭐️ 8.0/10
11. [Vulnerabilidad en herramienta de IA de PewDiePie permite toma de control de administrador con un clic](#item-11) ⭐️ 8.0/10
12. [120 tok/s en 12 GB VRAM con Gemma 4 12B QAT MTP](#item-12) ⭐️ 8.0/10
13. [Archivo de imágenes de dominio público con procedencia](#item-13) ⭐️ 7.0/10
14. [Superviviente de tiroteo escolar demanda a empresa de detección de armas con IA por fallo](#item-14) ⭐️ 7.0/10
15. [dvlt.cu: motor de inferencia en CUDA/C++ para el transformador 3D DVLT de NVIDIA](#item-15) ⭐️ 7.0/10
16. [open-deepthink lanza el modo completo de destilación de conocimiento](#item-16) ⭐️ 7.0/10
17. [Home Assistant automatiza el hogar según señales de recuperación corporal, no solo movimiento](#item-17) ⭐️ 7.0/10
18. [Usuario encuentra control perdido con Claude y Home Assistant](#item-18) ⭐️ 7.0/10
19. [Fast Search Card: Panel que se construye solo para Home Assistant](#item-19) ⭐️ 7.0/10
20. [Campo de clones: cómo las réplicas de caballos llegaron a dominar el polo](#item-20) ⭐️ 6.0/10
21. [Investigadores independientes buscan respaldo en arXiv para pipeline SAM 2.1-LocateAnything](#item-21) ⭐️ 6.0/10
22. [Debate sobre cuantizaciones alternativas para modelos QAT como Gemma-4](#item-22) ⭐️ 6.0/10
23. [Plataforma de lifelogging desarrollada en solitario alcanza 4 años de uso diario](#item-23) ⭐️ 6.0/10
24. [Rootprint: gestión de logs autogestionada y de código abierto](#item-24) ⭐️ 6.0/10
25. [Agrupando tres Jetson Nano Orin Super](#item-25) ⭐️ 6.0/10
26. [espControl añade protector de pantalla con carátulas de álbumes](#item-26) ⭐️ 6.0/10
27. [Cómo arreglar dispositivos IKEA Matter en Home Assistant](#item-27) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Inferencia de LLM en CPU alcanza 7 tokens/s con Gemma-4-26B-A4B](https://www.reddit.com/r/LocalLLaMA/comments/1tz5ffp/you_dont_need_a_gpu_to_run_gemma426ba4b/) ⭐️ 9.0/10

Un usuario de Reddit ejecuta con éxito el nuevo modelo de mezcla de expertos Gemma-4-26B-A4B de Google completamente en una CPU sin GPU, usando Koboldcpp en Linux. La configuración alcanza aproximadamente 7 tokens por segundo en un antiguo Intel i5-8500 con 32GB de RAM. Esto demuestra que los modelos de lenguaje de última generación pueden ejecutarse de manera asequible en hardware de gama baja, reduciendo significativamente la barrera de entrada para usuarios individuales. Desafía la suposición de que se necesitan GPU costosas para ejecutar LLMs modernos localmente. El modelo Gemma-4-26B-A4B utiliza una arquitectura de mezcla de expertos con aproximadamente 26 mil millones de parámetros totales pero solo 4 mil millones activos por token, lo que permite eficiencia en CPU. El usuario reporta usar Koboldcpp, que es compatible con modelos cuantizados GGUF e incluye optimizaciones como caché KV cuantizada.

reddit · r/LocalLLaMA · /u/JackStrawWitchita · jun 7, 07:24

**Contexto**: Los grandes modelos de lenguaje típicamente requieren GPU potentes debido a sus enormes demandas de memoria y cómputo. Sin embargo, los modelos de mezcla de expertos (MoE) activan solo un subconjunto de parámetros por token, lo que los hace más eficientes. Además, las técnicas de cuantización reducen el uso de memoria, y software como Koboldcpp aprovecha optimizaciones específicas de CPU (p. ej., AVX2) para ejecutar estos modelos en hardware de consumo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://koboldcpp.com/">KoboldCPP – Run AI Models Locally, Free & Open-Source</a></li>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>

</ul>
</details>

**Etiquetas**: `#LLMs`, `#inferencia en CPU`, `#Gemma 4`, `#eficiencia`, `#hardware barato`

---

<a id="item-2"></a>
## [La cuantización KVarN del KV cache iguala precisión de mayor bit con menor memoria](https://www.reddit.com/r/LocalLLaMA/comments/1tyockn/kv_cache_quant_benchmarks_kvarn_6bit_matches_q8_0/) ⭐️ 9.0/10

Nuevos benchmarks muestran que KVarN, un cuantizador del KV cache normalizado por varianza, logra precisión equivalente a q8_0 con 6 bits y a q5_0 con 4 bits, ofreciendo efectivamente un nivel superior de precisión que los cuantizadores estándar. Este avance reduce significativamente los requisitos de memoria para la inferencia de modelos de lenguaje grandes, permitiendo ventanas de contexto más largas y mayores tamaños de lote en hardware con VRAM limitada sin sacrificar calidad. Los benchmarks se ejecutaron en un modelo Qwen 3.6 27B con contexto de 64k usando un fork de llama.cpp con DFlash. El procesamiento de prompts es actualmente más lento en esta implementación inicial, pero se esperan más optimizaciones.

reddit · r/LocalLLaMA · /u/Anbeeld · jun 6, 18:06

**Contexto**: El KV cache almacena tensores de clave y valor durante la inferencia de LLM para evitar recálculos, pero consume una cantidad significativa de memoria. La cuantización reduce la precisión para ahorrar memoria; KVarN aplica una rotación de Hadamard seguida de una normalización de varianza de doble escala para mitigar la acumulación de errores, logrando mejor precisión que los cuantizadores tradicionales al mismo ancho de bits.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.03458">KVarN: Variance-Normalized KV-Cache Quantization Mitigates ...</a></li>
<li><a href="https://www.baseten.co/blog/dflash-faster-llm-inference/">DFlash : 3x faster LLM inference</a></li>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**Etiquetas**: `#cuantización`, `#KV cache`, `#optimización de LLM`, `#benchmarks`, `#eficiencia de memoria`

---

<a id="item-3"></a>
## [Ganadores del 29º IOCCC: emulador de Game Boy y de 366 bytes para Linux/Doom](https://www.ioccc.org/2025/) ⭐️ 8.0/10

Se anunciaron los ganadores del 29º Concurso Internacional de Código C Ofuscado (IOCCC), con un emulador de Game Boy cuyo código fuente tiene la forma de la consola y un programa C de 366 bytes que emula una computadora de una sola instrucción (OISC) capaz de arrancar Linux y ejecutar Doom. Esto es significativo porque el IOCCC muestra una creatividad extrema en la programación en C, demostrando que el código muy ofuscado puede lograr tareas complejas como la emulación, empujando los límites del código mínimo. El emulador de Game Boy fue creado por Nick Craig-Wood, también conocido por rclone, y el emulador de 366 bytes implementa una OISC que ejecuta Linux y Doom. Las pautas del IOCCC permiten explícitamente el uso de LLMs en las entradas.

hackernews · matt_d · jun 7, 05:47 · [Discusión](https://news.ycombinator.com/item?id=48432199)

**Contexto**: El IOCCC es un concurso de programación iniciado en 1984 que desafía a los participantes a escribir el código C más ofuscado de forma creativa. Se celebra periódicamente y las entradas ganadoras se otorgan en categorías como 'Peor abuso del preprocesador de C'. El concurso tiene una larga historia de entradas impresionantes y desconcertantes.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOCCC">IOCCC</a></li>
<li><a href="https://github.com/ioccc-src/winner">GitHub - ioccc-src/winner: Winners of the International ... What Is IOCCC (Internet Obfuscated C Code Contest)? IOCCC (@ioccc@fosstodon.org) IOCCC 2024 Triumphs: Record 23 Winners Unveiled After 4-Year ... The 29th International Obfuscated C Code Contest (IOCCC) 2025 ...</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad expresan admiración por la creatividad, especialmente por la forma del código del emulador de Game Boy y el emulador de 366 bytes. Algunos señalan que el uso de LLMs está permitido, y un comentario desea el regreso del Underhanded C Contest. El sentimiento general es positivo y de asombro.

**Etiquetas**: `#Obfuscación C`, `#Concurso`, `#Programación`, `#Emulación`, `#Creatividad`

---

<a id="item-4"></a>
## [Científicos expulsados de conferencia por reimpresiones de un editorial crítico](https://arstechnica.com/science/2026/06/scientists-ejected-from-diabetes-conference-for-distributing-journal-reprints/) ⭐️ 8.0/10

Steven Kahn, editor en jefe de la revista de la ADA, y Desmond Schatz, expresidente de la ADA, fueron expulsados físicamente de la conferencia anual de la Asociación Estadounidense de Diabetes por distribuir reimpresiones de un editorial crítico sobre la administración de los NIH. Este incidente subraya las crecientes tensiones entre la comunidad científica y la administración gubernamental, lo que genera serias preocupaciones sobre la censura y la libertad académica en las conferencias científicas. Las personas expulsadas incluían a altos cargos de la Asociación Estadounidense de Diabetes, y el editorial fue publicado en la propia revista de la ADA, pero la distribución de reimpresiones se consideró una violación del código de conducta de la conferencia.

hackernews · Ars Technica · jun 7, 10:10 · [Discusión](https://news.ycombinator.com/item?id=48433410)

**Contexto**: Los Institutos Nacionales de Salud (NIH) son la principal agencia gubernamental de EE. UU. para la investigación biomédica. El editorial criticaba la gestión de la administración sobre los NIH, reflejando debates políticos más amplios sobre la financiación y las políticas científicas. La Asociación Estadounidense de Diabetes organiza una conferencia anual donde un código de conducta regula el comportamiento de los asistentes, incluida la distribución de materiales.

**Discusión**: Los comentaristas expresaron indignación por la expulsión, considerándola censura, e invocaron el efecto Streisand, prediciendo que el editorial ganaría mayor atención. Algunos cuestionaron cómo la distribución de un editorial de la propia revista de la ADA podría violar el código de conducta, mientras que otros denunciaron el estado de la financiación científica en EE. UU.

**Etiquetas**: `#Ciencia`, `#Libertad académica`, `#Censura`, `#Política científica`, `#Controversia`

---

<a id="item-5"></a>
## [Estudio de tokenomía revela uso dominante de tokens de entrada en ingeniería de software agéntica](https://arxiv.org/abs/2601.14470) ⭐️ 8.0/10

El artículo 'Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering' mide empíricamente el consumo de tokens en tareas de codificación agéntica, encontrando que los tokens de entrada representan el 53.9% del uso y que la etapa de revisión de código iterativa consume el 59.4% de todos los tokens. Este estudio proporciona datos empíricos críticos sobre la estructura de costos de la ingeniería de software impulsada por IA, esencial para desarrolladores y empresas que utilizan herramientas de IA agéntica. El alto consumo de tokens, especialmente los de entrada, tiene implicaciones significativas para los precios y la eficiencia. El artículo desglosa el uso de tokens en tokens de entrada, salida y razonamiento a lo largo de etapas como revisión de código y síntesis. También señala que el consumo de tokens es altamente variable y estocástico, con ejecuciones de la misma tarea que difieren hasta 30 veces.

hackernews · Anon84 · jun 7, 01:37 · [Discusión](https://news.ycombinator.com/item?id=48430923)

**Contexto**: La ingeniería de software agéntica implica agentes de IA que realizan tareas de desarrollo de forma autónoma, como codificar, depurar y revisar código. Los tokens son las unidades básicas que procesan los modelos de lenguaje, y cada solicitud consume tokens facturados por los proveedores de IA. Entender la tokenomía ayuda a gestionar costos y optimizar la eficiencia.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.14470v1">Tokenomics: Quantifying Where Tokens Are Used in Agentic Software Engineering</a></li>
<li><a href="https://arxiv.org/abs/2604.22750">[2604.22750] How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks</a></li>
<li><a href="https://digitaleconomy.stanford.edu/news/how-are-ai-agents-spending-your-tokens/">How are AI agents spending your tokens? - Stanford Digital Economy Lab</a></li>

</ul>
</details>

**Discusión**: Los comentaristas comparten experiencias personales: uno describe una configuración de múltiples agentes, otro reporta una relación de 10:1 entre tokens de entrada y salida, y se expresan preocupaciones sobre cambios en los precios y la impredecibilidad de los costos. En general, la discusión destaca desafíos reales con el consumo de tokens y la facturación.

**Etiquetas**: `#tokenomía`, `#ingeniería de software agentiva`, `#costos de IA`, `#tokens`, `#aprendizaje automático`

---

<a id="item-6"></a>
## [Ntsc-rs: Emulación open-source de artefactos de TV analógica y VHS](https://ntsc.rs/) ⭐️ 8.0/10

Se ha lanzado un nuevo efecto de video open-source llamado ntsc-rs, que emula con precisión los artefactos de TV analógica y VHS utilizando algoritmos de procesamiento de señales en lugar de superposiciones simples. Este proyecto llena un vacío para creadores de contenido y entusiastas de la retroinformática que buscan una degradación de video analógico auténtica sin hardware real, y su lanzamiento ha generado discusión técnica en la comunidad. La librería modela la transmisión NTSC y la codificación VHS, y está disponible como binario independiente y plugins para After Effects, Premiere y OpenFX. Está escrita en Rust e incluye una interfaz GTK4.

hackernews · gregsadetsky · jun 6, 19:17 · [Discusión](https://news.ycombinator.com/item?id=48428025)

**Contexto**: La TV analógica y las grabaciones VHS tienen artefactos visuales inherentes como ruido, sangrado de color y líneas de barrido. La emulación tradicional usa texturas pre-renderizadas o tablas de consulta de color, mientras que ntsc-rs simula la trayectoria real de la señal analógica para mayor precisión.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://ntsc.rs/">ntsc-rs - an accurate VHS video effect</a></li>
<li><a href="https://github.com/ntsc-rs/ntsc-rs">GitHub - ntsc-rs/ntsc-rs: Free, open-source VHS effect. Standalone application + plugin (After Effects, Premiere, and OpenFX). · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=48428025">Ntsc-rs – open-source video emulation of analog TV and VHS artifacts | Hacker News</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad destacan características faltantes como la desalineación del oscilador vertical y el soporte PAL, pero aprecian la precisión del proyecto. Algunos sugieren usarlo para generar datos de entrenamiento para modelos de IA de eliminación de ruido.

**Etiquetas**: `#emulación de video`, `#NTSC`, `#retroinformática`, `#software libre`, `#señal analógica`

---

<a id="item-7"></a>
## [Diseño con Claude más que con Figma ahora](https://blog.janestreet.com/i-design-with-claude-code-more-than-figma-now-index/) ⭐️ 8.0/10

Un desarrollador de Jane Street describe cómo ha adoptado Claude AI de Anthropic para diseñar interfaces, reemplazando en gran medida a Figma, destacando la iteración ilimitada y la integración con código. Este cambio resalta el creciente papel de la IA en los flujos de trabajo de diseño, reduciendo potencialmente la dependencia de herramientas tradicionales como Figma y permitiendo un prototipado más rápido. También genera debate sobre el futuro de los roles de diseño y la importancia de aprender a programar. Claude es un modelo de lenguaje grande de Anthropic, disponible en diferentes tamaños. El artículo enfatiza que los prototipos se convierten en 'documentos de propuesta vivos' y el código es desechable, con revisores dando retroalimentación sobre diseño y experiencia de usuario.

hackernews · MrBuddyCasino · jun 7, 05:04 · [Discusión](https://news.ycombinator.com/item?id=48431981)

**Contexto**: Claude es una serie de modelos de lenguaje grandes desarrollados por Anthropic, entrenados usando IA constitucional. Figma es una herramienta popular de diseño de interfaces basada en web, utilizada para diseño colaborativo de UI/UX. Jane Street es una firma de trading financiero conocida por su enfoque impulsado por la tecnología y el uso extensivo de OCaml. El artículo refleja una tendencia creciente donde los asistentes de IA generan código para prototipos de interfaz, difuminando las líneas entre diseño y desarrollo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_AI">Claude AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jane_Street_Capital">Jane Street Capital - Wikipedia</a></li>

</ul>
</details>

**Discusión**: Los comentarios expresan opiniones mixtas: algunos aprecian el enfoque pero señalan que Jane Street es inversionista de Anthropic, lo que introduce posible sesgo. Otros valoran que los diseñadores aprendan a programar, mientras que algunos argumentan que el diseño basado en código puede perder aspectos centrados en el humano. Un comentarista también cuestiona el concepto de 'iteración ilimitada', sugiriendo que no es gratuito.

**Etiquetas**: `#diseño con IA`, `#Claude`, `#Jane Street`, `#Figma`, `#prototipado`

---

<a id="item-8"></a>
## [Más allá de fork() y exec() para la creación de procesos](https://lwn.net/SubscriberLink/1076018/16f01bbbb8e0d1f0/) ⭐️ 8.0/10

Un artículo técnico argumenta que el modelo tradicional de creación de procesos fork() + exec() en Unix está obsoleto y propone alternativas más eficientes como posix_spawn y clone. El artículo referencia el influyente trabajo 'A fork() in the road' que detalla las ineficiencias de la llamada al sistema fork. Esta discusión cuestiona un mecanismo fundamental de Unix, lo que podría influir en futuros diseños de sistemas operativos y mejorar la eficiencia en la creación de procesos. Plantea preguntas importantes sobre la conveniencia de programación frente al rendimiento en las llamadas al sistema. El artículo señala que fork() es O(N) en el tamaño del proceso y que las optimizaciones de copia en escritura no eliminan su sobrecarga. Alternativas como posix_spawn combinan la creación y ejecución del proceso en una sola llamada, evitando copias de memoria innecesarias.

hackernews · jwilk · jun 6, 14:34 · [Discusión](https://news.ycombinator.com/item?id=48425528)

**Contexto**: En Unix, la creación de un nuevo proceso tradicionalmente usa fork() para duplicar el proceso padre, luego exec() para reemplazar la imagen del hijo con un nuevo programa. Este enfoque de dos pasos fue innovador en los años 1970 pero ahora se considera ineficiente porque fork copia todo el estado del proceso, a menudo descartado inmediatamente por exec. La copia en escritura mitiga esto pero no elimina la sobrecarga. Alternativas como posix_spawn y clone ofrecen una creación de procesos más eficiente al combinar pasos o permitir un control más detallado sobre los recursos compartidos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://pubs.opengroup.org/onlinepubs/9699919799/functions/posix_spawn.html">posix_spawn</a></li>
<li><a href="https://www.man7.org/linux/man-pages/man2/clone.2.html">clone(2) - Linux manual page</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad incluyen debates sobre el costo real de fork, algunos señalando que la copia en escritura lo hace menos caro de lo asumido, mientras que otros argumentan que el modelo permite una configuración flexible mediante las APIs existentes. Algunos comentaristas expresan frustración por la falta de una forma directa de crear un nuevo proceso sin clonar, y otros defienden la elegancia de fork.

**Etiquetas**: `#Unix`, `#fork/exec`, `#sistemas operativos`, `#procesos`, `#ingeniería de software`

---

<a id="item-9"></a>
## [Aprendizaje autosupervisado en grafos sin entrenamiento iguala GCN con 5× menos etiquetas](https://www.reddit.com/r/MachineLearning/comments/1tyovlr/trainingfree_graph_ssl_matches_gcn_with_5_fewer/) ⭐️ 8.0/10

Un nuevo método llamado Optimus realiza aprendizaje autosupervisado en grafos sin entrenamiento, logrando una precisión comparable a las redes convolucionales de grafos (GCN) usando hasta cinco veces menos ejemplos etiquetados. Esto reduce significativamente la dependencia de grandes conjuntos de datos etiquetados para las redes neuronales de grafos, haciéndolas más prácticas en dominios donde las etiquetas son escasas. En el conjunto de datos PathMNIST con 2000 nodos y 9 clases, Optimus alcanzó un 73.9% de precisión con solo 9 etiquetas (una por clase), superando el 60.6% de GCN. Hay una demo interactiva en Hugging Face Spaces para realizar pruebas.

reddit · r/MachineLearning · /u/Loner_Indian · jun 6, 18:27

**Contexto**: Las redes neuronales de grafos (GNN) son modelos de aprendizaje profundo diseñados para datos estructurados en grafos. Las redes convolucionales de grafos (GCN) extienden las operaciones de convolución a los grafos, permitiendo que los modelos aprendan de las características de los nodos y la topología del grafo. El aprendizaje semisupervisado en grafos utiliza un pequeño conjunto de nodos etiquetados para inferir etiquetas para los nodos restantes, un enfoque que se vuelve difícil con muy pocas etiquetas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://tkipf.github.io/graph-convolutional-networks/">Graph Convolutional Networks | Thomas Kipf | Google DeepMind</a></li>

</ul>
</details>

**Etiquetas**: `#aprendizaje autosupervisado`, `#grafos`, `#eficiencia de rótulos`, `#GNN`, `#semisupervisado`

---

<a id="item-10"></a>
## [Cohere ofrece acceso anticipado a modelo de codificación no lanzado](https://www.reddit.com/r/LocalLLaMA/comments/1tylzy2/coheres_unreleased_coding_model_early_access_for/) ⭐️ 8.0/10

Cohere ha lanzado acceso anticipado a su primer modelo de codificación, un MoE de 30B con 3B parámetros activos, para pruebas comunitarias antes del lanzamiento oficial. Esto marca la entrada de Cohere en el espacio de modelos de codificación y utiliza una estrategia de acceso anticipado para recopilar comentarios de la comunidad. La arquitectura MoE permite una ejecución local eficiente, haciendo que la asistencia avanzada de codificación sea más accesible. El modelo tiene 30 mil millones de parámetros totales, pero solo 3 mil millones están activos por token, lo que permite ejecutarlo en configuraciones locales. Cohere destaca su velocidad y busca activamente comentarios de usuarios para perfeccionar el modelo antes del lanzamiento oficial.

reddit · r/LocalLLaMA · /u/nick_frosst · jun 6, 16:36

**Contexto**: MoE (Mixture of Experts) es una técnica de aprendizaje automático donde múltiples subredes expertas se especializan en diferentes partes de la entrada, y por cada token solo se activa un subconjunto de expertos. Esto reduce el costo computacional manteniendo una alta capacidad del modelo. Los parámetros activos se refieren a los parámetros utilizados para una entrada dada, a diferencia de los parámetros totales. Este enfoque permite que modelos grandes se ejecuten eficientemente en hardware de consumo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts ? | IBM</a></li>

</ul>
</details>

**Etiquetas**: `#modelo de codificación`, `#Cohere`, `#acceso anticipado`, `#MoE`, `#código abierto`

---

<a id="item-11"></a>
## [Vulnerabilidad en herramienta de IA de PewDiePie permite toma de control de administrador con un clic](https://www.reddit.com/r/LocalLLaMA/comments/1tys1wj/another_1click_admin_account_takeover_in/) ⭐️ 8.0/10

Se ha divulgado una vulnerabilidad de seguridad que permite tomar el control de cuentas de administrador con un solo clic en la herramienta de IA de PewDiePie, llamada Odysseus. El problema afecta a usuarios que hagan clic en un enlace malicioso, lo que podría comprometer sus cuentas. Esta vulnerabilidad pone en riesgo a miles de usuarios de la popular herramienta de IA, exponiéndolos a la toma de control de sus cuentas y al robo de datos. Resalta las persistentes preocupaciones de seguridad en aplicaciones de IA ampliamente adoptadas pero desarrolladas rápidamente. El ataque no requiere habilidades avanzadas y puede ejecutarse mediante un enlace especialmente diseñado. Se reporta como 'otra' toma de control con un clic, lo que sugiere que pueden haberse encontrado vulnerabilidades previas en la misma herramienta.

reddit · r/LocalLLaMA · /u/theonejvo · jun 6, 20:32

**Contexto**: La herramienta de IA de PewDiePie, Odysseus, es una plataforma lanzada recientemente que busca dar a los usuarios control sobre las herramientas de IA, a diferencia de los modelos basados en suscripción. Una vulnerabilidad de toma de control con un clic típicamente permite a un atacante obtener acceso no autorizado a la cuenta de un usuario engañándolo para que haga clic en un enlace, a menudo explotando una autenticación o manejo de sesión débil.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://medium.com/no-time/pewdiepies-new-ai-tool-odysseus-just-launched-honest-review-0134fb77729f">PewDiePie ’s New AI Tool (Odysseus) Just Launched... | Medium</a></li>
<li><a href="https://marxchryz.medium.com/escalating-an-html-injection-into-1-click-account-takeover-3ba9dbf0ce5f">Escalating an HTML Injection into 1 - Click Account Takeover | Medium</a></li>

</ul>
</details>

**Etiquetas**: `#seguridad`, `#vulnerabilidad`, `#cuenta de administrador`, `#herramienta de IA`, `#PewDiePie`

---

<a id="item-12"></a>
## [120 tok/s en 12 GB VRAM con Gemma 4 12B QAT MTP](https://www.reddit.com/r/LocalLLaMA/comments/1typjmc/120_toks_on_12gb_vram_with_gemma_4_12b_qat_mtp/) ⭐️ 8.0/10

Un usuario logró una velocidad de inferencia de 120 tokens por segundo con el modelo Gemma 4 12B QAT de Google en una GPU de 12 GB utilizando una versión modificada de llama.cpp y un modelo auxiliar de predicción multi-token (MTP). Esto demuestra que modelos de lenguaje grandes como Gemma 4 pueden ejecutarse eficientemente en GPU de consumo, haciendo que la IA avanzada sea más accesible. La combinación de QAT y MTP aumenta la velocidad de inferencia sin pérdida significativa de calidad, beneficiando el despliegue local de LLM. La configuración usa la versión cuantizada GGUF de Unsloth de Gemma 4 12B QAT y un modelo auxiliar GGUF Q8_0 para MTP, logrando hasta 135.7 tok/s en algunas tareas. La inferencia se ejecutó en una RTX 4070 Super con 12 GB VRAM, usando una compilación de llama.cpp modificada con soporte CUDA y un tamaño de contexto de 131072.

reddit · r/LocalLLaMA · /u/janvitos · jun 6, 18:53

**Contexto**: El entrenamiento consciente de la cuantización (QAT, por sus siglas en inglés) es una técnica que simula la aritmética de baja precisión durante el entrenamiento, permitiendo que los modelos mantengan precisión incluso cuando se cuantizan para inferencia eficiente. La predicción multi-token (MTP) es una forma de decodificación especulativa donde un modelo auxiliar más pequeño predice varios tokens por adelantado, que un modelo objetivo más grande verifica en paralelo, acelerando la generación. llama.cpp es un motor de inferencia de código abierto optimizado para ejecutar modelos grandes de lenguaje en hardware de consumo, y utiliza el formato GGUF para almacenar modelos cuantizados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>
<li><a href="https://mgrowtech.com/google-ai-releases-multi-token-prediction-mtp-drafters-for-gemma-4-delivering-up-to-3x-faster-inference-without-quality-loss/">Google AI Releases Multi-Token Prediction (MTP) Drafters for</a></li>
<li><a href="https://medium.com/data-science/llama-cpp-writing-a-simple-c-inference-program-for-gguf-llm-models-12bc5f58505f">llama.cpp: Writing A Simple C++ Inference Program for GGUF LLM</a></li>

</ul>
</details>

**Etiquetas**: `#Gemma 4`, `#cuantización`, `#benchmark`, `#llama.cpp`, `#especulación de tokens`

---

<a id="item-13"></a>
## [Archivo de imágenes de dominio público con procedencia](https://pdimagearchive.org/) ⭐️ 7.0/10

Se ha lanzado el Public Domain Image Archive, que ofrece una colección curada de imágenes de dominio público con documentación clara del estado de derechos y la procedencia tanto de la obra subyacente como de la copia digital. Este archivo aborda una necesidad crítica de información de procedencia, que a menudo falta en las colecciones de imágenes de dominio público, brindando a los usuarios confianza legal para su reutilización en proyectos, publicaciones o trabajos comerciales. Cada página de imagen incluye la fecha, el estado de derechos de la obra subyacente y el de la copia digital, con un enlace a una guía detallada de reutilización que aclara la declaración 'sin restricciones conocidas' y ofrece orientación para la autorización de derechos de autor.

hackernews · davidbarker · jun 7, 00:22 · [Discusión](https://news.ycombinator.com/item?id=48430539)

**Contexto**: Muchos sitios web afirman que las imágenes son de dominio público pero no proporcionan evidencia ni documentación de los derechos. El Public Domain Image Archive se destaca al documentar la procedencia, esencial para los usuarios que necesitan verificar el estado de los derechos de autor y evitar riesgos legales.

**Discusión**: Los comentaristas generalmente elogiaron el sitio por su transparencia y utilidad, especialmente la documentación de procedencia. Algunos plantearon preocupaciones prácticas sobre la autorización de derechos de autor y notaron una pequeña molestia en la interfaz de usuario con el desplazamiento en vista infinita.

**Etiquetas**: `#dominio público`, `#imágenes`, `#archivo digital`, `#procedencia`, `#recursos abiertos`

---

<a id="item-14"></a>
## [Superviviente de tiroteo escolar demanda a empresa de detección de armas con IA por fallo](https://arstechnica.com/tech-policy/2026/06/school-shooting-survivor-sues-ai-gun-detection-firm-after-system-failed-to-spot-weapon/) ⭐️ 7.0/10

Un superviviente de un tiroteo escolar ha presentado una demanda contra una empresa de detección de armas con IA, alegando que su sistema no logró identificar el arma durante el incidente, lo que plantea preguntas sobre la precisión aceptable de dichos sistemas. Esta demanda resalta las consecuencias reales de los fallos de IA en entornos críticos como las escuelas, y subraya la necesidad de estándares claros de precisión y responsabilidad legal para los sistemas de detección de amenazas basados en IA. El sistema de IA en cuestión utiliza visión por computadora y aprendizaje profundo para detectar armas de fuego en transmisiones de video en vivo, pero supuestamente no detectó el arma. La demanda argumenta que la comercialización de 'precisión excepcional' por parte de la empresa fue engañosa, y busca determinar qué nivel de precisión es legalmente requerido.

rss · Ars Technica · jun 7, 11:08

**Contexto**: Los sistemas de detección de armas con IA son utilizados por escuelas y otras instalaciones para identificar automáticamente armas de fuego visibles en videos de vigilancia. Estos sistemas se entrenan con grandes conjuntos de datos de imágenes de armas utilizando modelos de aprendizaje profundo como YOLO, pero su precisión puede variar y generalmente se mide con métricas como la precisión media promedio (mAP) y el recall. A pesar de las afirmaciones de marketing, ningún sistema es 100% preciso, y los falsos negativos pueden tener consecuencias de vida o muerte.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://roc.ai/ai-gun-detection/">Gun Detection System - AI Visual Threat Software | ROC</a></li>
<li><a href="https://www.omnilert.com/solutions/ai-gun-detection">AI Gun Detection Technology: Elevating Security and Safety | Omnilert</a></li>
<li><a href="https://volt.ai/blog/top-8-ai-gun-detection-providers-for-schools">Top 8 AI Gun Detection Providers for Schools</a></li>

</ul>
</details>

**Etiquetas**: `#IA`, `#detección de armas`, `#seguridad escolar`, `#responsabilidad legal`, `#precisión`

---

<a id="item-15"></a>
## [dvlt.cu: motor de inferencia en CUDA/C++ para el transformador 3D DVLT de NVIDIA](https://www.reddit.com/r/LocalLLaMA/comments/1tyu79c/dvltcu_inference_engine_written_from_scratch_in/) ⭐️ 7.0/10

Un desarrollador publicó dvlt.cu, un motor de inferencia altamente optimizado para el modelo transformador 3D DVLT de NVIDIA, escrito completamente desde cero en CUDA y C++ con dependencias mínimas. Esto demuestra que la reconstrucción 3D basada en transformadores puede ejecutarse eficientemente sin frameworks pesados, lo que podría permitir una experimentación más rápida y accesible en visión 3D. El binario pesa solo 5 MB, usa pesos bfloat16 cargados mediante mmap, y depende únicamente de cuBLASLt y cuTLASS para operaciones matriciales. Los pesos tienen una licencia no comercial de NVIDIA.

reddit · r/LocalLLaMA · /u/yassa9 · jun 6, 22:04

**Contexto**: DVLT es un modelo transformador 3D de NVIDIA para reconstrucción 3D multivista. Los pipelines de inferencia tradicionales dependen de frameworks pesados como PyTorch y TensorFlow, pero dvlt.cu los evita al implementar el modelo directamente en CUDA/C++. Esto reduce el tamaño del binario y las dependencias, a costa de apuntar solo a un modelo específico.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.30215v2">Déjà View: Looping Transformers for Multi-View 3D</a></li>
<li><a href="https://github.com/NVIDIA/CUDALibrarySamples/tree/main/cuBLASLt">CUDALibrarySamples/cuBLASLt at main · NVIDIA ... - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bfloat16_floating-point_format">bfloat16 floating-point format - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#CUDA`, `#C++`, `#inferencia`, `#DVLT`, `#reconstrucción 3D`

---

<a id="item-16"></a>
## [open-deepthink lanza el modo completo de destilación de conocimiento](https://www.reddit.com/r/LocalLLaMA/comments/1tz0zwy/5_months_later_opendeepthink_now_has_full/) ⭐️ 7.0/10

open-deepthink ha lanzado un modo completo de destilación de conocimiento donde una topología fija de red neuronal cuántica (QNN) de 7 capas evoluciona agentes en vivo durante la sesión, produciendo conjuntos de datos JSON estructurados que contienen el rastro de desarrollo del conocimiento extraído de un LLM objetivo. Esto mejora significativamente la capacidad de destilar conocimiento de modelos de código cerrado en modelos de código abierto, permitiendo un razonamiento más profundo y personalización, y democratiza el acceso a capacidades avanzadas de LLM al ejecutarse localmente. La versión beta-0.0.3 corrige 11 errores, pasa 195/195 pruebas y permite la selección de modelo por agente; el proyecto fue renombrado de local-deepthink a open-deepthink.

reddit · r/LocalLLaMA · /u/causality-ai · jun 7, 03:24

**Contexto**: La destilación de conocimiento es una técnica donde un modelo más pequeño se entrena para imitar un modelo más grande y más capaz. open-deepthink implementa esto con un enfoque multiagente utilizando algoritmos evolutivos para optimizar la colaboración y profundidad. El uso de topología QNN es experimental pero promete ventajas inspiradas en la computación cuántica.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.15048v1">GAT-QNN: Genetic Algorithm-Based Training of Hybrid Quantum</a></li>

</ul>
</details>

**Etiquetas**: `#destilación de conocimiento`, `#agentes múltiples`, `#redes evolutivas`, `#LLMs locales`, `#código abierto`

---

<a id="item-17"></a>
## [Home Assistant automatiza el hogar según señales de recuperación corporal, no solo movimiento](https://www.reddit.com/r/homeassistant/comments/1tyzctq/i_made_home_assistant_react_to_my_bodys_recovery/) ⭐️ 7.0/10

Un usuario de Reddit desarrolló una integración de Home Assistant que usa datos biométricos de wearables (HRV, sueño, oxígeno en sangre) para ajustar la iluminación y el ambiente del hogar según el estado de recuperación del usuario, en lugar de basarse únicamente en sensores de movimiento o presencia. Este enfoque representa un cambio de la automatización basada en la ubicación a una conciencia fisiológica del hogar inteligente, lo que podría permitir entornos que se adapten a las necesidades de recuperación y niveles de energía del usuario. Todo el proceso se ejecuta localmente: los datos de HealthKit se envían a un servidor local, se reenvían mediante MQTT a Home Assistant y se procesan allí. El sistema funciona correctamente incluso cuando los datos no están disponibles, y la entrada manual siempre anula la automatización.

reddit · r/homeassistant · /u/semiramist · jun 7, 02:03

**Contexto**: Home Assistant es una plataforma de automatización del hogar de código abierto que se integra con varios dispositivos y sensores. La variabilidad de la frecuencia cardíaca (HRV) es la variación en el tiempo entre latidos, utilizada a menudo como indicador de estrés y recuperación. MQTT es un protocolo de mensajería ligero para dispositivos IoT, comúnmente usado para la comunicación entre componentes en sistemas de hogar inteligente.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Heart_rate_variability">Heart rate variability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/MQTT">MQTT - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#Home Assistant`, `#automatización del hogar`, `#datos biométricos`, `#IoT`, `#salud`

---

<a id="item-18"></a>
## [Usuario encuentra control perdido con Claude y Home Assistant](https://www.reddit.com/r/homeassistant/comments/1tyzwzz/claude_ha_found_my_lost_remote/) ⭐️ 7.0/10

Un usuario de Reddit utilizó el asistente de IA Claude de Anthropic integrado con Home Assistant para encontrar un control remoto extraviado del NVIDIA Shield, haciendo que Claude enviara un comando ADB para hacer sonar el control, y Claude creó automáticamente un script para uso futuro. Esto demuestra un caso de uso práctico y directo de asistentes de IA integrados con plataformas de hogar inteligente, permitiendo el control en lenguaje natural de interacciones complejas de dispositivos y automatizando tareas de solución de problemas con facilidad. Claude utilizó la integración de Home Assistant con el NVIDIA Shield para descubrir el paquete 'com.remote.locator' y ejecutó un comando ADB para activar el localizador del control remoto. El usuario tuvo que confirmar el sonido, y Claude ofreció crear un script llamado 'script.find-shield-remote' para uso futuro.

reddit · r/homeassistant · /u/cdarrigo · jun 7, 02:31

**Contexto**: Home Assistant es una plataforma de automatización del hogar de código abierto que permite a los usuarios integrar y controlar varios dispositivos inteligentes desde una única interfaz. Claude es un modelo de lenguaje grande desarrollado por Anthropic, diseñado para ser un asistente de IA seguro y útil. Esta integración permite comandos en lenguaje natural para controlar automatizaciones de Home Assistant.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (language model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Home_Assistant">Home Assistant - Wikipedia</a></li>
<li><a href="https://www.home-assistant.io/">Home Assistant</a></li>

</ul>
</details>

**Etiquetas**: `#Home Assistant`, `#Inteligencia Artificial`, `#Domótica`, `#Automatización`, `#Claude`

---

<a id="item-19"></a>
## [Fast Search Card: Panel que se construye solo para Home Assistant](https://www.reddit.com/r/homeassistant/comments/1tytmnz/fast_search_card_a_dashboard_that_builds_itself/) ⭐️ 7.0/10

Fast Search Card es una tarjeta Lovelace personalizada para Home Assistant que construye automáticamente un panel completo a partir de la configuración de dispositivos existente, eliminando la necesidad de mantenimiento manual del panel. Se instala a través de HACS con una sola línea de YAML y lee los nombres de las entidades, áreas y configuraciones de visibilidad para crear una interfaz basada en búsqueda con búsqueda difusa, una pantalla de inicio estilo bento, calendario, tareas, panel de energía y más. Esta tarjeta resuelve un problema común en Home Assistant: el tedioso proceso de mantener manualmente un panel cada vez que se añaden o renombran dispositivos. Al autoconstruirse a partir de la configuración existente, reduce la fricción y anima a los usuarios a centrarse en la automatización en lugar de en la decoración de la interfaz. La tarjeta pesa aproximadamente 450 KB comprimida, arranca en menos de un segundo y tiene cero telemetría con una auditoría de seguridad publicada. Tiene licencia GPL-3.0 y fue construida con una asistencia significativa de IA (principalmente Claude), cada commit lo declara en el pie de página. No requiere Docker, complementos o demonios; vive completamente en el navegador y sobrevive a las actualizaciones del núcleo de HA.

reddit · r/homeassistant · /u/fastender · jun 6, 21:39

**Contexto**: Home Assistant es una plataforma de automatización del hogar de código abierto que utiliza un marco de interfaz de usuario llamado Lovelace para mostrar paneles. Tradicionalmente, los usuarios configuran sus paneles Lovelace manualmente a través de YAML o el editor de interfaz, lo que puede convertirse en una carga de mantenimiento a medida que los dispositivos cambian. HACS (Home Assistant Community Store) es una forma popular de instalar integraciones y tarjetas personalizadas. Fast Search Card aprovecha estas bases existentes para generar automáticamente un panel basado en la configuración de dispositivos y áreas del usuario.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.home-assistant.io/blog/2019/01/23/lovelace-released/">Lovelace UI released! - Home Assistant</a></li>
<li><a href="https://www.hacs.xyz/docs/use/download/download/">Step-by-step instructions on downloading HACS to your Home Assistant</a></li>

</ul>
</details>

**Etiquetas**: `#Home Assistant`, `#Panel de control`, `#Automatización del hogar`, `#Búsqueda`, `#Tarjeta Lovelace`

---

<a id="item-20"></a>
## [Campo de clones: cómo las réplicas de caballos llegaron a dominar el polo](https://knowablemagazine.org/content/article/technology/2026/cloned-polo-horses) ⭐️ 6.0/10

La clonación de caballos se ha vuelto prevalente en el polo, permitiendo la replicación de sementales campeones y generando debates sobre diversidad genética y regulación. Esta tendencia podría alterar fundamentalmente los deportes ecuestres, reduciendo la diversidad genética y planteando preocupaciones éticas sobre la clonación de animales para obtener ventaja competitiva. Los caballos clonados se producen mediante transferencia nuclear de células somáticas (SCNT), creando copias genéticamente casi idénticas, pero aún presentan variaciones naturales debidas a factores epigenéticos y ambientales.

hackernews · gscott · jun 7, 02:46 · [Discusión](https://news.ycombinator.com/item?id=48431286)

**Contexto**: La clonación es el proceso de crear una copia genéticamente idéntica de un organismo. En caballos, la clonación ha estado disponible comercialmente durante más de una década, utilizada principalmente para preservar la genética de animales valiosos. En el polo, los ponis clonados se han vuelto cada vez más comunes, permitiendo a los equipos reproducir los rasgos de los caballos de mejor rendimiento, pero generando preocupaciones sobre la reducción de la diversidad genética y la regulación del deporte.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.geminigenetics.com/how-to-clone-horse/">How To Clone Your Horse - Gemini Genetics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cloning">Cloning - Wikipedia</a></li>
<li><a href="https://brian.carnell.com/articles/1998/cloning-could-conserve-animal-genetic-diversity/">Cloning could conserve animal genetic diversity –</a></li>

</ul>
</details>

**Discusión**: Los comentaristas expresaron preocupaciones sobre la diversidad genética si todos clonan el mismo caballo, señalando que esto podría limitar la evolución de mejores caballos. Otros reflexionaron humorísticamente sobre la familiaridad de los caballos clonados, mientras que otro señaló un video de drama legal sobre el tema. Algunos especularon que el polo podría adoptar reglas de 'diseño único' basadas en clones.

**Etiquetas**: `#clonación`, `#caballos`, `#polo`, `#biotecnología`, `#deportes`

---

<a id="item-21"></a>
## [Investigadores independientes buscan respaldo en arXiv para pipeline SAM 2.1-LocateAnything](https://www.reddit.com/r/MachineLearning/comments/1tza169/two_independent_mlcv_researchers_meng/) ⭐️ 6.0/10

Dos investigadores independientes solicitan respaldo para arXiv de su artículo sobre un pipeline sin entrenamiento que conecta LocateAnything-3B de NVIDIA con SAM 2.1 de Meta para mejorar la segmentación texto-máscara. Reportan 0.772 mIoU en RefCOCO val, superando a Grounding DINO Base (0.717) con el mismo backend de SAM 2.1. Este trabajo demuestra que la elección del grounder impacta significativamente la calidad final de la máscara incluso en pipelines modulares congelados, y obtener resultados sólidos sin entrenamiento podría reducir las barreras computacionales. También resalta los desafíos de publicación que enfrentan los investigadores independientes sin afiliación institucional. El pipeline usa LocateAnything-3B como grounder y SAM 2.1 como segmentador, con un adaptador ligero que los conecta. Los autores reconocen que RefCOCO aparece en los datos de entrenamiento de LocateAnything, por lo que presentan los resultados como evaluación en dominio y no como transferencia cero-shot.

reddit · r/MachineLearning · /u/j_root_ · jun 7, 11:49

**Contexto**: El visual grounding consiste en localizar objetos en imágenes según descripciones en lenguaje natural. Modelos como Grounding DINO realizan detección de objetos en conjunto abierto, mientras que SAM (Segment Anything Model) es un modelo de segmentación fundamental. LocateAnything es un modelo más reciente de visión-lenguaje para grounding rápido y de alta calidad. Este artículo aísla el efecto de diferentes grounders en un pipeline modular para evaluar su influencia en las máscaras de segmentación finales.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/LocateAnything-3B">nvidia/LocateAnything-3B · Hugging Face</a></li>
<li><a href="https://huggingface.co/IDEA-Research/grounding-dino-base">IDEA-Research/grounding-dino-base · Hugging Face</a></li>
<li><a href="https://huggingface.co/docs/transformers/en/model_doc/grounding-dino">Grounding DINO</a></li>

</ul>
</details>

**Etiquetas**: `#machine learning`, `#visión por computadora`, `#segmentación semántica`, `#arXiv`, `#procesamiento de imágenes`

---

<a id="item-22"></a>
## [Debate sobre cuantizaciones alternativas para modelos QAT como Gemma-4](https://www.reddit.com/r/MachineLearning/comments/1tyo8gf/does_it_make_sense_to_use_alternative/) ⭐️ 6.0/10

Una publicación en Reddit cuestiona si usar métodos de cuantización alternativos (p. ej., de Unsloth) en Gemma-4, entrenado con Quantization-Aware Training (QAT), socava los beneficios del QAT o es una optimización válida. El debate resalta una tensión entre seguir la ruta de cuantización prevista por QAT y aprovechar técnicas de cuantización más agresivas que pueden ofrecer ganancias adicionales de eficiencia, lo cual es crucial para implementar modelos grandes en entornos con recursos limitados. La publicación hace referencia a puntos de referencia de Unsloth que muestran que las cuantizaciones alternativas de Gemma-4-QAT producen resultados más cercanos a los ajustes finos de QAT, lo que plantea la pregunta de si dichas cuantizaciones preservan los beneficios de precisión previstos por QAT.

reddit · r/MachineLearning · /u/we_are_mammals · jun 6, 18:02

**Contexto**: Quantization-Aware Training (QAT) es una técnica donde se simula la cuantización durante el entrenamiento, lo que permite que el modelo se adapte a la inferencia de menor precisión, generalmente dando mejor precisión que la cuantización posterior al entrenamiento. Gemma-4 es una familia de modelos abiertos de Google DeepMind, construidos con QAT. Unsloth es una biblioteca que proporciona métodos de cuantización personalizados, incluido soporte para modelos como Gemma-4. La discusión se centra en si usar un esquema de cuantización diferente al utilizado durante el entrenamiento QAT anula las ventajas del QAT.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/quantization-aware-training">What is quantization aware training? - IBM</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 is a family of open models , purpose-built for advanced...</a></li>
<li><a href="https://huggingface.co/unsloth/gemma-4-12b-it-GGUF">unsloth/gemma-4-12b-it-GGUF · Hugging Face</a></li>

</ul>
</details>

**Etiquetas**: `#cuantización`, `#modelos QAT`, `#Gemma-4`, `#Machine Learning`, `#optimización de modelos`

---

<a id="item-23"></a>
## [Plataforma de lifelogging desarrollada en solitario alcanza 4 años de uso diario](https://www.reddit.com/r/selfhosted/comments/1tz7z34/lifelog_platform_i_use_daily_and_developed_for_4/) ⭐️ 6.0/10

Un usuario anunció LifelogBB, una plataforma de lifelogging autohospedada y para un solo usuario que ha desarrollado durante unos 4 años y usa a diario, publicada bajo la licencia AGPL v3.0. Este proyecto demuestra la viabilidad de una plataforma integral de lifelogging autohospedada desarrollada por una sola persona, ofreciendo una alternativa integrada a múltiples aplicaciones especializadas y dando a los usuarios control total sobre sus datos. Todos los datos se almacenan en un único archivo SQLite para portabilidad, la arquitectura se mantiene simple para facilitar modificaciones, e incluye una API RESTful con Swagger UI, feeds iCal, un servidor MCP y chat AI opcional compatible con LLMs locales.

reddit · r/selfhosted · /u/spech66 · jun 7, 09:56

**Contexto**: El lifelogging es la práctica de registrar diversos aspectos de la vida diaria, a menudo utilizando herramientas digitales. Las plataformas autohospedadas permiten a los individuos ejecutar software en sus propios servidores, manteniendo la privacidad y el control. La licencia AGPL v3.0 garantiza que las obras derivadas también permanezcan de código abierto, fomentando contribuciones de la comunidad.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lifelogging">Lifelogging</a></li>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#lifelogging`, `#autohospedaje`, `#seguimiento de peso`, `#diario personal`, `#código abierto`

---

<a id="item-24"></a>
## [Rootprint: gestión de logs autogestionada y de código abierto](https://www.reddit.com/r/selfhosted/comments/1tz7phe/rootprint_selfhosted_and_opensource_logs_at_scale/) ⭐️ 6.0/10

Rootprint es una nueva herramienta de código abierto que proporciona indexación, almacenamiento y consulta de logs autoalojados, construida sobre Quickwit. Añade funciones esenciales como autenticación, interfaz de usuario e histogramas. Rootprint hace posible ejecutar un sistema de gestión de logs de grado de producción completamente en su propia infraestructura, reduciendo la dependencia de servicios externos. Su arquitectura con almacenamiento y cómputo desacoplados permite un escalado rentable y un mejor control sobre los datos de logs. La herramienta utiliza Honojs, Svelte, Postgres y Quickwit, y almacena datos en almacenamiento compatible con S3 con capas de cómputo y almacenamiento completamente separadas. Rootprint ya está desplegado en producción en la empresa del desarrollador, demostrando su madurez.

reddit · r/selfhosted · /u/badfatcat17 · jun 7, 09:41

**Contexto**: Quickwit es un motor de búsqueda de código abierto diseñado específicamente para datos de logs y observabilidad, capaz de consultar datos directamente desde el almacenamiento en la nube con latencia de subsegundo. Utiliza almacenamiento columnar y compresión para la eficiencia, pero carece de autenticación integrada, interfaz de usuario e histogramas. Rootprint aborda estas carencias, convirtiendo a Quickwit en una solución de gestión de logs más completa.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://quickwit.io/docs">Quickwit documentation | Quickwit</a></li>
<li><a href="https://github.com/quickwit-oss/quickwit">GitHub - quickwit -oss/ quickwit : Cloud-native search engine for...</a></li>

</ul>
</details>

**Etiquetas**: `#logs`, `#autoalojado`, `#código abierto`, `#monitoreo`, `#Quickwit`

---

<a id="item-25"></a>
## [Agrupando tres Jetson Nano Orin Super](https://www.reddit.com/r/LocalLLaMA/comments/1tz7s8n/clustering_3x_jetson_nano_orin_supers/) ⭐️ 6.0/10

Se ha publicado una guía que explica cómo agrupar tres dispositivos Jetson Nano Orin Super para entrenamiento e inferencia distribuida, como parte de una serie sobre construcción de pequeños clústeres de computación con hardware asequible. Esta guía reduce la barrera de entrada para la IA distribuida, permitiendo a aficionados y desarrolladores ejecutar modelos grandes en clústeres de bajo consumo. Demuestra que la IA de alto rendimiento ya no es exclusiva de grandes centros de datos. El Jetson Orin Nano Super ofrece hasta 67 TOPS, 1024 núcleos CUDA y 8 GB de memoria unificada. La configuración incluye redes y ajustes de software para habilitar entrenamiento e inferencia distribuida en el clúster.

reddit · r/LocalLLaMA · /u/East-Muffin-6472 · jun 7, 09:45

**Contexto**: La NVIDIA Jetson Orin Nano Super es una placa compacta de IA en el borde con una GPU Ampere y 67 TOPS de rendimiento de IA, a un precio de $249. Agrupar estos dispositivos permite distribuir cargas de trabajo de IA entre varios nodos, una técnica común en grandes centros de datos ahora accesible en hardware de borde de bajo consumo. Esta guía se basa en publicaciones anteriores para clústeres con Mac Mini y Raspberry Pi.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/">Jetson Orin Nano Super Developer Kit - NVIDIA</a></li>
<li><a href="https://www.amazon.com/NVIDIA-Jetson-Orin-Nano-Developer/dp/B0BZJTQ5YP">NVIDIA Jetson Orin Nano Super Developer Kit - amazon.com NVIDIA Jetson Orin™ Nano Super Developer Kit | Gen AI ... NVIDIA Jetson Orin™ Nano Super Developer Kit - Seeed Studio NVIDIA Jetson Orin Nano Super Specs - TechPowerUp Jetson ORIN NANO SUPER - Yahboom ajeetraina/jetson-orin-nano-super-guide - GitHub Computer Components - Deals On External Components</a></li>

</ul>
</details>

**Etiquetas**: `#clúster`, `#Jetson Nano`, `#aprendizaje distribuido`, `#entrenamiento de IA`, `#edge computing`

---

<a id="item-26"></a>
## [espControl añade protector de pantalla con carátulas de álbumes](https://www.reddit.com/r/homeassistant/comments/1tyi5pr/added_cover_art_screen_saver_to_espcontrol/) ⭐️ 6.0/10

La última actualización de espControl añade una vista de carátula de álbum a pantalla completa con detalles de pista y barra de progreso, barra de reloj personalizable con múltiples lecturas de temperatura, soporte ampliado de idiomas y protección opcional con contraseña. Esta actualización mejora el atractivo visual y la personalización de espControl, convirtiéndolo en un panel de control más atractivo y funcional para Home Assistant. Muestra la creciente madurez de los controladores táctiles DIY para el hogar inteligente. El protector de pantalla con carátula se puede descartar tocando para volver a los controles. La barra de reloj ahora recuerda su diseño en diferentes tamaños de pantalla. La protección con contraseña está disponible para configuraciones manuales de ESPHome.

reddit · r/homeassistant · /u/hometechgeek · jun 6, 14:05

**Contexto**: espControl es un controlador de hogar inteligente sin código y fácil de configurar para Home Assistant, diseñado para pantallas táctiles basadas en ESP32 como la económica pantalla S3 de 4 pulgadas por £16. Utiliza el firmware ESPHome para integrarse con Home Assistant. Esta actualización añade funciones comunes en pantallas de hogar inteligente comerciales.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/ESPHome">ESPHome</a></li>
<li><a href="https://esphome.io/">ESPHome - Smart Home Made Simple</a></li>

</ul>
</details>

**Etiquetas**: `#espControl`, `#Home Assistant`, `#pantalla de bloqueo`, `#carátula de álbum`, `#personalización`

---

<a id="item-27"></a>
## [Cómo arreglar dispositivos IKEA Matter en Home Assistant](https://www.reddit.com/r/homeassistant/comments/1tz6wye/how_i_solved_my_ikea_matter_integration/) ⭐️ 6.0/10

Un usuario de Home Assistant resolvió problemas persistentes con dispositivos Matter de IKEA añadiéndolos directamente a través de Home Assistant, evitando Google Home, y verificando la interferencia entre canales Wi-Fi y Thread. Esto proporciona una guía práctica de solución de problemas para un problema común con dispositivos Matter, que aún están madurando. Destaca la importancia de la configuración de red para la fiabilidad de Matter sobre Thread. El usuario recomendó eliminar todos los dispositivos de Google Home y Home Assistant, luego añadirlos uno por uno directamente a través de Home Assistant. También enfatizó verificar el número de canal Thread en /config/thread de Home Assistant y compararlo con el canal Wi-Fi para evitar interferencias.

reddit · r/homeassistant · /u/Acceptable_Record100 · jun 7, 08:54

**Contexto**: Matter es un estándar abierto para el hogar inteligente que utiliza Thread para dispositivos de bajo consumo. Un enrutador de borde Thread, como el Google Nest Hub Max, conecta la red Thread a Wi-Fi o Ethernet. La superposición de canales entre Wi-Fi y Thread puede causar problemas de conectividad, por lo que la configuración de canales es importante.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/Thread_border_router">Thread border router</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matter_(standard)">Matter (standard) - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#integración`, `#Matter`, `#IKEA`, `#Thread`, `#Home Assistant`

---

