'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint

num = randint(1, 10)
player = int(input("insira um numero entre 0 a 10: "))
while player != num:
    player = int(input("Numero errado, tente novamente: "))