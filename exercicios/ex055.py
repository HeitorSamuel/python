maior = 0
menor = 0

for r in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    if r == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < maior:
            menor = peso
        