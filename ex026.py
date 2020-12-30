# Faça um programa que leia uma frase pelo teclado e mostre:
frase = str(input('Digite uma frase: ')).strip().upper()

# Quantas vezes aparece a letra "A"
print(f'A letra A apareceu {frase.count("A")} vezes')

# Em que posição ela aparece a primeira vez
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')

# Em que posição ela aparece a última vez
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
