# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual é o valor do salário atual do funcionário? R$'))

if sal > 1250:
    novo_sal = sal + (sal * 10 / 100)
else:
    novo_sal = sal + (sal * 15 / 100)

print(f'O novo salário vai ser de R${novo_sal :.2f}')
