```
idade = []
peso = []
jejun = []
doadores = 0
n_doadores = 0

for i in range(10):
    i = int(input("Idade: "))
    p = float(input("Peso: "))
    j = input("Em jejum? (s/n): ")

    if 18 <= i <= 67 and p > 50 and j.lower() == 's':
        doadores += 1
        print("Pode doar sangue.")
    else:
        n_doadores += 1
        print("Não pode doar sangue.")

print(f"Quantidade de doadores: {doadores}")
print(f"Quantidade de não doadores: {n_doadores}")

