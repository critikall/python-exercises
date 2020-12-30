# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n  # s = s + n (acumulador)
        c += 1  # c = c + 1 (contador)
print(f'A soma dos valores é {s} e um total de {c} números foram somados.')
