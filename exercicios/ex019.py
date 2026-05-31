import random

nome1 = input('Digite o nome do(a) 1°(ª) aluno(a): ')
nome2 = input('Digite o nome do(a) 2°(ª) aluno(a): ')
nome3 = input('Digite o nome do(a) 3°(ª) aluno(a): ')
nome4 = input('Digite o nome do(a) 4°(ª) aluno(a): ')
lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)
print('O(A) aluno(a) sorteado(a) para apagar o quadro é: {}'.format(sorteio))