```
for i in range(1, 21):
    divisores = [j for j in range(1, i+1) if i % j == 0]
    print(f"{i}: {divisores}")
```

