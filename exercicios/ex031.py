kmRod = float(input('Digite a distância da sua viagem: '))
if kmRod <= 200:
    print('Você vai fazer uma viagem de {}Km. \nO valor da sua passagem é R${:.2f}!'.format(kmRod, kmRod*0.5))
else:
    print('Você vai fazer uma viagem de {}Km. \nO valor da sua passagem é R${:.2f}!'.format(kmRod, kmRod*0.45))