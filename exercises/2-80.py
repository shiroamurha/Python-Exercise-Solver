nome = input("Nome: ")
mes_nascimento = int(input("Mês de nascimento: "))
ano_nascimento = int(input("Ano de nascimento: "))

if mes_nascimento >= 1 and mes_nascimento <= 12:
    if ano_nascimento % 4 == 0 and (ano_nascimento % 100 != 0 or ano_nascimento % 400 == 0):
        if mes_nascimento > 6:
            print(f"{nome}, você não pode votar este ano.")
        else:
            print(f"{nome}, você pode votar este ano.")
    else:
        if mes_nascimento > 6:
            print(f"{nome}, você pode votar este ano.")
        else:
            print(f"{nome}, você não pode votar este ano.")
else:
    print("Mês de nascimento inválido.")

