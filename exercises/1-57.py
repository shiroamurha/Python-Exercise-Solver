```
n_eleitores = int(input())
n_votos_brancos = int(input())
n_votos_nulos = int(input())
n_votos_validos = int(input())

porcentagem_brancos = (n_votos_brancos / n_eleitores) * 100
porcentagem_nulos = (n_votos_nulos / n_eleitores) * 100
porcentagem_validos = (n_votos_validos / n_eleitores) * 100

print(int(porcentagem_brancos))
print(int(porcentagem_nulos))
print(int(porcentagem_validos))
```

