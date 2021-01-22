# Faça um programa que tenha uma função chamada area(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a área
# do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')


area(largura=float(input('Largura (m): ')), comprimento=float(input(
    'Comprimento (m): ')))
