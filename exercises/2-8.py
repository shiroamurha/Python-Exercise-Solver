par = 0
impar = 0

valor1 = int(input())
if valor1 % 2 == 0:
    par += 1
else:
    impar += 1

valor2 = int(input())
if valor2 % 2 == 0:
    par += 1
else:
    impar += 1

valor3 = int(input())
if valor3 % 2 == 0:
    par += 1
else:
    impar += 1

print(f"Pares: {par}")
print(f"Ímpares: {impar}")

