```
import math

x1 = float(input("Insira a coordenada x do primeiro ponto: "))
y1 = float(input("Insira a coordenada y do primeiro ponto: "))
x2 = float(input("Insira a coordenada x do segundo ponto: "))
y2 = float(input("Insira a coordenada y do segundo ponto: "))

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("A distância entre os pontos é: ", d)

