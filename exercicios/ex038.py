n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

if n1 > n2:
    print('O 1° valor é MAIOR! O n° {} é maior que o n° {}!'.format(n1, n2))
elif n2 > n1:
    print('O 2° valor é Maior! O n° {} é maior que o n° {}!'.format(n2, n1))
elif n1 == n2:
    print('NÃO EXISTE valor Maior! Ambos são iguais a {}!'.format(n1))