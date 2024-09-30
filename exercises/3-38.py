numbers = []
for i in range(10):
    numbers.append(int(input("Insira um número: ")))

soma = 0
cont = 0
for num in numbers:
    if num % 2 != 0:
        soma += num
        cont += 1

media = soma / cont
print("Média dos números ímpares: ", media)

