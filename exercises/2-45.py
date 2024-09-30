ano1 = int(input())
ano2 = int(input())
ano3 = int(input())

if ano1 == ano2 and ano2 == ano3:
    print("TRIGEMEOS")
elif (ano1 == ano2 and ano1 != ano3) or (ano1 == ano3 and ano1 != ano2) or (ano2 == ano3 and ano2 != ano1):
    print("GEMEOS")
else:
    print("IRMAOS")

