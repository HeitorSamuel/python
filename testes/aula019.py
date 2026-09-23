'''pessoas = {'Nome': 'Heitor', 'Sexo': 'M', 'idade': 20}
del pessoas['Sexo']
pessoas['Nome'] = 'Gustavo'
pessoas['peso'] = 62.5
for k, v in pessoas.items():
    print(f'O(A) {k} é {v}')
'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''
'''estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['silga'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()'''
kit_rick = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
kit_michonne = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
kit_daryl = ["arco e flecha","flechas","faca_de_caca", "corda", "carne_seca"]
kit_carol = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]

#Para começar a jornada
kit = ["taco_beisebol","besta","kit_medico", "feijao_enlatado", "walkie_talkie", "garrafa_agua","biscoito"]

sobrevivente = str(input()).strip()

if sobrevivente == 'Rick':
  print('Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite')
  kit.append("lanterna")

elif sobrevivente == 'Michonne':
  print('Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos.')
  kit.append("faca_afiada")
  
elif sobrevivente == 'Daryl':
  print('Daryl é um ótimo caçador. Ele te dá carne para comer na refeição')
  kit.append("carne")

elif sobrevivente == 'Carol':
  print('Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.')
  kit.append("roupa_de_camuflagem")
  
#Primeiro Dia

if sobrevivente == 'Rick':
  kit.remove("taco_beisebol")
  print(f'Kit atual sobrevivente: {kit}')

elif sobrevivente == 'Michonne':
  kit.remove("kit_medico")
  print('Você usou o kit médico para socorrer Michonne!')
  print(f'Kit atual sobrevivente: {kit}')
  
elif sobrevivente == 'Daryl':
  kit.replace("besta", "arco e flecha")
  kit_daryl.replace("arco e flecha", "besta")
  print(f'Kit atual sobrevivente: {kit}')
  print(f'Kit atual Daryl: {kit_daryl}')
  
elif sobrevivente == 'Carol':
  kit_carol += kit[2:5]
  
#Segundo dia:

if sobrevivente == 'Rick':
  kit_rick += kit[2:]

elif sobrevivente == 'Michonne':
  kit_michonne+= kit[2:]

elif sobrevivente == 'Daryl': 
  kit_daryl+= kit[2:]

elif sobrevivente == 'Carol':
  kit_carol+= kit[2:]

del kit[2:]

print('Agora com as costas mais leves, podemos continuar com a nossa caminhada\n')

#Terceiro dia

print('Finalmente chegamos em Alexandria!\n')
print(f'Ufa, podemos ficar aqui por um tempo,{sobrevivente}\n')

if sobrevivente == 'Rick':
  print(f'Kit do sobrevivente: {kit}\n Kit do {sobrevivente}: {kit_rick}')

elif sobrevivente == 'Michonne':
  print(f'Kit do sobrevivente: {kit}\n Kit do {sobrevivente}: {kit_michonne}')

elif sobrevivente == 'Daryl': 
  print(f'Kit do sobrevivente: {kit}\n Kit do {sobrevivente}: {kit_daryl}')

elif sobrevivente == 'Carol':
  print(f'Kit do sobrevivente: {kit}\n Kit do {sobrevivente}: {kit_carol}')

