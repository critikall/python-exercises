# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quantos reais você quer converter? R$'))
dolar = 5.10 #Cotação dolar 19/12/2020
euro = 6.25 #Cotação euro 19/12/2020
libra = 6.90 #Cotação libra 19/12/2020
iene = 0.049 #Cotação iene 19/12/2020
bitcoin = 122136.85 #Cotação bitcoin 19/12/2020
print(f'Com R${real :.2f} você pode comprar US${real/dolar :.2f}')
print(f'Com R${real :.2f} você pode comprar {real/euro :.2f}€')
print(f'Com R${real :.2f} você pode comprar £{real/libra :.2f}')
print(f'Com R${real :.2f} você pode comprar ¥{real/iene :.2f}')
print(f'com R${real :.2f} você pode comprar ฿{real/bitcoin :.4f}')
