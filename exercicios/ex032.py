#ano bissexto
from datetime import date

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[4;34m',
    'roxo':'\033[1;35m',
    'ciano':'\033[36m'
}

ano = int(input('{}Qual ano você quer consultar?{} {}Digite{} {}0{} {}para ver o ano atual.{} '.format(cores['ciano'], cores['limpar'], cores['amarelo'], cores['limpar'], cores['roxo'], cores['limpar'], cores['amarelo'], cores['limpar'])))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 != 00:
        print('{}O ano{} {}{}{} {}é bissexto!{}'.format(cores['verde'], cores['limpar'], cores['azul'], ano, cores['limpar'], cores['verde'], cores['limpar']))
    else:
        if ano % 400 == 0:
            print('{}O ano{} {}{}{} {}é bissexto!{}'.format(cores['verde'], cores['limpar'], cores['azul'], ano, cores['limpar'], cores['verde'], cores['limpar']))  
        else:
            print('{}O ano{} {}{}{} {}não é bissexto!{}'.format(cores['vermelho'], cores['limpar'], cores['azul'], ano, cores['limpar'], cores['vermelho'], cores['limpar'])) 
else:
    print('{}O ano{} {}{}{} {}não é bissexto!{}'.format(cores['vermelho'], cores['limpar'], cores['azul'], ano, cores['limpar'], cores['vermelho'], cores['limpar']))
