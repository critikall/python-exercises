# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M] para masculino ou [F] para feminino: ')).strip().upper()
    print('Inválido, tente novamente.\n')
print(f'Sexo {sexo} confirmado.')
