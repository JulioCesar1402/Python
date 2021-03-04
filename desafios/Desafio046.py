'''
Exercício Python 46: Faça um programa que mostre na tela uma contagem 
regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma 
pausa de 1 segundo entre eles.
'''
s = 11
for c in range(0, 11):
    s -= 1
    print(s)
print('Explodiu!!')