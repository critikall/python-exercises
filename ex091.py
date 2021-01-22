# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número no
# dado.

from random import randint
from operator import itemgetter
from time import sleep

jogadores = {"jogador1": randint(1, 6),
             "jogador2": randint(1, 6),
             "jogador3": randint(1, 6),
             "jogador4": randint(1, 6)}

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print(f'{"RANKING DOS JOGADORES":^24}')

for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
