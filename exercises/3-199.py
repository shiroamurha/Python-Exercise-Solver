```
salario_minimo = float(input())
salario_bruto = 0
salario_liquido = 0
gratificacao = 0

while True:
    horas_trabalhadas = float(input())
    if horas_trabalhadas == -1:
        break
    dependentes = int(input())
    horas_extras = float(input())

    valor_hora = salario_minimo / 10
    salario_mes = horas_trabalhadas * valor_hora
    acréscimo_dependente = dependentes * 32
    acréscimo_hora_extra = horas_extras * valor_hora * 1.5
    salario_bruto = salario_mes + acréscimo_dependente + acréscimo_hora_extra

    if salario_bruto <= 900:
        irrf = salario_bruto * 0.1
    elif salario_bruto <= 1500:
        irrf = salario_bruto * 0.2
    else:
        irrf = salario_bruto * 0.3

    salario_liquido = salario_bruto - irrf

    if salario_liquido <= 900:
        gratificacao = 100
    else:
        gratificacao = 50

    salario_receber = salario_liquido + gratificacao

    print(f"Salário a receber: R${salario_receber:.2f}")
```

