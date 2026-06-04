kmRod = float(input('Digite a distância da sua viagem: '))
if kmRod <= 200:
    print('O valor da sua passagem é R${:.2f}!'.format(kmRod*0.5))
else:
    print('O valor da sua passagem é R${:.2f}!'.format(kmRod*0.45))