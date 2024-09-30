```
n = int(input("Digite o número de alunos por turma: "))
turmas = []
for _ in range(5):
    turma = []
    for _ in range(n):
        nome, nota = input("Nome e nota do aluno: ").split(), float(input("Nota do aluno: "))
        turma.append((nome, nota))
    turmas.append(turma)

for i, turma in enumerate(turmas, 1):
    alunos = [aluno for aluno in turma if aluno[1] > 7]
    print(f"Turma {i}: {len(alunos)} alunos com média superior a 7")
print("Média geral da escola:", sum(sum(aluno[1] for aluno in turma) for turma in turmas) / sum(len(turma) for turma in turmas))

