cores = {
    'limpar':'\033[m',
    'amarelo':'\033[4;33m',
    'verde':'\033[4;32m',
    'vermelho':'\033[7;31;47m',
    'azul':'\033[4;34m',
    'roxo':'\033[4;35m',
    'ciano':'\033[1;36m'
}

num = int(input('{}Digite um número entre 0 e 9999:{} '.format(cores['vermelho'], cores['limpar'])))

print('{}Unidade:{} {}{}{}'.format(cores['azul'], cores['limpar'], cores['ciano'], num%10, cores['limpar']))
print('{}Dezena:{} {}{}{}'.format(cores['amarelo'], cores['limpar'], cores['ciano'], (num//10)%10, cores['limpar']))
print('{}Centena:{} {}{}{}'.format(cores['verde'], cores['limpar'], cores['ciano'], (num//100)%10, cores['limpar']))
print('{}Milhar:{} {}{}{}'.format(cores['roxo'], cores['limpar'], cores['ciano'], num//1000, cores['limpar']))
