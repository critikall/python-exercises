# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de insercão (sem usar o
# sort()). No final, mostre a lista ordenada na tela.

lista_num = []

for i in range(5):
    n = int(input('Digite um número: '))

    if i == 0 or n > lista_num[-1]:
        lista_num.append(n)
        print('Adicionado ao final da lista...')

    else:
        pos = 0
        while pos < len(lista_num):
            if n <= lista_num[pos]:
                lista_num.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'\nLista em ordem crescente {lista_num}')
