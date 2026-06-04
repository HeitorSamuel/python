from random import randint
numAdv = int(input('Adivinhe o número que estou pensando entre 0 e 5: '))
numPens = randint(0, 5)
if numAdv == numPens:
    print('Você venceu! Eu pensei no n° {} e você no n° {}!'.format(numPens, numAdv))
else:
    print('Você perdeu! Eu pensei no n° {} e você no n° {}'.format(numPens, numAdv))
print('-'*10 + 'FIM' + '-'*10)