from random import choice
from time import sleep

print('='*11 + ' JOGANDO JOKENPÔ ' + '='*11)

usuario = str(input('Escolha entre Pedra, Papel ou Tesoura: ')).strip().upper()
print('-='*22)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*22)

comput = ['pedra', 'papel', 'tesoura']

sorteio = choice(comput).upper()

if (usuario == 'PEDRA' and sorteio == 'PEDRA') or (usuario == 'PAPEL' and sorteio == 'PAPEL') or (usuario == 'TESOURA' and sorteio == 'TESOURA'):
    print('EMPATE! Eu escolhi: {} e você escolheu: {}'.format(sorteio, usuario))
elif (usuario == 'PEDRA' and sorteio == 'TESOURA') or (usuario == 'PAPEL' and sorteio == 'PEDRA') or (usuario == 'TESOURA' and sorteio == 'PAPEL'):
    print('VOCÊ VENCEU! Você escolheu: {} e eu escolhi: {}'.format(usuario, sorteio))
elif (sorteio == 'PEDRA' and usuario == 'TESOURA') or (sorteio == 'PAPEL' and usuario == 'PEDRA') or (sorteio == 'TESOURA' and usuario == 'PAPEL'):
    print('EU VENCI! Eu escolhi: {} e você escolheu: {}'.format(sorteio, usuario))
else:
    print('Carater Inválido! Tente Novamente!')

print('='*17 + ' FIM ' + '='*17)
