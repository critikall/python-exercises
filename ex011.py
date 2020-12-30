# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

alt = float(input('Altura da parede: '))
larg = float(input('Largura da parede: '))
area = alt * larg
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
print(f'Para pintar a parede vai precisar de {tinta :.2f} litros de tinta.')
