```
valor_carro = float(input("Insira o valor do carro: "))

preco_final = valor_carro * 0.8

print("Preço final à vista: R$ {:.2f}".format(preco_final))

parcelas = [6, 12, 18, 24, 36, 48, 60]
percentual_acrescimo = [0.03, 0.06, 0.09, 0.12, 0.18, 0.24, 0.30]

for i in range(len(parcelas)):
    valor_parcela = (preco_final * (1 + percentual_acrescimo[i])) / parcelas[i]
    print("Parcelas: {}x R$ {:.2f}".format(parcelas[i], valor_parcela))

