# Escreva um programa que leia um valor em metros e o exiba convertido em centímentros e milímetros.

medida = float(input('Digite um valor em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m equivale a: \n{km :.1f} km \n{hm :.0f} hm \n{dam :.0f} dam \n{dm :.0f} dm \n{cm :.0f} cm '
      f'\n{mm :.0f} mm')
