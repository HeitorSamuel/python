pessoas = []
dadoIndv = []
maiorP = menorP = 0
maiorN = menorN = ''
listaMaiorN = []
listaMenorN = []
cont = 0
while True:
    dadoIndv.append(str(input('Nome: ').strip()))
    dadoIndv.append(float(input('Peso: ').strip()))
    pessoas.append(dadoIndv[:])
    cont += 1
    dadoIndv.clear()
    for p in pessoas:
        if cont == 1:
            maiorP = menorP = p[1]
            maiorN = menorN = p[0]
        else:
            if p[1] > maiorP:
                maiorP = p[1]
                maiorN = p[0]
                listaMaiorN.append(maiorN)
            elif p[1] < menorP:
                menorP = p[1]
                menorN = p[0]
                listaMenorN.append(menorN)
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while 'S' not in perg and 'N' not in perg:
        perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorP}Kg. Peso de {listaMaiorN}')
print(f'O menor peso foi de {menorP}Kg. Peso de {listaMenorN}')