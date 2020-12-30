# Desenvola um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Qual a distância da viagem? '))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45

print(f'O preço da passagem é de R${preço :.2f}')
