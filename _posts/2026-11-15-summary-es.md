---
layout: default
title: "Horizon Summary: 2026-11-15 (ES)"
date: 2026-11-15
lang: es
---

> De 25 artículos, 18 fueron seleccionados por relevancia

---

1. [SpaceX atrapa la Starship al finalizar el vuelo 15](#item-1) ⭐️ 10.0/10
2. [Apps de Lovable exponen datos de pasaporte y más de 200K mensajes privados](#item-2) ⭐️ 9.0/10
3. [Tribunal niega desestimar caso de fijación de precios de DRAM](#item-3) ⭐️ 8.0/10
4. [PyPI lanza páginas de proyecto rediseñadas con señales de seguridad claras](#item-4) ⭐️ 8.0/10
5. [Benchmark: PocketBase + SQLite en VPS de $4/mes logra 1,420 RPS con WAL y Litestream](#item-5) ⭐️ 8.0/10
6. [Cómo Wozniak programó a mano el BASIC del Apple I sin hardware](#item-6) ⭐️ 7.0/10
7. [Documental de KDE celebra la historia y comunidad del escritorio de software libre](#item-7) ⭐️ 7.0/10
8. [Un árbol genealógico de los títulos laborales en software](#item-8) ⭐️ 7.0/10
9. [datasette-llm 0.1a11 añade soporte para endpoints compatibles con OpenAI](#item-9) ⭐️ 7.0/10
10. [Infisical limita roles personalizados a Enterprise para autohospedados en parche](#item-10) ⭐️ 7.0/10
11. [Una lista de mis juegos modernos favoritos para NES](#item-11) ⭐️ 6.0/10
12. [datasette-vega 0.7: plugin de gráficos Vega-Lite actualizado para Datasette y Datasette Lite](#item-12) ⭐️ 6.0/10
13. [Juegos en la nube autogestionados en AWS: experiencia y desafíos](#item-13) ⭐️ 6.0/10
14. [Usuario pregunta si pixelserv-tls sigue evitando la detección de bloqueadores en 2026](#item-14) ⭐️ 5.0/10
15. [8 meses usando un MacBook Pro 2014 como servidor casero y sus mejoras](#item-15) ⭐️ 5.0/10
16. [Inkheart 1.5 - Renovación de interfaz, búsqueda de texto completo y pestañas de documentos múltiples](#item-16) ⭐️ 5.0/10
17. [Usuario busca cliente de correo web con notificaciones en tiempo real](#item-17) ⭐️ 5.0/10
18. [Plan para recuperación segura de bóveda Bitwarden autohospedada tras pérdida total](#item-18) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [SpaceX atrapa la Starship al finalizar el vuelo 15](https://www.spacex.com/launches/starship-flight-15) ⭐️ 10.0/10

SpaceX logró atrapar la nave Starship al finalizar el vuelo 15, un hito crucial hacia la reutilización completa del sistema de lanzamiento.

hackernews · ls612 · nov 14, 21:22 · [Discusión](https://news.ycombinator.com/item?id=50500963)

**Etiquetas**: `#SpaceX`, `#Starship`, `#Cohetes reutilizables`, `#Exploración espacial`, `#Ingeniería aeroespacial`

---

<a id="item-2"></a>
## [Apps de Lovable exponen datos de pasaporte y más de 200K mensajes privados](https://www.crissyfield.de/research/lovable-en/) ⭐️ 9.0/10

Una investigación de seguridad revela que aplicaciones creadas con Lovable, un constructor de aplicaciones con IA, están filtrando datos personales sensibles—incluidos detalles de pasaporte y más de 200.000 mensajes privados—debido a configuraciones incorrectas de Row-Level Security (RLS) en Supabase. Esto pone de manifiesto un grave riesgo de seguridad en el código generado por IA: los usuarios que despliegan estas aplicaciones pueden exponer datos sensibles sin saberlo, lo que afecta la privacidad, el cumplimiento normativo y la confianza en las plataformas low-code/no-code. La causa raíz son políticas de Row-Level Security insuficientes o ausentes en la base de datos Supabase subyacente; según la discusión, Lovable escanea las aplicaciones en busca de estos problemas y ofrece correcciones automáticas, pero las implementaciones mal configuradas siguen siendo accesibles mediante una simple inspección de red en el navegador.

hackernews · armcat · nov 14, 17:43 · [Discusión](https://news.ycombinator.com/item?id=50499017)

**Contexto**: Row-Level Security (RLS) es una característica de PostgreSQL que restringe qué filas puede ver un usuario según su identidad o atributos. Supabase, una plataforma backend construida sobre PostgreSQL, utiliza RLS para proteger tablas en esquemas expuestos, pero los desarrolladores deben crear políticas explícitamente. Lovable es un constructor de aplicaciones con IA que genera aplicaciones full-stack con un backend de Supabase, y el código generado a menudo carece de RLS adecuado por defecto. Esta vulnerabilidad surge cuando esas aplicaciones se despliegan sin controles de acceso seguros.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://supabase.com/docs/guides/database/postgres/row-level-security">Row Level Security | Supabase Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Row_level_security">Row level security</a></li>

</ul>
</details>

**Discusión**: Los comentarios reflejan una mezcla de opiniones. El autor del blog y varios usuarios sugieren que el problema es evidente y señalan que las decisiones previas de Supabase para facilitar la incorporación contribuyeron al riesgo. El Jefe de Seguridad de Lovable responde que su plataforma escanea en busca de problemas de RLS y puede corregirlos automáticamente, mientras otros argumentan que las aplicaciones generadas por IA son objetivos fáciles y que las plataformas deberían adoptar seguridad de base de datos denegar por defecto.

**Etiquetas**: `#seguridad`, `#aplicaciones generadas por IA`, `#Supabase`, `#fuga de datos`, `#Row-Level Security`

---

<a id="item-3"></a>
## [Tribunal niega desestimar caso de fijación de precios de DRAM](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal) ⭐️ 8.0/10

Un tribunal denegó una moción de desestimación en la demanda por fijación de precios de DRAM contra Samsung, SK Hynix y Micron, permitiendo que las reclamaciones antimonopolio avancen. La decisión permite que una importante demanda antimonopolio contra los tres principales proveedores de DRAM siga adelante, lo que podría afectar los precios mundiales de la memoria y las prácticas de la industria en un mercado ya tensado por la demanda de IA. La sentencia no determina culpabilidad; solo permite que el caso avance más allá de la fase de moción de desestimación. Las tres empresas controlan la gran mayoría del mercado mundial de DRAM.

hackernews · ybathaee · nov 15, 01:18 · [Discusión](https://news.ycombinator.com/item?id=50502988)

**Contexto**: La DRAM (memoria dinámica de acceso aleatorio) es un tipo de memoria semiconductora volátil utilizada como memoria principal en computadoras y tarjetas gráficas. Samsung, SK Hynix y Micron son los tres principales proveedores mundiales de chips de DRAM. En los últimos años, los precios de la DRAM han aumentado considerablemente debido a la alta demanda de aplicaciones de IA, en particular de memoria de alto ancho de banda (HBM), lo que ha reducido la producción de DRAM estándar.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DRAM">DRAM</a></li>

</ul>
</details>

**Discusión**: Los miembros de la comunidad expresaron frustración por los altos precios de la RAM, y algunos sospechan firmemente de colusión entre los tres fabricantes de DRAM y piden intervención regulatoria. Otros se mostraron más escépticos y señalaron que las mejoras tecnológicas como el paso de DDR4 a DDR5 y la competencia de fabricantes chinos podrían explicar la dinámica del mercado. Varios comentaristas esperan que el juicio revele pruebas, aunque reconocen que la colusión es plausible pero no está probada.

**Etiquetas**: `#DRAM`, `#fijación de precios`, `#antimonopolio`, `#semiconductores`, `#litigios tecnológicos`

---

<a id="item-4"></a>
## [PyPI lanza páginas de proyecto rediseñadas con señales de seguridad claras](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 8.0/10

PyPI ha completado una actualización de su interfaz que rediseña las páginas de proyecto para mostrar de forma destacada señales de seguridad, como la procedencia y la publicación de confianza, facilitando a los usuarios evaluar la fiabilidad de los paquetes. Esta mejora fortalece la cadena de suministro de software de Python al hacer más visibles la procedencia y las señales de confianza, lo que ayuda a los desarrolladores a evitar paquetes maliciosos o comprometidos y fomenta la adopción de prácticas de publicación seguras. Las nuevas páginas destacan señales como la publicación de confianza (basada en OIDC y sin claves) y las atestaciones de procedencia (p. ej., SLSA o sigstore), pero estas señales detectan cuentas comprometidas en lugar de proyectos maliciosos desde su origen.

hackernews · rbanffy · nov 14, 15:40 · [Discusión](https://news.ycombinator.com/item?id=50497892)

**Contexto**: PyPI es el repositorio oficial de paquetes de Python, con más de 500.000 proyectos, y es la fuente predeterminada del gestor de paquetes pip. La seguridad de la cadena de suministro busca garantizar que los paquetes no hayan sido alterados entre el código fuente y la instalación. La firma de código y las atestaciones de procedencia utilizan criptografía para verificar el origen y la integridad del software. El rediseño de PyPI muestra esta información directamente en las páginas de proyecto.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PyPI">PyPI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code_signing">Code signing</a></li>

</ul>
</details>

**Discusión**: La comunidad acoge en general la mejora, valorando la visibilidad de la procedencia, pero algunos usuarios temen que la confianza se centralice en los grandes proveedores de CI en la nube y que las señales solo detecten cuentas comprometidas, no paquetes maliciosos desde el principio. Otros piden soporte para flujos de trabajo reutilizables en la publicación de confianza y una adopción más amplia de la firma sin claves.

**Etiquetas**: `#seguridad`, `#PyPI`, `#Python`, `#cadena de suministro`, `#firma de código`

---

<a id="item-5"></a>
## [Benchmark: PocketBase + SQLite en VPS de $4/mes logra 1,420 RPS con WAL y Litestream](https://www.reddit.com/r/selfhosted/comments/1xwq1ly/benchmarking_pocketbase_sqlite_on_a_4mo_hetzner/) ⭐️ 8.0/10

Un desarrollador evaluó una configuración de PocketBase + SQLite en un VPS Hetzner CX22 de $4 al mes, logrando 1.420 solicitudes por segundo con latencia P99 inferior a 8 ms usando modo WAL y ajustes de PRAGMA. La configuración incluye Litestream transmitiendo los marcos WAL de SQLite a Cloudflare R2 para recuperación continua ante desastres con un RPO inferior a 1 segundo. Esto demuestra que un backend SQLite autoalojado puede manejar cargas de trabajo con predominio de lecturas a nivel de producción por una fracción del costo de PostgreSQL administrado, reduciendo la latencia al eliminar los saltos de red y simplificando el despliegue. Es especialmente relevante para desarrolladores independientes y entusiastas del autoalojamiento que buscan evitar costosos servicios de bases de datos administradas. El benchmark utilizó k6 con 200 usuarios concurrentes, atacando endpoints de lectura autenticados y logrando 100% de estado 200, latencia media de 2,84 ms y P95 de 5,2 ms. Los ajustes clave de PRAGMA de SQLite incluyen modo WAL, synchronous=NORMAL, busy_timeout=5000, cache_size de 64 MB, mmap_size de 256 MB y temp_store=MEMORY; Litestream transmite a Cloudflare R2 con intervalo de sincronización de 1 segundo y retención de 30 días.

reddit · r/selfhosted · /u/NikShiP · nov 15, 08:07

**Contexto**: PocketBase es un backend autoalojado de código abierto que ofrece una base de datos SQLite en tiempo real, autenticación, almacenamiento de archivos y un panel de administración en un solo ejecutable. El modo Write-Ahead Logging (WAL) de SQLite permite lecturas concurrentes durante las escrituras, mejorando la concurrencia para cargas con predominio de lecturas. Litestream es una herramienta que replica continuamente bases de datos SQLite a almacenamiento de objetos como S3 o Cloudflare R2, permitiendo la recuperación a un punto en el tiempo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://pocketbase.io/">PocketBase - Open Source backend in 1 file</a></li>
<li><a href="https://litestream.io/docs/">Litestream replicates SQLite databases in real-time to S3.</a></li>
<li><a href="https://sqlite.org/wal.html">Write-Ahead Logging - SQLite</a></li>

</ul>
</details>

**Etiquetas**: `#PocketBase`, `#SQLite`, `#rendimiento`, `#autoalojamiento`, `#respaldo`

---

<a id="item-6"></a>
## [Cómo Wozniak programó a mano el BASIC del Apple I sin hardware](https://retrocomputing.stackexchange.com/questions/17957) ⭐️ 7.0/10

El artículo explica que Steve Wozniak escribió a mano el intérprete BASIC del Apple I en ensamblador del 6502 en papel antes de tener una computadora funcional, una práctica común entre aficionados en los años setenta. Los miembros de la comunidad describen cómo ellos también escribían código ensamblador a mano, memorizaban códigos de operación y probaban los programas directamente en el hardware objetivo. Esto ilustra cómo los pioneros de los microcomputadores trabajaban sin herramientas modernas de desarrollo, confiando en un profundo conocimiento del hardware. Proporciona contexto histórico para la retrocomputación y destaca la simplicidad de los conjuntos de instrucciones de 8 bits frente a los procesadores modernos. El Integer BASIC de Wozniak fue escrito para el 6502, usaba solo enteros por velocidad y luego se incluyó en la ROM del Apple II. El ensamblado a mano requería conocer valores hexadecimales de códigos de operación como A9 para LDA, y el código se ingresaba a menudo mediante un monitor de lenguaje de máquina.

hackernews · Skyfall106 · nov 14, 22:22 · [Discusión](https://news.ycombinator.com/item?id=50501594)

**Contexto**: El lenguaje ensamblador es una representación legible por humanos del código de máquina, donde cada instrucción corresponde a un código de operación binario. El MOS Technology 6502 era un microprocesador de 8 bits económico y popular en las primeras computadoras domésticas. Antes de que los ensambladores estuvieran ampliamente disponibles, los programadores a veces traducían los mnemónicos a código de máquina a mano. Steve Wozniak diseñó la Apple I en 1976 y escribió su intérprete BASIC para facilitar la programación.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_BASIC">Apple BASIC</a></li>
<li><a href="https://en.wikipedia.org/wiki/MOS_Technology_6502">MOS Technology 6502 - Wikipedia</a></li>
<li><a href="https://techarya.net/embedded-systems/internals/11-hand-assembly">Hand-Assembly — Turning Mnemonics Into Machine Code With Just ...</a></li>

</ul>
</details>

**Discusión**: Los comentaristas coinciden en gran medida en que escribir ensamblador a mano era una práctica predeterminada para los aficionados a las computadoras de 8 bits debido al costo y la falta de herramientas, y que los códigos de operación del 6502 se memorizaban con la práctica. Algunos señalan el uso de formularios en papel o secciones de código impresas para depurar. Una pregunta de seguimiento plantea incertidumbre sobre cómo Wozniak transfirió el intérprete escrito a mano a la ROM, lo que sugiere que la discusión no aborda por completo la brecha del papel al silicio.

**Etiquetas**: `#retrocomputación`, `#programación en ensamblador`, `#historia de la computación`, `#Steve Wozniak`, `#BASIC`

---

<a id="item-7"></a>
## [Documental de KDE celebra la historia y comunidad del escritorio de software libre](https://tube.kockatoo.org/w/fFinNHfanLT7aBEb2B8y4c) ⭐️ 7.0/10

Se ha publicado un video documental sobre el entorno de escritorio KDE, que ofrece una mirada profunda a su historia, desarrollo y logros comunitarios. Este documental destaca el papel de KDE como proyecto de escritorio de código abierto emblemático, mostrando cómo un esfuerzo impulsado por la comunidad puede competir con gigantes propietarios como Microsoft y Apple mientras defiende la libertad del usuario y la personalización. El video está disponible en la URL proporcionada y celebra los hitos de KDE, su evolución técnica (incluida su base en C++/Qt) y el espíritu colaborativo que ha sostenido el proyecto durante décadas. No se ofrecen detalles específicos de producción, pero el documental se presenta como un homenaje a la comunidad KDE.

hackernews · mrkn1 · nov 14, 13:43 · [Discusión](https://news.ycombinator.com/item?id=50496976)

**Contexto**: KDE es una comunidad internacional de software libre que desarrolla un entorno de escritorio gráfico (Plasma), frameworks y una serie de aplicaciones como Krita y Kdenlive. Comenzó a mediados de los años 1990 como un esfuerzo para crear un escritorio para Unix utilizando el toolkit Qt, y desde entonces se ha convertido en uno de los entornos de escritorio Linux más populares, conocido por su personalización y rendimiento. El proyecto está representado legalmente por KDE e.V. en Alemania y es utilizado por organizaciones como la NASA y el CERN.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KDE">KDE</a></li>
<li><a href="https://kde.org/">Home - KDE Community</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad son abrumadoramente positivos: los usuarios expresan admiración por el rendimiento de KDE, su flexibilidad de diseño y el logro de competir con grandes corporaciones. Varios usuarios comparten recuerdos personales, desde los primeros anuncios en Usenet hasta usar KDE durante años, y uno destaca los desafíos de escribir software de escritorio en C++. Algunos mencionan inestabilidad histórica (por ejemplo, KDE 4), pero en general el sentimiento es de gratitud y entusiasmo por los 30 años del proyecto.

**Etiquetas**: `#KDE`, `#Linux`, `#software libre`, `#documental`, `#escritorio`

---

<a id="item-8"></a>
## [Un árbol genealógico de los títulos laborales en software](https://zwischenzugs.com/2026/11/03/a-family-tree-of-software-job-titles/) ⭐️ 7.0/10

La entrada de blog presenta un análisis genealógico de los títulos laborales en software, mostrando cómo roles como Desarrollador, Ingeniero, DevOps e Ingeniero de Confiabilidad del Sitio han evolucionado y se han diversificado. Ha provocado un amplio debate sobre si estos títulos aún conservan un significado claro. Los títulos laborales influyen en la contratación, la negociación salarial y la identidad profesional, por lo que la ambigüedad puede generar expectativas desalineadas y fricciones en la carrera. A medida que metodologías como Agile y DevOps cambian o decaen, comprender la evolución de los títulos ayuda a los profesionales a navegar un mercado laboral cada vez más fragmentado. El artículo usa una metáfora de árbol genealógico para mostrar el linaje y la ramificación entre roles. Los comentarios de la comunidad destacan que títulos como Ingeniero DevOps, SRE y Scrum Master a menudo significan cosas distintas según la organización y la región, y algunos profesionales los consideran vacíos u obsoletos.

hackernews · umerf · nov 14, 17:45 · [Discusión](https://news.ycombinator.com/item?id=50499038)

**Contexto**: Los títulos laborales en software se han multiplicado más allá de 'programador' para incluir roles especializados como Ingeniero DevOps, Ingeniero de Confiabilidad del Sitio (SRE) y Scrum Master. Estos títulos a menudo reflejan prácticas organizativas más que habilidades estandarizadas, lo que genera definiciones inconsistentes. La metáfora del árbol genealógico sugiere que los títulos comparten ancestros comunes y han divergido con el tiempo, de forma similar a la taxonomía biológica.

**Discusión**: Los comentaristas coinciden en general en que muchos títulos laborales en software han perdido un significado concreto, citando a DevOps y SRE como especialmente inconsistentes entre empresas. Un comentarista señala que los títulos son específicos de cada cultura, como en Japón, donde 'ingeniero de software' puede estar infravalorado. Otros recomiendan eliminar certificaciones obsoletas como Scrum Master, mientras que algunos señalan que el mismo título puede significar cosas completamente distintas según el contexto.

**Etiquetas**: `#títulos laborales`, `#cultura organizacional`, `#desarrollo de software`, `#carrera profesional`, `#comunidad tecnológica`

---

<a id="item-9"></a>
## [datasette-llm 0.1a11 añade soporte para endpoints compatibles con OpenAI](https://simonwillison.net/2026/Nov/14/datasette-llm/) ⭐️ 7.0/10

El lanzamiento de datasette-llm 0.1a11 incorpora soporte para endpoints compatibles con OpenAI, lo que permite a Datasette utilizar LLMs alojados en servicios como LM Studio, Ollama y llama.cpp, incluidos modelos locales. Esto permite a los desarrolladores ejecutar Datasette con modelos de lenguaje alojados localmente, lo que mejora la privacidad, reduce la latencia y posibilita el uso sin conexión, aprovechando el ecosistema existente compatible con OpenAI. La configuración se realiza mediante la clave plugins.datasette-llm.default_model, que acepta un objeto JSON con los campos model, model_name y api_base; el ejemplo incluido utiliza el modelo Qwen 3.8-27b a través de LM Studio en http://localhost:1234/v1 y se ejecuta con uvx junto a datasette-agent.

rss · Simon Willison · nov 14, 23:59

**Contexto**: Datasette es una herramienta de código abierto para explorar y publicar datos como sitios web interactivos y API. El plugin datasette-llm actúa como intermediario para configurar modelos de lenguaje que pueden ser utilizados por otros plugins de Datasette, como datasette-agent. Los endpoints compatibles con OpenAI son APIs web que siguen el protocolo de la API de OpenAI, lo que permite la interoperabilidad con herramientas diseñadas para OpenAI. Aplicaciones como LM Studio, Ollama y llama.cpp exponen estos endpoints para ejecutar modelos localmente.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/LM_Studio">LM Studio - Wikipedia</a></li>
<li><a href="https://restfulapi.net/openai-compatible-api/">What Is an OpenAI-Compatible API? Endpoints and Pitfalls</a></li>

</ul>
</details>

**Etiquetas**: `#Datasette`, `#LLMs`, `#OpenAI`, `#modelos locales`, `#herramientas de desarrollo`

---

<a id="item-10"></a>
## [Infisical limita roles personalizados a Enterprise para autohospedados en parche](https://www.reddit.com/r/selfhosted/comments/1xwoq7y/infisical_paywalled_custom_roles_for_selfhosters/) ⭐️ 7.0/10

Infisical incorporó un commit el 1 de abril titulado 'feat: custom roles as enterprise-only feature' (e4880e71ed) y lo lanzó en la versión de parche v0.159.6; luego actualizó la documentación en junio (PR #7078). Los usuarios autohospedados con plan gratuito ya no pueden crear nuevos roles personalizados ni editar los existentes, aunque los roles creados anteriormente siguen funcionando. Esto elimina una función crítica de mínimo privilegio en los despliegues autohospedados gratuitos, obligando a los usuarios a otorgar acceso total de 'Miembro' o pagar por Enterprise, una elección inaceptable para un gestor de secretos. La medida ha provocado rechazo en la comunidad y puede dañar la confianza en las credenciales de código abierto de Infisical. La restricción se aplica en el código, como muestra el mensaje de error: 'Failed to update custom role due to plan RBAC restriction. Upgrade to Infisical Enterprise plan to update custom roles.' Los roles existentes siguen funcionando pero no se pueden modificar; el cambio fue desencadenado inicialmente por el bot de dependencias Renovate al actualizar la instancia.

reddit · r/selfhosted · /u/Agreeable_Repeat_568 · nov 15, 06:46

**Contexto**: Infisical es una plataforma de gestión de secretos de código abierto (licencia MIT) con opciones autohospedadas y en la nube. El control de acceso basado en roles (RBAC) permite a los administradores definir roles personalizados con permisos específicos, como acceso solo de creación para automatizaciones. Las versiones de parche suelen ser actualizaciones menores que no deberían introducir eliminaciones importantes de funciones. Renovate es una herramienta que actualiza automáticamente las dependencias de un proyecto, lo que puede incorporar inadvertidamente cambios disruptivos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/Infisical">Infisical</a></li>
<li><a href="https://en.wikipedia.org/wiki/RBAC">RBAC</a></li>
<li><a href="https://grokipedia.com/page/Renovate_software">Renovate (software)</a></li>

</ul>
</details>

**Etiquetas**: `#Infisical`, `#autohospedaje`, `#gestión de secretos`, `#código abierto`, `#licencias`

---

<a id="item-11"></a>
## [Una lista de mis juegos modernos favoritos para NES](https://jordi.inversethought.com/blog/25-of-my-favourite-modern-nes-games/) ⭐️ 6.0/10

El autor publicó una selección personal de juegos modernos desarrollados para la Nintendo Entertainment System, mostrando títulos homebrew recientes para la clásica consola de 8 bits. Esto resalta una comunidad homebrew activa y demuestra que las herramientas de desarrollo mejoradas están haciendo que la creación de juegos para NES sea más accesible que nunca, lo que podría atraer a nuevos desarrolladores a plataformas retro. El artículo en sí es una lista personal sin especificaciones técnicas, pero la discusión adjunta hace referencia a la charla de Frank Cigaldi de 2019 sobre el uso continuado de la NES y señala que las herramientas modernas han reducido significativamente la barrera de entrada.

hackernews · jordigh · nov 15, 02:41 · [Discusión](https://news.ycombinator.com/item?id=50503465)

**Contexto**: La NES (Nintendo Entertainment System) es una consola de 8 bits lanzada en 1985. El término homebrew se refiere al software no oficial creado por aficionados para consolas propietarias, que normalmente requiere eludir restricciones de hardware. Hoy en día, las cadenas de herramientas mantenidas por la comunidad y los emuladores permiten a los desarrolladores crear y probar nuevos juegos de NES con más facilidad que en el pasado.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homebrew_(video_games)">Homebrew (video games)</a></li>

</ul>
</details>

**Discusión**: Los comentaristas expresaron entusiasmo y nostalgia, y algunos se sorprendieron de que existan juegos modernos para NES. Destacaron la importancia de las herramientas mejoradas, hicieron referencia a la charla de Frank Cigaldi sobre la longevidad de la plataforma y compartieron anécdotas personales sobre coleccionar juegos retro.

**Etiquetas**: `#videojuegos retro`, `#NES`, `#desarrollo de juegos`, `#homebrew`, `#hardware antiguo`

---

<a id="item-12"></a>
## [datasette-vega 0.7: plugin de gráficos Vega-Lite actualizado para Datasette y Datasette Lite](https://simonwillison.net/2026/Nov/14/datasette-vega/) ⭐️ 6.0/10

Simon Willison lanzó datasette-vega 0.7, un plugin para renderizar gráficos Vega-Lite a partir de tablas o resultados de consultas personalizadas en Datasette. Es la primera versión desde julio de 2018 y añade compatibilidad con las últimas alphas de Datasette y ajustes cosméticos para Datasette Lite. Esta versión reactiva un plugin de visualización que llevaba años sin actualizarse y lo hace utilizable directamente en el navegador mediante Datasette Lite, que ahora admite plugins de JavaScript. Amplía la exploración de datos y la creación de gráficos sin servidor para los usuarios de Datasette. El plugin usa Vega-Lite, una gramática de alto nivel para gráficos interactivos, y funciona tanto en vistas de tabla como en consultas SQL personalizadas. La demo en vivo del README ahora enlaza a una instancia de Datasette Lite que muestra un gráfico de barras con datos de seguridad aérea y opciones de gráfico configurables.

rss · Simon Willison · nov 14, 17:09

**Contexto**: Datasette es una herramienta de código abierto para explorar y publicar datos como un sitio web interactivo y una API. Vega-Lite es una gramática concisa para crear visualizaciones comunes que se compila a especificaciones Vega. Datasette Lite es Datasette empaquetado con WebAssembly para que se ejecute completamente en el navegador sin un servidor Python. Los plugins amplían Datasette con funcionalidades adicionales, como la creación de gráficos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://vega.github.io/vega-lite/">A High-Level Grammar of Interactive Graphics | Vega - Lite</a></li>
<li><a href="https://lite.datasette.io/">Datasette</a></li>

</ul>
</details>

**Etiquetas**: `#Datasette`, `#Visualización de datos`, `#Vega-Lite`, `#Plugins`, `#Datasette Lite`

---

<a id="item-13"></a>
## [Juegos en la nube autogestionados en AWS: experiencia y desafíos](https://www.reddit.com/r/selfhosted/comments/1xw5bj6/anyone_running_their_own_cloud_gaming_pc_on_aws/) ⭐️ 6.0/10

Un usuario de self-hosting detalla cómo ejecuta un PC de juegos en la nube en instancias spot de AWS con GPU por 0,25–0,35 USD/hora, usando Sunshine + Moonlight a través de Tailscale y Steam con Proton. Reporta costos más bajos de lo esperado, pero enfrentó desafíos con apagado automático, disponibilidad spot, cuotas de GPU y almacenamiento persistente, y pregunta si otros usarían una herramienta de automatización. Esto resalta las ventajas e inconvenientes de los juegos en la nube autogestionados frente a servicios comerciales como GeForce NOW: las configuraciones propias en AWS pueden ser más baratas y flexibles, pero requieren controles de costos, planificación de capacidad spot y gestión de cuotas. Si una herramienta de automatización reduce esas barreras, podría hacer los juegos en la nube más accesibles para los autohospedadores y desafiar a las plataformas centralizadas. La configuración técnica incluye Sunshine (anfitrión de streaming de juegos autohospedado) con el cliente Moonlight, conectados mediante la VPN mallada Tailscale; los juegos se ejecutan en Linux usando la capa de compatibilidad Proton para títulos de Windows. El precio de las instancias spot es de 0,25–0,35 USD/hora, pero el usuario señala que la máquina debe apagarse automáticamente de forma fiable y que la capacidad spot de GPU puede no estar disponible en horas pico en su región.

reddit · r/selfhosted · /u/rememberyouandme · nov 14, 15:37

**Contexto**: Sunshine es un servidor de streaming de juegos autohospedado y de código abierto que funciona con el cliente Moonlight para transmitir juegos de PC a otros dispositivos a través de una red. Tailscale proporciona una VPN de configuración cero que crea una red mallada privada, permitiendo acceso remoto seguro a la instancia de juegos. Proton es una capa de compatibilidad desarrollada por Valve que permite ejecutar muchos juegos de Windows en Linux, lo cual es necesario para usar Steam en una instancia de AWS basada en Linux. Las instancias spot de AWS ofrecen capacidad EC2 no utilizada a precios reducidos y variables, pero pueden interrumpirse o no estar disponibles.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://sunshine.lizardbyte.dev/">Sunshine — Your games. Your hardware. Every screen.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tailscale">Tailscale - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proton_(software)">Proton (software) - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#juegos en la nube`, `#self-hosting`, `#AWS`, `#GPU`, `#infraestructura`

---

<a id="item-14"></a>
## [Usuario pregunta si pixelserv-tls sigue evitando la detección de bloqueadores en 2026](https://www.reddit.com/r/selfhosted/comments/1xwppd4/pixelserv_question/) ⭐️ 5.0/10

Un usuario de Reddit que utiliza Unbound con listas de bloqueo de oisd.nl informa ver banners de «detectamos un bloqueador de anuncios» y pregunta si pixelserv-tls, que sirve imágenes de reemplazo de 1 píxel localmente, sigue funcionando en 2026; también pide otros consejos para bloqueo de anuncios a nivel de red. Esto refleja los desafíos actuales del bloqueo de anuncios basado en DNS autoalojado a medida que los sitios web mejoran la detección, lo que resalta la necesidad de técnicas que evolucionen para preservar la privacidad y la experiencia del usuario sin interrupciones. El usuario utiliza el DNS Unbound con listas de bloqueo de oisd.nl y ocasionalmente se encuentra con avisos de bloqueador de anuncios; pixelserv-tls es un servidor HTTP/1.1 mínimo que sirve un píxel de 1x1 y admite TLSv1.0/1.2/1.3, pero los resultados de búsqueda no incluyen pruebas recientes que confirmen su eficacia en 2026.

reddit · r/selfhosted · /u/toakao · nov 15, 07:46

**Contexto**: Unbound es un resolutor DNS validador, recursivo y con caché que a menudo se usa para bloqueo de anuncios a nivel de red consultando listas de bloqueo como oisd.nl. Cuando se bloquea un dominio, el resolutor puede devolver una dirección sumidero, y pixelserv-tls normalmente se ejecuta en esa IP para servir un píxel diminuto y certificados TLS válidos para los dominios bloqueados, lo que reduce la detección del bloqueador. oisd.nl proporciona listas de bloqueo de dominios de anuncios y rastreadores mantenidas por la comunidad. La pregunta del usuario surge porque la detección moderna de bloqueadores puede detectar recursos faltantes a pesar de la respuesta con píxel, como sugieren sus sesiones de chat con IA, pero no se encontró un punto de referencia actual definitivo en los resultados de búsqueda.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/kvic-z/pixelserv-tls">GitHub - kvic-z/ pixelserv - tls : A tiny bespoke HTTP/1.1 server for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unbound_(DNS_server)">Unbound (DNS server)</a></li>
<li><a href="https://blockmeter.io/de/blocklists/">DNS-Blocklisten erklärt: HaGeZi vs. OISD , welche Stufe, URLs für...</a></li>

</ul>
</details>

**Etiquetas**: `#selfhosted`, `#bloqueo de anuncios`, `#DNS`, `#privacidad`, `#filtrado de red`

---

<a id="item-15"></a>
## [8 meses usando un MacBook Pro 2014 como servidor casero y sus mejoras](https://www.reddit.com/r/selfhosted/comments/1xwiwtq/8_months_of_running_a_2014_macbook_pro_as_a_home/) ⭐️ 5.0/10

El autor comparte una actualización de 8 meses sobre el uso de un MacBook Pro 2014 como servidor casero, detallando mejoras como cambiar de Wi-Fi a Ethernet para una transmisión más rápida en Plex, añadir Pi-hole para bloquear anuncios en toda la red y establecer una rutina mensual de actualizaciones de seguridad tras los recientes exploits de Plex. Esto demuestra un enfoque práctico y de bajo costo para reutilizar hardware antiguo en servicios autoalojados como Plex y Pi-hole, lo cual es relevante para la comunidad de autoalojamiento; destaca problemas comunes (buffering, seguridad) y soluciones que otros pueden aprender. Las mejoras específicas incluyen pasar de Wi-Fi a Ethernet para transferencias de archivos 10 veces más rápidas y solucionar el buffering de 4K en Plex, planear reemplazar discos de 10 años por dos discos de 4TB (uno para copia de seguridad) pero retrasarlo por el aumento de precios, y desactivar el reenvío de puertos, UPnP y acceso remoto de Plex en favor de Tailscale para acceso remoto.

reddit · r/selfhosted · /u/williamsburg_psycho · nov 15, 01:28

**Contexto**: Plex es una aplicación de servidor de medios que permite transmitir colecciones de medios personales a varios dispositivos. Pi-hole es un bloqueador de anuncios a nivel de red que funciona como un sumidero de DNS, filtrando anuncios y rastreadores en todos los dispositivos de la red. Miniflux es un lector de feeds RSS minimalista y autoalojado. El usuario también utiliza Tailscale, un servicio VPN que simplifica el acceso remoto seguro a servidores caseros sin abrir puertos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pi-hole">Pi-hole</a></li>
<li><a href="https://miniflux.app/">Miniflux - Minimalist and Opinionated Feed Reader</a></li>
<li><a href="https://en.wikipedia.org/wiki/Plex">Plex</a></li>

</ul>
</details>

**Etiquetas**: `#servidor casero`, `#autoalojamiento`, `#Plex`, `#Pi-hole`, `#seguridad`

---

<a id="item-16"></a>
## [Inkheart 1.5 - Renovación de interfaz, búsqueda de texto completo y pestañas de documentos múltiples](https://www.reddit.com/r/selfhosted/comments/1xw2dqs/inkheart_15_ui_refresh_fulltext_search_and/) ⭐️ 5.0/10

Inkheart 1.5, una aplicación autoalojada para bibliotecas PDF, presenta una renovación de interfaz, búsqueda de texto completo y pestañas de documentos múltiples.

reddit · r/selfhosted · /u/M4dmaddy · nov 14, 13:26

**Etiquetas**: `#autoalojamiento`, `#PDF`, `#gestión de documentos`, `#actualización de software`, `#búsqueda de texto completo`

---

<a id="item-17"></a>
## [Usuario busca cliente de correo web con notificaciones en tiempo real](https://www.reddit.com/r/selfhosted/comments/1xw9rwf/webmail_client_with_notifications/) ⭐️ 5.0/10

Un usuario de Reddit en r/selfhosted busca un cliente de correo web que pueda enviar notificaciones de correo en tiempo real tanto a Linux como a Android, para evitar tener Thunderbird ejecutándose constantemente e iniciar sesión por separado en cada dispositivo. La solicitud pone de relieve un problema común para los usuarios de correo autoalojado: equilibrar las notificaciones en tiempo real con la comodidad en múltiples dispositivos. Una solución de correo web adecuada podría mejorar la experiencia del usuario y reducir el uso de recursos en las máquinas locales. El usuario desea específicamente notificaciones en Linux y Android y señala que el correo web resolvería automáticamente el problema de los inicios de sesión separados. La solución técnica subyacente para las notificaciones de correo en tiempo real suele ser IMAP IDLE, que permite al servidor enviar actualizaciones al cliente sin necesidad de sondeo.

reddit · r/selfhosted · /u/Reasonable-Weekend27 · nov 14, 18:37

**Contexto**: IMAP IDLE es una extensión del protocolo IMAP (RFC 2177) que permite al servidor de correo notificar al cliente de inmediato cuando llega nuevo correo, en lugar de que el cliente lo compruebe periódicamente. Es el mecanismo estándar utilizado por muchos clientes de correo, incluido Thunderbird, para proporcionar notificaciones en tiempo real mientras el cliente está en ejecución. Las aplicaciones de correo web suelen gestionar las notificaciones mediante funciones del navegador, pero las soluciones autoalojadas pueden necesitar implementar mecanismos push similares para alertar a los usuarios en el escritorio o en el móvil.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IMAP_IDLE">IMAP IDLE</a></li>
<li><a href="https://es.wikipedia.org/wiki/IMAP_IDLE">IMAP IDLE - Wikipedia, la enciclopedia libre</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojamiento`, `#cliente de correo`, `#notificaciones`, `#thunderbird`, `#consejos`

---

<a id="item-18"></a>
## [Plan para recuperación segura de bóveda Bitwarden autohospedada tras pérdida total](https://www.reddit.com/r/selfhosted/comments/1xwd1sf/how_to_provide_secure_bootstrap_access_in_the/) ⭐️ 5.0/10

El autor describe una estrategia de recuperación ante desastres para su gestor de contraseñas Vaultwarden autohospedado: exporta la bóveda, la cifra con age usando una contraseña larga y compleja que recuerda, la almacena en la nube pública con un enlace protegido por otra contraseña y publica el enlace en su sitio web. Pide críticas o mejores ideas, considerando también una copia USB cifrada con un amigo o familiar. Esto aborda la gestión de claves y la recuperación ante pérdida total en servicios autohospedados, un escenario a menudo descuidado por quienes confían en copias locales en caché. La compensación entre disponibilidad y seguridad es clave para la comunidad de autohospedaje. El plan utiliza cifrado age (herramienta moderna y simple) y una exportación JSON protegida por contraseña, además de un enlace público en la nube con otra contraseña; no se mencionan hardware de confianza ni división de claves. Una preocupación es que la bóveda cifrada expuesta públicamente depende de la fortaleza de las contraseñas y del secreto del enlace; la alternativa USB con un amigo es más segura pero menos fiable.

reddit · r/selfhosted · /u/langdalenerd · nov 14, 20:54

**Contexto**: Vaultwarden es una implementación autohospedada de código abierto compatible con Bitwarden, un gestor de contraseñas que almacena credenciales cifradas. age es una herramienta de cifrado de archivos que admite frases de contraseña y cifrado de clave pública, con un diseño moderno y seguro. La recuperación ante desastres en autohospedaje requiere acceso fuera de banda a las claves de cifrado, porque si se pierden todos los dispositivos, no hay forma de recuperar los datos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/FiloSottile/age">GitHub - FiloSottile/ age : A simple, modern and secure encryption tool...</a></li>
<li><a href="https://grokipedia.com/page/Vaultwarden">Vaultwarden</a></li>
<li><a href="https://bitwarden.com/products/personal/">Best Free & Premium Password Manager | Bitwarden</a></li>

</ul>
</details>

**Etiquetas**: `#autohospedaje`, `#seguridad`, `#gestión de claves`, `#recuperación ante desastres`, `#cifrado`

---