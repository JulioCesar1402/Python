dia = int(input('Por quantos dias o carro foi utilizado? '))
km = float(input('Quantos km foram rodados? '))
divida = dia * 50 + km * 0.15
print('Será necessario pagar {}'.format(divida))