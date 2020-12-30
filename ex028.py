# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint

print('-=-' * 18)
print('Pensei em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 18)

nc = randint(0, 5)
np = int(input('Qual número eu pensei? '))

if np == nc:
    print('PARABÉNS! Você acertou.')
else:
    print(f'ERROU. Eu pensei no número {nc} e não no {np}')
