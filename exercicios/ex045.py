from random import choice

print('='*11 + ' JOGANDO JOKENPÔ ' + '='*11)

usuario = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).strip().lower()

comput = ['pedra', 'papel', 'tesoura']

sorteio = choice(comput)

if (usuario == 'pedra' and sorteio == 'pedra') or (usuario == 'papel' and sorteio == 'papel') or (usuario == 'tesoura' and sorteio == 'tesoura'):
    print('EMPATE! Eu escolhi: {} e você escolheu: {}'.format(sorteio, usuario))
elif (usuario == 'pedra' and sorteio == 'tesoura') or (usuario == 'papel' and sorteio == 'pedra') or (usuario == 'tesoura' and sorteio == 'papel'):
    print('VOCÊ VENCEU! Você escolheu: {} e eu escolhi: {}'.format(usuario, sorteio))
elif (sorteio == 'pedra' and usuario == 'tesoura') or (sorteio == 'papel' and usuario == 'pedra') or (sorteio == 'tesoura' and usuario == 'papel'):
    print('EU VENCI! Eu escolhi: {} e você escolheu: {}'.format(sorteio, usuario))

print('='*17 + ' FIM ' + '='*17)
