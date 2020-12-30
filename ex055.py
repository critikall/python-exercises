# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª: '))
    lista += [peso]
print(f'''\nMaior peso: {max(lista)}Kg
Menor peso: {min(lista)}Kg''')
