from random import randint
from time import sleep

numComp = randint(0, 10)
print('-='* 20)
print('Vou pensar em um número entre 0 e 10...')
print('-=' * 20)
numUsuario = int(input('Adivinhe um número que estou pensando entre 0 e 10: '))
print('PROCESSANDO...')
sleep(1)
contPalp = 1

while numComp != numUsuario:
    if numUsuario < numComp:
        print('Mais... Tente mais uma vez!')
        numUsuario = int(input('Digite outro número: '))
    elif numUsuario > numComp:
        print('Menos... Tenta mais uma vez!')
        numUsuario = int(input('Digite outro número: '))
    contPalp += 1
    print('PROCESSANDO...')
    sleep(1)
print('Você ACERTOU! eu pensei no número {} e você no número {}!'.format(numComp, numUsuario))
print('Ao todo foram {} palpite(s) para acertar!'.format(contPalp))
