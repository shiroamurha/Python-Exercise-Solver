```
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if idade <= 10:
    valor = 30
elif 10 < idade <= 29:
    valor = 60
elif 29 < idade <= 45:
    valor = 120
elif 45 < idade <= 59:
    valor = 150
elif 59 < idade <= 65:
    valor = 250
else:
    valor = 400

print(f"{nome} deve pagar R${valor:.2f}.")

