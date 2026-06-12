nota1 = float(input('Digite a sua 1ª nota: '))
nota2 = float(input('Digite a sua 2ª nota: '))
media = (nota1+nota2)/2

if media < 5:
    print('Com as notas {} e {} a sua média vale {:.1f}! Você está REPROVADO!'.format(nota1, nota2, media))
elif media >= 5 and media <= 6.9:
    print('Com as notas {} e {} a sua média vale {:.1f}! Você está de RECUPERAÇÃO!'.format(nota1, nota2, media))
elif media >= 7:
    print('Com as notas {} e {} a sua média vale {:.1f}! Você está APROVADO!'.format(nota1, nota2, media))