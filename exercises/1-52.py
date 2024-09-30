ano = 365
mes = 30

idade_dias = int(input("Digite a idade em dias: "))
anos = idade_dias // (ano * 12)
idade_dias %= (ano * 12)
meses = idade_dias // mes
dia = idade_dias % mes

print(f"A idade é {anos} anos, {meses} meses e {dia} dias.")

