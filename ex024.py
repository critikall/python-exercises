# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('Digite o nome da cidade: ')).strip().upper().split()
print(f'Começa com Santo?', cid[0] == 'SANTO')
