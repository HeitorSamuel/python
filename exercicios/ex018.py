from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo qualquer: '))
angconv = radians(ang)
print('O ângulo de {}° tem o seno valendo: {:.1f}, \no cosseno valendo {:.1f}, e \na tangente valendo: {:.1f}'.format(ang, sin(angconv), cos(angconv), tan(angconv)))