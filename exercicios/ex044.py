print('='*11 + ' LOJAS SAMUEL ' + '='*11)
precoComp = int(input('Digite o preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão')
opcPag = int(input('Qual opção você prefere? '))

if opcPag == 1:
    print('O valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format(precoComp, precoComp*0.9))
elif opcPag == 2:
    print('O valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format(precoComp, precoComp*0.95))
elif opcPag == 3:
    print('O valor da sua compra de R${:.2f} vai continuar com o mesmo valor!'.format(precoComp))
elif opcPag == 4:
    print('O valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format(precoComp, precoComp*1.2))