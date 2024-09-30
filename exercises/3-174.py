```
n = int(input())
aprovados = 0
reprovados = 0
exame = 0
aprovados_maior_8 = 0
soma_notas = 0
maior_nota = 0
for i in range(n):
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2) / 2
    if media >= 6:
        aprovados += 1
        if media > 8:
            aprovados_maior_8 += 1
        soma_notas += media
    elif media < 4:
        reprovados += 1
    else:
        exame += 1
    if nota1 > maior_nota:
        maior_nota = nota1
    if nota2 > maior_nota:
        maior_nota = nota2
per_reprovados = (reprovados / n) * 100
media_aprovados = soma_notas / aprovados
print(f"a) {aprovados}")
print(f"b) {reprovados}")
print(f"c) {exame}")
print(f"d) {media_aprovados:.2f}")
print(f"e) {per_reprovados:.2f}%")
print(f"f) {maior_nota}")
print(f"g) {aprovados_maior_8}")

