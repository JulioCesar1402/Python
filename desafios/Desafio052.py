'''
Exercício Python 52: Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo.
'''
#! numeros primos são numeros divisiveis por 1 e por ele mesmo, apenas
n = int(input('Insira um numero para a verificação: '))

if n != 2 and n % 2 ==0 :
    print('O numero inserido não é primo!')
else:
    print('O numero inserido é primo!')