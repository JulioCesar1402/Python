dinheiroTotal = int(input("Quanto dinheiro deseja converter? "))
valorDoDolar = float(input("Insira o cambio do dolar: "))
cambio = dinheiroTotal / valorDoDolar
print('Tendo {} reais e com o cambio do dolar estando em {}, você irá receber {:.2f} dolares'.format(dinheiroTotal, valorDoDolar, cambio))