```
n = int(input())
sm = float(input())
pc = float(input())
nv = int(input())

salario_minimo = 2 * sm
comissao = (pc * nv) * 0.15
salario_final = salario_minimo + comissao / n
lucro = (pc * nv) * 1.5 - (pc * nv)
print(f"{salario_final:.0f}")
print(f"{lucro:.0f}")

