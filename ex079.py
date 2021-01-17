# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break

numeros.sort()
print(f'\nVocê digitou os valores {numeros}')
