# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No
# final mostre o maior e o menor valor digitado e as suas respectivas
# posições na lista.

nums = []
for cont in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'\nVocê digitou os valores: {nums}')

max_nums = []
for p, n in enumerate(nums):
    if n == max(nums):
        max_nums.append(p)
print(f'\nO maior valor digitado foi {max(nums)} na posições {max_nums}')

min_nums = []
for p, n in enumerate(nums):
    if n == min(nums):
        min_nums.append(p)
print(f'\nO menor valor digitado foi {min(nums)} nas posições {min_nums}')
