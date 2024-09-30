```
alunos = []
for i in range(int(input("Quantos alunos foram entrevistados? "))):
    aluno = {}
    aluno['nome'] = input("Nome do aluno: ")
    aluno['uso_xerox'] = int(input("Quantas vezes o aluno usou o xerox? "))
    alunos.append(aluno)

total_usuarios = len([aluno for aluno in alunos if aluno['uso_xerox'] > 0])
print(f"a) Total de alunos que fizeram uso do xerox: {total_usuarios}")

menos_5 = len([aluno for aluno in alunos if aluno['uso_xerox'] <= 5])
print(f"b) Percentual de alunos que utilizaram menos de 5 vezes: {(menos_5 / total_usuarios) * 100}%")

entre_5_e_10 = len([aluno for aluno in alunos if 5 < aluno['uso_xerox'] <= 10])
print(f"c) Percentual de alunos que utilizaram entre 5 e 10 vezes: {(entre_5_e_10 / total_usuarios) * 100}%")

mais_10 = len([aluno for aluno in alunos if aluno['uso_xerox'] > 10])
print(f"d) Percentual de alunos que utilizaram mais de 10 vezes: {(mais_10 / total_usuarios) * 100}%")

print(f"e) Quantidade de vezes que os alunos utilizaram: {sum(aluno['uso_xerox'] for aluno in alunos)}")

media = sum(aluno['uso_xerox'] for aluno in alunos) / total_usuarios
print(f"g) A média de utilização: {media}")

print(f"g) A maior e a menor quantidade utilizada no mês: {max(aluno['uso_xerox'] for aluno in alunos)}, {min(aluno['uso_xerox'] for aluno in alunos)}")
```

