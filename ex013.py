# Faça um algoritmo que leia o salário deum funcionário e mostre seu novo salário, com 15% de aumento.

# Salário Atual
salario_atual = float(input('Qual é o salário do funcionário? R$'))
salario_novo = salario_atual + (salario_atual * 15 / 100)

# Salário com aumento de 15%
print(f'O Novo salário com aumento de 15% vai ser de R${salario_novo :.2f}')
