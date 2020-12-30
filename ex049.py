# Refaça o exercício 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número inteiro para ver sua tabuada: '))
for mult in range(1, 11):
    print(f'{num} x {mult :2} = {num * mult}')
