print('{:=^40}'.format(' LOJAS SAMUEL '))
precoComp = int(input('Digite o preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista no dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcPag = int(input('Qual opção você prefere? '))

if opcPag == 1:
    print('O valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format(precoComp, precoComp*0.9))
elif opcPag == 2:
    print('O valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format(precoComp, precoComp*0.95))
elif opcPag == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS. \nO valor da sua compra de R${:.2f} vai continuar com o mesmo valor!'.format(precoComp/2,  precoComp))
elif opcPag == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas < 3:
        print('Digite um valor válido! Tente novamente!')
    else:
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS \nO valor da sua compra de R${:.2f} vai passar a custar R${:.2f}!'.format((parcelas),(precoComp*1.2/parcelas), (precoComp), (precoComp*1.2)))
else:
    print('Opção INVÁLIDA de pagamento! Tente Novamente!')