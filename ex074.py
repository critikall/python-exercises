# Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# tupla. Depois disso, mostre a listagem de numeros gerados e também indique
# o menor e o maior valor que estão na tupla.

from random import randint

nums = tuple(randint(1, 10) for i in range(0, 5))
print(f'Os valores sorteados foram: ', end='')
for n in nums:
    print(n, end=' ')

print(f'''\nO maior valor sorteado foi {max(nums)}
O menor valor sorteado foi {min(nums)}''')
