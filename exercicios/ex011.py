larg = float(input('Digite a largura da parede em metros(m): '))
alt = float(input('Digite a altura da parede em metros(m): '))
area = larg*alt
print('A área da parede vale: {:.0f}m² \ne a quantidade de tinta necessária para pintá-la é de: {:.0f}L'.format(area, area/2))