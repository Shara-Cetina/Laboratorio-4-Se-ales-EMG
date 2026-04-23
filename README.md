# Laboratorio No. 4 "Señales electromiográficas EMG"
## Shara Cetina y Juanita Gómez

## Descripción
Este proyecto contiene el código y la información para comprender la adquisición, el acondicionamiento y el procesamiento de señales EMG, evaluando los cambios en sus características temporales y frecuenciales. Para ello, se emplean caracteristicas espectrales como la frecuencia media y la frecuencia mediana, filtros pasa banda, la transformada rápida de Fourier (FFT) y el espectro de amplitud.

## Propósito
El propósito de este laboratorio es que el estudiante aplique técnicas de análisis espectral y comprenda la importancia del cálculo de atributos en el dominio de la frecuencia dentro del procesamiento de señales, específicamente en señales electromiográficas (EMG). Se busca que el estudiante entienda el análisis espectral como una herramienta que permite observar la distribución de la energía al descomponer una señal en sus componentes de frecuencia y amplitud. Asimismo, mediante el cálculo de parámetros como la frecuencia media y la frecuencia mediana, junto con el análisis espectral de señales biológicas, se pretende que el estudiante evalúe el impacto de estos procedimientos en la detección de fatiga muscular en escenarios no controlados y reconozca su relevancia en aplicaciones propias del ámbito de la ingeniería biomédica. Además, se busca que el estudiante relacione estos parámetros con características fisiológicas y de calidad de la señal.

## Metodología (FALTA)

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
### Señales EMG 
#### Generador de señales (original y filtrada)
<p align="center">
<img src="https://github.com/user-attachments/assets/5c9c1ec5-21bb-48cb-91a6-739b13e9d596" width="400"/>
<img src="https://github.com/user-attachments/assets/32812072-62b6-42cd-b9d8-90e61788319c" width="400"/>
</p>
 
#### Contracciones simuladas (original y filtrada)
<p align="center">
  <img src="https://github.com/user-attachments/assets/26c5c0a3-1879-49ca-ae06-0f4020fd9b4e" width="400"/>
  <img src="https://github.com/user-attachments/assets/0e8c781c-3d45-45af-8924-9e9d2b3ada65" width="400"/>
</p>

### Resultados de cada contracción simulada

  | Contracción   | MNF (Hz)  | MDF (Hz)  |
|--------------|----------:|----------:|
| Contraccion_1 | 162.355172 | 199.833333 |
| Contraccion_2 | 163.347246 | 199.833333 |
| Contraccion_3 | 163.908955 | 199.833333 |
| Contraccion_4 | 163.749431 | 199.833333 |
| Contraccion_5 | 163.676518 | 199.833333 |


### Evolución de las frecuencias
<p align="center">
  <img width="492" height="356" alt="Captura de pantalla 2026-04-23 000255" src="https://github.com/user-attachments/assets/fd32480e-38a0-43ba-b805-325f0e4a5e3a" />
</p>

La evolución de la frecuencia media (MNF) y la frecuencia mediana (MDF) a lo largo de las contracciones simuladas no presenta variaciones significativas, lo que indica que existe poca variabilidad espectral en la señal. La estabilidad de la frecuencia mediana (MDF) sugiere que el contenido en frecuencia permanece constante en todas las contracciones, lo cual es esperable al tratarse de una señal sintética con un espectro prácticamente fijo.
Por otro lado, el ligero incremento observado en la frecuencia media (MNF) podría atribuirse a pequeñas variaciones en la amplitud, efectos de discretización o la presencia de ruido en la señal.
Estos resultados son coherentes con lo esperado, ya que al ser una señal “ideal”, carece de dinámica fisiológica. En consecuencia, no reproduce los cambios típicos de un EMG real, como las variaciones espectrales asociadas a incrementos de fuerza o a la aparición de fatiga.

### Señal EMG de paciente, original y filtrada
<p align="center">
  <img width="914" height="356" alt="Captura de pantalla 2026-04-23 001739" src="https://github.com/user-attachments/assets/72fa9528-d7f7-4f47-ae7b-fac276be4796" />
  <img width="922" height="358" alt="Captura de pantalla 2026-04-23 001806" src="https://github.com/user-attachments/assets/db25adfb-d7cf-4779-97b2-fe1cc1b9258d" />
  <img width="773" height="353" alt="Captura de pantalla 2026-04-23 001922" src="https://github.com/user-attachments/assets/6c3eb02a-14b8-4b56-9178-6f222dafc2dc" />
  <img width="784" height="355" alt="Captura de pantalla 2026-04-23 001953" src="https://github.com/user-attachments/assets/d578e25d-50a6-4892-bc16-a83813252282" />
</p>

### Segmentos de contracción
<p align="center">
  <img width="922" height="339" alt="Captura de pantalla 2026-04-23 002148" src="https://github.com/user-attachments/assets/f22ff0ec-2d2c-4ebd-b5e7-84a3d6bf343c" />
  <img width="922" height="339" alt="Captura de pantalla 2026-04-23 002234" src="https://github.com/user-attachments/assets/5202c2e2-8897-436e-b128-916e7acccda2" />
  <img width="923" height="337" alt="Captura de pantalla 2026-04-23 002215" src="https://github.com/user-attachments/assets/2312a0b6-75db-48cd-9a12-6d96268eefe5" />
  <img width="922" height="338" alt="Captura de pantalla 2026-04-23 002258" src="https://github.com/user-attachments/assets/238d1cca-a85e-4fcd-a5e1-c080205716db" />
  <img width="924" height="338" alt="Captura de pantalla 2026-04-23 002320" src="https://github.com/user-attachments/assets/1edd9bd5-0772-4054-b9ed-1f0d628839be" />
</p>

### Resultados de cada contracción
<p align="center">
<img width="470" height="118" alt="Captura de pantalla 2026-04-23 002411" src="https://github.com/user-attachments/assets/95654dc5-7fa6-47aa-9c79-614741fedcfb" />
</p>

### Evolución de las frecuencias
<p align="center">
  <img width="529" height="355" alt="Captura de pantalla 2026-04-23 002525" src="https://github.com/user-attachments/assets/7b90269b-41e8-47dc-9baa-407ea0910dd9" />
</p>

# Discutir la relación entre los cambios de frecuencia y la fisiología de la fatiga muscular. (FALTA)

### Transformada rápida de Fourier (FFT) para cada contracción
<p align="center">
  <img width="923" height="332" alt="Captura de pantalla 2026-04-23 004107" src="https://github.com/user-attachments/assets/1ebca35b-49e7-4e4c-badd-1ab98c942a97" />
  <img width="920" height="330" alt="Captura de pantalla 2026-04-23 004133" src="https://github.com/user-attachments/assets/2bee861b-42aa-4113-8367-edb18a075156" />
  <img width="924" height="332" alt="Captura de pantalla 2026-04-23 004156" src="https://github.com/user-attachments/assets/a3308ab0-30bf-44a4-87ba-365fb1fd7fae" />
  <img width="922" height="329" alt="Captura de pantalla 2026-04-23 004217" src="https://github.com/user-attachments/assets/9f52fc70-6fc0-463b-b07e-6f70f70b36ad" />
  <img width="923" height="333" alt="Captura de pantalla 2026-04-23 004234" src="https://github.com/user-attachments/assets/5881041a-5af6-4701-84f8-cf4a93fedbab" />
</p>

### Espectro de amplitud
<p align="center">
  <img width="921" height="331" alt="Captura de pantalla 2026-04-23 004516" src="https://github.com/user-attachments/assets/83dfbb8f-abf1-49eb-81b5-c9fdcf61e188" />
  <img width="923" height="325" alt="Captura de pantalla 2026-04-23 004545" src="https://github.com/user-attachments/assets/ecd115f1-5132-4cc6-ac86-5d742e7b1dc4" />
  <img width="923" height="333" alt="Captura de pantalla 2026-04-23 004607" src="https://github.com/user-attachments/assets/fbde9ee2-413e-4a0a-98ba-fcab443863bd" />
  <img width="922" height="330" alt="Captura de pantalla 2026-04-23 004629" src="https://github.com/user-attachments/assets/9a1e303a-a2cb-421d-aa9f-eef2f19350ac" />
  <img width="924" height="331" alt="Captura de pantalla 2026-04-23 004647" src="https://github.com/user-attachments/assets/87802805-61cd-4f43-a95c-77985bab9969" />
</p>

# c. Comparar los espectros de las primeras contracciones con los de las últimas. (FALTA)
# e. Calcular y discutir el desplazamiento del pico espectral y su relación con el esfuerzo sostenido.(FALTA)
# f. Redactar conclusiones sobre el uso del análisis espectral como herramienta diagnóstica en electromiografía. (FALTA)

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

