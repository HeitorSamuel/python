print('='*40)
print('{:^40}'.format(' SEQUÊNCIA DE FIBONACCI '))
print('='*40)

termo = int(input('Quantos termos você quer? '))
a = 0
b = 1

while termo > 0:
    print(a, end=' → ')
    b = b + a
    a = b - a
    termo -= 1
print('FIM')