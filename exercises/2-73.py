pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(10):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    elif valor % 2 != 0:
        impares += 1
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

