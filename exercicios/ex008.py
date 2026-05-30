medida = float(input('Digite um valor em metros(m): '))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('O seu valor em quilometro é {}km, \no seu valor em hectômetro é {}hm, \no seu valor em decâmetro é {}dam, \no seu valor em decímetro é {:.0f}dm, \no seu valor em centímetros é {:.0f}cm, \no seu valor em milímetros é {:.0f}mm.'.format(km, hm, dam, dm, cm, mm))