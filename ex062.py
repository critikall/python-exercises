# Melhore o DEAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

print('10 TERMOS DE UMA PA\n')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = 0
termos_mais = 0
menu = False
condicao = 0
contagem = 10

while termo < 10:
    print(f'{primeiro_termo}', end=' ➝ ')
    primeiro_termo += razao
    termo += 1
print('Pausa')

while not menu:
    termos_mais = int(input('\nQuantos termos a mais quer mostrar? '))
    contagem += termos_mais
    if termos_mais == 0:
        menu = True
    else:
        while condicao < termos_mais:
            print(f'{primeiro_termo}', end=' ➝ ')
            primeiro_termo += razao
            condicao += 1
        print('Pausa')
        condicao = 0

print(f'\nProgressão finalizada com {contagem} termos.')
