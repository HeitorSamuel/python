print('='*40)
print('{:^40}'.format(' Os 10 primeiros termos de uma PA '))
print('='*40)

termoAtual = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('='*40)
cont = 0
ultimoTerm = 0
print('Os 10 primeiros termos dessa PA são:', end=' ')
while cont < 10:
    print(termoAtual, end=' ')
    termoAtual += razao
    ultimoTerm += termoAtual
    cont += 1
print('''

Você quer mostrar mais algum termo?
[0] NÃO
[1] SIM    
''')
opcao = int(input('Digite a sua opção: '))

while opcao != 0:
    termo = int(input('Quantos termos você quer? '))
    termoCont = termo
    while termoCont > 0:
        ultimoTerm += razao
        print(ultimoTerm)
        termoCont -= 1
    print('Os {} termos a mais dessa PA são esses acima!'.format(termo))
    if termoCont == 0:
        print('FIM DO PROGRAMA')

print('FIM DO PROGRAMA')

        