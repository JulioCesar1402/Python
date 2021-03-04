'''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for.
'''
c = 0
i = 0
n = int(input('Insira o valor que deseja ver a tabuada:'))
for c in range(0,11):
    i = c * n
    print("{} x {} = {}".format(n,c,i))


