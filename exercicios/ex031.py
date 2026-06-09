cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[4;32m',
    'vermelho':'\033[1;37;41m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

kmRod = float(input('{}Digite a distância da sua viagem:{} '.format(cores['verde'], cores['limpar'])))
if kmRod <= 200:
    print('{}Você vai fazer uma viagem de{} {}{}Km.{} \n{}O valor da sua passagem é{} {}R${:.2f}!{}'.format(cores['ciano'], cores['limpar'], cores['roxo'], kmRod, cores['limpar'], cores['amarelo'], cores['limpar'], cores['vermelho'], kmRod*0.5, cores['limpar']))
else:
    print('{}Você vai fazer uma viagem de{} {}{}Km.{} \n{}O valor da sua passagem é{} {}R${:.2f}!{}'.format(cores['ciano'], cores['limpar'], cores['roxo'], kmRod, cores['limpar'], cores['amarelo'], cores['limpar'], cores['vermelho'], kmRod*0.45, cores['limpar']))