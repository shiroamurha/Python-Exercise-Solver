sexo = input()
cont = 0
while sexo.upper() != 'S':
    if sexo.upper() == 'M':
        cont += 1
    sexo = input()
print(cont)

