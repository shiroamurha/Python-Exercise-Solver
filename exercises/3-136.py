```
n1 = [[], [], [], [], []]
n2 = [[], [], [], [], []]
n3 = [[], [], [], [], []]
media_alunos = []
media_geral = 0

for i in range(5):
    for j in range(3):
        n1[i].append(float(input(f"Nota {j+1} do aluno {i+1}: ")))
        n2[i].append(float(input(f"Nota {j+1} do aluno {i+1}: ")))
        n3[i].append(float(input(f"Nota {j+1} do aluno {i+1}: ")))

for i in range(5):
    media_aluno = (n1[i][0] + n1[i][1] + n1[i][2]) / 3
    media_alunos.append(media_aluno)

media_geral = sum(media_alunos) / 5

for i in range(5):
    if media_alunos[i] >= 9:
        conceito = 'A'
    elif 7.5 <= media_alunos[i] < 9:
        conceito = 'B'
    elif 6.0 <= media_alunos[i] < 7.5:
        conceito = 'C'
    elif 4.0 <= media_alunos[i] < 6.0:
        conceito = 'D'
    else:
        conceito = 'E'

    print(f"Aluno {i+1} média: {media_alunos[i]:.1f}, conceito: {conceito}")

print(f"Média geral: {media_geral:.1f}, conceito: {conceito}")
if media_geral >= 9:
    print("Turma: A")
elif 7.5 <= media_geral < 9:
    print("Turma: B")
elif 6.0 <= media_geral < 7.5:
    print("Turma: C")
elif 4.0 <= media_geral < 6.0:
    print("Turma: D")
else:
    print("Turma: E")
```

