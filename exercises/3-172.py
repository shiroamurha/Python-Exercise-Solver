```
turmas = []
for _ in range(int(input("Quantas turmas? "))):
    alunos = []
    for _ in range(int(input("Quantos alunos na turma? "))):
        nota = float(input("Nota do aluno: "))
        alunos.append(nota)
    turmas.append(alunos)

for i, turma in enumerate(turmas):
    aprovados = sum(1 for nota in turma if nota >= 7.0)
    media = sum(turma) / len(turma)
    reprovados = len(turma) - aprovados
    print(f"Turma {i+1}:")
    print(f"Aprovados: {aprovados}")
    print(f"Média: {media:.2f}")
    print(f"Reprovados: {reprovados} ({(reprovados / len(turma) * 100):.2f}%)")
```

