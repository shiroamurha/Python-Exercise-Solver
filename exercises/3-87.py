pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(10):
    x = int(input())
    if x % 2 == 0:
        pares += 1
    else:
        impares += 1
    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')

