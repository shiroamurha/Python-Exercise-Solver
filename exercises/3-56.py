```
n = int(input("Quantos valores deseja digitar? "))
for i in range(n):
    valor = float(input(f"Digite o valor {i+1}: "))
    print(f"A raiz cúbica de {valor} é {valor ** (1/3)}")

