# Laboratorio No. 4 "Señales electromiográficas EMG"
## Shara Cetina y Juanita Gómez

## Descripción
Este proyecto contiene el código y la información para comprender la adquisición, el acondicionamiento y el procesamiento de señales EMG, evaluando los cambios en sus características temporales y frecuenciales. Para ello, se emplean caracteristicas espectrales como la frecuencia media y la frecuencia mediana, filtros pasa banda, la transformada rápida de Fourier (FFT) y el espectro de amplitud.

## Propósito
El propósito de este laboratorio es que el estudiante aplique técnicas de análisis espectral y comprenda la importancia del cálculo de atributos en el dominio de la frecuencia dentro del procesamiento de señales, específicamente en señales electromiográficas (EMG). Se busca que el estudiante entienda el análisis espectral como una herramienta que permite observar la distribución de la energía al descomponer una señal en sus componentes de frecuencia y amplitud. Asimismo, mediante el cálculo de parámetros como la frecuencia media y la frecuencia mediana, junto con el análisis espectral de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la detección de fatiga muscular en escenarios no controlados y reconozca su relevancia en aplicaciones propias del ámbito de la ingeniería biomédica. Además, se busca que el estudiante relacione estos parámetros con características fisiológicas y de calidad de la señal.

## Metodología
## Diagrama de flujo
### Parte A
<img width="849" height="636" alt="Captura de pantalla 2026-04-22 165117" src="https://github.com/user-attachments/assets/0e059d49-9445-4c21-9679-40903f6ca8c4" />
<img width="845" height="307" alt="Captura de pantalla 2026-04-22 165335" src="https://github.com/user-attachments/assets/5b83f92d-b095-42a2-81aa-37f674b0d4f3" />

### Parte B
### Parte C
## Resultados
### Señal EMG generador de señales, original y filtrada
<p align="center">
<img width="874" height="406" alt="Captura de pantalla 2026-04-22 235415" src="https://github.com/user-attachments/assets/5c9c1ec5-21bb-48cb-91a6-739b13e9d596" />
<img width="877" height="403" alt="Captura de pantalla 2026-04-22 235724" src="https://github.com/user-attachments/assets/32812072-62b6-42cd-b9d8-90e61788319c" />
</p>

### Contracciones simuladas, original y filtradas
<p align="center">
  <img width="498" height="578" alt="Captura de pantalla 2026-04-22 235925" src="https://github.com/user-attachments/assets/26c5c0a3-1879-49ca-ae06-0f4020fd9b4e" />
  <img width="500" height="575" alt="Captura de pantalla 2026-04-23 000009" src="https://github.com/user-attachments/assets/0e8c781c-3d45-45af-8924-9e9d2b3ada65" />
</p>

### Resultados de cada contracción simulada
<p align="center">
  <img width="437" height="128" alt="Captura de pantalla 2026-04-23 000144" src="https://github.com/user-attachments/assets/539c68b2-7152-47d3-bfcb-91f503e9bc94" />
</p>

### Evolución de las frecuencias
<p align="center">
  <img width="492" height="356" alt="Captura de pantalla 2026-04-23 000255" src="https://github.com/user-attachments/assets/fd32480e-38a0-43ba-b805-325f0e4a5e3a" />
</p>

La evolución de la frecuencia media (MNF) y la frecuencia mediana (MDF) a lo largo de las contracciones simuladas no presenta variaciones significativas, lo que indica que existe poca variabilidad espectral en la señal. La estabilidad de la frecuencia mediana (MDF) sugiere que el contenido en frecuencia permanece constante en todas las contracciones, lo cual es esperable al tratarse de una señal sintética con un espectro prácticamente fijo.
Por otro lado, el ligero incremento observado en la frecuencia media (MNF) podría atribuirse a pequeñas variaciones en la amplitud, efectos de discretización o la presencia de ruido en la señal.
Estos resultados son coherentes con lo esperado, ya que al ser una señal “ideal”, carece de dinámica fisiológica. En consecuencia, no reproduce los cambios típicos de un EMG real, como las variaciones espectrales asociadas a incrementos de fuerza o a la aparición de fatiga.

<p align="center">
</p>
## Análisis de resultados
- Identificar el mecanismo fisiológico mediante el cual parámetros como la frecuencia media y frecuencia mediana experimentan cambios a medida que el músculo tiende a fatigarse.
- Determinar el alcance y las posibles limitaciones de emplear parámetros del dominio frecuencial en contextos como fisiología del deporte. 

## Conclusión
Breve reflexión sobre la factibilidad de emplear técnicas espectrales en la detección de la fatiga muscular en escenarios no controlados como, por ejemplo, durante entrenamiento de atletas

## Discusión
- ¿Cambian los valores de frecuencia media y mediana a medida que el músculo se acerca a la fatiga? ¿A qué podría atribuirse este cambio?
- ¿Cómo justifica el uso de herramientas como la transformada de Fourier en escenarios como, por ejemplo, terapias de rehabilitación? 

