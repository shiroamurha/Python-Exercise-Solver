n = int(input("Quantos números você deseja digitar? "))
maior = menor = 0

for i in range(n):
    num = int(input(f"Digite o {i+1}º número: "))
    if i == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

