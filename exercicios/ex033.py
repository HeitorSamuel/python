#números maiores
#preciso completar
n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))

if n1 > n2 > n3:
    print('O maior valor é {} e o menor valor é {}'.format(n1, n3))
elif n3 > n2 > n1:
    print('O maior valor é {} e o menor valor é {}'.format(n3, n1))
elif n2 > n1 > n3:
    print('O maior valor é {} e o menor valor é {}'.format(n2 , n3))
elif n3 > n1 > n2:
    print('O maior valor é {} e o menor valor é {}'.format(n3, n2))
elif n2 > n3 > n1:
    print('O maior valor é {} e o menor valor é {}'.format(n2, n1))
elif n1 > n3 > n2:
    print('O maior valor é {} e o menor valor é {}'.format(n1, n2))
elif n1 == n2 > n3:
    print('Os maiores valores são {} e o menor valor é {}'.format(n1, n3))
elif n3 > n2 == n1:
    print('O maior valor é {} e os menores valores são {}'.format(n3, n2))
elif n1 == n3 > n2:
    print('Os maiores valores são {} e o menor valor é {}'.format(n1, n2))
elif n2 > n1 == n3:
    print('O maior valor é {} e os menores valores são {}'.format(n2, n1))
elif n2 == n3 > n1:
    print('Os maiores valores são {} e o menor valor é {}'.format(n2, n1))
elif n1 > n2 == n3:
    print('O maior valor é {} e os menores valores são {}'.format(n1, n2))
elif n1 == n2 == n3:
    print('Os 3 números tem o mesmo valor, sendo ele o {}'.format(n1))