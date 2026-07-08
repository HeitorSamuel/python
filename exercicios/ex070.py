print('-'*40)
print(f'{' LOJA SUPER BARATÃO ':^40}')
print('-'*40)
TotalComp = QuantProdtMil = contProdt = maior = menor = 0
nomeMaior = nomeMenor = ''

while True:
    nomeProdt = str(input('Digite o nome do Produto: ').strip())
    preco = float(input('Digite o preço do produto: R$').strip())
    TotalComp += preco
    contProdt += 1
    if contProdt == 1:
        precoMaior = precoMenor = preco
        nomeMaior = nomeMenor = nomeProdt
    else:
        if preco < precoMenor:
            precoMenor = preco
            nomeMenor = nomeProdt

    if preco > 1000:
        QuantProdtMil += 1
    
    pergCont = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    while pergCont != 'S' and pergCont != 'N':
        pergCont = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if pergCont == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${TotalComp:.2f}')
print(f'Temos {QuantProdtMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenor} que custa R${precoMenor:.2f}')