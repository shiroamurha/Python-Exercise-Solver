lata = float(input("Quantas latas de 350ml foram compradas? "))
garrafa600 = float(input("Quantas garrafas de 600ml foram compradas? "))
garrafa2000 = float(input("Quantas garrafas de 2 litros foram compradas? "))

litros_lata = lata * 0.35
litros_garrafa600 = garrafa600 * 0.6
litros_garrafa2000 = garrafa2000 * 2

total_litros = litros_lata + litros_garrafa600 + litros_garrafa2000

print("O comerciante comprou {} litros de refrigerante.".format(total_litros))

