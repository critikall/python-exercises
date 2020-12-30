# Crie um programa que leia duas notas de um aluno calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota : '))
media = (nota1 + nota2) / 2

print(f'Sua média foi de {media :.1f}', end=' ')

if media < 5:
    print('\033[1:31mREPROVADO\033[m!')
elif media >= 7:
    print('\033[1:34mAPROVADO\033[m!')
else:
    print('\033[1:33mRECUPERAÇÃO\033[m!')
