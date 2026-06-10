peso = float(input('Digite o seu peso em kilogramas(Kg): '))
altura = float(input('Digite a sua altura em metros(m): '))
imc = altura/(peso**2)

if imc < 18.5:
    print('O seu imc é {}! Você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('O seu imc é {}! Você está no PESO IDEAL!'.format(imc))
elif imc > 25 and imc <= 30:
    print('O seu imc é {}! Você está com SOBREPESO!'.format(imc))
elif imc > 30 and imc <= 40:
    print('O seu imc é {}! Você está com OBESIDADE'.format(imc))
elif imc > 40:
    print('O seu imc é {}! Você está COM OBESIDADE MÓRBIDA!'.format(imc))
