b = int(input("Digite o valor de b: "))
n = int(input("Digite o valor de n: "))

while n <= 1:
    print("O valor de n deve ser maior que 1. Tente novamente!")
    n = int(input("Digite o valor de n: "))

while b < 2:
    print("O valor de b deve ser maior ou igual a 2. Tente novamente!")
    b = int(input("Digite o valor de b: "))

bn = b ** n
print("O valor de bn é: ", bn)

