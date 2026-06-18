from datetime import date

anoAtual = date.today().year
contMaior = 0
contMenor = 0

for c in range (0, 7):
    anoNasc = int(input('Digite o ano do seu nascimento: '))
    if anoNasc < 1926 or anoNasc > anoAtual:
        print('Digite um ano de nascimento válido!')
        break
    else:
        if (anoAtual-anoNasc) >= 18:
            contMaior += 1
        elif (anoAtual-anoNasc) < 18:
            contMenor += 1

print('-='*25)
print('{} pessoas ainda NÃO ATINGIRAM A MAIORIDADE e\n{} pessoas já SÃO MAIORES DE IDADE'.format(contMenor, contMaior))