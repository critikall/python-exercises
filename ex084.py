# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
# uma lista. No final, mostre:

# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

cadastro = []
dados = []
maior = menor = 0
nome_pesados = []
nome_leves = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    cadastro.append(dados[:])
    dados.clear()

    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cont == 'S' or cont == 'N':
            break
    if cont == 'N':
        break

for p in cadastro:
    if p[1] == maior:
        nome_pesados.append(p[0])
    if p[1] == menor:
        nome_leves.append(p[0])

print(f'''
Total de pessoas cadastradas: {len(cadastro)}
Pessoas mais pesadas {nome_pesados} que tem {maior:.1f}Kg
Pessoas mais leves {nome_leves} que tem {menor:.1f}Kg''')
