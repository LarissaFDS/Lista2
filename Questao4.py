import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Função para leitura dos arquivos WAV
def read(file):
    sample_rate, data = wav.read(file)
    if len(data.shape) == 2:  # Verifica se tem 2 canais
      data = np.mean(data, axis=1)
    return sample_rate, data

# Leitura dos arquivos de áudio
rate1, audio1 = read("audio1.wav")
rate2, audio2 = read("audio2.wav")
min_len = min(audio1.shape[0], audio2.shape[0])

audio1 = audio1[:min_len]
audio2 = audio2[:min_len]

time1 = np.linspace(0., len(audio1) / rate1, len(audio1))
time2 = np.linspace(0., len(audio2) / rate2, len(audio2))

# Definindo os coeficientes da combinação linear
a = 0.7  # Exemplo de coeficiente para o áudio 1
b = 0.3  # Exemplo de coeficiente para o áudio 2

# Fazendo a combinação linear
result = a * audio1 + b * audio2

# Normalizando para evitar distorção
result = result / np.max(np.abs(result))  # Normalizar entre -1 e 1
result = np.int16(result * 32767)  # Converter para int16

result_time = np.linspace(0., len(result) / rate1, len(result))

# Plot do audio1
plt.subplot(3, 1, 1)
plt.plot(time1, audio1, label="Áudio 1")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do audio 2
plt.subplot(3, 1, 2)
plt.plot(time2, audio2, label="Áudio 2")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do result
plt.subplot(3, 1, 3)
plt.plot(result_time, result, label="Resultado")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

plt.show()

# Salvando o arquivo resultante
wav.write("resultado.wav", rate1, result)
print(f'coeficiente 1: {a}, coeficiente 2: {b}')
