---
layout: default
title: "Horizon Summary: 2026-07-16 (ES)"
date: 2026-07-16
lang: es
---

> De 30 artículos, 20 fueron seleccionados por relevancia

---

1. [Cero-día de Windows HiveLegacy lanzado en un Patch Tuesday récord](#item-1) ⭐️ 9.0/10
2. [Inkling: el modelo multimodal de pesos abiertos más grande con audio](#item-2) ⭐️ 8.0/10
3. [Si quieres crear un botón desde cero, primero debes crear el universo](#item-3) ⭐️ 8.0/10
4. [xAI publica el código fuente de Grok Build](#item-4) ⭐️ 8.0/10
5. [Informe insta a invertir en IA libre y de código abierto](#item-5) ⭐️ 8.0/10
6. [SQLite debería adoptar ediciones estilo Rust para corregir valores predeterminados](#item-6) ⭐️ 8.0/10
7. [Gemma 4 26B en CPU de 13 años: 5 tokens/segundo](#item-7) ⭐️ 8.0/10
8. [Vulnerabilidad en web_fetch de Claude permite exfiltración de datos](#item-8) ⭐️ 8.0/10
9. [Google Play se abrirá a tiendas de aplicaciones de terceros la próxima semana](#item-9) ⭐️ 8.0/10
10. [Bluesky adquiere la marca del Protocolo AT](#item-10) ⭐️ 7.0/10
11. [Sheetz abandona VMware, migra 11,000 máquinas virtuales a StorMagic](#item-11) ⭐️ 7.0/10
12. [Juez impide que Trump deporte a investigadores de moderación de contenido](#item-12) ⭐️ 7.0/10
13. [OpenAI lanza Codex Micro, un teclado iluminado para agentes de IA](#item-13) ⭐️ 7.0/10
14. [Buscando perspectivas críticas sobre los modelos del mundo JEPA para robótica](#item-14) ⭐️ 7.0/10
15. [Papers with Code lanza página de benchmarks de robótica](#item-15) ⭐️ 7.0/10
16. [La alegría perdida de la piratería musical](#item-16) ⭐️ 6.0/10
17. [FCC derogará el límite de propiedad del 39% en TV](#item-17) ⭐️ 6.0/10
18. [Presentadores de artículos en ECCV deben pagar tarifa completa de inscripción](#item-18) ⭐️ 6.0/10
19. [Modelo PyTorch 170 veces más lento en T4 que en A100; investigación de cuello de botella](#item-19) ⭐️ 6.0/10
20. [Revisiones de NeurIPS esperadas para el 22 de julio, surgen especulaciones](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Cero-día de Windows HiveLegacy lanzado en un Patch Tuesday récord](https://arstechnica.com/security/2026/07/windows-0-day-drops-the-same-day-microsoft-releases-record-number-of-patches/) ⭐️ 9.0/10

Un exploit de elevación de privilegios de Windows llamado HiveLegacy fue divulgado públicamente el mismo día que Microsoft lanzó un número récord de parches de seguridad, afectando una vulnerabilidad en el Servicio de Perfiles de Usuario de Windows. Este día cero es particularmente preocupante porque se describe como una 'primitiva poderosa' que podría ser aprovechada para ataques adicionales, y su lanzamiento simultáneo con un lote récord de parches sugiere un panorama de seguridad de alto riesgo. HiveLegacy es un exploit de elevación de privilegios que apunta al Servicio de Perfiles de Usuario de Windows, y los investigadores creen que podría habilitar otras acciones maliciosas más allá de la escalada de privilegios.

rss · Ars Technica · jul 15, 19:59

**Contexto**: Una vulnerabilidad de día cero es un fallo de seguridad desconocido para el proveedor y sin parche disponible en el momento de la divulgación. Los exploits que logran elevación de privilegios permiten a un atacante obtener acceso de mayor nivel a un sistema, a menudo llevando a un compromiso total. El 'Patch Tuesday' de Microsoft es una liberación mensual de actualizaciones de seguridad. El término 'primitiva' en el desarrollo de exploits se refiere a una capacidad básica que puede usarse como bloque de construcción para ataques más complejos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/windows-0-day-drops-the-same-day-microsoft-releases-record-number-of-patches/">Windows 0-day drops the same day Microsoft releases record number of patches - Ars Technica</a></li>

</ul>
</details>

**Etiquetas**: `#seguridad`, `#Windows`, `#vulnerabilidad`, `#zero-day`, `#actualización`

---

<a id="item-2"></a>
## [Inkling: el modelo multimodal de pesos abiertos más grande con audio](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines ha lanzado Inkling, el modelo multimodal de pesos abiertos más grande que admite audio, y está disponible para fine-tuning en la plataforma Tinker. Este modelo permite a las empresas personalizar una IA multimodal potente para sus tareas específicas a un costo potencialmente menor, desafiando el dominio de los modelos cerrados y fomentando el desarrollo abierto de IA. Inkling no es el modelo más fuerte en general, pero combina capacidades multimodales, razonamiento eficiente y disponibilidad en Tinker para fine-tuning, soportando audio junto con texto e imágenes.

hackernews · vimarsh6739 · jul 15, 18:12 · [Discusión](https://news.ycombinator.com/item?id=48924912)

**Contexto**: Los modelos de pesos abiertos liberan solo los parámetros entrenados, lo que permite ejecutar y ajustar el modelo, pero no necesariamente acceder al código o datos de entrenamiento. La IA multimodal procesa múltiples tipos de datos, como texto, imágenes y audio. El enfoque de pesos abiertos de Inkling permite la personalización para tareas especializadas a un costo menor que los modelos propietarios.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.ai21.com/glossary/open-weights-model/">What is an Open - Weights Model ? | AI21</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_learning">Multimodal learning - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/multimodal-ai">What is Multimodal AI? | IBM</a></li>

</ul>
</details>

**Discusión**: Segmondy proporcionó enlaces para ejecución local mediante llama.cpp y Unsloth, mostrando interés en la calidad del audio. Ls_stats destacó la necesidad de un modelo abierto estadounidense como DeepSeek, sugiriendo que Thinking Machines podría ocupar ese lugar. Wxw elogió el modelo de negocio de ofrecer modelos base abiertos ajustables en Tinker para personalización empresarial.

**Etiquetas**: `#modelo abierto`, `#multimodal`, `#audio`, `#pesos abiertos`, `#inteligencia artificial`

---

<a id="item-3"></a>
## [Si quieres crear un botón desde cero, primero debes crear el universo](https://madcampos.dev/blog/2026/07/accessibility-from-scratch/) ⭐️ 8.0/10

Un artículo satírico de MadCampos critica la tendencia de construir componentes web personalizados desde cero, destacando cómo la accesibilidad suele pasarse por alto en el proceso. Esta sátira subraya el esfuerzo desperdiciado en recrear elementos web nativos y los consiguientes fallos de accesibilidad, instando a los desarrolladores a priorizar los estándares y la experiencia del usuario. El autor utiliza el ejemplo de un botón simple para demostrar la cascada de decisiones y los problemas de accesibilidad al construir desde cero, abogando por el uso de elementos HTML nativos cuando sea posible.

hackernews · treve · jul 16, 03:48 · [Discusión](https://news.ycombinator.com/item?id=48930136)

**Contexto**: Los Web Components, un conjunto de estándares del W3C (custom elements, Shadow DOM, templates HTML), permiten a los desarrolladores crear elementos HTML reutilizables y encapsulados. Sin embargo, los componentes personalizados a menudo carecen de las funcionalidades de accesibilidad integradas del HTML nativo. Las Pautas de Accesibilidad al Contenido Web (WCAG) proporcionan estándares internacionales para hacer que el contenido web sea accesible para personas con discapacidades.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_Components">Web Components</a></li>
<li><a href="https://www.w3.org/WAI/standards-guidelines/wcag/">WCAG 2 Overview | Web Accessibility Initiative (WAI) | W3C</a></li>

</ul>
</details>

**Discusión**: Los comentaristas están en su mayoría de acuerdo con la sátira, compartiendo ejemplos de complejidad innecesaria y problemas de accesibilidad. Señalan que los elementos HTML nativos suelen ser suficientes, pero reconocen carencias como el filtrado del lado del servidor en comboboxes. También hay debate sobre estándares de accesibilidad contrapuestos (APCA vs. WCAG).

**Etiquetas**: `#accesibilidad`, `#desarrollo web`, `#HTML`, `#componentes`, `#sátira`

---

<a id="item-4"></a>
## [xAI publica el código fuente de Grok Build](https://github.com/xai-org/grok-build) ⭐️ 8.0/10

xAI ha publicado el código fuente completo de Grok Build, un asistente de codificación y sistema de construcción basado en terminal, en GitHub. Esto permite a cualquiera inspeccionar, modificar y redistribuir el software. Este movimiento aumenta la transparencia y permite a la comunidad examinar el software después de preocupaciones sobre la exfiltración de datos. Podría fomentar la confianza y acelerar el desarrollo de bifurcaciones que respeten la privacidad. El código incluye un renderizador de diagramas Mermaid autónomo para la terminal que utiliza caracteres Unicode. Sin embargo, el lanzamiento sigue a la controversia sobre el CLI grok que subía directorios completos al almacenamiento en la nube de xAI por defecto.

hackernews · skp1995 · jul 15, 20:24 · [Discusión](https://news.ycombinator.com/item?id=48926590)

**Contexto**: Grok Build es una herramienta de línea de comandos y sistema de construcción de xAI para desarrollar aplicaciones de IA, aprovechando el modelo de lenguaje Grok. Permite a los usuarios interactuar con la IA mediante indicaciones de lenguaje natural en la terminal. xAI, fundada por Elon Musk, es la empresa detrás del chatbot Grok.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://deepwiki.com/xai-org/grok-build">xai-org/grok-build | DeepWiki</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://grokipedia.com/page/Grok_Build">Grok Build</a></li>

</ul>
</details>

**Discusión**: Las reacciones de la comunidad son mixtas: algunos desarrolladores han creado bifurcaciones centradas en la privacidad como 'gork-build' que eliminan la telemetría y la recolección de datos. Otros ven la liberación del código como un movimiento táctico para recuperar la confianza tras el incidente de subida de datos, mientras que algunos elogian la calidad técnica del código.

**Etiquetas**: `#código abierto`, `#inteligencia artificial`, `#Grok Build`, `#xAI`, `#infraestructura`

---

<a id="item-5"></a>
## [Informe insta a invertir en IA libre y de código abierto](https://www.siegelendowment.org/wp-content/uploads/2026/07/fortune-david-siegel-open-source-ai.pdf) ⭐️ 8.0/10

Un nuevo informe de David Siegel insta a gobiernos, empresas y organizaciones sin fines de lucro a invertir en inteligencia artificial libre y de código abierto. Esto es importante porque podría redirigir la financiación pública y privada hacia la IA de código abierto, fomentando la transparencia y la competencia frente a los modelos propietarios. El informe argumenta que la inversión en IA de código abierto es una medida de seguridad, en contraste con los llamados a la captura regulatoria por parte de empresas privadas.

hackernews · bilsbie · jul 15, 21:16 · [Discusión](https://news.ycombinator.com/item?id=48927095)

**Contexto**: La IA de código abierto se refiere a modelos y código disponibles públicamente que cualquiera puede usar, modificar y distribuir. Los defensores argumentan que democratiza el acceso y reduce la concentración de poder, mientras que los críticos se preocupan por el uso indebido.

**Discusión**: Los comentarios de la comunidad expresan opiniones variadas: algunos abogan por la publicación obligatoria de pesos abiertos debido a los riesgos, otros proponen premios de incentivo para modelos abiertos, y algunos cuestionan la viabilidad de que el código abierto compita con la IA comercial.

**Etiquetas**: `#inteligencia artificial`, `#código abierto`, `#inversión pública`, `#regulación`, `#política tecnológica`

---

<a id="item-6"></a>
## [SQLite debería adoptar ediciones estilo Rust para corregir valores predeterminados](https://mort.coffee/home/sqlite-editions/) ⭐️ 8.0/10

Un artículo propone que SQLite adopte ediciones anuales, como Rust, para permitir optar por valores predeterminados mejorados, como claves foráneas, modo WAL y tipado estricto, sin romper la compatibilidad hacia atrás. Las ediciones permitirían a SQLite corregir sus 'valores predeterminados defectuosos' conservando la compatibilidad hacia atrás, un punto crítico para los desarrolladores. Este enfoque podría influir en cómo otros sistemas de bases de datos evolucionan. La edición propuesta 2026 habilitaría claves foráneas, modo WAL, un tiempo de espera de 5 segundos y tipado estricto para tablas nuevas. Las versiones antiguas de SQLite aún podrían leer bases de datos con una edición superior, aunque algunas funciones podrían no estar activas.

hackernews · gnyeki · jul 15, 22:42 · [Discusión](https://news.ycombinator.com/item?id=48928135)

**Contexto**: Los valores predeterminados de SQLite han sido criticados durante mucho tiempo: sin claves foráneas por defecto, modo de journal que puede llevar a corrupción, y tipado laxo mediante afinidad de tipos. Cambiar estos valores rompería bases de datos existentes. Las ediciones de Rust permiten que el lenguaje evolucione proporcionando rutas de migración optativas para nuevos comportamientos. La propuesta de ediciones de SQLite aplica esta idea a un motor de bases de datos, utilizando un PRAGMA que agrupa correcciones para problemas comunes.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://doc.rust-lang.org/edition-guide/editions/index.html">What are editions? - The Rust Edition Guide</a></li>
<li><a href="https://byteiota.com/sqlites-broken-defaults-the-case-for-rust-style-editions/">SQLite’s Broken Defaults: The Case for Rust-Style Editions</a></li>

</ul>
</details>

**Discusión**: Los comentarios en Hacker News muestran una mezcla de apoyo y escepticismo. Algunos elogian la propuesta por abordar problemas de larga data, mientras que otros argumentan que los comportamientos predeterminados de SQLite son intencionales y que objetos como DuckDB podrían adaptarse mejor a las necesidades del autor. También se plantearon preocupaciones sobre los metadatos de edición en archivos de base de datos y la compatibilidad con versiones antiguas.

**Etiquetas**: `#SQLite`, `#ediciones`, `#compatibilidad hacia atrás`, `#bases de datos`, `#evolución`

---

<a id="item-7"></a>
## [Gemma 4 26B en CPU de 13 años: 5 tokens/segundo](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

Una demostración muestra el modelo de mezcla de expertos Gemma 4 26B de Google ejecutándose a 5 tokens por segundo en un servidor dual Xeon de 13 años sin GPU, utilizando solo inferencia en CPU. Este logro destaca la creciente viabilidad de ejecutar modelos de lenguaje grandes en hardware común, reduciendo potencialmente la dependencia de costosas GPU y permitiendo la inferencia local para privacidad y uso sin conexión. El modelo en cuestión es una variante MoE de 26B parámetros con una ventana de contexto de 256K tokens, y el rendimiento reportado de 5 tokens/segundo es suficiente para tareas interactivas simples aunque más lento que las API en la nube.

hackernews · neomindryan · jul 15, 15:34 · [Discusión](https://news.ycombinator.com/item?id=48922434)

**Contexto**: Gemma 4 es la última familia de modelos de pesos abiertos de Google, lanzada en abril de 2026, con arquitecturas densas y de mezcla de expertos (MoE) con hasta 256K de contexto y soporte para más de 140 idiomas. Ejecutar modelos de lenguaje grandes en CPU es posible gracias a la cuantización y frameworks de inferencia eficientes como llama.cpp, aunque la velocidad está limitada por el ancho de banda de la memoria y la potencia de la CPU. La demostración utiliza un sistema dual Xeon de 13 años sin GPU, mostrando que incluso servidores antiguos pueden ejecutar modelos modernos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://itsfoss.com/testing-local-llms-without-gpu/">Can You Run LLMs Locally Without a GPU? I Tested 8 Models on Linux</a></li>

</ul>
</details>

**Discusión**: Los comentaristas debaten la rentabilidad de la inferencia local frente a las API en la nube, señalando que con los precios de la electricidad en Alemania, ejecutar el servidor cuesta aproximadamente $0.15 por los mismos tokens que cuestan $0.005 en un proveedor. Algunos comparten sus propias pruebas en hardware similar, logrando 7-12 tokens/segundo, y predicen que para mediados de 2027, los modelos de más de 200B parámetros se ejecutarán en hardware de consumo.

**Etiquetas**: `#Gemma 4`, `#inferencia local`, `#hardware antiguo`, `#optimización`, `#costo de inferencia`

---

<a id="item-8"></a>
## [Vulnerabilidad en web_fetch de Claude permite exfiltración de datos](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

El investigador Ayush Paul demostró un ataque de inyección de instrucciones que engaña a la herramienta web_fetch de Claude para extraer recuerdos privados del usuario, evitando las protecciones de navegación de Anthropic. Este ataque resalta una debilidad crítica en la seguridad de los agentes de IA, donde la combinación de datos sensibles con acceso web puede provocar violaciones de privacidad, subrayando la necesidad de defensas más robustas. El exploit aprovechó la capacidad de web_fetch de seguir enlaces incrustados en páginas obtenidas; Anthropic afirmó haberlo descubierto internamente y lo solucionó bloqueando la navegación a enlaces adicionales desde contenido obtenido.

rss · Simon Willison · jul 15, 14:21

**Contexto**: La herramienta web_fetch permite a Claude recuperar contenido de URLs especificadas por el usuario, inicialmente restringida a URLs ingresadas por el usuario o derivadas de búsquedas para evitar exfiltración. La 'tríada letal' se refiere a la combinación peligrosa de agentes de IA que procesan entradas no confiables, acceden a datos privados y tienen capacidades de exfiltración. Este ataque eludió las restricciones mediante indirección de instrucciones en múltiples pasos a través de un sitio honeypot.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool | Simon Willison’s Weblog</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>

</ul>
</details>

**Etiquetas**: `#seguridad en IA`, `#vulnerabilidad`, `#Claude`, `#exfiltración de datos`, `#ataque de inyección`

---

<a id="item-9"></a>
## [Google Play se abrirá a tiendas de aplicaciones de terceros la próxima semana](https://arstechnica.com/gadgets/2026/07/third-party-app-stores-coming-to-google-play-next-week-as-epic-settlement-withdrawn/) ⭐️ 8.0/10

Tras la retirada del acuerdo con Epic, Google debe implementar las medidas antimonopolio completas, permitiendo tiendas de aplicaciones de terceros en Google Play la próxima semana. Esto abre el ecosistema Android a tiendas de aplicaciones competidoras, potencialmente reduciendo costos para los desarrolladores y ofreciendo más opciones a los usuarios. Las medidas ordenadas por el tribunal exigen que Google detenga prácticas que mantienen su monopolio, como vincular el acceso a Play Store con su sistema de facturación.

rss · Ars Technica · jul 15, 16:55

**Contexto**: Epic Games demandó a Google por prácticas anticompetitivas en Play Store. Un jurado determinó que Google violó las leyes antimonopolio, y un tribunal ordenó medidas que incluyen permitir tiendas de aplicaciones de terceros. Google tenía un acuerdo con Epic que habría limitado estas medidas, pero Epic se retiró, activando las medidas completas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/07/third-party-app-stores-coming-to-google-play-next-week-as-epic-settlement-withdrawn/">Third-party app stores coming to Google Play next week as ...</a></li>
<li><a href="https://news.bloomberglaw.com/antitrust/google-proposes-to-share-play-store-catalog-to-resolve-case">Google Revamps Android App Stores to Resolve Antitrust Claims</a></li>
<li><a href="https://cdn.ca9.uscourts.gov/datastore/opinions/2025/07/31/24-6256.pdf">UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT</a></li>

</ul>
</details>

**Etiquetas**: `#Google`, `#Antimonopolio`, `#Google Play`, `#Epic Games`, `#Tiendas de aplicaciones`

---

<a id="item-10"></a>
## [Bluesky adquiere la marca del Protocolo AT](https://atproto.com/blog/at-protocol-trademark) ⭐️ 7.0/10

Bluesky adquirió recientemente la marca comercial de 'ATPROTOCOL' y sus variantes de una empresa que amenazaba con acciones legales, y planea transferir la propiedad a una organización independiente de gobernanza del protocolo en el futuro. Este movimiento aborda las preocupaciones sobre el control centralizado de un protocolo descentralizado, señalando un compromiso con la gobernanza abierta, mientras que resalta la actual falta de un organismo de gobierno independiente para el Protocolo AT. La marca fue adquirida de una empresa no identificada que amenazó con acciones legales para impedir que Bluesky y otros usaran el término. Bluesky ha delineado una política de uso para proteger el uso continuo de la marca por parte de la comunidad.

hackernews · chaosharmonic · jul 16, 01:21 · [Discusión](https://news.ycombinator.com/item?id=48929351)

**Contexto**: El Protocolo AT (Authenticated Transfer Protocol) es un protocolo abierto y descentralizado para construir aplicaciones web sociales a gran escala, y sirve como base para Bluesky, una plataforma de microblogging. Bluesky Social PBC, una corporación de beneficio, mantiene actualmente el protocolo. El protocolo se compara a menudo con ActivityPub, otro protocolo de redes sociales descentralizadas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bluesky">Bluesky - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>

</ul>
</details>

**Discusión**: Los miembros de la comunidad expresaron reacciones mixtas, algunos cuestionando el control por parte de una sola entidad sobre el Protocolo AT y haciendo comparaciones desfavorables con ActivityPub. Otros notaron los desafíos comunes de marcas comerciales que enfrentan las startups y apreciaron la transferencia planificada a una organización independiente.

**Etiquetas**: `#Protocolo AT`, `#Bluesky`, `#marcas comerciales`, `#gobernanza`, `#ActivityPub`

---

<a id="item-11"></a>
## [Sheetz abandona VMware, migra 11,000 máquinas virtuales a StorMagic](https://arstechnica.com/information-technology/2026/07/sheetz-moves-838-stores-off-vmware-broadcom-created-too-much-uncertainty/) ⭐️ 7.0/10

Sheetz, una gran cadena de tiendas de conveniencia, está migrando 11,000 máquinas virtuales de VMware a StorMagic debido a la incertidumbre generada por la adquisición de VMware por parte de Broadcom. Esta migración significativa destaca el creciente descontento entre los clientes de VMware tras la adquisición por parte de Broadcom, lo que podría desencadenar un éxodo mayor hacia plataformas de virtualización alternativas. Sheetz opera 838 tiendas y trasladará toda su infraestructura virtualizada a StorMagic, un proveedor británico de soluciones de virtualización de almacenamiento.

rss · Ars Technica · jul 15, 21:41

**Contexto**: VMware es un proveedor líder de software de virtualización, ampliamente utilizado en centros de datos empresariales. Broadcom adquirió VMware en 2023 por $61 mil millones, generando preocupaciones sobre cambios en las licencias y las hojas de ruta de los productos. StorMagic ofrece alternativas de virtualización de almacenamiento más simples y rentables, especialmente para entornos multisitio.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://stormagic.com/company/contact/">Contact StorMagic</a></li>
<li><a href="https://ch.linkedin.com/company/stormagic">StorMagic | LinkedIn</a></li>

</ul>
</details>

**Etiquetas**: `#VMware`, `#Broadcom`, `#migración`, `#virtualización`, `#StorMagic`

---

<a id="item-12"></a>
## [Juez impide que Trump deporte a investigadores de moderación de contenido](https://arstechnica.com/tech-policy/2026/07/judge-trump-cant-deport-researchers-just-for-working-in-content-moderation/) ⭐️ 7.0/10

Un juez federal falló que la administración Trump no puede deportar o negar visas a investigadores únicamente por su trabajo en moderación de contenido e investigación de desinformación. Esta decisión protege a los investigadores que estudian la desinformación en línea de represalias migratorias. Este fallo es importante porque protege la investigación académica y periodística sobre desinformación de la presión política. También establece un precedente de que la política migratoria no puede usarse para suprimir investigaciones que puedan ser críticas con el gobierno o sus políticas. El fallo se aplica específicamente a investigadores que estudian la moderación de contenido y la desinformación, bloqueando las denegaciones de visa y las deportaciones basadas únicamente en ese trabajo. La decisión fue elogiada por investigadores de desinformación como una victoria para la libertad de expresión y la libertad académica.

rss · Ars Technica · jul 15, 21:26

**Contexto**: En los últimos años, ha habido controversia política sobre las políticas de moderación de contenido en las plataformas de redes sociales. Algunos políticos han argumentado que los investigadores que estudian la desinformación están sesgados o forman parte de una conspiración para suprimir las voces conservadoras. La administración Trump, según informes, había apuntado a dichos investigadores para restricciones de visa como parte de una aplicación migratoria más amplia.

**Etiquetas**: `#moderación de contenido`, `#libertad de expresión`, `#inmigración`, `#desinformación`, `#política tecnológica`

---

<a id="item-13"></a>
## [OpenAI lanza Codex Micro, un teclado iluminado para agentes de IA](https://arstechnica.com/ai/2026/07/openais-first-branded-hardware-is-a-light-up-keyboard/) ⭐️ 7.0/10

OpenAI anunció el Codex Micro, un teclado de escritorio de edición limitada que permite a los usuarios monitorear y controlar múltiples agentes de IA a la vez mediante teclas iluminadas, un joystick y un dial. Este es el primer hardware de marca de OpenAI, lo que señala un cambio hacia interfaces físicas para gestionar flotas de agentes de IA, algo que podría volverse esencial a medida que la IA agentiva ingresa al lugar de trabajo. Con un precio de $230, el Codex Micro fue co-diseñado con el fabricante de teclados Work Louder e incluye teclas iluminadas que indican el estado del agente, un joystick para navegación, un dial para ajustar el nivel de razonamiento y teclas de acceso directo para acciones comunes.

rss · Ars Technica · jul 15, 16:00

**Contexto**: La IA agentiva se refiere a agentes de IA semi-autónomos que pueden realizar tareas complejas de múltiples pasos con mínima intervención humana. Actualmente, gestionar múltiples agentes a menudo requiere alternar entre interfaces de software, pero un teclado físico dedicado busca agilizar este proceso al proporcionar actualizaciones de estado de un vistazo y controles directos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.axios.com/2026/07/15/openai-keyboard-codex-agents">Codex Micro is a physical keyboard for AI agents - Axios</a></li>
<li><a href="https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/">Amid hardware legal battle, OpenAI releases a $230 keyboard for Codex | TechCrunch</a></li>
<li><a href="https://ainave.com/tech-news/openai-codex-micro-keyboard-230-hardware-for-multi-agent-coding-control">OpenAI Codex Micro keyboard: hands-on agent control for $230</a></li>

</ul>
</details>

**Etiquetas**: `#OpenAI`, `#hardware`, `#teclado inteligente`, `#agentes IA`, `#Codex Micro`

---

<a id="item-14"></a>
## [Buscando perspectivas críticas sobre los modelos del mundo JEPA para robótica](https://www.reddit.com/r/MachineLearning/comments/1uxcryc/looking_for_jepa_devil_advocates_r/) ⭐️ 7.0/10

Un usuario de Reddit en r/MachineLearning solicitó argumentos en contra de los modelos JEPA (Joint-Embedding Predictive Architecture) como modelos del mundo para robótica, buscando un contrapunto a las afirmaciones optimistas de Yann LeCun. Esta solicitud subraya el debate en curso sobre si los modelos JEPA pueden realmente ofrecer el próximo gran avance en modelos del mundo para robótica, desafiando la narrativa dominante y promoviendo un escrutinio más profundo de sus limitaciones en comparación con los LLM y el aprendizaje por refuerzo. El usuario señala específicamente que Yann LeCun a menudo descarta los LLM y el RL mientras promociona JEPA como lo único revolucionario, y quiere identificar posibles banderas rojas que podrían pasarse por alto.

reddit · r/MachineLearning · /u/Amazing-Coat5160 · jul 15, 17:34

**Contexto**: JEPA (Joint-Embedding Predictive Architecture) es un marco de aprendizaje auto-supervisado propuesto por Yann LeCun que se centra en predecir información faltante en un espacio de representación, en lugar de en el espacio de píxeles. Está diseñado para aprender modelos del mundo que permitan a los robots planificar y razonar. LeCun ha sido un defensor vocal, contrastando a menudo JEPA con los LLM y el RL, que según él son insuficientes para alcanzar la inteligencia humana. La comunidad de Reddit está discutiendo si las promesas de JEPA se sostienen bajo un análisis crítico.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://vinesmsuic.github.io/paper-jepa/">JEPA (Joint-Embedding Predictive Architecture) | Vines' Log</a></li>
<li><a href="https://www.turingpost.com/p/jepamap">All JEPA Models : 14 Milestones From I- JEPA to ThinkJEPA</a></li>

</ul>
</details>

**Etiquetas**: `#modelos del mundo`, `#JEPA`, `#robótica`, `#aprendizaje automático`, `#debate crítico`

---

<a id="item-15"></a>
## [Papers with Code lanza página de benchmarks de robótica](https://www.reddit.com/r/MachineLearning/comments/1uxa7ak/all_major_robotics_and_vla_papers_ranked_and/) ⭐️ 7.0/10

Papers with Code ha lanzado una página dedicada de Robótica que recopila los principales benchmarks, artículos en tendencia con código vinculado y artefactos de código abierto para robótica y modelos de Visión-Lenguaje-Acción (VLA). Actualmente, la página incluye más de 110 entradas por benchmark, incluyendo LIBERO, SimplerEnv y RoboTwin. Este centro centralizado estandariza la comparación de modelos robóticos, facilitando a los investigadores seguir el progreso e identificar contribuciones de código abierto. Acelera el desarrollo en IA incorporada al proporcionar una plataforma unificada para evaluaciones y reproducibilidad. La página visualiza las tendencias de rendimiento en cada benchmark a lo largo del tiempo e indica claramente qué modelos son de código abierto versus propietarios. Actualmente cuenta con aproximadamente 110 entradas por benchmark, con planes de añadir más según los comentarios de la comunidad.

reddit · r/MachineLearning · /u/NielsRogge · jul 15, 16:05

**Contexto**: Los modelos de Visión-Lenguaje-Acción (VLA) combinan visión, lenguaje y control robótico para crear políticas robóticas generalistas que pueden seguir instrucciones en lenguaje natural. Benchmarks como LIBERO evalúan el aprendizaje continuo y la transferencia de conocimiento en tareas de manipulación robótica a lo largo de 130 tareas, mientras que SimplerEnv proporciona entornos simulados para reproducir configuraciones robóticas reales para una evaluación escalable.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision–language–action_model">Vision–language–action model - Wikipedia</a></li>
<li><a href="https://libero-project.github.io/main.html">LIBERO – LIBERO</a></li>
<li><a href="https://github.com/simpler-env/SimplerEnv">GitHub - simpler-env/SimplerEnv: Evaluating and reproducing ...</a></li>

</ul>
</details>

**Discusión**: La comunidad de Reddit mostró gran interés, con usuarios elogiando el recurso centralizado y sugiriendo benchmarks y características adicionales. Niels Rogge, el creador, interactuó activamente con los comentarios, prometiendo expandir el repositorio y añadir más entradas.

**Etiquetas**: `#robótica`, `#VLA`, `#benchmarks`, `#Papers with Code`, `#código abierto`

---

<a id="item-16"></a>
## [La alegría perdida de la piratería musical](https://www.pigeonsandplanes.com/read/music-piracy-what-cd-oink-nine-inch-nails-streaming) ⭐️ 6.0/10

Un artículo nostálgico reflexiona sobre cómo la piratería musical solía facilitar la exploración cultural y la conexión social, un papel que los servicios de streaming modernos no han reemplazado por completo. Destaca un cambio cultural del descubrimiento activo de música mediante la piratería al consumo pasivo a través del streaming, afectando la forma en que las personas se relacionan con la música y entre sí. El artículo menciona plataformas como Oink y What.cd y señala que los servicios de streaming no tienen archivos completos, dejando vacíos que la piratería solía llenar.

hackernews · mcgin · jul 16, 04:46 · [Discusión](https://news.ycombinator.com/item?id=48930454)

**Contexto**: En la década de 2000, la piratería musical floreció a través de redes peer-to-peer y trackers privados como Oink y What.cd, ofreciendo vastas bibliotecas que los servicios de streaming luego intentaron replicar. El iPod se convirtió en un dispositivo popular para almacenar música pirateada, creando un fenómeno cultural de colecciones musicales compartidas. Los servicios de streaming como Spotify trajeron conveniencia y legalidad pero limitaron el descubrimiento a través de algoritmos.

**Discusión**: Los comentaristas expresan nostalgia por los aspectos sociales y exploratorios de la piratería musical, citando la pérdida de efectos de red y archivos completos. Algunos señalan la ironía de que el iPod de Apple estuviera diseñado para reproducir música pirateada, y destacan que los servicios de streaming aún carecen de catálogos completos.

**Etiquetas**: `#piratería musical`, `#nostalgia`, `#streaming`, `#descubrimiento musical`, `#iPod`

---

<a id="item-17"></a>
## [FCC derogará el límite de propiedad del 39% en TV](https://arstechnica.com/tech-policy/2026/07/fcc-to-repeal-39-tv-ownership-cap-in-boost-for-trump-friendly-news-orgs/) ⭐️ 6.0/10

El presidente de la FCC anunció planes para derogar el límite de propiedad de estaciones de TV del 39%, un límite establecido por el Congreso que restringe a cualquier entidad a poseer estaciones que alcancen a más del 39% de los hogares con TV en EE.UU. Esta medida podría permitir que grandes empresas de medios, especialmente aquellas alineadas con organizaciones de noticias afines a Trump, expandan su alcance e influencia, reduciendo potencialmente la diversidad mediática. La derogación anularía un límite legal vigente desde 1996, y la FCC afirma tener autoridad para hacerlo sin aprobación del Congreso.

rss · Ars Technica · jul 15, 18:52

**Contexto**: El límite de propiedad del 39% fue parte de la Ley de Telecomunicaciones de 1996, destinado a evitar que una sola cadena domine el mercado. Los partidarios argumentan que el límite está obsoleto en la era del cable e internet, mientras que los opositores advierten que podría llevar a la consolidación y menos programación local.

**Etiquetas**: `#FCC`, `#regulación de medios`, `#propiedad de televisión`, `#política de telecomunicaciones`, `#Trump`

---

<a id="item-18"></a>
## [Presentadores de artículos en ECCV deben pagar tarifa completa de inscripción](https://www.reddit.com/r/MachineLearning/comments/1uxyd6z/why_is_eccv_so_insanely_expensive_for_students/) ⭐️ 6.0/10

Un usuario estudiante de Reddit informa que ECCV exige la tarifa completa de inscripción ($805) para cualquier autor que presente un artículo, y no se permite la inscripción de estudiante ($440) para los presentadores, mientras que sus solicitudes de subvención de viaje y exención fueron rechazadas. Esta política crea una barrera económica para los estudiantes investigadores, potencialmente excluyéndolos de presentar su trabajo en una importante conferencia de visión por computadora, lo que plantea preocupaciones de equidad en la publicación académica. La inscripción temprana para estudiantes es de $440, pero la inscripción completa es de $805, y la publicación indica que incluso con un artículo aceptado, los estudiantes deben pagar la tarifa completa, y las becas de viaje son insuficientes o rechazadas.

reddit · r/MachineLearning · /u/NotGondor · jul 16, 09:55

**Contexto**: ECCV (European Conference on Computer Vision) es una conferencia de primer nivel en visión por computadora que se celebra bienalmente, junto con CVPR e ICCV. Las tarifas de inscripción a conferencias a menudo varían según el estatus, con descuentos para estudiantes, pero algunas conferencias exigen que al menos un autor se inscriba a la tarifa completa por cada artículo aceptado, lo que puede ser costoso para estudiantes sin financiamiento.

**Etiquetas**: `#Aprendizaje automático`, `#Conferencias académicas`, `#ECCV`, `#Estudiantes`, `#Costos de inscripción`

---

<a id="item-19"></a>
## [Modelo PyTorch 170 veces más lento en T4 que en A100; investigación de cuello de botella](https://www.reddit.com/r/MachineLearning/comments/1ux6a9x/pytorch_model_running_170x_slower_on_t4_vs_a100/) ⭐️ 6.0/10

Un usuario reporta que un modelo de seguimiento de puntos que utiliza volúmenes de correlación 4D y transformadores se ejecuta 170 veces más lento en una GPU NVIDIA T4 que en una A100, a pesar de que ambas usan precisión FP32 y la GPU está completamente utilizada. Esta desaceleración extrema resalta el impacto crítico de las diferencias de arquitectura de GPU, especialmente el ancho de banda de memoria y las capacidades de los núcleos tensor, en modelos con volúmenes de correlación 4D y capas transformadoras, comunes en tareas modernas de visión por computadora. La T4 tiene 320 GB/s de ancho de banda de memoria y carece de núcleos tensor para FP32, mientras que la A100 tiene 1,555 GB/s y potentes núcleos tensor. El volumen de correlación 4D implica accesos a memoria O(N^2), probablemente causando un cuello de botella de ancho de banda que la A100 maneja mucho mejor.

reddit · r/MachineLearning · /u/Future-Structure-296 · jul 15, 13:44

**Contexto**: La T4 (arquitectura Turing) es una GPU más antigua diseñada para inferencia con 16 GB de memoria GDDR6 y 320 GB/s de ancho de banda, mientras que la A100 (Ampere) es una GPU de centro de datos con 80 GB de memoria HBM2e y 1,555 GB/s de ancho de banda. El volumen de correlación 4D calcula similitudes por pares entre mapas de características, lo que resulta en grandes huellas de memoria y tráfico intenso de memoria, beneficiándose enormemente del mayor ancho de banda y eficiencia de los núcleos tensor de la A100.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://deploybase.ai/articles/tesla-t4-vs-a100">Tesla T4 vs A100: Budget GPU Inference vs Production Performance</a></li>
<li><a href="https://gpuperhour.com/compare/t4-vs-a100">T4 vs A100: 38.5x FP16 Gap, 80GB vs 16GB | GPUPerHour</a></li>
<li><a href="https://arxiv.org/html/2407.15420">Local All-Pair Correspondence for Point Tracking</a></li>

</ul>
</details>

**Etiquetas**: `#PyTorch`, `#A100`, `#T4`, `#Rendimiento GPU`, `#Depuración`

---

<a id="item-20"></a>
## [Revisiones de NeurIPS esperadas para el 22 de julio, surgen especulaciones](https://www.reddit.com/r/MachineLearning/comments/1ux8p0a/neurips_reviews_coming_in_soon_d/) ⭐️ 6.0/10

Un usuario de Reddit especula que las decisiones de revisión de NeurIPS 2025 se publicarán el 22 de julio a las 5:30 pm AoE, basándose en rumores en redes sociales. NeurIPS es una de las conferencias más importantes de aprendizaje automático, por lo que la publicación de las revisiones es crucial para miles de investigadores que esperan decisiones sobre sus trabajos. La fecha y hora son especulativas y no están confirmadas oficialmente; la zona horaria AoE asegura cobertura global. La publicación invita a discutir a autores, revisores y participantes de talleres.

reddit · r/MachineLearning · /u/Practical-Buddy6323 · jul 15, 15:13

**Contexto**: NeurIPS (Conferencia sobre Sistemas de Procesamiento de Información Neural) es una prestigiosa conferencia anual sobre aprendizaje automático e inteligencia artificial. Utiliza un proceso de revisión por pares donde los trabajos reciben evaluaciones de expertos, y las decisiones se publican antes de la conferencia. La comunidad espera con entusiasmo los resultados para planificar sus próximos pasos.

**Etiquetas**: `#conferencia`, `#aprendizaje automático`, `#revisión por pares`, `#NeurIPS`, `#comunidad`

---