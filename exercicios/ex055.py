maior = 0
menor = 0

for r in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(r)))
    if r == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('-='*22)
print('O maior peso é {}Kg e o menor peso é {}Kg'.format(maior, menor))
print('-='*22)
        