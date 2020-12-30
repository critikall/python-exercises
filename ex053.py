# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

# Obs: Frase que pode-se ler de frente pra trás ou de trás pra frente que o resultado é o mesmo.
# Exemplo: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
pali = ''
for c in frase:
    pali = c + pali
if frase == pali:
    print(f'{frase} = {pali} \nÉ um palíndromo.')
else:
    print(f'{frase} ≠ {pali} \nNão é um palíndromo.')
