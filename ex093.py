# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
# vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o
# campeonato.

jogador = {"nome": str(input('Nome do Jogador: ')).strip().capitalize()}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

total_gol = 0
gols = list()
for p in range(partidas):
    gol = int(input(f'Quantos gols na partida {p+1}? '))
    total_gol += gol
    gols.append(gol)

jogador["gols"] = gols[:]
jogador["total"] = total_gol

print(f'''
{jogador}
''')

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print(f'\nO jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(jogador["gols"]):
    print(f'Na partida {i+1}, fez {v} gols.')

print(f'\nFoi um total de {jogador["total"]} gols.')

