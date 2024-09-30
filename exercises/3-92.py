```
nota = int(input("Nota: "))
nome = input("Nome: ")
idade = int(input("Idade: "))

if 1 <= nota <= 10:
    if idade > 40 and nota == 10:
        print("Pessoas com idade superior a 40 anos que atribuíram nota 10: ", pessoas40)
    else:
        print("Nota válida, mas não atendeu ao critério")
else:
    print("Nota inválida")
```

