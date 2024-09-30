maior = float('-inf')
menor = float('inf')
for i in range(50):
    valor = float(input())
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print("Maior valor:", maior)
print("Menor valor:", menor)

