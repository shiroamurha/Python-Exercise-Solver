```
import math

raio = float(input("Insira o raio do círculo: "))

perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print("Perímetro: {:.2f}".format(perimetro))
print("Área: {:.2f}".format(area))

