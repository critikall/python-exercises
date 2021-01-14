# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('=-' * 11)
print('JOGO DE PAR OU ÍMPAR')
print('=-' * 11)

vitoria = 0

while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    par_impar = ' '
    while par_impar not in 'pi':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    soma = (jogador + computador)
    condicao_vitoria = soma % 2
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end=' ')
    print('Deu PAR' if condicao_vitoria == 0 else 'Deu ÍMPAR')
    if par_impar == 'p':
        if condicao_vitoria == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif par_impar == 'i':
        if condicao_vitoria == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    sleep(1)
    print('\nVamos jogar novamente...\n')
    sleep(1)

print(f'\nGAME OVER! Você venceu {vitoria} vez(es).')
