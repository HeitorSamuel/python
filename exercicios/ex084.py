pessoas = []
dadoIndv = []
maiorP = menorP = 0
listaMaiorN = []
listaMenorN = []
cont = 0
while True:
    nome = str(input('Nome: ').strip())
    peso = float(input('Peso: ').strip())
    dadoIndv.append(nome)
    dadoIndv.append(peso)
    pessoas.append(dadoIndv[:])
    cont += 1
    if cont == 1:
        maiorP = menorP = peso
    else:
        if peso > maiorP:
            maiorP = peso
        elif peso < menorP:
            menorP = peso
    dadoIndv.clear()
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while 'S' not in perg and 'N' not in perg:
        perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break

for p in pessoas:
    if p[1] == maiorP:
        listaMaiorN.append(p[0])
    elif p[1] == menorP:
        listaMenorN.append(p[0])
print(f'Ao todo você cadastrou {len(pessoas)} pessoa(s).')
if len(pessoas) == 1:
    print(f'Não há maior e nem menor peso, só {pessoas[0][0]} com o peso de {pessoas[0][1]}Kg')
if len(pessoas) > 1:
    print(f'O maior peso foi de {maiorP}Kg. Peso de', end=' ')
    for nomeMaior in listaMaiorN:
        print(f'[{nomeMaior}]', end=' ')
    print(f'\nO menor peso foi de {menorP}Kg. Peso de', end=' ')
    for nomeMenor in listaMenorN:
        print(f'[{nomeMenor}]', end=' ')