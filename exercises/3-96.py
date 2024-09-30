n = int(input("Quantos números deseja somar? "))
soma = 0
for i in range(n):
    soma += int(input("Insira o número {}: ".format(i+1)))
print("A soma é: ", soma)

