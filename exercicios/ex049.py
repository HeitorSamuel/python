numTab = int(input('Digite um número inteiro: '))
print('{:=^40}'.format(' TABUADA DE {} '.format(numTab)))

for c in range (0, 11):
    print('{} X {} = {}'.format(numTab, c, c*numTab))

print('{:=^50}'.format(' FIM '))