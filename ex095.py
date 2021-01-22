# Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de deatalhes do aproveitamento de
# cada jogador.

time = list()
jogador = dict()
total_gol = 0

while True:
    print('=' * 36)
    jogador["nome"] = str(input('Nome: ')).strip().capitalize()
    tot_jogos = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    jogador_gol = list()

    for p in range(tot_jogos):
        gol = int(input(f'Quantos gols na partida {p+1}? '))

        jogador_gol.append(gol)
        total_gol += gol

    jogador["gols"] = jogador_gol[:]
    jogador["total"] = total_gol
    time.append(jogador.copy())
    total_gol = 0

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        else:
            print('ERRO! Por favor, digite S ou N.')
    if resp == "N":
        break

print('=-=' * 16)
print('COD', end=' ')
for i in jogador.keys():
    print(f'{i.upper():<15}', end=' ')
print()

for k, v in enumerate(time):
    print(f'{k:>2} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('=-=' * 16)

while True:
    dados = int(input('Mostrar dados de qual jogador? [999 p/ sair] '))
    if dados < len(time) and dados != 999:
        print('=' * 46)
        print(f'LEVANTAMENTO DO JOGADOR {time[dados]["nome"].upper()}:')

        for c, g in enumerate(time[dados]["gols"]):
            print(f'No jogo {c+1} fez {g} gols.')
        print('=' * 46)

    elif dados == 999:
        break

    else:
        print(f'ERRO! Não existe jogador com código {dados}.')
        print('=' * 46)
