```
n = int(input("Digite o número de elementos: "))
valores = []
for i in range(n):
    valores.append(int(input(f"Digite o {i+1}º valor: ")))

maior = max(valores)
menor = min(valores)
soma = sum(valores)
media = soma / n

maiores_20 = len([x for x in valores if x > 20])
percentagem_maiores_10 = (maiores_20 / n) * 100

media_entre_10_e_100 = sum([x for x in valores if 10 <= x <= 100]) / len([x for x in valores if 10 <= x <= 100])

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
print(f"Quantos números maiores a 20: {maiores_20}")
print(f"Percentagem de valores maiores que 10: {percentagem_maiores_10:.2f}%")
print(f"Média dos valores entre 10 e 100: {media_entre_10_e_100:.2f}")
```

