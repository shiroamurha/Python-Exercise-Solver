```
def questao159():
    pop_a = 5000000
    pop_b = 7000000
    taxa_a = 0.03
    taxa_b = 0.02
    anos = 0
    while pop_a < pop_b:
        pop_a += pop_a * taxa_a
        pop_b += pop_b * taxa_b
        anos += 1
    print(anos)

def questao160():
    altura_chico = 1.5
    altura_juca = 1.1
    crescimento_chico = 0.02
    crescimento_juca = 0.03
    anos = 0
    while altura_juca < altura_chico:
        altura_chico += crescimento_chico
        altura_juca += crescimento_juca
        anos += 1
    print(anos)

questao159()
questao160()
```

