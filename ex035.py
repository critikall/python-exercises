# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro segmento: '))

if (y + z) > x and (x + z) > y and (x + y) > z:
    print('Os segmentos acima PODEM formar um triângulo.')

else:
    print('Os segmentos acima NÂO PODEM formar um triângulo.')
