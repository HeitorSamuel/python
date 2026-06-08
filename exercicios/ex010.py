cores = {
    'limpar':'\033[m',
    'amarelo':'\033[4;33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[1;34m'
}

dinh = float(input('{}Digite quantos reais você tem na carteira:{} R$'.format(cores['amarelo'], cores['limpar'])))
print('Você tem {}R${}{}, o valor dessa quantia em dólares é de {}US${:.2f}{}, \no valor dessa qauntia em euros é de {}€{:.2f}{}'.format(cores['verde'], dinh, cores['limpar'], cores['azul'], dinh/5.06, cores['limpar'], cores['vermelho'], dinh/5.90, cores['limpar']))