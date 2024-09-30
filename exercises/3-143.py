```
matriculas = []
notas_finais = []
aprovados = 0
reprovados = 0
total_reprovados = 0
total_superior_9 = 0
percentual_reprovados = 0

for i in range(20):
    matricula = int(input("Matrícula: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    frequencia = int(input("Frequência: "))

    media = (nota1 + nota2 + nota3) / 3
    if media >= 6 and frequencia >= 20:
        aprovados += 1
        msg = "aprovado"
    else:
        reprovados += 1
        msg = "reprovado"

    matriculas.append(matricula)
    notas_finais.append(media)

    if media > 9:
        total_superior_9 += 1

    if frequencia < 20:
        total_reprovados += 1

maior_nota = max(notas_finais)
menor_nota = min(notas_finais)

percentual_reprovados = (total_reprovados / 20) * 100

print("Matrícula\tNota Final\tMensagem")
for i in range(20):
    print(f"{matriculas[i]}\t{notas_finais[i]:.2f}\t{msg}")

print(f"Maior nota final: {maior_nota:.2f}")
print(f"Menor nota final: {menor_nota:.2f}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Total de alunos com nota final superior a 9: {total_superior_9}")
print(f"Percentual de alunos reprovados por frequência abaixo da mínimo necessária: {percentual_reprovados:.2f}%")

