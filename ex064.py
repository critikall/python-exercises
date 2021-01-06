# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag 999).

num = soma = contador = 0

while num != 999:
    num = int(input('Digite um número [ ou 999 para finalizar a sessão]: '))
    if num != 999:
        soma += num
        contador += 1
print(f'\nVocê digitou {contador} número(s) e a soma entre eles foi {soma}.')
