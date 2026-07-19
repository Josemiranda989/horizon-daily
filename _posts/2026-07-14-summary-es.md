---
layout: default
title: "Horizon Summary: 2026-07-14 (ES)"
date: 2026-07-14
lang: es
---

> De 31 artículos, 22 fueron seleccionados por relevancia

---

1. [JetBrains abre el código de YouTrackDB, su base de datos de grafos orientada a objetos.](#item-1) ⭐️ 8.0/10
2. [Apple demanda a OpenAI por robo de secretos comerciales por exempleado](#item-2) ⭐️ 8.0/10
3. [Estados demandan para bloquear fusión Paramount/WBD aprobada por Trump](#item-3) ⭐️ 8.0/10
4. [SRM-LoRA: Reducción de alucinaciones en LLMs con geometría sub-riemanniana](#item-4) ⭐️ 8.0/10
5. [CoT como trampa de escalado; el razonamiento latente surge con Coconut, HRM, RecursiveMAS.](#item-5) ⭐️ 8.0/10
6. [GPUHedge: La cobertura de proveedores de GPU serverless mejora la latencia p95 de inicio en frío de 117s a 30s (P)](#item-6) ⭐️ 8.0/10
7. [Herramienta open-source Research Radar filtra artículos de arXiv por relevancia personal](#item-7) ⭐️ 8.0/10
8. [Los comercializadores de energía australianos deben proporcionar tres horas de electricidad gratuita durante el día](#item-8) ⭐️ 7.0/10
9. [Comando Git History para Navegación de Commits](#item-9) ⭐️ 7.0/10
10. [Construir y publicar apps de Mac e iOS sin abrir Xcode](#item-10) ⭐️ 7.0/10
11. [Discusión sobre libro clásico inalámbrico destaca enfoque en MIMO](#item-11) ⭐️ 7.0/10
12. [DOOMQL: Un juego similar a Doom que usa SQLite como motor de juego](#item-12) ⭐️ 7.0/10
13. [CISA advierte que hackers rusos atacan routers](#item-13) ⭐️ 7.0/10
14. [Industria preocupada por disponibilidad de Crew Dragon en los 2030s](#item-14) ⭐️ 7.0/10
15. [Defensores usan inyección de prompts como defensa con 'context bombing'](#item-15) ⭐️ 7.0/10
16. [Recordatorio AMA: CTO de Mozilla sobre IA de código abierto](#item-16) ⭐️ 7.0/10
17. [Japón desarrolla método para recuperar 90% de litio de baterías usadas de VE](#item-17) ⭐️ 6.0/10
18. [Uso de uvx en GitHub Actions con caché eficiente](#item-18) ⭐️ 6.0/10
19. [Gráfico de Datasette muestra que agentes de IA aumentan la productividad](#item-19) ⭐️ 6.0/10
20. [SpaceX se alista para el vuelo de prueba 13 de Starship](#item-20) ⭐️ 6.0/10
21. [California otorga reembolso de $3,500 para autos eléctricos nuevos](#item-21) ⭐️ 6.0/10
22. [Apple y Samsung se benefician de escasez de memoria que reduce envíos a mínimos](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [JetBrains abre el código de YouTrackDB, su base de datos de grafos orientada a objetos.](https://github.com/JetBrains/youtrackdb) ⭐️ 8.0/10

JetBrains ha abierto el código de YouTrackDB, una base de datos orientada a grafos de propósito general que soporta consultas Gremlin y transacciones ACID. El código fuente está ahora disponible en GitHub. Este movimiento hace que la base de datos de grafos interna de JetBrains esté disponible públicamente, ofreciendo a los desarrolladores una nueva opción para manejar datos altamente conectados. También fortalece el ecosistema de bases de datos de grafos de código abierto y podría ser de interés para equipos que usan YouTrack o buscan una solución de grafos basada en Java. YouTrackDB está escrito en Java y utiliza un formato de almacenamiento nativo optimizado para relaciones de grafos. Soporta el lenguaje de consultas Gremlin y transacciones ACID, y ha sido la base de datos detrás de la herramienta de gestión de proyectos YouTrack de JetBrains.

hackernews · gjvc · jul 14, 03:39 · [Discusión](https://news.ycombinator.com/item?id=48902026)

**Contexto**: Las bases de datos de grafos almacenan datos como nodos, aristas y propiedades, lo que las hace adecuadas para relaciones complejas. YouTrackDB es una variante orientada a objetos, lo que significa que puede almacenar objetos directamente, alineándose con los paradigmas de programación orientada a objetos. JetBrains usaba YouTrackDB internamente para su sistema de seguimiento de incidencias YouTrack, y ahora se ha abierto para un uso más amplio.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/JetBrains/youtrackdb">GitHub - JetBrains/youtrackdb: YouTrackDB is a general-use object-oriented graph database with storage format native to handle graph relations. YouTrackDB supports Gremlin queries and ACID transactions. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/YouTrack">YouTrack</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad expresaron sorpresa de que la base de datos esté escrita en Java en lugar de Kotlin. Otros se preguntaron cuándo son realmente beneficiosas las bases de datos de grafos frente a SQL, y si opciones existentes como Neo4j eran insuficientes para las necesidades de JetBrains. Algunos usuarios notaron la presencia de definiciones de agentes Claude en el repositorio.

**Etiquetas**: `#base de datos grafos`, `#JetBrains`, `#código abierto`, `#YouTrack`, `#Java`

---

<a id="item-2"></a>
## [Apple demanda a OpenAI por robo de secretos comerciales por exempleado](https://arstechnica.com/tech-policy/2026/07/apple-sues-openai-after-ex-engineer-allegedly-used-bug-to-steal-trade-secrets/) ⭐️ 8.0/10

Apple ha presentado una demanda contra OpenAI, alegando que un exempleado de Apple conspiró con OpenAI para robar secretos comerciales explotando una vulnerabilidad. Esta demanda resalta la intensa competencia y las tensiones legales en la industria de la IA, ya que las empresas protegen ferozmente su propiedad intelectual. El caso podría sentar un precedente sobre cómo se manejan las disputas de secretos comerciales entre grandes empresas tecnológicas. La demanda acusa a OpenAI de conspirar con el exempleado, quien supuestamente utilizó una vulnerabilidad para acceder y robar secretos comerciales confidenciales de Apple. La vulnerabilidad específica y la naturaleza de los secretos robados no han sido reveladas.

rss · Ars Technica · jul 13, 19:17

**Contexto**: Los secretos comerciales son información empresarial confidencial que proporciona una ventaja competitiva, como algoritmos propietarios o planos de productos. Apple y OpenAI son líderes en tecnología, con Apple enfocándose en hardware e integración de IA, mientras que OpenAI es una organización prominente de investigación en IA. La demanda subraya los riesgos de la movilidad de empleados entre empresas rivales.

**Etiquetas**: `#Apple`, `#OpenAI`, `#demanda`, `#secretos comerciales`, `#espionaje industrial`

---

<a id="item-3"></a>
## [Estados demandan para bloquear fusión Paramount/WBD aprobada por Trump](https://arstechnica.com/tech-policy/2026/07/states-sue-to-block-paramount-wbd-merger-that-was-approved-by-trump-admin/) ⭐️ 8.0/10

Varios estados de EE.UU. presentaron una demanda para bloquear la fusión de Paramount Global y Warner Bros. Discovery, alegando que el acuerdo, aprobado por la administración Trump, generaría precios más altos, menor calidad y menos contenido para los consumidores. Esta acción antimonopolio podría reconfigurar el panorama mediático al impedir la consolidación de dos grandes conglomerados de entretenimiento, preservando potencialmente la competencia y la elección del consumidor. La demanda fue presentada por una coalición de fiscales generales estatales, citando preocupaciones sobre el dominio del mercado y la reducción de la competencia en la producción de cine y televisión.

rss · Ars Technica · jul 13, 18:34

**Contexto**: La fusión entre Paramount Global y Warner Bros. Discovery fue aprobada por la administración Trump a pesar de las preocupaciones antimonopolio. Ahora, los fiscales generales estatales impugnan el acuerdo, argumentando que perjudicará a los consumidores. Este caso resalta las tensiones continuas entre los reguladores federales y estatales sobre la consolidación de medios.

**Etiquetas**: `#Fusión`, `#Antimonopolio`, `#Entretenimiento`, `#Política`, `#Paramount`

---

<a id="item-4"></a>
## [SRM-LoRA: Reducción de alucinaciones en LLMs con geometría sub-riemanniana](https://www.reddit.com/r/MachineLearning/comments/1uw4j6a/llm_hallucination_paperusing_math_accepted_to/) ⭐️ 8.0/10

Un nuevo método llamado SRM-LoRA, que utiliza geometría sub-riemanniana para reducir las alucinaciones en modelos de lenguaje grandes, ha sido aceptado en un workshop de ICML. Este trabajo demuestra un enfoque matemático novedoso para un problema apremiante en IA, mejorando potencialmente la confiabilidad de los LLMs. SRM-LoRA construye una métrica riemanniana basada en sensibilidad que reforma los gradientes hacia atrás en el espacio de parámetros de LoRA, suprimiendo direcciones de actualización costosas mientras mantiene la inferencia sin cambios.

reddit · r/MachineLearning · /u/Round_Apple2573 · jul 14, 10:13

**Contexto**: La adaptación de bajo rango (LoRA) es un método de ajuste fino eficiente en parámetros que congela los pesos preentrenados e inyecta matrices entrenables de bajo rango, reduciendo el costo computacional. La geometría sub-riemanniana generaliza la geometría riemanniana restringiendo las direcciones permitidas, lo que aquí se usa para guiar las actualizaciones de gradiente lejos de caminos propensos a alucinaciones.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sub-Riemannian_geometry">Sub-Riemannian geometry</a></li>
<li><a href="https://arxiv.org/abs/2106.09685">LoRA: Low-Rank Adaptation of Large Language Models</a></li>

</ul>
</details>

**Etiquetas**: `#alucinaciones en LLM`, `#fine-tuning eficiente`, `#LoRA`, `#geometría riemanniana`, `#ICML workshop`

---

<a id="item-5"></a>
## [CoT como trampa de escalado; el razonamiento latente surge con Coconut, HRM, RecursiveMAS.](https://www.reddit.com/r/MachineLearning/comments/1uviru5/chain_of_thought_is_a_scaling_trap_the_next_wave/) ⭐️ 8.0/10

Una publicación de Reddit argumenta provocativamente que el razonamiento de Cadena de Pensamiento es una trampa de escalado debido a problemas de fidelidad y costo, y señala enfoques de razonamiento latente como Coconut, HRM y RecursiveMAS como la próxima frontera. La discusión también destaca a BDH (Dragon Hatchling) como un modelo que integra recurrencia latente con modelado de lenguaje. Este cambio podría reducir el uso de tokens y la latencia al evitar texto intermedio verbose, pero también introduce una 'pared de caja negra' que complica la auditoría y seguridad en aplicaciones de alto riesgo. El debate influye en cómo se diseñarán los futuros LLMs para tareas de razonamiento, equilibrando eficiencia e interpretabilidad. Coconut omite la cabeza de lenguaje alimentando directamente el estado oculto final como un pensamiento continuo. HRM utiliza una arquitectura recurrente de dos escalas temporales con módulos lentos de alto nivel y rápidos de bajo nivel. RecursiveMAS trata a los agentes como capas en un grafo computacional recursivo, pasando incrustaciones latentes en lugar de texto. BDH reportó una precisión top-1 del 97.4% en Sudoku Extreme sin CoT.

reddit · r/MachineLearning · /u/meowsterpieces · jul 13, 17:50

**Contexto**: La Cadena de Pensamiento (CoT) hace que los LLMs generen texto de razonamiento paso a paso, lo que mejora el rendimiento pero puede ser infiel y costoso debido a la generación autorregresiva de tokens. Los métodos de razonamiento latente como Coconut (Chain of Continuous Thought) mantienen el estado interno del modelo en un espacio latente continuo, generando lenguaje solo al final, permitiendo un cómputo más eficiente y una búsqueda implícita. Sin embargo, este proceso opaco genera preocupaciones sobre la auditabilidad y la confianza en dominios de alto riesgo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06769">Training Large Language Models to Reason in a Continuous ...</a></li>
<li><a href="https://arxiv.org/abs/2506.21734">[2506.21734] Hierarchical Reasoning Model</a></li>
<li><a href="https://arxiv.org/html/2604.25917v1">Recursive Multi-Agent Systems</a></li>

</ul>
</details>

**Etiquetas**: `#razonamiento en modelos de lenguaje`, `#cadena de pensamiento`, `#razonamiento latente`, `#escalado de LLMs`, `#técnicas de razonamiento`

---

<a id="item-6"></a>
## [GPUHedge: La cobertura de proveedores de GPU serverless mejora la latencia p95 de inicio en frío de 117s a 30s (P)](https://www.reddit.com/r/MachineLearning/comments/1uvlb6h/gpuhedge_hedging_serverless_gpu_providers/) ⭐️ 8.0/10

Técnica de ejecución especulativa entre proveedores de GPU serverless reduce la latencia p95 de 117s a 30s.

reddit · r/MachineLearning · /u/Putrid_Construction3 · jul 13, 19:20

**Etiquetas**: `#GPU serverless`, `#inferencia`, `#latencia`, `#cold start`, `#ejecución especulativa`

---

<a id="item-7"></a>
## [Herramienta open-source Research Radar filtra artículos de arXiv por relevancia personal](https://www.reddit.com/r/MachineLearning/comments/1uvcdf7/hundreds_of_papers_hit_arxiv_every_day_and_maybe/) ⭐️ 8.0/10

Research Radar es una herramienta de código abierto que puntúa automáticamente artículos de arXiv según los intereses de investigación del usuario y entrega un resumen diario de los más relevantes. Esta herramienta ahorra tiempo a los investigadores al filtrar la abrumadora cantidad diaria de artículos de arXiv para mostrar solo aquellos que coinciden con su enfoque de investigación, haciendo la revisión de literatura más eficiente. La herramienta utiliza un sistema de puntuación de dos fases: un modelo económico para una evaluación inicial y un modelo más potente para la lectura profunda de los mejores artículos. Es independiente del modelo, compatible con varios backends, incluyendo local mediante Ollama/vLLM.

reddit · r/MachineLearning · /u/usedtobreath · jul 13, 13:59

**Contexto**: arXiv es un repositorio gratuito de acceso abierto con más de 2.4 millones de artículos académicos en campos como física, informática y matemáticas. Publica miles de artículos nuevos cada día, lo que dificulta que los investigadores se mantengan al día con los trabajos relevantes. Research Radar automatiza el proceso de filtrado para ayudar a los investigadores a centrarse en los artículos que les interesan.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">ArXiv</a></li>
<li><a href="https://arxiv.org/">arXiv.org e-Print archive</a></li>

</ul>
</details>

**Etiquetas**: `#arXiv`, `#búsqueda bibliográfica`, `#código abierto`, `#PLN`, `#investigación`

---

<a id="item-8"></a>
## [Los comercializadores de energía australianos deben proporcionar tres horas de electricidad gratuita durante el día](https://lenergy.com.au/free-daytime-electricity-is-coming-heres-how-it-actually-works/) ⭐️ 7.0/10

Los grandes comercializadores de electricidad en Australia deberán ofrecer planes con tres horas de electricidad gratuita al día a partir de julio de 2026.

hackernews · i2oc · jul 14, 04:31 · [Discusión](https://news.ycombinator.com/item?id=48902320)

**Etiquetas**: `#energía`, `#Australia`, `#política`, `#red eléctrica`, `#baterías`

---

<a id="item-9"></a>
## [Comando Git History para Navegación de Commits](https://lalitm.com/post/git-history/) ⭐️ 7.0/10

Un artículo de blog discute el comando `git history`, que ofrece una forma alternativa de navegar y manipular el historial de commits, posiblemente como un alias o envoltorio de comandos estándar de Git. Comprender el historial de commits es fundamental para un control de versiones efectivo, y este comando podría simplificar los flujos de trabajo de los desarrolladores, especialmente al combinarse con las perspectivas de la comunidad sobre los internals de Git y las mejores prácticas. El comando `git history` no es un comando incorporado estándar de Git, sino probablemente un alias o script que agrega vistas comunes del historial. Miembros de la comunidad señalaron preocupaciones sobre el firmado de commits y la seguridad de las operaciones de rebase, con las cuales el comando puede interactuar.

hackernews · turbocon · jul 14, 00:57 · [Discusión](https://news.ycombinator.com/item?id=48901010)

**Contexto**: Git ofrece varias formas de ver el historial de commits, principalmente `git log` para una lista detallada y `git reflog` para un registro local de los movimientos de HEAD. El comando `git history` parece consolidar estos o proporcionar una interfaz personalizada, reflejando un deseo común de una navegación más intuitiva del historial.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History">Git - Viewing the Commit History</a></li>
<li><a href="https://www.warp.dev/terminus/git-commit-history">View Commit History - git log, git reflog, and git show | Warp</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad elogiaron el libro Pro Git por construir un modelo mental de los internals de Git, facilitando la curva de aprendizaje. Otros compartieron consejos para usar rebase de forma segura mediante `--abort` o etiquetas, mientras que algunos destacaron la incapacidad de los comandos `git history` para firmar commits modificados, una limitación para ciertos flujos de trabajo.

**Etiquetas**: `#git`, `#comandos de git`, `#historial de commits`, `#flujo de trabajo`, `#control de versiones`

---

<a id="item-10"></a>
## [Construir y publicar apps de Mac e iOS sin abrir Xcode](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 7.0/10

El artículo demuestra cómo compilar, firmar, notarizar y distribuir aplicaciones de Mac e iOS completamente desde la línea de comandos usando xcodebuild y otras herramientas, sin abrir Xcode nunca. Este enfoque agiliza los flujos de trabajo de desarrollo y abre posibilidades de automatización, permitiendo a los desarrolladores integrar compilaciones de plataformas Apple en tuberías de integración continua y usar agentes de codificación de IA de manera más efectiva. El método se basa en las herramientas de línea de comandos de Apple como xcodebuild y notarytool, y puede mejorarse con utilidades de terceros como xtool (para Linux) y el proyecto de código abierto Axiom. Sin embargo, requiere ejecutar el agente de codificación en el Mac del desarrollador, lo que puede exponer datos sensibles.

hackernews · speckx · jul 13, 18:22 · [Discusión](https://news.ycombinator.com/item?id=48896665)

**Contexto**: Xcode es el entorno de desarrollo integrado de Apple para crear aplicaciones para Mac, iPhone, iPad y otras plataformas Apple. Incluye un conjunto de herramientas de línea de comandos que pueden realizar compilaciones sin la interfaz gráfica, pero la mayoría de desarrolladores confían en el IDE completo. Automatizar las compilaciones con estas herramientas permite tuberías de integración y entrega continua, y se está volviendo más popular con el auge de asistentes de codificación de IA que operan desde la terminal.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with ...</a></li>
<li><a href="https://fastlane.tools/">fastlane - App automation done right</a></li>

</ul>
</details>

**Discusión**: La discusión comunitaria destaca preocupaciones de seguridad sobre ejecutar agentes de codificación en la máquina de desarrollo (como señala @codazoda), con referencias al incidente de xAI de exposición de claves SSH. Otros usuarios comparten herramientas alternativas como xtool para Linux y el proyecto Axiom para mejorar la eficiencia de tokens. El sentimiento general es cautelosamente optimista pero con notables preocupaciones de privacidad.

**Etiquetas**: `#desarrollo iOS`, `#herramientas`, `#seguridad`, `#automatización`, `#alternativas a Xcode`

---

<a id="item-11"></a>
## [Discusión sobre libro clásico inalámbrico destaca enfoque en MIMO](https://web.stanford.edu/~dntse/wireless_book.html) ⭐️ 7.0/10

El libro de texto de 2005 'Fundamentals of Wireless Communication' de Tse y Viswanath se discute en línea, elogiado por su cobertura profunda de MIMO pero criticado por omitir conceptos de nivel inferior como OFDM. Esta discusión destaca cómo un texto fundamental puede moldear la educación en ingeniería, al tiempo que revela vacíos que requieren recursos complementarios. Los comentarios subrayan la evolución de las comunicaciones inalámbricas y la necesidad de planes de estudio actualizados. El comentarista bri3d señala que el libro dedica solo un capítulo corto a OFDM, mientras que el 'Digital Communications' de Proakis y Salehi y el 'Wireless Communications' de Goldsmith cubren esos temas en profundidad. Otro comentarista, JoeAltmaier, señala una falla en la adaptación de velocidad del 802.11 temprano que causó congestión severa.

hackernews · teleforce · jul 14, 02:10 · [Discusión](https://news.ycombinator.com/item?id=48901454)

**Contexto**: MIMO (múltiples entradas y múltiples salidas) es una tecnología de antenas que utiliza múltiples antenas tanto en el transmisor como en el receptor para mejorar las tasas de datos y la confiabilidad. El libro 'Fundamentals of Wireless Communication' fue uno de los primeros libros de texto en enfatizar MIMO, que luego se convirtió en una piedra angular de los sistemas 4G y 5G. Sin embargo, cubre OFDM (multiplexación por división de frecuencias ortogonales) solo brevemente, a pesar de que OFDM es crucial para las redes Wi-Fi y celulares modernas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MIMO">MIMO - Wikipedia</a></li>
<li><a href="https://www.rfpage.com/mimo-technology-in-wireless-communication/">MIMO Technology: How It Works, Massive MIMO, Beamforming, and ...</a></li>

</ul>
</details>

**Discusión**: El sentimiento general es un reconocimiento respetuoso del valor del libro, con críticas constructivas sobre su enfoque limitado. Los usuarios recomiendan textos complementarios y discuten problemas prácticos como las fallas en la adaptación de velocidad del 802.11 temprano. Una pregunta sobre la relevancia del libro en 2026 refleja el interés continuo en el conocimiento fundamental a pesar de los avances tecnológicos.

**Etiquetas**: `#comunicaciones inalámbricas`, `#MIMO`, `#libro de texto`, `#ingeniería`, `#redes`

---

<a id="item-12"></a>
## [DOOMQL: Un juego similar a Doom que usa SQLite como motor de juego](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 7.0/10

Peter Gostev creó DOOMQL, un shooter en primera persona similar a Doom donde SQLite maneja toda la lógica del juego, el renderizado y el estado, construido usando el modelo de IA GPT-5.6 Sol. El juego se ejecuta en una terminal e incluye un trazador de rayos completo implementado mediante una consulta SQL CTE recursiva. Este proyecto demuestra un uso innovador de SQLite como motor de juego completo, llevando los límites de lo que el SQL declarativo puede lograr. También muestra las capacidades avanzadas de generación de código de GPT-5.6 Sol, inspirando nuevas posibilidades en la intersección de bases de datos y videojuegos. El juego está implementado como un script de Python en la terminal que crea un archivo de base de datos SQLite, que puede explorarse con Datasette. Utiliza una sola consulta SQL masiva con una expresión de tabla común recursiva para realizar el trazado de rayos en cada fotograma.

rss · Simon Willison · jul 13, 22:34

**Contexto**: SQLite es un motor de base de datos relacional incrustado ampliamente utilizado que almacena datos en archivos simples. Los motores de juego normalmente manejan renderizado, física y lógica, pero DOOMQL los reemplaza por completo con consultas SQL y CTE recursivas, tratando la base de datos como el entorno central de simulación. GPT-5.6 Sol es un modelo reciente de OpenAI con capacidades mejoradas de codificación y razonamiento, utilizado aquí para generar todo el código del juego.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/petergpt/doomql">GitHub - petergpt/ doomql : A playable terminal FPS whose simulation...</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT‑5.6 Sol: a next-generation model - OpenAI</a></li>

</ul>
</details>

**Etiquetas**: `#juego`, `#SQLite`, `#inteligencia artificial`, `#generación de código`, `#demostración`

---

<a id="item-13"></a>
## [CISA advierte que hackers rusos atacan routers](https://arstechnica.com/security/2026/07/the-us-government-warns-that-russia-state-hackers-are-coming-after-your-router/) ⭐️ 7.0/10

CISA ha advertido que hackers patrocinados por el estado ruso están atacando routers domésticos y de oficina, instando a los usuarios a mantener la vigilancia ante posibles ataques que utilizan proxies residenciales. La vulneración de routers puede dar a los atacantes un punto de apoyo en las redes, permitiendo espionaje, robo de datos y actividades maliciosas adicionales, mientras que los proxies residenciales ocultan su origen. Los proxies residenciales enrutan el tráfico a través de IPs domésticas reales, haciendo que el tráfico malicioso parezca legítimo. La advertencia de CISA enfatiza actualizar el firmware, cambiar las credenciales predeterminadas y deshabilitar la administración remota.

rss · Ars Technica · jul 13, 21:03

**Contexto**: CISA (Agencia de Seguridad de Ciberseguridad e Infraestructura) es una agencia estadounidense responsable de la ciberseguridad. Los proxies residenciales son direcciones IP asignadas por los ISP a hogares reales, lo que los hace parecer usuarios legítimos. Los hackers patrocinados por el estado ruso, a menudo asociados con grupos APT, tienen un historial de atacar infraestructuras críticas. La advertencia surge en medio del mayor uso de proxies residenciales con fines maliciosos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cybersecurity_and_Infrastructure_Security_Agency">Cybersecurity and Infrastructure Security Agency - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Residential_proxy">Residential proxy</a></li>
<li><a href="https://cybernews.com/editorial/the-worlds-most-dangerous-state-sponsored-hacker-groups/">Most Dangerous State Sponsored Hacker Groups in 2021 | Cybernews</a></li>

</ul>
</details>

**Etiquetas**: `#ciberseguridad`, `#hackers rusos`, `#routers`, `#CISA`, `#advertencia gubernamental`

---

<a id="item-14"></a>
## [Industria preocupada por disponibilidad de Crew Dragon en los 2030s](https://arstechnica.com/space/2026/07/what-happens-if-crew-dragon-stops-flying-in-the-2030s/) ⭐️ 7.0/10

Funcionarios de la industria expresan su preocupación de que Estados Unidos carece de un vehículo de tripulación de respaldo al Crew Dragon de SpaceX para el transporte de astronautas en la década de 2030, calificando la situación como un 'desastre a punto de ocurrir'. Esto es importante porque las misiones tripuladas de la NASA podrían volverse completamente dependientes de una sola nave espacial, sin respaldo en caso de problemas técnicos o retrasos con Crew Dragon. El artículo señala que, a pesar del éxito del Programa de Tripulación Comercial, la falta de un segundo vehículo operativo de tripulación sigue siendo una vulnerabilidad significativa para los vuelos espaciales estadounidenses.

rss · Ars Technica · jul 13, 16:05

**Etiquetas**: `#Crew Dragon`, `#NASA`, `#vuelos espaciales`, `#transporte de tripulación`, `#dependencia`

---

<a id="item-15"></a>
## [Defensores usan inyección de prompts como defensa con 'context bombing'](https://arstechnica.com/security/2026/07/now-defenders-are-embracing-the-prompt-injection-too/) ⭐️ 7.0/10

Investigadores de seguridad han convertido la inyección de prompts en una técnica defensiva llamada 'context bombing', que engaña a agentes de IA maliciosos para que se apaguen por sí mismos. Esto convierte un vector de ataque bien conocido en una defensa proactiva, protegiendo potencialmente a los agentes autónomos de IA de ser secuestrados sin necesidad de intervención humana inmediata. Una 'context bomb' es un prompt cuidadosamente diseñado oculto en la salida del sistema que, al ser leído por un agente de IA malicioso, activa sus medidas de seguridad y hace que se detenga o falle en su tarea.

rss · Ars Technica · jul 13, 15:06

**Contexto**: La inyección de prompts es una vulnerabilidad de seguridad donde entradas maliciosas anulan el comportamiento previsto de un modelo de IA, a menudo eludiendo las salvaguardas. El 'context bombing' reutiliza esta técnica de forma defensiva: al incrustar una instrucción de apagado en un archivo o documento señuelo, los defensores pueden desactivar preventivamente agentes de IA adversarios que intenten acceder a ellos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://agentic.tracebit.com/context-bombs/">Context bombs : stopping AI attackers in their tracks | Tracebit Research</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection - OWASP Foundation</a></li>

</ul>
</details>

**Etiquetas**: `#seguridad informática`, `#IA`, `#ataques adversariales`, `#defensa`

---

<a id="item-16"></a>
## [Recordatorio AMA: CTO de Mozilla sobre IA de código abierto](https://www.reddit.com/r/MachineLearning/comments/1uw2do8/n_ama_reminder_raffi_krikorian_cto_mozilla/) ⭐️ 7.0/10

Raffi Krikorian, CTO de Mozilla, está realizando un AMA hoy para discutir el primer informe 'State of Open Source AI' de Mozilla. Los temas incluyen adopción empresarial, el costo real de los modelos 'gratuitos', confianza del desarrollador, modelos chinos de código abierto, infraestructura de IA agéntica y el futuro de la IA de código abierto. Este AMA brinda una oportunidad única para que la comunidad interactúe directamente con el liderazgo de Mozilla sobre temas críticos en IA de código abierto. Los conocimientos del informe y la discusión pueden influir en las estrategias empresariales y la confianza de los desarrolladores en los modelos de IA de código abierto. El AMA comenzó a la 1pm ET (10am PT, 6pm BST) y se proporcionó prueba de identidad a través de LinkedIn. El informe marca el primer 'State of Open Source AI' anual de Mozilla y cubre tendencias clave que afectan al ecosistema.

reddit · r/MachineLearning · /u/Benlus · jul 14, 08:08

**Contexto**: El informe 'State of Open Source AI' es el primer análisis de Mozilla sobre el panorama de la IA de código abierto, examinando adopción, costos, confianza y tecnologías emergentes como la IA agéntica. La IA agéntica se refiere a sistemas que pueden tomar acciones y decisiones de forma autónoma, lo que requiere infraestructura especializada. Los modelos chinos de IA de código abierto, como DeepSeek y Qwen, han estado ganando atención por su rendimiento competitivo y apertura, impactando la dinámica global de la IA.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/best-chinese-open-source-ai-models-june-2026/">Best Chinese Open-Source AI Models June 2026: Pangu, DeepSeek ...</a></li>
<li><a href="https://grokipedia.com/page/AI_Infrastructure_and_Agentic_Systems">AI Infrastructure and Agentic Systems</a></li>

</ul>
</details>

**Etiquetas**: `#IA de código abierto`, `#Mozilla`, `#AMA`, `#Machine Learning`, `#adopción empresarial`

---

<a id="item-17"></a>
## [Japón desarrolla método para recuperar 90% de litio de baterías usadas de VE](https://tech.supercarblondie.com/japan-recovers-up-to-90-of-lithium-from-used-ev-batteries/) ⭐️ 6.0/10

Investigadores japoneses del Instituto Nacional de Ciencia y Tecnología Industrial Avanzada (AIST) han desarrollado un método que recupera hasta el 90% del litio de baterías de vehículos eléctricos usadas mediante un proceso químico de disolución selectiva. Este avance podría reducir significativamente la dependencia de litio recién extraído y disminuir el impacto ambiental de la producción de baterías, abordando un cuello de botella crítico a medida que la adopción de vehículos eléctricos se acelera a nivel mundial. El método logra tasas de recuperación muy superiores a los métodos de reciclaje convencionales, que a menudo recuperan menos del 50% del litio. Se espera que el proceso se comercialice en 2026.

hackernews · donohoe · jul 14, 02:27 · [Discusión](https://news.ycombinator.com/item?id=48901569)

**Contexto**: Las baterías de iones de litio contienen metales valiosos como litio, cobalto y níquel. Los métodos de reciclaje actuales, como la pirometalurgia (fundición) y la hidrometalurgia (lixiviación ácida), consumen mucha energía y a menudo son ineficientes para la recuperación de litio. Los métodos de reciclaje directo buscan recuperar materiales con menos energía y productos químicos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/japan-lithium-ev-battery-recycling-90-percent-2026">Japan 90% Lithium EV Battery Recycling 2026 | explainx.ai ...</a></li>
<li><a href="https://rottenpanda.com/science-nature/japan-develops-a-method-to-recover-up-to-90-of-lithium-from-used-ev-batteries/">Japan develops a method to recover up to 90% of lithium from ...</a></li>
<li><a href="https://www.vespernews.com/en/articles/tech/83f23960-3701-40c5-969b-8840389a7bc8">Lithium recycling: how Japan recovers 90% of it from used EV ...</a></li>

</ul>
</details>

**Discusión**: La discusión en Hacker News critica el artículo original por carecer de detalles técnicos, como el nombre de la institución de investigación o los científicos. Algunos comentaristas señalan que las altas tasas de recuperación de litio no son sorprendentes dada la fuente de alta pureza, y el desafío clave es la viabilidad económica. Otros enlazan a artículos más detallados y sugieren que se necesitan incentivos políticos para escalar el reciclaje.

**Etiquetas**: `#reciclaje de baterías`, `#litio`, `#vehículos eléctricos`, `#Japón`, `#sostenibilidad`

---

<a id="item-18"></a>
## [Uso de uvx en GitHub Actions con caché eficiente](https://simonwillison.net/2026/Jul/14/uvx-github-actions-cache/#atom-everything) ⭐️ 6.0/10

Simon Willison compartió una técnica para usar uvx en GitHub Actions de forma eficiente con caché, estableciendo la variable de entorno UV_EXCLUDE_NEWER a una fecha específica y usando esa fecha como parte de la clave de caché. Esto evita descargas repetidas de herramientas Python desde PyPI en cada ejecución del flujo de trabajo, acelerando significativamente los pipelines de CI y reduciendo costos de ancho de banda para desarrolladores que usan herramientas Python en GitHub Actions. El truco usa UV_EXCLUDE_NEWER con una fecha como '2026-07-12' y la incorpora en la clave de caché de GitHub Actions; cambiar la fecha posteriormente fuerza una actualización de caché y actualiza las herramientas.

rss · Simon Willison · jul 14, 00:56

**Contexto**: uvx es una herramienta de línea de comandos que ejecuta herramientas CLI de Python en entornos aislados temporales sin instalación permanente, a menudo usada en flujos de CI. En GitHub Actions, cada ejecución normalmente descarga copias nuevas de dependencias desde PyPI, lo cual es lento y desperdicia ancho de banda. Al establecer UV_EXCLUDE_NEWER, uvx solo considera versiones de paquetes publicadas antes de una fecha dada, permitiendo un caché estable.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/guides/tools/">Using tools | uv - Astral</a></li>
<li><a href="https://docs.astral.sh/uv/reference/environment/">Environment variables | uv - Astral</a></li>

</ul>
</details>

**Etiquetas**: `#GitHub Actions`, `#Python`, `#uvx`, `#caché`, `#optimización`

---

<a id="item-19"></a>
## [Gráfico de Datasette muestra que agentes de IA aumentan la productividad](https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything) ⭐️ 6.0/10

Simon Willison compartió un gráfico de frecuencia de código en GitHub de su proyecto Datasette, que revela un pico dramático en adiciones y eliminaciones de código en 2026 que se correlaciona con su uso de agentes de codificación y modelos de IA avanzados como Opus 4.5. Esto ilustra el impulso tangible de productividad que las herramientas de programación asistida por IA pueden proporcionar al desarrollo de código abierto, mostrando cómo la codificación agéntica puede acelerar la producción significativamente. El pico más grande muestra 37,022 adiciones y 9,528 eliminaciones en una sola semana de 2026, atribuido a modelos como Opus 4.8, GPT-5.5, Fable 5 y GPT-5.6 Sol. La actividad significativa anterior incluye un pico de 14,638 adiciones a finales de 2025 y un pico de eliminación de -10,658 a mediados de 2020.

rss · Simon Willison · jul 13, 21:45

**Contexto**: Datasette es una herramienta de código abierto de Simon Willison para explorar y publicar datos tabulares, construida sobre SQLite. Los 'modelos de clase Opus' se refieren a un nivel de modelos de IA avanzados capaces de realizar tareas complejas de razonamiento y codificación, como el Claude Opus de Anthropic. El gráfico rastrea cambios semanales de código en el repositorio de GitHub de Datasette desde 2018.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/">SpaceXAI releases Grok 4.5, which Elon describes as an ‘Opus ...</a></li>
<li><a href="https://www.wionews.com/technology/elon-musk-calls-grok-4-5-an-opus-class-ai-model-here-s-what-that-means-1783492275419">Elon Musk calls Grok 4.5 an 'Opus-class' AI model. Here's ...</a></li>

</ul>
</details>

**Etiquetas**: `#Datasette`, `#GitHub`, `#agentes de codificación`, `#productividad`, `#Opus 4.5`

---

<a id="item-20"></a>
## [SpaceX se alista para el vuelo de prueba 13 de Starship](https://arstechnica.com/space/2026/07/spacex-is-gearing-up-for-starships-13th-test-flight-later-this-week/) ⭐️ 6.0/10

SpaceX se prepara para el decimotercer vuelo de prueba de su vehículo Starship, que probará condiciones de mayor presión y desplegará nuevos satélites Starlink en órbita. Este vuelo de prueba avanza la capacidad de Starship para operar bajo mayor presión, un paso clave hacia misiones orbitales, y demuestra la capacidad de desplegar satélites Starlink operativos, expandiendo la constelación. El vuelo someterá a Starship a presiones internas más altas que las pruebas anteriores, probando los límites estructurales, e intentará desplegar satélites Starlink de nueva generación directamente desde la etapa superior.

rss · Ars Technica · jul 14, 01:17

**Contexto**: Starship es el vehículo de lanzamiento superpesado completamente reutilizable de SpaceX en desarrollo, diseñado para misiones a la Luna, Marte y más allá. Starlink es la constelación de satélites de internet de SpaceX que brinda cobertura de banda ancha global. Este vuelo de prueba continúa la campaña de pruebas iterativas tras vuelos anteriores que han demostrado capacidades crecientes.

**Etiquetas**: `#SpaceX`, `#Starship`, `#Starlink`, `#Pruebas espaciales`, `#Tecnología aeroespacial`

---

<a id="item-21"></a>
## [California otorga reembolso de $3,500 para autos eléctricos nuevos](https://arstechnica.com/cars/2026/07/first-time-ev-buyers-in-california-can-now-claim-a-new-rebate/) ⭐️ 6.0/10

California ha introducido un programa de reembolsos que ofrece hasta $3,500 para compradores de vehículos eléctricos nuevos y $1,750 para usados, ambos sujetos a límites de precio. Este reembolso reduce el costo inicial de los vehículos eléctricos, haciéndolos más accesibles para compradores primerizos y acelerando la transición hacia el transporte de cero emisiones en California. Los reembolsos tienen límites de precio, lo que significa que no todos los vehículos eléctricos son elegibles; el programa está dirigido específicamente a compradores primerizos de EVs que residan en California.

rss · Ars Technica · jul 13, 19:52

**Contexto**: Los vehículos eléctricos (EV) tienen costos iniciales más altos en comparación con los automóviles de gasolina, lo que puede ser una barrera para muchos consumidores. California ha establecido metas ambiciosas para eliminar gradualmente los vehículos de gasolina y reducir las emisiones de gases de efecto invernadero. Reembolsos como este están diseñados para incentivar la adopción de EVs y ayudar a cumplir los objetivos ambientales.

**Etiquetas**: `#Vehículos eléctricos`, `#Subvenciones`, `#California`, `#Medio ambiente`, `#Política ambiental`

---

<a id="item-22"></a>
## [Apple y Samsung se benefician de escasez de memoria que reduce envíos a mínimos](https://arstechnica.com/gadgets/2026/07/apple-and-samsung-benefit-as-memory-shortage-pushes-smartphone-shipments-to-historic-lows/) ⭐️ 6.0/10

Los envíos de smartphones han alcanzado mínimos históricos debido a una escasez global de memoria, pero los principales fabricantes Apple y Samsung han logrado mantener e incluso fortalecer sus posiciones en el mercado. Este desarrollo demuestra la creciente concentración del mercado en la industria de los smartphones, ya que los actores más grandes con cadenas de suministro robustas resisten mejor la escasez de componentes que los rivales más pequeños. A largo plazo, podría reducir la competencia y las opciones para los consumidores. La escasez afecta principalmente a los chips de memoria DRAM y NAND flash, esenciales para la producción de smartphones. El mínimo histórico en los envíos refleja tanto la crisis de componentes como los vientos económicos en contra, con datos que muestran que Apple y Samsung son los únicos vendedores de primer nivel que mantuvieron volúmenes de envío.

rss · Ars Technica · jul 13, 17:18

**Contexto**: La escasez global de semiconductores, que comenzó en 2020, ha afectado a múltiples industrias, incluida la electrónica de consumo. Los chips de memoria, como DRAM y NAND, son componentes fundamentales en los smartphones. Apple y Samsung tienen acuerdos de suministro a largo plazo y aprovechan su escala para asegurar asignaciones, lo que les da una ventaja sobre competidores más pequeños. Esto les ha permitido continuar la producción mientras otros enfrentan retrasos.

**Etiquetas**: `#escasez de memoria`, `#smartphones`, `#Apple`, `#Samsung`, `#industria tecnológica`

---