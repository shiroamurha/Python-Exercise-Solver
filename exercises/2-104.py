```
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))

print("Quadrados dos números pares e cubos dos números ímpares:")
if n1 % 2 == 0:
    print(f"{n1}² = {n1**2}")
else:
    print(f"{n1}³ = {n1**3}")
if n2 % 2 == 0:
    print(f"{n2}² = {n2**2}")
else:
    print(f"{n2}³ = {n2**3}")
if n3 % 2 == 0:
    print(f"{n3}² = {n3**2}")
else:
    print(f"{n3}³ = {n3**3}")
if n4 % 2 == 0:
    print(f"{n4}² = {n4**2}")
else:
    print(f"{n4}³ = {n4**3}")
if n5 % 2 == 0:
    print(f"{n5}² = {n5**2}")
else:
    print(f"{n5}³ = {n5**3}")

