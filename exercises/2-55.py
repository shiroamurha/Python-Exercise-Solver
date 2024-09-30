nome = input("Digite o seu nome: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media < 6.0:
    print(f"{nome}, Reprovado, faltou estudo!!!")
elif 6.1 <= media <= 6.9:
    print(f"{nome}, Recuperação, pode melhorar")
elif 7.0 <= media <= 8.0:
    print(f"{nome}, Aprovado, mas não ganha coxinha")
elif 8.1 <= media <= 9.7:
    print(f"{nome}, Aprovado!")
else:
    print(f"{nome}, Aprovado, levando a coxinha no final do semestre:-)")

