''''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
print('{:=^40}'.format(' Jokenpô '))

#? Escolha do jogador
print('[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura')
num = int(input('Sua escolha: '))
if num == 1:
    print('Você jogou pedra!')
elif num == 2:
    print('Você jogou papel!')
elif num == 3:
    print('Você jogou a tesoura!')
else:
    print('Tente novamente')
    exit()
#? Escolha do sistema
itens = (1,2,3)
escolha = randint(1,3)

if escolha == 1:
    print('O sistema jogou pedra!')
elif escolha == 2:
    print('O sistema jogou papel!')
elif escolha == 3:
    print(' O sistema jogou a tesoura!')

#? ver quem ganhou

if escolha == num:
    print('Empate')

#! chances do jogador ganhar
elif escolha == 3 and num == 1:
    print('Você ganhou!')
elif escolha == 1 and num == 2:
    print('Você ganhou!')
elif escolha == 2 and num == 3:
    print('Você ganhou!')

#! chances do sistema ganhar
elif escolha == 1 and num == 3:
    print('O sistema ganhou!')
elif escolha == 2 and num == 1:
    print('O sistema ganhou!')
elif escolha == 2 and num == 3:
    print('O sistema ganhou!')
