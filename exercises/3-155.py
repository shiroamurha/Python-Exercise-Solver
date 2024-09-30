```
n = int(input("Digite um número: "))
while n >= 1:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é {fatorial}")
    n = int(input("Digite outro número (ou um número menor que 1 para parar): "))

