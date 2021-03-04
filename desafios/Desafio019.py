
#! Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#! Faça um programa que ajude ele,
#! lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

#? Armazena os nomes dos alunos
a1 = input("O nome do primeiro aluno: ")
a2 = input("o nome do segundo aluno: ")
a3 = input("O nome do terceiro aluno: ")
a4 = input("O nome do quarto aluno: ")

#! para que o choice funcione é necessario colocar as variaveis entre "[]" dentro de um array
c = [a1, a2, a3, a4]

#? trás para o usuario o aluno escolhido a partir da utilização do "choice()"
print("O aluno escolhido foi o {} ".format(choice(c)))