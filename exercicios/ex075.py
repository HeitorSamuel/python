print('{:=^50}'.format(' Digite 4 números '))



n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))


numTotal = (n1, n2, n3, n4)
print(f'Você digitou os valores {numTotal}')
print(f'O número 9 apareceu {numTotal.count(9)} veze(s)')
print(f'O número 3 apareceu na {numTotal.index(3)+1}ª posição')
print(numTotal[0])