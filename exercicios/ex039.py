from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - anoNasc

if idade < 18:
    print('Você tem {} anos! \nVocê ainda vai se alistar ao serviço militar qunado fizer 18 anos!'.format(idade))
elif idade == 18:
    print('Você tem {} anos! \nÉ a hora de você se alistar ao serviço militar!'.format(idade))
else:
    print('Você tem {} anos! \nVocê já passou do tempo do alistamento militar que é aos 18 anos!'.format(idade))