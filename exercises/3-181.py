```
pares = 0
impares = 0
soma_pares = 0
soma_total = 0
n = int(input())

while n != 0:
    if n > 0:
        if n % 2 == 0:
            pares += 1
            soma_pares += n
        else:
            impares += 1
        soma_total += n
    n = int(input())

media_pares = soma_pares / pares if pares > 0 else 0
media_total = soma_total / (pares + impares)

print(f'Quantidade de pares: {pares}')
print(f'Quantidade de impares: {impares}')
print(f'Média dos pares: {media_pares}')
print(f'Média geral: {media_total}')

