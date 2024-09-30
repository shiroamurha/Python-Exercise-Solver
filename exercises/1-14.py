```
hora = float(input("Quantos você ganha por hora? "))
horas = float(input("Quantas horas você trabalha por mês? "))
salario_bruto = hora * horas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR (11%): R$ {imposto_renda:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

