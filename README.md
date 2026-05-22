# LABORATORIO 5 – HRV Y BALANCE AUTONÓMICO



Sara Sofía Piñeros Tovar – 5600962

---

# INTRODUCCIÓN

La variabilidad de la frecuencia cardíaca (HRV, Heart Rate Variability) corresponde a las variaciones temporales existentes entre latidos consecutivos del corazón, conocidos como intervalos RR. Estas variaciones permiten evaluar el comportamiento del sistema nervioso autónomo, especialmente el equilibrio entre la actividad simpática y parasimpática. El análisis HRV es ampliamente utilizado en ingeniería biomédica y medicina debido a que proporciona información importante sobre el estado fisiológico, el estrés, la regulación cardíaca y diferentes condiciones clínicas.

Para la realización de esta práctica se adquirió una señal electrocardiográfica (ECG) utilizando un sistema STM32 conectado a un sensor AD8232. La señal fue registrada durante dos condiciones fisiológicas diferentes: reposo y lectura en voz alta. Posteriormente, la señal ECG fue procesada en Python utilizando técnicas de filtrado digital, detección de picos R y análisis estadístico y geométrico de la variabilidad cardíaca.

Durante el procesamiento se implementó un filtro IIR Butterworth pasa banda para reducir el ruido presente en la señal ECG y facilitar la identificación de los complejos QRS. A partir de la detección de los picos R se calcularon los intervalos RR y parámetros HRV como SDNN, SD1, SD2, CSI y CVI, además de construir diagramas de Poincaré para analizar el balance autonómico entre ambas condiciones experimentales.

---

# OBJETIVOS

## Objetivo General

Analizar la variabilidad de la frecuencia cardíaca mediante el procesamiento digital de una señal ECG para evaluar el balance autonómico durante estados de reposo y lectura en voz alta.

---

## Objetivos Específicos

* Adquirir una señal ECG utilizando STM32 y el sensor AD8232.
* Procesar la señal ECG en Python mediante técnicas de filtrado digital.
* Detectar automáticamente los picos R de la señal cardíaca.
* Calcular los intervalos RR y parámetros HRV.
* Construir diagramas de Poincaré para el análisis geométrico de la HRV.
* Comparar la actividad simpática y parasimpática entre reposo y lectura.

---

# DESCRIPCIÓN DE LA SEÑAL

La señal utilizada en el laboratorio correspondió a una señal electrocardiográfica (ECG) adquirida mediante un módulo AD8232 conectado a una tarjeta STM32. La adquisición se realizó durante un tiempo total de cuatro minutos con una frecuencia de muestreo determinada por el sistema de captura. La señal fue almacenada en formato `.wav` para su posterior procesamiento digital en Python.

La captura experimental fue dividida en dos segmentos fisiológicos diferentes. Durante los primeros dos minutos el participante permaneció en estado de reposo y silencio, mientras que en los dos minutos restantes realizó lectura en voz alta. Esto permitió comparar el comportamiento cardíaco y el balance autonómico bajo dos condiciones distintas de actividad fisiológica.

Para el procesamiento digital de la señal se utilizaron las librerías NumPy, Matplotlib y SciPy, las cuales permitieron realizar el filtrado digital, detección de picos R, análisis estadístico y construcción de diagramas de Poincaré.

---

# PROCEDIMIENTO

Para el desarrollo de la práctica inicialmente se realizó una investigación teórica sobre variabilidad de la frecuencia cardíaca, sistema nervioso simpático, sistema nervioso parasimpático, intervalos RR y diagramas de Poincaré. Posteriormente, se preparó el sistema de adquisición utilizando el módulo AD8232, la tarjeta STM32 y electrodos de superficie colocados en configuración RA-LA-RL para registrar la actividad eléctrica cardíaca.

La señal ECG fue adquirida durante cuatro minutos y transmitida desde la STM32 hacia Python mediante comunicación serial UART. Posteriormente, la señal fue almacenada en formato `.wav` para facilitar su procesamiento digital. Una vez cargada la señal en Python mediante `wavfile.read()`, se realizó la normalización de amplitud y la construcción del vector de tiempo para visualizar gráficamente el ECG original.

El código fue estructurado inicialmente para importar la señal ECG utilizando SciPy. Posteriormente, se verificó si el archivo contenía uno o dos canales y se seleccionó únicamente el primer canal para el análisis. Después se realizó la normalización de la señal y la generación del vector de tiempo con base en la frecuencia de muestreo.

Seguido a esto, se implementó un filtro IIR Butterworth pasa banda de cuarto orden con frecuencias de corte entre 0.5 Hz y 40 Hz. Este filtro permitió eliminar ruido de alta frecuencia y variaciones lentas de línea base presentes en la señal ECG. Las frecuencias de corte fueron normalizadas respecto a la frecuencia de Nyquist y posteriormente se calcularon los coeficientes del filtro mediante `signal.butter()`. Finalmente, el filtrado se realizó utilizando `signal.lfilter()`.

Posteriormente, la señal filtrada fue dividida en dos segmentos correspondientes a reposo y lectura. Para cada segmento se utilizó la función `find_peaks()` de SciPy con el fin de detectar automáticamente los picos R presentes en la señal ECG. La detección se realizó estableciendo una distancia mínima entre latidos equivalente a 0.6 segundos y un nivel de prominencia de 0.3.

A partir de los picos R detectados se calcularon los intervalos RR utilizando la diferencia temporal entre latidos consecutivos. Posteriormente, se calcularon parámetros HRV como la media RR y SDNN. Además, se construyeron diagramas de Poincaré mediante pares consecutivos RR(n) y RR(n+1), permitiendo calcular parámetros geométricos SD1 y SD2.

Finalmente, se calcularon los índices CSI y CVI para evaluar el balance autonómico del participante. El índice CSI permitió analizar el predominio simpático, mientras que el índice CVI se relacionó con la actividad vagal o parasimpática. Los resultados obtenidos fueron comparados entre los estados de reposo y lectura.

---

# DIAGRAMA DE FLUJO

El procedimiento experimental desarrollado durante el laboratorio siguió una secuencia organizada que inició con la investigación teórica sobre HRV y balance autonómico. Posteriormente, se realizó la preparación del sistema biomédico utilizando STM32, el sensor AD8232 y los electrodos de superficie para adquirir la señal ECG.

Después de la adquisición, la señal fue enviada desde la STM32 hacia Python mediante comunicación serial y almacenada en formato `.wav`. Posteriormente, se realizó el filtrado digital utilizando un filtro Butterworth pasa banda y se dividió la señal en segmentos de reposo y lectura.

Finalmente, se detectaron los picos R, se calcularon los intervalos RR y parámetros HRV, se construyeron diagramas de Poincaré y se evaluó el comportamiento simpático y parasimpático mediante los índices CSI y CVI.

---

# RESULTADOS

## Parámetros HRV

| Parámetro | Reposo  | Lectura |
| --------- | ------- | ------- |
| Media RR  | 0.84 s  | 0.76 s  |
| SDNN      | 0.072 s | 0.049 s |
| SD1       | 0.041   | 0.028   |
| SD2       | 0.083   | 0.071   |
| CSI       | 2.02    | 2.53    |
| CVI       | -2.47   | -2.70   |

---

## ECG Original

La señal ECG original presentó una adecuada morfología cardíaca permitiendo identificar claramente los complejos QRS. Sin embargo, también se observaron pequeñas fluctuaciones y componentes de ruido asociados a la adquisición biomédica y movimiento del paciente.

---

## ECG Filtrado

El filtro Butterworth permitió reducir considerablemente las interferencias de alta frecuencia y las variaciones lentas de línea base. Esto facilitó la identificación de los picos R y mejoró la calidad general de la señal ECG para el análisis HRV.

---

## Detección de Picos R

La detección automática de picos R realizada mediante `find_peaks()` mostró una adecuada precisión tanto en el segmento de reposo como en el segmento de lectura. Los picos detectados coincidieron correctamente con los complejos QRS observados en la señal ECG.

---

## Diagramas de Poincaré

El diagrama de Poincaré obtenido durante el estado de reposo presentó una nube de puntos más dispersa, indicando mayor variabilidad cardíaca y predominio parasimpático. En contraste, durante la lectura la nube presentó menor dispersión y una alineación más longitudinal, indicando disminución de la variabilidad cardíaca y aumento relativo de actividad simpática.

---

# ANÁLISIS DE LOS RESULTADOS

Los resultados obtenidos permitieron identificar cambios fisiológicos importantes entre las condiciones de reposo y lectura en voz alta. Durante la lectura se observó una disminución de los intervalos RR promedio, indicando un aumento de la frecuencia cardíaca asociado al esfuerzo cognitivo y respiratorio producido por la verbalización.

Asimismo, el parámetro SDNN disminuyó durante la lectura, evidenciando una reducción de la variabilidad cardíaca respecto al estado de reposo. Esto indica una menor capacidad adaptativa del sistema cardiovascular frente a estímulos fisiológicos.

Por otra parte, el índice CSI aumentó durante la lectura, sugiriendo un incremento de la actividad simpática. Adicionalmente, el índice CVI disminuyó ligeramente, indicando una reducción relativa de la actividad parasimpática o vagal.

Los diagramas de Poincaré confirmaron estos hallazgos, ya que durante la lectura se observó una nube de puntos menos dispersa y más alineada, reflejando menor variabilidad de los intervalos RR.

---

# PREGUNTAS

## ¿La lectura en voz alta modifica la variabilidad cardíaca?

Sí, debido a que durante la lectura se incrementa la actividad simpática asociada al esfuerzo cognitivo y respiratorio. Esto produce un aumento de la frecuencia cardíaca y una disminución de la variabilidad de los intervalos RR, evidenciada mediante la reducción de SDNN y SD1.

---

## ¿Por qué es necesario filtrar la señal ECG?

El filtrado permite eliminar ruido e interferencias presentes en la señal biomédica, tales como variaciones lentas de línea base y ruido de alta frecuencia. Esto mejora considerablemente la detección de los complejos QRS y aumenta la precisión del análisis HRV.

---

## ¿Qué representan los índices CSI y CVI?

El índice CSI representa el predominio de actividad simpática, mientras que el índice CVI se relaciona con la actividad parasimpática o vagal. Ambos parámetros permiten evaluar el balance autonómico del organismo bajo diferentes condiciones fisiológicas.

---

# CONCLUSIONES

Como se evidenció durante el desarrollo de la práctica, fue posible adquirir y procesar correctamente una señal ECG utilizando el sistema STM32 y Python. El filtrado digital implementado mediante el filtro Butterworth permitió mejorar considerablemente la calidad de la señal y facilitar la detección de los picos R.

Adicionalmente, el análisis HRV permitió identificar cambios fisiológicos importantes entre las condiciones de reposo y lectura. Durante la lectura se observó una disminución de la variabilidad cardíaca y un incremento relativo de actividad simpática, evidenciado mediante los parámetros SDNN, CSI y los diagramas de Poincaré.

Finalmente, los índices geométricos y estadísticos utilizados demostraron ser herramientas útiles para evaluar el comportamiento del sistema nervioso autónomo y analizar la dinámica cardíaca bajo diferentes condiciones fisiológicas.
