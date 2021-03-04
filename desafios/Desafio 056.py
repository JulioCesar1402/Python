'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
mIdade = 0
mulheres = 0
maior = 0
nomevelho = 0
mulheresMenores = 0
for c in range(1,5):
    nome = input('Insira um nome: ')
    idade = int(input('Insira uma idade: '))
    sexualidade = input('Insira a sua sexualidade: (M/F) ')
    mIdade += idade
    if c == 1 and sexualidade == 'M':
        maior = idade
        nomevelho = nome
    else:
        if idade > maior:
            maior = idade
            nomevelho = nome
    if sexualidade == 'F' and idade < 20:
        mulheresMenores += 1

print('O homem mais velho é o {}'.format(nomevelho))
#! media das idade:
print('A media das idades são: {}'.format(mIdade/c))
#! quantidade de mulheres menores de vinte anos:
print('Existem {} mulheres com menos de 20 anos'.format(mulheresMenores))




