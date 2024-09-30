```
while True:
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
        print("Nota inválida")
    else:
        media = (nota1 + nota2) / 2
        print(f"{nota1} (nota 1) {nota2} (nota 2) {media} (média)")
    resposta = int(input("Novo cálculo?(1.sim 2.não)? "))
    if resposta != 1:
        break

