---
layout: default
title: "Horizon Summary: 2026-07-08 (ES)"
date: 2026-07-08
lang: es
---

> De 34 artículos, 24 fueron seleccionados por relevancia

---

1. [GitLost: Engañando al agente de IA de GitHub para filtrar repos privados](#item-1) ⭐️ 9.0/10
2. [sqlite-utils 4.0 añade migraciones de esquemas de base de datos](#item-2) ⭐️ 9.0/10
3. [Construye un NAS minimalista con ZFS sin Synology ni TrueNAS (2024)](#item-3) ⭐️ 8.0/10
4. [Firmware de Tenda contiene puerta trasera de autenticación oculta](#item-4) ⭐️ 8.0/10
5. [MIT OCW Publica las Conferencias en Video de SICP de 1986](#item-5) ⭐️ 8.0/10
6. [Informe GAO: DOE excluye opciones más baratas de limpieza en Oak Ridge](#item-6) ⭐️ 8.0/10
7. [Kokoro TTS: texto a voz local de alta calidad y optimizado para CPU](#item-7) ⭐️ 8.0/10
8. [Estadísticas de LineageOS revelan 74% de instalaciones no oficiales, muchas en no teléfonos](#item-8) ⭐️ 8.0/10
9. [Hackers pueden usar 9 de las herramientas de IA más populares para montar botnets masivos](#item-9) ⭐️ 8.0/10
10. [La demanda energética de los centros de datos amenaza el plan de fabricación de Trump](#item-10) ⭐️ 8.0/10
11. [DeepSeek de China planea fabricar sus propios chips de IA](#item-11) ⭐️ 8.0/10
12. [Nuevo catálogo de virus identifica los patógenos de mayor amenaza pandémica](#item-12) ⭐️ 8.0/10
13. [TorchJD: Descenso jacobiano para múltiples pérdidas en PyTorch](#item-13) ⭐️ 8.0/10
14. [CTO de Mozilla realizará AMA sobre informe de IA de código abierto](#item-14) ⭐️ 8.0/10
15. [Descifran script bash ofuscado en camiseta de Uniqlo](#item-15) ⭐️ 7.0/10
16. [Propuestas Chat Control de la UE generan debate sobre privacidad](#item-16) ⭐️ 7.0/10
17. [El Tribunal Supremo permite a Texas imponer ley de verificación de edad en tiendas de aplicaciones](#item-17) ⭐️ 7.0/10
18. [Tesis doctoral sobre trazado de rayos diferenciable para propagación de radio](#item-18) ⭐️ 7.0/10
19. [Restringir el Fine-Tuning a un Subespacio de LoRA Confiable Evita el Envenenamiento](#item-19) ⭐️ 7.0/10
20. [30papers.com: Los 30 artículos esenciales de ML de Ilya Sutskever](#item-20) ⭐️ 6.0/10
21. [Componente web experimental incrusta código de GitHub mediante GPT-5.5](#item-21) ⭐️ 6.0/10
22. [Despidos de Microsoft golpean fuerte a Bethesda e id Software](#item-22) ⭐️ 6.0/10
23. [Coche de carreras fabricado con fibras vegetales, basalto y agua de mar](#item-23) ⭐️ 6.0/10
24. [Alineación inversa: ¿podrían los modelos 'malos' mostrar comportamiento 'bueno'?](#item-24) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GitLost: Engañando al agente de IA de GitHub para filtrar repos privados](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) ⭐️ 9.0/10

Investigadores demostraron un ataque de inyección de indicaciones que engañó al agente de IA de GitHub para filtrar el contenido de repositorios privados, evadiendo sus barreras de seguridad. Este ataque revela una vulnerabilidad sistémica crítica en los sistemas de IA agentiva, comparable a la inyección SQL, que podría provocar filtraciones de datos generalizadas si no se aborda. El ataque tuvo éxito al simplemente agregar la palabra 'Además' al indicador, lo que hizo que el modelo priorizara las instrucciones del usuario sobre las reglas del sistema, exponiendo la dificultad de imponer límites de seguridad dentro de la ventana de contexto de un LLM.

hackernews · ColinEberhardt · jul 8, 05:25 · [Discusión](https://news.ycombinator.com/item?id=48827858)

**Contexto**: La inyección de indicaciones es una vulnerabilidad de seguridad donde entradas cuidadosamente diseñadas anulan las instrucciones previstas de un modelo, similar a la inyección SQL en aplicaciones web. En este caso, al agente de IA se le había otorgado acceso a repositorios privados y luego se le pidió responder una pregunta en un repositorio público, lo que provocó que filtrara datos privados. El ataque resalta que los LLM están diseñados para seguir instrucciones, por lo que mezclar entradas del sistema y del usuario puede causar comportamientos no deseados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection - OWASP Foundation</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html">AI Agent Security - OWASP Cheat Sheet Series</a></li>

</ul>
</details>

**Discusión**: Los comentarios sobre el artículo muestran una mezcla de perspectivas: algunos comparan la inyección de indicaciones con la inyección SQL en gravedad, mientras que otros argumentan que la vulnerabilidad se debe a una mala configuración del usuario en lugar de un fallo en la IA de GitHub. Un comentario destaca que el modelo simplemente trataba de ser útil, y otro señala que los intentos de construir límites de seguridad sólidos dentro de la ventana de contexto de un LLM están destinados al fracaso.

**Etiquetas**: `#inyección de prompts`, `#seguridad en IA`, `#GitHub`, `#filtración de datos`, `#agentes de IA`

---

<a id="item-2"></a>
## [sqlite-utils 4.0 añade migraciones de esquemas de base de datos](https://simonwillison.net/2026/Jul/7/sqlite-utils/#atom-everything) ⭐️ 9.0/10

Se ha lanzado sqlite-utils 4.0, que introduce tres funcionalidades principales: migraciones de esquemas de base de datos, transacciones anidadas a través de un nuevo método `db.atomic()` y soporte para claves foráneas compuestas. Esta es la primera actualización de versión mayor desde la versión 3.0 de noviembre de 2020. Esta versión aborda una funcionalidad muy solicitada para gestionar cambios de esquema en SQLite, haciendo que sqlite-utils sea más potente para los desarrolladores que dependen de SQLite para bases de datos ligeras. La adición de transacciones anidadas y claves foráneas compuestas mejora aún más su utilidad para operaciones complejas de bases de datos. Las migraciones se definen en archivos Python utilizando la biblioteca Python de sqlite-utils y aprovechan el método `table.transform()` para capacidades mejoradas de alteración de tablas. El lanzamiento también incluye cambios importantes, detallados en una guía de actualización.

rss · Simon Willison · jul 7, 15:42

**Contexto**: sqlite-utils es una utilidad de línea de comandos y biblioteca Python para manipular bases de datos SQLite, que permite importar datos desde JSON/CSV/TSV y consultarlos. SQLite es un sistema de gestión de bases de datos relacional ligero basado en archivos. Las migraciones de esquemas permiten cambios versionados en la estructura de la base de datos, que SQLite maneja de forma nativa con limitaciones.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/">sqlite-utils</a></li>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library ...</a></li>

</ul>
</details>

**Etiquetas**: `#sqlite-utils`, `#SQLite`, `#migraciones de esquemas`, `#herramientas de base de datos`, `#lanzamiento`

---

<a id="item-3"></a>
## [Construye un NAS minimalista con ZFS sin Synology ni TrueNAS (2024)](https://neil.computer/notes/how-to-setup-minimal-zfs-nas-without-truenas/) ⭐️ 8.0/10

Un tutorial detallado describe cómo construir un NAS doméstico mínimo usando ZFS en Linux sin depender de soluciones comerciales como Synology, QNAP o TrueNAS, utilizando solo componentes básicos y herramientas de código abierto. Este enfoque brinda a los usuarios control total sobre su almacenamiento, reduce la dependencia de proveedores y puede ser más rentable para quienes se sienten cómodos con la línea de comandos de Linux. La configuración utiliza ZFS para integridad de datos y agrupación, Nix para la gestión del sistema y Docker Compose para ejecutar servicios como Samba. El tutorial enfatiza un enfoque minimalista y manual sin interfaz web.

hackernews · 4diii · jul 8, 03:59 · [Discusión](https://news.ycombinator.com/item?id=48827325)

**Contexto**: ZFS es un sistema de archivos y administrador de volúmenes avanzado conocido por su integridad de datos, instantáneas y RAID-Z. Originalmente de Sun Microsystems, ahora es de código abierto como OpenZFS en Linux. Muchos usuarios recurren a ZFS para construir NAS caseros y obtener funciones de nivel empresarial sin hardware costoso.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZFS">ZFS - Wikipedia</a></li>
<li><a href="https://itsfoss.com/what-is-zfs/">What is ZFS? Why are People Crazy About it? - It's FOSS OpenZFS Understanding the ZFS File System: A Complete Guide Why ZFS is the ultimate filesystem for your NAS - XDA Developers ZFS on Linux: How to Use It Properly (With Real Examples) An Introduction to the Z File System (ZFS) for Linux</a></li>

</ul>
</details>

**Discusión**: Los comentaristas compartieron sus propias experiencias: uno usó Proxmox para gestionar volúmenes, otro extrajo unidades WD Elements para discos de helio, y otros recomendaron servicios adicionales como Avahi y wsdd2 para descubrimiento automático. También se mencionaron sistemas de archivos alternativos como XFS con dm-integrity para quienes desconfían de la estabilidad de ZFS.

**Etiquetas**: `#NAS`, `#ZFS`, `#almacenamiento`, `#tutorial`, `#DIY`

---

<a id="item-4"></a>
## [Firmware de Tenda contiene puerta trasera de autenticación oculta](https://kb.cert.org/vuls/id/213560) ⭐️ 8.0/10

Una divulgación de vulnerabilidad revela que múltiples versiones del firmware de Tenda contienen una puerta trasera de autenticación oculta que permite acceso al router sin validar el nombre de usuario. Esta puerta trasera podría permitir a atacantes obtener acceso administrativo no autorizado a los routers Tenda afectados, comprometiendo potencialmente la seguridad de la red. Esto destaca los problemas de seguridad continuos en dispositivos de red de consumo y la necesidad de mayor transparencia por parte de los fabricantes. La puerta trasera se activa mediante una contraseña específica almacenada en la variable 'sys.rzadmin.password', que es 'rzadmin'. El nombre de usuario asociado no se valida, por lo que cualquier nombre de usuario funciona con esta contraseña.

hackernews · miniBill · jul 8, 00:08 · [Discusión](https://news.ycombinator.com/item?id=48825749)

**Contexto**: Una puerta trasera de firmware es un método oculto para eludir la autenticación normal en el firmware de un dispositivo. Tenda es un fabricante chino de equipos de red como routers y switches. Esta puerta trasera parece estar insertada intencionalmente, permitiendo acceso remoto sin credenciales adecuadas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hardware_backdoor">Hardware backdoor - Wikipedia</a></li>

</ul>
</details>

**Discusión**: Los comentaristas expresan fuertes críticas hacia Tenda y las empresas de hardware de red en general, y algunos recomiendan usar firmware de código abierto como OpenWRT. Un comentarista señala un artículo de 2022 que revela la contraseña de la puerta trasera 'rzadmin', y otro señala que el acceso root podría usarse para desactivar funciones no deseadas.

**Etiquetas**: `#seguridad`, `#backdoor`, `#firmware`, `#routers`, `#vulnerabilidad`

---

<a id="item-5"></a>
## [MIT OCW Publica las Conferencias en Video de SICP de 1986](https://ocw.mit.edu/courses/6-001-structure-and-interpretation-of-computer-programs-spring-2005/video_galleries/video-lectures/) ⭐️ 8.0/10

MIT OpenCourseWare ha puesto a disposición del público el conjunto completo de conferencias en video de 1986 para 'Estructura e Interpretación de Programas de Computadora'. Estas conferencias, impartidas por los autores del libro Harold Abelson y Gerald Jay Sussman, ofrecen una forma accesible de aprender conceptos fundamentales de ciencias de la computación a través de Lisp. La calidad de audio en las conferencias es reportadamente pobre, pero el contenido sigue siendo muy valioso. Miembros de la comunidad recomiendan usar Racket con un paquete de compatibilidad SICP como alternativa moderna a MIT Scheme para seguir las lecciones.

hackernews · gjvc · jul 7, 23:57 · [Discusión](https://news.ycombinator.com/item?id=48825664)

**Contexto**: SICP es un libro de texto seminal de ciencias de la computación que enseña principios de programación usando el dialecto Scheme de Lisp. Las conferencias en video, grabadas en 1986 en MIT, presentan a los autores impartiendo el material en un entorno de aula.

**Discusión**: Los miembros de la comunidad expresan un fuerte entusiasmo por las conferencias, y algunos les atribuyen su carrera en Lisp y Clojure. Se sugieren usar Racket como entorno moderno, y un usuario señala que las conferencias son más fáciles de seguir que el libro solo. Se mencionan quejas sobre la mala calidad de audio, pero el sentimiento general es muy positivo, y muchos recomiendan las conferencias como imprescindibles.

**Etiquetas**: `#programación funcional`, `#Lisp`, `#educación en computación`, `#SICP`, `#conferencias`

---

<a id="item-6"></a>
## [Informe GAO: DOE excluye opciones más baratas de limpieza en Oak Ridge](https://www.gao.gov/products/gao-26-108193) ⭐️ 8.0/10

La Oficina de Responsabilidad Gubernamental (GAO) publicó un informe que concluye que el Departamento de Energía (DOE) está eliminando prematuramente opciones más económicas para la limpieza de mercurio en la Reserva de Oak Ridge, lo que podría aumentar los costos en miles de millones de dólares. Esta decisión podría desperdiciar hasta 2 mil millones de dólares de los contribuyentes si las alternativas más baratas resultan efectivas, y plantea dudas sobre la gestión del DOE en proyectos de limpieza ambiental en sitios de armas nucleares. El informe de la GAO critica específicamente al DOE por no evaluar completamente tecnologías de menor costo antes de comprometerse con un único enfoque de limpieza, y enfatiza que la contaminación implica mercurio, no radiactividad, de la producción histórica de armas en la planta Y-12.

hackernews · Jimmc414 · jul 7, 22:23 · [Discusión](https://news.ycombinator.com/item?id=48824826)

**Contexto**: La Reserva de Oak Ridge en Tennessee se utilizó para la producción de armas nucleares desde la década de 1950 hasta la de 1980, liberando más de 700,000 libras de mercurio al medio ambiente. El DOE estima que la limpieza de este mercurio podría costar al menos 3.2 mil millones de dólares y llevar décadas. Un informe anterior de la GAO en 2024 ya destacaba riesgos en la gestión de costos y tecnologías en este sitio.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.gao.gov/products/gao-24-107096">U.S. GAO - Oak Ridge Mercury Cleanup: Opportunities Exist to Enhance Risk Management and Technology Development</a></li>
<li><a href="https://www.gao.gov/assets/gao-24-107096.pdf">Page 1 GAO-24-107096 MERCURY CLEANUP AT OAK RIDGE</a></li>

</ul>
</details>

**Discusión**: Los comentaristas elogiaron el informe de la GAO por su comunicación clara y recomendaciones prácticas. Un usuario aclaró que el problema es sobre contaminación por mercurio, no radiactividad, y otro expresó preocupación por el posible desperdicio de 2 mil millones de dólares que podrían haberse utilizado en otra parte.

**Etiquetas**: `#auditoría gubernamental`, `#limpieza nuclear`, `#mercurio`, `#eficiencia del gasto`, `#Oak Ridge`

---

<a id="item-7"></a>
## [Kokoro TTS: texto a voz local de alta calidad y optimizado para CPU](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro es un modelo de texto a voz de código abierto optimizado para CPU, que ofrece síntesis de voz de alta calidad sin necesidad de una GPU dedicada. Incluye soporte para guías de pronunciación IPA manuales y se ejecuta localmente mediante una herramienta de línea de comandos. Esto es importante porque democratiza la síntesis de voz de alta calidad, haciéndola accesible para usuarios con hardware limitado, beneficiando especialmente las aplicaciones de accesibilidad. También permite control manual de pronunciación, mejorando la precisión para vocabulario especializado. Kokoro tiene 82 millones de parámetros y soporta múltiples idiomas y voces personalizadas. Los usuarios informan que a veces pronuncia mal los homógrafos y tiene un rendimiento inferior en frases muy cortas.

hackernews · speckx · jul 7, 18:24 · [Discusión](https://news.ycombinator.com/item?id=48821576)

**Contexto**: Los sistemas de texto a voz (TTS) convierten texto escrito en palabras habladas. Muchos modelos TTS modernos de alta calidad dependen del aprendizaje profundo y a menudo requieren GPU potentes para inferencia en tiempo real, lo que limita su uso en computadoras estándar. Kokoro aborda esto al estar optimizado para ejecución solo en CPU, haciéndolo factible en portátiles y escritorios sin aceleradores de IA dedicados. Esto permite la síntesis de voz privada y fuera de línea para tareas como leer artículos en voz alta o ayudar a usuarios con discapacidades visuales.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/nazdridoy/kokoro-tts">GitHub - nazdridoy/kokoro-tts: A CLI text-to-speech tool ...</a></li>
<li><a href="https://kokorottsai.com/">Kokoro TTS: Advanced AI Text-to-Speech Model with 82M parameters</a></li>

</ul>
</details>

**Discusión**: La retroalimentación de la comunidad es en gran medida positiva, valorando su eficiencia en CPU y el control manual de pronunciación. Los desarrolladores lo han integrado en herramientas de accesibilidad y extensiones de Chrome. Algunos señalan limitaciones con homógrafos y texto muy corto.

**Etiquetas**: `#TTS`, `#accesibilidad`, `#CPU`, `#modelo local`, `#ingeniería de software`

---

<a id="item-8"></a>
## [Estadísticas de LineageOS revelan 74% de instalaciones no oficiales, muchas en no teléfonos](https://stats.lineageos.org/) ⭐️ 8.0/10

El equipo de LineageOS publicó estadísticas oficiales que muestran que el 74% de todas las instalaciones de LineageOS son compilaciones no oficiales, y solo el 9% ejecuta la versión más reciente. Esto indica un cambio en el uso de ROMs personalizados hacia dispositivos no telefónicos y compilaciones no oficiales, destacando los desafíos para mantener parches de seguridad actualizados y soporte oficial de dispositivos. Más de dos tercios de las instalaciones en EE. UU. son en dispositivos no telefónicos como Waydroid y Nintendo Switch; la mayoría de las instalaciones en teléfonos provienen de China, Brasil y Vietnam, y menos del 21% recibe actualizaciones de seguridad.

hackernews · pentagrama · jul 8, 01:27 · [Discusión](https://news.ycombinator.com/item?id=48826329)

**Contexto**: LineageOS es un popular ROM personalizado de Android basado en el Proyecto de Código Abierto de Android (AOSP), que permite a los usuarios ejecutar una experiencia Android estándar en varios dispositivos. Waydroid es una capa de compatibilidad basada en contenedores que permite ejecutar Android en escritorios Linux utilizando una compilación personalizada de LineageOS. Las estadísticas revelan que muchos usuarios ejecutan LineageOS en dispositivos no tradicionales como la Nintendo Switch, que tiene un puerto oficial de LineageOS.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Waydroid">Waydroid</a></li>
<li><a href="https://xdaforums.com/t/official-lineageos-22-for-the-nintendo-switch-v1-v2-lite-oled-android-tv-tablet.4676854/">[OFFICIAL] LineageOS 22 for the Nintendo Switch (v1/v2/Lite ...</a></li>

</ul>
</details>

**Discusión**: Los comentaristas expresaron sorpresa por la alta proporción de compilaciones no oficiales y el total relativamente bajo de 1 millón de dispositivos. Algunos señalaron que los usuarios preocupados por la privacidad pueden no enviar telemetría, sesgando los datos, mientras que otros lamentaron el declive de los ROMs personalizados y la creciente dificultad para desbloquear cargadores de arranque. Varios usuarios también destacaron la prevalencia de instalaciones no telefónicas en Waydroid y Nintendo Switch.

**Etiquetas**: `#LineageOS`, `#Android`, `#ROMs personalizados`, `#Estadísticas`

---

<a id="item-9"></a>
## [Hackers pueden usar 9 de las herramientas de IA más populares para montar botnets masivos](https://arstechnica.com/security/2026/07/hackers-can-use-9-of-the-most-popular-ai-tools-to-assemble-massive-botnets/) ⭐️ 8.0/10

Investigadores descubrieron una nueva técnica de ataque llamada 'HalluSquatting' que explota la tendencia de los grandes modelos de lenguaje (LLMs) a alucinar—generar información falsa—para orquestar botnets a gran escala. El ataque se dirige a 9 herramientas de IA populares, aprovechando su incapacidad para decir 'no sé' para engañarlas y ejecutar comandos maliciosos. Esta vulnerabilidad representa una nueva clase de ataques 'pull-based' que pueden escalar masivamente sin necesidad de enviar cargas maliciosas directamente. Destaca una falla de seguridad fundamental en los LLMs: su incapacidad para reconocer la incertidumbre, que puede ser armada para comprometer sistemas de IA ampliamente utilizados y potencialmente controlar vastas redes de dispositivos comprometidos. HalluSquatting es un ataque 'pull-based', lo que significa que el atacante coloca trampas en las que el LLM cae, en lugar de enviar explotaciones al modelo. Explota específicamente el fenómeno de alucinación en los LLMs, donde generan información falsa pero con apariencia plausible, para manipular el modelo y ejecutar comandos de botnet. La investigación afirma que 9 de las herramientas de IA más populares son vulnerables.

rss · Ars Technica · jul 8, 07:00

**Contexto**: Los grandes modelos de lenguaje (LLMs) son sistemas de IA entrenados con grandes cantidades de datos textuales para generar texto similar al humano. Un problema conocido es la 'alucinación', donde el modelo produce información falsa o sin sentido. HalluSquatting es un nuevo ataque que arma este fenómeno engañando a los LLMs para que crean y actúen sobre información falsa, reclutándolos efectivamente en una botnet. Las botnets tradicionales se basan en ataques 'push' como descargas de malware, pero HalluSquatting es 'pull-based', lo que dificulta su detección.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://rutgersradiationoncologyresidency.org/article/ai-botnet-alert-hallusquatting-exposes-9-popular-tools-to-massive-attacks">AI Botnet Alert: HalluSquatting Exposes 9 Popular Tools to</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#ciberseguridad`, `#inteligencia artificial`, `#botnets`, `#modelos de lenguaje`, `#vulnerabilidad`

---

<a id="item-10"></a>
## [La demanda energética de los centros de datos amenaza el plan de fabricación de Trump](https://arstechnica.com/tech-policy/2026/07/us-manufacturers-energy-costs-soar-because-of-ai-data-center-demand/) ⭐️ 8.0/10

Un aumento en el consumo de electricidad de los centros de datos de IA está elevando los costos energéticos para los fabricantes en el Rust Belt, lo que podría socavar la iniciativa 'Hecho en América' de Trump. Esta tensión resalta un conflicto crítico entre la rápida expansión de la infraestructura de IA y el objetivo de revitalizar la fabricación nacional, ya que las facturas de energía más altas podrían desalentar el crecimiento industrial en regiones clave. El Rust Belt, tradicionalmente un centro de fabricación, está experimentando precios elevados de electricidad debido a los crecientes requisitos energéticos de los centros de datos de IA cercanos, que pueden consumir tanta electricidad como cientos de miles de hogares.

rss · Ars Technica · jul 7, 21:03

**Contexto**: Los centros de datos de inteligencia artificial requieren enormes cantidades de energía para alimentar y enfriar sus servidores. Esta demanda ha crecido rápidamente, sobrecargando las redes locales y aumentando los costos para otros consumidores, incluidos los fabricantes. El plan 'Hecho en América' busca impulsar la fabricación estadounidense, pero el aumento de los precios de la energía podría hacer que la producción nacional sea menos competitiva.

**Etiquetas**: `#energía`, `#centros de datos`, `#inteligencia artificial`, `#fabricación`, `#política`

---

<a id="item-11"></a>
## [DeepSeek de China planea fabricar sus propios chips de IA](https://arstechnica.com/ai/2026/07/facing-us-export-controls-chinas-deepseek-plans-to-make-its-own-chips/) ⭐️ 8.0/10

DeepSeek ha anunciado planes para desarrollar sus propios chips de inteligencia artificial, con el objetivo de reducir su dependencia de Nvidia y Huawei en medio del endurecimiento de los controles de exportación de EE.UU. La empresa ha comenzado a reclutar talento en diseño de semiconductores para llevar a cabo esta iniciativa. Este movimiento podría reconfigurar el panorama del hardware de IA al crear un nuevo actor en el diseño de chips y reducir la dependencia china de proveedores extranjeros de GPU. El enfoque de bajo coste de entrenamiento de DeepSeek ya presionó a Nvidia, y la integración vertical podría perturbar aún más el mercado. DeepSeek se estaría centrando en el diseño de chips en lugar de la fabricación, aprovechando su acceso a 10.000 GPUs Hopper autorizadas. El proyecto aún se encuentra en etapas tempranas y no se ha anunciado un cronograma para la producción en masa.

rss · Ars Technica · jul 7, 16:14

**Contexto**: DeepSeek es una empresa china de IA fundada en 2023, conocida por desarrollar modelos de lenguaje grandes eficientes como DeepSeek-R1 a una fracción del coste de los competidores. Enfrentó restricciones de exportación de EE.UU. sobre chips de IA avanzados, lo que limitó el acceso a las mejores GPU de Nvidia. Los modelos de peso abierto y las ventajas de coste de la compañía ya han impactado en la industria, provocando una caída significativa en el valor de las acciones de Nvidia.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://www.techpowerup.com/332565/deepseek-reportedly-pursuing-development-of-proprietary-ai-chip">DeepSeek Reportedly Pursuing Development of Proprietary AI Chip</a></li>
<li><a href="https://www.digitimes.com/news/a20250213PD232/chips-talent-development-design-hpc.html">DeepSeek reportedly exploring in-house chip development</a></li>

</ul>
</details>

**Etiquetas**: `#DeepSeek`, `#chips`, `#controles de exportación`, `#independencia tecnológica`, `#IA`

---

<a id="item-12"></a>
## [Nuevo catálogo de virus identifica los patógenos de mayor amenaza pandémica](https://arstechnica.com/health/2026/07/new-virus-catalog-reveals-which-pathogens-pose-the-greatest-threat/) ⭐️ 8.0/10

Investigadores han elaborado un catálogo completo de virus que clasifica los patógenos según su potencial pandémico, utilizando datos sobre sus características genéticas y biológicas. Este catálogo proporciona una herramienta crucial para la seguridad sanitaria mundial al destacar qué virus requieren vigilancia e investigación urgentes, lo que podría orientar los esfuerzos de preparación y el desarrollo de vacunas. El catálogo aprovecha bases de datos genómicas existentes y datos epidemiológicos para evaluar factores de riesgo como la transmisibilidad, la virulencia y el potencial evolutivo.

rss · Ars Technica · jul 7, 13:15

**Contexto**: Identificar qué virus representan la mayor amenaza pandémica es un desafío clave en la salud pública. La vigilancia tradicional a menudo se centra en patógenos conocidos, pero los nuevos catálogos buscan evaluar sistemáticamente tanto los virus conocidos como los nuevos utilizando datos moleculares y ecológicos.

**Etiquetas**: `#virus`, `#pandemia`, `#salud pública`, `#investigación`, `#catálogo`

---

<a id="item-13"></a>
## [TorchJD: Descenso jacobiano para múltiples pérdidas en PyTorch](https://www.reddit.com/r/MachineLearning/comments/1upzxk2/torchjd_training_with_multiple_losses_in_pytorch_p/) ⭐️ 8.0/10

TorchJD, una nueva biblioteca de PyTorch, implementa métodos de descenso jacobiano para entrenar con múltiples funciones de pérdida. Ha sido aceptada oficialmente en el ecosistema de PyTorch. TorchJD ofrece una alternativa práctica a la escalarización para entrenar con múltiples pérdidas, especialmente cuando los objetivos están en conflicto. Permite a los investigadores probar fácilmente varios métodos de descenso jacobiano, lo que puede mejorar el rendimiento en aprendizaje multitarea. TorchJD implementa muchos métodos de agregación existentes para el descenso jacobiano de la literatura. Se basa en la teoría del descenso jacobiano para optimización multiobjetivo y soporta aprendizaje multitarea y minimización de riesgo por instancia.

reddit · r/MachineLearning · /u/Skeylos2 · jul 7, 16:20

**Contexto**: Al entrenar con múltiples funciones de pérdida, un enfoque común es la escalarización, que combina las pérdidas en una suma ponderada única. Sin embargo, cuando los objetivos están en conflicto, la escalarización puede ser subóptima. El descenso jacobiano extiende el descenso de gradiente a funciones vectoriales calculando la matriz jacobiana de gradientes y agregándolos en una actualización que busca disminuir todas las pérdidas simultáneamente. TorchJD proporciona una biblioteca que hace que estos métodos sean fácilmente accesibles.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.16232">[2406.16232] Jacobian Descent for Multi-Objective Optimization</a></li>
<li><a href="https://github.com/TorchJD/torchjd">GitHub - SimplexLab/TorchJD: Library for Jacobian descent with PyTorch. It enables the optimization of neural networks with multiple losses (e.g. multi-task learning). · GitHub</a></li>
<li><a href="https://torchjd.org/stable/index.html">TorchJD</a></li>

</ul>
</details>

**Etiquetas**: `#PyTorch`, `#múltiples pérdidas`, `#descenso jacobiano`, `#optimización`, `#aprendizaje automático`

---

<a id="item-14"></a>
## [CTO de Mozilla realizará AMA sobre informe de IA de código abierto](https://www.reddit.com/r/MachineLearning/comments/1upxdvc/raffi_krikorian_cto_mozilla_ama_on_the_state_of/) ⭐️ 8.0/10

Raffi Krikorian, CTO de Mozilla, anunció un AMA en Reddit para discutir el informe inaugural 'State of Open Source AI', que se publicará el 14 de julio. Abordará temas como los costos ocultos de los modelos gratuitos, la adopción empresarial, el efecto China, la confianza del desarrollador y el 'agentic harness'. Este AMA ofrece a la comunidad de aprendizaje automático un diálogo directo con un alto ejecutivo de la industria sobre el estado real de la IA de código abierto, más allá del bombo publicitario. Las conclusiones del informe y la discusión podrían influir en cómo los desarrolladores y las empresas navegan por el panorama de la IA de código abierto. El informe se basa en una encuesta a más de 950 desarrolladores y cubre el 'impuesto oculto' de los modelos supuestamente gratuitos, el auge del 'agentic harness' como nueva capa competitiva y el impacto disruptivo de los modelos chinos de código abierto como DeepSeek y OpenClaw.

reddit · r/MachineLearning · /u/raffikrikorian · jul 7, 14:51

**Contexto**: La IA de código abierto se refiere a modelos y herramientas disponibles públicamente para su uso, modificación y distribución. El 'agentic harness' es la infraestructura de ingeniería necesaria para que los agentes de IA sean fiables en producción, y se ha convertido en un diferenciador clave. Los modelos chinos de código abierto han desencadenado recientemente guerras de precios y han cambiado el equilibrio de poder en el ecosistema de IA.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://harness-engineering.ai/blog/agent-harness-complete-guide/">The Complete Guide to Agent Harness: What It Is and Why It ...</a></li>
<li><a href="https://investorplace.com/hypergrowthinvesting/2026/06/why-the-smartest-ai-investors-are-ignoring-the-model-race/">The Agentic AI Tax: Who Pays and Who Profits | InvestorPlace</a></li>
<li><a href="https://theaicronicle.com/en/news/economics/when-disruptor-gets-disrupted-chinese-open-source-ai">Chinese AI: How Open-Source is Disrupting the Industry</a></li>

</ul>
</details>

**Etiquetas**: `#inteligencia artificial`, `#código abierto`, `#Mozilla`, `#AMA`, `#desarrolladores`

---

<a id="item-15"></a>
## [Descifran script bash ofuscado en camiseta de Uniqlo](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) ⭐️ 7.0/10

Un blogger descifró el script bash ofuscado impreso en una camiseta de Uniqlo x Akamai, revelando que se trata de una animación auto-evaluada de desplazamiento sinusoidal que muestra '♥PEACE♥FOR♥ALL'. Este incidente ilustra la intersección de la cultura de programación y la moda, proporcionando un ejemplo concreto de ofuscación y desofuscación de bash que involucra a la comunidad técnica con creatividad y humor. El script utiliza sustitución con sed, sustitución de comandos y eval para desofuscarse a sí mismo, produciendo finalmente una animación en terminal con códigos de escape ANSI. El diseñador hizo intencionalmente que el script fuera difícil de OCR, añadiendo un desafío adicional.

hackernews · speerer · jul 8, 08:46 · [Discusión](https://news.ycombinator.com/item?id=48829312)

**Contexto**: La ofuscación de bash es la práctica de hacer que un script de shell sea difícil de leer mientras se preserva su funcionalidad, a menudo usando codificación, eval y sustitución. Los scripts auto-evaluados usan el comando eval para ejecutar código generado dinámicamente, ocultando la lógica original. Comprender estas técnicas es común en ciberseguridad y entre aficionados con fines de aprendizaje.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/bash-obfuscate-script">How to Obfuscate a Bash Script to Make It Unreadable - Baeldung GitHub - iyarivky/debash: DeBash is a online tool that aims ... How do I Deobfuscate a bash script? – Technical-QA.com Obfuscator.io Deobfuscator Script Deobfuscator - SkriptTools.net JavaScript Deobfuscator</a></li>
<li><a href="https://github.com/Bashfuscator/Bashfuscator">GitHub - Bashfuscator/Bashfuscator: A fully configurable and ...</a></li>

</ul>
</details>

**Discusión**: Los comentarios en el artículo fueron desenfadados y técnicos, con usuarios bromeando sobre devolver la camiseta debido a errores de sintaxis, compartiendo un vídeo del diseñador sobre el proceso de creación, e incluso proporcionando una versión en Python del script. Otros discutieron el desafío de aplicar OCR al texto ofuscado y elogiaron la creatividad detrás del diseño.

**Etiquetas**: `#bash`, `#script ofuscado`, `#camiseta técnica`, `#análisis de código`, `#comunidad hacker`

---

<a id="item-16"></a>
## [Propuestas Chat Control de la UE generan debate sobre privacidad](https://fightchatcontrol.eu/chat-control-overview) ⭐️ 7.0/10

La Ley Chat Control 1.0 de la Unión Europea, una norma temporal que permitía el escaneo de mensajes privados en busca de contenido de abuso infantil, expiró en abril de 2026, mientras que la propuesta más amplia Chat Control 2.0 sigue en negociación. Estas propuestas podrían obligar a la vigilancia masiva de las comunicaciones privadas, lo que socavaría el cifrado de extremo a extremo y afectaría la privacidad y seguridad de millones de ciudadanos de la UE. Chat Control 1.0 fue una exención temporal que permitía a los proveedores escanear mensajes sin orden judicial, mientras que Chat Control 2.0 propone el escaneo en el lado del cliente y podría afectar mensajes cifrados, aunque sigue sin acordarse tras cinco rondas de trílogos.

hackernews · gasull · jul 7, 14:23 · [Discusión](https://news.ycombinator.com/item?id=48818311)

**Contexto**: La UE ha estado desarrollando leyes para combatir el material de abuso sexual infantil en línea. Chat Control 1.0, aprobada en 2021, permitía a las empresas escanear en busca de dicho contenido. Chat Control 2.0 pretende hacer el escaneo permanente y obligatorio. Los críticos argumentan que permite la vigilancia masiva sin orden judicial y rompe el cifrado de extremo a extremo, violando derechos fundamentales.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://stateofsurveillance.org/news/eu-chat-control-expires-april-3-scanning-ends-whats-next-2026/">Chat Control Is Dead. Long Live Chat Control. - State of ...</a></li>

</ul>
</details>

**Discusión**: Los comentaristas expresan un fuerte escepticismo, argumentando que las propuestas son un pretexto para la vigilancia masiva y cuestionan su efectividad, señalando alternativas técnicas como la instalación de clientes de código abierto.

**Etiquetas**: `#privacidad`, `#seguridad infantil`, `#cifrado`, `#legislación`, `#vigilancia masiva`

---

<a id="item-17"></a>
## [El Tribunal Supremo permite a Texas imponer ley de verificación de edad en tiendas de aplicaciones](https://arstechnica.com/tech-policy/2026/07/supreme-court-lets-texas-enforce-age-verification-law-on-app-stores/) ⭐️ 7.0/10

El Tribunal Supremo de Estados Unidos permitió a Texas hacer cumplir su ley de verificación de edad para tiendas de aplicaciones, rechazando la solicitud de las grandes tecnológicas de bloquearla mientras continúan las apelaciones. Esta decisión permite a los estados regular las plataformas digitales en materia de verificación de edad, lo que podría reconfigurar el ecosistema de internet y las protecciones de la libertad de expresión en línea. La ley, aprobada originalmente por Texas, exige que las tiendas de aplicaciones verifiquen las edades de los usuarios y obtengan consentimiento parental para menores, enfrentando la oposición de grupos de la industria tecnológica.

rss · Ars Technica · jul 7, 20:18

**Contexto**: Las leyes de verificación de edad para plataformas en línea se han debatido como una forma de proteger a los menores de contenido dañino. Sin embargo, las empresas tecnológicas argumentan que dichas leyes imponen requisitos gravosos y pueden conducir a la censura. La ley de Texas es parte de una tendencia más amplia de regulación de internet a nivel estatal.

**Etiquetas**: `#ley de verificación de edad`, `#tiendas de aplicaciones`, `#Tribunal Supremo`, `#censura`, `#Texas`

---

<a id="item-18"></a>
## [Tesis doctoral sobre trazado de rayos diferenciable para propagación de radio](https://www.reddit.com/r/MachineLearning/comments/1upvkp5/phd_thesis_on_differentiable_ray_tracing_for/) ⭐️ 7.0/10

Una nueva tesis doctoral presenta un marco de trazado de rayos diferenciable para el modelado de propagación de radio, utilizando JAX para la diferenciación automática y resolver problemas inversos en comunicaciones inalámbricas. Este trabajo tiende un puente entre la simulación de propagación de radio y el aprendizaje automático al hacer el trazado de rayos diferenciable, permitiendo la optimización basada en gradientes y el entrenamiento de modelos para tareas como modelado de canales y localización. La tesis se divide en tres partes que cubren teoría electromagnética, trazado de rayos acelerado por GPU y aplicaciones como calibración de materiales. Utiliza el ecosistema de JAX y el autor ha publicado herramientas de código abierto como DiffeRT2d.

reddit · r/MachineLearning · /u/jeertmans · jul 7, 13:45

**Contexto**: El trazado de rayos es una técnica para simular la propagación de ondas siguiendo trayectorias de rayos. Hacerlo diferenciable permite calcular gradientes con respecto a los parámetros de la escena, posibilitando tareas de optimización. Los modelos de propagación de radio predicen la cobertura de señal y las características del canal. La combinación de ambos permite entrenar modelos de aprendizaje automático directamente sobre simulaciones físicas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/jeertmans/DiffeRT2d">GitHub - jeertmans/DiffeRT2d: 2D Toolbox for Differentiable ...</a></li>
<li><a href="https://docs.jax.dev/en/latest/automatic-differentiation.html">Automatic differentiation — JAX documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Radio_propagation">Radio propagation - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#diferenciable`, `#trazado de rayos`, `#propagación de radio`, `#comunicaciones inalámbricas`, `#aprendizaje automático`

---

<a id="item-19"></a>
## [Restringir el Fine-Tuning a un Subespacio de LoRA Confiable Evita el Envenenamiento](https://www.reddit.com/r/MachineLearning/comments/1uq68li/what_if_a_model_could_only_learn_what_trusted/) ⭐️ 7.0/10

Un nuevo artículo presenta una defensa que limita las actualizaciones de fine-tuning a un subespacio aprendido de adaptadores LoRA confiables, haciendo geométricamente inalcanzables ciertas actualizaciones maliciosas. Este enfoque replantea la seguridad del fine-tuning al restringir el espacio aprendible en lugar de detectar o eliminar datos envenenados, lo que podría proteger a los modelos contra puertas traseras ocultas. El método fue evaluado en 196 adaptadores LoRA públicos y contra ataques adaptativos diseñados para eludir la defensa, logrando una caída pronunciada en el éxito del ataque mientras se preserva la adaptación útil.

reddit · r/MachineLearning · /u/Bright_Warning_8406 · jul 7, 20:00

**Contexto**: LoRA (Low-Rank Adaptation) es una técnica eficiente en parámetros que ajusta modelos grandes aprendiendo actualizaciones de bajo rango, reduciendo costos de memoria y cómputo. Los ataques de envenenamiento en fine-tuning introducen datos maliciosos para insertar puertas traseras que provocan comportamientos no deseados. Esta defensa restringe el fine-tuning a solo actualizaciones en direcciones representadas en un conjunto de adaptadores LoRA confiables.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/">LLM04:2025 Data and Model Poisoning - OWASP Gen AI Security ...</a></li>

</ul>
</details>

**Discusión**: En el hilo de Reddit, los comentaristas discuten el potencial y las limitaciones del enfoque, y algunos sugieren formas de probar su robustez y otros proponen estrategias de ataque alternativas.

**Etiquetas**: `#seguridad en machine learning`, `#fine-tuning`, `#LoRA`, `#envenenamiento de datos`, `#defensa`

---

<a id="item-20"></a>
## [30papers.com: Los 30 artículos esenciales de ML de Ilya Sutskever](https://30papers.com/) ⭐️ 6.0/10

30papers.com se lanzó, ofreciendo una lista curada de 30 artículos de aprendizaje automático atribuidos a Ilya Sutskever, con una interfaz amigable para principiantes. Esta compilación proporciona una ruta de aprendizaje estructurada para principiantes en aprendizaje automático, basada en la experiencia de un investigador líder en IA. Sin embargo, la falta de verificación directa de Sutskever ha generado dudas en la comunidad. El sitio web incluye funciones de accesibilidad como interruptores para animaciones y fondos. El creador es un estudiante de primer año de ciencias de la computación en Trinity College Dublin.

hackernews · notmcrowley · jul 7, 15:58 · [Discusión](https://news.ycombinator.com/item?id=48819608)

**Contexto**: Ilya Sutskever es cofundador y científico jefe de OpenAI, conocido por sus contribuciones clave a los avances en aprendizaje profundo, incluidos los modelos GPT. Las listas curadas de artículos influyentes son una forma popular para que los estudiantes naveguen por el vasto campo del aprendizaje automático. Este sitio intenta presentar dicha lista en un formato accesible, pero la autenticidad de la atribución sigue sin confirmarse.

**Discusión**: Los comentarios de la comunidad expresaron escepticismo sobre el origen de la lista de artículos, señalando la falta de conexión directa con Ilya Sutskever. Algunos usuarios criticaron la usabilidad del sitio debido a animaciones intensas, mientras que el autor reconoció esto y agregó interruptores de accesibilidad. En general, la opinión fue mixta, con agradecimiento por el esfuerzo pero preocupación por la verificación.

**Etiquetas**: `#machine learning`, `#aprendizaje automático`, `#artículos esenciales`, `#Ilya Sutskever`, `#recursos para principiantes`

---

<a id="item-21"></a>
## [Componente web experimental incrusta código de GitHub mediante GPT-5.5](https://simonwillison.net/2026/Jul/7/github-code-component/#atom-everything) ⭐️ 6.0/10

Simon Willison creó un componente web experimental llamado github-code que incrusta código de repositorios de GitHub usando GPT-5.5. El componente obtiene el contenido del archivo sin procesar y muestra un rango específico de líneas con números de línea, pero sin resaltado de sintaxis. Este experimento demuestra cómo los modelos de lenguaje grandes pueden prototipar rápidamente componentes web funcionales. Reduce la barrera para incrustar fragmentos de código de GitHub en páginas web, aunque carece de funciones como el resaltado de sintaxis. El componente se construyó completamente mediante un prompt a GPT-5.5, sin código manual. Convierte las URLs de GitHub a URLs de raw.githubusercontent.com y usa fetch() para recuperar el código, mostrando solo el rango de líneas especificado en el fragmento de la URL.

rss · Simon Willison · jul 7, 16:18

**Contexto**: Los Web Components son un conjunto de APIs del navegador que permiten a los desarrolladores crear elementos HTML personalizados reutilizables. Este componente github-code es un ejemplo de un elemento personalizado que encapsula la funcionalidad para obtener y mostrar código de GitHub. GPT-5.5 es un modelo de lenguaje grande capaz de generar código a partir de instrucciones en lenguaje natural.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/7/github-code-component/">Tool: github-code Web Component - simonwillison.net</a></li>
<li><a href="https://github.com/topics/web-components">web-components · GitHub Topics · GitHub</a></li>

</ul>
</details>

**Etiquetas**: `#componente web`, `#GitHub`, `#código`, `#JavaScript`, `#incrustar`

---

<a id="item-22"></a>
## [Despidos de Microsoft golpean fuerte a Bethesda e id Software](https://arstechnica.com/gaming/2026/07/bethesda-id-software-reportedly-hit-hard-by-microsoft-layoffs/) ⭐️ 6.0/10

Microsoft ha despedido supuestamente hasta el 50% del personal en Bethesda e id Software, con posibles reducciones adicionales. Estos despidos podrían impactar significativamente el desarrollo de próximos juegos de estos renombrados estudios, y señalar una mayor consolidación en la industria del videojuego. Algunos equipos han perdido hasta la mitad de sus miembros, y las reducciones podrían continuar. El número exacto de empleados afectados no ha sido revelado.

rss · Ars Technica · jul 7, 19:52

**Etiquetas**: `#despidos`, `#Microsoft`, `#Bethesda`, `#id Software`, `#videojuegos`

---

<a id="item-23"></a>
## [Coche de carreras fabricado con fibras vegetales, basalto y agua de mar](https://arstechnica.com/cars/2026/07/this-race-car-is-made-from-plant-fibers-volcanoes-and-seawater/) ⭐️ 6.0/10

Lola ha anunciado una serie de continuación del T70, el T70S, que incorpora materiales sostenibles como fibra de basalto de roca volcánica y fibras vegetales, y puede usarse en competiciones o como vehículo legal en carretera. Esto representa un paso significativo hacia el automovilismo sostenible, demostrando que los compuestos ecológicos pueden cumplir con las exigencias de los coches de carreras de alto rendimiento. El T70S es un modelo de continuación basado en escaneos del Lola T70 original de la década de 1960. El uso de fibra de basalto y fibras vegetales reduce la dependencia de la fibra de carbono tradicional, que tiene una mayor huella ambiental.

rss · Ars Technica · jul 7, 16:45

**Contexto**: El Lola T70 es un coche de carreras clásico que compitió en la década de 1960, ganando eventos como las 24 Horas de Daytona. Los modelos de continuación son construcciones modernas de diseños históricos, a menudo utilizando planos originales o escaneos 3D. La fibra de basalto es una fibra natural hecha de roca volcánica, conocida por su resistencia al calor y su fuerza, y se considera una alternativa más ecológica a la fibra de vidrio o carbono. Las fibras vegetales como el lino o el cáñamo también se están explorando en compuestos automotrices.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arstechnica.com/cars/2026/07/this-race-car-is-made-from-plant-fibers-volcanoes-and-seawater/">This race car is made from plant fibers, volcanoes, ... and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lola_T70">Lola T70 - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a70894413/lola-t70-v8-powered-continuation-announced/">Lola Announces V-8-Powered T70 Race Car Continuation Model</a></li>

</ul>
</details>

**Etiquetas**: `#materiales sostenibles`, `#automoción`, `#innovación`, `#fibras vegetales`

---

<a id="item-24"></a>
## [Alineación inversa: ¿podrían los modelos 'malos' mostrar comportamiento 'bueno'?](https://www.reddit.com/r/MachineLearning/comments/1uq4qis/mid_research_got_me_thinking_what_about_reversed/) ⭐️ 6.0/10

Un usuario de Reddit propuso un experimento mental: si un modelo se entrena con recompensas por engaño y daño, podría ocasionalmente mostrar comportamiento bueno, lo que sería una forma de desalineación respecto a su entrenamiento. Esta idea cuestiona la suposición de que la alineación es solo un producto de RLHF, sugiriendo que el preentrenamiento podría incrustar una alineación latente que emerge incluso en modelos entrenados de forma adversaria. El usuario destaca que el comportamiento bueno en un modelo entrenado para el daño sería una desalineación irónica. Especula que el preentrenamiento ya podría contener una 'alineación' latente que el entrenamiento de alineación selecciona después.

reddit · r/MachineLearning · /u/Objective_River_5218 · jul 7, 19:08

**Contexto**: El Aprendizaje por Refuerzo a partir de Retroalimentación Humana (RLHF) es una técnica para alinear modelos de IA con preferencias humanas, entrenando un modelo de recompensa basado en retroalimentación humana y luego optimizando la IA con aprendizaje por refuerzo. La alineación de IA busca guiar los sistemas hacia objetivos y valores deseados. La desalineación ocurre cuando la IA persigue objetivos no intencionados. El preentrenamiento en grandes conjuntos de datos puede impartir conocimiento general y tendencias que el entrenamiento de alineación luego refina o redirige.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback">Reinforcement learning from human feedback - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**Etiquetas**: `#alineación de IA`, `#RLHF`, `#comportamiento emergente`, `#preentrenamiento`

---