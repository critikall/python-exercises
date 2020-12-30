# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número: '))
conversao = int(input('Qual será a conversão? Digite: \n[1] para binário \n[2] para octal \n[3] para hexadecimal \n'))

if conversao == 1:
    print(f'Conversão binária: {bin(num)[2:]}')
elif conversao == 2:
    print(f'Conversão octal: {oct(num)[2:]}')
elif conversao == 3:
    print(f'Conversão hexadecimal: {hex(num)[2:]}')
else:
    print('Opção inválida.')