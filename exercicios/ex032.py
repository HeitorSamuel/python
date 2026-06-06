#ano bissexto
from datetime import date

ano = int(input('Qual ano você quer consultar? Digite 0 para ver o ano atual. '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 != 00:
        print('O ano {} é bissexto!'.format(ano))
    else:
        if ano % 400 == 0:
            print('O ano {} é bissexto!'.format(ano))  
        else:
            print('O ano {} não é bissexto!'.format(ano)) 
else:
    print('O ano {} não é bissexto!'.format(ano))
