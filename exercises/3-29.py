```
N = int(input())
soma = 0
maior = float('-inf')
menor = float('inf')
for i in range(N):
    x = float(input())
    if x > 0:
        soma += x
        if x > maior:
            maior = x
        if x < menor:
            menor = x
media = soma / N
print('Soma:', soma)
print('Média:', media)
print('Maior valor:', maior)
print('Menor valor:', menor)

