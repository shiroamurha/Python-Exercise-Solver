```
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
jejum = input("Você está em jejum? (S/N): ")

if 18 <= idade <= 67 and peso > 50 and jejum.upper() == "S":
    print("Você pode doar sangue.")
else:
    print("Você não pode doar sangue.")
```

