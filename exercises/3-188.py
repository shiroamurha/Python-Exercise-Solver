```
alunos = []
for _ in range(int(input("Quantidade de alunos: "))):
    nome = input("Nome do aluno: ")
    notas = [int(input(f"Nota da matéria {i+1}: ")) for i in range(5)]
    alunos.append((nome, notas))

aprovados_todas = []
aprovados_14 = []
aprovados_3 = 0

for aluno in alunos:
    nome, notas = aluno
    if all(i >= 6 for i in notas):
        aprovados_todas.append(nome)
    if (notas[0] >= 6 and notas[3] >= 6) and not all(i >= 6 for i in notas):
        aprovados_14.append(nome)
    if notas[2] >= 6:
        aprovados_3 += 1

print("Alunos aprovados em todas as matérias:", aprovados_todas)
print("Alunos aprovados somente nas matérias 1 e 4:", aprovados_14)
print(f"Porcentagem de aprovados na matéria 3: {(aprovados_3 / len(alunos)) * 100}%")

