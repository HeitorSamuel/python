nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
media = (nota1+nota2)/2
print('Sua média é {:.1f}!'.format(media))
if media > 6.0:
    print('Parabéns! Você está acima da média!')
elif media == 6.0:
    print('Cuidado! Você está na média!')
else:
    print('Lamentável! Você está abaixo da média!')