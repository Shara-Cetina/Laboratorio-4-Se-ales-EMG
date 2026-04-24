# Laboratorio No. 4 "Señales electromiográficas EMG"
## Shara Cetina y Juanita Gómez

## Descripción
<p align="justify">
Este proyecto contiene el código y la información para comprender la adquisición, el acondicionamiento y el procesamiento de señales EMG, evaluando los cambios en sus características temporales y frecuenciales. Para ello, se emplean caracteristicas espectrales como la frecuencia media y la frecuencia mediana, filtros pasa banda, la transformada rápida de Fourier (FFT) y el espectro de amplitud.

## Propósito
<p align="justify">
El propósito de este laboratorio es que el estudiante aplique técnicas de análisis espectral y comprenda la importancia del cálculo de atributos en el dominio de la frecuencia dentro del procesamiento de señales, específicamente en señales electromiográficas (EMG). Se busca que el estudiante entienda el análisis espectral como una herramienta que permite observar la distribución de la energía al descomponer una señal en sus componentes de frecuencia y amplitud. Asimismo, mediante el cálculo de parámetros como la frecuencia media y la frecuencia mediana, junto con el análisis espectral de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la detección de fatiga muscular en escenarios no controlados y reconozca su relevancia en aplicaciones propias del ámbito de la ingeniería biomédica. Además, se busca que el estudiante relacione estos parámetros con características fisiológicas y de calidad de la señal.

## Metodología 
<p align="justify">
Para el desarrollo de la presente práctica se adquirieron dos señales electromiográficas (EMG), una generada mediante un generador de señales y otra registrada en una mujer de 19 años, a partir del músculo braquial durante un protocolo de esfuerzo máximo de 60 segundos. Ambas señales fueron procesadas en Python con el objetivo de identificar la cantidad de contracciones musculares en el intervalo analizado y calcular parámetros espectrales como la frecuencia media y la frecuencia mediana. En el caso de la señal obtenida de la participante, se aplicó un filtro digital FIR con ventana de Hamming, configurado como pasa banda entre 20 Hz y 450 Hz, con el fin de eliminar artefactos de movimiento y ruido de alta frecuencia sin afectar la fase de los potenciales de acción.

<p align="justify">
Para el análisis de la fatiga muscular, se realizó una segmentación basada en las contracciones previamente identificadas. A cada segmento se le aplicó la Transformada Rápida de Fourier (FFT) para obtener el espectro de potencia y calcular la Frecuencia Media (MNF) y la Frecuencia Mediana (MDF) a partir de la densidad espectral de potencia. Finalmente, se evaluó la evolución temporal de estos parámetros con el propósito de identificar el desplazamiento del contenido espectral hacia frecuencias más bajas, característico de la fatiga muscular.



 
### Diagrama de flujo
#### Parte A
<img width="1024" height="768" alt="4" src="https://github.com/user-attachments/assets/1d436047-969e-47b0-9a9d-e0b557a56fd4" />
<img width="1022" height="508" alt="5 1" src="https://github.com/user-attachments/assets/065fced0-af17-4e8d-8e41-ba36a89eefb2" />


#### Parte B
<img width="1024" height="768" alt="4" src="https://github.com/user-attachments/assets/b12d3ced-7dee-440f-9a8c-83a2c8b51a3b" />
<img width="1021" height="367" alt="5 1" src="https://github.com/user-attachments/assets/b3c9c1b5-3196-495e-8f58-051a60e2aad7" />

#### Parte C
<img width="1024" height="768" alt="Parte A" src="https://github.com/user-attachments/assets/14518f97-f881-48f5-98df-3e7f52a1875c" />

## Resultados
### Señales EMG Generador de señales
#### Original y filtrada
<p align="center">
<img src="https://github.com/user-attachments/assets/4baf197a-e798-4415-8625-55de7a2aa7b0" width="400"/>
<img src="https://github.com/user-attachments/assets/a2420ba8-eb11-4f46-a5e1-81e0dc7c77df" width="400"/>

</p>
 
#### Contracciones simuladas (original y filtrada)
<p align="center">
  <img src="https://github.com/user-attachments/assets/3f2797c1-70ba-4122-a63d-260794849514" width="400"/>
  <img src="https://github.com/user-attachments/assets/313ff873-41eb-47c6-886b-1e15b7208bf4" width="400"/>
</p>


<div align="center">
 
#### Resultados de cada contracción simulada


  | Contracción   | MNF (Hz)  | MDF (Hz)  |
|--------------|----------:|----------:|
| Contraccion_1 | 162.355172 | 199.833333 |
| Contraccion_2 | 163.347246 | 199.833333 |
| Contraccion_3 | 163.908955 | 199.833333 |
| Contraccion_4 | 163.749431 | 199.833333 |
| Contraccion_5 | 163.676518 | 199.833333 |

</div>

#### Evolución de las frecuencias
<p align="center">
  <img width="492" height="356" alt="Captura de pantalla 2026-04-23 000255" src="https://github.com/user-attachments/assets/fd32480e-38a0-43ba-b805-325f0e4a5e3a" />
</p>

<p align="justify">
La evolución de la frecuencia media (MNF) y la frecuencia mediana (MDF) a lo largo de las contracciones simuladas no presenta variaciones significativas, lo que indica que existe poca variabilidad espectral en la señal. La estabilidad de la frecuencia mediana (MDF) sugiere que el contenido en frecuencia permanece constante en todas las contracciones, lo cual es esperable al tratarse de una señal sintética con un espectro prácticamente fijo.
Por otro lado, el ligero incremento observado en la frecuencia media (MNF) podría atribuirse a pequeñas variaciones en la amplitud, efectos de discretización o la presencia de ruido en la señal.
Estos resultados son coherentes con lo esperado, ya que al ser una señal “ideal”, carece de dinámica fisiológica. En consecuencia, no reproduce los cambios típicos de un EMG real, como las variaciones espectrales asociadas a incrementos de fuerza o a la aparición de fatiga.
</p>

### Señales EMG Paciente
#### Original y filtrada
<p align="center">
  <img src="https://github.com/user-attachments/assets/ea7e7c86-6b90-4e79-9971-de8e5ece2914" width="400"/>
  <img src="https://github.com/user-attachments/assets/edf49441-af38-41bb-9471-35328992f095" width="400"/>

 
  <img src="https://github.com/user-attachments/assets/4c7df783-ba27-461a-9ce7-6b03081285c5" width="400"/>
  <img src="https://github.com/user-attachments/assets/1354faa0-b042-4346-87d8-ceecb09c2d6d" width="400"/>
</p>

### Segmentos de contracción
<p align="center">
  <img src="https://github.com/user-attachments/assets/cfc90413-fc2d-47c1-b9cb-69bf6f3e5af8" width="300"/>
  <img src="https://github.com/user-attachments/assets/cbbbeb9b-0233-4e42-be4c-356d24a3d4ca" width="300"/>
  <img src="https://github.com/user-attachments/assets/93156dc3-9d09-4550-b416-97ef144a7b06" width="300"/>

  <img src="https://github.com/user-attachments/assets/a9763879-8719-4c82-ae2a-7c121fd6628c" width="300"/>
  <img src="https://github.com/user-attachments/assets/a1e6f420-f8cc-4ace-acd3-f3ca9c404c0e" width="300"/>
</p>

<div align="center">

### Resultados de cada contracción

| Contracción   | MNF (Hz) | MDF (Hz) |
|--------------|---------:|---------:|
| Contraccion_1 | 191.31 | 172.67 |
| Contraccion_2 | 188.54 | 174.00 |
| Contraccion_3 | 188.92 | 169.33 |
| Contraccion_4 | 188.82 | 168.00 |
| Contraccion_5 | 186.60 | 169.33 |
</div>

### Evolución de las frecuencias
<p align="center">
  <img width="529" height="355" alt="Captura de pantalla 2026-04-23 002525" src="https://github.com/user-attachments/assets/7b90269b-41e8-47dc-9baa-407ea0910dd9" />
</p>

# Discutir la relación entre los cambios de frecuencia y la fisiología de la fatiga muscular. (FALTA)

## Transformada rápida de Fourier (FFT) para cada contracción
<p align="center">
  <img src="https://github.com/user-attachments/assets/1ebca35b-49e7-4e4c-badd-1ab98c942a97" width="325"/>
  <img src="https://github.com/user-attachments/assets/2bee861b-42aa-4113-8367-edb18a075156" width="325"/>
  <img src="https://github.com/user-attachments/assets/a3308ab0-30bf-44a4-87ba-365fb1fd7fae" width="325"/>
 
  <img src="https://github.com/user-attachments/assets/9f52fc70-6fc0-463b-b07e-6f70f70b36ad" width="325"/>
  <img src="https://github.com/user-attachments/assets/5881041a-5af6-4701-84f8-cf4a93fedbab" width="325"/>
</p>

## Espectro de amplitud
<p align="center">
  <img src="https://github.com/user-attachments/assets/83dfbb8f-abf1-49eb-81b5-c9fdcf61e188" width="325"/>
  <img src="https://github.com/user-attachments/assets/ecd115f1-5132-4cc6-ac86-5d742e7b1dc4" width="325"/>
  <img src="https://github.com/user-attachments/assets/fbde9ee2-413e-4a0a-98ba-fcab443863bd" width="325"/>
 
  <img src="https://github.com/user-attachments/assets/9a1e303a-a2cb-421d-aa9f-eef2f19350ac" width="325"/>
  <img src="https://github.com/user-attachments/assets/87802805-61cd-4f43-a95c-77985bab9969" width="325"/>
</p>

<p align="justify">
Al comparar los espectros de los primeros segmentos con los de los últimos, se observan cambios compatibles con fatiga muscular en un EMG isométrico. En los primeros segmentos, el espectro presenta un mayor contenido relativo en frecuencias altas, mientras que en los últimos se aprecia un ligero desplazamiento hacia frecuencias más bajas. Asimismo, se observa una disminución progresiva de la frecuencia media y la frecuencia mediana (indicadas por las líneas verde y roja), lo cual es consistente con un EMG isométrico sostenido y se asocia a la reducción de la velocidad de conducción de las fibras musculares.
</p>

## Desplazamiento del pico espectral

<p align="center">
<img width="713" height="483" alt="WhatsApp Image 2026-04-23 at 15 51 05" src="https://github.com/user-attachments/assets/be543dc0-c903-436a-b92e-96c1b4960861" />
</p> 

<p align="justify">
El desplazamiento del pico espectral indica la frecuencia dominante de la señal electromiográfica en un instante dado. En contracciones isométricas sostenidas, suele esperarse un desplazamiento progresivo hacia frecuencias más bajas como consecuencia de la fatiga muscular. Sin embargo, este parámetro es más variable y sensible al ruido en comparación con la frecuencia media y la frecuencia mediana.

En este caso, se observan irregularidades y ausencia de una tendencia clara, lo que sugiere que el pico espectral no es un indicador fiable de la fatiga en estos datos. Además, el espectro del EMG isométrico es ancho, con múltiples frecuencias activas, lo que puede provocar saltos en la localización del pico. Este comportamiento también puede verse afectado por ruido y por variaciones en el nivel de fuerza durante la contracción.
</p> 
 
# f. Redactar conclusiones sobre el uso del análisis espectral como herramienta diagnóstica en electromiografía. (FALTA) / JUANITA

<p align="center">
</p>

## Análisis de resultados / JUANITA
- Identificar el mecanismo fisiológico mediante el cual parámetros como la frecuencia media y frecuencia mediana experimentan cambios a medida que el músculo tiende a fatigarse.
- Determinar el alcance y las posibles limitaciones de emplear parámetros del dominio frecuencial en contextos como fisiología del deporte. 

## Conclusión / JUANITA
Breve reflexión sobre la factibilidad de emplear técnicas espectrales en la detección de la fatiga muscular en escenarios no controlados como, por ejemplo, durante entrenamiento de atletas

## Discusión / JUANITA
- ¿Cambian los valores de frecuencia media y mediana a medida que el músculo se acerca a la fatiga? ¿A qué podría atribuirse este cambio?
- ¿Cómo justifica el uso de herramientas como la transformada de Fourier en escenarios como, por ejemplo, terapias de rehabilitación? 

