dia = int(input('Quantos dias o seu carro ficou alugado? '))
kmPerc = int(input('Quantos km você percorreu com o carro alugado? '))
diaCalc = 60 * dia
kmCalc = 0.15 * kmPerc
print('O preço total a pagar pelo aluguel do carro é de: R${:.0f},00'.format(diaCalc+kmCalc))