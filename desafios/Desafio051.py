'''

Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

num = int(input("Insira o primeiro termo da P.A.: "))
ra = int(input('Insira a razão da P.A.: '))
for c in range(1,11):
    print('{}º Valor da PA: {}'.format(c,num))
    num += ra
print('Acabou!')