gremio = int(input("Gols do Grêmio: "))
inter = int(input("Gols do Inter: "))

if gremio > inter:
    print("O Grêmio é o vencedor!")
    print(f"O Grêmio fez {gremio - inter} gols a mais.")
elif inter > gremio:
    print("O Inter é o vencedor!")
    print(f"O Inter fez {inter - gremio} gols a mais.")
else:
    print("EMPATE")
    print(f"Grêmio: {gremio} gols")
    print(f"Inter: {inter} gols")

