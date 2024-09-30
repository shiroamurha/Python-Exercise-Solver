```
alunos = []
while True:
    renda_pessoal = float(input("Renda pessoal: "))
    if renda_pessoal == 0:
        break
    renda_familiar = float(input("Renda familiar: "))
    gasto_alimentacao = float(input("Gasto com alimentação: "))
    gasto_outras_despesas = float(input("Gasto com outras despesas: "))
    alunos.append((renda_pessoal, renda_familiar, gasto_alimentacao, gasto_outras_despesas))

acima_200 = 0
renda_pessoal_maior = 0
gasto_alimentacao_total = 0
gasto_outras_despesas_total = 0
for aluno in alunos:
    renda_pessoal, renda_familiar, gasto_alimentacao, gasto_outras_despesas = aluno
    gasto_alimentacao_total += gasto_alimentacao
    gasto_outras_despesas_total += gasto_outras_despesas
    if gasto_outras_despesas > 200:
        acima_200 += 1
    if renda_pessoal > renda_familiar:
        renda_pessoal_maior += 1

porcentagem_acima_200 = (acima_200 / len(alunos)) * 100
porcentagem_gasto_alimentacao = (gasto_alimentacao_total / (gasto_alimentacao_total + gasto_outras_despesas_total)) * 100
porcentagem_gasto_outras_despesas = (gasto_outras_despesas_total / (gasto_alimentacao_total + gasto_outras_despesas_total)) * 100
print(f"Porcentagem de alunos que gastam mais de R$200,00 com outras despesas: {porcentagem_acima_200}%")
print(f"Numero de alunos com renda pessoal maior que a renda familiar: {renda_pessoal_maior}")
print(f"Porcentagem gasta com alimentação: {porcentagem_gasto_alimentacao}%")
print(f"Porcentagem gasta com outras despesas: {porcentagem_gasto_outras_despesas}%")

