velocidade = float(input("Insira a velocidade do veículo: "))
if velocidade > 80:
    multa = 360
elif velocidade > 60:
    multa = 180
else:
    multa = 0
print(f"A multa é de R${multa:.2f}")

