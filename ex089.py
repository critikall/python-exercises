# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim contendo a média
# de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

cadastro = []
dados = []

while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    cadastro.append(dados[:])
    dados.clear()

    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont == 'S' or cont == 'N':
            break

    if cont == 'N':
        break

print()

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, n in enumerate(cadastro):
    print(f'{i:<4}{cadastro[i][0]:<10}'
          f'{(cadastro[i][1] + cadastro[i][2]) / 2:>8.1f}')

while True:
    aluno = int(input('\nMostrar notas de qual aluno? (999 interrompe): '))

    if aluno != 999 and aluno < len(cadastro):
        print(f'Notas de {cadastro[aluno][0]} são {cadastro[aluno][1:3]}')

    elif aluno == 999:
        break
