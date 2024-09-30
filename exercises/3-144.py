```
alunos = []
while True:
    notas = []
    for i in range(3):
        nota = float(input("Nota {}: ".format(i+1)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    alunos.append({"notas": notas, "media": media})
    resposta = int(input("Digitar as notas de um novo aluno? 1. Sim 2. Não "))
    if resposta == 2:
        break
aprovados = sum(1 for aluno in alunos if aluno["media"] >= 6)
print("Quantidade de alunos: {}".format(len(alunos)))
print("Quantidade de aprovados: {}".format(aprovados))
```

