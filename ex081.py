# Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, mostre:

# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista_nums = []
pos_5 = []
contador = 0

while True:
    n = int(input('Digite um valor: '))
    lista_nums.append(n)
    contador += 1

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break

for p, n in enumerate(lista_nums):
    if n == 5:
        pos_5.append(p)

print(f'\nVocê digitou {contador} elementos.')

lista_nums.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista_nums}''')

if 5 in lista_nums:
    print(f'O valor 5 faz parte da lista e está nas posições {pos_5}')
else:
    print('O valor 5 não foi encontrado na lista!')
