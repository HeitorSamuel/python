cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[1;32m',
    'azul':'\033[1;34m',
    'roxo':'\033[35m',
}

salario = float(input('{}Digite o valor do seu salário:{} R$'.format(cores['amarelo'], cores['limpar'])))
print('{}O valor do seu salário com{} {}15% de aumento{} {}é de{} {}R${:.0f},00{}'.format(cores['roxo'], cores['limpar'], cores['verde'], cores['limpar'], cores['roxo'], cores['limpar'], cores['azul'], salario*1.15, cores['limpar']))