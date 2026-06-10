nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
media = (nota1+nota2)/2

if media < 5.0:
    print('Sua média vale {:.1f}! Você está REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média vale {:.1f}! Você está de RECUPERAÇÃO!'.format(media))
elif media >= 7.0:
    print('Sua média vale {:.1f}! Você está APROVADO!'.format(media))