'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#//– O nome com todas as letras maiúsculas e minúsculas.

#//– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

nome = input("Qual é o seu nome completo? ")
up = nome.upper()
lo = nome.lower()
ca = len(nome)
primeiroNome = nome.split()


print("O seu nome em caixa alta é {}\nO seu nome em caixa baixa é {}\nO seu nome possui {} caracteres\nO seu primeiro nome possui {} caracteres".format(up,lo,ca,len(primeiroNome[0])))
