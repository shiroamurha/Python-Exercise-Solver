```
idades = []
for i in range(5):
    idade = float(input(f"Idade do aluno {i+1}: "))
    idades.append(idade)

media_idade = sum(idades) / len(idades)

if media_idade < 25:
    print("Turma Jovem")
    for idade in idades:
        print(f"Idade do aluno: {idade}")
elif 25 <= media_idade <= 40:
    print("Turma Adulta")
    print(f"Média de idade: {media_idade}")
else:
    print("Turma Idosa")
    print(f"Média de idade: {media_idade}")
    for idade in idades:
        print(f"Idade do aluno: {idade}")
```

