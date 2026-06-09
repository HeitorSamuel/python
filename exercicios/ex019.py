from random import choice

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[1;33m',
    'verde':'\033[1;32m',
    'vermelho':'\033[1;31m',
    'azul':'\033[1;34m',
    'roxo':'\033[1;35m',
    'ciano':'\033[4;36m'
}

nome1 = input('{}Digite o nome do(a) 1°(ª) aluno(a):{} '.format(cores['amarelo'], cores['limpar']))
nome2 = input('{}Digite o nome do(a) 2°(ª) aluno(a):{} '.format(cores['azul'], cores['limpar']))
nome3 = input('{}Digite o nome do(a) 3°(ª) aluno(a):{} '.format(cores['verde'], cores['limpar']))
nome4 = input('{}Digite o nome do(a) 4°(ª) aluno(a):{} '.format(cores['vermelho'], cores['limpar']))
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print('{}O(A) aluno(a) sorteado(a) para apagar o quadro é:{} {}{}{}'.format(cores['ciano'], cores['limpar'], cores['roxo'], sorteio, cores['limpar']))