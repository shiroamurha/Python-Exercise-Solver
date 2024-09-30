peso = float(input("Peso de peixes: "))
excesso = peso - 50
if excesso > 0:
    multa = excesso * 4
    print("Excesso: {:.2f} kg".format(excesso))
    print("Multa: R$ {:.2f}".format(multa))
else:
    print("Excesso: 0 kg")
    print("Multa: R$ 0.00")

