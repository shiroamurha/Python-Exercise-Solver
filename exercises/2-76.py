```
mes = int(input("Insira o mês: "))
dia = int(input("Insira o dia: "))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    print("Áries")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("Peixes")
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print("Peixes")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("Touro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("Gêmeos")
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    print("Câncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print("Leão")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print("Virgem")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print("Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Escorpião")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Sagitariano")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print("Capricórnio")

