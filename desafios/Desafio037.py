'''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.
'''
numero = int(input('Insira um número inteiro: '))
print('Selecione uma das bases para coversão: \n[ 1 ] para binario\n[ 2 ] para octal\n[ 3 ] para hexadecimal')
base = int(input ("Sua opcão: "))

if base == 1:
    print('{} convertido para binário é igual a {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print('{} convertido para octal é igual a {}'.format(numero,oct(numero)[2:]))
elif base ==3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção invalida, Tente Novamente')