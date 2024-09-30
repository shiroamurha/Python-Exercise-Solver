```
matricula = []
nome = []
sexo = []
salario_bruto = []
num_dependentes = []
ano_nascimento = []
ano_ingresso = []

while True:
    m = int(input("Matrícula: "))
    n = input("Nome: ")
    s = input("Sexo (M/F): ")
    sb = float(input("Salário bruto: "))
    nd = int(input("Número de dependentes: "))
    an = int(input("Ano de nascimento: "))
    ai = int(input("Ano de ingresso na empresa: "))
    matricula.append(m)
    nome.append(n)
    sexo.append(s)
    salario_bruto.append(sb)
    num_dependentes.append(nd)
    ano_nascimento.append(an)
    ano_ingresso.append(ai)
    r = input("Deseja continuar? (S/N): ")
    if r.upper() != "S":
        break

nome_anc = nome[0]
salario_liquido = [0] * len(matricula)
for i in range(len(matricula)):
    salario_bruto_i = salario_bruto[i]
    desconto_inss = salario_bruto_i * 0.12
    salario_bruto_i -= desconto_inss
    if salario_bruto_i <= 1500:
        desconto_ir = 0
    elif salario_bruto_i <= 2700:
        desconto_ir = salario_bruto_i * 0.15
    elif salario_bruto_i <= 4700:
        desconto_ir = salario_bruto_i * 0.275
    else:
        desconto_ir = salario_bruto_i * 0.35
    salario_liquido_i = salario_bruto_i - desconto_ir
    for j in range(num_dependentes[i]):
        salario_liquido_i += 14
    salario_liquido[i] = salario_liquido_i

nome_antigo = nome[0]
for i in range(len(matricula)):
    if ano_ingresso[i] < ano_ingresso[int(nome_antigo.find(nome[0]))]:
        nome_antigo = nome[i]

nome_maior_salario = nome[0]
salario_maior = salario_liquido[0]
for i in range(len(matricula)):
    if salario_liquido[i] > salario_maior:
        nome_maior_salario = nome[i]
        salario_maior = salario_liquido[i]

percentual_homem_jovem = 0
for i in range(len(matricula)):
    if sexo[i] == "M" and ano_nascimento[i] < 1985 and salario_bruto[i] < 1700:
        percentual_homem_jovem += 1

percentual_funcionarias_maiores_3_dependentes = 0
for i in range(len(matricula)):
    if sexo[i] == "F" and num_dependentes[i] > 3:
        percentual_funcionarias_maiores_3_dependentes += 1

soma_salarios_liquidos = sum(salario_liquido)
percentual_funcionarios = len(matricula) / (len(matricula) + len(female))

print(f"a) {nome_antigo}")
print(f"b) {nome_maior_salario}")
print(f"c) {percentual_homem_jovem / len(matricula) * 100}%")
print(f"d) {salario_maior}")
print(f"e) {soma_salarios_liquidos}")
print(f"f) {percentual_funcionarias_maiores_3_dependentes / len(sexo) * 100}%")
```

