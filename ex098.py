# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: inicio, fim e passo, e realize a contagem. Seu programa tem
# que realizar três contagens através da função criada:

# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep


def contador(i, f, p):
    print('=' * 40)
    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if f > i:
        f = f + 1
    elif f < i:
        f = f - 1
        p = -p
    for n in range(i, f, p):
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
sleep(1)
contador(10, 0, 2)

print('\nAgora é a sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
