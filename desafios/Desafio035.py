
#! Pega os valores das retas que formaram o triangulo
r1 = float(input('Insira o valor da primeira reta: '))
r2 = float(input('Insira o valor da segunda reta: '))
r3 = float(input('Insira o valor da terceira reta: '))

#? verifica se é possivel fazer um triangulo com os valores inseridos
if r1 < (r2 + r3) and r2 < (r1 + r3 ) and r3 < (r2 + r1):
    print('É possivel fazer um triangulo com os valores inseridos!')
else:
    print('Não é possivel fazer um triangulo com os valores inseridos!')