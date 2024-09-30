```
n = []
for i in range(10):
    num = float(input("Insira o %dº número: "%(i+1)))
    n.append(num)

for i in range(10):
    metade = n[i]/2
    quadrado = n[i]**2
    cubo = n[i]**3
    print("O número %d é: \nMetade: %.2f\nQuadrado: %.2f\nCubo: %.2f"%((i+1), metade, quadrado, cubo))

