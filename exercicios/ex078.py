valores = []

for p in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {p}: ')))
print('=-'*30)
print(f'Você digitou os valores {valores}')

if max(valores) == min(valores):
    print(f'Todos os valores digitados são iguais a {valores[0]}!')
else:
    print(f'O maior valor digitado foi {max(valores)} nas posições', end='')
    for i, v in enumerate(valores):
        if v == max(valores):
            print(f' {i}', end='...')

    print(f'\nO menor valor digitado foi {min(valores)} nas posições', end='')
    for i, v in enumerate(valores):
        if v == min(valores):
            print(f' {i}', end='...')
