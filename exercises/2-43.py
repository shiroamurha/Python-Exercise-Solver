```
from datetime import datetime

nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
dia, mes, ano = map(int, nascimento.split('/'))
nascimento = datetime(ano, mes, dia)

ano_referencia = 2026
idade = ano_referencia - nascimento.year

if (nascimento.month, nascimento.day) > (1, 1):
    idade += 1

print(f"A idade que você terá em 01/01/2026 é {idade} anos.")
```

