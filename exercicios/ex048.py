s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print('A SOMA DOS NÚMEROS ímpares que são primos e são múltiplos de 3 e que estão ente 1 e 500 é: {}'.format(s))