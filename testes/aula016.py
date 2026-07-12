#TUPLAS SÃO IMUTÁVEIS
#lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

#print(sorted(lanche))
'''
#1ª MANEIRA:
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#2ª MANEIRA:
for comida in lanche:
    print(f'Eu vou comer {comida}')

#3ª MANEIRA:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi Demais!!!')
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
print(c)