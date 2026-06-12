num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)))
elif opcao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)))
elif opcao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)))