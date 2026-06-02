nome = input('Digite o seu nome completo: ')

print('\nO seu nome completo com letras maiúsculas é: {}\n'.format(nome.upper()))

print('O seu nome completo com letras minúsculas é: {}\n'.format(nome.lower()))

print('O seu nome completo possui {} letras.\n'.format(len(nome.strip())))

print('O seu 1° nome possui {} letras.\n'.format(len(nome.strip().split()[0])))
