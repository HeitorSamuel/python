cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m'
}

nota1 = float(input('Digite a sua {}1ª nota{}: '.format(cores['azul'], cores['limpar'])))
nota2 = float(input('Digite a sua {}2ª nota{}: '.format(cores['amarelo'], cores['limpar'])))
print('A sua {}média{} é {}{:.1f}{}'.format(cores['vermelho'], cores['limpar'], cores['verde'], (nota1+nota2)/2, cores['limpar']))