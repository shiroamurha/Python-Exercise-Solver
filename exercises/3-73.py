num = int(input("Digite um número (-999 para parar): "))
while num != -999:
    divisores = [i for i in range(1, num+1) if num % i == 0]
    print(divisores)
    num = int(input("Digite um número (-999 para parar): "))

