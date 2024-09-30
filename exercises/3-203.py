```
sexo_feminino = 0
idade_total = 0
for _ in range(int(input())):
    sexo = input()
    olhos = input()
    cabelos = input()
    idade = int(input())
    idade_total += idade
    if sexo == 'fem' and olhos == 'verdes' and cabelos == 'louros' and 18 <= idade <= 35:
        sexo_feminino += 1
max_idade = max(idade_total)
porcentagem = (sexo_feminino / (_ + 1)) * 100
print(f'Maior idade: {max_idade}')
print(f'Porcentagem de individuos do sexo feminino: {porcentagem:.2f}%')
```

