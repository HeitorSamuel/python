from random import randint
from time import sleep

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

numPens = randint(0, 5)
print(('{}' + '-=-' * 20 + '{}').format(cores['ciano'], cores['limpar']))
print('{}Vou pensar em um número entre 0 e 5...{}'.format(cores['amarelo'], cores['limpar']))
print(('{}' + '-=-' * 20 + '{}').format(cores['ciano'], cores['limpar']))
numAdv = int(input('{}Adivinhe o número que estou pensando entre 0 e 5:{} '.format(cores['roxo'], cores['limpar'])))
print('{}PROCESSANDO...{}'.format(cores['azul'], cores['limpar']))
sleep(3)
if numAdv == numPens:
    print('{}Você venceu!{} {}Eu pensei no n°{} {}{}{} e você no n° {}{}{}!'.format(cores['verde'], cores['limpar'], cores['roxo'], cores['limpar'], cores['verde'], numPens, cores['limpar'], cores['verde'], numAdv, cores['limpar']))
else:
    print('{}Você perdeu!{} {}Eu pensei no n°{} {}{}{} e você no n° {}{}{}!'.format(cores['vermelho'], cores['limpar'], cores['roxo'], cores['limpar'], cores['vermelho'], numPens, cores['limpar'], cores['verde'], numAdv, cores['limpar']))
print(('{}' + '-'*10 + 'FIM' + '-'*10 + '{}').format(cores['azul'], cores['limpar']))