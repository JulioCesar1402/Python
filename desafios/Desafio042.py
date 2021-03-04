'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''
n1 = float(input('Insira o valor da primeira reta: '))
n2 = float(input('Insira o valor da segunda reta: '))
n3 = float(input('Insira o valor da terceira reta: '))

if n1 < (n2 + n3) and n2 < (n1 + n3) and n3 < (n1 + n2):
    if n1 == n2 == n3:
        triangulo = 'EQUILATERO'
    elif n1 == n2 != n3:
        triangulo = 'ISÓSCELES'
    elif n1 != n2 != n3:
        triangulo = 'ESCALENO'
    print('É possivel formar um triangulo {} com esses valores'.format(triangulo))

else:
    print('Não é possivel formar um triangulo com esses valores')