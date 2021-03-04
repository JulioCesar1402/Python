
#! Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de 
#! apresentação de trabalhos dos alunos. 
#! Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input("O nome do primeiro aluno: ")
a2 = input("O nome do segundo aluno: ")
a3 = input("O nome do terceiro aluno: ")
a4 = input(" o nome do quarto aluno: ")

deck = [a1,a2,a3,a4]
shuffle(deck)
print("A ordem de apresentação de trabalho será:{}".format(deck))