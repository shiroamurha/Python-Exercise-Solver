```
n = int(input("Digite um valor: "))
while True:
    print(n, end=' ')
    n = int(input("Deseja digitar outro valor (1.Sim 2.Não)? "))
    if n == 2:
        break

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))

print("O menor valor é:", min(n1, n2, n3, n4))

