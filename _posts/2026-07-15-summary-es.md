---
layout: default
title: "Horizon Summary: 2026-07-15 (ES)"
date: 2026-07-15
lang: es
---

> De 37 artículos, 22 fueron seleccionados por relevancia

---

1. [Secure Boot de Microsoft vulnerable durante una década por 'shims' no revocados](#item-1) ⭐️ 9.0/10
2. [Nueva York impone una prohibición de un año a la construcción de centros de datos](#item-2) ⭐️ 9.0/10
3. [Inyección de argumentos en Tailscale SSH permite acceso root](#item-3) ⭐️ 8.0/10
4. [La IA no resuelve los problemas de coordinación en software](#item-4) ⭐️ 8.0/10
5. [Cómo uso HTMX con Go](#item-5) ⭐️ 8.0/10
6. [Claude Engañado para Revelar Secretos de Memoria Persistente](#item-6) ⭐️ 8.0/10
7. [Vulnerabilidad de día cero en Cursor se divulga tras seis meses sin parche](#item-7) ⭐️ 8.0/10
8. [Nightingale: Karaoke autoalojado con ML local](#item-8) ⭐️ 8.0/10
9. [Computadoras de Jurassic Park en detalle exhaustivo](#item-9) ⭐️ 7.0/10
10. [El sitio web de la policía de Vancouver incluye botón de escape rápido](#item-10) ⭐️ 7.0/10
11. [Bonsai 27B: un modelo de clase 27B que se ejecuta en un teléfono](#item-11) ⭐️ 7.0/10
12. [Dependabot agrega cooldown predeterminado para actualizaciones](#item-12) ⭐️ 7.0/10
13. [Lobste.rs completa la migración de MariaDB a SQLite](#item-13) ⭐️ 7.0/10
14. [Citando a Armin Ronacher](#item-14) ⭐️ 7.0/10
15. [Subasta de T. rex de Sotheby's genera preocupación científica](#item-15) ⭐️ 7.0/10
16. [Demanda afirma que Meta usó IA para despedir a discapacitados](#item-16) ⭐️ 7.0/10
17. [Los tatuajes electrónicos pintados podrían ser el futuro de los biosensores portátiles](#item-17) ⭐️ 7.0/10
18. [Quartermaster: App nativa iOS para controlar servicios autogestionados](#item-18) ⭐️ 7.0/10
19. [Centros de datos orbitales: el desafío clave de los radiadores](#item-19) ⭐️ 6.0/10
20. [El ejército de EE.UU. usa botes dron explosivos en combate por primera vez](#item-20) ⭐️ 6.0/10
21. [Aumento de paywall en NocoDB impulsa a usuario a buscar alternativa FOSS](#item-21) ⭐️ 6.0/10
22. [Buscan plataforma autoalojada tras el muro de pago de la API de Strava](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Secure Boot de Microsoft vulnerable durante una década por 'shims' no revocados](https://arstechnica.com/security/2026/07/microsoft-secure-boot-has-been-broken-for-most-of-its-existence/) ⭐️ 9.0/10

Investigadores descubrieron que Microsoft no revocó 'shims' antiguos de Secure Boot durante la última década, lo que permite a atacantes eludir la protección de Secure Boot cargando binarios no verificados. Esto socava un pilar de la seguridad de Windows, permitiendo potencialmente que malware persista sin ser detectado tras reinicios del sistema. Las organizaciones que dependen de Secure Boot para la integridad de dispositivos están en mayor riesgo. La vulnerabilidad proviene de 'shims' antiguos (pequeños binarios tipo gestor de arranque firmados por Microsoft) que nunca se agregaron a la lista de revocación UEFI (dbx). Los atacantes pueden usar estos shims para cargar código sin firmar durante el arranque.

rss · Ars Technica · jul 14, 22:20

**Contexto**: Secure Boot es una característica UEFI que garantiza que solo se ejecute software de confianza durante el proceso de arranque, evitando malware de bajo nivel. Los 'shims' son pequeños gestores de arranque firmados por Microsoft que permiten que distribuciones Linux y otros SO arranquen en sistemas con Secure Boot habilitado. Microsoft revoca normalmente los shims vulnerables mediante actualizaciones de revocación UEFI, pero algunos shims antiguos fueron aparentemente pasados por alto.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.welivesecurity.com/en/eset-research/forgotten-uefi-shims-undermining-secure-boot/">Forgotten UEFI shims undermining Secure Boot</a></li>
<li><a href="https://github.com/rhboot/shim/blob/main/SBAT.md">shim/SBAT.md at main · rhboot/shim · GitHub</a></li>

</ul>
</details>

**Etiquetas**: `#seguridad`, `#ciberseguridad`, `#Microsoft`, `#Secure Boot`, `#vulnerabilidad`

---

<a id="item-2"></a>
## [Nueva York impone una prohibición de un año a la construcción de centros de datos](https://arstechnica.com/tech-policy/2026/07/new-york-is-the-first-state-to-impose-a-data-center-moratorium/) ⭐️ 9.0/10

El estado de Nueva York ha promulgado una moratoria de un año para la construcción de nuevos centros de datos, convirtiéndose en el primer estado en tomar esta medida. Esta moratoria podría sentar un precedente para otros estados y gobiernos locales preocupados por los impactos ambientales y de infraestructura de los centros de datos, afectando directamente la rápida expansión de la industria de la IA. La moratoria tiene una duración de un año, durante el cual el estado evaluará los efectos a largo plazo del desarrollo de centros de datos en las redes eléctricas, los recursos hídricos y las comunidades locales.

rss · Ars Technica · jul 14, 15:06

**Contexto**: Los centros de datos son grandes instalaciones que albergan servidores y equipos de red, consumiendo enormes cantidades de electricidad y agua para refrigeración. El auge de la IA ha acelerado la construcción de estos centros, generando preocupación por su huella ambiental y la presión sobre la infraestructura local.

**Etiquetas**: `#regulación`, `#centros de datos`, `#inteligencia artificial`, `#política tecnológica`, `#Nueva York`

---

<a id="item-3"></a>
## [Inyección de argumentos en Tailscale SSH permite acceso root](https://tailscale.com/security-bulletins) ⭐️ 8.0/10

Tailscale emitió un boletín de seguridad (TS-2026-009) detallando una vulnerabilidad crítica en su función SSH donde el manejo inadecuado de nombres de usuario permitía la inyección de argumentos, permitiendo a un usuario con acceso SSH obtener privilegios root en el host. Este es un grave error de escalada de privilegios que socava las garantías de seguridad de Tailscale SSH, permitiendo potencialmente a los atacantes comprometer completamente los nodos en una red Tailscale. Destaca los riesgos de confiar en implementaciones SSH de terceros en lugar de la probada OpenSSH. La vulnerabilidad se origina al pasar nombres de usuario directamente como argumentos al comando getent, lo que permite a un atacante inyectar indicadores como `-i` para desencadenar un inicio de sesión como root. Esto afecta a Tailscale SSH, que reemplaza a OpenSSH en el puerto 22 para conexiones Tailscale.

hackernews · jervant · jul 15, 01:08 · [Discusión](https://news.ycombinator.com/item?id=48915004)

**Contexto**: Tailscale es un servicio VPN que crea una red segura en malla utilizando WireGuard. Su función SSH proporciona autenticación basada en identidad y controles de acceso. La inyección de argumentos ocurre cuando una aplicación pasa entrada sin sanitizar a un subproceso, permitiendo a los atacantes agregar argumentos adicionales que alteran el comportamiento previsto. En este caso, el comando getent se invocó con argumentos controlados por el usuario, lo que llevó a una escalada de privilegios.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://tailscale.com/docs/features/tailscale-ssh">Tailscale SSH · Tailscale Docs</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/88.html">CWE - CWE-88: Improper Neutralization of Argument Delimiters in...</a></li>

</ul>
</details>

**Discusión**: Los comentarios reflejan una confianza mixta en Tailscale: algunos usuarios evitan Tailscale SSH por preferir el historial de seguridad de OpenSSH, mientras que otros se mantienen con Wireguard autoalojado. Un comentarista señaló que el error es una clase antigua de vulnerabilidad, y otro enfatizó el uso de llamadas al sistema en lugar de subprocesos.

**Etiquetas**: `#seguridad`, `#vulnerabilidad`, `#Tailscale`, `#SSH`, `#VPN`

---

<a id="item-4"></a>
## [La IA no resuelve los problemas de coordinación en software](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

El nuevo ensayo de Armin Ronacher argumenta que la programación asistida por IA no resuelve los problemas fundamentales de coordinación y comprensión que limitan los proyectos de software grandes. Esto desafía la narrativa predominante de que la IA acelerará drásticamente el desarrollo de software a gran escala, destacando que la coordinación—no la velocidad de codificación—es el cuello de botella principal. El ensayo discute la composabilidad y la 'Maldición de Lisp', comparándola con el Tetris, y señala que los agentes de IA pueden producir código rápidamente pero pueden violar la integridad arquitectónica.

hackernews · cdrnsf · jul 14, 16:57 · [Discusión](https://news.ycombinator.com/item?id=48909785)

**Contexto**: La composabilidad es el principio de construir software a partir de componentes reutilizables. En proyectos grandes, la coordinación entre desarrolladores se convierte en un cuello de botella a medida que el sistema crece. La 'Maldición de Lisp' se refiere a la idea de que los lenguajes de programación altamente flexibles como Lisp facilitan la creación de soluciones personalizadas, reduciendo el incentivo para crear código de propósito general y compartible, lo que puede dificultar la colaboración y la composabilidad.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Composability">Composability - Wikipedia</a></li>
<li><a href="https://www.mulesoft.com/integration/what-is-composability">What is composability? - MuleSoft</a></li>

</ul>
</details>

**Discusión**: Los comentaristas generalmente están de acuerdo con la tesis del artículo. tekacs compara la composabilidad con el Tetris, señalando que los agentes de IA a menudo violan las líneas arquitectónicas. ssivark conecta el argumento con la 'Maldición de Lisp', mientras que noisy_boy aconseja a los desarrolladores arreglar manualmente problemas pequeños en lugar de confiar en la IA para todo.

**Etiquetas**: `#complejidad del software`, `#programación asistida por IA`, `#composabilidad`, `#arquitectura de software`, `#ingeniería de software`

---

<a id="item-5"></a>
## [Cómo uso HTMX con Go](https://www.alexedwards.net/blog/how-i-use-htmx-with-go) ⭐️ 8.0/10

Guía detallada sobre cómo integrar HTMX con Go para construir aplicaciones web reactivas con mínima JavaScript. Este tutorial de un autor reconocido de Go ofrece orientación de alta calidad sobre la combinación de HTMX con Go, un tema que gana tracción entre desarrolladores que buscan crear aplicaciones reactivas con menos JavaScript. La discusión comunitaria que lo acompaña destaca los desafíos reales de adopción en equipos y herramientas complementarias como templ. La guía detalla cómo usar los atributos HTML personalizados de HTMX para enviar solicitudes AJAX y actualizar partes de la página sin recargas completas, todo procesado por el backend en Go con mínimo JavaScript en el frontend.

hackernews · gnabgib · jul 14, 19:55 · [Discusión](https://news.ycombinator.com/item?id=48912175)

**Contexto**: HTMX es una biblioteca JavaScript de código abierto creada por Carson Gross que extiende HTML con atributos personalizados para permitir interacciones dinámicas como AJAX y actualizaciones parciales de página sin escribir JavaScript. Sigue un enfoque hipermedia, permitiendo construir interfaces de usuario modernas solo con HTML y CSS. Go, con su biblioteca estándar y plantillas, se combina bien con HTMX para renderizado del lado del servidor y mínima complejidad en el frontend.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>

</ul>
</details>

**Discusión**: Los comentarios de la comunidad muestran experiencias mixtas. Algunos desarrolladores elogian HTMX por reducir JavaScript repetitivo y disfrutan combinarlo con Go, pero otros reportan dificultades al usarlo en proyectos grandes con estado complejo o para obtener la aceptación del equipo, ya que a veces es visto como 'no una tecnología seria'.

**Etiquetas**: `#Go`, `#HTMX`, `#Desarrollo web`, `#Golang`, `#Herramientas frontend`

---

<a id="item-6"></a>
## [Claude Engañado para Revelar Secretos de Memoria Persistente](https://www.ayush.digital/blog/the-memory-heist) ⭐️ 8.0/10

El autor ejecutó un ataque de inyección de instrucciones en Claude, un modelo de IA, obligándolo a revelar información confidencial almacenada en su memoria persistente. Esto demuestra una vulnerabilidad de seguridad en los sistemas de IA con capacidades de memoria. Esta vulnerabilidad podría permitir a actores malintencionados extraer datos sensibles de asistentes de IA, comprometiendo la privacidad del usuario. Destaca la necesidad de medidas de seguridad robustas en los sistemas de memoria de IA. El ataque utilizó un aviso de seguridad falso de Cloudflare para engañar a Claude y hacerle revelar recuerdos. El autor señaló la falta de un programa de bug bounty por parte de Anthropic, lo que generó críticas en la comunidad.

hackernews · macleginn · jul 15, 06:28 · [Discusión](https://news.ycombinator.com/item?id=48916975)

**Contexto**: La memoria persistente en los modelos de IA les permite recordar información a lo largo de las sesiones, mejorando la personalización. Sin embargo, estos datos pueden ser explotados mediante inyección de instrucciones, donde entradas adversarias eluden las salvaguardas para provocar comportamientos no deseados. El ataque de inyección de instrucciones descrito en la noticia es una explotación de ciberseguridad que aprovecha la incapacidad del modelo para distinguir entre instrucciones definidas por el desarrollador y las entradas del usuario.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.com/thedotmack/claude-mem">GitHub - thedotmack/ claude -mem: Persistent Context Across...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**Discusión**: La comunidad de Hacker News criticó a Anthropic por no ofrecer un programa de bug bounty. Algunos usuarios expresaron preocupaciones sobre la privacidad y la facilidad de extraer recuerdos, mientras que otros señalaron paralelismos con los problemas de seguridad de los inicios de Internet. Un usuario destacó que las personas a menudo proporcionan datos sensibles voluntariamente, pero el problema central sigue siendo la vulnerabilidad de la memoria de la IA.

**Etiquetas**: `#seguridad`, `#inteligencia artificial`, `#vulnerabilidad`, `#privacidad`, `#agentes`

---

<a id="item-7"></a>
## [Vulnerabilidad de día cero en Cursor se divulga tras seis meses sin parche](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 8.0/10

La firma de seguridad Mindgard reveló públicamente una vulnerabilidad de día cero en el editor de código Cursor que permite ejecución remota de código mediante un repositorio malicioso. La vulnerabilidad fue reportada en diciembre de 2025 pero no fue parcheada durante más de seis meses, lo que provocó la divulgación completa. Esta vulnerabilidad es crítica porque Cursor es ampliamente utilizado por desarrolladores y puede provocar ataques en la cadena de suministro si se clona un repositorio malicioso. La inacción del proveedor resalta los riesgos de depender de programas de recompensas por errores para la seguridad del producto. El problema surge porque Cursor se envía con Workspace Trust desactivado por defecto, lo que permite que los repositorios ejecuten comandos arbitrarios mediante un .exe malicioso o tasks.json con 'runOn': 'folderOpen'. La vulnerabilidad afecta a todas las versiones hasta la última probada, y no hay parche disponible a la fecha de divulgación.

hackernews · Synthetic7346 · jul 14, 17:58 · [Discusión](https://news.ycombinator.com/item?id=48910676)

**Contexto**: Cursor es un editor de código popular basado en Visual Studio Code con funciones de IA. Workspace Trust es una característica de seguridad que restringe la ejecución automática de código desde carpetas no confiables; desactivarla permite que repositorios maliciosos ejecuten comandos arbitrarios. Una vulnerabilidad de día cero se refiere a un fallo de seguridad desconocido para el proveedor o sin parche disponible. La divulgación completa es la práctica de revelar públicamente todos los detalles de una vulnerabilidad después de que el proveedor no la corrige a tiempo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left">Cursor 0day: When Full Disclosure Becomes the Only Protection ...</a></li>
<li><a href="https://thehackernews.com/2025/09/cursor-ai-code-editor-flaw-enables.html">Cursor AI Code Editor Flaw Enables Silent Code Execution via ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>

</ul>
</details>

**Discusión**: Los comentaristas señalan que el problema central es que Cursor desactiva Workspace Trust por defecto, haciéndolo inherentemente inseguro. Algunos argumentan que el vector de ataque requiere que un atacante coloque un archivo malicioso en el espacio de trabajo, lo que reduce la gravedad. También hay críticas sobre el uso de informes de seguridad generados por LLM, que pueden ser abrumadores y a menudo irrelevantes.

**Etiquetas**: `#vulnerabilidad`, `#cursor`, `#0day`, `#seguridad`, `#divulgación`

---

<a id="item-8"></a>
## [Nightingale: Karaoke autoalojado con ML local](https://www.reddit.com/r/selfhosted/comments/1ux2te3/i_built_nightingale_selfhosted_karaoke_from_your/) ⭐️ 8.0/10

Nightingale es una nueva aplicación de código abierto que convierte cualquier canción de la biblioteca musical local del usuario en una pista de karaoke, eliminando las voces, sincronizando las letras palabra por palabra y ofreciendo puntuación de tono en tiempo real, todo funcionando completamente sin conexión y sin dependencia de la nube. Este proyecto lleva capacidades de karaoke de nivel profesional al ecosistema autoalojado, permitiendo a los usuarios disfrutar del karaoke sin subir su música a servicios en la nube. Aprovecha modelos de ML de última generación para la separación de voces y transcripción, haciendo que el karaoke de alta calidad sea accesible y privado. Nightingale admite integración con Jellyfin y Navidrome, utiliza el modelo UVR o Demucs para la separación de voces y WhisperX para la transcripción, e incluye funciones como cambios de tono y tempo, tablas de puntuación por perfil y fondos reactivos al audio. Se distribuye como un único binario, imagen Docker o se puede desplegar mediante el modo web autoalojado.

reddit · r/selfhosted · /u/rzzzzru · jul 15, 11:11

**Contexto**: El karaoke típicamente requiere acceso a pistas instrumentales pre-hechas o servicios en la nube que eliminan las voces. Nightingale utiliza modelos de aprendizaje automático locales como UVR (Ultimate Vocal Remover) o Demucs para la separación de fuentes, y WhisperX para el reconocimiento automático del habla con marcas de tiempo a nivel de palabra. Estos modelos se ejecutan completamente en el hardware del usuario, garantizando la privacidad. La aplicación también admite la importación de canciones de UltraStar Deluxe y muestra letras con romanización para escrituras no latinas.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://nightingale.cafe/">Nightingale — Karaoke from your music library</a></li>
<li><a href="https://github.com/facebookresearch/demucs">GitHub - facebookresearch/demucs: Code for the paper Hybrid Spectrogram and Waveform Source Separation · GitHub</a></li>
<li><a href="https://github.com/m-bain/whisperX">GitHub - m-bain/whisperX: WhisperX: Automatic Speech ...</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojado`, `#karaoke`, `#ML local`, `#música`, `#código abierto`

---

<a id="item-9"></a>
## [Computadoras de Jurassic Park en detalle exhaustivo](https://fabiensanglard.net/jurrasic_park_computers/index.html) ⭐️ 7.0/10

Un artículo técnico documenta meticulosamente cada computadora y software visible en la película Jurassic Park de 1993, incluyendo hardware como estaciones de trabajo Silicon Graphics y la supercomputadora Cray X-MP. El artículo ofrece una mirada poco común al hardware real utilizado en una película emblemática, conectando la retrocomputación y la historia del cine para una audiencia técnica. El análisis cubre no solo las computadoras sino también el software, como el código del Macintosh Programmer's Workshop que aparece en pantalla, y revela secretos de producción como el uso de un prototipo de tableta Motorola Envoy.

hackernews · vinhnx · jul 15, 02:57 · [Discusión](https://news.ycombinator.com/item?id=48915709)

**Contexto**: En Jurassic Park, las computadoras jugaron un papel clave en la historia. La película presentó varios sistemas auténticos de alta gama de principios de los 90, incluyendo estaciones de trabajo Silicon Graphics para renderizar dinosaurios y una supercomputadora Cray X-MP para la secuenciación de ADN. Estas máquinas eran de última generación en ese momento.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://fabiensanglard.net/jurrasic_park_computers/index.html">Jurassic Park computers in excruciating detail</a></li>
<li><a href="https://en.wikipedia.org/wiki/SGI_Crimson">SGI Crimson - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cray_X-MP">Cray X-MP - Wikipedia</a></li>

</ul>
</details>

**Discusión**: Los comentaristas proporcionaron contexto adicional, como cómo se obtuvo el accesorio Motorola Envoy mediante un encuentro casual, y señalaron que el código en pantalla era del Macintosh Programmer's Workshop de Apple. También hubo correcciones técnicas y elogios por la profundidad del artículo.

**Etiquetas**: `#retrocomputación`, `#cine`, `#hardware clásico`, `#análisis técnico`, `#cultura pop`

---

<a id="item-10"></a>
## [El sitio web de la policía de Vancouver incluye botón de escape rápido](https://vpd.ca/) ⭐️ 7.0/10

El Departamento de Policía de Vancouver ha añadido un botón de 'Escape Rápido' a su sitio web que, al hacer clic, oculta inmediatamente el contenido del sitio, cambia el título del navegador y redirige a una página neutral como Google o Weather Canada, eliminando también la visita del historial del navegador. Esta función es crucial para víctimas de violencia doméstica que pueden estar navegando buscando ayuda y necesitan abandonar rápidamente el sitio sin dejar rastros digitales. Destaca una tendencia creciente en los sitios web gubernamentales de priorizar la seguridad y privacidad del usuario. La implementación utiliza JavaScript para establecer document.opacity en 0, cambiar document.title a 'New Tab', abrir una nueva ventana con un sitio neutral y luego reemplazar la ubicación actual con otro sitio neutral. Sin embargo, este patrón tiene limitaciones ya que no puede borrar completamente el historial de todas las fuentes, como los registros del router o la caché del navegador.

hackernews · LookAtThatBacon · jul 15, 00:15 · [Discusión](https://news.ycombinator.com/item?id=48914644)

**Contexto**: El patrón 'Escape Rápido' es un patrón de diseño web utilizado por varios sitios web gubernamentales y de servicios sociales para ayudar a los usuarios a salir rápidamente de una página si están en una situación peligrosa. Fue pionero del Servicio Digital del Gobierno del Reino Unido y también se utiliza en Nueva Zelanda y Canadá. El botón típicamente abre un sitio neutral e intenta prevenir la detección al no almacenar el tráfico en el historial de sesión del navegador.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://www.alberta.ca/quick-escape-button">Quick Escape button | Alberta.ca</a></li>
<li><a href="https://www.health.columbia.edu/content/quick-escape-button">The Quick Escape Button | Columbia Health</a></li>

</ul>
</details>

**Discusión**: Los comentaristas señalaron que existen patrones similares en gov.uk y en sitios web gubernamentales de Nueva Zelanda, mencionando el patrón 'Salir de una página rápidamente' del Sistema de Diseño del Gobierno del Reino Unido. Otro comentarista discutió la ventana emergente 'Sitio Protegido' utilizada en Nueva Zelanda. Algunos compartieron detalles de implementación y limitaciones, como que el patrón no puede proteger contra todas las formas de vigilancia.

**Etiquetas**: `#seguridad`, `#privacidad`, `#desarrollo web`, `#gobierno`, `#diseño`

---

<a id="item-11"></a>
## [Bonsai 27B: un modelo de clase 27B que se ejecuta en un teléfono](https://prismml.com/news/bonsai-27b) ⭐️ 7.0/10

PrismML anunció Bonsai 27B, un modelo de lenguaje de 27 mil millones de parámetros que puede ejecutarse completamente en un teléfono inteligente moderno mediante cuantización agresiva, incluyendo variantes de 1 bit y 2 bits con contexto de 262K tokens. Este avance permite que un modelo de clase 27B se ejecute en un teléfono, haciendo que la IA avanzada sea accesible en dispositivos de consumo y potencialmente acelerando la adopción de IA en el borde y la inferencia que preserva la privacidad. Bonsai 27B utiliza atención híbrida (75% atención lineal) y cuantización de caché KV de 4 bits para caber en un dispositivo móvil, e incluye un decodificador especulativo DSpark para generación más rápida. Está disponible en formatos GGUF con cuantización de pesos de 1 y 2 bits.

hackernews · xenova · jul 14, 17:50 · [Discusión](https://news.ycombinator.com/item?id=48910545)

**Contexto**: Los modelos de lenguaje grandes generalmente requieren GPUs potentes o servidores en la nube. La cuantización es una técnica que reduce la precisión de los pesos del modelo (por ejemplo, de 16 bits a 1 o 2 bits), reduciendo drásticamente el uso de memoria mientras se intenta preservar el rendimiento. Bonsai 27B utiliza cuantización avanzada y atención híbrida para llevar un modelo de 27 mil millones de parámetros al hardware móvil.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">Announcing Bonsai 27 B : The First 27 B -Class Model to Run on a Phone</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf">prism-ml/Ternary-Bonsai-27B-gguf · Hugging Face</a></li>

</ul>
</details>

**Discusión**: La discusión comunitaria incluye solicitudes de comparaciones con otros modelos pequeños cuantizados como Gemma 4 12B, preguntas sobre la degradación del rendimiento en llamadas a herramientas, y evaluaciones comparativas de inferencia en CPU. Algunos usuarios también notaron noticias de que Apple está en conversaciones con PrismML, lo que genera especulaciones sobre una posible integración.

**Etiquetas**: `#Modelos de lenguaje`, `#Cuantización`, `#Dispositivos móviles`, `#Benchmarking`, `#IA eficiente`

---

<a id="item-12"></a>
## [Dependabot agrega cooldown predeterminado para actualizaciones](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/) ⭐️ 7.0/10

Dependabot ahora impone un período de espera de tres días antes de abrir solicitudes de extracción para nuevas versiones de paquetes. Esta política busca reducir el riesgo de actualizar a paquetes con errores o maliciosos, pero puede retrasar actualizaciones de seguridad críticas. El cooldown está habilitado por defecto y no se reinicia si se publica una versión corregida dentro de los tres días.

hackernews · woodruffw · jul 14, 21:15 · [Discusión](https://news.ycombinator.com/item?id=48913050)

**Contexto**: Dependabot es una herramienta de GitHub que automatiza las actualizaciones de dependencias. Un cooldown de paquete es un período de retraso que da tiempo a los mantenedores para detectar y reportar problemas antes de que una nueva versión se adopte ampliamente.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/">Dependabot version updates introduce default package cooldown</a></li>
<li><a href="https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference">Dependabot options reference - GitHub Docs</a></li>

</ul>
</details>

**Discusión**: Algunos comentaristas se preocupan de que los cooldowns generalizados reduzcan las posibilidades de detectar vulnerabilidades graves tempranamente. Otros señalan que esto refleja prácticas tradicionales de gestión de paquetes de distribuciones. Varios usuarios critican el enfoque dogmático de actualizaciones frecuentes, argumentando que puede priorizar el cambio sobre la estabilidad.

**Etiquetas**: `#Dependabot`, `#actualizaciones`, `#cooldown`, `#seguridad`, `#dependencias`

---

<a id="item-13"></a>
## [Lobste.rs completa la migración de MariaDB a SQLite](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 7.0/10

Lobste.rs migró su base de datos principal de MariaDB a SQLite, completando la transición durante el fin de semana. El sitio ahora funciona en un solo VPS con una base de datos SQLite principal de 3.8GB, junto con bases de datos de caché, cola y limitación de tasas. Esta migración demuestra que SQLite puede funcionar eficazmente como base de datos principal para un sitio comunitario en producción con miles de visitantes diarios, reduciendo costos y mejorando el rendimiento. Proporciona un caso de estudio convincente para otros proyectos que consideren alejarse de sistemas de bases de datos más pesados. La migración implicó una solicitud de extracción que agregó 735 líneas y eliminó 593 en 188 archivos. El sitio ahora usa cuatro bases de datos SQLite separadas: una base de datos principal de 3.8GB, un caché de 1.1GB, una cola de 218MB y una base de datos rack_attack de 555MB para la limitación de tasas.

rss · Simon Willison · jul 14, 19:44

**Contexto**: Lobste.rs es un sitio de agregación de enlaces impulsado por la comunidad centrado en tecnología y computación, similar a Hacker News. Originalmente usaba MariaDB, una base de datos relacional derivada de MySQL. SQLite es un motor de base de datos autónomo y sin servidor que almacena datos en un solo archivo, lo que lo hace liviano y fácil de administrar. La migración buscaba reducir los costos de alojamiento y mejorar el rendimiento al consolidarse en un solo VPS.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/Lobsters">Lobste.rs</a></li>
<li><a href="https://en.wikipedia.org/wiki/MariaDB">MariaDB</a></li>
<li><a href="https://daily.dev/blog/sqlite-production-guide-when-how-to-use-beyond-prototyping/">SQLite for Production: When and How to Use It Beyond ...</a></li>

</ul>
</details>

**Discusión**: La comunidad de Lobste.rs informó resultados positivos, notando un uso significativamente menor de CPU y memoria y un sitio más ágil. La migración se considera estable y la nueva arquitectura es permanente. El hilo también incluye discusión técnica sobre la implementación y las compensaciones.

**Etiquetas**: `#SQLite`, `#bases de datos`, `#Rails`, `#migración`, `#rendimiento`

---

<a id="item-14"></a>
## [Citando a Armin Ronacher](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything) ⭐️ 7.0/10

Reflexión sobre cómo el lenguaje compartido en proyectos de software se mantiene mediante fricción y cómo los agentes podrían alterar ese proceso.

rss · Simon Willison · jul 14, 18:04

**Etiquetas**: `#arquitectura de software`, `#cultura de desarrollo`, `#agentes de IA`, `#comunicación en equipos`

---

<a id="item-15"></a>
## [Subasta de T. rex de Sotheby's genera preocupación científica](https://arstechnica.com/science/2026/07/sothebys-big-t-rex-auction-raises-concerns-hype-and-wealth-are-upending-science/) ⭐️ 7.0/10

La subasta de un esqueleto de Tyrannosaurus rex por Sotheby's ha generado preocupación de que la riqueza privada está superando a los museos, obstaculizando la investigación científica. Esta tendencia podría privar a los paleontólogos del acceso a fósiles cruciales, potencialmente ralentizando los descubrimientos sobre la biología y evolución de los dinosaurios. La venta ejemplifica cómo las subastas de alto perfil están dificultando que las instituciones públicas compitan con coleccionistas privados.

rss · Ars Technica · jul 15, 10:30

**Contexto**: Las subastas de fósiles se han vuelto cada vez más comunes, con especímenes raros alcanzando millones de dólares. Los museos dependen de estos fósiles para la investigación y la educación, pero los compradores privados a menudo los adquieren para exhibición personal o inversión.

**Etiquetas**: `#Ciencia`, `#Paleontología`, `#Subastas`, `#Fósiles`, `#Investigación`

---

<a id="item-16"></a>
## [Demanda afirma que Meta usó IA para despedir a discapacitados](https://arstechnica.com/tech-policy/2026/07/lawsuit-claims-metas-layoff-decisions-were-made-by-ai-not-humans/) ⭐️ 7.0/10

Una demanda alega que Meta utilizó inteligencia artificial para tomar decisiones de despido, apuntando específicamente a trabajadores con discapacidades y problemas médicos, sin supervisión humana. De ser cierto, este caso resalta serias preocupaciones éticas y legales sobre el sesgo algorítmico en decisiones de recursos humanos, afectando potencialmente a miles de trabajadores y sentando un precedente para la responsabilidad de la IA en el empleo. Meta niega las acusaciones, afirmando que no usó IA para despedir a trabajadores con discapacidades o condiciones médicas. La demanda plantea preguntas sobre la transparencia en los sistemas automatizados de toma de decisiones.

rss · Ars Technica · jul 14, 20:05

**Contexto**: La ética algorítmica es un campo en expansión que examina las implicaciones morales de las decisiones automatizadas tomadas por IA. Los sistemas de IA utilizados en recursos humanos pueden perpetuar sesgos presentes en los datos de entrenamiento, lo que lleva a resultados discriminatorios. Varios estudios han demostrado que la IA utilizada en decisiones de contratación y despido puede reducir la diversidad y apuntar injustamente a grupos protegidos. Este caso subraya la necesidad de regulación y supervisión de la IA en el lugar de trabajo.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://proyectoscio.ucv.es/articulos-filosoficos/articulos_fondo/de-que-hablamos-cuando-hablamos-de-etica-algoritmica/">¿De qué hablamos cuando hablamos de ética algorítmica? - UCV</a></li>
<li><a href="https://www.infobae.com/tecno/2025/01/28/aumenta-la-discriminacion-en-las-empresas-por-el-uso-de-ia-al-momento-de-contratar-empleados/">Aumenta la discriminación en las empresas por el uso de IA al momento de contratar empleados - Infobae</a></li>
<li><a href="https://dialogos.justiciajujuy.gov.ar/index.php/dvj/en/article/download/36/47/98?inline=1">Del trabajo decente al trabajo emergente: La inteligencia artificial como derecho humano y nuevo factor de desigualdad laboral</a></li>

</ul>
</details>

**Etiquetas**: `#inteligencia artificial`, `#Meta`, `#despidos`, `#ética algorítmica`, `#demanda`

---

<a id="item-17"></a>
## [Los tatuajes electrónicos pintados podrían ser el futuro de los biosensores portátiles](https://arstechnica.com/science/2026/07/these-painted-e-tattoos-could-be-the-future-of-wearable-biosensors/) ⭐️ 7.0/10

Investigadores han desarrollado un método para pintar tinta conductora directamente sobre la piel en diseños personalizados, que se seca formando electrodos funcionales para biosensores. Esta innovación cierra la brecha entre la monitorización médica y la expresión personal, potencialmente aumentando el cumplimiento y la adopción de biosensores portátiles. La tinta conductora se seca formando electrodos que pueden medir biopotenciales como el ritmo cardíaco o la actividad muscular, y los tatuajes son temporales, durando solo unos días.

rss · Ars Technica · jul 14, 17:31

**Contexto**: Los tatuajes electrónicos son dispositivos portátiles suaves equipados con sensores que se adhieren a la piel para recopilar datos, a menudo utilizando materiales conductores como el grafeno o el carbono. La tinta conductora es una tinta que conduce electricidad, típicamente hecha al infundir grafito, nanopartículas de plata o materiales basados en carbono en un vehículo líquido. La capacidad de pintar dicha tinta directamente sobre la piel en diseños personalizados podría hacer que los tatuajes electrónicos sean más accesibles y personalizados.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conductive_ink">Conductive ink</a></li>
<li><a href="https://builtin.com/hardware/electronic-tattoo">What Is an Electronic Tattoo? - Built In What Is an Electronic Tattoo and How Does It Work? How Electronic Tattoos Work - HowStuffWorks Digital Tattoo Tech: Are Biometric Tattoos the Ultimate ... Researchers Develop Novel Electronic Tattoos for Wearable Tech What is a Digital Tattoo? Digital Tattoos Explained - The ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Biosensor">Biosensor</a></li>

</ul>
</details>

**Etiquetas**: `#Biosensores`, `#Tatuajes electrónicos`, `#Tinta conductora`, `#Wearables`, `#Tecnología portátil`

---

<a id="item-18"></a>
## [Quartermaster: App nativa iOS para controlar servicios autogestionados](https://www.reddit.com/r/selfhosted/comments/1uwq1rk/quartermaster_a_native_ios_app_for_controlling/) ⭐️ 7.0/10

Quartermaster, una aplicación iOS nativa que funciona como cliente puro para controlar servicios autogestionados, ha sido lanzada en la App Store con soporte para 41 servicios, sin backend y con almacenamiento cifrado de credenciales localmente. Esto es importante porque ofrece una forma segura y privada de administrar una amplia gama de servicios autogestionados directamente desde un iPhone, sin dependencia de la nube, lo que atrae a los usuarios que priorizan la soberanía de datos y el control. Quartermaster está construido con React Native, Expo y TypeScript con elementos de Swift UI, es de código cerrado, y ofrece una versión Pro de £14.99 único o £3.99/mes con una prueba de 7 días; se conecta a 41 servicios como Radarr, Sonarr, Plex y Home Assistant.

reddit · r/selfhosted · /u/Swityyyy · jul 15, 00:13

**Contexto**: Los servicios autogestionados son aplicaciones que los usuarios ejecutan en su propio hardware por privacidad y control. Quartermaster se conecta a servicios populares como Prowlarr, NZBHydra2 y Bazarr, que se utilizan para gestión de indexadores y descarga de subtítulos, respectivamente. La aplicación consolida estos en un único panel de iOS sin necesidad de un servidor central.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://prowlarr.com/">Prowlarr</a></li>
<li><a href="https://github.com/theotherp/nzbhydra2">GitHub - theotherp/nzbhydra2: Usenet meta search</a></li>

</ul>
</details>

**Etiquetas**: `#iOS`, `#autohosting`, `#cliente puro`, `#servicios autogestionados`, `#privacidad`

---

<a id="item-19"></a>
## [Centros de datos orbitales: el desafío clave de los radiadores](https://arstechnica.com/space/2026/07/how-hard-is-it-to-build-orbital-data-centers-actually/) ⭐️ 6.0/10

Un artículo de Ars Technica explora la viabilidad de los centros de datos orbitales, destacando la necesidad de radiadores más baratos y ligeros. Reducir el costo y el peso de los radiadores es crítico para hacer viables económicamente los centros de datos orbitales, lo que podría permitir la IA basada en el espacio y la computación en el borde. Los radiadores espaciales actuales, como los de la ISS, son costosos y masivos; se están explorando diseños innovadores como los radiadores de gotas líquidas para superar estas limitaciones.

rss · Ars Technica · jul 15, 11:00

**Contexto**: Los centros de datos orbitales son instalaciones propuestas en el espacio que procesarían datos en órbita, aprovechando la energía solar continua y la baja latencia para ciertas aplicaciones. El concepto tiene raíces históricas en arquitecturas militares como el programa Brilliant Pebbles. La gestión térmica en el espacio es un desafío debido a la falta de atmósfera para convección, lo que hace que los radiadores sean un componente clave.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Orbital_data_centers">Orbital data centers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Liquid_droplet_radiator">Liquid droplet radiator - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#centros de datos orbitales`, `#radiadores`, `#infraestructura espacial`, `#innovación`, `#artículo especulativo`

---

<a id="item-20"></a>
## [El ejército de EE.UU. usa botes dron explosivos en combate por primera vez](https://arstechnica.com/ai/2026/07/us-military-sent-explosive-drone-boats-into-combat-for-the-first-time/) ⭐️ 6.0/10

Por primera vez, el ejército estadounidense desplegó vehículos de superficie no tripulados (USV, por sus siglas en inglés) cargados con explosivos en combate, atacando un submarino enano y un puerto naval iraní en una reciente escalada. Este despliegue representa un hito importante en el uso de sistemas no tripulados para misiones de ataque, lo que podría remodelar las tácticas navales y provocar un debate sobre la guerra autónoma. Los botes dron unidireccionales, capaces de transportar más de 400 kilogramos de explosivos, se utilizaron como armas de ataque contra fuerzas iraníes, marcando su primer uso en combate por parte de EE.UU.

rss · Ars Technica · jul 14, 18:00

**Contexto**: Los vehículos de superficie no tripulados se han utilizado en conflictos recientes, notablemente por los rebeldes hutíes en Yemen y Ucrania contra objetivos rusos. Estos drones suicidas están diseñados para misiones de ida y han evolucionado desde simples botes controlados por control remoto hasta sistemas sofisticados guiados por GPS. Estados Unidos había probado estos sistemas anteriormente, pero no los había usado en combate real hasta ahora.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/07/us-military-sent-explosive-drone-boats-into-combat-for-the-first-time/">US military sent explosive drone boats into combat for... - Ars Technica</a></li>
<li><a href="https://www.abc.net.au/news/2026-07-15/us-uses-explosive-drone-speedboats-against-iran-for-first-time/106912714">US uses explosive one-way drone boats for first time in combat...</a></li>

</ul>
</details>

**Etiquetas**: `#drones`, `#tecnología militar`, `#combate autónomo`, `#vehículos no tripulados`

---

<a id="item-21"></a>
## [Aumento de paywall en NocoDB impulsa a usuario a buscar alternativa FOSS](https://www.reddit.com/r/selfhosted/comments/1ux1ke8/nocodb_paywall_creep_looking_for_selfhosted_foss/) ⭐️ 6.0/10

Un usuario de Reddit anunció que abandona NocoDB debido al creciente número de funciones en la edición comunitaria que se han movido tras un muro de pago, y busca una alternativa autogestionada de código abierto con interfaz tipo hoja de cálculo. Esto resalta una frustración común en la comunidad de autogestión cuando los proyectos de código abierto monetizan agresivamente, y genera debate sobre alternativas viables que sigan siendo completamente de código abierto y autogestionables. El usuario necesita específicamente un frontend para una base de datos PostgreSQL existente, no un creador de aplicaciones que sea dueño del esquema, y requiere una interfaz tipo hoja de cálculo para que miembros no técnicos del equipo puedan navegar, filtrar y editar filas.

reddit · r/selfhosted · /u/Efficient_View_3885 · jul 15, 10:07

**Contexto**: NocoDB es una plataforma de código abierto que convierte bases de datos en interfaces tipo hoja de cálculo, similar a Airtable. Ofrece una edición comunitaria, pero también funciones empresariales de pago. Recientemente, más funciones se han movido tras un muro de pago, lo que ha llevado a usuarios de largo plazo a buscar alternativas como Baserow o Grist, que ofrecen funcionalidad similar sin restricciones de pago.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://grokipedia.com/page/NocoDB">NocoDB</a></li>
<li><a href="https://alternativeto.net/software/airtable/?platform=self-hosted">Airtable Alternatives : Top 17 Self - Hosted Team... | AlternativeTo</a></li>

</ul>
</details>

**Etiquetas**: `#self-hosting`, `#FOSS`, `#NocoDB`, `#alternativas`, `#bases de datos`

---

<a id="item-22"></a>
## [Buscan plataforma autoalojada tras el muro de pago de la API de Strava](https://www.reddit.com/r/selfhosted/comments/1ux10xp/what_platform_for_sports_activities/) ⭐️ 6.0/10

Un usuario busca una plataforma autoalojada que reemplace la API de Strava para sincronizar actividades de un reloj Coros, ya que Strava ahora cobra una tarifa mensual por el acceso a su API. Esto es importante porque muchos atletas que autoalojan dependen de la API gratuita de Strava para acceder a sus propios datos. El muro de pago obliga a los usuarios a buscar alternativas abiertas, lo que se alinea con la filosofía de autoalojamiento y podría impulsar la adopción de soluciones de fitness autoalojadas. El usuario ha solicitado acceso a la plataforma de desarrollo de Coros pero espera poco. Busca una plataforma que se conecte a Coros o Strava y ofrezca acceso a la API con webhooks para activar descargas automáticas.

reddit · r/selfhosted · /u/paranoid-alkaloid · jul 15, 09:36

**Contexto**: Strava es una red social popular para atletas que proporciona una API para aplicaciones de terceros. Recientemente, Strava anunció un muro de pago para el acceso a la API, cobrando 11,99 dólares al mes. Los relojes Coros registran actividades pero tienen un ecosistema cerrado, lo que dificulta la exportación directa de datos sin un intermediario.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://communityhub.strava.com/developers-api-7/new-strava-api-update-what-the-message-means-13433">New STRAVA API UPDATE, what the message means</a></li>
<li><a href="https://futureprompt.org/stravas-api-paywall-signals-a-bigger-reckoning/">Strava's API paywall signals a bigger reckoning - Future ...</a></li>
<li><a href="https://coaio.com/news/2026/06/stravas-api-paywall-fighting-scrapers-and-prepping-for-a-massive-ipo-2s4c/">Strava's API Paywall: Fighting Scrapers and Prepping for a ...</a></li>

</ul>
</details>

**Etiquetas**: `#autoalojamiento`, `#deportes`, `#API`, `#Strava`, `#Coros`

---