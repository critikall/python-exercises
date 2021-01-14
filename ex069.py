# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final mostre:

# a) Quantas pessoas tem mais de 18 anos.
# b) Quantos homens foram cadastrados.
# c) Quantas mulheres tem menos de 20 anos.

maior_18 = 0
contador_homens = 0
mulheres_menos_20 = 0

while True:
    print('=' * 25)
    print('CADASTRO DE PESSOAS'.center(25))
    print('=' * 25)
    idade = int(input('Idade: '))
    if idade > 18:
        maior_18 += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if sexo == 'm' or sexo == 'f':
            if sexo == 'm':
                contador_homens += 1
            elif idade < 20 and sexo == 'f':
                mulheres_menos_20 += 1
            break
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar == 's' or continuar == 'n':
            break
    if continuar == 'n':
        break

print('\n===== CADASTRO FINALIZADO ====='.center(25))
print(f'''Pessoas com mais de 18 anos: {maior_18}
Total de homens: {contador_homens}
Mulheres com menos de 20 anos: {mulheres_menos_20}''')
