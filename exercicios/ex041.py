from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('Você tem {} anos! Você é da categoria MIRIM de natação!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos! Você é da categoria INFANTIL de natação!'.format(idade))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos! Você é da categoria JUNIOR de natação!'.format(idade))
elif idade == 20:
    print('Você tem {} anos! Você é da categoria SÊNIOR de natação!'.format(idade))
elif idade > 20:
    print('Você tem {} anos! Você é da categoria MASTER de natação!'.format(idade))