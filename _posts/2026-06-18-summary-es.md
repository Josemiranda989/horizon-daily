---
layout: default
title: "Horizon Summary: 2026-06-18 (ES)"
date: 2026-06-18
lang: es
---

> De 14 artículos, 10 fueron seleccionados por relevancia

---

1. [GLM-5.2: El LLM de solo texto con pesos abiertos más potente](#item-1) ⭐️ 9.0/10
2. [Filtración masiva expone credenciales de Oracle, Lenovo, FedEx y contratista de la OTAN](#item-2) ⭐️ 9.0/10
3. [Tesco migra 40.000 cargas desde VMware por alza del 175%](#item-3) ⭐️ 8.0/10
4. [Charity Majors: la IA hace el código instantáneo y desechable](#item-4) ⭐️ 7.0/10
5. [Amazon y QuEra prometen corrección de errores cuánticos útil para 2028](#item-5) ⭐️ 7.0/10
6. [Agentes de programación de IA enseñan a robots a instalar GPUs y cortar bridas](#item-6) ⭐️ 7.0/10
7. [California acusa a AT&T de mentir a la FCC para cerrar su antigua red telefónica](#item-7) ⭐️ 6.0/10
8. [IA peligrosas con capacidades de hackeo serán inevitables](#item-8) ⭐️ 6.0/10
9. [Altavoz Google Home con Gemini ya en preventa por $100](#item-9) ⭐️ 6.0/10
10. [Demuelen torres históricas del transbordador espacial en Vandenberg para SpaceX](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [GLM-5.2: El LLM de solo texto con pesos abiertos más potente](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai lanzó GLM-5.2, un modelo de solo texto con arquitectura Mixture of Experts de 753B parámetros, ventana de contexto de 1 millón de tokens y licencia MIT. Ahora lidera clasificaciones como el Índice de Inteligencia de Artificial Analysis entre modelos de pesos abiertos. Este lanzamiento demuestra que los modelos de pesos abiertos pueden superar a los propietarios en rendimiento, democratizando el acceso a IA de vanguardia. Su licencia MIT permisiva permite un amplio uso comercial e investigativo, acelerando potencialmente la innovación en múltiples sectores. A pesar de su tamaño, solo 40B parámetros están activos por token gracias a Mixture of Experts. Es intensivo en tokens, usando 43k tokens de salida por tarea de referencia, y ocupa el segundo lugar en Code Arena WebDev a pesar de carecer de entrada de imágenes.

rss · Simon Willison · jun 17, 23:58

**Contexto**: Mixture of Experts (MoE) es una arquitectura de aprendizaje automático que combina múltiples redes 'expertas' pequeñas, activando solo un subconjunto por entrada, lo que permite enormes cantidades de parámetros totales con costos de inferencia manejables. 'Pesos abiertos' significa que los parámetros del modelo entrenado están disponibles públicamente, pero a diferencia del código abierto completo, los datos y código de entrenamiento pueden no compartirse.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights : not quite what you’ve been told – Open Source Initiative</a></li>

</ul>
</details>

**Etiquetas**: `#modelos de lenguaje`, `#código abierto`, `#inteligencia artificial`, `#GLM-5.2`, `#procesamiento de lenguaje natural`

---

<a id="item-2"></a>
## [Filtración masiva expone credenciales de Oracle, Lenovo, FedEx y contratista de la OTAN](https://arstechnica.com/security/2026/06/massive-breach-spills-credentials-for-thousands-of-sensitive-networks/) ⭐️ 9.0/10

Una filtración masiva de datos ha expuesto credenciales de acceso de miles de redes sensibles, afectando a grandes organizaciones como Oracle, Lenovo, FedEx, un contratista de la OTAN y Fortinet. Esta brecha supone un grave riesgo de seguridad, ya que las credenciales comprometidas podrían permitir el acceso no autorizado a redes corporativas y de defensa, con posibles robos de datos, espionaje o interrupciones operativas. Cabe destacar que la brecha comprometió a un contratista de la OTAN y a Fortinet, un importante proveedor de ciberseguridad, lo que aumenta la preocupación por ataques a la cadena de suministro y la exposición de redes relacionadas con la defensa.

rss · Ars Technica · jun 17, 19:54

**Contexto**: Una filtración de datos ocurre cuando se accede a información confidencial sin autorización. Las credenciales, como nombres de usuario y contraseñas, son un objetivo frecuente porque permiten el acceso directo a redes y sistemas. En este incidente se filtraron miles de credenciales, afectando a empresas destacadas y a un contratista de defensa, con posibles implicaciones para la seguridad nacional.

**Etiquetas**: `#ciberseguridad`, `#filtración de datos`, `#credenciales comprometidas`, `#redes sensibles`, `#vulnerabilidad`

---

<a id="item-3"></a>
## [Tesco migra 40.000 cargas desde VMware por alza del 175%](https://arstechnica.com/information-technology/2026/06/tesco-moving-40000-server-workloads-off-vmware-amid-broadcoms-abusive-conduct/) ⭐️ 8.0/10

Tesco, un importante minorista del Reino Unido, está migrando 40.000 cargas de trabajo desde VMware a otras plataformas después de que Broadcom aumentara las tarifas de licencia en aproximadamente un 175%. La medida se produce tras demandas judiciales en el Reino Unido donde Tesco acusó a Broadcom de 'conducta abusiva'. Esto subraya la creciente fricción entre los clientes empresariales de TI y Broadcom tras su adquisición de VMware por 69 mil millones de dólares, ya que los fuertes aumentos de precios impulsan migraciones a gran escala. Podría indicar un cambio más amplio alejándose de la posición dominante de VMware en el mercado de virtualización. Tesco citó un aumento del 175% en documentos judiciales del Reino Unido, y la migración de 40.000 cargas de trabajo en servidores representa un enorme proyecto de TI. No se revelaron plazos ni tecnologías de reemplazo, pero el desafío legal subraya la gravedad de la carga de costos.

rss · Ars Technica · jun 17, 19:43

**Contexto**: VMware es una empresa líder en virtualización que permite ejecutar múltiples máquinas virtuales en un solo servidor físico, reduciendo los costos de hardware. Broadcom adquirió VMware en 2023 por 69 mil millones de dólares y desde entonces ha reestructurado las licencias, lo que ha provocado aumentos de precios significativos. Broadcom tiene un historial de aumentar los precios del software después de las adquisiciones, lo que genera rechazo de los clientes. Tesco opera una gran infraestructura de TI para su negocio minorista, lo que hace que esta migración sea un esfuerzo complejo y costoso.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VMware">VMware</a></li>

</ul>
</details>

**Etiquetas**: `#VMware`, `#Broadcom`, `#migración`, `#virtualización`, `#costos`

---

<a id="item-4"></a>
## [Charity Majors: la IA hace el código instantáneo y desechable](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 7.0/10

En 2025, la IA invirtió la economía de la producción de código, volviéndola gratuita e instantánea, y convirtiendo las líneas de código de un recurso cuidadosamente seleccionado a un producto desechable y regenerable. Este cambio de paradigma permite prototipados e iteraciones más rápidos, pero exige una mayor disciplina de ingeniería para gestionar el mayor volumen de código generado y garantizar la calidad y la seguridad. La cita proviene de un artículo donde se argumenta que la IA exige más disciplina de ingeniería, ya que la generación de código desechable puede dar lugar a montones de código no verificado y mal comprendido sin pruebas y revisiones rigurosas.

rss · Simon Willison · jun 17, 17:12

**Contexto**: Charity Majors es ingeniera de software y cofundadora de Honeycomb.io, conocida por sus reflexiones sobre observabilidad y cultura de ingeniería. Su cita captura el momento en que las herramientas de programación asistida por IA alcanzaron un punto de inflexión, reduciendo drásticamente el coste de generar código. Este cambio guarda paralelismo con transiciones históricas como el paso de productos artesanales a bienes producidos en masa, que requirieron nuevas disciplinas en diseño, pruebas y gestión.

**Etiquetas**: `#Inteligencia Artificial`, `#Programación Asistida por IA`, `#Ingeniería de Software`, `#Generación de Código`, `#Charity Majors`

---

<a id="item-5"></a>
## [Amazon y QuEra prometen corrección de errores cuánticos útil para 2028](https://arstechnica.com/science/2026/06/amazon-quera-promise-useful-quantum-error-correction-by-2028/) ⭐️ 7.0/10

Amazon y QuEra han anunciado una hoja de ruta para lograr una corrección de errores cuánticos práctica para 2028, mucho antes de lo que muchos expertos anticipaban, lo que podría permitir una computación cuántica tolerante a fallos antes de lo esperado. La corrección de errores cuánticos práctica es un hito crítico para construir computadoras cuánticas fiables a gran escala. Lograrlo para 2028 podría acelerar los plazos para aplicaciones reales en descubrimiento de fármacos, ciencia de materiales y criptografía. La promesa proviene de Amazon Web Services (AWS) y QuEra Computing, que colaboran en hardware basado en átomos neutros. No se han revelado por completo los detalles técnicos del esquema de corrección de errores ni las tasas de error lógico objetivo, y el cronograma sigue siendo una proyección, no un resultado demostrado.

rss · Ars Technica · jun 17, 20:44

**Contexto**: Las computadoras cuánticas son muy susceptibles al ruido y la decoherencia, que corrompen los qubits y provocan errores. La corrección de errores cuánticos (QEC) codifica qubits lógicos a través de múltiples qubits físicos para detectar y corregir errores, pero requiere tasas de error físico extremadamente bajas y muchos qubits para ser eficaz. El código de superficie es un esquema QEC líder, pero las implementaciones actuales aún luchan por superar el punto de equilibrio donde la tasa de error lógico es menor que la física. Muchos planes de la industria apuntaban a la computación cuántica tolerante a fallos más cerca de la década de 2030, por lo que un objetivo de 2028 representa una aceleración ambiciosa.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quantum_error_correction">Quantum error correction</a></li>
<li><a href="https://arxiv.org/abs/1907.11157">[1907.11157] Quantum Error Correction: An Introductory Guide Quantum Error Correction: An Introductory Guide What Is Quantum Error Correction & How Does It Work Top Stories Quantum ErrorCorrection:An IntroductoryGuide - arXiv.org Quantum error correction below the surface code threshold Quantum error correction with the toric code</a></li>
<li><a href="https://arstechnica.com/science/2026/06/amazon-quera-promise-useful-quantum-error-correction-by-2028/">Sooner than expected? Useful quantum error correction ...</a></li>

</ul>
</details>

**Etiquetas**: `#computación cuántica`, `#corrección de errores`, `#Amazon`, `#QuEra`, `#tecnología`

---

<a id="item-6"></a>
## [Agentes de programación de IA enseñan a robots a instalar GPUs y cortar bridas](https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/) ⭐️ 7.0/10

Nvidia usa agentes de programación de IA para enseñar a robots tareas como instalar GPUs y cortar bridas.

rss · Ars Technica · jun 17, 19:25

**Etiquetas**: `#robótica`, `#agentes de IA`, `#Nvidia`, `#aprendizaje automático`, `#automatización`

---

<a id="item-7"></a>
## [California acusa a AT&T de mentir a la FCC para cerrar su antigua red telefónica](https://arstechnica.com/tech-policy/2026/06/california-says-att-lied-to-fcc-in-attempt-to-shut-off-old-phone-network/) ⭐️ 6.0/10

California ha alegado que AT&T engañó a la Comisión Federal de Comunicaciones (FCC) en su petición para discontinuar el servicio telefónico tradicional de cobre, mientras la FCC evalúa si anular las regulaciones estatales. La disputa sobre la autoridad de la infraestructura de telecomunicaciones podría afectar a millones que dependen de líneas fijas de cobre, especialmente en zonas rurales y servicios de emergencia, en medio de una migración sectorial a redes digitales. AT&T busca anular las normas estatales que exigen mantener las antiguas redes de cobre, argumentando que es necesaria la migración a fibra e inalámbrico, mientras California sostiene que AT&T proporcionó información falsa a la FCC sobre el impacto del cierre.

rss · Ars Technica · jun 17, 20:07

**Contexto**: La red telefónica pública conmutada (PSTN) y el servicio telefónico tradicional (POTS) son los sistemas analógicos de cobre. Los proveedores están retirando estas redes legadas en favor de infraestructura digital basada en IP, un proceso conocido como el 'ocaso del cobre'. Los reguladores estatales suelen imponer condiciones para proteger a los consumidores que aún dependen de estos servicios.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Public_switched_telephone_network">Public switched telephone network</a></li>
<li><a href="https://en.wikipedia.org/wiki/Plain_old_telephone_service">Plain old telephone service</a></li>
<li><a href="https://www.aizan.com/article/the-copper-sunset-countdown-preparing-for-the-end-of-traditional-telephony">The Copper Sunset Countdown: Preparing for the End of</a></li>

</ul>
</details>

**Etiquetas**: `#política tecnológica`, `#telecomunicaciones`, `#AT&T`, `#FCC`, `#regulación`

---

<a id="item-8"></a>
## [IA peligrosas con capacidades de hackeo serán inevitables](https://arstechnica.com/ai/2026/06/dangerous-ai-models-are-coming-no-matter-what/) ⭐️ 6.0/10

Expertos advierten que los sistemas de IA con sofisticadas capacidades de hackeo se volverán algo habitual en un futuro cercano, a pesar de los esfuerzos regulatorios. Esta tendencia podría democratizar los ciberataques, facilitando que actores maliciosos aprovechen vulnerabilidades a gran escala, y desafía las defensas de ciberseguridad existentes. Los avances en modelos de lenguaje grandes y aprendizaje por refuerzo están permitiendo que la IA descubra vulnerabilidades y genere código de explotación de forma autónoma, aunque los sistemas actuales aún tienen limitaciones en fiabilidad y sigilo.

rss · Ars Technica · jun 17, 17:50

**Contexto**: Las capacidades de hackeo de la IA surgen de modelos entrenados con enormes repositorios de código y datos de ciberseguridad. Investigadores han demostrado agentes de IA que pueden realizar pruebas de penetración, escribir correos de phishing y descifrar contraseñas. Esta progresión refleja una tendencia más amplia hacia la ejecución autónoma de tareas, lo que suscita preocupaciones éticas y de seguridad.

**Etiquetas**: `#inteligencia artificial`, `#ciberseguridad`, `#riesgos`, `#modelos de IA`, `#hacking`

---

<a id="item-9"></a>
## [Altavoz Google Home con Gemini ya en preventa por $100](https://arstechnica.com/google/2026/06/the-gemini-powered-google-home-speaker-arrives-on-june-25-for-100/) ⭐️ 6.0/10

Google ha abierto los pedidos anticipados para su nuevo altavoz inteligente Google Home, con un precio de $100, tras diez meses de espera. El dispositivo prioriza la integración de Gemini sobre la calidad de audio. Este lanzamiento demuestra el compromiso de Google de integrar Gemini más profundamente en el hardware de consumo, haciendo que la asistencia de IA avanzada sea más accesible en los hogares. También refleja un cambio en el mercado donde las capacidades de IA, no la calidad de sonido, diferencian a los altavoces inteligentes. El altavoz tiene un precio competitivo de $100, pero los detalles sobre el hardware o la versión de Gemini (por ejemplo, Nano en dispositivo o procesamiento en la nube) siguen sin estar claros. Se informa que la calidad de audio no es un enfoque principal.

rss · Ars Technica · jun 17, 15:57

**Contexto**: Google Home es una línea de altavoces inteligentes que anteriormente funcionaban con Google Assistant. Gemini, anunciado en diciembre de 2023, es un modelo multimodal de IA generativa que desde entonces se ha integrado en todo el ecosistema de Google. Este nuevo altavoz es uno de los primeros dispositivos Home diseñados de forma nativa para Gemini, priorizando interacciones impulsadas por IA como conversaciones contextuales y automatización de tareas sobre el audio premium. El movimiento se alinea con la tendencia general de la industria hacia dispositivos domésticos inteligentes centrados en la IA.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>

</ul>
</details>

**Etiquetas**: `#altavoz inteligente`, `#Google Home`, `#Gemini`, `#asistente virtual`, `#producto`

---

<a id="item-10"></a>
## [Demuelen torres históricas del transbordador espacial en Vandenberg para SpaceX](https://arstechnica.com/space/2026/06/towers-once-planned-for-california-shuttle-launches-leveled-for-spacex-rockets/) ⭐️ 6.0/10

Las torres de lanzamiento del Complejo Espacial 6 de la Base de la Fuerza Espacial Vandenberg, construidas originalmente para el transbordador espacial pero nunca utilizadas en un vuelo tripulado, han sido demolidas para dar paso a futuros lanzamientos de cohetes de SpaceX. Esto marca la eliminación final de la infraestructura de la era de la Guerra Fría, simbolizando el cambio de programas espaciales gubernamentales a empresas espaciales comerciales, y permitirá a SpaceX aumentar su cadencia de lanzamientos desde la Costa Oeste. La demolición incluyó la Torre de Servicio Móvil y la Estructura de Servicio Fijo, que fueron modificadas para el Delta IV Heavy pero originalmente diseñadas para el transbordador. Los planes de SpaceX para SLC-6 probablemente incluyen lanzamientos de Falcon 9 y posiblemente Falcon Heavy a órbitas polares y heliosincrónicas.

rss · Ars Technica · jun 17, 15:47

**Contexto**: El Complejo Espacial 6 (SLC-6) en la Base de la Fuerza Espacial Vandenberg fue construido inicialmente en los años 60 para el programa del Laboratorio Orbital Tripulado. Posteriormente se convirtió para lanzamientos del transbordador espacial en los 80, pero esos planes se cancelaron tras el desastre del Challenger debido a preocupaciones de seguridad y el alto costo de mantener una infraestructura separada para el transbordador. Luego, la plataforma se utilizó para cohetes Delta IV Heavy desde 2006 hasta su retiro en 2022. Ahora, SpaceX se hará cargo del sitio, continuando el legado de Vandenberg como centro principal para lanzamientos en órbita polar.

<details><summary>Referencias</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vandenberg_Space_Launch_Complex_6">Vandenberg Space Launch Complex 6 - Wikipedia</a></li>
<li><a href="https://www.thelogbook.com/vandenberg-slc6/">Vandenberg shuttle launch pad ready – theLogBook.com</a></li>

</ul>
</details>

**Etiquetas**: `#Aeroespacial`, `#SpaceX`, `#Historia espacial`, `#Infraestructura`, `#Cohetes`

---