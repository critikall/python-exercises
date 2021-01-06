# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

contagem = 0
soma = 0
lista_nums = []
condicao = False

while not condicao:
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar [S/N]? ')).strip().upper()
    contagem += 1
    soma += n
    lista_nums += [n]
    if continuar == 'N':
        condicao = True
    else:
        while continuar not in "SN":
            continuar = str(input('Opção inválida. Quer continuar [S/N]? ')).strip().upper()
            if continuar == 'N':
                condicao = True
print(f'''\nForam digitados {contagem} números e a média foi de {soma / contagem :.2f}
O menor valor foi {min(lista_nums)} e o maior valor foi {max(lista_nums)}.''')
