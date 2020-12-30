# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

print('10 TERMOS DE UMA PA')
a = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pa = a + (10 - 1) * r  # 10 = Décimo Termo
for c in range(a, pa + r, r):
    print(f'{c}', end=' ➝ ')
print('Fim')
