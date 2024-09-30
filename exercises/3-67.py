maior = 0
menor = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print("O maior número é:", maior)
print("O menor número é:", menor)

