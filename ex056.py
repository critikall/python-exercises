# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

somaIdades = 0
maiorIdadeHomem = 0
nomeHomemVelho = ''
mulher20 = 0
for pessoa in range(1, 5):
    print(f'===== {pessoa}ª PESSOA =====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    somaIdades += idade
    if pessoa == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
media = somaIdades / 4
print(f'''\nA média de idade do grupo é de {media :.1f} anos.
O Homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeHomemVelho}.
Total de {mulher20} mulher(es) com menos de 20 anos.''')
