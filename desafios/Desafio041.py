'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
idade = int(input('Insira a sua idade: '))
print('De acordo com a sua idade, você é ',end='')
if idade <= 9:
    print('Mirim')
elif idade > 9 and idade <=  14:
    print('Infantil')
elif idade > 14 and idade < 19:
    print('Junior')
elif idade > 19 and idade <= 25:
    print('Sênior')
else:
    print('Master')
