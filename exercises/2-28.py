```
idade = int(input("Idade: "))
peso = float(input("Peso: "))
jejun = input("Esteve em jejum? (sim/nao): ")
doc_foto = input("Tem documento com foto? (sim/nao): ")
hepatite = input("Teve hepatite após os 10 anos? (sim/nao): ")

if 18 <= idade <= 67 and peso > 50 and jejun.lower() == "sim" and doc_foto.lower() == "sim":
    if hepatite.lower() == "nao":
        print("Pode doar sangue")
    else:
        print("Não pode doar sangue")
else:
    print("Não pode doar sangue")

