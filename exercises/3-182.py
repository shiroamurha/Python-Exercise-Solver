```
cargo = int(input("Cargo: "))
salario = float(input("Salário: "))

if cargo == 101:
    percentual = 0.10
elif cargo == 102:
    percentual = 0.15
elif cargo == 103:
    percentual = 0.20
elif cargo == 104:
    percentual = 0.30
elif cargo == 105:
    percentual = 0.35
elif cargo == 106:
    percentual = 0.40
else:
    percentual = 0.50

novo_salario = salario * (1 + percentual)
diferenca = novo_salario - salario

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print(f"Diferença: R$ {diferenca:.2f}")

print("Deseja digitar novamente os dados? (S/N)")
resposta = input().upper()
while resposta != "S" and resposta != "N":
    print("Opção inválida. Digite S para sim ou N para não.")
    resposta = input().upper()
if resposta == "N":
    print("Fim do programa.")

