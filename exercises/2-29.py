```
idade = int(input("Insira sua idade: "))
peso = float(input("Insira seu peso: "))
documentofoto = input("Possui documento com foto? (s/n): ")
hepatite = input("Já teve hepatite? (s/n): ")
malaria = input("Já teve malária? (s/n): ")

if 18 <= idade <= 67 and peso > 50 and documentofoto.lower() == "s":
    if hepatite.lower() != "s" or malaria.lower() != "s":
        print("Pode doar sangue.")
    else:
        print("Não pode doar sangue.")
else:
    print("Não pode doar sangue.")

