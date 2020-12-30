# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas ja são maiores.
# Obs: Maioridade = 21 anos

from datetime import date
atual = date.today().year
maior = 0  # Contador
menor = 0  # Contador
for pessoa in range(1, 8):
    nas = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nas
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'''\nTotal de {maior} pessoa(s) maior(es) de idade.
Total de {menor} pessoa(s) menor(es) de idade.''')
