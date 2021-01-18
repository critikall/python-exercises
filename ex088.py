# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O
# programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('=' * 25)
print('MEGA SENA'.center(25))
print('=' * 25)

jogos = []
temp_jogos = []

quant_jogos = int(input('Quantos jogos você quer? '))

while True:

    while len(temp_jogos) < 6:
        num = randint(1, 60)
        if num not in temp_jogos:
            temp_jogos.append(num)

    temp_jogos.sort()
    jogos.append(temp_jogos[:])
    temp_jogos.clear()

    if len(jogos) == quant_jogos:
        break

print()

for pos, j in enumerate(jogos):
    print(f'Jogo {pos+1}: {j}')
    sleep(1)

print('\nBOA SORTE!')
