```
def questao182():
    while True:
        num = int(input())
        if num < 1000 or num > 9999:
            break
        resto = num % 100
        if num // 100 + resto == num:
            print("Sim")
        else:
            print("Nao")

def questao183():
    num = int(input())
    i = 0
    while num > 0:
        num -= i * 2 + 1
        i += 1
    print(i)
```

