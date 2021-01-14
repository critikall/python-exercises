# Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:

# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000.
# c) Qual é o nome do produto mais barato.

total = 0
produto_mais_1000 = 0
nome_produto_barato = ''
preco_produto_barato = 0
quantidade = 0
print('=' * 30)
print('LOJA DE INFORMÁTICA'.center(30))
print('=' * 30)
while True:
    nome_produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    quantidade += 1
    if preco > 1000:
        produto_mais_1000 += 1
    if quantidade == 1 or preco < preco_produto_barato:
        preco_produto_barato = preco
        nome_produto_barato = nome_produto
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar == 's' or continuar == 'n':
            break
    if continuar == 'n':
        break

print('\n====== COMPRA FINALIZADA ======')
print(f'''Total gasto na compra: R${total:.2f}
Produtos custando mais de R$1000: {produto_mais_1000}
Nome do produto mais barato: {nome_produto_barato} que custa R${preco_produto_barato:.2f}
Total de produtos: {quantidade}''')
