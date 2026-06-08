cores = {
    'limpar':'\033[m',
    'amarelo':'\033[4;33m',
    'verde':'\033[4;32m',
    'vermelho':'\033[31m',
    'azul':'\033[4;34m'
}

from math import sqrt, pow
co = float(input('{}Digite o valor do Cateto Oposto:{} '.format(cores['azul'], cores['limpar'])))
ca = float(input('{}Digite o valor do Cateto Adjacente:{} '.format(cores['amarelo'], cores['limpar'])))
hipot = sqrt((pow(co,2) + pow(ca,2)))
print('{}O valor do Cateto Oposto é{} {}{}{}, {}do Cateto Adjacente é{} {}{}{} {}e da hipotenusa é{} {}{:.2f}{}'.format(cores['vermelho'], cores['limpar'], cores['azul'], co, cores['limpar'], cores['vermelho'], cores['limpar'], cores['amarelo'], ca, cores['limpar'], cores['vermelho'], cores['limpar'], cores['verde'], hipot, cores['limpar']))
