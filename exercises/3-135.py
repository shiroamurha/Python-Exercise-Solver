```
notas_aluno = []
for i in range(10):
    notas_aluno_individual = []
    for j in range(5):
        nota = float(input(f"Nota do aluno {i+1} na avaliação {j+1}: "))
        notas_aluno_individual.append(nota)
    media = sum(notas_aluno_individual) / 5
    if media <= 2:
        situacao = "Nota PÉSSIMA"
    elif media <= 4:
        situacao = "Nota MUITO RUIM"
    elif media <= 6:
        situacao = "Nota de quem NÃO ESTUDOU O SUFICIENTE"
    elif media <= 7:
        situacao = "Nota NO LIMITE"
    elif media <= 8:
        situacao = "Nota BOA, pode melhorar"
    elif media <= 9.7:
        situacao = "Nota MUITO BOA!"
    else:
        situacao = "Nota na DISPUTA PELA COXINHA! :)"
    print(f"Média do aluno {i+1}: {media:.2f}\nSituação: {situacao}\n")
```

