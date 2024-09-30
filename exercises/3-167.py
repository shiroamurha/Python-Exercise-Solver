```
idade = 0
soma_idade = 0
total_feminino = 0
total_masculino = 0
total_feminino_35_40 = 0

while True:
    sexo = int(input("Digite o sexo (1-masculino, 2-feminino): "))
    idade = int(input("Digite a idade: "))
    
    if idade == 0:
        break
    
    soma_idade += idade
    
    if sexo == 2:
        total_feminino += 1
        if 35 <= idade <= 40:
            total_feminino_35_40 += 1
    else:
        total_masculino += 1

media_idade = soma_idade / (total_feminino + total_masculino)
print(f"Idade média: {media_idade:.2f}")
print(f"Total de pessoas do sexo feminino com idade entre 35-40 anos: {total_feminino_35_40}")
print(f"Total de pessoas do sexo masculino: {total_masculino}")
```

