n1 = float(input("digite a primeira nota: "))
n2 = float(input('digite a segunda nota: '))
m = (n2 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉns!')
else:
    print('Repetend feelsbad')

    '''
    Por if simplificado ficari:
    print('Sua media foi boa' if m >=6.0 else 'repetente')
  '''
  