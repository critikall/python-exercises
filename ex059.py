# Crie um programa que leia dois valores e mostre na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
menu = 0

while menu != 5:
    print("=" * 30, '''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    menu = int(input('\n>>>>>Opção selecionada: '))
    if menu == 1:
        print(f'\nA soma entre {n1} + {n2} = {n1 + n2}')
    elif menu == 2:
        print(f'\nA multiplicação entre {n1} x {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'\nEntre {n1} e {n2} o maior valor é {n1}')
        else:
            print(f'\nEntre {n1} e {n2} o maior valor é {n2}')
    elif menu == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo Valor: '))
    elif menu > 5:
        print('Opção inválida.')

print('\nSessão finalizada.')
