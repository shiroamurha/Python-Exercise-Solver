gols_gremio = int(input("Gols do Grêmio: "))
gols_inter = int(input("Gols do Inter: "))

if gols_gremio > gols_inter:
    print("Vencedor: Grêmio")
elif gols_gremio < gols_inter:
    print("Vencedor: Inter")
else:
    print("Empate")

