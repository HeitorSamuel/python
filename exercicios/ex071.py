print('='*40)
print(f'{'BANCO DE GOTHAM':^40}')
print('='*40)
quant50 = quant20 = quant10 = quant1 = 0
pergValor = int(input('Que valor você quer sacar? R$').strip())
total = pergValor
while True:
    if total >= 50:
        total -= 50
        quant50 += 1
    elif total >= 20:
        total -= 20
        quant20 += 1
    elif total >= 10:
        total -= 10
        quant10 += 1
    elif total >= 1:
        total -= 1
        quant1 += 1
    else:
        break
if quant50 > 0:
    print(f'Total de {quant50} cédulas de R$50')
if quant20 > 0:
    print(f'Total de {quant20} cédulas de R$20')
if quant10 > 0:
    print(f'Total de {quant10} cédulas de R$10')
if quant1 > 0:
    print(f'Total de {quant1} cédulas de R$1')
print('='*40)
print('Volte Sempre no BANCO DE GOTHAM! Tenha um bom dia!')