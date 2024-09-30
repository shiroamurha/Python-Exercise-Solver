p = 1

for i in range(92, 1479):
    if i % 5 == 0 or i % 7 == 0:
        p *= i

print(p)

