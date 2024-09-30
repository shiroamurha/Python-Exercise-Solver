```
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1 + n2 + n3) / 3

if media < 7:
    print("Aluno ficou em recuperação")
    recuperacao = float(input("Nota de recuperacao: "))
    nova_media = (media * 0.6) + (recuperacao * 0.4)
    print("Nova media final: ", nova_media)
else:
    print("Aluno passou")

