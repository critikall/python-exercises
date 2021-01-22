# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e
# vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[n], end=' ')
        sleep(0.3)
    print('Fim!')


def somapar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos {s}')


# Programa principal
numeros = list()
sorteio()
somapar()
