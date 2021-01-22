# Crie um programa que leia nome, ano de nascimento, e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso o CTPS for
# diferente de ZERO, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import datetime

ficha = {"nome": str(input('Nome: ')).strip().capitalize()}
ano_nasc = int(input('Ano de Nascimento: '))
ficha["idade"] = datetime.now().year - ano_nasc
ficha["ctps"] = int(input('Carteira de Trabalho (0 não tem): '))

if ficha["ctps"] != 0:
    ficha["contratação"] = int(input('Ano de contratação: '))
    ficha["salário"] = float(input('Salário: R$ '))
    ficha["aposentadoria"] = (ficha["contratação"] + 35) - datetime.now(
    ).year + ficha["idade"]

print('-=-' * 10)

for k, v in ficha.items():
    print(f'{k.capitalize()} tem o valor {v}')
