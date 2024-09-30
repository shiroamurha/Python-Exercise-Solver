total_eleitores = int(input())
votos_candidato1 = int(input())
votos_candidato2 = int(input())

votos_nulos = total_eleitores - votos_candidato1 - votos_candidato2

porcentagem_candidato1 = (votos_candidato1 / total_eleitores) * 100
porcentagem_candidato2 = (votos_candidato2 / total_eleitores) * 100
porcentagem_nulos = (votos_nulos / total_eleitores) * 100

print(f'Percentual de votos do 1o candidato: {porcentagem_candidato1:.2f}%')
print(f'Percentual de votos do 2o candidato: {porcentagem_candidato2:.2f}%')
print(f'Percentual de votos nulos: {porcentagem_nulos:.2f}%')

