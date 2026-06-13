peso = float(input('Digite o seu peso em kilogramas(Kg): '))
altura = float(input('Digite a sua altura em metros(m): '))
imc = peso/(altura**2)

if imc < 18.5:
    print('O seu IMC é {:.1f}! Você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é {:.1f}! Você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é {:.1f}! Você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc < 40:
    print('O seu IMC é {:.1f}! Você está com OBESIDADE'.format(imc))
elif imc >= 40:
    print('O seu IMC é {:.1f}! Você está COM OBESIDADE MÓRBIDA!'.format(imc))
