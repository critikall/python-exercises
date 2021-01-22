# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

from time import sleep


def maior(* valores):
    num_maior = cont = 0
    print('=' * 50)
    print(f'Analisando os valores passados...')
    for n in valores:
        print(n, end=' ')
        if n > num_maior:
            num_maior = n
        cont += 1
        sleep(0.3)
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()
