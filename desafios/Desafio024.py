'''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga 
se ela começa ou não com o nome “SANTO”.

'''
procura = input('o que deseja encontrar? (coloque em caixa alta) ')

nomeDaCidade = input('Insira o nome da sua cidade: (coloque em caixa alta) ')

check = procura in nomeDaCidade

print('A sua cidade começa com o nome {}: {}'.format(procura,check))