'''teste = []
teste.append('Gustavo')
teste.append(40)
pessoas = []
pessoas.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
pessoas.append(teste[:])
print(pessoas)'''
'''
pessoas = [['Maria', 22], ['José', 30], ['João', 15], ['Ana', 45]]
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos!')'''
dado = []
galera = []
for c in range (0, 3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)