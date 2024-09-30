custo_fabrica = float(input())
impostos = (custo_fabrica * 45) / 100
custo_consumidor = custo_fabrica + impostos + (custo_fabrica * 28) / 100
print(custo_consumidor)

