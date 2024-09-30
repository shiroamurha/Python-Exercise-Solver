```
conta = float(input())
amigos = int(input())
if conta < 300:
    joao = conta * 0.8
    amigo = (conta * 0.2) / amigos
elif conta < 600:
    joao = conta / 2
    amigo = (conta - joao) / amigos
else:
    joao = conta / (amigos + 1)
    amigo = (conta - joao) / amigos
print(f"João pagará R${joao:.2f}")
print(f"Seu amigo pagará R${amigo:.2f}")

