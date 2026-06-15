termoAtual = int(input('Digite o 1° termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('{:=^80}'.format(' Os 10 primeiros termos da PA são: ' ))

for c in range(1, 11):
    print(termoAtual)
    termoAtual += razao

print('{:=^40}'.format(' FIM '))