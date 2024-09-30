```
capital = 'Brasília'
tentativas = 0

while tentativas < 3:
    resposta = input('Qual a capital do Brasil? ')
    if resposta.lower() == capital.lower():
        print('Parabéns! Brasília é a capital do Brasil e é conhecida como a cidade-gêmea.')
        break
    else:
        tentativas += 1
        print('Tente novamente!')
        if tentativas == 1:
            print('Dica: Brasília é a capital do Brasil e está localizada no Planalto Central.')
        elif tentativas == 2:
            print('Dica: Brasília é a capital do Brasil e é conhecida por seus monumentos e arquitetura moderna.')
if tentativas == 3:
    print('Você errou as 3 tentativas. A resposta certa era Brasília.')
```

