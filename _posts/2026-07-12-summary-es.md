---
layout: default
title: "Horizon Summary: 2026-07-12 (ES)"
date: 2026-07-12
lang: es
---

> De 17 artículos, 9 fueron seleccionados por relevancia

---

1. [RISCBoy: consola portátil de código abierto basada en RISC-V](#item-1) ⭐️ 8.0/10
2. [Arquitectura de UPI: cómo funciona el sistema de pagos de India](#item-2) ⭐️ 8.0/10
3. [Anthias: 8 lanzamientos en 2 meses / reproducción de video finalmente arreglada en todas partes, placas ARM no Pi, HDMI-CEC, correcciones de seguridad y una biblioteca de aplicaciones gratuita.](#item-3) ⭐️ 8.0/10
4. [Mesh LLM: computación distribuida de IA en iroh](#item-4) ⭐️ 7.0/10
5. [Nvidia, CoreWeave y Nebius: Dentro del financiamiento circular del boom de GPU](#item-5) ⭐️ 7.0/10
6. [Chat Control 1.0 de la UE aprobado entre controversia, aumentando urgencia por el autoalojamiento](#item-6) ⭐️ 7.0/10
7. [Ant: Un entorno de ejecución y ecosistema JavaScript con soporte de escritorio](#item-7) ⭐️ 6.0/10
8. [Lanzamiento de Lanemu P2P VPN 0.14 con soporte RUDP y STUN](#item-8) ⭐️ 6.0/10
9. [Archivando fotos RAW](#item-9) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [RISCBoy: consola portátil de código abierto basada en RISC-V](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

RISCBoy es una consola de juegos portátil de código abierto diseñada desde cero por el ingeniero de ASIC de Raspberry Pi, Luke Wren, con una arquitectura RISC-V personalizada e inspirada en la Gameboy Advance; fue enviada a fabricación en la primera ronda de wafer.space. Este proyecto demuestra la creciente viabilidad del hardware abierto y el diseño de ASIC personalizados, lo que podría inspirar más hardware de juegos abierto y promover la adopción de RISC-V en electrónica de consumo. La consola cuenta con un pipeline de renderizado programable basado en búferes de líneas de escaneo, descrito en su documentación PDF detallada. Fue diseñada por Luke Wren, conocido por su trabajo en la salida DVI/HDMI del RP2040, aunque aún no se ha confirmado si el chip fabricado funciona.

hackernews · mariuz · jul 11, 21:58 · [Discusión](https://news.ycombinator.com/item?id=48876245)

**Contexto**: RISC-V es un estándar de arquitectura de conjunto de instrucciones (ISA) libre y abierto que permite diseños de procesador personalizados sin tarifas de licencia, desafiando arquitecturas propietarias como ARM. Proyectos de hardware abierto como RISCBoy combinan estas ISAs con chips personalizados (ASIC) para crear dispositivos completamente transparentes. La Gameboy Advance, lanzada en 2001, era una popular consola portátil que usaba una CPU propietaria basada en ARM, lo que hace de esto una reinterpretación retro inspirada pero moderna.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>

</ul>
</details>

**Discusión**: Los miembros de la comunidad elogiaron la profundidad técnica y el concepto nostálgico, destacando la experiencia de Luke Wren como ingeniero de ASIC en Raspberry Pi. Algunos cuestionaron si el chip funcionaría, ya que fue fabricado pero aún no probado. También se resaltó el singular pipeline de renderizado y trabajos previos como PicoDVI.

**Etiquetas**: `#hardware abierto`, `#RISC-V`, `#consola portátil`, `#diseño de chips`, `#videojuegos retro`

---

<a id="item-2"></a>
## [Arquitectura de UPI: cómo funciona el sistema de pagos de India](https://timeseriesofindia.com/economy/reads/upi-architecture/) ⭐️ 8.0/10

El artículo 'UPI: Anatomía de una transacción de pago' ofrece un desglose técnico detallado de la Unified Payments Interface, explicando el flujo de una transacción desde su inicio hasta su liquidación. UPI ha impulsado la revolución de los pagos digitales en India, procesando miles de millones de transacciones mensuales, y entender su arquitectura es crucial para ingenieros, legisladores y empresas que construyen sobre ella. El artículo probablemente cubre los roles del banco del pagador, del banco del beneficiario, de NPCI como conmutador, y el uso de direcciones de pago virtuales; entre las métricas de rendimiento destacan más de 22 mil millones de transacciones al año, con un promedio de ~700 consultas por segundo en el conmutador de NPCI, con picos mucho más altos.

hackernews · prtk25 · jul 11, 16:33 · [Discusión](https://news.ycombinator.com/item?id=48873457)

**Contexto**: La Interfaz Unificada de Pagos (UPI) es un sistema de pagos instantáneos desarrollado por la Corporación Nacional de Pagos de India (NPCI) y lanzado en 2016. Permite a los usuarios transferir dinero entre cuentas bancarias usando un ID de UPI único, sin necesidad de compartir números de cuenta bancaria. UPI ha logrado una adopción masiva, posibilitando desde pequeños pagos a vendedores ambulantes hasta grandes transacciones de comercio electrónico. Opera sobre la infraestructura bancaria existente y está regulado por el Banco de la Reserva de India.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/u/unified-payment-interface-upi.asp">investopedia.com/terms/u/ unified - payment - interface -upi.asp</a></li>

</ul>
</details>

**Discusión**: Los comentaristas elogiaron la ingeniería de UPI y su adopción generalizada, señalando que incluso llevó a las generaciones mayores a los pagos digitales. Sin embargo, se expresaron preocupaciones sobre la privacidad de UPI, ya que requiere un número de teléfono y está vinculado a la identidad, y su control por parte del gobierno en lugar de redes de tarjetas privadas. Se establecieron comparaciones técnicas con otros sistemas basados en QR como PromptPay de Tailandia, y un usuario destacó la impresionante escala de UPI con 22 mil millones de transacciones anuales, lo que se traduce en un promedio de ~700 consultas por segundo en el conmutador de NPCI.

**Etiquetas**: `#UPI`, `#pagos digitales`, `#arquitectura de sistemas`, `#tecnología financiera`, `#India`

---

<a id="item-3"></a>
## [Anthias: 8 lanzamientos en 2 meses / reproducción de video finalmente arreglada en todas partes, placas ARM no Pi, HDMI-CEC, correcciones de seguridad y una biblioteca de aplicaciones gratuita.](https://www.reddit.com/r/selfhosted/comments/1uuai2v/anthias_8_releases_in_2_months_video_playback/) ⭐️ 8.0/10

Anthias lanza 8 versiones en 2 meses con reproducción de video arreglada, soporte para otras placas ARM, HDMI-CEC, correcciones de seguridad y una biblioteca de aplicaciones gratuita.

reddit · r/selfhosted · /u/514sid · jul 12, 09:16

**Etiquetas**: `#software de código abierto`, `#auto-hospedado`, `#señalización digital`, `#actualización de proyecto`, `#Raspberry Pi`

---

<a id="item-4"></a>
## [Mesh LLM: computación distribuida de IA en iroh](https://www.iroh.computer/blog/mesh-llm) ⭐️ 7.0/10

Mesh LLM permite la inferencia distribuida de modelos de lenguaje grandes a través de múltiples nodos utilizando la red iroh.

hackernews · tionis · jul 11, 22:38 · [Discusión](https://news.ycombinator.com/item?id=48876505)

**Etiquetas**: `#inferencia distribuida`, `#LLM`, `#iroh`, `#computación distribuida`, `#IA`

---

<a id="item-5"></a>
## [Nvidia, CoreWeave y Nebius: Dentro del financiamiento circular del boom de GPU](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 7.0/10

Un reportaje investigativo expone la dinámica de financiamiento circular entre Nvidia y los proveedores de nube de IA CoreWeave y Nebius, en la que las inversiones de capital de Nvidia ayudan a estas startups a comprar GPUs de Nvidia, distorsionando posiblemente la demanda real de infraestructura de IA. Si el auge de las GPU se sostiene en parte por financiamiento de proveedor en lugar de una demanda genuina, podría indicar una burbuja en infraestructura de IA, con riesgo de sobrecapacidad, pérdidas financieras y una corrección brusca en el gasto de hardware. Nvidia invirtió cerca de 2 mil millones de dólares por una participación del 9% en CoreWeave, cuyo plan de gasto de capital para 2026 asciende a 35 mil millones de dólares; es decir, la contribución directa de Nvidia equivale solo al 5.7% del CapEx de un año. Tanto CoreWeave como Nebius construyen grandes clústeres de GPUs Nvidia para cargas de trabajo de IA; CoreWeave opera un superordenador de 1.6 mil millones de dólares para Nvidia en Texas.

hackernews · adletbalzhanov · jul 11, 17:21 · [Discusión](https://news.ycombinator.com/item?id=48873836)

**Contexto**: El financiamiento circular, o vendor finance, es una práctica en la que un inversionista proporciona capital a una empresa que luego lo usa para comprar los productos del inversionista, creando un flujo de efectivo cerrado. Nvidia, el fabricante dominante de GPU para IA, ha invertido en proveedores de nube especializados como CoreWeave y Nebius para facilitar la adquisición de su hardware, lo que impulsa sus ventas y permite que estos 'neoclouds' escalen. Este modelo se ha expandido durante el auge de la IA, generando dudas sobre si la demanda reportada refleja una necesidad real de usuarios finales o se trata de un ciclo que se realimenta a sí mismo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Circular_financing">Circular financing</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group - Wikipedia</a></li>

</ul>
</details>

**Discusión**: La reacción de la comunidad es mixta: algunos sostienen que la participación de Nvidia es menor y que no es verdaderamente 'circular' dado el pequeño porcentaje sobre el CapEx de CoreWeave, mientras que otros consideran superado el debate sobre financiamiento circular y piden centrarse en métricas de rentabilidad como el ROI por token y los presupuestos empresariales de tokens. Otros comentarios plantean preocupaciones sobre la utilización de GPU y la viabilidad económica de hardware más antiguo como los H100.

**Etiquetas**: `#financiamiento circular`, `#GPU`, `#Nvidia`, `#CoreWeave`, `#infraestructura de IA`

---

<a id="item-6"></a>
## [Chat Control 1.0 de la UE aprobado entre controversia, aumentando urgencia por el autoalojamiento](https://www.reddit.com/r/selfhosted/comments/1uu0zv5/chat_control_10_was_passed_through_the_backdoor/) ⭐️ 7.0/10

Se informa que el Parlamento Europeo aprobó la legislación Chat Control 1.0 mientras muchos eurodiputados estaban de vacaciones, supuestamente impulsada por la presidenta Roberta Metsola. Esta legislación podría socavar la privacidad al permitir el escaneo de chats privados, afectando potencialmente a todos los ciudadanos de la UE e impulsando un cambio hacia servicios autoalojados para evadir la vigilancia. La ley aparentemente apunta a plataformas de comunicación para detectar material de abuso sexual infantil, pero los críticos advierten que podría romper el cifrado y sentar un precedente de vigilancia masiva. La próxima versión, Chat Control 2.0, aún está pendiente.

reddit · r/selfhosted · /u/HardwareIsHardWhere · jul 12, 00:56

**Contexto**: Chat Control es una propuesta legislativa controvertida de la UE destinada a combatir el abuso infantil en línea exigiendo a los proveedores de servicios escanear mensajes privados, incluidos los cifrados. Los defensores de la privacidad argumentan que viola los derechos fundamentales y debilita el cifrado. El autoalojamiento es la práctica de administrar sus propios servidores y servicios, otorgando a los usuarios control total sobre sus datos y reduciendo la dependencia de terceros que puedan cumplir con dichas leyes.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://better-paas.com/glossary/self-hosting">What Is self - hosting ? | Better-PaaS Glossary — Better-PaaS</a></li>
<li><a href="https://dockerspot.com/blog/why-self-hosting/">Why Self Hosting Matters in 2024: Control Your Data</a></li>
<li><a href="https://goong.com/word/selfhosting-meaning/">self - hosting Meaning | Goong.com - New Generation Dictionary</a></li>

</ul>
</details>

**Etiquetas**: `#privacidad`, `#autoalojamiento`, `#Chat Control`, `#UE`, `#legislación`

---

<a id="item-7"></a>
## [Ant: Un entorno de ejecución y ecosistema JavaScript con soporte de escritorio](https://antjs.org/) ⭐️ 6.0/10

Ant, anteriormente un entorno de ejecución JavaScript independiente, ahora incluye un gestor de paquetes, el registro ants.land, una plataforma de despliegue y Ant Desktop para construir aplicaciones de escritorio nativas. Ofrece una alternativa todo en uno a las herramientas JavaScript fragmentadas, simplificando potencialmente los flujos de trabajo de desarrollo y despliegue para aplicaciones web y de escritorio. El entorno de ejecución utiliza un motor JavaScript personalizado inicialmente derivado del motor Elk con licencia AGPL, pero el autor afirma que ha sido reimplementado; el ecosistema está en etapas tempranas y busca compatibilidad con herramientas JavaScript existentes.

hackernews · theMackabu · jul 11, 20:07 · [Discusión](https://news.ycombinator.com/item?id=48875377)

**Contexto**: El desarrollo moderno en JavaScript generalmente depende de herramientas separadas como Node.js para el entorno de ejecución, npm para paquetes y Electron para aplicaciones de escritorio. Han surgido ecosistemas unificados como Deno y Bun, pero Ant apunta a ofrecer una pila completa con su propio motor y registro.

**Discusión**: Los comentaristas expresaron preocupaciones sobre la originalidad del código debido al uso inicial del motor Elk con licencia AGPL, señalaron posible confusión con Apache Ant y solicitaron benchmarks. Algunos elogiaron el rápido esfuerzo de desarrollo en solitario detallado en las publicaciones del blog del autor.

**Etiquetas**: `#JavaScript`, `#Runtime`, `#Ecosistema`, `#Desarrollo web`, `#Herramientas de desarrollo`

---

<a id="item-8"></a>
## [Lanzamiento de Lanemu P2P VPN 0.14 con soporte RUDP y STUN](https://www.reddit.com/r/selfhosted/comments/1uu2kvt/released_lanemu_p2p_vpn_014_opensource/) ⭐️ 6.0/10

La versión 0.14 de Lanemu P2P VPN introduce el protocolo RUDP (Reliable User Datagram Protocol) como transporte por defecto, reemplazando TCP, y añade soporte STUN para atravesar NAT, junto con la instalación automática del controlador TAP en Windows. Esta alternativa de código abierto a Hamachi mejora la conectividad punto a punto detrás de NATs, haciendo que las configuraciones de VPN autogestionadas sean más accesibles y fiables para usuarios preocupados por la privacidad. RUDP opera sobre los puertos UDP n y n+1 con multiplexación para operaciones de cliente y servidor en un único puerto, por defecto el 5521; STUN utiliza stun.l.google.com de forma predeterminada, con alternativas configurables; y la aplicación ahora se ejecuta con privilegios de administrador en Windows.

reddit · r/selfhosted · /u/MonsterovichIsBack · jul 12, 02:12

**Contexto**: Lanemu es una herramienta VPN punto a punto de código abierto similar al propietario Hamachi, que permite que las computadoras se conecten como si estuvieran en una red local. RUDP (Reliable UDP) añade características de confiabilidad como confirmaciones y retransmisiones sobre UDP, mejorando el rendimiento para aplicaciones en tiempo real. STUN (Session Traversal Utilities for NAT) ayuda a los dispositivos detrás de NAT a descubrir sus direcciones IP y puertos públicos, permitiendo conexiones directas. Un controlador TAP es un adaptador de red virtual utilizado por el software VPN para crear un túnel para el tráfico.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reliable_User_Datagram_Protocol">Reliable User Datagram Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/STUN_protocol">STUN protocol</a></li>
<li><a href="https://www.thewindowsclub.com/tap-windows-adapters-vpn-driver">What is TAP-Windows Adapter? Where do I download it?</a></li>

</ul>
</details>

**Etiquetas**: `#VPN`, `#P2P`, `#código abierto`, `#autoalojamiento`, `#redes`

---

<a id="item-9"></a>
## [Archivando fotos RAW](https://www.reddit.com/r/selfhosted/comments/1utr47x/archiving_raw_photos/) ⭐️ 6.0/10

Un usuario comparte su método para reducir el tamaño de archivos RAW convirtiéndolos a formato DNG mediante herramientas automatizadas en Docker y Wine.

reddit · r/selfhosted · /u/skykery · jul 11, 18:04

**Etiquetas**: `#archivado de fotos`, `#automatización`, `#formato DNG`, `#Docker`, `#selfhosted`

---