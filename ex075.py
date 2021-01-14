# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre:

# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

nums = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))

print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O valor 3 apareceu na {nums.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares são:', end=' ')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
