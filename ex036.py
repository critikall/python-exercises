# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = casa / (anos * 12)

if prestacao <= salario * 30 / 100:
    print(f'O valor da prestação será de R${prestacao :.2f}, empréstimo \033[1;32mAPROVADO\033[m!')
else:
    print(f'O valor da prestação será de R${prestacao :.2f}, empréstimo \033[1;31mNEGADO\033[m!')
