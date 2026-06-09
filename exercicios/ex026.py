cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[4;34m',
    'roxo':'\033[1;35m'
}

frase = str(input('{}Digite uma frase:{} '.format(cores['amarelo'], cores['limpar']))).strip()
print('{}A letra A aparece{} {}{} vezes{}.'.format(cores['azul'], cores['limpar'], cores['vermelho'], frase.lower().count('a'), cores['limpar']))
print('{}A letra A aparece primeiramente na posição{} {}{}{}.'.format(cores['azul'], cores['limpar'], cores['verde'], frase.lower().find('a')+1, cores['limpar']))
print('{}A letra A aparece pela última vez na posição{} {}{}{}.'.format(cores['azul'], cores['limpar'], cores['roxo'], frase.lower().rfind('a')+1, cores['limpar']))