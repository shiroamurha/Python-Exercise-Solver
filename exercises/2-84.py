```
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
n5 = float(input("Nota 5: "))

media = (n1 + n2 + n3 + n4 + n5) / 5

if media <= 2:
    print(f"Média: {media:.2f} - Situação: PÉSSIMA")
elif 2 < media <= 4:
    print(f"Média: {media:.2f} - Situação: MUITO RUIM")
elif 4 < media <= 6:
    print(f"Média: {media:.2f} - Situação: de quem NÃO ESTUDOU O SUFICIENTE")
elif 6 < media <= 7:
    print(f"Média: {media:.2f} - Situação: NO LIMITE")
elif 7 < media <= 8:
    print(f"Média: {media:.2f} - Situação: BOA, pode melhorar")
elif 8 < media <= 9.7:
    print(f"Média: {media:.2f} - Situação: MUITO BOA!")
else:
    print(f"Média: {media:.2f} - Situação: na DISPUTA PELA COXINHA!")

