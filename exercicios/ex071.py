print('='*40)
print(f'{'BANCO DE GOTHAM':^40}')
print('='*40)

pergValor = int(input('Que valor você quer sacar? R$').strip())

while True:
    
    if ValorRest < 50:
        ValorRest = pergValor - 50
    else:
        break
print(ValorRest)
