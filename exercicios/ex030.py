cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[1;32m',
    'roxo':'\033[4;35m',
    'ciano':'\033[1;36m'
}

num = int(input('{}Digite um número:{} '.format(cores['ciano'], cores['limpar'])))
if num % 2 == 0:
    print('{}O número{} {}{}{} {}é{} {}PAR!{}'.format(cores['roxo'], cores['limpar'], cores['amarelo'], num, cores['limpar'], cores['roxo'], cores['limpar'], cores['vermelho'], cores['limpar']))
else:
    print('{}O número{} {}{}{} {}é{} {}ÍMPAR!{}'.format(cores['roxo'], cores['limpar'], cores['amarelo'], num, cores['limpar'], cores['roxo'], cores['limpar'], cores['verde'], cores['limpar']))