'''
Exercício Python 26: Faça um programa que leia uma frase pelo teclado 
e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez.

frase: Dhaurehra tinha uma população de 18,882 habitantes.
'''
frase = input('Insira a frase: ')
vezes = frase.count('a')
priVez = frase.find('a')
ultVez = frase.rfind('a')

print('Na sua frase a letra "a" aparece {} vezes. \nAparece a letra "a" pela primeira vez em {}. \nAparece a letra "a" pela última vez em {}. '.format(vezes,priVez,ultVez))