'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
cont = 0
cont2 = 0
for c in range(1,8):
    n = int(input('Insira o ano de nascimento da {}° pessoa: '.format(c)))
    if (date.today().year - n) >= 18:
        cont +=1
        print('A pessoa {} que  nasceu em {} atingiu a maioridade!'.format(c, n))
    else:
        cont2 +=1
        print('A pessoa {} que nasceu em {} ainda não atingiu a maioridade!'.format(c, n))

print('Resumindo, {} já atingiram a maioridade e {} ainda não atingiram a maioridade'.format(cont, cont2))
