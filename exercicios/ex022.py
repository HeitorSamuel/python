cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'roxo':'\033[4;35m',
    'ciano':'\033[1;36m'
}

nome = str(input('{}Digite o seu nome completo:{} '.format(cores['roxo'], cores['limpar']))).strip()

print('O seu nome completo com letras maiúsculas é: {}{}{}'.format(cores['verde'], nome.upper(), cores['limpar']))

print('O seu nome completo com letras minúsculas é: {}{}{}'.format(cores['amarelo'], nome.lower(), cores['limpar']))

print('O seu nome completo possui {}{}{} letras.'.format(cores['ciano'], len(nome.replace(' ', '')), cores['limpar']))

print('O seu 1° nome possui {}{}{} letras.'.format(cores['vermelho'], len(nome.split()[0]), cores['limpar']))
