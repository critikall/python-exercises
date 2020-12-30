# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
rad = radians(angulo)
s = sin(rad)
c = cos(rad)
t = tan(rad)

print(
    f"O ângulo de {angulo} tem o SENO de {s:.2f} \nO ângulo de {angulo} tem o COSSENO de {c:.2f} \nO ângulo de {angulo}"
    f" tem a TANGENTE de {t:.2f}")
