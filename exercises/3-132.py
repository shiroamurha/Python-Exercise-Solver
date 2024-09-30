```
notas = []
soma = 0
for i in range(20):
    aluno = []
    for j in range(5):
        nota = float(input(f"Nota do aluno {i+1}, {j+1}ª: "))
        aluno.append(nota)
        soma += nota
    notas.append(aluno)

media_aluno = soma / (20 * 5)
media_turma = soma / (20 * 5)

acima_media = 0
alunos_acima_media = 0
for aluno in notas:
    media = sum(aluno) / 5
    if media >= 5:
        acima_media += 1
    if media > media_turma:
        alunos_acima_media += 1

print(f"a) Média de cada aluno: {notas}")
print(f"b) Média da turma: {media_turma}")
print(f"c) Percentual de alunos com média >= 5: {(acima_media / 20) * 100}%")
print(f"d) Quantos alunos tiveram média maior que a média da turma: {alunos_acima_media}")
```

