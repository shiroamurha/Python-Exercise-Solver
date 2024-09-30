nome = input("Qual é o seu nome? ")
turno = input("Qual é o seu turno de estudo? M - manhã, T - tarde, N - noite ").upper()

if turno == 'M':
    print(f"Bom dia, {nome}!")
elif turno == 'T':
    print(f"Boa tarde, {nome}!")
elif turno == 'N':
    print(f"Boa noite, {nome}!")
else:
    print("Valor Inválido!")

