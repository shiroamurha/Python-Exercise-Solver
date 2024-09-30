alunos = []

while True:
    nome = input("Nome do aluno: ")
    if nome == "sair":
        break
    notas = list(map(float, input("Notas (separadas por vírgula): ").split(',')))
    alunos.append({"nome": nome, "notas": notas})

media = sum(sum(aluno["notas"])/len(aluno["notas"]) for aluno in alunos) / len(alunos)

print("Média das notas:", media)

