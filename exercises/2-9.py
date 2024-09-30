n1 = int(input())
n2 = int(input())
n3 = int(input())

negativos = 0

if n1 < 0:
    negativos += 1
if n2 < 0:
    negativos += 1
if n3 < 0:
    negativos += 1

print(f"{negativos} valores são negativos")

