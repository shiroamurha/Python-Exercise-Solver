salario = float(input("Digite o salário bruto: "))
prestacao = float(input("Digite o valor da prestação: "))

if prestacao <= salario * 0.3:
    print("O empréstimo pode ser concedido.")
else:
    print("O empréstimo não pode ser concedido.")

