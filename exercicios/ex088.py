from random import randint
from time import sleep
print('-'*30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-'*30)

quantJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantJogos} JOGOS -=-=-=')
for j in range(0, quantJogos):
    jogos = []
    for numeros in range(1, 7):
        geradorNum = randint(1, 60)
        jogos.append(geradorNum)
    print(f'Jogo {j+1}: {sorted(jogos)}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)