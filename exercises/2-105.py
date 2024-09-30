```
nome = input()
idade = int(input())
grupo_risco = int(input())

if idade < 17 or idade > 70:
    print(f"{nome} não pode adquirir seguro pois sua idade não está na faixa necessária.")
else:
    if idade <= 20:
        categoria = 1 if grupo_risco == 1 else 2 if grupo_risco == 2 else 3
    elif idade <= 24:
        categoria = 2 if grupo_risco == 1 else 3 if grupo_risco == 2 else 4
    elif idade <= 34:
        categoria = 3 if grupo_risco == 1 else 4 if grupo_risco == 2 else 5
    elif idade <= 64:
        categoria = 4 if grupo_risco == 1 else 5 if grupo_risco == 2 else 6
    else:
        categoria = 7 if grupo_risco == 1 else 8 if grupo_risco == 2 else 9

    print(f"{nome} tem {idade} anos e é do grupo de risco {grupo_risco}, portanto, sua categoria é {categoria}.")

