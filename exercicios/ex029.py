cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[7;32;40m',
    'vermelho':'\033[7;31m',
    'azul':'\033[34m',
    'roxo':'\033[4;35m',
    'ciano':'\033[7;36m'
}

vel = int(input('{}Digite a velocidade do seu carro:{} '.format(cores['azul'], cores['limpar'])))
if vel > 80:
    print('{}MULTADO!{} {}Você excedeu o limite de velocidade que é de{} {}80Km/h!{} \n{}Você vai ter que pagar{} {}R${:.2f}!{}'.format(cores['vermelho'], cores['limpar'], cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar'], cores['amarelo'], cores['limpar'], cores['vermelho'], (vel-80)*7, cores['limpar']))
elif vel == 80:
    print('{}Você está no limite de velocidade que é de{} {}80Km/h!{}'.format(cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar']))
    print('{}Dirija com Cuidado!{}'.format(cores['verde'], cores['limpar']))
else:
    print('{}Você está abaixo do limite de velocidade que é de{} {}80Km/h!{}'.format(cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar']))
    print('{}Mantenha o cuidado!{}'.format(cores['ciano'], cores['limpar']))