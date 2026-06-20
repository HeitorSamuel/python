print('='*50)
print('{:^50}'.format('Os 10 primeiros termos de uma PA' ))
print('='*50)

termoAtual = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('='*50)
print('{}'.format('Os 10 primeiros termos da PA são: ' ))

for c in range(1, 11):
    print(termoAtual, end=' → ')
    termoAtual += razao
print('FIM')