'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))

print('''
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
''')
opção = int(input('Insira a opção desejada: '))
while opção != 5:
    if opção == 1:
        print('A soma entre {} e {} é igual à {}'.formart(n1, n2, n1+n2))
    elif opção == 2:
        print('A multiplicação entre {} e {} é igual à {}'.formart(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}'.formart(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Insira o novo valor: '))
        n2 = int(input('Insira o outro novo valor: '))
        opção = int(input('Insira uma opção novamente: '))
    elif opção == 5:
        exit()
    else:
        print('Opção não encontrada!')