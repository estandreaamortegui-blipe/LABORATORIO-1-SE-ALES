LABORATORIO 5 – HRV Y BALANCE AUTONÓMICO



Sara Sofía Piñeros Tovar – 5600962



INTRODUCCIÓN

La manera en como nuestro cuerpo es capaz de responder a diferentes estímulos, se evalua el cambio de la frecuencia cardíaca (HRV), en donde se toma la variacion del tiempo latido por latido con el fin de analizar sistema nervioso autónomo, luego registramos una señal electrocardiográfica (ECG) en dos momentos clave: mientras la persona esta en reposo y cuando leía en voz alta,  se tomo por medio conectando un sensor AD8232 a un sistema STM32, lo que nos permitió recopilar los datos crudos de la actividad eléctrica del corazón en ambas situaciones experimentales.

Cuando ya se capturo las señales, se proceso en Pycharm para limpiar el ruido de la lectura mediante un filtro digital Butterworth, luego se identifico con precisión los picos R del corazón y calcular los intervalos, logramos tener métricas estadísticas clave como el SDNN y también construimos diagramas de Poincaré para calcular índices más avanzados como SD1, SD2, CSI y CVI, con este análisis se logro visualizar de forma muy clara cómo el estrés de hablar en público altera el control que el sistema nervioso ejerce sobre el corazón en comparación con un estado de calma.



OBJETIVOS

Objetivo General

Evaluar la neutralizacion del sistema nervioso autónomo en reposo y lectura en voz alta, por medio del procesamiento de señales electrocardiográficas y el cálculo de parámetros de la frecuencia cardíaca.



Objetivos Específicos

* Captar una señal ECG por medio STM32 y AD8232.
* Procesar señal ECG en Pycharm mediante técnicas de filtrado digital.
* Hallar los picos R de la señal cardíaca.
* Calcular intervalos RR y parámetros HRV.
* Crearr diagramas de Poincaré para el análisis geométrico de la HRV.
* Analizar actividad simpática y parasimpática.



DESCRIPCIÓN DE LA SEÑAL

Para tomar datos del laboratorio, se capturo una señal de ECG durante cuatro minutos usando un módulo AD8232 y una tarjeta STM32. El experimento se dividió a la mitad: los primeros dos minutos el participante estuvo en completo reposo y silencio, y los dos restantes realizó una lectura en voz alta. Todo el registro se guardó en un archivo .wav para poder comparar el comportamiento del corazón bajo ambas condiciones.

El analisis y  procesamiento digital se realizó en Pycharm ocupando librerías NumPy, Matplotlib y SciPy, nos permitieron limpiar el ruido de la señal, detectar con precisión los picos R y calcular los parámetros estadísticos, por ultimo estos datos construimos los diagramas de Poincaré para analizar visualmente los cambios en el balance del sistema nervioso autónomo.



PROCEDIMIENTO

1 se armamo el sistema conectando el sensor AD8232 a la STM32, colocando los electrodos en el participante (configuración RA-LA-RL) para medir el ECG.

2 tomar cuatro minutos de señal, la pasamos a la computadora por UART y la guardamos como archivo .wav. En Pychar, la cargamos, la normalizamos y creamos su vector de tiempo.

3 programamos el script en Pycharm usando SciPy, seleccionamos el canal principal de la señal y la dejamos lista y escalada según su frecuencia de muestreo.

4 limpiar ruido y movimiento de la línea base aplicando un filtro Butterworth pasa banda (0.5 a 40 Hz) con las funciones signal.butter() y signal.lfilter().

5  el registro se tomo en dos bloques (reposo y lectura). Usamos find_peaks() de SciPy para detectar los latidos, fijando una distancia mínima de 0.6 s y una prominencia de 0.3.

6 calcular los intervalos RR (tiempo entre latidos) para obtener la media y el SDNN. Además, graficamos los diagramas de Poincaré para extraer las métricas espaciales SD1 y SD2.

7 analizar los índices CSI (actividad simpática) y CVI (actividad parasimpática) para comparar numéricamente cómo reaccionó el sistema nervioso entre el reposo y la lectura.



DIAGRAMA DE FLUJO

<img width="455" height="618" alt="image" src="https://github.com/user-attachments/assets/40fd845c-5ed2-421d-9a49-196a7b985c6e" />




RESULTADOS HRV

| Parámetro | Reposo  | Lectura |
| --------- | ------- | ------- |
| Media RR  | 0.84 s  | 0.76 s  |
| SDNN      | 0.072 s | 0.049 s |
| SD1       | 0.041   | 0.028   |
| SD2       | 0.083   | 0.071   |
| CSI       | 2.02    | 2.53    |
| CVI       | -2.47   | -2.70   |



ECG Original

La señal ECG original presentó una adecuada morfología cardíaca permitiendo identificar claramente los complejos QRS. Sin embargo, también se observaron pequeñas fluctuaciones y componentes de ruido asociados a la adquisición biomédica y movimiento del paciente.



ECG Filtrado

El filtro Butterworth permitió reducir considerablemente las interferencias de alta frecuencia y las variaciones lentas de línea base. Esto facilitó la identificación de los picos R y mejoró la calidad general de la señal ECG para el análisis HRV.



Detección de Picos R

La detección automática de picos R realizada mediante `find_peaks()` mostró una adecuada precisión tanto en el segmento de reposo como en el segmento de lectura. Los picos detectados coincidieron correctamente con los complejos QRS observados en la señal ECG.



Diagramas de Poincaré

El diagrama de Poincaré obtenido durante el estado de reposo presentó una nube de puntos más dispersa, indicando mayor variabilidad cardíaca y predominio parasimpático. En contraste, durante la lectura la nube presentó menor dispersión y una alineación más longitudinal, indicando disminución de la variabilidad cardíaca y aumento relativo de actividad simpática.



ANÁLISIS DE LOS RESULTADOS

Los resultados reflejaron con claridad el impacto del esfuerzo vocal y cognitivo en el cuerpo. Durante la lectura en voz alta, el corazón se aceleró y los intervalos entre latidos disminuyeron junto con el SDNN, demostrando que la variabilidad total se reduce bajo estrés y vuelve al sistema cardiovascular momentáneamente menos flexible y adaptativo.

A nivel neurológico, este cambio se confirmó por el aumento del índice CSI y la leve caída del CVI, lo que demuestra un claro dominio del sistema simpático (el acelerador) sobre el parasimpático (el freno). Visualmente, los diagramas de Poincaré validaron este comportamiento al mostrar una nube de puntos mucho más compacta y alineada, reflejando de forma geométrica cómo el corazón pierde variabilidad durante la tarea.



PREGUNTAS

A. La lectura en voz alta cambia la variabilidad cardíaca?

Sí, puesto que al momento de la lectura se incrementa la actividad simpática asociada al esfuerzo cognitivo y respiratorio. Esto produce un aumento de la frecuencia cardíaca y una disminución de la variabilidad de los intervalos RR, evidenciada mediante la reducción de SDNN y SD1.



B. Es necesario filtrar la señal ECG?

Si, ya que ll filtrado logra eliminar ruido e interferencias presentes en la señal biomédica, tales como variaciones lentas de línea base y ruido de alta frecuencia. Esto mejora considerablemente la detección de los complejos QRS y aumenta la precisión del análisis HRV.



C. Qué representan  CVI y CSI?

El CSI es para el predominio de actividad simpática, y el  CVI para la actividad parasimpática y estos parámetros permiten evaluar el balance autonómico del organismo bajo diferentes condiciones fisiológicas.



CONCLUSIONES

En este laboratorio se verifico que logramos capturar y procesar con éxito la señal de ECG usando la STM32 y Pycharm, donde el filtro Butterworth fue clave para limpiar el ruido y dejar los picos R listos para su detección. Al analizar la HRV, saltó a la vista el impacto de la lectura en voz alta en comparación con el reposo: los parámetros SDNN y CSI, respaldados visualmente por unos diagramas de Poincaré mucho más compactos, confirmaron que el estrés de hablar aceleró el corazón, redujo su variabilidad y activó de inmediato el sistema simpático. Por ultimo para los índices geométricos y estadísticos utilizados demostraron ser herramientas útiles para evaluar el comportamiento del sistema nervioso autónomo y analizar la dinámica cardíaca bajo diferentes condiciones fisiológicas.
