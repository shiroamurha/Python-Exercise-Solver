```
soma = 0
cont = 0
maior = float('-inf')
menor = float('inf')

while True:
    n = float(input())
    if n == 0:
        break
    soma += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n

media = soma / cont
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Media: {media:.2f}")

