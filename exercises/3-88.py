```
import math

while True:
    r = float(input("Insira o raio do círculo: "))
    if r == 0:
        print("A área é zero")
        print("ByeBye")
        break
    else:
        area = math.pi * (r ** 2)
        print("A área do círculo é:", area)

