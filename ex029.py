# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 para cada Km acima do limite.

vel = int(input('Velocidade atual? '))
multa = (vel - 80) * 7

if vel > 80:
    print(f'Você foi MULTADO. O limite máximo é 80 Km/h e você está a {vel} Km/h. O valor da sua multa é de'
          f' R${multa :.2f}')
else:
    print('Você está dentro do limite de velocidade.')
