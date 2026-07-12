numExten = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

numInt = int(input('Digite um número entre 0 e 20: '))
while numInt < 0 and numInt > 20:
    numInt = int(input('Tente Novamente! Digite um número entre 0 e 20: '))

for c in range(0, len(numExten)):
    if c