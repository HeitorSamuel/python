cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[35m'
}

num = int(input('{}Digite um número inteiro:{} '.format(cores['amarelo'], cores['limpar'])))
print(('{}'+'=' * 5 + ' Tabuada de {} ' + '='*5+'{}').format(cores['ciano'], num, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 0, cores['limpar'], cores['vermelho'], num*0, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 1, cores['limpar'], cores['vermelho'], num*1, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 2, cores['limpar'], cores['vermelho'], num*2, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 3, cores['limpar'], cores['vermelho'], num*3, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 4, cores['limpar'], cores['vermelho'], num*4, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 5, cores['limpar'], cores['vermelho'], num*5, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 6, cores['limpar'], cores['vermelho'], num*6, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 7, cores['limpar'], cores['vermelho'], num*7, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 8, cores['limpar'], cores['vermelho'], num*8, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 9, cores['limpar'], cores['vermelho'], num*9, cores['limpar']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['azul'], num, cores['limpar'], cores['verde'], 10, cores['limpar'], cores['vermelho'], num*10, cores['limpar']))
print(('{}'+'='*24+'{}').format(cores['ciano'], cores['limpar']))
