tamanho_arquivo = float(input("Tamanho do arquivo (em MB): "))
velocidade_internet = float(input("Velocidade da Internet (em Mbps): "))

tempo_download = (tamanho_arquivo * 8) / velocidade_internet

minutos = tempo_download / 60

print("O tempo aproximado de download é de {:.2f} minutos.".format(minutos))

