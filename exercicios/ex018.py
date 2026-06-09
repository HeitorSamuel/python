from math import sin, cos, tan, radians

cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'azul':'\033[34m',
    'roxo':'\033[35m'
}

ang = int(input('{}Digite um ângulo qualquer:{} '.format(cores['verde'], cores['limpar'])))
angconv = radians(ang)
print('O ângulo de {}{}°{} tem {}o seno{} valendo: {}{:.1f}{}, \n{}o cosseno{} valendo {}{:.1f}{}, e \n{}a tangente{} valendo: {}{:.1f}{}'.format(cores['verde'], ang, cores['limpar'], cores['amarelo'], cores['limpar'], cores['amarelo'], sin(angconv), cores['limpar'], cores['azul'], cores['limpar'], cores['azul'], cos(angconv), cores['limpar'], cores['roxo'], cores['limpar'], cores['roxo'], tan(angconv), cores['limpar']))