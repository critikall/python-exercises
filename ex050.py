# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

s = 0
c = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        s += num
        c += 1
print(f'A soma dos números pares é {s} e um total de {c} números pares foram digitados.')
