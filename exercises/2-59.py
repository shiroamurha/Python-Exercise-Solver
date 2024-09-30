```
p1 = input("Você esteve no local do crime? ")
p2 = input("Você tem conhecimento sobre o crime? ")
p3 = input("Você tem um histórico de crimes anteriores? ")
p4 = input("Você tem um motivo para cometer o crime? ")
p5 = input("Você tem um alibi para o tempo do crime? ")

if p1 == "SIM" and p2 == "SIM":
    print("Suspeita")
elif p1 == "SIM" or p2 == "SIM" or p3 == "SIM" or p4 == "SIM":
    print("Cúmplice")
elif p1 == "SIM" and p2 == "SIM" and p3 == "SIM" and p4 == "SIM" and p5 == "SIM":
    print("Assassino")
else:
    print("Inocente")

