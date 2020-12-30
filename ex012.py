# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o valor do produto? R$'))
desconto = preço * 0.05
novo = preço - desconto
print(f'Preço original R${preço :.2f}')
print(f'Valor do desconto R${desconto :.2f}')
print(f'Preço do produto com Desconto R${novo :.2f}')
