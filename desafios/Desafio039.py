'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e 
informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa 
também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
atual = date.today().year
data = int(input('Insira o ano de nascimento: '))
idade = atual - data

if idade > 18:
    mais = idade - 18
    print('Vocẽ já deveria ter feito o alistamento à {} anos '.format(mais))
elif idade < 18:
    menos = 18 - idade
    print('Você ainda vai se alistar daqui {} anos'.format(menos))
elif idade == 18:
    print('É hora de se alistar')
else:
    print('Algo deu errado, tente novamente')

