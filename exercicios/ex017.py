from math import sqrt, pow
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hipot = sqrt((pow(co,2) + pow(ca,2)))
print('O valor do Cateto Oposto é {}, do Cateto Adjacente é {} e da hipotenusa é {}'.format(co, ca, hipot))
