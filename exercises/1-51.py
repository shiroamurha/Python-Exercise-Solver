salario_fixo = float(input("Salário fixo: "))
vendas = float(input("Valor de vendas: "))
comissao = (vendas * 0.04)
salario_final = salario_fixo + comissao

print("Comissão: R$ {:.2f}".format(comissao))
print("Salário final: R$ {:.2f}".format(salario_final))

