```
a = int(input())
b = int(input())
while a > b:
    a = int(input())
print(*range(a, b+1), sep=' ')

