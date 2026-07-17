print('{:=^50}'.format(' Digite 4 números '))

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))

numTotal = (n1, n2, n3, n4)

print(f'Você digitou os valores {numTotal}')
print(f'O número 9 apareceu {numTotal.count(9)} veze(s)')
if 3 in numTotal:
    print(f'O número 3 apareceu na {numTotal.index(3)+1}ª posição')
else:
    print(f'O número 3 não foi encontrado em nenuma posição')
print(f'O(s) valor(es) par(es) digitado(s) foram', end=' ')
for c in numTotal:
    if c % 2 == 0:
        print(c, end=' ')
