pessoas = {'Nome': 'Heitor', 'Sexo': 'M', 'idade': 20}
del pessoas['Sexo']
pessoas['Nome'] = 'Gustavo'
pessoas['peso'] = 62.5
for k, v in pessoas.items():
    print(f'O(A) {k} é {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['silga'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()