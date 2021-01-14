# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços,
# organizando os dados em forma tabular.

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)

print('='*42)
print(f'{"LISTAGEM DE PREÇOS":^42}')
print('='*42)

total = 0
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<32}', end='')
    else:
        print(f'R${listagem[i]:>7.2f}')
        total += listagem[i]
print(f'\n{"TOTAL":.<32}R$ {total:>6.2f}')

print('='*42)
