LABORATORIO 1 – SEÑALES
Andrea Carolina Amortegui Carrillo – 5600963
Sara Sofía Piñeros Tovar – 5600962

INTRODUCCIÓN

Los  (ECG)  electrocardiogramas son señales las cuales muestran el comportamiento del corazón en su forma eléctrica  en la cual se puede  analizar que partes están afectadas de acuerdo a la forma de ruido que arroja para así realizar una interpretación del resultado ya que esta nos da información fisiología del comportamiento eléctrico de corazon.
Para la realización de esta práctica, lo que se hizo fue generar un análisis de un (ECG) en la página  PhysioNet (registro ath_001) la cual son  datos reales, para luego cuantificar datos  manualmente y  en Python, tomando la señal por medio de un NI-DAQ identificando que tan buena era la señal por medio de (SNR)  alterando el ruido de la señal.


OBJETIVOS

Objetivo General

Identificar de forma estadística la  toma del ECG analizando su condición por medio de la Relación Señal-Ruido.

Objetivos Específicos

Tomar los datos de un ECG mediante PhysioNet.
 Realizar la gráfica y los cálculos de la señal en Python.
 Crear un histograma de las amplitudes.
 Obtener la señal  con el NI-DAQ
 Analizar el SNR mediante varias formas de ruido.

DESCRIPCIÓN DE LA SEÑAL

Implementamos un  registro ath_001, que le pertenece a  Norwegian Endurance Athlete ECG Database, la cual es una señal ECG, que cuenta con una derivación del Canal 1 con su frecuencia de 1000 Hz, para ser analizada en Python utilizando 20000 muestras para poder ser vista. por otro lado se usaron las siguientes librerías:  matplotlib, nidaqmx, scipy.stats, numpy y wfdb

 
PROCEDIMIENTO

Para la realización de esta guía, se inició con la lectura de los ECG por medio de wfdb.rdrecord("ath_001"), luego se tomó la derivación para construir el vector tiempo con el fin de mostrar la señal graficada, se calculó la media, coeficiente de variación, curtosis, skewness y desviación estándar, para evaluar los datos tomados de scipy.stats y numpy con el propósito de crear en 20 intervalos un histograma
Por otro lado, se tomó una señal por el NI-DAQ  que tenia en 10 segundos una frecuencia de 1000 Hz para realizar un procesamiento por medio de un .txt. y luego se analizo la contraste de la señal por el  SNR, e cual fue utilizado con ruido gaussiano, tipo artefacto e   impulso.

ANÁLISIS ESTADÍSTICO

Media: valor estimado de su amplitud

<img width="201" height="62" alt="image" src="https://github.com/user-attachments/assets/78f0c2bd-08a6-452d-b8ce-3c77643dc328" />


Desviación Estándar: dispersión de la señal de acuerdo al promedio

<img width="212" height="72" alt="image" src="https://github.com/user-attachments/assets/598e38ee-4633-4239-bc7a-e22b73319f66" />


Coeficiente de Variación: dispersión de la señal según la media

<img width="132" height="83" alt="image" src="https://github.com/user-attachments/assets/99ffc9e8-fac5-4d06-ad0c-5b0feeac8954" />



Skewness: asimetría en los picos r

<img width="323" height="88" alt="image" src="https://github.com/user-attachments/assets/4e6e7d22-52d9-41bd-8205-2da5200191bc" />


Curtosis. complejos QRS

<img width="312" height="91" alt="image" src="https://github.com/user-attachments/assets/96df522f-e77d-46f0-ac11-1bd3ba0a6fa8" />


TOMA DE SEÑAL

Con la NI-DAQ se realizó una configuración, ya que se ocuparon 1000 Hz para su Frecuencia de muestreo de 10 segundos y se obtuvo un total muestras de 10000, par después ser guardada en un archivo .txt y  vector de tiempo para poder ser vista gracias a la gráfica

(SNR) RELACIÓN SEÑAL RUIDO 
P ruido: promedio del ruido
P señal: promedio de la señal original

<img width="283" height="88" alt="image" src="https://github.com/user-attachments/assets/4625310c-aa9d-4915-a49b-fb31a099c495" />


Se ocuparon 3 ruidos. Gaussiano el cual disminuye el SNR  aumentando su varianza. El impulso proporciona picos que hacen que la curtosis aumente. El artefacto modifica su línea original alterando la desviación y la media

<img width="763" height="573" alt="image" src="https://github.com/user-attachments/assets/931f696f-1931-48e2-8874-35bcc81617e9" />
<img width="735" height="571" alt="image" src="https://github.com/user-attachments/assets/3d09e9e1-1fe8-40f0-93d4-100d58bf04f5" />
<img width="746" height="563" alt="image" src="https://github.com/user-attachments/assets/d57e4e5b-be23-48f5-9ad8-b2e9195e51c7" />



ANÁLISIS DE LOS RESULTADOS

Los datos  tomados lograron identificar de forma general el ECG, ya que se vio diferentes alteraciones según el ruido que se colocaba, debido a que en el impulso se modificó la organización de la señal, por parte de la curtosis, cuando esta se eleva, muestra los complejos QRS, y por último en el ruido gaussiano, se evidencio una disminución del SNR cambiando la forma de la onda, por lo cual se alteró la desviación, con ellos se pudo datificar el deterioro.


CONCLUSIONES

Como se evidencio, se pudo cuantificar la señal ECG real, y la señal capturada en laboratorio, y los datos fueron similares a los del  Python. Por otro lado, se comprobó que la curtosis es la responsable de aumentar la visualización de los complejos QRS en el ECG, comprobando así que hay  picos en actividad eléctrica del corazón.
Adicionalmente, el  SNR logró analizar  la activación de los cambios por medio de variaciones de ruidos para la señal, evidenciando como su integridad actúa de forma diferente.A pesar de esto, lo ideal sería complementar con otro tipo de formas de análisis para evaluar la señal, para si lograr unos datos más precisos y que el resultado sea más completo


PREGUNTAS

¿Los valores estadísticos de la señal real y la adquirida son iguales?


No, debido a que esta señal cuenta con cambios  del ritmo del corazón, tales como frecuencia y por otro lado, la señal que se obtuvo en la guía, está directamente relacionada con los equipo y su debida realización, generado que todos los datos cambian como lo sería  en su desviación estándar, curtosis y media

¿El tipo de ruido afecta la SNR?


Sí, puesto que cada  ruido alterado, va a cambiar  el comportamiento del SNR, ya que  cada uno actúa de forma distinta, como lo sería el  impulso, pues este crea pico exagerados que la alteran, por parte del artefacto su frecuencia disminuye y el gaussiano cambia señal de forma paulatinamente.
