from random import randint

numSort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram:', end= ' ')
for c in numSort:  
    print(f'{c}', end=' ')

print(f'\nO maior valor sorteado foi {max(numSort)}')
print(f'O menor valor sorteado foi {min(numSort)}')


