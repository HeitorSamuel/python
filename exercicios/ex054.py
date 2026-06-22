from datetime import date

anoAtual = date.today().year
contMaior = 0
contMenor = 0

for c in range (1, 8):
    anoNasc = int(input('Digite o ano do nascimento da {}ª pessoa: '.format(c)))
    if anoNasc < 1926 or anoNasc > anoAtual:
        print('Digite um ano de nascimento válido! Tente Novamente!')
        break
    else:
        if (anoAtual-anoNasc) >= 18:
            contMaior += 1
        elif (anoAtual-anoNasc) < 18:
            contMenor += 1

print('-='*25)
print('{} pessoas ainda NÃO ATINGIRAM A MAIORIDADE e\n{} pessoas já SÃO MAIORES DE IDADE'.format(contMenor, contMaior))
print('-='*25)