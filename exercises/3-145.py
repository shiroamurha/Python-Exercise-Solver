```
alunos = []
while True:
    nome = input("Nome do aluno: ")
    notas = list(map(float, input("Notas do aluno (separadas por espaço): ").split()))
    media = sum(notas) / len(notas)
    alunos.append({"nome": nome, "notas": notas, "media": media})
    continuar = input("Deseja adicionar outro aluno? (S/N): ")
    if continuar.upper() != "S":
        break

aprovados = 0
recuperacao = 0
reprovados = 0
for aluno in alunos:
    if aluno["media"] >= 6:
        aprovados += 1
    elif 3 <= aluno["media"] < 6:
        recuperacao += 1
    else:
        reprovados += 1

print(f"Quantidade de alunos: {len(alunos)}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos em recuperação: {recuperacao}")
print(f"Quantidade de alunos reprovados: {reprovados}")

