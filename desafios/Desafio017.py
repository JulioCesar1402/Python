
#!Exercício Python 17: Faça um programa que leia o comprimento do cateto 
#!oposto e do cateto adjacente de um triângulo retângulo.
#! Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))
'''
hip = (ca**2 + co**2) ** (1/2)

print('O valor da hipotenusa é {:.2f}'.format(hip))
'''
hi = math.hypot(ca,co)

print("O valor da hipotenusa será de {:.2f}".format(hi))
