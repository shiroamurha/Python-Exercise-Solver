```
idades = []
sexos = []
salarios = []

while True:
    idade = int(input("Idade: "))
    if idade < 0:
        break
    sexo = int(input("Sexo (1. Feminino 2. Masculino): "))
    salario = float(input("Salário: "))
    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)

media_salario = sum(salarios) / len(salarios)
maior_idade = max(idades)
menor_idade = min(idades)
maior_salario = max(salarios)
maior_salario_feminino = max([salario for sexo, salario in zip(sexos, salarios) if sexo == 1 and salario > 0])
menor_idade_masculino = min([idade for sexo, idade in zip(sexos, idades) if sexo == 2])
femininas_acima_500 = len([salario for sexo, salario in zip(sexos, salarios) if sexo == 1 and salario > 500])
masculinos_entre_15_50 = len([idade for sexo, idade in zip(sexos, idades) if sexo == 2 and 15 <= idade <= 50])
idade_e_salario_acima_1000 = len([salario for sexo, idade, salario in zip(sexos, idades, salarios) if idade >= 18 and idade <= 65 and salario > 1000])

print("a) Média de salário: ", media_salario)
print("b) Maior idade: ", maior_idade)
print("c) Menor idade: ", menor_idade)
print("d) Maior salário: ", maior_salario)
print("e) Maior salário feminino: ", maior_salario_feminino)
print("f) Menor idade masculino: ", menor_idade_masculino)
print("g) Quantas pessoas do sexo feminino possuem salário maior R$500: ", femininas_acima_500)
print("h) Quantos habitantes são do sexo masculino e tem idade entre 15 e 50 anos: ", masculinos_entre_15_50)
print("i) Quantos habitantes tem idade entre 18 e 65 anos e possuem salário acima de R$1000: ", idade_e_salario_acima_1000)

