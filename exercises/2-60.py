```
alcool = 1.9
gasolina = 2.5

tipo = input("Tipo de combustível (A/G): ")
litros = float(input("Número de litros vendidos: "))

if tipo == "A":
    if litros <= 20:
        valor = litros * alcool
    else:
        valor = 20 * alcool + (litros - 20) * alcool * 0.95
elif tipo == "G":
    if litros <= 20:
        valor = litros * gasolina
    else:
        valor = 20 * gasolina + (litros - 20) * gasolina * 0.94
else:
    print("Erro: tipo de combustível inválido")

print("Valor a ser pago: R$ {:.2f}".format(valor))

