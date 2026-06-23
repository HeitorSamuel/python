from random import randint
from time import sleep

numComp = randint(0, 10)
print('-='* 20)
print('Vou pensar em um número entre 0 e 10...')
print('-=' * 20)
numUsuario = int(input('Adivinhe um número que estou pensando entre 0 e 10: '))
print('PROCESSANDO...')
sleep(1.5)
contPalp = 1

while numComp != numUsuario:
    numUsuario = int(input('Você ERROU! Tente Novamente! '))
    print('PROCESSANDO...')
    sleep(1.5)
    contPalp += 1
print('Você ACERTOU! eu pensei no n° {} e você no n° {}!'.format(numComp, numUsuario))
print('Ao todo foram {} palpites para acertar!'.format(contPalp))
