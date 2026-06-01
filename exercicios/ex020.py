from random import shuffle

aluno1 = input('Digite o(a) 1°(ª) aluno(a) a ser sorteado(a): ')
aluno2 = input('Digite o(a) 2°(ª) aluno(a) a ser sorteado(a): ') 
aluno3 = input('Digite o(a) 3°(ª) aluno(a) a ser sorteado(a): ')
aluno4 = input('Digite o(a) 4°(ª) aluno(a) a ser sorteado(a): ')

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print('O(A) 1°(ª) sorteado(a) foi: {}, o(a) 2°(ª) foi: {}, o(a) 3°(ª) foi: {} e o(a) 4°(ª) foi: {}'.format(lista[0], lista[1], lista[2], lista[3]))