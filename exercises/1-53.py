salario = 1200
c1 = 200
c2 = 120
multa_c1 = c1 * 0.02
multa_c2 = c2 * 0.02
total_multas = multa_c1 + multa_c2
total_a_pagar = c1 + c2 + multa_c1 + multa_c2
resto = salario - total_a_pagar
print("Resto do salário: R$%.2f" % resto)

