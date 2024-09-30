```
n = []
for i in range(10):
    x = int(input("Digite um valor: "))
    n.append(x)

for x in n:
    print("Valor:", x)
    print("Antecessor:", x-1)
    print("Sucessor:", x+1)
    print()

