nome = str(input('Digite o seu nome: '))

if nome == 'Heitor':
    print('Que nome lindo você tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('O seu nome é bem popular no Brasil!')
elif nome in 'Ana Lívia Júlia Ellen':
    print('Que belo nome feminino!')
else:
    print('O seu nome é tão normal!')

print('Tenha um bom dia, {}!'.format(nome))