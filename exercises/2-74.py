salario_por_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

if horas_trabalhadas > 40:
    horas_extras = horas_trabalhadas - 40
    salario_bruto = (40 * salario_por_hora) + (horas_extras * salario_por_hora * 2)
else:
    salario_bruto = horas_trabalhadas * salario_por_hora

print("O salário bruto é: R$", salario_bruto)

