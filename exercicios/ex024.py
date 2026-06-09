cores = {
    'limpar':'\033[m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[7;34;47m'
}

cidade = str(input('{}Digite a cidade em que você nasceu:{} '.format(cores['azul'], cores['limpar']))).strip()
if cidade[:5].lower() == 'santo':
    print('{}{}{}'.format(cores['verde'], cidade[:5].lower() == 'santo', cores['limpar']))
else:    print('{}{}{}'.format(cores['vermelho'], cidade[:5].lower() == 'santo', cores['limpar']))