# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()

print(f'O primeiro nome é {nome1[0]} \nO último nome é {nome1[len(nome1)-1]}')
