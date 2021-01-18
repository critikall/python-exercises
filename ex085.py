# Crie um programa onde o usuário possa digitar sete valores númericos e
# cadastre-os em uma listagem única que mantenha separados os valores pares
# e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()

print(f'''
Valores pares: {valores[0]}
Valores ímpares: {valores[1]}''')
