'''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = input('Insira o seu nome completo: ')
deck = nome.split()
print('O seu primeiro nome é {} e o seu ultimo nome é {}.'.format(deck[0],deck[(len(deck) - 1)]))