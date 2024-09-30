```
alunos = {
    'Joao': [85, 90, 95, 88, 92],
    'Maria': [78, 82, 88, 90, 92],
    'Pedro': [92, 95, 98, 96, 95],
    'Ana': [88, 90, 92, 94, 96],
    'Luiz': [90, 92, 95, 98, 99]
}

aprovados_todas = [aluno for aluno, notas in alunos.items() if all(i >= 80 for i in notas)]
aprovados_14 = [aluno for aluno, notas in alunos.items() if notas[0] >= 80 and notas[3] >= 80]
aprovados_3 = [aluno for aluno, notas in alunos.items() if notas[2] >= 80]

aprovados = sum(1 for aluno in alunos.values() if all(i >= 80 for i in aluno)) / len(alunos)
print(f"a) {aprovados_todas}")
print(f"b) {aprovados_14}")
print(f"c) {aprovados * 100}%")
```

