'''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal 
não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorDaCasa = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira o valor do seu salário: R$'))
anosDePagamento = int(input('Insira por quantos anos deseja efetuar o pagamento: '))
prestação = valorDaCasa / (anosDePagamento * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorDaCasa, anosDePagamento), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
#! print('Comparação tem que pagar {} e o minimo é de {}'.format(prestação, minimo))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')