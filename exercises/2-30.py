```
idade = int(input("Idade: "))
peso = float(input("Peso: "))
jejum = input("Jejum? ")
documento = input("Documento com foto? ")
hepatite = input("Teve hepatite após os 10 anos? ")
malária = input("Teve malária? ")
sexo = input("Sexo (M/F): ")

if 18 <= idade <= 67 and peso > 50 and jejum.lower() == "sim" and documento.lower() == "sim":
    if hepatite.lower() == "não" and malária.lower() == "não":
        if sexo.upper() == "M":
            if int(input("Dias desde a última doação: ")) < 60:
                print("Pode doar sangue.")
            else:
                print("Não pode doar sangue.")
        elif sexo.upper() == "F":
            if int(input("Dias desde a última doação: ")) < 90:
                print("Pode doar sangue.")
            else:
                print("Não pode doar sangue.")
    else:
        print("Não pode doar sangue.")
else:
    print("Não pode doar sangue.")

