# Melhore o DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('-=-' * 18)
print('Pensei em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 18)

computador = randint(0, 10)
tentativas = 0
vitoria = False

while not vitoria:
    jogador = int(input('Qual número eu pensei? '))
    tentativas += 1
    if jogador == computador:
        vitoria = True
    else:
        print('Errou, tente novamente.\n')

print(f'\nPARABÉNS! Você acertou com {tentativas} tentativas.')
