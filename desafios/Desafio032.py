ano = int(input("Insira o ano: "))
if ano % 4 == 0:
    print('O ano {} inserido é bissexto!'.format(ano))
else:
    print('O ano {} inserido não é bissexto!'.format(ano))