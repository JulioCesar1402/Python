largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
area = largura * altura
tinta = 2 * area
print('A sua paredde tem {} m² de área e será necessario {} litros de tinta para pintá-la'.format(area,tinta))