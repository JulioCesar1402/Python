'''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre 
a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
t = 0
for c in range(1,7):
    i = int(input('Insira o {}º numero: '.format(c)))
    if (i % 2) == 0:
        t += i
print(t)