print('='*40)
print(f'{'BANCO DE GOTHAM':^40}')
print('='*40)
ValorRest =  quant50 = quant20 = quant10 = quant1 = 0
pergValor = int(input('Que valor você quer sacar? R$').strip())
while True:
    
    if pergValor >= 50:
        pergValor -= 50
        ValorRest = pergValor
        quant50 += 1
    elif pergValor >= 20:
        pergValor -= 20
        ValorRest = pergValor
        quant20 += 1
    elif pergValor >= 10:
        pergValor -= 10
        ValorRest = pergValor
        quant10 += 1
    elif pergValor >= 1:
        pergValor -= 1
        ValorRest = pergValor
        quant1 += 1
    else:
        break
print(f'''Total de {quant50} cédulas de R$50
Total de {quant20} cédulas de R$20
Total de {quant10} cédulas de R$10
Total de {quant1} cédulas de R$1''')
print('='*40)
print('Volte Sempre no BANCO DE GOTHAM! Tenha um bom dia!')