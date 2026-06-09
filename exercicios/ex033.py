#números maiores
#Preciso simplificar!

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[1;34m',
    'roxo':'\033[1;35m',
    'ciano':'\033[4;36m'
}

n1 = float(input('{}Digite o 1° número:{} '.format(cores['amarelo'], cores['limpar'])))
n2 = float(input('{}Digite o 2° número:{} '.format(cores['roxo'], cores['limpar'])))
n3 = float(input('{}Digite o 3° número:{} '.format(cores['azul'], cores['limpar'])))

if n1 > n2 > n3:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n3, cores['limpar']))
elif n3 > n2 > n1:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n3, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n1, cores['limpar']))
elif n2 > n1 > n3:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n2,  cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n3, cores['limpar']))
elif n3 > n1 > n2:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n3, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n2, cores['limpar']))
elif n2 > n3 > n1:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n2, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n1, cores['limpar']))
elif n1 > n3 > n2:
    print('{}O maior valor é{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n2, cores['limpar']))
elif n1 == n2 > n3:
    print('{}Os maiores valores são{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n3, cores['limpar']))
elif n3 > n2 == n1:
    print('{}O maior valor é{} {}{}{} {}e os menores valores são{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n3, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n2, cores['limpar']))
elif n1 == n3 > n2:
    print('{}Os maiores valores são{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n2, cores['limpar']))
elif n2 > n1 == n3:
    print('{}O maior valor é{} {}{}{} {}e os menores valores são{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n2, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n1, cores['limpar']))
elif n2 == n3 > n1:
    print('{}Os maiores valores são{} {}{}{} {}e o menor valor é{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n2, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n1, cores['limpar']))
elif n1 > n2 == n3:
    print('{}O maior valor é{} {}{}{} {}e os menores valores são{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar'], cores['ciano'], cores['limpar'], cores['vermelho'], n2, cores['limpar']))
elif n1 == n2 == n3:
    print('{}Os 3 números tem o mesmo valor, sendo ele o{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['verde'], n1, cores['limpar']))