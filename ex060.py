# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5x4x3x2x1=120


n = int(input('Digite um número: '))
f = 1
print(f'{n}! = {n}', end='')
while n != 1:
    f *= n
    n -= 1
    print(f' X {n}', end='')
print(f' = {f}')
