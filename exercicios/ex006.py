cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'vermelho':'\033[31m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

num = int(input('{}Digite um número{}: '.format(cores['amarelo'], cores['limpar'])))
print('O seu {}dobro{} é {}, \no seu {}triplo{} é {} e \na sua {}raiz quadrada{} é {:.2f}'.format(cores['ciano'], cores['limpar'], num*2, cores['roxo'], cores['limpar'], num*3, cores['vermelho'], cores['limpar'], num**(1/2)))