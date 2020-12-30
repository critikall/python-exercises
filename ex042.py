# Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))

if (y + z) > x and (x + z) > y and (x + y) > z:
    print('Os segmentos acima \033[1:34mPODEM\033[m formar um triângulo', end=' ')
    if x == y and y == z:
        print('EQUILÁTERO.')
    elif x != y and y != z and x != z:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima \033[1:31mNÂO PODEM\033[m formar um triângulo.')
