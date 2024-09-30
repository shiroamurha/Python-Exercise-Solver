```
altura = float(input())
peso = float(input())

if altura < 1.75:
    print("RECUSADO POR ALTURA")
elif altura > 1.90:
    print("RECUSADO POR ALTURA")
elif peso < 70:
    print("RECUSADO POR PESO")
elif peso > 80:
    print("RECUSADO POR PESO")
else:
    print("ACEITO")

