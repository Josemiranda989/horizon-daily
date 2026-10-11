---
layout: default
title: "Horizon Summary: 2026-10-11 (ES)"
date: 2026-10-11
lang: es
---

> De 21 artículos, 17 fueron seleccionados por relevancia

---

1. [LineageOS 24.0 añade objetivo genérico experimental para hardware bare-metal](#item-1) ⭐️ 8.0/10
2. [Bitwarden adopta doble licencia para las versiones de las tiendas de aplicaciones](#item-2) ⭐️ 8.0/10
3. [Cloudflare Radar muestra caída brusca del tráfico de bots de Yandex tras ataques](#item-3) ⭐️ 7.0/10
4. [La web de IRCv3 reaviva el debate sobre su evolución y extensiones fragmentadas](#item-4) ⭐️ 7.0/10
5. [La comunidad crea modelos de decisión propios inspirados en Jev](#item-5) ⭐️ 7.0/10
6. [Un juego de construcción de ciudades donde la ciudad preferiría que no construyeras](#item-6) ⭐️ 7.0/10
7. [PSPi 6 coloca una Raspberry Pi dentro de una PSP 1000](#item-7) ⭐️ 6.0/10
8. [Cheque de recompensa de Knuth por hallar un error en The Art of Computer Programming](#item-8) ⭐️ 6.0/10
9. [Panel ePaper casero e inalámbrico monitorea CISA KEV y noticias de BleepingComputer](#item-9) ⭐️ 6.0/10
10. [Cómo reformatear en masa discos HPE 3Par y Dell EMC de 520 a 512](#item-10) ⭐️ 6.0/10
11. [NutriTrace v1.4.0 añade modo sin conexión en el navegador y soporte plegable](#item-11) ⭐️ 6.0/10
12. [Motif: editor de UI y gráficos vectoriales autoalojable, multijugador y no destructivo](#item-12) ⭐️ 6.0/10
13. [Nitter busca financiación y ayuda legal en su actualización del 10 de octubre](#item-13) ⭐️ 5.0/10
14. [El creador de Dwarf Fortress adopta el control de versiones tras años sin usarlo](#item-14) ⭐️ 5.0/10
15. [Python 3.15.0 añadido a actions/python-versions](#item-15) ⭐️ 5.0/10
16. [Usuario de Reddit duda entre Komodo y Arcane para sustituir Dockhand con OpenBao](#item-16) ⭐️ 5.0/10
17. [Opciones de autoalojamiento para inquilinos en Países Bajos](#item-17) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [LineageOS 24.0 añade objetivo genérico experimental para hardware bare-metal](https://lineageos.org/Changelog-32/) ⭐️ 8.0/10

LineageOS 24.0 fue lanzado e incluye un objetivo genérico experimental, presentado por el colaborador 0xCAFEBABE, que ha arrancado con éxito en PCs x86_64 comunes, Macs con Apple Silicon, NVIDIA DGX Spark y portátiles Qualcomm Snapdragon X. Además, mantiene soporte para muchos teléfonos. Esto amplía LineageOS más allá de los teléfonos hacia PCs y portátiles bare-metal, ofreciendo una alternativa Android sin Google para reutilizar hardware antiguo y ejecutar Android en equipos ARM modernos. Podría reducir los residuos electrónicos y ampliar las alternativas a Linux de escritorio. El objetivo genérico sigue en estado experimental, por lo que no equivale a una compilación estable ni con soporte oficial para esos dispositivos. Los arranques exitosos reportados cubren PCs x86_64, Macs con Apple Silicon, NVIDIA DGX Spark y portátiles Qualcomm Snapdragon X Series.

hackernews · timschumi · oct 11, 06:18 · [Discusión](https://news.ycombinator.com/item?id=50040276)

**Contexto**: LineageOS es una distribución Android de código abierto basada en AOSP y sucesora de CyanogenMod, con millones de dispositivos activos. En este contexto, bare-metal significa ejecutarse directamente sobre el hardware sin otro sistema operativo debajo, y un objetivo genérico es una compilación pensada para categorías amplias de hardware en lugar de un teléfono concreto. Snapdragon X es una línea de sistemas en chip ARM de Qualcomm para portátiles, y NVIDIA DGX Spark es un equipo de escritorio ARM orientado a cargas de trabajo de IA.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LineageOS">LineageOS</a></li>
<li><a href="https://grokipedia.com/page/NVIDIA_DGX_Spark">NVIDIA DGX Spark</a></li>
<li><a href="https://grokipedia.com/page/Snapdragon_X_Elite">Snapdragon X Elite</a></li>

</ul>
</details>

**Discusión**: La reacción de la comunidad es mayoritariamente positiva: los usuarios están entusiasmados con reutilizar portátiles viejos con Android y agradecen a los mantenedores por prolongar la vida de teléfonos antiguos. Algunos usuarios preguntan por qué ciertos dispositivos no reciben soporte, mientras que otros comparten experiencias positivas con LineageOS en equipos como el Poco F3.

**Etiquetas**: `#LineageOS`, `#Android`, `#ROM personalizada`, `#Software libre`, `#Compatibilidad de hardware`

---

<a id="item-2"></a>
## [Bitwarden adopta doble licencia para las versiones de las tiendas de aplicaciones](https://www.reddit.com/r/selfhosted/comments/1x2iazs/bitwarden_announces_dual_license_published/) ⭐️ 8.0/10

Bitwarden anunció un modelo de doble licencia a partir de su próxima versión: las compilaciones oficiales de las tiendas de aplicaciones usarán una licencia comercial, mientras que las versiones GPLv3 seguirán disponibles en GitHub. Las funciones existentes permanecerán en ambas versiones, pero algunas funciones futuras podrían ser exclusivas de las compilaciones comerciales. Este cambio es importante porque Bitwarden es un gestor de contraseñas muy usado en la comunidad de código abierto y autoalojamiento, y la doble licencia podría generar una divergencia a largo plazo entre la versión GPLv3 y la comercial. Los usuarios y quienes lo autoalojan deberán vigilar qué funciones siguen siendo abiertas y cuáles se vuelven privativas. Según Bitwarden, las funciones existentes seguirán disponibles en ambas versiones, el autoalojamiento y la bifurcación seguirán siendo compatibles, y el plan gratuito no cambiará. Sin embargo, algunas funciones futuras podrían limitarse a las compilaciones comerciales, y el modelo comenzará con la próxima versión.

reddit · r/selfhosted · /u/cainejunkazama · oct 10, 15:38

**Contexto**: Bitwarden es un gestor de contraseñas que ha ofrecido una edición de código abierto autoalojable, con versiones distribuidas a través de GitHub. La GPLv3 es una licencia de software libre con copyleft que exige que quien distribuya versiones modificadas proporcione el código fuente bajo la misma licencia, lo que protege las libertades de los usuarios pero puede limitar la comercialización privativa. La doble licencia permite a un proveedor ofrecer el mismo software bajo una licencia de código abierto y una licencia comercial, lo que habilita versiones de pago o privativas sin dejar de ofrecer la versión GPL.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPLv3_license">GPLv3 license</a></li>
<li><a href="https://directdeals.com/blog/how-can-dual-licensing-benefit-software-developers">How Can Dual Licensing Benefit Software Developers? - DirectDeals</a></li>

</ul>
</details>

**Etiquetas**: `#Bitwarden`, `#código abierto`, `#licenciamiento`, `#self-hosted`, `#gestores de contraseñas`

---

<a id="item-3"></a>
## [Cloudflare Radar muestra caída brusca del tráfico de bots de Yandex tras ataques](https://radar.cloudflare.com/bots/as13238?dateRange=7d) ⭐️ 7.0/10

Los datos de Cloudflare Radar para el AS13238 muestran una caída abrupta del tráfico de bots de Yandex, y el tráfico HTTP habría bajado casi a cero tras un tercer ataque contra la infraestructura de centros de datos de Yandex. La caída se produjo después de ataques anteriores y de interrupciones en cascada. Muestra cómo el daño a la infraestructura física puede reducir rápidamente la actividad de rastreo de un gran motor de búsqueda, lo que podría afectar la indexación y la visibilidad en los resultados de Yandex. Para los operadores de sitios y quienes monitorean redes, el cambio repentino es una señal útil de una degradación más amplia del servicio. Según los comentarios, los dos primeros ataques degradaron el tráfico HTTP de Yandex y un tercero lo redujo a aproximadamente 0 %, aunque la página de búsqueda seguía respondiendo. Cloudflare Radar clasifica como probablemente automatizadas las solicitudes con puntuaciones de bot entre 1 y 29, y un comentarista señaló que la mayor parte del tráfico del AS13238 era UDP, no rastreo malicioso.

hackernews · walrus01 · oct 11, 10:27 · [Discusión](https://news.ycombinator.com/item?id=50041619)

**Contexto**: Yandex es una gran empresa tecnológica rusa, a menudo descrita como el «Google de Rusia». Opera YandexBot, un rastreador web que indexa contenido para su motor de búsqueda, utilizado por una parte importante de los usuarios de internet de habla rusa. Cloudflare Radar monitorea el tráfico por número de sistema autónomo, o ASN; el AS13238 está asociado con Yandex. El tráfico de bots incluye rastreadores automatizados, como los indexadores de motores de búsqueda, no solo actores maliciosos.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://llmpulse.ai/es/ai-crawler-index/yandexbot">YandexBot : el rastreador web de Yandex | Cómo funciona y cómo...</a></li>
<li><a href="https://bots.fyi/d/yandexbot">YandexBot is a web crawler operated by Yandex, a major Russian...</a></li>
<li><a href="https://www.cloudflare.com/products/bot-management/">Bot Management - Cloudflare</a></li>

</ul>
</details>

**Discusión**: Los comentaristas coincidieron en general en que la caída es esperable porque Yandex, al igual que Google, usa rastreadores para indexar la web y la indexación se vuelve menos prioritaria durante una interrupción. Algunos matizaron que el AS13238 es bastante benigno y mayormente UDP, mientras que otros destacaron los umbrales de clasificación de bots de Cloudflare y señalaron que las fallas en cascada de los centros de datos probablemente desactivaron el rastreador de Yandex.

**Etiquetas**: `#Yandex`, `#Cloudflare`, `#bots`, `#centro de datos`, `#tráfico web`

---

<a id="item-4"></a>
## [La web de IRCv3 reaviva el debate sobre su evolución y extensiones fragmentadas](https://ircv3.net/) ⭐️ 7.0/10

Se compartió el sitio web de IRCv3 y se generó un debate en Hacker News sobre el rumbo del protocolo, la fragmentación de sus extensiones opcionales y su comparación con plataformas de chat modernas. No se anunció ninguna especificación ni versión nueva de IRCv3. IRC sigue siendo uno de los protocolos de chat más antiguos aún en uso, y su evolución afecta a desarrolladores, operadores de redes y comunidades que eligen entre IRCv3, Matrix, Discord o Slack. El debate destaca si las extensiones opcionales y la gobernanza están ayudando o frenando la modernización de IRC. Los comentaristas señalaron que la matriz de soporte de clientes de IRCv3 muestra muchas extensiones opcionales —como reacciones, respuestas, SASL, WHOX y notificaciones de escritura—, lo que puede hacer que una misma conversación se vea distinta según el cliente. También se mencionaron los proyectos federados Parley y Ahoy, que buscan ofrecer una experiencia similar a Discord/Slack manteniéndose compatibles con IRC/IRCv3.

hackernews · basilikum · oct 11, 10:11 · [Discusión](https://news.ycombinator.com/item?id=50041540)

**Contexto**: Internet Relay Chat (IRC) es un protocolo de chat grupal basado en texto de finales de los años ochenta, estandarizado en el RFC 1459 y todavía utilizado por muchas comunidades técnicas y de software libre. IRCv3 es un grupo de trabajo que desarrolla extensiones compatibles hacia atrás para modernizar IRC con funciones como autenticación de cuentas, etiquetado de mensajes, respuestas e indicadores de escritura. Como muchas de esas extensiones son opcionales, los servidores y clientes pueden soportar subconjuntos distintos, lo que genera experiencias inconsistentes. Alternativas modernas como Matrix y aplicaciones comerciales como Discord y Slack han atraído usuarios, pero IRC mantiene comunidades activas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Irc_protocol">Irc protocol</a></li>
<li><a href="https://ircv3-net.nproxy.org/faq">Frequently Asked Questions of the IRCv 3 Working Group.</a></li>
<li><a href="https://www.inspircd.org/">InspIRCd - Internet Relay Chat ( IRCv 3 ) server for UNIX-like and...</a></li>

</ul>
</details>

**Discusión**: El sentimiento general es variado pero sustancial: algunos sostienen que las extensiones opcionales de IRCv3 fragmentan la experiencia, mientras que otros destacan la permanencia de IRC durante 35 años. Se sugirieron un nuevo liderazgo para IRCv3, clientes federados como Parley/Ahoy, mejor soporte multidispositivo y móvil, y funciones más ricas de multimedia y voz. Un comentarista señaló que IRC podría extrañar el acceso móvil y las cuentas multidispositivo en comparación con Discord.

**Etiquetas**: `#IRCv3`, `#Protocolos`, `#Mensajería`, `#Software libre`, `#Comunidades`

---

<a id="item-5"></a>
## [La comunidad crea modelos de decisión propios inspirados en Jev](https://nishtahir.com/build-your-own-decision-model/) ⭐️ 7.0/10

Una publicación sobre cómo construir tu propio modelo de decisión generó un debate de 341 puntos y 77 comentarios en el que varios desarrolladores compartieron alternativas como JobFit, un evaluador de ajuste entre CV y ofertas laborales que funciona en el navegador, y browser-laya, un modelo de decisión puro que responde en menos de 200 ms. La respuesta muestra un interés creciente por modelos de decisión locales y ligeros que evitan depender de grandes LLM propietarios y pueden ejecutarse en el navegador con baja latencia, lo que podría abaratar y hacer más accesibles la clasificación y la toma de decisiones automatizadas. El debate destacó opciones técnicas concretas: SQLite-vec con un modelo de embeddings pequeño de Qwen para recuperación, pipelines de entrenamiento de decisiones tipadas que se ejecutan en el navegador y un modelo de decisión puro llamado Laya con respuestas en menos de 200 ms; algunos participantes sostuvieron que los LLM comunes ya funcionan bien como clasificadores zero-shot.

hackernews · softwaredoug · oct 10, 22:50 · [Discusión](https://news.ycombinator.com/item?id=50037949)

**Contexto**: Un modelo de decisión es un marco formalizado que estructura alternativas, criterios, incertidumbres y resultados para permitir decisiones sistemáticas; en aprendizaje automático, estos modelos suelen adoptar la forma de clasificadores. Jev es un modelo de decisión de IA propietario desarrollado por TypeSafe AI y lanzado en acceso anticipado limitado el 15 de septiembre de 2026. Los clasificadores zero-shot asignan etiquetas sin entrenamiento específico para la tarea, a menudo mediante LLM de propósito general.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decision_model">Decision model</a></li>

</ul>
</details>

**Discusión**: El sentimiento de la comunidad fue mixto: varios comentaristas se inspiraron para crear alternativas y compartieron enlaces, mientras que profesionales del aprendizaje automático expresaron frustración porque el entusiasmo por Jev renombra clasificadores existentes y enfoques zero-shot con LLM; algunos también señalaron problemas de rendimiento de los LLM locales y ofrecieron opciones más rápidas para el navegador.

**Etiquetas**: `#modelos de decisión`, `#clasificadores`, `#LLM`, `#aprendizaje automático`, `#desarrollo de software`

---

<a id="item-6"></a>
## [Un juego de construcción de ciudades donde la ciudad preferiría que no construyeras](https://housing.over.pizza/) ⭐️ 7.0/10

Un juego de navegador en housing.over.pizza convierte la construcción de ciudades en una simulación de los obstáculos burocráticos que frenan la vivienda, y pide al jugador gestionar permisos y trámites en lugar de limitarse a colocar edificios. Reformula un debate de política pública —cómo las normas urbanísticas y la burocracia restringen la oferta de vivienda— como una experiencia interactiva, lo que puede ayudar a un público más amplio a entender por qué el desarrollo urbano es lento y costoso. El juego está alojado en housing.over.pizza y se resume como una simulación de barreras burocráticas para el desarrollo residencial; la publicación obtuvo 378 puntos y 129 comentarios, con menciones a permisos, audiencias, apelaciones, demandas y zonificación.

hackernews · JumpCrisscross · oct 10, 20:31 · [Discusión](https://news.ycombinator.com/item?id=50036864)

**Contexto**: Los juegos de construcción de ciudades suelen premiar al jugador por hacer crecer un asentamiento de forma eficiente. En muchas ciudades reales, la construcción de vivienda debe superar normas de zonificación, revisiones ambientales, aprobaciones discrecionales, audiencias públicas y apelaciones, procesos que pueden retrasar o bloquear proyectos. El juego convierte esa maquinaria regulatoria en su obstáculo central, lo que lo conecta con los debates sobre oferta y asequibilidad de vivienda.

**Discusión**: Los comentaristas recibieron bien la premisa y compartieron ejemplos cercanos: un mod burocrático de Factorio, el juego satírico Car Park Capital y bromas sobre obstáculos de infraestructura como el HS2. Una persona relató una partida en la que construyó 4.147 viviendas en San Francisco cuando la ciudad necesitaba 82.069, lo que refuerza la dificultad; otra recordó un juego de mesa donde la única solución viable era aumentar drásticamente la zonificación en una ciudad remota del este de la bahía.

**Etiquetas**: `#videojuegos`, `#urbanismo`, `#vivienda`, `#burocracia`, `#simulación`

---

<a id="item-7"></a>
## [PSPi 6 coloca una Raspberry Pi dentro de una PSP 1000](https://github.com/othermod/PSPi-Version-6) ⭐️ 6.0/10

El proyecto PSPi 6 ha lanzado una placa de circuito personalizada que sustituye la placa base de una PSP 1000 por una Raspberry Pi, convirtiendo la consola en un dispositivo portátil de juegos retro. Esto ofrece a los aficionados a los juegos retro una forma de reutilizar carcasas antiguas de PSP y aprovechar el mayor soporte de emuladores de la Raspberry Pi, aunque sigue siendo una alternativa de nicho frente a las consolas retro modernas. El diseño está orientado específicamente a la PSP 1000, por lo que adaptarlo a los modelos más pequeños PSP-2000/3000 requeriría cambios. Los miembros de la comunidad también señalan que las placas Raspberry Pi son actualmente caras y no tienen un verdadero modo de suspensión, así que los usuarios deben dejarla encendida o esperar a que arranque.

hackernews · therepanic · oct 11, 00:45 · [Discusión](https://news.ycombinator.com/item?id=50038623)

**Contexto**: La PlayStation Portable, o PSP, es la consola portátil de Sony lanzada por primera vez en 2004; la PSP-1000 es el modelo original. Una Raspberry Pi es una computadora de placa única de bajo costo popular en proyectos de electrónica y emulación. En el mod PSPi, una placa de reemplazo personalizada permite que la Raspberry Pi actúe como procesador de la portátil.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/othermod/PSPi-Version-6">GitHub - othermod/ PSPi -Version- 6 · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Raspberry_Pi">Raspberry Pi</a></li>

</ul>
</details>

**Discusión**: Los comentarios muestran interés, pero con reservas prácticas. Los usuarios señalan que las baterías viejas de PSP suelen hincharse, lo que hace más atractivos estos mods, y sugieren conseguir unidades baratas para piezas en lugar de sacrificar una PSP funcional. Otros cuestionan el costo, la falta de modo de suspensión y si el homebrew nativo de PSP ya cubre gran parte del uso.

**Etiquetas**: `#Raspberry Pi`, `#PSP`, `#modding`, `#emulación`, `#hardware`

---

<a id="item-8"></a>
## [Cheque de recompensa de Knuth por hallar un error en The Art of Computer Programming](https://www.thomas-huehn.com/knuth-reward-check/) ⭐️ 6.0/10

Thomas Huehn ha publicado un relato personal sobre cómo recibió un cheque de recompensa de Knuth después de que Donald Knuth confirmara un error que encontró en uno de sus libros. Según los comentarios, el error consistía en afirmar que se pueden generar “infinitos alfabetos” aunque solo es posible una cantidad finita, aunque enorme. El cheque de recompensa de Knuth es uno de los trofeos más valorados en la informática; esta historia muestra que incluso pequeñas correcciones de exactitud otorgan prestigio en la cultura hacker. También evidencia que el sistema de recompensas de Knuth sigue motivando una lectura cuidadosa de sus densos y usados libros. Knuth ha ofrecido tradicionalmente 2,56 dólares por cada error reportado primero, y los cheques suelen guardarse como recuerdo en lugar de cobrarse. En los comentarios se menciona un cheque número 790 por 2,88 dólares y se señala que los cheques físicos se han vuelto menos comunes; el error concreto implicaba la expresión “infinitos alfabetos”.

hackernews · Curiositry · oct 10, 15:47 · [Discusión](https://news.ycombinator.com/item?id=50034081)

**Contexto**: Donald Knuth es un informático pionero y autor de The Art of Computer Programming (TAOCP). Desde finales de los años sesenta ofrece pequeñas recompensas económicas, normalmente de 2,56 dólares, a quien informe primero de cada error técnico, tipográfico o histórico. Los cheques son famosos en la informática como símbolo de prestigio y rara vez se cobran.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knuth_reward_check">Knuth reward check - Wikipedia</a></li>
<li><a href="https://www.thomas-huehn.com/knuth-reward-check/">Knuth reward check - thomas-huehn.com</a></li>
<li><a href="https://www.truetex.com/knuthchk.htm">TrueTeX Software -- Donald Knuth's Reward Check</a></li>

</ul>
</details>

**Discusión**: El sentimiento general es afectuoso y nostálgico: los lectores intercambian historias sobre cheques perdidos, números y montos, y valoran más el reconocimiento simbólico que el dinero. Algunos debaten si Knuth debería haber escrito “una cantidad enorme de alfabetos”, y un comentarista observa que Knuth ha dejado de enviar cheques físicos.

**Etiquetas**: `#Donald Knuth`, `#The Art of Computer Programming`, `#cultura hacker`, `#recompensas`, `#corrección de errores`

---

<a id="item-9"></a>
## [Panel ePaper casero e inalámbrico monitorea CISA KEV y noticias de BleepingComputer](https://www.reddit.com/r/selfhosted/comments/1x2vrs5/anyone_ive_told_about_this_irl_wasnt_as_excited/) ⭐️ 6.0/10

Un usuario de Reddit completó un panel ePaper inalámbrico alimentado por batería que se actualiza cada hora con entradas del catálogo de Vulnerabilidades Explotadas Conocidas (KEV) de CISA y noticias de BleepingComputer. Fue su primer proyecto con ePaper, Arduino y C/C++, y el dispositivo funciona desde el 4 de agosto sin recargarse. Muestra cómo las pantallas ePaper de bajo consumo y las placas con microcontrolador pueden crear un tablero de seguridad práctico y siempre visible para entusiastas del autohospedaje, combinando inteligencia de amenazas gubernamental con noticias de ciberseguridad. No es un avance técnico revolucionario, pero es un proyecto de nicho útil para esa comunidad. El panel usa una pantalla ePaper de Seeed Studio y consume casi nada de electricidad salvo durante las actualizaciones horarias, lo que explica la duración de batería de varios meses. El creador también mencionó un repositorio de GitHub, pero no publicó el enlace porque el subreddit restringe los enlaces a repositorios.

reddit · r/selfhosted · /u/ImLostTbh- · oct 11, 01:41

**Contexto**: El papel electrónico (ePaper) es una tecnología de pantalla reflectiva que imita la tinta sobre papel y puede mantener contenido estático sin consumo continuo de energía. El catálogo de Vulnerabilidades Explotadas Conocidas (KEV) de CISA enumera vulnerabilidades con explotación activa confirmada y fija plazos de corrección para las agencias federales de EE. UU. BleepingComputer es un sitio de noticias de ciberseguridad y Arduino es una plataforma de microcontroladores amigable para principiantes, frecuente en proyectos electrónicos de bricolaje.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_paper">Electronic paper - Wikipedia</a></li>
<li><a href="https://securitytribune.com/noticias/cisa-suma-cve-2026-34486">CISA suma CVE-2026-34486 a su catálogo KEV — CiberLATAM</a></li>

</ul>
</details>

**Etiquetas**: `#ePaper`, `#ciberseguridad`, `#autohospedado`, `#Arduino`, `#CISA`

---

<a id="item-10"></a>
## [Cómo reformatear en masa discos HPE 3Par y Dell EMC de 520 a 512](https://www.reddit.com/r/selfhosted/comments/1x364ha/how_to_massreformat_storage_array_disks_from_3par/) ⭐️ 6.0/10

Un miembro de la comunidad selfhosted publicó una guía práctica actualizada para convertir discos retirados de arrays HPE 3Par y Dell EMC de sectores de 520 bytes a 512 bytes usando sg3_utils y GNU parallel, y también ofrece a la venta parte de los 40 discos Seagate de 8 TB adquiridos. Permite a los usuarios de homelab y selfhosting reutilizar discos empresariales retirados y económicos en servidores Linux estándar, lo que reduce el costo de hardware, aunque el proceso es de nicho y exige un formateo de bajo nivel cuidadoso. La guía advierte iniciar sesión localmente en lugar de usar SSH, asume que todos los datos se destruirán y señala que el formateo es rápido en SSD, pero puede tardar muchas horas en HDD; el comando principal es sg_format --format --size=512 usado con GNU parallel.

reddit · r/selfhosted · /u/Accurate-Ad6361 · oct 11, 11:43

**Contexto**: Los arrays de almacenamiento empresarial, como HPE 3Par y Dell EMC, suelen usar los mismos discos físicos que los servidores normales, pero los formatean a bajo nivel con sectores de 520 bytes en lugar de los 512 bytes habituales. Los 8 bytes adicionales por sector permiten sumas de verificación de integridad de datos como T10 DIF, con las que el array puede verificar la información al leer y escribir. Los sistemas Linux estándar generalmente esperan sectores de 512 bytes, por lo que los discos procedentes de arrays retirados deben reformatearse antes de reutilizarse. El paquete sg3_utils envía comandos SCSI a los dispositivos a través de la interfaz de paso SCSI del sistema operativo para realizar este formateo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://forum.level1techs.com/t/reformat-hp-3par-hgst-520-byte-drives-to-512-or-4096-bytes/208798">Reformat HP 3PAR HGST 520 byte drives to 512 or 4096 bytes</a></li>
<li><a href="https://ygerber.online/post/reformatting-drives/">Reformatting enterprise storage drives to 512 bytes</a></li>
<li><a href="https://manpages.debian.org/stretch/sg3-utils/sg3_utils.8.en.html">sg 3 _ utils (8) — sg 3 - utils — Debian stretch — Debian Manpages</a></li>

</ul>
</details>

**Etiquetas**: `#almacenamiento`, `#homelab`, `#HPE 3Par`, `#Dell EMC`, `#reformateo de discos`

---

<a id="item-11"></a>
## [NutriTrace v1.4.0 añade modo sin conexión en el navegador y soporte plegable](https://www.reddit.com/r/selfhosted/comments/1x2dvj4/nutritrace_v140_released_offline_mode_in_the/) ⭐️ 6.0/10

NutriTrace v1.4.0 amplía el registro sin conexión a la aplicación web y a la PWA instalada, añade diseños preliminares para dispositivos plegables, búsqueda que ignora acentos e importaciones corregidas de Open Food Facts. La versión también reconstruye la sincronización, hace opcionales las comprobaciones de actualización, deja de cargar fuentes externas y cierra vulnerabilidades de aislamiento de cuentas, restablecimiento de contraseña y acceso a la red interna. Esta actualización hace que un diario de alimentos autohospedado sea más fiable con conectividad escasa o nula y más atractivo para usuarios centrados en la privacidad que desean un seguimiento al estilo MyFitnessPal sin dependencia de la nube. Los cambios de seguridad y privacidad por defecto reducen la exposición de quienes autohospedan, y el soporte plegable muestra la adaptación del proyecto a nuevos formatos de dispositivo. La aplicación web mantiene el diario, los alimentos, las comidas, las recetas, los objetivos y el temporizador de ayuno funcionando sin conexión en una pestaña del navegador o PWA, y sincroniza al volver; la sincronización ahora usa el reloj del servidor y evita fugas de datos entre cuentas. La búsqueda relaciona 'platano' con 'Plátano' y 'cafe' con 'Café' incluso en un espejo local de Open Food Facts, y las correcciones de seguridad cierran fallos de edición de alimentos entre cuentas, enlaces de restablecimiento redirigibles y conexiones de CookTrace/Mealie que podían alcanzar servicios internos.

reddit · r/selfhosted · /u/SimplyRavishing1 · oct 10, 12:16

**Contexto**: NutriTrace es un rastreador nutricional autohospedado con licencia AGPL-3.0, distribuido como un único contenedor Docker, que guarda cada diario de alimentos en un archivo SQLite local. Compite con aplicaciones comerciales como MyFitnessPal, Cronometer y Lose It al evitar la telemetría y la sincronización en la nube. Los datos de alimentos pueden provenir de Open Food Facts, una base de datos colaborativa y gratuita de productos alimentarios de todo el mundo, y del USDA, con opción de espejo local para despliegues aislados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Food_Facts">Open Food Facts</a></li>
<li><a href="https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License">GNU Affero General Public License - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojado`, `#nutrición`, `#seguimiento de alimentos`, `#software libre`, `#Docker`

---

<a id="item-12"></a>
## [Motif: editor de UI y gráficos vectoriales autoalojable, multijugador y no destructivo](https://www.reddit.com/r/selfhosted/comments/1x332rf/motif_free_multiplayer_selfhostable/) ⭐️ 6.0/10

Motif ha lanzado una versión alfa como editor gratuito, de código abierto y autoalojable para gráficos vectoriales e interfaces, que combina técnicas CAD no destructivas con un flujo de trabajo inspirado en los Geometry Nodes de Blender. El desarrollador también ha publicado el código fuente, un servidor de demostración multijugador público y compilaciones de servidor Linux x64 por medio de GitHub Actions. Ofrece una alternativa autoalojable a herramientas como Figma e Illustrator, lo que es relevante para la privacidad, el control y la personalización en los flujos de diseño. Su modelo de edición procedimental, similar a un programa, podría hacer que los diseños reutilizables y las futuras ramificaciones sean más potentes que solo la manipulación directa tradicional. El proyecto está en fase alfa, con los prefabs en desarrollo como alternativa a los componentes de Figma y planes futuros para sombreadores personalizados mediante un editor de grafos real, animaciones y nodos generadores. El servidor multijugador público está abierto a todos, por lo que conviene no compartir información personal, y las aplicaciones de macOS/iPadOS por ahora deben compilarse localmente en lugar de obtenerse desde CI.

reddit · r/selfhosted · /u/kekland322 · oct 11, 08:41

**Contexto**: Geometry Nodes es el sistema basado en nodos de Blender para generar y modificar geometría de forma procedimental sin consolidar permanentemente cada edición. El modelado CAD no destructivo mantiene del mismo modo un historial de operaciones como cortes y uniones para que los diseños puedan modificarse posteriormente. En las herramientas de diseño, los prefabs o componentes son plantillas reutilizables que conservan una fuente central de control entre varias instancias.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html">Geometry Nodes - Blender 5.2 LTS Manual</a></li>
<li><a href="https://hinatahugu29.github.io/Blender_Seamless_CAD/">Non-destructive CAD modelling inside Blender</a></li>
<li><a href="https://github.com/wurde/prefab-ui">GitHub - wurde/prefab-ui: A suite of Web Components built ...</a></li>

</ul>
</details>

**Etiquetas**: `#editor de gráficos vectoriales`, `#autoalojable`, `#código abierto`, `#diseño UI`, `#CAD no destructivo`

---

<a id="item-13"></a>
## [Nitter busca financiación y ayuda legal en su actualización del 10 de octubre](https://nitter.net/) ⭐️ 5.0/10

El 10 de octubre, Nitter anunció que busca financiación y apoyo legal para seguir funcionando como interfaz alternativa de X/Twitter. La actualización no presenta una novedad técnica, pero indica que el proyecto necesita recursos económicos y jurídicos para mantenerse. Es relevante para las comunidades de código abierto y privacidad porque Nitter ha permitido consultar contenido de X/Twitter sin cuentas, anuncios ni rastreadores. Si no se consiguen financiación y apoyo legal, las instancias públicas podrían volverse menos fiables o desaparecer, reduciendo una alternativa respetuosa con la privacidad. Nitter es una interfaz alternativa gratuita y de código abierto para X, antes Twitter, centrada en la privacidad y el rendimiento; permite explorar perfiles, publicaciones, medios, búsquedas y canales RSS, pero no permite iniciar sesión ni interactuar con la plataforma. El anuncio no detalla una meta de financiación concreta ni una estrategia jurídica.

hackernews · ForHackernews · oct 11, 10:37 · [Discusión](https://news.ycombinator.com/item?id=50041682)

**Contexto**: Nitter surgió como una forma respetuosa con la privacidad de leer contenido público de Twitter/X sin ser rastreado por los anuncios y las tecnologías de seguimiento de la plataforma. Funciona como una interfaz alternativa que recupera publicaciones públicas, por lo que no se necesita una cuenta para ver perfiles, respuestas, medios o resultados de búsqueda. Como Nitter depende del acceso a los datos de X/Twitter, ha enfrentado incertidumbre operativa y jurídica, y algunas instancias públicas han dejado de funcionar o han sido reemplazadas. La sostenibilidad del proyecto depende de personas voluntarias, donaciones y, ahora, de apoyo legal.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>

</ul>
</details>

**Discusión**: Las reacciones de la comunidad son variadas. Algunas personas explican el propósito de Nitter como una interfaz gratuita y de código abierto para ver X/Twitter sin cuentas ni rastreo, mientras que otras dudan de que pueda funcionar legalmente, comparándolo con un proxy de grandes medios. También hay escepticismo sobre su viabilidad a largo plazo o sobre la necesidad del proyecto, y al menos un comentario muestra resignación al decir que fue bueno mientras duró.

**Etiquetas**: `#Nitter`, `#código abierto`, `#privacidad`, `#redes sociales`, `#financiación`

---

<a id="item-14"></a>
## [El creador de Dwarf Fortress adopta el control de versiones tras años sin usarlo](https://simonwillison.net/2026/Oct/11/dwarf-fortress/) ⭐️ 5.0/10

Tarn Adams, creador de Dwarf Fortress, comenzó a usar control de versiones después de evitarlo durante mucho tiempo, según una entrevista de marzo de 2023 en la que menciona que ahora tiene "cosas de control de versiones que usar". Citas anteriores de 2013 y 2016 mostraban que trabajaba deliberadamente sin control de código fuente. El cambio refleja la transición de Dwarf Fortress de un proyecto de hobby sostenido por donaciones a un lanzamiento comercial en Steam respaldado por un equipo mayor, lo que llevó a su creador hacia prácticas de ingeniería más convencionales. Adams describió su objeción anterior en 2013 como que no le gustaba la sensación de que el código entrara en una "cajita negra sin beneficio inmediato", y en 2023 también citó los canales de Discord como parte de un proceso más complejo.

rss · Simon Willison · oct 11, 00:52

**Contexto**: Dwarf Fortress es un videojuego de simulación, construcción y gestión con elementos roguelike creado por Bay 12 Games, desarrollado desde 2002 y conocido por sus mundos de fantasía generados proceduralmente con gran detalle. El control de versiones es la práctica de registrar los cambios en el código fuente y otros archivos para poder consultar o restaurar versiones anteriores. Tarn Adams ha llamado al juego el trabajo de su vida, y en 2022 se publicó una edición de pago con gráficos en Steam e Itch.io.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dwarf_Fortress">Dwarf Fortress</a></li>
<li><a href="https://en.wikipedia.org/wiki/Version_control">Version control</a></li>

</ul>
</details>

**Etiquetas**: `#Dwarf Fortress`, `#control de versiones`, `#desarrollo de videojuegos`, `#ingeniería de software`

---

<a id="item-15"></a>
## [Python 3.15.0 añadido a actions/python-versions](https://simonwillison.net/2026/Oct/10/python-actions/) ⭐️ 5.0/10

Se incorporó Python 3.15.0 al repositorio actions/python-versions, lo que permite especificar "3.15" en las matrices de pruebas de GitHub Actions para ejecutar pruebas contra la nueva versión estable. Esto facilita a los proyectos que usan GitHub Actions para probar Python adoptar y validar la compatibilidad con la versión estable más reciente sin configuración adicional, detectando incompatibilidades de forma temprana. El cambio se encuentra en actions/python-versions, el repositorio que provee las compilaciones de Python para las imágenes de los runners y para la acción setup-python; ahora se puede usar la cadena de versión "3.15" en la matriz del flujo de trabajo.

rss · Simon Willison · oct 10, 23:58

**Contexto**: GitHub Actions es una plataforma de integración y entrega continua donde los flujos de trabajo se ejecutan en runners alojados. Una matriz de pruebas permite que un mismo trabajo se ejecute con varias versiones o configuraciones, definiendo valores como las versiones de Python. El repositorio actions/python-versions suministra las compilaciones de Python que se instalan en las imágenes de los runners y que quedan disponibles mediante la acción setup-python.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/actions/python-versions">GitHub - actions/python-versions: Python builds for Actions ...</a></li>
<li><a href="https://github.com/actions/python-versions/releases">Releases: actions/python-versions - GitHub</a></li>

</ul>
</details>

**Etiquetas**: `#python`, `#github actions`, `#integración continua`, `#versionado`, `#desarrollo de software`

---

<a id="item-16"></a>
## [Usuario de Reddit duda entre Komodo y Arcane para sustituir Dockhand con OpenBao](https://www.reddit.com/r/selfhosted/comments/1x2mnzt/from_dockerhand_to_komodo_or_arcane_openbao/) ⭐️ 5.0/10

Un usuario de HomeLab que automatizó su infraestructura con Semaphore, Forgejo, Renovate, OpenBao y Dockhand planea reemplazar Dockhand por su política de licencias y pregunta si Komodo o Arcane es la mejor alternativa de código abierto. En concreto, quiere mantener OpenBao como proveedor de secretos, aunque ninguno parece ofrecer soporte nativo todavía. La consulta refleja una preocupación más amplia en la comunidad de autoalojamiento y DevOps por evitar depender de herramientas cuya licencia puede cambiar, y muestra que la integración nativa con gestores de secretos se está volviendo un criterio decisivo. Una respuesta clara podría ayudar a otros a elegir pilas de código abierto sostenibles. El usuario despliega máquinas Docker en nodos Proxmox mediante playbooks de Semaphore y usa Forgejo como fuente única de verdad. Señala que la interfaz y la API de Arcane parecen prometedoras para Semaphore, que Komodo se solaparía con procesos existentes de Ansible y que ambos carecen de soporte nativo de OpenBao por ahora.

reddit · r/selfhosted · /u/Simplixt · oct 10, 18:40

**Contexto**: Dockhand es una aplicación moderna de administración de Docker con gestión de contenedores en tiempo real, soporte para pilas de Compose y autenticación de nivel empresarial. Komodo y Arcane se consideran alternativas de código abierto en el ámbito de los paneles de administración de Docker, comparables a Portainer o Dockge. OpenBao es un fork de HashiCorp Vault gestionado por la Linux Foundation y de código abierto que sirve para almacenar, administrar y distribuir secretos y datos sensibles. La configuración del usuario combina estas herramientas para automatizar despliegues de infraestructura y aplicaciones desde una única fuente de verdad basada en Git.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://openbao.org/">OpenBao</a></li>
<li><a href="https://cloudzy.com/blog/portainer-alternatives/">Portainer Alternatives: Dockge, Arcane, Dockhand, Komodo ...</a></li>
<li><a href="https://www.bigiron.cc/guides/dockge-vs-komodo-vs-portainer-the-2026-docker-management-verdict">Dockge vs Komodo vs Portainer: The 2026 Docker Management ...</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojamiento`, `#Docker`, `#OpenBao`, `#DevOps`, `#gestión de secretos`

---

<a id="item-17"></a>
## [Opciones de autoalojamiento para inquilinos en Países Bajos](https://www.reddit.com/r/selfhosted/comments/1x2uphy/selfhosting_options_for_renters_in_netherlands/) ⭐️ 5.0/10

Un usuario de Reddit pregunta cómo mantener un servidor autoalojado siendo inquilino en los Países Bajos, con mudanzas cada 1 o 2 años y conexiones de internet deficientes. La pregunta pone de relieve una tensión práctica del autoalojamiento: una infraestructura doméstica fiable suele depender de una vivienda estable y una buena banda ancha, algo que muchos inquilinos no pueden garantizar. El usuario se mudó recientemente a un apartamento con una conexión de internet deficiente que no se puede mejorar y prevé seguir alquilando en el futuro próximo; la publicación no incluye comentarios ni soluciones propuestas.

reddit · r/selfhosted · /u/KyndMiki · oct 11, 00:46

**Contexto**: El autoalojamiento consiste en ejecutar sitios web o servicios en línea en un servidor privado bajo control propio, a menudo en casa, en lugar de depender de plataformas de alojamiento administrado. Las mudanzas frecuentes y las conexiones deficientes hacen que un servidor doméstico sea menos fiable y más difícil de mantener. Algunas personas que practican el autoalojamiento resuelven esto usando un VPS o un dispositivo pequeño de bajo consumo para que sus servicios no dependan de una vivienda permanente.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/Self-hosting_network">Self-hosting (network)</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojamiento`, `#alquiler`, `#Países Bajos`, `#servidores`, `#redes`

---