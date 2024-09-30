```
def acesso_permitido(hora, tipo_usuario):
    if tipo_usuario == 'Funcionário':
        if (0 <= int(hora[:2]) < 7 or 18 <= int(hora[:2]) < 24) and (0 <= int(hora[3:]) < 60):
            return True
        elif 12 <= int(hora[:2]) < 14 and 0 <= int(hora[3:]) < 30:
            return True
    return False

hora = input('Insira a hora (HH:MM): ')
tipo_usuario = input('Insira o tipo de usuário: ')

if acesso_permitido(hora, tipo_usuario):
    print('Acesso permitido.')
else:
    print('Acesso não permitido.')
```

