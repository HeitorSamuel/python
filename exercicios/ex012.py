cores = {
    'limpar':'\033[m',
    'verde':'\033[4;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[1;34m'
}

preco = float(input('{}Digite o preço do produto:{} R$ '.format(cores['verde'], cores['limpar'])))
print('{}O preço dele com{} {}5% de desconto{} {}é de{} {}R${:.2f}{}'.format(cores['verde'], cores['limpar'], cores['vermelho'], cores['limpar'], cores['verde'], cores['limpar'], cores['azul'], preco*0.95, cores['limpar']))