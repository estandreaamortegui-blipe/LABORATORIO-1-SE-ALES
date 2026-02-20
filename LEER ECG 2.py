import wfdb
import nidaqmx
from nidaqmx.constants import (AcquisitionType)
import matplotlib.pyplot as plt
import os
import numpy as np

#GRAFICA DE LA SEÑAL
record = wfdb.rdrecord("ath_001")
signal = record.p_signal# p_signal contiene la matriz con las señales digitales del registro Dimensión típica: (muestras, canales)
print("Forma de la señal:", signal.shape) # Muestra el número de muestras y número de derivaciones
print("Frecuencia de muestreo:", record.fs)

x=signal[:,1]
N=len(x)
fs = record.fs
tiempo = []
for n in range(N):
    tiempo.append(n/fs)

plt.figure()
plt.plot(tiempo[:20000], x[:20000])
plt.title("Señal ECG Original")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

#Estadistica
suma=0 # Se inicializan las variables para poder hacer las estadisticas
sumacuadrado=0
sumaskew=0
sumacurt=0

# MEDIA
for m in range(N):
    suma+=x[m] #se suman los datos de x tomados desde la grafica y se meten en un arreglo m
media=suma/N #se divide esta suma entre la cantidad de muestras o qrs
print ("MANUAL")
print ("Media:",media)

#DESVIACION
sumacuadrado = 0  # Reiniciar acumulador
for m in range(N):
    sumacuadrado += (x[m] - media)**2  # Se calcula la diferencia entre cada dato y la media, luego se eleva al cuadrado
varianza = sumacuadrado / N
desviacion = varianza**0.5
print("Desviación:", desviacion)

#Coeficiente de variacion
cv=abs(desviacion/media)
print ("Coeficiente de variación:",cv)

#HISTOGRAMA
intervalos=20
xmin=x[0]
xmax=x[0]
for m in range(N):
    if x[m]>xmax:
        xmax=x[m]
    if x[m]<xmin:
        xmin=x[m]
ancho=(xmax-xmin)/intervalos
frecuencia=[0]*intervalos
for m in range(N):
    indice=int((x[m]-xmin)/ancho)
    if indice >= intervalos:
        indice= intervalos-1
    frecuencia[indice]+=1

#SKEWNESS
for m in range(N):
    sumaskew+= ((x[m]- media)/desviacion)**3
skew=sumaskew/N
print ("Skewness:",skew)

#CURTOSIS
for m in range(N):
    sumacurt+=((x[m]-media)/desviacion)**4
kurtosis=sumacurt/N
kurt=kurtosis-3
print ("Kurtosis:",kurtosis)
print("Exceso de kurtosis:",kurt)

#CON FUNCIONES DE PYTHON
from scipy.stats import skew, kurtosis
print ("CON FUNCIONES DE PYTHON")
media_np = np.mean(x)
desv_np = np.std(x)
cv_np = desv_np / media_np

#MEDIA
media_np= np.mean(x)
print("Media:", media_np)

#DESVIACION
desviacion_np= np.std(x)
print("Desviación estándar:", desv_np)

#COEFICIENTE DE VARIACION
if media_np != 0:
    cv_np = desv_np / abs(media_np)
    print("Coeficiente de variación:", cv_np)

#HISTOGRAMA
plt.figure()
plt.hist(x, bins=20)
plt.title("Histograma ECG")
plt.xlabel("Amplitud")
plt.ylabel("Frecuencia")
plt.show()

#SKEWNESS
skew_np = skew(x)
print("Skewness:", skew_np)

#CURTOSIS
kurt_np = kurtosis(x)   # devuelve exceso de curtosis
kurt_total = kurt_np + 3
print("Curtosis:", kurt_total)
print("Exceso de curtosis:", kurt_np)

# PARÁMETROS DE ADQUISICIÓN

fs = 1000  # Frecuencia de muestreo (Hz)
duracion = 10  # Duración en segundos
dispositivo = "Dev2/ai1"  # Verificar en NI MAX

total_muestras = int(fs * duracion)

# RUTA DONDE SE GUARDARÁ EL ARCHIVO

ruta_guardado = r"C:/Users/USER/OneDrive/ANDY/UNI/3ER SEMESTRE/SEÑALES/"
nombre_archivo = "senal_adquirida.txt"

# Crear carpeta si no existe
os.makedirs(ruta_guardado, exist_ok=True)

ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
# ADQUISICIÓN DE LA SEÑAL

with nidaqmx.Task() as task:
    # Agregar canal analógico
    task.ai_channels.add_ai_voltage_chan(dispositivo)

    # Configurar reloj de muestreo
    task.timing.cfg_samp_clk_timing(
        rate=fs,
        sample_mode=AcquisitionType.FINITE,
        samps_per_chan=total_muestras
    )

    # Leer datos
    senal = task.read(number_of_samples_per_channel=total_muestras)
# PROCESAMIENTO
senal = np.array(senal)
t = np.arange(len(senal)) / fs

# GUARDAR ARCHIVO
datos = np.column_stack((t, senal))
np.savetxt(
    ruta_completa,
    datos,
    delimiter="\t",
    header="Tiempo(s)\tVoltaje(V)",
    comments=''
)
print("Archivo guardado en:")
print(ruta_completa)
# GRÁFICA
plt.figure()
plt.plot(t, senal)
plt.grid()
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.title(f"fs = {fs} Hz | Duración = {duracion} s | Muestras = {len(senal)}")
plt.show()
data = np.loadtxt("senal_adquirida.txt", skiprows=1)
t = data[:,0]
senal = data[:,1]

# FUNCIÓN SNR
def calcular_snr(signal, signal_noisy):
    ruido = signal_noisy - signal      # Diferencia = ruido agregado
    pot_signal = np.mean(signal**2)    # Potencia señal
    pot_ruido = np.mean(ruido**2)      # Potencia ruido
    snr = 10 * np.log10(pot_signal / pot_ruido)
    return snr

# Ruido gaussiano
ruido_gauss = np.random.normal(0, 0.03, len(senal))
senal_gauss = senal + ruido_gauss
snr_gauss = calcular_snr(senal, senal_gauss)
print("SNR Ruido Gaussiano:", snr_gauss, "dB")
plt.figure()
plt.plot(t, senal_gauss)
plt.title(f"Señal con Ruido Gaussiano | SNR = {snr_gauss:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()
senal_impulso = senal.copy()

# 1% de muestras contaminadas
num_impulsos = int(0.005 * len(senal))   # Solo 0.5%
senal_impulso[indices] = np.max(senal) * 1.2
senal_impulso[indices] = np.max(senal) * 2
snr_impulso = calcular_snr(senal, senal_impulso)
print("SNR Ruido Impulso:", snr_impulso, "dB")
plt.figure()
plt.plot(t, senal_impulso)
plt.title(f"Señal con Ruido Impulso | SNR = {snr_impulso:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()

#Ruido Artefacto
artefacto = 0.15 * np.sin(2*np.pi*1*t)
senal_artefacto = senal + artefacto
snr_artefacto = calcular_snr(senal, senal_artefacto)
print("SNR Ruido Artefacto:", snr_artefacto, "dB")
plt.figure()
plt.plot(t, senal_artefacto)
plt.title(f"Señal con Artefacto | SNR = {snr_artefacto:.2f} dB")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()
