from random import randint
from time import sleep
numPens = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('-=-' * 20)
numAdv = int(input('Adivinhe o número que estou pensando entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if numAdv == numPens:
    print('Você venceu! Eu pensei no n° {} e você no n° {}!'.format(numPens, numAdv))
else:
    print('Eu ganhei! Eu pensei no n° {} e você no n° {}'.format(numPens, numAdv))
print('-'*10 + 'FIM' + '-'*10)