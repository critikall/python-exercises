# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:

# - À vista no dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f'{" LOJAS GUANABARA ":=^40}')

preco = float(input('Valor total das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('Digite o número da opção desejada: '))

if pagamento == 1:
    print(f'Desconto de 10%. Valor a pagar: R${preco - (preco * 10 / 100) :.2f}')
elif pagamento == 2:
    print(f'Desconto de 5%. Valor a pagar: R${preco - (preco * 5 / 100) :.2f}')
elif pagamento == 3:
    print(f'Valor a pagar: R${preco :.2f}')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela}x de R${(preco + (preco * 20 / 100)) / parcela :.2f}:')
    print(f'Acréscimo de 20%. Valor total das parcelas: R${preco + (preco * 20 / 100) :.2f}')
else:
    print('Opção inválida.')
