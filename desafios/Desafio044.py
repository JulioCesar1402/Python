'''
Exercício Python 44: Elabore um programa que calcule o valor 
a ser pago por um produto, considerando o seu preço normal e 
condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros


'''
print('{:=^40}'.format(' Lojas Monteiros '))
preço = float(input('Insira o preço do produto: '))

print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opção = int(input('Insira a opção escolhida: '))
if opção == 1:
    valor = preço * 90/100
elif opção == 2:
    valor = preço * 95/100
elif opção == 3:
    valor = preço
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    tparcelas = int(input('Quantas parcelas? '))
    valor = preço * 120/100
    parcela = valor / tparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(tparcelas,parcela))
else:
    print('Opção ivalida de pagamento. Tente novamente')
print('Será necessario pagar {:.2f}'.format(valor))