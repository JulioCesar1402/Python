'''
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Insira o seu sexo [ M / F ]: ')).strip().upper()[0]
while sexo not in 'MnfF' :
    sexo = input('Dados incorretos! Insira o sexo da pessoa: ').strip().upper()[0]
print('Sexo {} registrado!'.format(sexo))
