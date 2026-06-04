vel = int(input('Digite a velocidade do seu carro: '))
if vel > 80:
    print('MULTADO!')
    print('Você excedeu o limite de velocidade! Você vai ter que pagar R${:.2f}!'.format((vel-80)*7))
elif vel == 80:
    print('Você está no limite de velocidade!')
    print('Dirija com Cuidado!')
else:
    print('Você está abaixo do limite de velocidade!')
    print('Mantenha o cuidado!')