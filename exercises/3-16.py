```
a = int(input("Intervalo inicial: "))
b = int(input("Intervalo final: "))

if a > b:
    print("Intervalo inválido")
else:
    pares = [i for i in range(a, b+1) if i % 2 == 0]
    impares = [i for i in range(a, b+1) if i % 2 != 0]
    soma_pares = sum(pares)
    media_impares = sum(impares) / len(impares)

    print("Valores:", end=" ")
    for i in range(a, b+1):
        print(i, end=" ")
    print()
    print("Quantidade de pares:", len(pares))
    print("Soma dos pares:", soma_pares)
    print("Quantidade de ímpares:", len(impares))
    print("Média dos ímpares:", media_impares)

