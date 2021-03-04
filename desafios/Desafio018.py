
#!     Exercício Python 18: Faça um programa que leia um ângulo qualquer
#!     e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan 

Ang = float(input("Digite o valor do ângulo: "))
ang = radians(Ang)
seno = sin(ang)
cos = cos(ang)
tg = tan(ang)

print('O valor do seno de {} é {:.2f} \no valor do cosseno de {} é {:.2f} \no valor da tangente de {} é {:.2f}'.format(Ang,seno,Ang,cos,Ang,tg))
