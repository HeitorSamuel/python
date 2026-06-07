cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m',
}

num = int(input('{}Digite um número inteiro:{} '.format(cores['amarelo'], cores['limpar'])))
print(('{}'+'=' * 5 + ' Tabuada de {} ' + '='*5+'{}').format(cores['ciano'], num, cores['limpar']))
print('{} x {} = {}'.format(num, 0, num*0))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print(('{}'+'='*24+'{}').format(cores['ciano'], cores['limpar']))
