# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('10 TERMOS DE UMA PA\n')

primero_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0

while contador < 10:
    print(f'{primero_termo}', end=' ➝ ')
    primero_termo += razao
    contador += 1
print('Fim')
