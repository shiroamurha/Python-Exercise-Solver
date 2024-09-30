nome = []
idade = []
sexo = []

for i in range(20):
    n = input("Nome: ")
    i = int(input("Idade: "))
    s = input("Sexo (M/F): ")
    nome.append(n)
    idade.append(i)
    sexo.append(s)

for i in range(len(nome)):
    if sexo[i] == "M" and idade[i] > 21:
        print(nome[i])

