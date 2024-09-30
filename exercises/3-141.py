```
elevador1 = {'E1': {'matutino': 0, 'vespertino': 0, 'noturno': 0}, 'E2': {'matutino': 0, 'vespertino': 0, 'noturno': 0}, 'E3': {'matutino': 0, 'vespertino': 0, 'noturno': 0}}
for i in range(100):
    morador = input().split()
    elevador = morador[0]
    periodo = morador[1]
    elevador1[elevador][periodo] += 1

elevadorMaisFrequentado = max(elevador1, key=lambda x: sum(elevador1[x].values()))
periodoMaisFrequentado = max((k for k, v in elevador1[elevadorMaisFrequentado].items()), key=elevador1[elevadorMaisFrequentado].get)

periodoMaisUtilizado = max((k for k in elevador1.keys()), key=lambda x: sum(elevador1[x].values()))

media = sum(sum(v.values()) for v in elevador1.values()) / 300

print(f'a) O elevador mais frequentado é o {elevadorMaisFrequentado}')
print(f'b) O elevador mais frequentado é o {elevadorMaisFrequentado} e o período mais frequentado é {periodoMaisFrequentado}')
print(f'c) O período mais utilizado dos elevadores é {periodoMaisUtilizado}')
print(f'd) A média de utilização dos elevadores é {media:.2f}')
```

