# Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

nums = []
par = []
impar = []

while True:
    nums.append(int(input('Digite um número: ')))

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break

for n in nums:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(f'''
Lista completa: {nums}
Lista de pares: {par}
Lista de ímpares: {impar}''')
