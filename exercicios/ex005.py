cores = {
    'limpar':'\033[m',
    'azul':'\033[34m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'amarelo':'\033[33m'
}

num = int(input('{}Digite um número inteiro{}: '.format(cores['amarelo'], cores['limpar'])))

print('O número {}{}{} possui o antecessor valendo {}{}{} e o sucessor valendo {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['vermelho'], num-1, cores['limpar'], cores['verde'], num+1, cores['limpar']))