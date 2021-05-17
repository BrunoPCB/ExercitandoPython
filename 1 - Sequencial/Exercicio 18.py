"""
18 - Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""
# Recebendo dados
tamanho_arquivo = float(input("Informe o tamanho do arquivo para download[MB]: "))
velocidade_internet = float(input("Informe a velocidade de download[Mbps]: "))

# Cálculo
tempo_daownload = tamanho_arquivo / velocidade_internet

print(f"Tamanho: {tamanho_arquivo:.2f} Mb\n"
      f"Velocidade: {velocidade_internet:.2f} Mbps")
print(f"O seu ddownload terminará em {tempo_daownload:.1f} segundos.")
