```
salario = float(input())
codigo = int(input())

if codigo == 1:
    bicho = salario * 2.1
    classe = 'Excelente'
elif codigo == 2:
    bicho = salario * 1.8
    classe = 'Bom'
elif codigo == 3:
    bicho = salario * 1.5
    classe = 'Médio'
elif codigo == 4:
    bicho = salario * 1.3
    classe = 'Regular'
elif codigo == 5:
    bicho = salario * 1.1
    classe = 'Precisa treinar mais'
elif codigo == 6:
    bicho = salario * 1.05
    classe = 'Te cuida'
elif codigo == 7:
    bicho = 0
    classe = 'Passe no Departamento Pessoal'

salario_final = salario + bicho
print(f'Salário final: R$ {salario_final:.2f}')
print(f'Classe: {classe}')
```

