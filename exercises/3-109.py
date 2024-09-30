```
inter_gols = 0
gremio_gols = 0
inter_vitorias = 0
gremio_vitorias = 0
empates = 0
total_grenais = 0

while True:
    inter_gols = int(input("Gols do Inter: "))
    gremio_gols = int(input("Gols do Grêmio: "))
    total_grenais += 1

    if inter_gols > gremio_gols:
        inter_vitorias += 1
    elif inter_gols < gremio_gols:
        gremio_vitorias += 1
    else:
        empates += 1

    print("Novo GRENAL")
    print("1.Sim 2.Não?")
    resposta = int(input())

    if resposta == 1:
        continue
    else:
        break

print(f"Total de GRENAIS: {total_grenais}")
print(f"Time do Inter venceu {inter_vitorias} vezes")
print(f"Time do Grêmio venceu {gremio_vitorias} vezes")
print(f"Houve {empates} empates")
if inter_vitorias > gremio_vitorias:
    print("O time do Inter é o campeão")
elif inter_vitorias < gremio_vitorias:
    print("O time do Grêmio é o campeão")
else:
    print("Não houve um vencedor")

