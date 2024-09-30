```
publico = float(input())
popular = publico * 0.1
geral = publico * 0.5
arquibancada = publico * 0.3
cadeiras = publico * 0.1
popular_renda = popular * 1
geral_renda = geral * 5
arquibancada_renda = arquibancada * 10
cadeiras_renda = cadeiras * 20
renda_total = popular_renda + geral_renda + arquibancada_renda + cadeiras_renda
print(f'Renda do jogo: R${renda_total:.2f}')

