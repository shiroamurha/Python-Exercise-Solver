massa = 1
while massa >= 0.1:
    massa *= 0.75
    print(f"Tempo necessário: {int(30 * math.log(massa/1) / math.log(0.75))} segundos")

