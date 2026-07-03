s = cont = 0

for c in range(1, 7):
    num = int(input('Digite o {}° número inteiro: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('Você digitou {} números PARES e a soma deles é {}!'.format(cont, s))