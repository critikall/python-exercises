# Aprimore o desafio anterior, mostrando no final:

# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_terceira_coluna = soma_pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()

for n in matriz:
    soma_terceira_coluna += n[2]

print(f'''
A soma dos valores pares: {soma_pares}
A soma dos valores da terceira coluna: {soma_terceira_coluna}
O Maior valor da segunda linha: {max(matriz[1])}''')
