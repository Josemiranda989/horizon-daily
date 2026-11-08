---
layout: default
title: "Horizon Summary: 2026-11-08 (ES)"
date: 2026-11-08
lang: es
---

> De 12 artículos, 8 fueron seleccionados por relevancia

---

1. [Lo que ejecuto en mi homelab OpenStick de $10 USD](#item-1) ⭐️ 8.0/10
2. [La función 'No preguntar de nuevo' de Claude Code expone contraseñas en 1.122 archivos públicos](#item-2) ⭐️ 8.0/10
3. [Desarrollador pasa de Claude al harness de terminal Pi para programar con LLM](#item-3) ⭐️ 7.0/10
4. [Cómo expresar cualquier entero con cuatro doses (2025)](#item-4) ⭐️ 6.0/10
5. [Datasette deja de servir link rel=next a Firefox para evitar prefetch innecesario](#item-5) ⭐️ 6.0/10
6. [GRFNet: modelo PyTorch ligero para clasificación de series temporales multicanal](#item-6) ⭐️ 6.0/10
7. [Usuario de Reddit propone usar modelos de difusión para generar pesos de redes neuronales](#item-7) ⭐️ 5.0/10
8. [Modelo VLA entrenado localmente con codificador de visión de atención mínima](#item-8) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Lo que ejecuto en mi homelab OpenStick de $10 USD](https://blog.bosscher.ch/posts/openstick/) ⭐️ 8.0/10

El autor describe qué servicios puede alojar en un dispositivo OpenStick de 10 dólares, demostrando la viabilidad de self-hosting con hardware mínimo.

hackernews · LaurensBER · nov 7, 18:12 · [Discusión](https://news.ycombinator.com/item?id=50406670)

**Etiquetas**: `#self-hosting`, `#hardware barato`, `#homelab`, `#Linux embebido`, `#frugal computing`

---

<a id="item-2"></a>
## [La función 'No preguntar de nuevo' de Claude Code expone contraseñas en 1.122 archivos públicos](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 8.0/10

Apiiro halló 1.122 archivos públicos de GitHub con configuraciones locales de Claude Code que guardaban comandos aprobados con contraseñas y claves API en texto plano después de que los usuarios pulsaran "Sí, y no volver a preguntar". Esto pone de relieve cómo los agentes de codificación de IA pueden filtrar secretos sin querer cuando se suben archivos de configuración local al control de versiones, afectando a desarrolladores y organizaciones que usan Claude Code y exponiendo credenciales a cualquiera que escanee repositorios públicos. La exposición proviene de archivos .claude/settings.local.json creados y subidos manualmente; Claude Code los añade automáticamente a .gitignore cuando los crea él. Los 1.122 archivos contenían secretos como contraseñas directamente en los comandos aprobados, y Anthropic está estudiando cómo prevenirlo, aunque históricamente ha dejado el borrado de secretos a herramientas específicas.

hackernews · shmulc · nov 7, 20:45 · [Discusión](https://news.ycombinator.com/item?id=50407882)

**Contexto**: Claude Code es el agente de codificación de IA basado en terminal de Anthropic. Cuando un usuario aprueba un comando y elige "Sí, y no volver a preguntar", ese comando se guarda en un archivo de configuración del proyecto (.claude/settings.local.json) para que no se vuelva a preguntar. Este archivo está pensado para permanecer local y se añade automáticamente a .gitignore cuando Claude Code lo crea, pero los usuarios pueden crearlo o subirlo manualmente, publicando sin querer cualquier secreto incrustado en los comandos guardados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html">Claude Code's “Don't Ask Again” File Exposes Passwords and ...</a></li>
<li><a href="https://www.idlen.io/news/claude-code-dont-ask-again-passwords-github/">Claude Code “don’t ask again” leaked secrets on GitHub</a></li>
<li><a href="https://madrobot.blog/2026/11/07/claude-code-dont-ask-again-secrets-github/">Claude Code “Don’t ask again” left secrets in 1,122 GitHub files</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad muestran reacciones encontradas: algunos señalan que el titular es engañoso porque la exposición requiere que los usuarios suban un archivo de configuración local que normalmente está en .gitignore, mientras que otros expresan una paranoia más amplia sobre el acceso de los agentes de IA y sugieren usar máquinas virtuales efímeras o repositorios privados de desarrollo para limitar el riesgo. Un miembro del equipo de Claude Code reconoció el problema y dijo que están investigando medidas preventivas, señalando que el borrado de secretos históricamente se ha dejado a herramientas externas.

**Etiquetas**: `#seguridad`, `#inteligencia artificial`, `#desarrollo de software`, `#fuga de secretos`, `#Claude Code`

---

<a id="item-3"></a>
## [Desarrollador pasa de Claude al harness de terminal Pi para programar con LLM](https://caleb.software/posts/claude-to-pi.html) ⭐️ 7.0/10

El autor del artículo describe su cambio de Claude de Anthropic a Pi, un harness de terminal personalizable para modelos de lenguaje de gran tamaño, y la publicación generó una discusión sustancial con 240 comentarios. Este cambio destaca una tendencia creciente entre desarrolladores de usar herramientas basadas en terminal que ofrecen mayor control y personalización sobre los flujos de trabajo con LLM, pasando de interfaces de chat directas a orquestar múltiples agentes y reducir interrupciones. Pi es un harness de codificación de terminal minimalista que admite extensiones, habilidades, plantillas de avisos y temas, y puede empaquetarse y compartirse mediante npm o git. Los comentarios de la comunidad señalan limitaciones como la falta de soporte integrado para subagentes y posibles violaciones de los Términos de Servicio al usarse con una suscripción de Anthropic.

hackernews · karagenit · nov 8, 03:11 · [Discusión](https://news.ycombinator.com/item?id=50410107)

**Contexto**: Pi es un agente de codificación basado en terminal que permite a los desarrolladores adaptar la herramienta a sus flujos de trabajo mediante extensiones, habilidades, plantillas de avisos y temas. Claude es un modelo de lenguaje de gran tamaño desarrollado por Anthropic, al que normalmente se accede a través de una interfaz de chat web o una API. Un harness de terminal proporciona un entorno de línea de comandos basado en texto para interactuar con modelos de lenguaje, ofreciendo un control más fino que las interfaces gráficas. Esta configuración atrae a desarrolladores que prefieren integrar la IA directamente en sus flujos de trabajo de desarrollo basados en terminal.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://pi-dev.nproxy.org/press-kit">Press Kit · Pi | A terminal -based coding agent</a></li>

</ul>
</details>

**Discusión**: La discusión es en general positiva, con usuarios elogiando el control total que ofrece Pi y la reducción de frustraciones, pero hay preocupaciones sobre posibles violaciones de los Términos de Servicio con la suscripción de Anthropic, la falta de soporte nativo para subagentes y algunos usuarios que prefieren interfaces gráficas para gestionar muchas sesiones. Un usuario señala que está considerando el harness de DeepSeek debido a la limitación de subagentes.

**Etiquetas**: `#Modelos de lenguaje`, `#Interfaz de terminal`, `#Inteligencia artificial`, `#Herramientas para desarrolladores`, `#Claude`

---

<a id="item-4"></a>
## [Cómo expresar cualquier entero con cuatro doses (2025)](https://eli.thegreenplace.net/2025/making-any-integer-with-four-2s/) ⭐️ 6.0/10

Un artículo de 2025 de Eli Bendersky presenta un método para expresar cualquier entero usando exactamente cuatro doses y operaciones matemáticas, lo que generó una discusión en Hacker News con 156 puntos y 38 comentarios. El artículo reaviva el interés por un clásico rompecabezas de matemáticas recreativas, ilustrando cómo la elección de reglas afecta la expresividad y generando debates en la comunidad de HN sobre notación matemática y variantes del problema. El hilo de HN señala que las raíces cuadradas usan implícitamente un 2 (como en raíz cúbica o cuarta), que la concatenación como 22 es arbitraria en base 10, y menciona un problema de entrevista de ITA Software que pide el menor entero no expresable con el dígito K usado N veces bajo operaciones básicas.

hackernews · germanrabbit · nov 7, 22:38 · [Discusión](https://news.ycombinator.com/item?id=50408713)

**Contexto**: El rompecabezas de los 'cuatro doses' es un reto de matemáticas recreativas donde se deben expresar enteros usando exactamente cuatro doses y operaciones permitidas como +, -, ×, ÷, exponenciación, factoriales, etc. Una técnica conocida con logaritmos y raíces cuadradas anidadas permite generar cualquier entero, pero los conjuntos de reglas estrictos suelen excluir esas operaciones. El artículo de 2025 presenta una construcción específica y la discusión en HN examina si se mantiene dentro del espíritu del rompecabezas.

**Discusión**: Los comentaristas debaten la legitimidad de las operaciones: algunos sostienen que las raíces cuadradas usan implícitamente un 2, otros dicen que la concatenación como 22 es arbitraria en base 10, y uno menciona un problema de entrevista de ITA Software sobre enteros no expresables bajo operaciones restringidas. En general, el hilo muestra gran interés pero desacuerdos sobre qué constituye una solución válida.

**Etiquetas**: `#matemáticas recreativas`, `#rompecabezas matemático`, `#álgebra`, `#hackernews`, `#curiosidades`

---

<a id="item-5"></a>
## [Datasette deja de servir link rel=next a Firefox para evitar prefetch innecesario](https://simonwillison.net/2026/Nov/7/link-rel-next/) ⭐️ 6.0/10

Simon Willison descubrió que las páginas de tabla de Datasette provocaban que Firefox precargara la página siguiente mediante un encabezado HTTP link rel=next, y abrió la incidencia #3046 para dejar de servir ese encabezado en páginas HTML. Esto elimina carga innecesaria en el servidor y consumo de ancho de banda, ya que solo una pequeña fracción de usuarios hace clic en siguiente; pone de relieve un comportamiento de navegador de larga data que puede perjudicar el rendimiento web. Firefox tiene un error abierto (Bugzilla #175418) sobre este comportamiento de precarga desde hace más de 24 años, y Willison había escrito al respecto en 2002; la solución es no emitir encabezados link rel=next en las respuestas de páginas HTML de Datasette.

rss · Simon Willison · nov 7, 23:57

**Contexto**: Datasette es una herramienta de código abierto para publicar datos como un sitio web interactivo. Los encabezados HTTP Link con rel='next' indican paginación, y los navegadores pueden usarlos para precargar la siguiente página y mejorar la velocidad percibida. La precarga provoca carga adicional en el servidor y consumo de ancho de banda cuando la página precargada no se visualiza realmente.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Link">Link header - HTTP | MDN - MDN Web Docs</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/prefetch">rel=" prefetch " HTML attribute value - HTML | MDN</a></li>
<li><a href="https://web.dev/articles/codelab-two-ways-to-prefetch">Two ways to prefetch : tags and HTTP headers | Articles | web.dev</a></li>

</ul>
</details>

**Etiquetas**: `#Datasette`, `#HTTP`, `#Firefox`, `#rendimiento web`, `#prefetch`

---

<a id="item-6"></a>
## [GRFNet: modelo PyTorch ligero para clasificación de series temporales multicanal](https://www.reddit.com/r/MachineLearning/comments/1xqqj67/grfnet_pytorch_model_for_multichannel_timeseries/) ⭐️ 6.0/10

Un desarrollador presentó GRFNet, un modelo PyTorch de código abierto para clasificación de series temporales multicanal. Combina núcleos convolucionales aleatorios estilo ROCKET con filtros espaciales aprendidos, logrando solo 3.847 parámetros para una configuración de EEG de 22 canales y 4 clases. El modelo aborda desafíos clave del EEG, como conjuntos de datos pequeños y alta variabilidad entre sujetos, mediante una arquitectura de pocos parámetros que podría generalizar mejor. Su capacidad de adaptarse a cualquier longitud de entrada y frecuencia de muestreo podría hacerlo ampliamente útil para decodificación de EEG y otras tareas de series temporales multicanal. La arquitectura aprende filtros espaciales que mezclan los canales de entrada, opcionalmente inicializados a partir de las posiciones de los electrodos, y luego pasa los componentes por un banco de convoluciones dilatadas aleatorias en su mayoría congeladas con algunos núcleos aprendibles. Las estadísticas de resumen se combinan mediante una puerta aprendida y se clasifican por una cabeza pequeña; el autor planea una evaluación independiente del sujeto en PhysioNet EEGMMIDB y comparaciones con EEGNet y ShallowConvNet.

reddit · r/MachineLearning · /u/joekrry · nov 8, 05:13

**Contexto**: ROCKET es un método de clasificación de series temporales que utiliza un gran número de núcleos convolucionales aleatorios para extraer características, seguido de un clasificador lineal, ofreciendo alta precisión con bajo costo computacional. El EEG (electroencefalografía) registra la actividad eléctrica cerebral desde múltiples electrodos en el cuero cabelludo; el filtrado espacial combina las señales de los electrodos para aislar fuentes cerebrales y reducir ruido. Las convoluciones dilatadas aumentan el campo receptivo sin agregar parámetros al insertar espacios entre los elementos del núcleo. El modelo sigue la tendencia del aprendizaje profundo para decodificación de EEG, donde las líneas base comunes incluyen EEGNet y ShallowConvNet.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.13051">[1910.13051] ROCKET : Exceptionally fast and accurate time series ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dilated_convolution">Dilated convolution</a></li>
<li><a href="https://journals.physiology.org/doi/full/10.1152/jn.00560.2019">Local spatial analysis: an easy-to-use adaptive spatial EEG ...</a></li>

</ul>
</details>

**Etiquetas**: `#series temporales`, `#EEG`, `#PyTorch`, `#clasificación`, `#aprendizaje profundo`

---

<a id="item-7"></a>
## [Usuario de Reddit propone usar modelos de difusión para generar pesos de redes neuronales](https://www.reddit.com/r/MachineLearning/comments/1xqsl8d/what_if_diffusion_models_generates_neural_network/) ⭐️ 5.0/10

Un usuario de Reddit presentó una prueba de concepto que entrena un modelo de difusión para generar pesos de redes neuronales en lugar de imágenes, con el objetivo de crear redes a partir de descripciones en lenguaje natural como dibujar un hombre o jugar Pong. El experimento, construido con ZCode de Z.ai y el modelo GLM, está disponible en GitHub y ha alcanzado 3000 de 4000 pasos de entrenamiento en una CPU de portátil. Si tiene éxito, este enfoque podría permitir que la IA generativa produzca directamente redes neuronales funcionales para tareas específicas, evitando el entrenamiento convencional y expandiéndose más allá de la generación de imágenes o texto. Sin embargo, el concepto se superpone con investigaciones existentes sobre hiperredes y búsqueda de arquitecturas neuronales, y los resultados preliminares carecen de validación rigurosa. La prueba de concepto trata los pesos de la red neuronal como la distribución de datos objetivo para un proceso de difusión, en lugar de las intensidades de píxeles como en la generación de imágenes. El repositorio de GitHub del autor (github.com/vagrillo/nngen) incluye una aplicación web para pruebas, pero el entrenamiento está incompleto y solo se muestran los mejores resultados preliminares.

reddit · r/MachineLearning · /u/Specific-Tax-6700 · nov 8, 07:20

**Contexto**: Los modelos de difusión son modelos generativos que aprenden a revertir un proceso gradual de adición de ruido, lo que les permite producir nuevas muestras similares a los datos de entrenamiento; se utilizan ampliamente en la generación de imágenes (por ejemplo, Stable Diffusion, DALL-E). Los pesos de una red neuronal son parámetros numéricos que definen su comportamiento, y generarlos directamente evitaría el entrenamiento basado en gradientes. GLM se refiere a una serie de modelos de lenguaje grandes de código abierto de Z.ai, que el autor utilizó como asistente de codificación.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#modelos de difusión`, `#generación de pesos`, `#redes neuronales`, `#IA generativa`

---

<a id="item-8"></a>
## [Modelo VLA entrenado localmente con codificador de visión de atención mínima](https://www.reddit.com/r/MachineLearning/comments/1xqrtcz/locally_trained_vla_model_with_minimal_attention/) ⭐️ 5.0/10

Un usuario de Reddit compartió el progreso de un modelo de visión-lenguaje-acción (VLA) entrenado localmente que utiliza un codificador de visión basado en atención mínima, operando directamente sobre píxeles RGB crudos de 128x128. El modelo mantiene una matriz de estado recurrente de 768x768 y fue entrenado en una sola GPU RTX 3060 de 12 GB. Este proyecto demuestra que un modelo VLA puede entrenarse en una GPU de consumo sin un codificador de visión preentrenado, lo que podría hacer que estos modelos sean más accesibles para aficionados y laboratorios pequeños. También explora una alternativa a los codificadores de visión basados en transformers dominantes, lo que podría inspirar investigación en agentes multimodales ligeros. El número total de parámetros es de 25.561.354, de los cuales 12.976.128 están dedicados a un decodificador de salida de vocabulario heredado de 49.000 tokens; el modelo se entrenó inicialmente con datos de lenguaje y luego se ajustó para tareas VLA. Procesa entradas de resolución variable durante la inferencia y muestra valores de atención por píxel para la resolución de problemas, pero el autor no comparó la velocidad de arranque con un punto de control nuevo.

reddit · r/MachineLearning · /u/Sl0wJH1 · nov 8, 06:31

**Contexto**: Los modelos de visión-lenguaje-acción (VLA) son sistemas multimodales que combinan percepción visual, comprensión del lenguaje y generación de acciones; suelen construirse ajustando un modelo de visión-lenguaje sobre trayectorias de robots. Un codificador de visión basado en atención utiliza pesos de atención aprendidos para centrarse en las partes relevantes de una imagen, reemplazando a menudo un codificador convolucional o transformer preentrenado. Las redes neuronales recurrentes (RNN) mantienen un estado oculto que se actualiza en cada paso de tiempo, y los modelos de espacio de estados generalizan esta idea con estados matriciales. Este proyecto utiliza una gran matriz de estado recurrente con compuertas similares a LSTM por celda para procesar píxeles crudos y producir salidas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision-language-action_model">Vision-language-action model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recurrent_neural_network">Recurrent neural network - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision-language_model">Vision -language model - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#modelos VLA`, `#aprendizaje automático`, `#visión por computadora`, `#agentes autónomos`, `#atención visual`

---