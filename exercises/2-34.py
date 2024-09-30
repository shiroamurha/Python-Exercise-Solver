ddi = {
    1: "Estados Unidos",
    49: "Alemanha",
    55: "Brasil"
}

mesada = float(input("Digite o valor da mesada: "))
gastos = []

for i in range(5):
    gasto = float(input(f"Digite o valor do gasto {i+1}: "))
    gastos.append(gasto)

if sum(gastos) <= mesada:
    print("Você terá mesada para todos os gastos.")
else:
    print("Você ficará sem condições de gastar.")

