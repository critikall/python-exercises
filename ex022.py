# Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')).strip()

# O nome com todas as letras maiúsculas
print(f'Seu nome em maiúsculas é {nome.upper()}')

# O nome com todas as letras minúsculas
print(f'Seu nome em minúsculas é {nome.lower()}')

# Quantas letras ao todo (sem considerar espaços)
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')

# Quantas letras tem o primeiro nome
np = nome.split()
print(f'Seu primeiro nome tem {len(np[0])} letras')
