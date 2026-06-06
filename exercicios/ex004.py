cores = {
    'limpar':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

item = input('Digite algum caracter: ')

print('O seu {}tipo primitivo{} é {}!'.format(cores['verde'], cores['limpar'], type(item)))
print('Só {}tem espaços?{} {}'.format(cores['amarelo'], cores['limpar'], item.isspace()))
print('É {}um número?{} {}'.format(cores['vermelho'], cores['limpar'], item.isnumeric()))
print('É {}alfabético?{} {}'.format(cores['ciano'], cores['limpar'], item.isalpha()))
print('É {}alfanumérico?{} {}'.format(cores['roxo'], cores['limpar'], item.isalnum()))
print('Está {}em maiúsculas?{} {}'.format(cores['amarelo'], cores['limpar'], item.isupper()))
print('Está {}em minúsculas?{} {}'.format(cores['vermelho'], cores['limpar'], item.islower()))
print('Está {}capitalizada?{} {}'.format(cores['verde'], cores['limpar'], item.istitle()))