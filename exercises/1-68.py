kW = float(input("Quantidade de quilowatts gasta por uma residência: "))
sm = float(input("Valor do salário mínimo: "))
valor_kW = sm / 7
valor_pago = kW * valor_kW
desconto = valor_pago * 0.1
novo_valor_pago = valor_pago - desconto

print(f"O valor em reais de cada quilowatts é: R$ {valor_kW:.2f}")
print(f"O valor a ser pago é: R$ {valor_pago:.2f}")
print(f"O novo valor a ser pago com desconto de 10% é: R$ {novo_valor_pago:.2f}")

