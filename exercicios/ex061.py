print('='*40)
print('{:^40}'.format(' Os 10 primeiros termos de uma PA '))
print('='*40)

termoAtual = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('='*40)
cont = 0
print('Os 10 primeiros termos dessa PA são:', end=' ')
while cont < 10:
    print(termoAtual, end=' ')
    termoAtual += razao
    cont += 1