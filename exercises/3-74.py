78:
```
n = []
for i in range(12):
    n.append(int(input()))
cont = 0
for i in n:
    if 30 <= i <= 60:
        cont += 1
print(cont)
```

79:
```
n = []
for i in range(10):
    n.append(int(input()))
cont = 0
for i in n:
    if 10 <= i <= 50 or 100 <= i <= 200 and i % 2 == 0:
        cont += 1
print(cont)
```

