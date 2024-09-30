```
soma_pares = 0
soma_impares = 0
count_maiores_50 = 0
count_maiores_20 = 0
maior_valor = float('-inf')
menor_valor = float('inf')
count = 0

while True:
    num = float(input("Digite um número: "))
    if num < 0:
        break
    count += 1
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num
    if num > 50:
        count_maiores_50 += 1
    if num > 20:
        count_maiores_20 += 1
    if 50 <= num <= 150 and num % 2 == 0:
        soma_pares += num

media_impares = soma_impares / count_maiores_20
media_pares_50_150 = soma_pares / count_maiores_20
percentagem_maiores_20 = (count_maiores_20 / count) * 100
total_valores = count

print(f"O maior valor é {maior_valor}")
print(f"O menor valor é {menor_valor}")
print(f"A soma dos valores pares é {soma_pares}")
print(f"A média dos valores ímpares é {media_impares}")
print(f"Quantos números maiores a 50 {count_maiores_50}")
print(f"A percentagem de valores maiores que 20 é {percentagem_maiores_20}%")
print(f"A média dos valores pares que estão entre 50 e 150 é {media_pares_50_150}")
print(f"O total de valores digitados é {total_valores}")
```

