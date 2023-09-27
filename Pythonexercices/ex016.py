# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 - O número 6.127 tem a parte inteira 6.#

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, math.floor(num)))

from math import floor
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, floor(num)))

# Esse exercício pode ser feito tb usando o trunc no lugar do floor ou não importar nada de math e usar o int no lugar do floor.#

num = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}.'.format(num, int(num)))
