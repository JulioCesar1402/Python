salario = float(input('Insira o seu salario: R$'))

if salario > 1250:
    aumento = salario * 110/100
if salario <= 1250:
    aumento = salario *115/100

print('Seu salario com aumento será igual à R${:.2f}'.format(aumento))