```
soma = 0
cont_pares = 0
for i in range(10):
    n = int(input("Digite um número: "))
    soma += n
    if n % 2 == 0:
        cont_pares += 1
if soma % 2 == 0:
    print("A soma é", soma, "e foram digitados", cont_pares, "pares.")
else:
    print("A soma é", soma, "e foram digitados", 10 - cont_pares, "ímpares.")

