from scipy import signal
from scipy.io import wavfile

# =========================================================
# a. SEÑAL ECG
# =========================================================

fs, ecg = wavfile.read("ecg.wav")

# usar un canal
if len(ecg.shape) > 1:
    ecg = ecg[:, 0]

# Normalizar
ecg = ecg / np.max(np.abs(ecg))

# tiempo
t = np.arange(len(ecg)) / fs

# =========================================================
# b. GRAFICA ORIGINAL
# =========================================================

plt.figure(figsize=(12,4))
plt.plot(t, ecg)
plt.title("ECG Original")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# =========================================================
# c. BUTTERWORTH
# =========================================================

lowcut = 0.5
highcut = 40
order = 4

# Nyquist
nyquist = fs / 2

# Normalizar
low = lowcut / nyquist
high = highcut / nyquist

# filtro
b, a = signal.butter(order, [low, high], btype='band')

# =========================================================
# d. ECG FILTRADO
# =========================================================

ecg_filtrado = signal.lfilter(b, a, ecg)

# =========================================================
# e. FILTRO GRAFICADO
# =========================================================

plt.figure(figsize=(12,4))
plt.plot(t, ecg_filtrado)
plt.title("ECG Filtrado")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# =========================================================
# f. REPOSO Y LECTURA
# =========================================================

mitad = len(ecg_filtrado) // 2

reposo = ecg_filtrado[:mitad]
lectura = ecg_filtrado[mitad:]

t1 = t[:mitad]
t2 = t[mitad:]

# =========================================================
# g. PICOS R
# =========================================================

distancia = int(0.6 * fs)

peaks1, _ = signal.find_peaks(
    reposo,
    distance=distancia,
    prominence=0.3
)

peaks2, _ = signal.find_peaks(
    lectura,
    distance=distancia,
    prominence=0.3
)

# =========================================================
# h. PICOS R GRAFICADOS
# =========================================================

plt.figure(figsize=(12,4))
plt.plot(t1, reposo)
plt.plot(t1[peaks1], reposo[peaks1], "ro")
plt.title("Picos R - Reposo")
plt.xlabel("Tiempo [s]")
plt.grid()
plt.show()

plt.figure(figsize=(12,4))
plt.plot(t2, lectura)
plt.plot(t2[peaks2], lectura[peaks2], "ro")
plt.title("Picos R - Lectura")
plt.xlabel("Tiempo [s]")
plt.grid()
plt.show()

# =========================================================
# i. RR
# =========================================================

rr1 = np.diff(peaks1) / fs
rr2 = np.diff(peaks2) / fs

# =========================================================
# j. MEDIA SDNN y RR
# =========================================================

media_rr1 = np.mean(rr1)
media_rr2 = np.mean(rr2)

sdnn1 = np.std(rr1)
sdnn2 = np.std(rr2)

print("\n============== RESULTADOS HRV ==============")

print("\nREPOSO")
print("Media RR:", media_rr1)
print("SDNN:", sdnn1)

print("\nLECTURA")
print("Media RR:", media_rr2)
print("SDNN:", sdnn2)

# =========================================================
# k. POINCARÉ
# =========================================================

x1 = rr1[:-1]
y1 = rr1[1:]

x2 = rr2[:-1]
y2 = rr2[1:]

plt.figure(figsize=(6,6))
plt.scatter(x1, y1)
plt.title("Poincaré - Reposo")
plt.xlabel("RR(n)")
plt.ylabel("RR(n+1)")
plt.grid()
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(x2, y2)
plt.title("Poincaré - Lectura")
plt.xlabel("RR(n)")
plt.ylabel("RR(n+1)")
plt.grid()
plt.show()

# =========================================================
# l. SD1 Y SD2
# =========================================================

def poincare(rr):

    diff_rr = np.diff(rr)

    sd1 = np.sqrt(np.var(diff_rr) / 2)

    sd2 = np.sqrt(
        2 * np.var(rr) - (np.var(diff_rr) / 2)
    )

    return sd1, sd2

sd1_1, sd2_1 = poincare(rr1)
sd1_2, sd2_2 = poincare(rr2)

# =========================================================
# m. CSI Y CVI
# =========================================================

csi1 = sd2_1 / sd1_1
cvi1 = np.log10(sd1_1 * sd2_1)

csi2 = sd2_2 / sd1_2
cvi2 = np.log10(sd1_2 * sd2_2)

print("\n============== POINCARÉ ==============")

print("\nREPOSO")
print("SD1:", sd1_1)
print("SD2:", sd2_1)
print("CSI:", csi1)
print("CVI:", cvi1)

print("\nLECTURA")
print("SD1:", sd1_2)
print("SD2:", sd2_2)
print("CSI:", csi2)
print("CVI:", cvi2)
