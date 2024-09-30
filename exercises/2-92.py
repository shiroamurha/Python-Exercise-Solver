```
prato = input("Escolha o prato: ")
sobremesa = input("Escolha a sobremesa: ")
bebida = input("Escolha a bebida: ")

if prato == "Vegetariano":
    calorias_prato = 180
elif prato == "Peixe":
    calorias_prato = 230
elif prato == "Frango":
    calorias_prato = 250
elif prato == "Carne":
    calorias_prato = 350
else:
    calorias_prato = 0

if sobremesa == "Abacaxi":
    calorias_sobremesa = 75
elif sobremesa == "Sorvete diet":
    calorias_sobremesa = 110
elif sobremesa == "Mousse diet":
    calorias_sobremesa = 170
elif sobremesa == "Mousse Chocolate":
    calorias_sobremesa = 200
else:
    calorias_sobremesa = 0

if bebida == "Chá":
    calorias_bebida = 20
elif bebida == "Suco de Laranja":
    calorias_bebida = 70
elif bebida == "Suco de Melão":
    calorias_bebida = 100
elif bebida == "Refrigerante diet":
    calorias_bebida = 65
else:
    calorias_bebida = 0

calorias_total = calorias_prato + calorias_sobremesa + calorias_bebida
print(f"A quantidade total de calorias é: {calorias_total} calorias.")

