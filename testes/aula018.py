'''teste = []
teste.append('Gustavo')
teste.append(40)
pessoas = []
pessoas.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
pessoas.append(teste[:])
print(pessoas)'''

pessoas = [['Maria', 22], ['José', 30], ['João', 15], ['Ana', 45]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos!')