# Horizon Diario - 2026-06-06

> De 14 artículos, 7 fueron seleccionados por relevancia

---

1. [La integración de DeepSeek V4 Flash en llama.cpp muestra gran potencial](#item-1) ⭐️ 8.0/10
2. [Usuario de GrapheneOS reportado a autoridades por usar el SO](#item-2) ⭐️ 7.0/10
3. [Buscando alternativas económicas a Backblaze para backups off-site](#item-3) ⭐️ 7.0/10
4. [Integración de Home Assistant facilita la limpieza de entidades huérfanas](#item-4) ⭐️ 7.0/10
5. [Comparación de los últimos modelos locales para GPUs 3×3090](#item-5) ⭐️ 6.0/10
6. [Fusión sin censura Qwen3.6-35B-A3B mejora codificación y razonamiento](#item-6) ⭐️ 6.0/10
7. [Reutilicé una pantalla táctil de señalización digital antigua como un enorme panel físico de Home Assistant, con una tarjeta Lovelace personalizada para cine en casa.](#item-7) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [La integración de DeepSeek V4 Flash en llama.cpp muestra gran potencial](https://www.reddit.com/r/LocalLLaMA/comments/1tyb3np/deepseek_v4_flash_is_amazing_wip_llamacpp_pr_24162/) ⭐️ 8.0/10

Una solicitud de incorporación de cambios en progreso (PR #24162) agrega soporte para el modelo DeepSeek V4 Flash de mezcla de expertos (MoE) a llama.cpp, permitiendo la inferencia local de un modelo de 284 mil millones de parámetros a velocidades lentas (5-6 tokens por segundo). Esta integración lleva la inteligencia de modelos de frontera al hardware local, comparable a los mejores modelos en la nube, lo que podría democratizar el acceso a modelos de lenguaje de última generación para investigadores y entusiastas. La cuantización híbrida nativa FP4-FP8 también reduce los requisitos de memoria, haciendo más factible la inferencia local de alto rendimiento. El PR se encuentra en etapas tempranas con soporte limitado de GPU y atención flash, y el modelo se ejecuta a 5-6 tokens por segundo actualmente. La arquitectura del modelo utiliza un diseño de mezcla de expertos (MoE) con 284 mil millones de parámetros totales, pero solo 13 mil millones activados por token, y admite una ventana de contexto de 1 millón de tokens.

reddit · r/LocalLLaMA · /u/Lowkey_LokiSN · jun 6, 07:56

**Contexto**: DeepSeek V4 Flash es un modelo de lenguaje de mezcla de expertos (MoE) desarrollado por DeepSeek con 284 mil millones de parámetros totales y 13 mil millones activados, optimizado para eficiencia. llama.cpp es una implementación de código abierto de inferencia de modelos de lenguaje en C/C++ que se ejecuta en CPU y GPU. La cuantización reduce el uso de memoria; la cuantización híbrida FP4-FP8 permite que el modelo se ejecute en hardware de consumo manteniendo la calidad.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://rcrtech.com/semiconductor-news/llms-quantization-fp8-fp4-int8/">LLMs and quantization: FP8, FP4, and INT8 explained</a></li>

</ul>
</details>

**Etiquetas**: `#DeepSeek V4 Flash`, `#llama.cpp`, `#inferencia local`, `#modelos de lenguaje`, `#cuantización`

---

<a id="item-2"></a>
## [Usuario de GrapheneOS reportado a autoridades por usar el SO](https://discuss.grapheneos.org/d/36134-grapheneos-user-reported-to-authorities-for-using-grapheneos) ⭐️ 7.0/10

Un usuario de GrapheneOS fue reportado a las autoridades del Reino Unido por Yoti, un servicio de verificación de identidad, únicamente por usar el sistema operativo móvil GrapheneOS, generando controversia sobre la elaboración de perfiles de privacidad. Este incidente resalta el estigma y la sospecha que rodean a las tecnologías centradas en la privacidad, lo que podría disuadir a los usuarios de adoptar herramientas que protejan sus datos. También genera preocupación sobre los sistemas automatizados de reporte que pueden marcar medidas de seguridad legítimas como sospechosas. El mensaje de Yoti indicaba que, debido a preocupaciones de seguridad pasadas, cualquier dispositivo que ejecute GrapheneOS se marca automáticamente y se reporta a las autoridades y a su equipo de seguridad. El usuario había realizado múltiples intentos de verificación, lo que también contribuyó al marcado.

hackernews · Cider9986 · jun 6, 08:43 · [Discusión](https://news.ycombinator.com/item?id=48422798)

**Contexto**: GrapheneOS es un sistema operativo móvil de código abierto basado en Android que se centra en mejoras de seguridad y privacidad. Está disponible para dispositivos Google Pixel y tiene alrededor de 400,000 usuarios activos. El sistema incluye características de hardening como un mejor sandboxing y controles de permisos, lo que puede dificultar que los servicios rastreen a los usuarios. Sin embargo, su asociación con la privacidad ha llevado a algunos servicios a tratarlo como sospechoso.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS : the private and secure mobile OS</a></li>

</ul>
</details>

**Discusión**: Los comentarios en el foro expresaron indignación y sarcasmo, señalando un usuario la tendencia del Reino Unido a criminalizar las prácticas de ciberseguridad. Otro comentarista analizó el mensaje de Yoti, sugiriendo que la parte 'reportado a las autoridades' podría ser una plantilla. Algunos compararon desfavorablemente la situación con China, donde usar cualquier sistema operativo no tiene tales consecuencias.

**Etiquetas**: `#privacidad`, `#seguridad`, `#GrapheneOS`, `#reporte`, `#sospecha`

---

<a id="item-3"></a>
## [Buscando alternativas económicas a Backblaze para backups off-site](https://www.reddit.com/r/selfhosted/comments/1tya8o4/currently_using_backblaze_for_backups_but_its/) ⭐️ 7.0/10

Un usuario en r/selfhosted pregunta por soluciones de backup fuera del sitio más asequibles, gastando actualmente unas £50 al mes en Backblaze para almacenar entre 3 y 4 TB de datos personales, incluyendo fotos familiares y documentos de la empresa. Esto resalta un problema común entre quienes hacen autoalojamiento: equilibrar la confiabilidad de las copias de seguridad con el costo, especialmente a medida que crecen los volúmenes de datos. La discusión ofrece estrategias del mundo real que pueden ayudar a otros a reducir gastos manteniendo la seguridad de los datos. El usuario utiliza TrueNAS en un HP Microserver con 4 discos de 6 TB y considera colocar un segundo Microserver en un garaje separado más una unidad USB en una caja fuerte ignífuga para mayor protección.

reddit · r/selfhosted · /u/CrappyTan69 · jun 6, 07:06

**Contexto**: Las copias de seguridad fuera del sitio son fundamentales para protegerse contra amenazas físicas como incendios, robos o fallos de hardware. Muchos autohosters utilizan servicios en la nube como Backblaze, pero los costos pueden dispararse con varios terabytes; las alternativas incluyen sincronización entre pares, servidores remotos autoalojados o configuraciones híbridas local/nube.

**Etiquetas**: `#backups`, `#almacenamiento`, `#autoalojamiento`, `#backups off-site`, `#ahorro de costos`

---

<a id="item-4"></a>
## [Integración de Home Assistant facilita la limpieza de entidades huérfanas](https://www.reddit.com/r/homeassistant/comments/1tya8f7/orphan_entity_cleaner/) ⭐️ 7.0/10

Una nueva integración personalizada llamada Orphan Entity Cleaner, creada por el usuario Franz646, permite a los usuarios de Home Assistant eliminar entidades huérfanas a través de una interfaz gráfica sencilla. La herramienta es instalable mediante HACS y ofrece múltiples opciones de limpieza. Las entidades huérfanas se acumulan con el tiempo a partir de dispositivos o integraciones eliminados, saturando el sistema y afectando potencialmente el rendimiento. Esta integración simplifica el proceso de limpieza, haciéndolo accesible para usuarios que no se sienten cómodos con la edición manual de la base de datos o la configuración YAML. Orphan Entity Cleaner escanea las entidades que ya no están activas y las presenta en una interfaz de usuario para su eliminación selectiva. Se distribuye como una integración personalizada y se puede agregar mediante HACS desde el repositorio de GitHub Franz646/orphan-cleaner.

reddit · r/homeassistant · /u/False-Assistance2111 · jun 6, 07:06

**Contexto**: En Home Assistant, una entidad representa un sensor, interruptor u otro componente. Cuando se elimina un dispositivo o integración, sus entidades asociadas pueden quedar huérfanas, permaneciendo en la base de datos y causando desorden. HACS (Home Assistant Community Store) es una herramienta popular para instalar integraciones personalizadas y elementos de interfaz.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://community.home-assistant.io/t/help-removing-orphans/936745">Help removing orphans - Home Assistant Community</a></li>
<li><a href="https://hacs.xyz/">HACS</a></li>

</ul>
</details>

**Etiquetas**: `#Home Assistant`, `#integración`, `#limpieza`, `#entidades huérfanas`, `#utilidad`

---

<a id="item-5"></a>
## [Comparación de los últimos modelos locales para GPUs 3×3090](https://www.reddit.com/r/LocalLLaMA/comments/1tya05j/aa_comparison_of_the_latest_local_models/) ⭐️ 6.0/10

Un usuario de Reddit publicó una comparación práctica de los modelos recientes de lenguaje grandes locales que pueden ejecutarse en tres GPUs NVIDIA RTX 3090, señalando que los modelos MiniMax y Step funcionan bien incluso con cuantización Q3. Esta comparación ayuda a la comunidad de LLM local a identificar qué modelos son viables en hardware de consumo, guiando a los usuarios en la elección de modelos que equilibren rendimiento y requisitos de recursos. El autor excluyó modelos de más de 300 mil millones de parámetros y sugirió omitir la mayoría de los modelos de 200B, pero destacó que los modelos MiniMax y Step son rápidos incluso con cuantización Q3. Gemma-4 12B no estaba incluido en la comparación.

reddit · r/LocalLLaMA · /u/jacek2023 · jun 6, 06:53

**Contexto**: Los modelos locales son modelos de lenguaje grandes que se pueden ejecutar en hardware personal en lugar de servidores en la nube. Las técnicas de cuantización como Q3 reducen la precisión del modelo para disminuir el uso de memoria, lo que permite ejecutar modelos más grandes en GPUs con VRAM limitada. La GPU NVIDIA RTX 3090 tiene 24GB de VRAM, y tres de esas GPUs pueden alojar modelos de hasta unos 200 mil millones de parámetros con cuantización.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.tipsblade.com/minimax-unveils-open-source-llm-with-staggering-4m-token-context/">MiniMax unveils open source LLM with staggering 4M token</a></li>
<li><a href="https://dat1.co/blog/llm-quantization-comparison">LLM Quantization Comparison</a></li>

</ul>
</details>

**Etiquetas**: `#modelos locales`, `#comparación`, `#LLM`, `#GPU`

---

<a id="item-6"></a>
## [Fusión sin censura Qwen3.6-35B-A3B mejora codificación y razonamiento](https://www.reddit.com/r/LocalLLaMA/comments/1tyb6u7/qwen3635ba3buncensoredclaude46genesisapexgguf/) ⭐️ 6.0/10

Se ha lanzado una fusión delta comunitaria de modelos Qwen, denominada Qwen3.6-35B-A3B-Uncensored-Claude-4.6-Genesis-APEX-GGUF, que ofrece mejor estabilidad para codificación, ausencia total de censura y razonamiento Claude 4.6 Opus. Utiliza cuantización APEX para inferencia local eficiente. Esta fusión demuestra la creciente capacidad de las fusiones comunitarias para mejorar modelos de lenguaje de código abierto, especialmente para inferencia local. Muestra cómo combinar distintas fortalezas puede crear herramientas versátiles para desarrolladores y usuarios de juegos de rol. El modelo se basa en una fusión delta de un lanzamiento anterior y requiere cuantización APEX. Funciona mejor con una primera línea específica en el prompt del sistema: 'You are Qwen, created by Alibaba Cloud. You are a helpful AI assistant.'

reddit · r/LocalLLaMA · /u/EvilEnginer · jun 6, 08:01

**Contexto**: La fusión de modelos es una técnica que combina diferentes checkpoints de modelos de lenguaje para aprovechar sus fortalezas respectivas. La fusión delta aplica solo la diferencia entre dos modelos, ahorrando almacenamiento y permitiendo un control más preciso. APEX (Precisión Adaptativa para Modelos de Expertos) es un método de cuantización diseñado para modelos Mixture-of-Experts (MoE), que logra mejor precisión que las cuantizaciones uniformes mientras reduce el tamaño del modelo. GGUF es un formato de archivo para inferencia eficiente en CPU de modelos cuantizados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://huggingface.co/collections/mudler/apex-quants-gguf">APEX Quants (GGUF) - a mudler Collection</a></li>
<li><a href="https://huggingface.co/mudler/Qwen3.5-35B-A3B-APEX-GGUF">mudler/Qwen3.5-35B-A3B-APEX-GGUF · Hugging Face</a></li>
<li><a href="https://github.com/mudler/apex-quant">GitHub - localai-org/apex-quant: Adaptive Precision for EXpert Models: MoE-aware mixed-precision quantization · GitHub</a></li>

</ul>
</details>

**Etiquetas**: `#modelos de lenguaje`, `#código abierto`, `#razonamiento`, `#local`, `#fusión`

---

<a id="item-7"></a>
## [Reutilicé una pantalla táctil de señalización digital antigua como un enorme panel físico de Home Assistant, con una tarjeta Lovelace personalizada para cine en casa.](https://www.reddit.com/r/homeassistant/comments/1tyd5xc/i_repurposed_an_old_digital_signage_touchscreen/) ⭐️ 6.0/10

Un usuario recicla una pantalla táctil de señalización digital para crear un panel de control de Home Assistant, incluyendo una tarjeta personalizada para el cine en casa.

reddit · r/homeassistant · /u/Nerdaxic · jun 6, 09:59

**Etiquetas**: `#Home Assistant`, `#Pantalla táctil`, `#Reciclaje`, `#Lovelace`, `#Domótica`

---

