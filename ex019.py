# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

a1 = input('Qual o nome do primeiro aluno(a)? ')
a2 = input('Qual o nome do segundo aluno(a)? ')
a3 = input('Qual o nome do terceiro aluno(a)? ')
a4 = input('Qual o nome do quarto aluno(a)? ')
lista = [a1, a2, a3, a4]
x = choice(lista)

print(f'A pessoa sorteada para apagar o quadro é {x}.')
