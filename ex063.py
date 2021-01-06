# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# Sequência de Fibonacci. Ex: 0 ➝ 1 ➝ 1 ➝ 2 ➝ 3 ➝ 5 ➝ 8

n = int(input('Quantos elementos da Sequência de Fibonacci você quer? '))
contador = 0
t3 = 0
t1 = 1
t2 = 1

if n == 1:
    print('0 ➝ ', end='')
elif n == 2:
    print('0 ➝ 1 ➝ ', end='')
elif n >= 3:
    print('0 ➝ 1 ➝ 1 ➝ ', end='')
    while contador < n - 3:
        t3 = t1 + t2
        t2 = t1
        t1 = t3
        print(f'{t3}', end=' ➝ ')
        contador += 1
print('Fim')
