# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângumo.#

import math
ang = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {:.2f}° possui:\nseno de {:.2f}\ncosseno de {:.2f}\ntangente de {:.2f}.'.format(ang, sen, cos, tan))

# Para a resolução deste exercício é necessário transformar primeiro o ãngulo em radiano para jogar na fórmula.#

from math import radians, sin, cos, tan
ang = float(input('Digite o valor de um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {:.2f}° possui seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}.'.format(ang, sen, cos, tan))
