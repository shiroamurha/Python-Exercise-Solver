```
n = []
while True:
    x = int(input("Digite um valor (ou 99 para parar): "))
    if x == 99:
        break
    n.append(x)

total = len(n)
num10_50 = len([x for x in n if 10 <= x <= 50])
impares = len([x for x in n if x % 2 != 0])
soma_pares = sum([x for x in n if x % 2 == 0])
multiplos_5 = [(x, x) for x in n if x % 5 == 0]
maior = max(n)
menor = min(n)
media = sum(n) / len(n)

print(f"a) Total de números digitados: {total}")
print(f"b) Números entre 10 e 50: {num10_50}")
print(f"c) Números ímpares: {impares}")
print(f"d) Soma dos números pares: {soma_pares}")
print(f"e) Números múltiplos de 5: {multiplos_5}")
print(f"f) Média dos números digitados: {media}")
print(f"g) Maior e menor número digitado: {maior} e {menor}")

