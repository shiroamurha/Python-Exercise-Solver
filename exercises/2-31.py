ano_atual = int(input("Ano atual: "))
ano_nascimento = int(input("Ano de nascimento: "))

if ano_nascimento < 0:
    print("Ano de nascimento inválido")
else:
    idade = ano_atual - ano_nascimento
    print("Idade: ", idade)

