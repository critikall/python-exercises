# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:

# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média

cadastro = list()
pessoa = dict()
tot_idade = media = 0

while True:
    pessoa["nome"] = str(input('Nome: ')).strip().capitalize()

    while True:
        pessoa["sexo"] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa["sexo"] == "M" or pessoa["sexo"] == 'F':
            break
        else:
            print('ERRO! por favor digite apenas M ou F.')

    pessoa["idade"] = int(input('Idade: '))

    tot_idade += pessoa["idade"]
    cadastro.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp == "S" or resp == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == "N":
        break

media = tot_idade / len(cadastro)

print(f'\nTotal de pessoas cadastradas: {len(cadastro)}')

print(f'A média de idade é de {media:.2f} anos.')

print('As mulheres cadastradas foram:', end=' ')

for p in cadastro:
    if p["sexo"] == "F":
        print(p["nome"], end=' ')

print('\nPessoas com idade acima da média:', end=' ')

for p in cadastro:
    if p["idade"] > media:
        print(f'{p["nome"]} com {p["idade"]} anos', end=' ')
