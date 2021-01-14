# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu Programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            print(f'Você digitou o número {numeros[n]}.')
            break
        print('Tente novamente.', end=' ')

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar == 's' or continuar == 'n':
            break
    if continuar == 'n':
        break
