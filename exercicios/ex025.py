cores = {
    'limpar':'\033[m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'roxo':'\033[4;35m'
}

nome = str(input('{}Digite o seu nome completo:{} '.format(cores['roxo'], cores['limpar']))).strip().lower()
if ('Silva').lower() in nome:
    print('{}{}{}'.format(cores['verde'], ('Silva').lower() in nome, cores['limpar']))
else:
    print('{}{}{}'.format(cores['vermelho'], ('Silva').lower() in nome, cores['limpar']))
