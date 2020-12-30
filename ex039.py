# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = str(input('Digite M para masculino ou F para feminino: ')).strip().upper()

if sexo == 'F':
    print('Alistamento militar não obrigatório.')
else:
    ano = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    x = idade - 18
    print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')

    if idade < 18:
        print(f'Ainda falta(m) {abs(x)} ano(s) para o alistamento. \nSeu alistamento será em {abs(atual - x)}.')
    elif idade > 18:
        print(f'Você ja deveria ter se alistado há {idade - 18} ano(s). \nSeu alistamento foi em {abs(x - atual)}.')
    else:
        print('Se aliste imediadamente!')
