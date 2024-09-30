```
n = int(input("Quantos valores você deseja digitar? "))
soma = 0
for i in range(n):
    valor = float(input("Digite o valor {}: ".format(i+1)))
    soma += valor
media = soma / n
if media > 30:
    print("A média é maior que 30.")
else:
    print("A média é menor ou igual a 30.")
print("A média é: {:.2f}".format(media))

