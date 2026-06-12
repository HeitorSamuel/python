from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - anoNasc

if idade < 18:
    print('''
Você tem {} anos em {}! 
Ainda faltam {} anos para o seu alistamento
Seu alistamento será em {}.
          '''.format(idade, anoAtual, 18-idade, anoAtual+(18-idade)))
elif idade == 18:
    print('''
Você tem {} anos em {}! 
É a hora de você se alistar ao serviço militar!'''.format(idade, anoAtual))
else:
    print('''
Você tem {} anos em {}! 
Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.
          '''.format(idade, anoAtual, idade-18, anoAtual-(idade-18)))