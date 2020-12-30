# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('Primeiro aluno(a): ')
a2 = input('Segundo aluno(a): ')
a3 = input('Terceiro aluno(a): ')
a4 = input('Quarto aluno(a): ')
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação será: \n{lista}')
