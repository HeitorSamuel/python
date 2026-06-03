nome = str(input('Digite o seu nome completo: ')).strip()

print('O seu nome completo com letras maiúsculas é: {}'.format(nome.upper()))

print('O seu nome completo com letras minúsculas é: {}'.format(nome.lower()))

print('O seu nome completo possui {} letras.'.format(len(nome.replace(' ', ''))))

print('O seu 1° nome possui {} letras.'.format(len(nome.split()[0])))
