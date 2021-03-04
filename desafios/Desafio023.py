'''
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada 
um dos dígitos separados.
'''
num = input('Insira um número de 0 à 9999: ')
print('Analisando o numero {}\nUnitade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num,num[3],num[2],num[1],num[0]))
