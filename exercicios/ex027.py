cores = {
    'limpar':'\033[m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[4;34m',
    'roxo':'\033[7;35;47m'
}

nomecomp = str(input('{}Digite o seu nome completo:{} '.format(cores['roxo'], cores['limpar']))).strip()
print('{}O seu primerio nome é:{} {}{}{}.'.format(cores['azul'], cores['limpar'], cores['verde'], nomecomp.split()[0], cores['limpar']))
print('{}O seu último nome é:{} {}{}{}.'.format(cores['azul'], cores['limpar'], cores['vermelho'], nomecomp.split()[-1], cores['limpar']))