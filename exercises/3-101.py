```
n = int(input())
t1 = 0
t2 = 1
print(t1, t2, end=' ')
for i in range(2, n):
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3

n = 0
while True:
    num = float(input())
    if num < 0:
        break
    if 0 <= num <= 25.9:
        n += 1
    elif 26 <= num <= 50.9:
        n += 1
    elif 51 <= num <= 75.9:
        n += 1
    elif 76 <= num <= 100:
        n += 1
print(n)

