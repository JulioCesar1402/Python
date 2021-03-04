'''
Exercício Python 28: Escreva um programa que faça o computador 
“pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
g = randint(0,5)
num = int(input('Insira um número de 0 à 5: '))
if g == num:
    print("parabens! você acertou!")
else:
    print('Que pena! o computador escolheu {} e não {}'.format(g, num))
