from math import trunc

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[4;31m',
    'ciano':'\033[36m'
}

num = float(input('{}Digite um número real:{} '.format(cores['vermelho'], cores['limpar'])))
inteiro = trunc(num)
print('{}O número{} {}{}{} {}tem a parte inteira igual a{} {}{}{}.'.format(cores['ciano'], cores['limpar'], cores['amarelo'], num, cores['limpar'], cores['ciano'], cores['limpar'], cores['verde'], inteiro, cores['limpar']))