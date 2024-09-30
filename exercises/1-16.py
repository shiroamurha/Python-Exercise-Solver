```
import math

metro_quadrado = float(input("Tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = math.ceil(metro_quadrado / 6)

latas_necessarias = math.ceil(litros_necessarios / 18)
galoes_necessarios = math.ceil(litros_necessarios / 3.6)

preco_latas = latas_necessarias * 80
preco_galoes = galoes_necessarios * 25

if preco_latas < preco_galoes:
    print("Comprar apenas latas de 18 litros: {} latas a R$ {:.2f}".format(latas_necessarias, preco_latas))
elif preco_galoes < preco_latas:
    print("Comprar apenas galões de 3,6 litros: {} galões a R$ {:.2f}".format(galoes_necessarios, preco_galoes))
else:
    print("Misturar latas e galões: {} latas a R$ {:.2f} + {} galões a R$ {:.2f} = R$ {:.2f}".format(latas_necessarias - (litros_necessarios % 18) // 3.6, 80 * (latas_necessarias - (litros_necessarios % 18) // 3.6), (litros_necessarios % 18) // 3.6, 25 * ((litros_necessarios % 18) // 3.6), preco_latas + preco_galoes))
```

