cores = {
    'limpar':'\033[m',
    'amarelo':'\033[33m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'azul':'\033[34m',
    'roxo':'\033[35m',
    'ciano':'\033[36m'
}

retaA = float(input('{}Digite o valor da 1ª reta:{} '.format(cores['azul'], cores['limpar'])))
retaB = float(input('{}Digite o valor da 2ª reta:{} '.format(cores['amarelo'], cores['limpar'])))
retaC = float(input('{}Digite o valor da 3° reta:{} '.format(cores['ciano'], cores['limpar'])))

if abs(retaB-retaC) < retaA < retaB+retaC and abs(retaA-retaC) < retaB < retaA+retaC and abs(retaA-retaB) < retaC < retaA+retaB:
    print('{}As retas{} {}{}{}, {}{}{} e {}{}{} {}podem formar um triangulo!{}'.format(cores['roxo'], cores['limpar'], cores['azul'], retaA, cores['limpar'], cores['amarelo'], retaB, cores['limpar'], cores['ciano'], retaC, cores['limpar'], cores['verde'], cores['limpar']))
    if retaA == retaB == retaC:
        print('É um triangulo Equilátero, pois todos os seu lados são iguais')
    elif retaA == retaB != retaC or retaA == retaC != retaB or retaB == retaC != retaA:
        print('É um triângulo isósceles, pois possui 2 lados iguais!')
    elif retaA != retaB != retaC != retaA:
        print('É um triângulo escaleno, pois todos os lados são diferentes!')
else:
    print('{}As retas{} {}{}{}, {}{}{} e {}{}{} {}não podem formar um triângulo!{}'.format(cores['roxo'], cores['limpar'], cores['azul'], retaA, cores['limpar'], cores['amarelo'], retaB, cores['limpar'], cores['ciano'], retaC, cores['limpar'], cores['vermelho'], cores['limpar']))