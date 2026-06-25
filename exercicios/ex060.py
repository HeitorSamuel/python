numDigit = int(input('Digite um número: '))
fat = 1
num = numDigit
print('A operação de {}! resulta em:'.format(numDigit), end=' ')
while num >= 1:
    if num > 1:
        print('{}'.format(num), end=' x ')
    elif num == 1:
        print('{}'.format(num), end=' = ')
    fat *= num
    num -= 1
print('{} '.format(fat))
