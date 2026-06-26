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
    ultimoTerm = termoAtual - razao
    cont += 1

print('''

Você quer mostrar mais algum termo?
      
[0] NÃO
[1] SIM    
''')
opcao = int(input('Digite a sua opção: '))

while opcao == 1:
    termo = int(input('Quantos termos você quer? '))
    cont += termo
    while termo > 0:
        ultimoTerm += razao
        print(ultimoTerm, end=' ')
        termo -= 1
    print('''

Você quer mostrar mais algum termo?
          
[0] NÃO
[1] SIM    
    ''')
    opcao = int(input('Digite a sua opção: '))

print('FIM DO PROGRAMA!')
print('Ao todo foram {} termos digitados!'.format(cont))
        