# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('\033[31m=-=\033[m' * 7)
print('\033[1;32;40mJOKENPÔ MINI GAME\033[m'.center(33))
print('\033[31m=-=\033[m' * 7)
print('\n')

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

print('Opções de jogo: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA')

jogador = int(input('Digite o número da sua jogada: '))

if jogador <= 2:
    print('\n')
    sleep(1)
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print(f'''
Computador jogou: {opcoes[computador].upper()}
Jogador jogou: {opcoes[jogador].upper()}
    ''')
    
    if computador == 0:  # PEDRA
        if jogador == 0:
            print('\033[1;32mEMPATE\033[m')
        elif jogador == 1:
            print('\033[1;34mJOGADOR VENCEU\033[m')
        else:
            print('\033[1;31mJOGADOR PERDEU\033[m')
    
    elif computador == 1:  # PAPEL
        if jogador == 0:
            print('\033[1;31mJOGADOR PERDEU\033[m')
        elif jogador == 1:
            print('\033[1;32mEMPATE\033[m')
        else:
            print('\033[1;34mJOGADOR VENCEU\033[m')
    
    else:
        if jogador == 0:  # TESOURA
            print('\033[1;34mJOGADOR VENCEU\033[m')
        elif jogador == 1:
            print('\033[1;31mJOGADOR PERDEU\033[m')
        else:
            print('\033[1;32mEMPATE\033[m')
else:
    print('\n\033[1;31mJOGADA INVÁLIDA\033[m! Tente novamente.')
