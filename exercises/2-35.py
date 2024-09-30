canais = []
for i in range(5):
    canal = int(input(f"Qual o canal de TV que você assiste ({1}, {2}, {3}): "))
    canais.append(canal)

mais_assistido = canais.count(1)
if mais_assistido < canais.count(2):
    mais_assistido = canais.count(2)
if mais_assistido < canais.count(3):
    mais_assistido = canais.count(3)

if mais_assistido == 1:
    print("O canal mais assistido é a Globo.")
elif mais_assistido == 2:
    print("O canal mais assistido é o SBT.")
else:
    print("O canal mais assistido é a Band.")

