frase = str(input('Digite qualquer frase: ')).strip().upper().replace(' ', '')

fraseComprim = len(frase)-1

fraseInvert = ''

for i in range(fraseComprim, -1, -1):
    fraseInvert += (frase[i])

if fraseInvert == frase:
    print('Esta frase é um PALÍNDROMO! As frases {} e {} são iguais!'.format(frase, fraseInvert))
else:
    print('Esta frase não é um PALÍNDROMO! As frases {} e {} são diferentes!'.format(frase, fraseInvert))