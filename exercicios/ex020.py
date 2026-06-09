from random import shuffle

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[1;35m'
}

aluno1 = input('{}Digite o(a) 1°(ª) aluno(a) a ser sorteado(a):{} '.format(cores['amarelo'], cores['limpar']))
aluno2 = input('{}Digite o(a) 2°(ª) aluno(a) a ser sorteado(a):{} '.format(cores['verde'], cores['limpar'])) 
aluno3 = input('{}Digite o(a) 3°(ª) aluno(a) a ser sorteado(a):{} '.format(cores['vermelho'], cores['limpar']))
aluno4 = input('{}Digite o(a) 4°(ª) aluno(a) a ser sorteado(a):{} '.format(cores['azul'], cores['limpar']))

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print('{}O(A) 1°(ª) sorteado(a) foi:{} {}{}{}, {}o(a) 2°(ª) foi:{} {}{}{}, {}o(a) 3°(ª) foi:{} {}{}{} {}e o(a) 4°(ª) foi:{} {}{}{}'.format(cores['amarelo'], cores['limpar'], cores['roxo'], lista[0], cores['limpar'], cores['verde'], cores['limpar'], cores['roxo'], lista[1], cores['limpar'], cores['vermelho'], cores['limpar'], cores['roxo'], lista[2], cores['limpar'], cores['azul'], cores['limpar'], cores['roxo'], lista[3], cores['limpar']))