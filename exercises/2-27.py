```
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
jejum = input("Você está em jejum? (s/n): ")
documento = input("Você tem documento com foto? (s/n): ")

if 18 <= idade <= 67 and peso > 50 and jejum.lower() == 's' and documento.lower() == 's':
    print("Você pode doar sangue.")
else:
    print("Você não pode doar sangue.")

