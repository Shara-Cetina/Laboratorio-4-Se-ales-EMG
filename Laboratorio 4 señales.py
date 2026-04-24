# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:19:09 2026

@author: manue
"""
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import firwin, filtfilt, periodogram

# Cargar los datos del archivo .txt
datos_emg = np.loadtxt('EMG_1minuto.txt')

# Definir parámetros de adquisición
fs = len(datos_emg) / 60
n = len(datos_emg)

# Crear el eje del tiempo en segundos
tiempo = np.arange(n) / fs

# Graficar la señal original
plt.figure(figsize=(10, 4))
plt.plot(tiempo, datos_emg, label='EMG Bruta')
plt.title('Visualización de la Señal EMG')
plt.xlabel('Tiempo (s)')
plt.ylabel('Potencial de acción')
plt.grid(True)
plt.legend()
plt.show()

# Definir los rangos en SEGUNDOS (inicio, fin)
segmentos_segundos = [
    (0.0, 6.0), # Contracción 1
    (6.0, 12.0), # Contracción 2
    (12.0, 18.0), # Contracción 3
    (18.0, 24.0), # Contracción 4
    (24.0, 30.0)  # Contracción 5
]

# Diccionario para guardar los datos segmentados
contracciones_dict = {}

# Filtro pasa banda EMG (20–450 Hz)
numtaps = 201

# Filtro FIR pasa banda con ventana de Hamming
b = signal.firwin(numtaps, [20, 250], pass_zero=False, fs=fs, window='hamming')

for i, (t_inicio, t_fin) in enumerate(segmentos_segundos):
    # Convertir segundos a índices enteros
    idx_inicio = int(t_inicio * fs)
    idx_fin = int(t_fin * fs)
    
    # Extraer el segmento de la señal bruta
    segmento = datos_emg[idx_inicio:idx_fin]

    # Aplicar filtro
    segmento_filtrado = signal.filtfilt(b, [1.0], segmento)

    # Calcular espectro con señal filtrada
    f, psd = signal.periodogram(segmento_filtrado, fs)
    
    # MNF: Frecuencia Media (Suma de producto f*P / Suma P)
    mnf = np.sum(f * psd) / np.sum(psd)
    
    # MDF: Frecuencia Mediana
    psd_acumulada = np.cumsum(psd)
    mitad_potencia = psd_acumulada[-1] / 2

    # np.where devuelve una tupla. Usamos  para obtener el PRIMER valor del PRIMER arreglo.
    indices = np.where(psd_acumulada >= mitad_potencia)[0]

    if len(indices) > 0:
        idx_primero = indices[0]
        mdf = float(f[idx_primero])
    else:
        mdf = 0.0

    # Guardar en el diccionario asegurando que sean escalares
    contracciones_dict[f'Contraccion_{i+1}'] = {
        'datos_crudos': segmento,          #sin filtrar
        'datos_filtrados': segmento_filtrado,
        'tiempos': (t_inicio, t_fin),
        'MNF': float(mnf),
        'MDF': mdf
    }   
    
# Crear una figura con 5 divisiones dispuestas verticalmente
fig1, axes1 = plt.subplots(nrows=5, ncols=1, figsize=(10, 12))
fig1.suptitle('Contracciones SIN filtrar', fontsize=16)

for i in range(5):
    key = f'Contraccion_{i+1}'
    datos = contracciones_dict[key]['datos_crudos']
    t_inicio, t_fin = contracciones_dict[key]['tiempos']
    
    eje_tiempo = np.arange(len(datos)) / fs
    
    axes1[i].plot(eje_tiempo, datos, color='pink')
    axes1[i].set_title(f'{key} ({t_inicio}s - {t_fin}s)')
    axes1[i].set_ylabel('Potencial de acción')
    axes1[i].grid(True, linestyle='--', alpha=0.6)

axes1[-1].set_xlabel('Tiempo (s)')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
    
fig2, axes2 = plt.subplots(nrows=5, ncols=1, figsize=(10, 12))
fig2.suptitle('Contracciones FILTRADAS (FIR - Hamming)', fontsize=16)

for i in range(5):
    key = f'Contraccion_{i+1}'
    datos = contracciones_dict[key]['datos_filtrados']
    t_inicio, t_fin = contracciones_dict[key]['tiempos']
    
    eje_tiempo = np.arange(len(datos)) / fs
    
    axes2[i].plot(eje_tiempo, datos, color='teal')
    axes2[i].set_title(f'{key} ({t_inicio}s - {t_fin}s)')
    axes2[i].set_ylabel('Potencial de acción')
    axes2[i].grid(True, linestyle='--', alpha=0.6)

    mnf = contracciones_dict[key]['MNF']
    mdf = contracciones_dict[key]['MDF']
    axes2[i].text(0.02, 0.8, f'MNF: {mnf:.1f}Hz\nMDF: {mdf:.1f}Hz', 
                  transform=axes2[i].transAxes,
                  fontsize=9,
                  bbox=dict(facecolor='white', alpha=0.6))

axes2[-1].set_xlabel('Tiempo (s)')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Crear listas para la tabla
nombres = []
mnf_list = []
mdf_list = []

for i in range(5):
    key = f'Contraccion_{i+1}'
    
    nombres.append(key)
    mnf_list.append(contracciones_dict[key]['MNF'])
    mdf_list.append(contracciones_dict[key]['MDF'])

# Crear DataFrame (estructura para la tabla)
tabla = pd.DataFrame({
    'Contracción': nombres,
    'MNF (Hz)': mnf_list,
    'MDF (Hz)': mdf_list
})

print(tabla)

contracciones = range(1, 6)

plt.plot(contracciones, mnf_list, marker='o', label='MNF')
plt.plot(contracciones, mdf_list, marker='s', label='MDF')

plt.title('Evolución de frecuencias por contracción')
plt.xlabel('Contracción')
plt.ylabel('Frecuencia (Hz)')
plt.grid(True)
plt.legend()

plt.show()

# Aplicar filtro a TODA la señal
senal_filtrada = signal.filtfilt(b, [1.0], datos_emg)

plt.figure(figsize=(10,4))
plt.plot(tiempo, datos_emg, alpha=0.4, label='Señal Bruta')
plt.plot(tiempo, senal_filtrada, color='red', label='Señal Filtrada')
plt.title('Señal EMG Completa Filtrada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Potencial de acción')
plt.legend()
plt.grid(True)
plt.show()

#-------------------------------------------------------------------------------
#PARTE B
# Cargar señal
senal = np.loadtxt('EMG_Sharaminuto.txt')

fs = len(senal) / 60   # señal de 1 minuto
N = len(senal)

tiempo = np.arange(N) / fs

# Filtro FIR (Hamming)
lowcut = 20
highcut = 450
numtaps = 401

coef = firwin(numtaps,
              [lowcut, highcut],
              pass_zero=False,
              fs=fs,
              window='hamming')

senal_filtrada = filtfilt(coef, [1.0], senal)

# Normalización (solo visual)
senal_filtrada = senal_filtrada - np.mean(senal_filtrada)
senal_filtrada = senal_filtrada / np.max(np.abs(senal_filtrada))

# VISUALIZACIÓN COMPLETA
step = 20

plt.figure(figsize=(12,4))
plt.plot(tiempo[::step], senal[::step], linewidth=0.6)
plt.title("Señal EMG Original (Completa)")
plt.xlabel("Tiempo (s)")
plt.ylabel('Potencial de acción')
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(12,4))
plt.plot(tiempo[::step], senal_filtrada[::step], linewidth=0.7)
plt.ylim(-0.8, 0.8)
plt.title("Señal EMG Filtrada (Hamming)")
plt.xlabel("Tiempo (s)")
plt.ylabel('Potencial de acción')
plt.grid(alpha=0.3)
plt.show()

# 5. ZOOM
inicio = 0
fin = int(3 * fs)

plt.figure(figsize=(10,4))
plt.plot(tiempo[inicio:fin], senal[inicio:fin])
plt.title("Zoom Señal Original")
plt.xlabel("Tiempo (s)")
plt.ylabel('Potencial de acción')
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(tiempo[inicio:fin], senal_filtrada[inicio:fin])
plt.title("Zoom Señal Filtrada")
plt.xlabel("Tiempo (s)")
plt.ylabel('Potencial de acción')
plt.grid(alpha=0.3)
plt.show()

# SEGMENTACIÓN
segmentos_segundos = [
    (1.5, 4.5),
    (7.5, 10.5),
    (13.5, 16.5),
    (19.5, 22.5),
    (25.5, 28.5)
]

resultados = []
print("")

peak_freqs = []

# 7. ANÁLISIS POR CONTRACCIÓN
for i, (t_ini, t_fin) in enumerate(segmentos_segundos):

    idx_ini = int(t_ini * fs)
    idx_fin = int(t_fin * fs)

    segmento = senal_filtrada[idx_ini:idx_fin]

    # FFT
    N_seg = len(segmento)
    fft_vals = np.fft.rfft(segmento)
    fft_vals = (2 / N_seg) * np.abs(fft_vals)
    freqs = np.fft.rfftfreq(N_seg, 1/fs)

    # PSD (para MNF y MDF)
    f, psd = periodogram(segmento, fs)
    
    # Pico espectral
    f_valid = f[1:]           # evitar 0 Hz
    psd_valid = psd[1:]
    
    idx_peak = np.argmax(psd_valid)
    f_peak = f_valid[idx_peak]
    
    peak_freqs.append(f_peak)

    print(f"Contracción {i+1}: Pico espectral = {f_peak:.2f} Hz")

    mnf = np.sum(f * psd) / np.sum(psd)

    psd_acum = np.cumsum(psd)
    mitad = psd_acum[-1] / 2
    mdf = f[np.where(psd_acum >= mitad)[0][0]]

    resultados.append((mnf, mdf))

    print(f"Contracción {i+1}: MNF={mnf:.2f} Hz | MDF={mdf:.2f} Hz")

    # GRÁFICAS
    # Señal en el tiempo
    t_seg = np.arange(N_seg) / fs

    plt.figure(figsize=(10,3))
    plt.plot(t_seg, segmento)
    plt.title(f"Contracción {i+1} - Señal")
    plt.xlabel("Tiempo (s)")
    plt.ylabel('Potencial de acción')
    plt.grid(alpha=0.3)
    plt.show()

    # FFT en semilog (eje Y logarítmico)
    plt.figure(figsize=(10,3))
    plt.semilogy(freqs, fft_vals)
    plt.xlim(0, 500)
    plt.title(f"Contracción {i+1} - FFT")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud []")
    plt.grid(alpha=0.3, which='both')
    plt.show()
    
    # Espectro de amplitud (lineal)
    plt.figure(figsize=(10,3))
    plt.plot(freqs, fft_vals, linewidth=1)
    plt.axvline(mnf, color='r', linestyle='--', label='MNF')
    plt.axvline(mdf, color='g', linestyle='--', label='MDF')
    plt.xlim(0, 500)
    plt.title(f"Contracción {i+1} - Espectro de Amplitud")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud []")
    plt.grid(alpha=0.3)
    plt.show()

# TENDENCIA DE FRECUENCIAS
mnf_vals = [r[0] for r in resultados]
mdf_vals = [r[1] for r in resultados]

plt.figure(figsize=(8,5))
plt.plot(range(1,6), mnf_vals, marker='o', label='MNF')
plt.plot(range(1,6), mdf_vals, marker='s', label='MDF')

plt.title("Evolución de Frecuencia (Fatiga)")
plt.xlabel("Contracción")
plt.ylabel("Frecuencia (Hz)")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(range(1,6), peak_freqs, marker='^', color='purple')

plt.title("Desplazamiento del Pico Espectral")
plt.xlabel("Contracción")
plt.ylabel("Frecuencia (Hz)")
plt.grid(True)
plt.show()